import logging

from pprint import pprint
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.loops import from_array


from qm_saas.client import QoPSaaS, QoPSaaSInstance, QoPVersion

import matplotlib.pyplot as plt
import numpy as np

# pulse function for config
def raise_cosine(t,T):
    return 0.5*(1-np.cos(2*np.pi*t/T))
"""
def rasie_cosine_puilse(duration:int):
    #t_edge = int(duration/10)
    t_edge = int(duration/10)
    t_edge = 20
    t =  np.arange(0,t_edge+1,1) # ns in unit
    raise_down_part = raise_cosine(t,t_edge)
    flat = np.ones(duration-t_edge)
    square = np.concatenate((raise_down_part[0:len(raise_down_part)//2],flat,raise_down_part[len(raise_down_part)//2+1:]),axis=0)
    return square
"""

# pulse function for program
def cosine_square_sticky_pulse(amplitude_scale, duration, element):
    play("raise_up"*amp(amplitude_scale), element)
    wait(duration, element)
    play("cosine_down_sitcky"*amp(amplitude_scale), element)

def cosine_square_pulse(amplitude_scale, duration, element):
    play("raise_up"*amp(amplitude_scale), element)
    play("const"*amp(amplitude_scale), element)
    #set_dc_offset(element=element,element_input ='single',offset =0.2)
    
    play("raise_down"*amp(amplitude_scale), element)

t_edge = 48
t =  np.arange(0,t_edge+1,1) # ns in unit
raise_down_part = raise_cosine(t,t_edge)

square_len = 100
# Define the quantum machine configuration in a dictionary
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": +0.0},
                2: {"offset": +0.0,"delay":0},
                3: {"offset": +0.0,"delay":0}
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
        "z1":{
            "singleInput": {"port": ("con1", 2)},
            "operations": {
                "raise_up": "cosine_up_pulse",
                "raise_down": "cosine_down_pulse",
                "cosine_down_sitcky": "cosine_down_sitcky_pulse",
                "const":"constPulse"
            },
            "sticky": {
                "analog":True,
                "digital":False,
                "duration": 4}
        },
        "z2":{
            "singleInput": {"port": ("con1", 3)},
            "operations": {
                "raise_up": "cosine_up_pulse",
                "raise_down": "cosine_down_pulse",
                "const":"constPulse"
            }
        }
    },
    "pulses": {
        "constPulse": {
            "operation": "control",
            "length": square_len,  # in ns
            "waveforms": {"single": "const_wf"},
        },
        "cosine_up_pulse": {
            "operation": "control",
            "length": t_edge//2,  # in ns
            "waveforms": {"single": "cosine_up"},
        },        
        "cosine_down_pulse": {
            "operation": "control",
            "length": t_edge//2,  # in ns
            "waveforms": {"single": "cosine_down"},
        },
        "cosine_down_sitcky_pulse": {
            "operation": "control",
            "length": t_edge//2,  # in ns
            "waveforms": {"single": "cosine_down_sitcky"},
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "cosine_up": {"type": "arbitrary", "samples": 0.2*raise_down_part[0:len(raise_down_part)//2]},
        "cosine_down_sitcky": {"type": "arbitrary", "samples": 0.2*(raise_down_part[len(raise_down_part)//2+1:]-1)},
        "cosine_down": {"type": "arbitrary", "samples": 0.2*raise_down_part[len(raise_down_part)//2+1:]},

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
qop_saas = client.simulator(QoPVersion.v2_2_2)

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
    try:
        # The following line will raise an exception if the simulator was not spawned.
        print(instance.qm_manager_parameters)
        #instance.version = "bad_version"
        #instance.spawn()
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

    t_min = 16 // 4
    t_max = 2000 // 4
    dt = 4 // 4
    durations = np.arange(t_min, t_max, dt)

    with program() as prog:
        t = declare(int) 
        n = declare(int)
        with for_(*from_array(t, durations)):
            cosine_square_pulse(amplitude_scale=1,
                                duration=t,
                                element="z2")
            
    qm = qmm.open_qm(config)
    job = qm.simulate(prog, SimulationConfig(int(1000)))  # in clock cycles, 4 ns
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
