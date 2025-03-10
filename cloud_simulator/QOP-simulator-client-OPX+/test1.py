from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

from qm_saas.client import QoPSaaS, QoPVersion


# Define quantum machine configuration dictionary
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": +0.0},
            },
        }
    },
    "elements": {
        "qe1": {
            "singleInput": {"port": ("con1", 1)},
            "intermediate_frequency": 5e6,
            "operations": {
                "playOp": "constPulse",
            },
        },
    },
    "pulses": {
        "constPulse": {
            "operation": "control",
            "length": 1000,  # in ns
            "waveforms": {"single": "const_wf"},
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
    },
}

# ======================================================================================================================
# Name: test1.py
# Description: This example will use the most minimal configuration possible to launch a simulator instance.
# The usage of a context manager ensures that the instance is properly closed.
# ======================================================================================================================

# These should be changed to your credentials.
email = "chao.jack@quantum-machines.co"
password = "wLr1Qy7J3mT5"
host = "qm-saas.dev.quantum-machines.co"

# Initialize QOP simulator client
client = QoPSaaS(email=email,
                 password=password,
                 host = host)


with client.simulator(QoPVersion.v2_2_2) as instance:  # Specify the QOP version

    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(host=instance.sim_host,
                                 port=instance.sim_port,
                                 connection_headers=instance.default_connection_headers)

    # Define a QUA program
    with program() as prog:
        play("playOp", "qe1")

    # Open quantum machine with the provided configuration and simulate the QUA program
    qm = qmm.open_qm(config)
    job = qm.simulate(prog, SimulationConfig(int(1000)))

    # Retrieve and handle simulated samples
    samples = job.get_simulated_samples()
    print('Test passed')
