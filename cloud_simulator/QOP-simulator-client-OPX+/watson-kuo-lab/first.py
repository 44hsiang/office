import logging

from pprint import pprint
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.loops import from_array


from qm_saas.client import QoPSaaS, QoPSaaSInstance, QoPVersion

import matplotlib.pyplot as plt
import numpy as np

# IQ imbalance matrix
def IQ_imbalance(g, phi):
    """
    Creates the correction matrix for the mixer imbalance caused by the gain and phase imbalances, more information can
    be seen here:
    https://docs.qualang.io/libs/examples/mixer-calibration/#non-ideal-mixer
    :param g: relative gain imbalance between the 'I' & 'Q' ports. (unit-less), set to 0 for no gain imbalance.
    :param phi: relative phase imbalance between the 'I' & 'Q' ports (radians), set to 0 for no phase imbalance.
    """
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]

mixer_qubit_g = 0.0
mixer_qubit_phi = 0.0
mixer_resonator_g = 0.0
mixer_resonator_phi = 0.0

resonator_LO = 5e9
resonator_IF = 50e6
readout_amp = 0.2
qubit_LO = 4e9
qubit_IF = 50e6
time_of_flight = 324
readout_len = 1000
sideband_len = 500
const_len = 500
# Define the quantum machine configuration in a dictionary
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": +0.0}, # readout I
                2: {"offset": +0.0,}, # readout Q
                3: {"offset": +0.0,},  # xy I
                4: {"offset": +0.0,},   # xy Q
                5: {"offset": +0.0,},  # z 
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        }
    },
    "elements": {
        "rr1": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "mixer_resonator",
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "xy1":{
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
            },
        },
        "z1":{
            "singleInput": {"port": ("con1", 5)},
            "operations": {
                "const": "const_flux_pulse",
                "sideband": "sideband_pulse",
            },
            "intermediate_frequency": 5e6,

        }
    },
    "pulses": {
        "const_flux_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,  # in ns
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights"
            },
            "digital_marker": "ON",
        },   
        "sideband_pulse": {
            "operation": "control",
            "length": sideband_len,  # in ns
            "waveforms": {"single": "const_wf"},
        },
        
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
    },
    "mixers": {
        "mixer_qubit": [
            {
                "intermediate_frequency": qubit_IF,
                "lo_frequency": qubit_LO,
                "correction": IQ_imbalance(mixer_qubit_g, mixer_qubit_phi),
            }
        ],
        "mixer_resonator": [
            {
                "intermediate_frequency": resonator_IF,
                "lo_frequency": resonator_LO,
                "correction": IQ_imbalance(mixer_resonator_g, mixer_resonator_phi),
            }
        ],
    },
}

# ======================================================================================================================
# Name: test2.py
# Description: This example explains different usage scenarios in the inline comments.
# Most notably it does not use the context manager, so you need to make sure you close the instance yourself.
# ======================================================================================================================

# These are static and should usually not be changed.
saas_port = 9000
saas_host = "qm-saas.dev.quantum-machines.co"

# These should be changed to your credentials.
email = "chao.jack@quantum-machines.co"
password = "wLr1Qy7J3mT5"

# This will configure logging to requested level.
log = logging.getLogger('qop_saas_simulator')
log.setLevel(logging.DEBUG)

# Initialize the QoPSaaS client
client = QoPSaaS(host=saas_host,
                 port=saas_port,
                 email=email,
                 password=password,
                 log=log)

# Create a simulator instance with a specific QOP version.
qop_saas = client.simulator(QoPVersion.v2_4_0)

# We can serialize the simulator object to a dict
# This allows to spawn simulations with the credentials of the user that spawned the simulator.
# Be careful not to make the values publicly available: they contain sensitive information.
json = qop_saas.to_dict()
pprint(json)
#del qop_saas

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

    print('Testing host: ', host)
    print('Testing port: ', port)
    print('Testing auth: ', auth)

    qmm = QuantumMachinesManager(host=host,
                                 port=port,
                                 connection_headers=headers)

    t_min = 500 // 4
    t_max = 2000 // 4
    dt = 100 // 4
    durations = np.arange(t_min, t_max, dt)
    amplitude = np.arange(0.05,0.5,0.2)
    frequency = np.arange(5e6,30e6,5e6)

    with program() as prog:
        t = declare(int) 
        n = declare(int)
        a = declare(fixed)
        f = declare(int)
        I = declare(fixed)  
        Q = declare(fixed)
        I_st = declare_stream()  # Stream for the 'I' quadrature
        Q_st = declare_stream()
         
        with for_(n, 0, n < 10, n + 1):

            with for_(*from_array(f,frequency)):
                update_frequency('z1',f)
                with for_(*from_array(a,amplitude)):
                    set_dc_offset('z1','single',0.1)
                    play("sideband"*amp(a), "z1")

                    play("const", "xy1")
                    set_dc_offset('z1','single',0.0)
                    align('z1','xy1')
                    measure(
                        "readout",
                        "rr1",
                        None,
                        dual_demod.full("cos", "out1", "sin","out2", I),
                        dual_demod.full("minus_sin","out1", "cos","out2", Q),
                    )
                    save(I, I_st)
                    save(Q, Q_st)
                    wait(250)

    qm = qmm.open_qm(config)
    job = qm.simulate(prog, SimulationConfig(int(5000)))  # in clock cycles, 4 ns
    samples = job.get_simulated_samples()
    wf_report = job.get_simulated_waveform_report()
    # todo: make save_path use node's storage location
    wf_report.create_plot(samples, plot=True)
    print('Test passed')
finally:
    # After the test, we can deallocate the instance. If we don't do it,
    # the instance will be deallocated by the server after 15 minutes.
    # Keep in mind that the current limit of simulator instances per user is 3.
    # Closing the instance will free the allocated slot from your limit.
    instance.close()
