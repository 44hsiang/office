from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qm_saas.client import QoPSaaS, QoPVersion

# Define quantum machine configuration dictionary
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
# Name: example1.py
# Description: Use default host and port for the QOP simulator. Email and password are mandatory.
#              Using the context manager ensures them simulator instance is closed properly.
# ======================================================================================================================

# These should be changed to your credentials.
email = "email"
password = "password"

# Initialize QOP simulator client
client = QoPSaaS(email=email, password=password)


with client.simulator(QoPVersion.v3_1_0) as instance:  # Specify the QOP version
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.sim_host, port=instance.sim_port, connection_headers=instance.default_connection_headers
    )

    # Define a QUA program
    with program() as prog:
        play("const", "qe_LF")

    # Open quantum machine with the provided configuration and simulate the QUA program
    qm = qmm.open_qm(config)
    job = qm.simulate(prog, SimulationConfig(int(1000)))

    # Retrieve and plot simulated samples
    samples = job.get_simulated_samples().con1.plot()
    print("Test passed")

