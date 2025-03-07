import logging
from pprint import pprint
from qm import QuantumMachinesManager
from qm.qua import play, program
from qm import SimulationConfig
from qm_saas.client import QoPSaaS, QoPSaaSInstance, QoPVersion

# Define the quantum machine configuration in a dictionary
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",#1-4 are LF FEMs, 5-8 are MW FEMs
            "fems":{
                1 :{
                "type": "LF",
                "analog_outputs": {
                    1: {
                        "offset": 0.0,
                        "output_mode": "direct",
                        "sampling_rate": 1e9,
                        "upsampling_mode": "pulse", # Default is 'mw'
                    },
                    2: {
                        "offset": 0.0,
                        "output_mode": "direct",
                        "sampling_rate": 1e9,
                        "upsampling_mode": "pulse", # Default is 'mw'
                    },
                },
                "digital_outputs": {
                    1: {}
                },
                "analog_inputs": {
                    1: {
                        "offset": 0.0,
                        "sampling_rate": 1e9, # Default sampling rate is 1e9
                        "gain_db": 0
                        },
                    2: {
                        "offset": 0.0,
                        "sampling_rate": 1e9,  # Default sampling rate is 1e9
                        "gain_db": 0
                        },
                    },
                },
                5 :{
                'type': 'MW',
                'analog_outputs': {
                    1: {
                        'band': 2,
                        'full_scale_power_dbm': 10,  # Default is -10
                        },
                    },
                'digital_outputs': {
                    },
                'analog_inputs': {
                    1: {
                        'sampling_rate': 2e9,  # Default sampling rate is 1e9
                        'band': 2,
                        },
                    }
                },
            },
        },
    },
    "elements": {
        "qe_LF": {
            "mixInputs": {
                "I": ("con1", 1, 1),
                "Q": ("con1", 1, 2),
                "lo_frequency": 6e9,
                "mixer": "mixer_qe_LF",
            },
            "intermediate_frequency": 100e6,
            "operations": {
                "const": "const_pulse",
            },
        },
        "qe_MW": {
            "MWInput": {
                "port": ("con1", 5, 1),
                "oscillator_frequency": 5e9,
                },
            "intermediate_frequency": 100e6,
            "operations": {
                "const": "const_pulse",
            },
            "MWOutput": {
                "port": ("con1", 5, 1),
                "oscillator_frequency": 5e9,
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "mixers": {
        "mixer_qe_LF": [
            {
                "intermediate_frequency": 100e6,
                "lo_frequency": 6e9,
                "correction": [1, 0, 0, 1],
            }
        ],
    },
}

# ======================================================================================================================
# Name: example2.py
# Description: If needed you can overwrite the default connection parameters.
#              Not using the context manager is also possible.
# ======================================================================================================================

# These are static and should usually not be changed.
saas_port = 9000
saas_host = "simulator.qopsim.prod.quantum-machines.co"

# These should be changed to your credentials.
email = "email"
password = "password"

# This will configure logging to requested level.
log = logging.getLogger("qop_saas_simulator")
log.setLevel(logging.DEBUG)

# Initialize the QoPSaaS client
client = QoPSaaS(host=saas_host, port=saas_port, email=email, password=password, log=log)

# Create a simulator instance with a specific QOP version.
qop_saas = client.simulator(QoPVersion.v3_1_0)

# We can serialize the simulator object to a dict
# This allows to spawn simulations with the credentials of the user that spawned the simulator.
# Be careful not to make the values publicly available: they contain sensitive information.
json = qop_saas.to_dict()
pprint(json)
del qop_saas

# we can send the QoPSaaSInstance over the network
# and reconstruct it on another machine.
# If the instance has been spawned, we have 15 minutes before it expires.
instance = QoPSaaSInstance.from_dict(**json)

try:
    # The attributes of the instance are open, but we don't recommend changing them.
    # Attempting an operation that may fail due to incorrect instance version.
    try:
        instance.version = "bad_version"
        instance.spawn()
    except ValueError as e:
        # The server double-checks the version and other attributes of the instance.
        # Expected answers are:
        # HTTP 400: Invalid QoP version (currently supported versions will be listed in the response).
        print(e)
        # Restore the correct data
        instance = QoPSaaSInstance.from_dict(**json)

    try:
        # The following line will raise an exception if the simulator was not spawned.
        print(instance.qm_manager_parameters)
    except ValueError as e:
        print(e)  # Simulator was not spawned
        # if we want to spawn it, just can do it this way:
        instance.spawn()
        # Now the instance has actually the parameters of the simulator and its internal token
        pprint(instance.to_dict())

    # The spawned simulator will be reachable through the provided information:
    host = instance.sim_host
    port = instance.sim_port
    auth = instance.sim_token
    headers = instance.default_connection_headers

    print("Testing host: ", host)
    print("Testing port: ", port)
    print("Testing auth: ", auth)

    qmm = QuantumMachinesManager(host=host, port=port, connection_headers=headers)

    with program() as prog:
        play("const", "qe_LF")

    qm = qmm.open_qm(config)
    job = qm.simulate(prog, SimulationConfig(int(1000)))  # in clock cycles, 4 ns
    # Retrieve and plot simulated samples
    samples = job.get_simulated_samples().con1.plot()

    print("Test passed")
finally:
    # After the test, we can deallocate the instance. If we don't do it,
    # the instance will be deallocated by the server after 15 minutes.
    # Keep in mind that the current limit of simulator instances per user is 3.
    # Closing the instance will free the allocated slot from your limit.
    instance.close()
