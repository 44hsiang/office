
# Single QUA script generated at 2025-02-27 13:19:28.177274
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(int, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    v11 = declare(fixed, )
    v12 = declare(fixed, )
    v13 = declare(bool, )
    v14 = declare(int, value=1)
    v15 = declare(fixed, )
    v16 = declare(fixed, )
    v17 = declare(bool, )
    v18 = declare(int, value=1)
    v19 = declare(fixed, )
    v20 = declare(fixed, )
    v21 = declare(bool, )
    v22 = declare(int, value=1)
    v23 = declare(fixed, )
    v24 = declare(fixed, )
    v25 = declare(bool, )
    v26 = declare(int, value=1)
    set_dc_offset("q0.z", "single", 0.05805230379096408)
    set_dc_offset("q1.z", "single", 0.07139578755228651)
    set_dc_offset("q2.z", "single", 0.07931339159421318)
    set_dc_offset("q3.z", "single", 0.05163964909558919)
    set_dc_offset("q4.z", "single", 0.06671223897937127)
    wait(1000, "q0.z")
    align("q0.xy", "q0.resonator", "q0.z")
    with for_(v1,0,(v1<5000),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        assign(v14, 1)
        align("q0.xy", "q0.resonator", "q0.z")
        measure("readout", "q0.resonator", None, dual_demod.full("iw1", "iw2", v11), dual_demod.full("iw3", "iw1", v12))
        assign(v13, (v11>4.916990328692865e-05))
        wait(250, "q0.resonator")
        align("q0.xy", "q0.resonator", "q0.z")
        play("x180", "q0.xy", condition=v13)
        align("q0.xy", "q0.resonator", "q0.z")
        with while_(((v11>-0.000636935560997132)&(v14<15))):
            align("q0.resonator", "q0.xy")
            measure("readout", "q0.resonator", None, dual_demod.full("iw1", "iw2", v11), dual_demod.full("iw3", "iw1", v12))
            assign(v13, (v11>4.916990328692865e-05))
            wait(250, "q0.resonator")
            align("q0.resonator", "q0.xy", "q0.z")
            play("x180", "q0.xy", condition=v13)
            align("q0.resonator", "q0.xy")
            assign(v14, (v14+1))
        wait(4, "q0.xy")
        align("q0.xy", "q0.resonator", "q0.z")
        assign(v18, 1)
        align("q0.xy", "q0.resonator", "q0.z")
        measure("readout", "q0.resonator", None, dual_demod.full("iw1", "iw2", v15), dual_demod.full("iw3", "iw1", v16))
        assign(v17, (v15>4.916990328692865e-05))
        wait(250, "q0.resonator")
        align("q0.xy", "q0.resonator", "q0.z")
        play("x180", "q0.xy", condition=v17)
        align("q0.xy", "q0.resonator", "q0.z")
        with while_(((v15>-0.000636935560997132)&(v18<15))):
            align("q0.resonator", "q0.xy")
            measure("readout", "q0.resonator", None, dual_demod.full("iw1", "iw2", v15), dual_demod.full("iw3", "iw1", v16))
            assign(v17, (v15>4.916990328692865e-05))
            wait(250, "q0.resonator")
            align("q0.resonator", "q0.xy", "q0.z")
            play("x180", "q0.xy", condition=v17)
            align("q0.resonator", "q0.xy")
            assign(v18, (v18+1))
        wait(4, "q0.xy")
        align("q0.xy", "q0.resonator", "q0.z")
    set_dc_offset("q0.z", "single", 0.05805230379096408)
    set_dc_offset("q1.z", "single", 0.07139578755228651)
    set_dc_offset("q2.z", "single", 0.07931339159421318)
    set_dc_offset("q3.z", "single", 0.05163964909558919)
    set_dc_offset("q4.z", "single", 0.06671223897937127)
    wait(1000, "q1.z")
    align("q1.xy", "q1.resonator", "q1.z")
    with for_(v1,0,(v1<5000),(v1+1)):
        save(v1, r1)
        assign(v22, 1)
        align("q1.xy", "q1.resonator", "q1.z")
        measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v19), dual_demod.full("iw3", "iw1", v20))
        assign(v21, (v19>0.0005793615114838012))
        wait(250, "q1.resonator")
        align("q1.xy", "q1.resonator", "q1.z")
        play("x180", "q1.xy", condition=v21)
        align("q1.xy", "q1.resonator", "q1.z")
        with while_(((v19>0.001528130590613003)&(v22<15))):
            align("q1.resonator", "q1.xy")
            measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v19), dual_demod.full("iw3", "iw1", v20))
            assign(v21, (v19>0.0005793615114838012))
            wait(250, "q1.resonator")
            align("q1.resonator", "q1.xy", "q1.z")
            play("x180", "q1.xy", condition=v21)
            align("q1.resonator", "q1.xy")
            assign(v22, (v22+1))
        wait(4, "q1.xy")
        align("q1.xy", "q1.resonator", "q1.z")
        assign(v26, 1)
        align("q1.xy", "q1.resonator", "q1.z")
        measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v23), dual_demod.full("iw3", "iw1", v24))
        assign(v25, (v23>0.0005793615114838012))
        wait(250, "q1.resonator")
        align("q1.xy", "q1.resonator", "q1.z")
        play("x180", "q1.xy", condition=v25)
        align("q1.xy", "q1.resonator", "q1.z")
        with while_(((v23>0.001528130590613003)&(v26<15))):
            align("q1.resonator", "q1.xy")
            measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v23), dual_demod.full("iw3", "iw1", v24))
            assign(v25, (v23>0.0005793615114838012))
            wait(250, "q1.resonator")
            align("q1.resonator", "q1.xy", "q1.z")
            play("x180", "q1.xy", condition=v25)
            align("q1.resonator", "q1.xy")
            assign(v26, (v26+1))
        wait(4, "q1.xy")
        align("q1.xy", "q1.resonator", "q1.z")
    with stream_processing():
        r1.save("n")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "delay": 174,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 172,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "3": {
                            "delay": 174,
                            "shareable": False,
                            "filter": {
                                "feedforward": [0.930566753281534, -1.99, 1.5555096131158408, -0.5663963111589002, 0.025217290417050606, 0.06075559088850318, 0.03375358974167169, -0.07057910169815002, 0.034284390746336005, 0.0020385711162261132, 0.003614667597226243, -0.034421462769617994, 0.022513274875880437, 0.04552318000189783, -0.06044323534122823, 0.01960355211152274, -0.025801154962076748, 0.020784734817433544, 0.02640072988181348, -0.04036221849512527, 0.0430548424440775, -0.04112524269212112, -0.012927313928236006, 0.06353596748352627, -0.053949828249563535, 0.014346142950503217, 0.04516400193430306, -0.08431492230979887, 0.055842531915586587, -0.01282744479378403],
                                "feedback": [0.9556355411471746, 0.5045807850848327],
                            },
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 175,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "5": {
                            "delay": 170,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                    },
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -8,
                            "upconverter_frequency": 7550000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4560000000.0,
                        },
                        "3": {
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4710000000.0,
                        },
                        "4": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4980000000.0,
                        },
                        "5": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 5690000000.0,
                        },
                        "6": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 5660000000.0,
                        },
                        "7": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 6000000000.0,
                        },
                        "8": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 6125000000.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "downconverter_frequency": 7550000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q0.xy": {
            "operations": {
                "x180_DragCosine": "q0.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q0.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q0.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q0.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q0.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q0.xy.-y90_DragCosine.pulse",
                "x180_Square": "q0.xy.x180_Square.pulse",
                "x90_Square": "q0.xy.x90_Square.pulse",
                "-x90_Square": "q0.xy.-x90_Square.pulse",
                "y180_Square": "q0.xy.y180_Square.pulse",
                "y90_Square": "q0.xy.y90_Square.pulse",
                "-y90_Square": "q0.xy.-y90_Square.pulse",
                "x180": "q0.xy.x180_DragCosine.pulse",
                "x90": "q0.xy.x90_DragCosine.pulse",
                "-x90": "q0.xy.-x90_DragCosine.pulse",
                "y180": "q0.xy.y180_DragCosine.pulse",
                "y90": "q0.xy.y90_DragCosine.pulse",
                "-y90": "q0.xy.-y90_DragCosine.pulse",
                "saturation": "q0.xy.saturation.pulse",
                "EF_x180": "q0.xy.EF_x180.pulse",
            },
            "intermediate_frequency": -34697346.90529516,
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
        },
        "q0.z": {
            "operations": {
                "const": "q0.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 1),
            },
        },
        "q0.resonator": {
            "operations": {
                "readout": "q0.resonator.readout.pulse",
                "const": "q0.resonator.const.pulse",
            },
            "intermediate_frequency": -301969911.0,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q1.xy": {
            "operations": {
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
                "EF_x180": "q1.xy.EF_x180.pulse",
            },
            "intermediate_frequency": -38385086.07454129,
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 2),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -174879836.0,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q2.xy": {
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
                "EF_x180": "q2.xy.EF_x180.pulse",
            },
            "intermediate_frequency": 267804596.93315327,
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q0": "q2.z.Cz_unipolar.flux_pulse_control_q0.pulse",
                "Cz_unipolar.flux_pulse_control_q1": "q2.z.Cz_unipolar.flux_pulse_control_q1.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 3),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": -40794189.0,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q3.xy": {
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
                "EF_x180": "q3.xy.EF_x180.pulse",
            },
            "intermediate_frequency": 185345952.95870727,
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "q3.z": {
            "operations": {
                "const": "q3.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q2": "q3.z.Cz_unipolar.flux_pulse_control_q2.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 4),
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "intermediate_frequency": 126195431.0,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q4.xy": {
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
                "EF_x180": "q4.xy.EF_x180.pulse",
            },
            "intermediate_frequency": 231635990.26926282,
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "q4.z": {
            "operations": {
                "const": "q4.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q2": "q4.z.Cz_unipolar.flux_pulse_control_q2.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 5),
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "intermediate_frequency": 348301377.0,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "twpa": {
            "operations": {
                "const": "twpa.const.pulse",
            },
            "intermediate_frequency": 50000000.0,
            "thread": "twpa",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 1000,
            },
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
        "q0.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.x180_DragCosine.wf.I",
                "Q": "q0.xy.x180_DragCosine.wf.Q",
            },
        },
        "q0.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.x90_DragCosine.wf.I",
                "Q": "q0.xy.x90_DragCosine.wf.Q",
            },
        },
        "q0.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.-x90_DragCosine.wf.I",
                "Q": "q0.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q0.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.y180_DragCosine.wf.I",
                "Q": "q0.xy.y180_DragCosine.wf.Q",
            },
        },
        "q0.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.y90_DragCosine.wf.I",
                "Q": "q0.xy.y90_DragCosine.wf.Q",
            },
        },
        "q0.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.-y90_DragCosine.wf.I",
                "Q": "q0.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q0.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.x180_Square.wf.I",
                "Q": "q0.xy.x180_Square.wf.Q",
            },
        },
        "q0.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.x90_Square.wf.I",
                "Q": "q0.xy.x90_Square.wf.Q",
            },
        },
        "q0.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.-x90_Square.wf.I",
                "Q": "q0.xy.-x90_Square.wf.Q",
            },
        },
        "q0.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.y180_Square.wf.I",
                "Q": "q0.xy.y180_Square.wf.Q",
            },
        },
        "q0.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.y90_Square.wf.I",
                "Q": "q0.xy.y90_Square.wf.Q",
            },
        },
        "q0.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.-y90_Square.wf.I",
                "Q": "q0.xy.-y90_Square.wf.Q",
            },
        },
        "q0.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.saturation.wf.I",
                "Q": "q0.xy.saturation.wf.Q",
            },
        },
        "q0.xy.EF_x180.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.xy.EF_x180.wf.I",
                "Q": "q0.xy.EF_x180.wf.Q",
            },
        },
        "q0.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q0.z.const.wf",
            },
        },
        "q0.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q0.resonator.readout.wf.I",
                "Q": "q0.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q0.resonator.readout.iw1",
                "iw2": "q0.resonator.readout.iw2",
                "iw3": "q0.resonator.readout.iw3",
            },
        },
        "q0.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q0.resonator.const.wf.I",
                "Q": "q0.resonator.const.wf.Q",
            },
        },
        "q1.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
        },
        "q1.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
        },
        "q1.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
        },
        "q1.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
        },
        "q1.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
        },
        "q1.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.xy.EF_x180.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.EF_x180.wf.I",
                "Q": "q1.xy.EF_x180.wf.Q",
            },
        },
        "q1.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
        },
        "q1.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
        },
        "q2.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
        },
        "q2.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
        },
        "q2.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
        },
        "q2.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
        },
        "q2.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.xy.EF_x180.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.EF_x180.wf.I",
                "Q": "q2.xy.EF_x180.wf.Q",
            },
        },
        "q2.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
        },
        "q2.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
        },
        "q3.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
        },
        "q3.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
        },
        "q3.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
        },
        "q3.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
        },
        "q3.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
        },
        "q3.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.xy.EF_x180.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.EF_x180.wf.I",
                "Q": "q3.xy.EF_x180.wf.Q",
            },
        },
        "q3.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
        },
        "q3.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
        },
        "q4.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
        },
        "q4.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
        },
        "q4.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
        },
        "q4.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
        },
        "q4.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
        },
        "q4.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.xy.EF_x180.pulse": {
            "operation": "control",
            "length": 48,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.EF_x180.wf.I",
                "Q": "q4.xy.EF_x180.wf.Q",
            },
        },
        "q4.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
        },
        "q4.resonator.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q0.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "q2.z.Cz_unipolar.flux_pulse_control_q0.wf",
            },
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q1.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "q2.z.Cz_unipolar.flux_pulse_control_q1.wf",
            },
        },
        "q3.z.Cz_unipolar.flux_pulse_control_q2.pulse": {
            "operation": "control",
            "length": 28,
            "waveforms": {
                "single": "q3.z.Cz_unipolar.flux_pulse_control_q2.wf",
            },
        },
        "q4.z.Cz_unipolar.flux_pulse_control_q2.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "single": "q4.z.Cz_unipolar.flux_pulse_control_q2.wf",
            },
        },
        "twpa.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "twpa.const.wf.I",
                "Q": "twpa.const.wf.Q",
            },
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001084800925224461, 0.0004319845402687823, 0.0009647403987050108, 0.0016972406269161174, 0.002616413740976422, 0.0037058570748899036, 0.004946129486553483, 0.006315098285398428, 0.007788334190777875, 0.009339547273058718, 0.010941056098038743, 0.01256428170279573, 0.01418025758795786, 0.015760146625571233, 0.017275755658331376, 0.01870003860714324, 0.02000757910904339, 0.021175044072799208, 0.022181600058474703, 0.023009285050659755, 0.02364332899106059, 0.02407241735053998] + [0.02428889303715773] * 2 + [0.02407241735053998, 0.02364332899106059, 0.02300928505065976, 0.022181600058474707, 0.021175044072799205, 0.020007579109043397, 0.018700038607143248, 0.01727575565833138, 0.015760146625571236, 0.01418025758795786, 0.01256428170279573, 0.010941056098038743, 0.00933954727305872, 0.007788334190777881, 0.0063150982853984365, 0.004946129486553492, 0.003705857074889909, 0.0026164137409764193, 0.0016972406269161202, 0.0009647403987050122, 0.00043198454026878365, 0.00010848009252244746, 0.0],
        },
        "q0.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.993916645243644e-05, -0.00011880871705954394, -0.00017555812329609315, -0.00022917469066337438, -0.0002787016302465185, -0.00032325513263534926, -0.000362040139524246, -0.00039436453154644246, -0.00041965147916052343, -0.0004374497361872568, -0.00044744169230835184, -0.0004494490408301139, -0.0004434359605706172, -0.00042950975508954483, -0.0004079189378536246, -0.0003790487975079273, -0.00034341452239086836, -0.00030165200698610334, -0.00025450650437040264, -0.00020281932715484106, -0.00014751283424132203, -8.957397130612306e-05, -3.003665873091936e-05, 3.0036658730919247e-05, 8.957397130612294e-05, 0.0001475128342413221, 0.00020281932715484079, 0.0002545065043704024, 0.0003016520069861034, 0.0003434145223908683, 0.0003790487975079272, 0.0004079189378536245, 0.00042950975508954483, 0.0004434359605706172, 0.0004494490408301139, 0.00044744169230835184, 0.0004374497361872568, 0.00041965147916052354, 0.0003943645315464426, 0.0003620401395242462, 0.0003232551326353495, 0.00027870163024651834, 0.0002291746906633745, 0.00017555812329609328, 0.00011880871705954408, 5.993916645243658e-05, -2.892692113931008e-19],
        },
        "q0.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.424004626122305e-05, 0.00021599227013439115, 0.0004823701993525054, 0.0008486203134580587, 0.001308206870488211, 0.0018529285374449518, 0.0024730647432767414, 0.003157549142699214, 0.0038941670953889377, 0.004669773636529359, 0.005470528049019372, 0.006282140851397865, 0.00709012879397893, 0.007880073312785616, 0.008637877829165688, 0.00935001930357162, 0.010003789554521695, 0.010587522036399604, 0.011090800029237352, 0.011504642525329878, 0.011821664495530295, 0.01203620867526999] + [0.012144446518578865] * 2 + [0.01203620867526999, 0.011821664495530295, 0.01150464252532988, 0.011090800029237353, 0.010587522036399602, 0.010003789554521698, 0.009350019303571624, 0.00863787782916569, 0.007880073312785618, 0.00709012879397893, 0.006282140851397865, 0.005470528049019372, 0.00466977363652936, 0.0038941670953889407, 0.0031575491426992183, 0.002473064743276746, 0.0018529285374449544, 0.0013082068704882096, 0.0008486203134580601, 0.0004823701993525061, 0.00021599227013439183, 5.424004626122373e-05, 0.0],
        },
        "q0.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -2.996958322621822e-05, -5.940435852977197e-05, -8.777906164804657e-05, -0.00011458734533168719, -0.00013935081512325925, -0.00016162756631767463, -0.000181020069762123, -0.00019718226577322123, -0.00020982573958026172, -0.0002187248680936284, -0.00022372084615417592, -0.00022472452041505695, -0.0002217179802853086, -0.00021475487754477241, -0.0002039594689268123, -0.00018952439875396366, -0.00017170726119543418, -0.00015082600349305167, -0.00012725325218520132, -0.00010140966357742053, -7.375641712066101e-05, -4.478698565306153e-05, -1.501832936545968e-05, 1.5018329365459623e-05, 4.478698565306147e-05, 7.375641712066105e-05, 0.00010140966357742039, 0.0001272532521852012, 0.0001508260034930517, 0.00017170726119543415, 0.0001895243987539636, 0.00020395946892681226, 0.00021475487754477241, 0.0002217179802853086, 0.00022472452041505695, 0.00022372084615417592, 0.0002187248680936284, 0.00020982573958026177, 0.0001971822657732213, 0.0001810200697621231, 0.00016162756631767474, 0.00013935081512325917, 0.00011458734533168726, 8.777906164804664e-05, 5.940435852977204e-05, 2.996958322621829e-05, -1.446346056965504e-19],
        },
        "q0.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -5.4240046261223045e-05, -0.00021599227013439115, -0.0004823701993525054, -0.0008486203134580587, -0.001308206870488211, -0.0018529285374449518, -0.0024730647432767414, -0.003157549142699214, -0.0038941670953889377, -0.004669773636529359, -0.005470528049019372, -0.006282140851397865, -0.00709012879397893, -0.007880073312785616, -0.008637877829165688, -0.00935001930357162, -0.010003789554521695, -0.010587522036399604, -0.011090800029237352, -0.011504642525329878, -0.011821664495530295, -0.01203620867526999] + [-0.012144446518578865] * 2 + [-0.01203620867526999, -0.011821664495530295, -0.01150464252532988, -0.011090800029237353, -0.010587522036399602, -0.010003789554521698, -0.009350019303571624, -0.00863787782916569, -0.007880073312785618, -0.00709012879397893, -0.006282140851397865, -0.005470528049019372, -0.00466977363652936, -0.0038941670953889407, -0.0031575491426992183, -0.002473064743276746, -0.0018529285374449544, -0.0013082068704882096, -0.0008486203134580601, -0.0004823701993525061, -0.00021599227013439183, -5.4240046261223736e-05, 1.7712630691222e-35],
        },
        "q0.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.9969583226218226e-05, 5.9404358529771995e-05, 8.777906164804663e-05, 0.0001145873453316873, 0.00013935081512325942, 0.00016162756631767485, 0.0001810200697621233, 0.0001971822657732216, 0.0002098257395802622, 0.00021872486809362896, 0.0002237208461541766, 0.0002247245204150577, 0.00022171798028530946, 0.0002147548775447734, 0.00020395946892681334, 0.0001895243987539648, 0.0001717072611954354, 0.00015082600349305297, 0.00012725325218520268, 0.00010140966357742194, 7.375641712066246e-05, 4.478698565306301e-05, 1.5018329365461167e-05, -1.5018329365458136e-05, -4.478698565305999e-05, -7.37564171206596e-05, -0.00010140966357741898, -0.00012725325218519986, -0.0001508260034930504, -0.00017170726119543293, -0.00018952439875396246, -0.0002039594689268112, -0.00021475487754477144, -0.00022171798028530773, -0.0002247245204150562, -0.00022372084615417524, -0.00021872486809362783, -0.00020982573958026128, -0.00019718226577322093, -0.0001810200697621228, -0.00016162756631767452, -0.000139350815123259, -0.00011458734533168715, -8.777906164804659e-05, -5.9404358529772015e-05, -2.9969583226218284e-05, 1.446346056965504e-19],
        },
        "q0.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.9939166452436446e-05, 0.00011880871705954396, 0.0001755581232960932, 0.00022917469066337449, 0.00027870163024651867, 0.0003232551326353495, 0.0003620401395242463, 0.00039436453154644284, 0.0004196514791605239, 0.0004374497361872574, 0.0004474416923083525, 0.00044944904083011467, 0.00044343596057061805, 0.0004295097550895458, 0.00040791893785362566, 0.00037904879750792845, 0.0003434145223908696, 0.00030165200698610464, 0.000254506504370404, 0.00020281932715484247, 0.00014751283424132346, 8.957397130612454e-05, 3.0036658730920846e-05, -3.003665873091776e-05, -8.957397130612146e-05, -0.00014751283424132067, -0.00020281932715483938, -0.00025450650437040107, -0.0003016520069861021, -0.00034341452239086706, -0.00037904879750792607, -0.00040791893785362344, -0.00042950975508954385, -0.0004434359605706163, -0.00044944904083011315, -0.0004474416923083512, -0.0004374497361872562, -0.00041965147916052305, -0.00039436453154644225, -0.0003620401395242459, -0.00032325513263534926, -0.0002787016302465182, -0.0002291746906633744, -0.00017555812329609323, -0.00011880871705954406, -5.9939166452436575e-05, 2.892692113931008e-19],
        },
        "q0.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001084800925224461, 0.0004319845402687823, 0.0009647403987050108, 0.0016972406269161174, 0.002616413740976422, 0.0037058570748899036, 0.004946129486553483, 0.006315098285398428, 0.007788334190777875, 0.009339547273058718, 0.010941056098038743, 0.01256428170279573, 0.01418025758795786, 0.015760146625571233, 0.017275755658331376, 0.01870003860714324, 0.02000757910904339, 0.021175044072799208, 0.022181600058474703, 0.023009285050659755, 0.02364332899106059, 0.02407241735053998] + [0.02428889303715773] * 2 + [0.02407241735053998, 0.02364332899106059, 0.02300928505065976, 0.022181600058474707, 0.021175044072799205, 0.020007579109043397, 0.018700038607143248, 0.01727575565833138, 0.015760146625571236, 0.01418025758795786, 0.01256428170279573, 0.010941056098038743, 0.00933954727305872, 0.007788334190777881, 0.0063150982853984365, 0.004946129486553492, 0.003705857074889909, 0.0026164137409764193, 0.0016972406269161202, 0.0009647403987050122, 0.00043198454026878365, 0.00010848009252244746, -1.7712630691222e-35],
        },
        "q0.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.9969583226218223e-05, 5.940435852977198e-05, 8.77790616480466e-05, 0.00011458734533168724, 0.00013935081512325934, 0.00016162756631767474, 0.00018102006976212316, 0.00019718226577322142, 0.00020982573958026196, 0.0002187248680936287, 0.00022372084615417625, 0.00022472452041505733, 0.00022171798028530903, 0.0002147548775447729, 0.00020395946892681283, 0.00018952439875396423, 0.0001717072611954348, 0.00015082600349305232, 0.000127253252185202, 0.00010140966357742123, 7.375641712066173e-05, 4.478698565306227e-05, 1.5018329365460423e-05, -1.501832936545888e-05, -4.478698565306073e-05, -7.375641712066034e-05, -0.00010140966357741969, -0.00012725325218520053, -0.00015082600349305105, -0.00017170726119543353, -0.00018952439875396303, -0.00020395946892681172, -0.00021475487754477193, -0.00022171798028530816, -0.00022472452041505657, -0.0002237208461541756, -0.0002187248680936281, -0.00020982573958026153, -0.00019718226577322112, -0.00018102006976212294, -0.00016162756631767463, -0.0001393508151232591, -0.0001145873453316872, -8.777906164804661e-05, -5.940435852977203e-05, -2.9969583226218287e-05, 1.446346056965504e-19],
        },
        "q0.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.424004626122305e-05, 0.00021599227013439115, 0.0004823701993525054, 0.0008486203134580587, 0.001308206870488211, 0.0018529285374449518, 0.0024730647432767414, 0.003157549142699214, 0.0038941670953889377, 0.004669773636529359, 0.005470528049019372, 0.006282140851397865, 0.00709012879397893, 0.007880073312785616, 0.008637877829165688, 0.00935001930357162, 0.010003789554521695, 0.010587522036399604, 0.011090800029237352, 0.011504642525329878, 0.011821664495530295, 0.01203620867526999] + [0.012144446518578865] * 2 + [0.01203620867526999, 0.011821664495530295, 0.01150464252532988, 0.011090800029237353, 0.010587522036399602, 0.010003789554521698, 0.009350019303571624, 0.00863787782916569, 0.007880073312785618, 0.00709012879397893, 0.006282140851397865, 0.005470528049019372, 0.00466977363652936, 0.0038941670953889407, 0.0031575491426992183, 0.002473064743276746, 0.0018529285374449544, 0.0013082068704882096, 0.0008486203134580601, 0.0004823701993525061, 0.00021599227013439183, 5.424004626122373e-05, -8.856315345611e-36],
        },
        "q0.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -2.9969583226218216e-05, -5.9404358529771954e-05, -8.777906164804655e-05, -0.00011458734533168713, -0.00013935081512325917, -0.00016162756631767452, -0.00018102006976212283, -0.00019718226577322104, -0.00020982573958026147, -0.0002187248680936281, -0.0002237208461541756, -0.00022472452041505657, -0.00022171798028530816, -0.00021475487754477193, -0.00020395946892681175, -0.0001895243987539631, -0.00017170726119543356, -0.00015082600349305102, -0.00012725325218520064, -0.00010140966357741982, -7.37564171206603e-05, -4.478698565306079e-05, -1.5018329365458936e-05, 1.5018329365460367e-05, 4.478698565306221e-05, 7.375641712066177e-05, 0.0001014096635774211, 0.0001272532521852019, 0.00015082600349305235, 0.00017170726119543478, 0.00018952439875396417, 0.0002039594689268128, 0.0002147548775447729, 0.00022171798028530903, 0.00022472452041505733, 0.00022372084615417625, 0.0002187248680936287, 0.00020982573958026201, 0.0001971822657732215, 0.00018102006976212327, 0.00016162756631767485, 0.00013935081512325925, 0.00011458734533168731, 8.777906164804667e-05, 5.9404358529772056e-05, 2.9969583226218294e-05, -1.446346056965504e-19],
        },
        "q0.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.424004626122305e-05, -0.00021599227013439115, -0.0004823701993525054, -0.0008486203134580587, -0.001308206870488211, -0.0018529285374449518, -0.0024730647432767414, -0.003157549142699214, -0.0038941670953889377, -0.004669773636529359, -0.005470528049019372, -0.006282140851397865, -0.00709012879397893, -0.007880073312785616, -0.008637877829165688, -0.00935001930357162, -0.010003789554521695, -0.010587522036399604, -0.011090800029237352, -0.011504642525329878, -0.011821664495530295, -0.01203620867526999] + [-0.012144446518578865] * 2 + [-0.01203620867526999, -0.011821664495530295, -0.01150464252532988, -0.011090800029237353, -0.010587522036399602, -0.010003789554521698, -0.009350019303571624, -0.00863787782916569, -0.007880073312785618, -0.00709012879397893, -0.006282140851397865, -0.005470528049019372, -0.00466977363652936, -0.0038941670953889407, -0.0031575491426992183, -0.002473064743276746, -0.0018529285374449544, -0.0013082068704882096, -0.0008486203134580601, -0.0004823701993525061, -0.00021599227013439183, -5.424004626122373e-05, -8.856315345611e-36],
        },
        "q0.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q0.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q0.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q0.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q0.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q0.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q0.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q0.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q0.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.012252345344633875,
        },
        "q0.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 8.075257200585712e-05, 0.0003215692564629215, 0.0007181526739320024, 0.001263425783933129, 0.0019476581749005714, 0.0027586397036077496, 0.0036818983854623737, 0.004700958647414346, 0.005797635334947146, 0.0069523582265909965, 0.008144521264988623, 0.009352850272476954, 0.010555782589291511, 0.011731851859740742, 0.012860071099831885, 0.013920307210497503, 0.014893640253225308, 0.015762701076809136, 0.016511981270263695, 0.01712810991078602, 0.017600092168189623, 0.017919505507909675] + [0.018080649991331826] * 2 + [0.017919505507909675, 0.017600092168189623, 0.017128109910786022, 0.0165119812702637, 0.015762701076809136, 0.014893640253225312, 0.013920307210497506, 0.012860071099831887, 0.011731851859740744, 0.010555782589291511, 0.009352850272476954, 0.008144521264988623, 0.006952358226590997, 0.005797635334947151, 0.004700958647414352, 0.0036818983854623798, 0.0027586397036077535, 0.0019476581749005694, 0.0012634257839331312, 0.0007181526739320034, 0.0003215692564629225, 8.075257200585813e-05, 0.0],
        },
        "q0.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.2202485249474724e-05, -8.365186614987714e-05, -0.0001236084775170855, -0.00016135929267466228, -0.00019623064743178707, -0.0002276002616367013, -0.0002549083437807583, -0.0002776675804911569, -0.0002954718326496237, -0.0003080033829546004, -0.0003150386055940164, -0.0003164519568532043, -0.00031221821544546064, -0.0003024129325865059, -0.00028721108378124957, -0.00026688394638176, -0.0002417942586364898, -0.00021238974661763916, -0.00017919513453879029, -0.0001428027810388851, -0.00010386210852828016, -6.30680142304493e-05, -2.1148469724566943e-05, 2.114846972456686e-05, 6.306801423044923e-05, 0.00010386210852828022, 0.0001428027810388849, 0.00017919513453879012, 0.0002123897466176392, 0.00024179425863648976, 0.0002668839463817599, 0.00028721108378124957, 0.0003024129325865059, 0.00031221821544546064, 0.0003164519568532043, 0.0003150386055940164, 0.0003080033829546004, 0.0002954718326496238, 0.00027766758049115704, 0.00025490834378075845, 0.00022760026163670146, 0.00019623064743178698, 0.00016135929267466236, 0.00012360847751708562, 8.365186614987723e-05, 4.220248524947482e-05, -2.03671161103514e-19],
        },
        "q0.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.012326234261830727,
        },
        "q0.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q0.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 8.852263618998774e-05, 0.0003525108562200021, 0.000787253784049609, 0.0013849934218324387, 0.002135063091571541, 0.0030240777822409426, 0.004036173005624497, 0.005153287898483947, 0.00635548751909127, 0.007621318586736088, 0.008928192316028191, 0.010252787514307945, 0.011571466748881805, 0.012860698157568703, 0.014097475375338174, 0.015259728083439316, 0.016326715854761795, 0.017279398267248947, 0.018100774680680467, 0.018776187613499914, 0.019293584305920285, 0.019643731801707986] + [0.019820381710505545] * 2 + [0.019643731801707986, 0.019293584305920285, 0.018776187613499914, 0.01810077468068047, 0.017279398267248943, 0.016326715854761798, 0.015259728083439322, 0.014097475375338175, 0.012860698157568707, 0.011571466748881805, 0.010252787514307945, 0.008928192316028191, 0.007621318586736089, 0.006355487519091275, 0.005153287898483953, 0.004036173005624504, 0.003024077782240947, 0.002135063091571539, 0.0013849934218324409, 0.0007872537840496101, 0.0003525108562200032, 8.852263618998885e-05, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.7220298797756847e-05, -9.359795024479807e-05, -0.00013830534405234428, -0.000180544675718762, -0.00021956218336979558, -0.00025466159865707047, -0.0002852165716832647, -0.0003106818482308651, -0.000330602999836596, -0.00034462453307811244, -0.00035249623336254315, -0.00035407763001182857, -0.00034934050296529806, -0.00033836938636732164, -0.00032136006005350083, -0.0002986160558548641, -0.00027054324106515166, -0.0002376425757293432, -0.00020050117299978755, -0.0001597818220880897, -0.00011621116077592803, -7.056670854662671e-05, -2.366299173155436e-05, 2.366299173155427e-05, 7.056670854662665e-05, 0.00011621116077592811, 0.00015978182208808945, 0.00020050117299978738, 0.00023764257572934323, 0.00027054324106515155, 0.00029861605585486406, 0.0003213600600535008, 0.00033836938636732164, 0.00034934050296529806, 0.00035407763001182857, 0.00035249623336254315, 0.00034462453307811244, 0.00033060299983659605, 0.0003106818482308652, 0.0002852165716832649, 0.00025466159865707063, 0.00021956218336979545, 0.00018054467571876207, 0.0001383053440523444, 9.359795024479818e-05, 4.722029879775695e-05, -2.2788736319536312e-19],
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.426131809499387e-05, 0.00017625542811000106, 0.0003936268920248045, 0.0006924967109162194, 0.0010675315457857706, 0.0015120388911204713, 0.0020180865028122485, 0.0025766439492419736, 0.003177743759545635, 0.003810659293368044, 0.004464096158014096, 0.005126393757153972, 0.005785733374440902, 0.006430349078784352, 0.007048737687669087, 0.007629864041719658, 0.008163357927380897, 0.008639699133624473, 0.009050387340340233, 0.009388093806749957, 0.009646792152960142, 0.009821865900853993] + [0.009910190855252772] * 2 + [0.009821865900853993, 0.009646792152960142, 0.009388093806749957, 0.009050387340340235, 0.008639699133624472, 0.008163357927380899, 0.007629864041719661, 0.007048737687669088, 0.006430349078784353, 0.005785733374440902, 0.005126393757153972, 0.004464096158014096, 0.0038106592933680444, 0.0031777437595456376, 0.0025766439492419767, 0.002018086502812252, 0.0015120388911204735, 0.0010675315457857695, 0.0006924967109162204, 0.00039362689202480504, 0.0001762554281100016, 4.4261318094994425e-05, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -2.3610149398878423e-05, -4.6798975122399034e-05, -6.915267202617214e-05, -9.0272337859381e-05, -0.00010978109168489779, -0.00012733079932853523, -0.00014260828584163236, -0.00015534092411543255, -0.000165301499918298, -0.00017231226653905622, -0.00017624811668127158, -0.00017703881500591429, -0.00017467025148264903, -0.00016918469318366082, -0.00016068003002675041, -0.00014930802792743206, -0.00013527162053257583, -0.0001188212878646716, -0.00010025058649989377, -7.989091104404485e-05, -5.8105580387964014e-05, -3.528335427331336e-05, -1.183149586577718e-05, 1.1831495865777136e-05, 3.528335427331332e-05, 5.8105580387964055e-05, 7.989091104404473e-05, 0.00010025058649989369, 0.00011882128786467161, 0.00013527162053257578, 0.00014930802792743203, 0.0001606800300267504, 0.00016918469318366082, 0.00017467025148264903, 0.00017703881500591429, 0.00017624811668127158, 0.00017231226653905622, 0.00016530149991829802, 0.0001553409241154326, 0.00014260828584163244, 0.00012733079932853532, 0.00010978109168489772, 9.027233785938104e-05, 6.91526720261722e-05, 4.679897512239909e-05, 2.3610149398878474e-05, -1.1394368159768156e-19],
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -4.426131809499387e-05, -0.00017625542811000106, -0.0003936268920248045, -0.0006924967109162194, -0.0010675315457857706, -0.0015120388911204713, -0.0020180865028122485, -0.0025766439492419736, -0.003177743759545635, -0.003810659293368044, -0.004464096158014096, -0.005126393757153972, -0.005785733374440902, -0.006430349078784352, -0.007048737687669087, -0.007629864041719658, -0.008163357927380897, -0.008639699133624473, -0.009050387340340233, -0.009388093806749957, -0.009646792152960142, -0.009821865900853993] + [-0.009910190855252772] * 2 + [-0.009821865900853993, -0.009646792152960142, -0.009388093806749957, -0.009050387340340235, -0.008639699133624472, -0.008163357927380899, -0.007629864041719661, -0.007048737687669088, -0.006430349078784353, -0.005785733374440902, -0.005126393757153972, -0.004464096158014096, -0.0038106592933680444, -0.0031777437595456376, -0.0025766439492419767, -0.002018086502812252, -0.0015120388911204735, -0.0010675315457857695, -0.0006924967109162204, -0.00039362689202480504, -0.0001762554281100016, -4.4261318094994425e-05, 1.395407649516659e-35],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.361014939887843e-05, 4.6798975122399055e-05, 6.91526720261722e-05, 9.027233785938108e-05, 0.00010978109168489793, 0.00012733079932853542, 0.0001426082858416326, 0.00015534092411543287, 0.00016530149991829838, 0.00017231226653905668, 0.00017624811668127212, 0.0001770388150059149, 0.00017467025148264973, 0.0001691846931836616, 0.00016068003002675128, 0.00014930802792743298, 0.00013527162053257683, 0.00011882128786467266, 0.00010025058649989488, 7.9890911044046e-05, 5.810558038796519e-05, 3.528335427331456e-05, 1.1831495865778393e-05, -1.1831495865775923e-05, -3.528335427331212e-05, -5.8105580387962876e-05, -7.989091104404357e-05, -0.00010025058649989258, -0.00011882128786467056, -0.00013527162053257477, -0.0001493080279274311, -0.00016068003002674952, -0.00016918469318366003, -0.00017467025148264832, -0.00017703881500591366, -0.00017624811668127103, -0.00017231226653905576, -0.00016530149991829764, -0.00015534092411543228, -0.0001426082858416322, -0.00012733079932853513, -0.00010978109168489759, -9.027233785938095e-05, -6.915267202617214e-05, -4.679897512239907e-05, -2.3610149398878467e-05, 1.1394368159768156e-19],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.722029879775685e-05, 9.35979502447981e-05, 0.00013830534405234434, 0.00018054467571876207, 0.00021956218336979572, 0.00025466159865707063, 0.000285216571683265, 0.0003106818482308654, 0.00033060299983659637, 0.00034462453307811293, 0.0003524962333625437, 0.0003540776300118292, 0.00034934050296529876, 0.00033836938636732245, 0.0003213600600535017, 0.00029861605585486503, 0.00027054324106515264, 0.00023764257572934426, 0.00020050117299978866, 0.00015978182208809083, 0.00011621116077592921, 7.056670854662792e-05, 2.3662991731555572e-05, -2.366299173155306e-05, -7.056670854662544e-05, -0.00011621116077592693, -0.0001597818220880883, -0.00020050117299978627, -0.00023764257572934217, -0.0002705432410651506, -0.00029861605585486314, -0.0003213600600534999, -0.0003383693863673208, -0.00034934050296529735, -0.0003540776300118279, -0.0003524962333625426, -0.00034462453307811195, -0.00033060299983659567, -0.0003106818482308649, -0.0002852165716832646, -0.00025466159865707047, -0.0002195621833697953, -0.000180544675718762, -0.00013830534405234434, -9.359795024479815e-05, -4.722029879775694e-05, 2.2788736319536312e-19],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 8.852263618998774e-05, 0.0003525108562200021, 0.000787253784049609, 0.0013849934218324387, 0.002135063091571541, 0.0030240777822409426, 0.004036173005624497, 0.005153287898483947, 0.00635548751909127, 0.007621318586736088, 0.008928192316028191, 0.010252787514307945, 0.011571466748881805, 0.012860698157568703, 0.014097475375338174, 0.015259728083439316, 0.016326715854761795, 0.017279398267248947, 0.018100774680680467, 0.018776187613499914, 0.019293584305920285, 0.019643731801707986] + [0.019820381710505545] * 2 + [0.019643731801707986, 0.019293584305920285, 0.018776187613499914, 0.01810077468068047, 0.017279398267248943, 0.016326715854761798, 0.015259728083439322, 0.014097475375338175, 0.012860698157568707, 0.011571466748881805, 0.010252787514307945, 0.008928192316028191, 0.007621318586736089, 0.006355487519091275, 0.005153287898483953, 0.004036173005624504, 0.003024077782240947, 0.002135063091571539, 0.0013849934218324409, 0.0007872537840496101, 0.0003525108562200032, 8.852263618998885e-05, -1.395407649516659e-35],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.3610149398878427e-05, 4.679897512239905e-05, 6.915267202617217e-05, 9.027233785938104e-05, 0.00010978109168489786, 0.00012733079932853532, 0.0001426082858416325, 0.0001553409241154327, 0.00016530149991829819, 0.00017231226653905646, 0.00017624811668127185, 0.0001770388150059146, 0.00017467025148264938, 0.00016918469318366123, 0.00016068003002675085, 0.00014930802792743252, 0.00013527162053257632, 0.00011882128786467213, 0.00010025058649989433, 7.989091104404542e-05, 5.8105580387964604e-05, 3.528335427331396e-05, 1.1831495865777786e-05, -1.183149586577653e-05, -3.528335427331272e-05, -5.8105580387963465e-05, -7.989091104404416e-05, -0.00010025058649989314, -0.00011882128786467108, -0.0001352716205325753, -0.00014930802792743157, -0.00016068003002674995, -0.0001691846931836604, -0.00017467025148264868, -0.00017703881500591396, -0.0001762481166812713, -0.00017231226653905598, -0.00016530149991829783, -0.00015534092411543244, -0.0001426082858416323, -0.00012733079932853523, -0.00010978109168489765, -9.0272337859381e-05, -6.915267202617217e-05, -4.6798975122399075e-05, -2.361014939887847e-05, 1.1394368159768156e-19],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.426131809499387e-05, 0.00017625542811000106, 0.0003936268920248045, 0.0006924967109162194, 0.0010675315457857706, 0.0015120388911204713, 0.0020180865028122485, 0.0025766439492419736, 0.003177743759545635, 0.003810659293368044, 0.004464096158014096, 0.005126393757153972, 0.005785733374440902, 0.006430349078784352, 0.007048737687669087, 0.007629864041719658, 0.008163357927380897, 0.008639699133624473, 0.009050387340340233, 0.009388093806749957, 0.009646792152960142, 0.009821865900853993] + [0.009910190855252772] * 2 + [0.009821865900853993, 0.009646792152960142, 0.009388093806749957, 0.009050387340340235, 0.008639699133624472, 0.008163357927380899, 0.007629864041719661, 0.007048737687669088, 0.006430349078784353, 0.005785733374440902, 0.005126393757153972, 0.004464096158014096, 0.0038106592933680444, 0.0031777437595456376, 0.0025766439492419767, 0.002018086502812252, 0.0015120388911204735, 0.0010675315457857695, 0.0006924967109162204, 0.00039362689202480504, 0.0001762554281100016, 4.4261318094994425e-05, -6.977038247583294e-36],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -2.361014939887842e-05, -4.679897512239902e-05, -6.915267202617211e-05, -9.027233785938095e-05, -0.00010978109168489772, -0.00012733079932853515, -0.00014260828584163222, -0.00015534092411543238, -0.0001653014999182978, -0.00017231226653905598, -0.0001762481166812713, -0.00017703881500591396, -0.00017467025148264868, -0.0001691846931836604, -0.00016068003002674998, -0.0001493080279274316, -0.00013527162053257534, -0.00011882128786467107, -0.00010025058649989322, -7.989091104404428e-05, -5.8105580387963425e-05, -3.5283354273312754e-05, -1.1831495865776573e-05, 1.1831495865777742e-05, 3.5283354273313926e-05, 5.8105580387964644e-05, 7.98909110440453e-05, 0.00010025058649989425, 0.00011882128786467214, 0.00013527162053257626, 0.0001493080279274325, 0.00016068003002675082, 0.00016918469318366123, 0.00017467025148264938, 0.0001770388150059146, 0.00017624811668127185, 0.00017231226653905646, 0.0001653014999182982, 0.00015534092411543276, 0.00014260828584163258, 0.0001273307993285354, 0.00010978109168489779, 9.027233785938108e-05, 6.915267202617222e-05, 4.67989751223991e-05, 2.3610149398878478e-05, -1.1394368159768156e-19],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.426131809499387e-05, -0.00017625542811000106, -0.0003936268920248045, -0.0006924967109162194, -0.0010675315457857706, -0.0015120388911204713, -0.0020180865028122485, -0.0025766439492419736, -0.003177743759545635, -0.003810659293368044, -0.004464096158014096, -0.005126393757153972, -0.005785733374440902, -0.006430349078784352, -0.007048737687669087, -0.007629864041719658, -0.008163357927380897, -0.008639699133624473, -0.009050387340340233, -0.009388093806749957, -0.009646792152960142, -0.009821865900853993] + [-0.009910190855252772] * 2 + [-0.009821865900853993, -0.009646792152960142, -0.009388093806749957, -0.009050387340340235, -0.008639699133624472, -0.008163357927380899, -0.007629864041719661, -0.007048737687669088, -0.006430349078784353, -0.005785733374440902, -0.005126393757153972, -0.004464096158014096, -0.0038106592933680444, -0.0031777437595456376, -0.0025766439492419767, -0.002018086502812252, -0.0015120388911204735, -0.0010675315457857695, -0.0006924967109162204, -0.00039362689202480504, -0.0001762554281100016, -4.4261318094994425e-05, -6.977038247583294e-36],
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.006053569048419676,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.35962527755611e-05, 0.00029307168422793825, 0.0006545097500833932, 0.0011514605794941091, 0.0017750560731362678, 0.002514168154652574, 0.0033556073514384773, 0.004284358161093272, 0.00528384700341615, 0.006336237976337529, 0.007422751138014025, 0.008523997635335545, 0.009620325698468372, 0.010692171327153404, 0.011720407410754268, 0.012686685051999737, 0.013573761003490246, 0.01436580537385623, 0.015048684112544617, 0.01561021123228583, 0.016040366268325255, 0.016331473093854205] + [0.01647833690067467] * 2 + [0.016331473093854205, 0.016040366268325255, 0.015610211232285832, 0.015048684112544623, 0.014365805373856228, 0.01357376100349025, 0.012686685051999741, 0.01172040741075427, 0.010692171327153405, 0.009620325698468372, 0.008523997635335545, 0.007422751138014025, 0.00633623797633753, 0.005283847003416155, 0.004284358161093277, 0.003355607351438483, 0.0025141681546525774, 0.0017750560731362658, 0.0011514605794941109, 0.0006545097500833941, 0.00029307168422793917, 7.359625277556202e-05, 0.0],
        },
        "q1.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.13971009767718e-05, -0.00010187701946899316, -0.000150538940135279, -0.00019651448984851706, -0.0002389832338348936, -0.00027718731635186856, -0.00031044498464185503, -0.0003381627548263294, -0.0003598460026397035, -0.00037510779001106206, -0.00038367576998320457, -0.0003853970467505492, -0.0003802409040884047, -0.0003682993534847284, -0.0003497854921929434, -0.0003250297005064032, -0.0002944737461142297, -0.0002586629007464352, -0.00021823620978698278, -0.00017391508849376978, -0.00012649044832626033, -7.680858311175474e-05, -2.5756066911990623e-05, 2.5756066911990528e-05, 7.680858311175466e-05, 0.0001264904483262604, 0.00017391508849376954, 0.0002182362097869826, 0.00025866290074643523, 0.0002944737461142296, 0.0003250297005064031, 0.0003497854921929434, 0.0003682993534847284, 0.0003802409040884047, 0.0003853970467505492, 0.00038367576998320457, 0.00037510779001106206, 0.00035984600263970354, 0.0003381627548263295, 0.0003104449846418552, 0.0002771873163518688, 0.00023898323383489346, 0.00019651448984851717, 0.00015053894013527912, 0.00010187701946899331, 5.139710097677191e-05, -2.4804480521497145e-19],
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.01650896347294208,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002569747209338718, 0.0010233131637525828, 0.0022853400007891342, 0.00402053433323864, 0.006197931577131021, 0.00877867602706552, 0.011716714237194083, 0.014959616846053556, 0.018449514179763045, 0.022124128937725293, 0.025917887532531245, 0.029763090252180772, 0.03359111936304718, 0.03733366359495935, 0.040923937157436314, 0.04429787153370051, 0.047395258784877506, 0.050160825962091586, 0.05254522145354784, 0.054505895665213897, 0.05600786031933331, 0.057024312821071114] + [0.05753711455145361] * 2 + [0.057024312821071114, 0.05600786031933331, 0.0545058956652139, 0.052545221453547855, 0.05016082596209158, 0.04739525878487752, 0.04429787153370052, 0.04092393715743632, 0.037333663594959356, 0.03359111936304718, 0.029763090252180772, 0.025917887532531245, 0.022124128937725297, 0.01844951417976306, 0.014959616846053575, 0.011716714237194103, 0.008778676027065533, 0.006197931577131014, 0.004020534333238646, 0.0022853400007891373, 0.001023313163752586, 0.00025697472093387497, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00027342744852201155, -0.0005419755777475313, -0.0008008521399485067, -0.0010454374767395614, -0.001271366956991325, -0.0014746088637763361, -0.0016515363404531259, -0.0017989921120089077, -0.001914344826706976, -0.0019955360126207877, -0.002041116811114255, -0.0020502738317584343, -0.002022843667302995, -0.001959315809682478, -0.0018608239150211235, -0.0017291255735124803, -0.0015665709451807616, -0.0013760608212195374, -0.0011609948593041652, -0.0009252109166200308, -0.0006729165632101575, -0.0004086139977881113, -0.00013701970589529013, 0.00013701970589528962, 0.00040861399778811087, 0.0006729165632101581, 0.0009252109166200296, 0.0011609948593041641, 0.0013760608212195376, 0.0015665709451807613, 0.0017291255735124799, 0.0018608239150211233, 0.001959315809682478, 0.002022843667302995, 0.0020502738317584343, 0.002041116811114255, 0.0019955360126207877, 0.0019143448267069764, 0.0017989921120089084, 0.001651536340453127, 0.001474608863776337, 0.0012713669569913244, 0.001045437476739562, 0.0008008521399485073, 0.000541975577747532, 0.0002734274485220122, -1.3195736125218487e-18],
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001284873604669359, 0.0005116565818762914, 0.0011426700003945671, 0.00201026716661932, 0.0030989657885655106, 0.00438933801353276, 0.005858357118597042, 0.007479808423026778, 0.009224757089881522, 0.011062064468862647, 0.012958943766265623, 0.014881545126090386, 0.01679555968152359, 0.018666831797479674, 0.020461968578718157, 0.022148935766850255, 0.023697629392438753, 0.025080412981045793, 0.02627261072677392, 0.027252947832606948, 0.028003930159666655, 0.028512156410535557] + [0.028768557275726806] * 2 + [0.028512156410535557, 0.028003930159666655, 0.02725294783260695, 0.026272610726773928, 0.02508041298104579, 0.02369762939243876, 0.02214893576685026, 0.02046196857871816, 0.018666831797479678, 0.01679555968152359, 0.014881545126090386, 0.012958943766265623, 0.011062064468862648, 0.00922475708988153, 0.007479808423026787, 0.005858357118597051, 0.0043893380135327665, 0.003098965788565507, 0.002010267166619323, 0.0011426700003945686, 0.000511656581876293, 0.00012848736046693749, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00013671372426100577, -0.00027098778887376567, -0.00040042606997425334, -0.0005227187383697807, -0.0006356834784956625, -0.0007373044318881681, -0.0008257681702265629, -0.0008994960560044539, -0.000957172413353488, -0.0009977680063103938, -0.0010205584055571276, -0.0010251369158792171, -0.0010114218336514974, -0.000979657904841239, -0.0009304119575105617, -0.0008645627867562402, -0.0007832854725903808, -0.0006880304106097687, -0.0005804974296520826, -0.0004626054583100154, -0.00033645828160507876, -0.00020430699889405565, -6.850985294764507e-05, 6.850985294764481e-05, 0.00020430699889405543, 0.00033645828160507903, 0.0004626054583100148, 0.0005804974296520821, 0.0006880304106097688, 0.0007832854725903807, 0.0008645627867562399, 0.0009304119575105616, 0.000979657904841239, 0.0010114218336514974, 0.0010251369158792171, 0.0010205584055571276, 0.0009977680063103938, 0.0009571724133534882, 0.0008994960560044542, 0.0008257681702265635, 0.0007373044318881685, 0.0006356834784956622, 0.000522718738369781, 0.00040042606997425366, 0.000270987788873766, 0.0001367137242610061, -6.597868062609244e-19],
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00012848736046693586, -0.0005116565818762914, -0.0011426700003945671, -0.00201026716661932, -0.0030989657885655106, -0.00438933801353276, -0.005858357118597042, -0.007479808423026778, -0.009224757089881522, -0.011062064468862647, -0.012958943766265623, -0.014881545126090386, -0.01679555968152359, -0.018666831797479674, -0.020461968578718157, -0.022148935766850255, -0.023697629392438753, -0.025080412981045793, -0.02627261072677392, -0.027252947832606948, -0.028003930159666655, -0.028512156410535557] + [-0.028768557275726806] * 2 + [-0.028512156410535557, -0.028003930159666655, -0.02725294783260695, -0.026272610726773928, -0.02508041298104579, -0.02369762939243876, -0.02214893576685026, -0.02046196857871816, -0.018666831797479678, -0.01679555968152359, -0.014881545126090386, -0.012958943766265623, -0.011062064468862648, -0.00922475708988153, -0.007479808423026787, -0.005858357118597051, -0.0043893380135327665, -0.003098965788565507, -0.002010267166619323, -0.0011426700003945686, -0.000511656581876293, -0.0001284873604669375, 8.080058004070959e-35],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001367137242610058, 0.0002709877888737657, 0.0004004260699742535, 0.0005227187383697809, 0.000635683478495663, 0.0007373044318881686, 0.0008257681702265637, 0.0008994960560044547, 0.0009571724133534891, 0.0009977680063103951, 0.001020558405557129, 0.0010251369158792189, 0.0010114218336514994, 0.0009796579048412413, 0.0009304119575105642, 0.0008645627867562429, 0.0007832854725903837, 0.0006880304106097717, 0.0005804974296520859, 0.0004626054583100188, 0.00033645828160508217, 0.00020430699889405915, 6.850985294764859e-05, -6.850985294764129e-05, -0.00020430699889405194, -0.0003364582816050756, -0.00046260545831001146, -0.0005804974296520788, -0.0006880304106097658, -0.0007832854725903777, -0.0008645627867562372, -0.0009304119575105591, -0.0009796579048412365, -0.0010114218336514955, -0.0010251369158792154, -0.001020558405557126, -0.0009977680063103925, -0.0009571724133534871, -0.0008994960560044533, -0.0008257681702265627, -0.000737304431888168, -0.0006356834784956618, -0.0005227187383697808, -0.0004004260699742535, -0.00027098778887376594, -0.00013671372426100607, 6.597868062609244e-19],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00027342744852201155, 0.0005419755777475314, 0.0008008521399485068, 0.0010454374767395616, 0.0012713669569913255, 0.0014746088637763366, 0.0016515363404531265, 0.0017989921120089086, 0.001914344826706977, 0.001995536012620789, 0.002041116811114257, 0.002050273831758436, 0.002022843667302997, 0.00195931580968248, 0.001860823915021126, 0.0017291255735124831, 0.0015665709451807644, 0.0013760608212195404, 0.0011609948593041684, 0.0009252109166200342, 0.000672916563210161, 0.00040861399778811477, 0.00013701970589529366, -0.0001370197058952861, -0.0004086139977881074, -0.0006729165632101546, -0.0009252109166200263, -0.0011609948593041609, -0.0013760608212195346, -0.0015665709451807585, -0.001729125573512477, -0.0018608239150211207, -0.0019593158096824757, -0.0020228436673029927, -0.0020502738317584326, -0.0020411168111142534, -0.0019955360126207864, -0.0019143448267069753, -0.0017989921120089075, -0.0016515363404531263, -0.0014746088637763366, -0.001271366956991324, -0.0010454374767395619, -0.0008008521399485072, -0.0005419755777475319, -0.0002734274485220122, 1.3195736125218487e-18],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002569747209338718, 0.0010233131637525828, 0.0022853400007891342, 0.00402053433323864, 0.006197931577131021, 0.00877867602706552, 0.011716714237194083, 0.014959616846053556, 0.018449514179763045, 0.022124128937725293, 0.025917887532531245, 0.029763090252180772, 0.03359111936304718, 0.03733366359495935, 0.040923937157436314, 0.04429787153370051, 0.047395258784877506, 0.050160825962091586, 0.05254522145354784, 0.054505895665213897, 0.05600786031933331, 0.057024312821071114] + [0.05753711455145361] * 2 + [0.057024312821071114, 0.05600786031933331, 0.0545058956652139, 0.052545221453547855, 0.05016082596209158, 0.04739525878487752, 0.04429787153370052, 0.04092393715743632, 0.037333663594959356, 0.03359111936304718, 0.029763090252180772, 0.025917887532531245, 0.022124128937725297, 0.01844951417976306, 0.014959616846053575, 0.011716714237194103, 0.008778676027065533, 0.006197931577131014, 0.004020534333238646, 0.0022853400007891373, 0.001023313163752586, 0.00025697472093387497, -8.080058004070959e-35],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00013671372426100577, 0.0002709877888737657, 0.0004004260699742534, 0.0005227187383697808, 0.0006356834784956627, 0.0007373044318881683, 0.0008257681702265633, 0.0008994960560044543, 0.0009571724133534885, 0.0009977680063103945, 0.0010205584055571284, 0.001025136915879218, 0.0010114218336514985, 0.00097965790484124, 0.000930411957510563, 0.0008645627867562416, 0.0007832854725903822, 0.0006880304106097702, 0.0005804974296520842, 0.0004626054583100171, 0.0003364582816050805, 0.00020430699889405739, 6.850985294764683e-05, -6.850985294764305e-05, -0.0002043069988940537, -0.0003364582816050773, -0.00046260545831001314, -0.0005804974296520804, -0.0006880304106097673, -0.0007832854725903793, -0.0008645627867562385, -0.0009304119575105603, -0.0009796579048412378, -0.0010114218336514963, -0.0010251369158792163, -0.0010205584055571267, -0.0009977680063103932, -0.0009571724133534877, -0.0008994960560044537, -0.0008257681702265632, -0.0007373044318881683, -0.000635683478495662, -0.0005227187383697809, -0.0004004260699742536, -0.00027098778887376594, -0.0001367137242610061, 6.597868062609244e-19],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001284873604669359, 0.0005116565818762914, 0.0011426700003945671, 0.00201026716661932, 0.0030989657885655106, 0.00438933801353276, 0.005858357118597042, 0.007479808423026778, 0.009224757089881522, 0.011062064468862647, 0.012958943766265623, 0.014881545126090386, 0.01679555968152359, 0.018666831797479674, 0.020461968578718157, 0.022148935766850255, 0.023697629392438753, 0.025080412981045793, 0.02627261072677392, 0.027252947832606948, 0.028003930159666655, 0.028512156410535557] + [0.028768557275726806] * 2 + [0.028512156410535557, 0.028003930159666655, 0.02725294783260695, 0.026272610726773928, 0.02508041298104579, 0.02369762939243876, 0.02214893576685026, 0.02046196857871816, 0.018666831797479678, 0.01679555968152359, 0.014881545126090386, 0.012958943766265623, 0.011062064468862648, 0.00922475708988153, 0.007479808423026787, 0.005858357118597051, 0.0043893380135327665, 0.003098965788565507, 0.002010267166619323, 0.0011426700003945686, 0.000511656581876293, 0.00012848736046693749, -4.0400290020354793e-35],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00013671372426100577, -0.0002709877888737656, -0.0004004260699742533, -0.0005227187383697806, -0.0006356834784956623, -0.0007373044318881678, -0.0008257681702265626, -0.0008994960560044534, -0.0009571724133534875, -0.0009977680063103932, -0.0010205584055571267, -0.0010251369158792163, -0.0010114218336514963, -0.0009796579048412378, -0.0009304119575105604, -0.0008645627867562388, -0.0007832854725903794, -0.0006880304106097672, -0.000580497429652081, -0.00046260545831001374, -0.000336458281605077, -0.00020430699889405392, -6.85098529476433e-05, 6.850985294764657e-05, 0.00020430699889405717, 0.00033645828160508076, 0.0004626054583100165, 0.0005804974296520837, 0.0006880304106097703, 0.0007832854725903821, 0.0008645627867562414, 0.0009304119575105629, 0.00097965790484124, 0.0010114218336514985, 0.001025136915879218, 0.0010205584055571284, 0.0009977680063103945, 0.0009571724133534888, 0.0008994960560044546, 0.0008257681702265638, 0.0007373044318881687, 0.0006356834784956624, 0.0005227187383697811, 0.0004004260699742537, 0.00027098778887376605, 0.0001367137242610061, -6.597868062609244e-19],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001284873604669359, -0.0005116565818762914, -0.0011426700003945671, -0.00201026716661932, -0.0030989657885655106, -0.00438933801353276, -0.005858357118597042, -0.007479808423026778, -0.009224757089881522, -0.011062064468862647, -0.012958943766265623, -0.014881545126090386, -0.01679555968152359, -0.018666831797479674, -0.020461968578718157, -0.022148935766850255, -0.023697629392438753, -0.025080412981045793, -0.02627261072677392, -0.027252947832606948, -0.028003930159666655, -0.028512156410535557] + [-0.028768557275726806] * 2 + [-0.028512156410535557, -0.028003930159666655, -0.02725294783260695, -0.026272610726773928, -0.02508041298104579, -0.02369762939243876, -0.02214893576685026, -0.02046196857871816, -0.018666831797479678, -0.01679555968152359, -0.014881545126090386, -0.012958943766265623, -0.011062064468862648, -0.00922475708988153, -0.007479808423026787, -0.005858357118597051, -0.0043893380135327665, -0.003098965788565507, -0.002010267166619323, -0.0011426700003945686, -0.000511656581876293, -0.00012848736046693749, -4.0400290020354793e-35],
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.0192265628415506,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001602185393266137, 0.0006380150536765267, 0.0014248632529319527, 0.0025067218123364, 0.0038642849402675903, 0.005473326890546326, 0.007305134271450967, 0.009327018436872956, 0.011502898815981004, 0.013793946771862364, 0.016159278499468407, 0.018556684598084253, 0.020943383299084496, 0.023276783907607835, 0.0255152468345159, 0.027618826655847837, 0.02954998493985725, 0.031274260121216, 0.03276088246846389, 0.033983323170595575, 0.03491976774432133, 0.035553505314038246] + [0.0358732268178012] * 2 + [0.035553505314038246, 0.03491976774432133, 0.033983323170595575, 0.0327608824684639, 0.031274260121215994, 0.029549984939857256, 0.027618826655847844, 0.025515246834515903, 0.023276783907607842, 0.020943383299084496, 0.018556684598084253, 0.016159278499468407, 0.013793946771862365, 0.011502898815981013, 0.009327018436872966, 0.007305134271450979, 0.0054733268905463334, 0.0038642849402675864, 0.002506721812336404, 0.0014248632529319546, 0.0006380150536765286, 0.0001602185393266157, 0.0],
        },
        "q2.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.000214939951450731, -0.00042604429437580177, -0.0006295458667745597, -0.000821813178266507, -0.000999415214123173, -0.0011591826618072248, -0.00129826446742978, -0.0014141787128745943, -0.0015048569056856458, -0.0015686808913640152, -0.001604511729373253, -0.001611710017560237, -0.0015901473023017397, -0.0015402083707623784, -0.001462784384358549, -0.0013592569759618357, -0.001231473594627688, -0.001081714537823258, -0.0009126522594650794, -0.0007273036799156127, -0.0005289763489679071, -0.00032120942254118805, -0.00010771050635962845, 0.00010771050635962804, 0.00032120942254118773, 0.0005289763489679074, 0.0007273036799156117, 0.0009126522594650787, 0.0010817145378232583, 0.0012314735946276877, 0.0013592569759618355, 0.0014627843843585486, 0.0015402083707623784, 0.0015901473023017397, 0.001611710017560237, 0.001604511729373253, 0.0015686808913640152, 0.0015048569056856462, 0.0014141787128745947, 0.0012982644674297806, 0.0011591826618072257, 0.0009994152141231723, 0.0008218131782665075, 0.0006295458667745601, 0.0004260442943758023, 0.00021493995145073152, -1.0373102252324863e-18],
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0204578599682783,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004110178090848037, 0.0016367366137989116, 0.003655283433034376, 0.006430637250981682, 0.009913271813010206, 0.014041039422855405, 0.018740279969730957, 0.023927135394750807, 0.029509046139976576, 0.035386402875921784, 0.041454324032396336, 0.04760452741261123, 0.05372726249154549, 0.059713268916665244, 0.06545572626150312, 0.07085216023869914, 0.07580627135608636, 0.08022965338340993, 0.08404337096360034, 0.08717936821609054, 0.08958168319561663, 0.09120744653445707] + [0.09202764644731523] * 2 + [0.09120744653445707, 0.08958168319561663, 0.08717936821609056, 0.08404337096360037, 0.08022965338340991, 0.07580627135608638, 0.07085216023869917, 0.06545572626150313, 0.05971326891666526, 0.05372726249154549, 0.04760452741261123, 0.041454324032396336, 0.035386402875921784, 0.0295090461399766, 0.02392713539475084, 0.01874027996973099, 0.014041039422855426, 0.009913271813010195, 0.006430637250981692, 0.0036552834330343814, 0.0016367366137989168, 0.0004110178090848089, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003687667501787422, -0.0007309528489642983, -0.0010800950768434922, -0.0014099629824884862, -0.00171467006530833, -0.001988778820191459, -0.002227397769913226, -0.0024262687536628596, -0.002581842914024005, -0.002691344026419398, -0.002752818040904213, -0.0027651679522336225, -0.0027281733759473782, -0.0026424944811357255, -0.00250966020970635, -0.00233204099237981, -0.002112806448297175, -0.0018558688230913636, -0.0015658131747711389, -0.0012478155532523196, -0.0009075506336244122, -0.0005510904514392059, -0.00018479604709249056, 0.00018479604709248988, 0.0005510904514392052, 0.0009075506336244128, 0.001247815553252318, 0.0015658131747711373, 0.0018558688230913638, 0.0021128064482971746, 0.002332040992379809, 0.0025096602097063494, 0.0026424944811357255, 0.0027281733759473782, 0.0027651679522336225, 0.002752818040904213, 0.002691344026419398, 0.0025818429140240053, 0.0024262687536628605, 0.0022273977699132272, 0.00198877882019146, 0.0017146700653083292, 0.0014099629824884871, 0.0010800950768434928, 0.0007309528489642991, 0.000368766750178743, -1.7796855266055385e-18],
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020550890454240186, 0.0008183683068994558, 0.001827641716517188, 0.003215318625490841, 0.004956635906505103, 0.007020519711427703, 0.009370139984865479, 0.011963567697375404, 0.014754523069988288, 0.017693201437960892, 0.020727162016198168, 0.023802263706305615, 0.026863631245772745, 0.029856634458332622, 0.03272786313075156, 0.03542608011934957, 0.03790313567804318, 0.04011482669170496, 0.04202168548180017, 0.04358968410804527, 0.044790841597808315, 0.04560372326722854] + [0.046013823223657616] * 2 + [0.04560372326722854, 0.044790841597808315, 0.04358968410804528, 0.042021685481800186, 0.040114826691704956, 0.03790313567804319, 0.035426080119349584, 0.032727863130751565, 0.02985663445833263, 0.026863631245772745, 0.023802263706305615, 0.020727162016198168, 0.017693201437960892, 0.0147545230699883, 0.01196356769737542, 0.009370139984865494, 0.007020519711427713, 0.004956635906505098, 0.003215318625490846, 0.0018276417165171907, 0.0008183683068994584, 0.00020550890454240444, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001843833750893711, -0.00036547642448214913, -0.0005400475384217461, -0.0007049814912442431, -0.000857335032654165, -0.0009943894100957295, -0.001113698884956613, -0.0012131343768314298, -0.0012909214570120025, -0.001345672013209699, -0.0013764090204521065, -0.0013825839761168112, -0.0013640866879736891, -0.0013212472405678627, -0.001254830104853175, -0.001166020496189905, -0.0010564032241485875, -0.0009279344115456818, -0.0007829065873855694, -0.0006239077766261598, -0.0004537753168122061, -0.0002755452257196029, -9.239802354624528e-05, 9.239802354624494e-05, 0.0002755452257196026, 0.0004537753168122064, 0.000623907776626159, 0.0007829065873855687, 0.0009279344115456819, 0.0010564032241485873, 0.0011660204961899045, 0.0012548301048531747, 0.0013212472405678627, 0.0013640866879736891, 0.0013825839761168112, 0.0013764090204521065, 0.001345672013209699, 0.0012909214570120027, 0.0012131343768314303, 0.0011136988849566136, 0.00099438941009573, 0.0008573350326541646, 0.0007049814912442436, 0.0005400475384217464, 0.00036547642448214957, 0.0001843833750893715, -8.898427633027693e-19],
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020550890454240183, -0.0008183683068994558, -0.001827641716517188, -0.003215318625490841, -0.004956635906505103, -0.007020519711427703, -0.009370139984865479, -0.011963567697375404, -0.014754523069988288, -0.017693201437960892, -0.020727162016198168, -0.023802263706305615, -0.026863631245772745, -0.029856634458332622, -0.03272786313075156, -0.03542608011934957, -0.03790313567804318, -0.04011482669170496, -0.04202168548180017, -0.04358968410804527, -0.044790841597808315, -0.04560372326722854] + [-0.046013823223657616] * 2 + [-0.04560372326722854, -0.044790841597808315, -0.04358968410804528, -0.042021685481800186, -0.040114826691704956, -0.03790313567804319, -0.035426080119349584, -0.032727863130751565, -0.02985663445833263, -0.026863631245772745, -0.023802263706305615, -0.020727162016198168, -0.017693201437960892, -0.0147545230699883, -0.01196356769737542, -0.009370139984865494, -0.007020519711427713, -0.004956635906505098, -0.003215318625490846, -0.0018276417165171907, -0.0008183683068994584, -0.00020550890454240446, 1.0897430918231721e-34],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00018438337508937112, 0.00036547642448214924, 0.0005400475384217463, 0.0007049814912442436, 0.0008573350326541657, 0.0009943894100957304, 0.001113698884956614, 0.0012131343768314313, 0.0012909214570120042, 0.0013456720132097011, 0.001376409020452109, 0.001382583976116814, 0.0013640866879736924, 0.0013212472405678664, 0.0012548301048531788, 0.0011660204961899093, 0.001056403224148592, 0.0009279344115456867, 0.0007829065873855745, 0.0006239077766261651, 0.00045377531681221157, 0.0002755452257196085, 9.239802354625092e-05, -9.23980235462393e-05, -0.000275545225719597, -0.00045377531681220094, -0.0006239077766261537, -0.0007829065873855636, -0.000927934411545677, -0.0010564032241485828, -0.0011660204961899002, -0.0012548301048531708, -0.001321247240567859, -0.0013640866879736859, -0.0013825839761168084, -0.0013764090204521039, -0.0013456720132096968, -0.001290921457012001, -0.0012131343768314287, -0.0011136988849566125, -0.0009943894100957291, -0.000857335032654164, -0.0007049814912442431, -0.0005400475384217462, -0.00036547642448214946, -0.00018438337508937147, 8.898427633027693e-19],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003687667501787422, 0.0007309528489642984, 0.0010800950768434924, 0.0014099629824884867, 0.0017146700653083307, 0.00198877882019146, 0.0022273977699132272, 0.002426268753662861, 0.0025818429140240066, 0.0026913440264194, 0.0027528180409042155, 0.0027651679522336255, 0.0027281733759473817, 0.002642494481135729, 0.0025096602097063538, 0.0023320409923798142, 0.00211280644829718, 0.0018558688230913686, 0.001565813174771144, 0.001247815553252325, 0.0009075506336244177, 0.0005510904514392115, 0.0001847960470924962, -0.00018479604709248425, -0.0005510904514391996, -0.0009075506336244073, -0.0012478155532523127, -0.0015658131747711321, -0.0018558688230913588, -0.00211280644829717, -0.0023320409923798047, -0.0025096602097063455, -0.002642494481135722, -0.0027281733759473748, -0.0027651679522336194, -0.0027528180409042103, -0.0026913440264193958, -0.0025818429140240036, -0.002426268753662859, -0.002227397769913226, -0.001988778820191459, -0.0017146700653083286, -0.0014099629824884867, -0.0010800950768434926, -0.000730952848964299, -0.000368766750178743, 1.7796855266055385e-18],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004110178090848037, 0.0016367366137989116, 0.003655283433034376, 0.006430637250981682, 0.009913271813010206, 0.014041039422855405, 0.018740279969730957, 0.023927135394750807, 0.029509046139976576, 0.035386402875921784, 0.041454324032396336, 0.04760452741261123, 0.05372726249154549, 0.059713268916665244, 0.06545572626150312, 0.07085216023869914, 0.07580627135608636, 0.08022965338340993, 0.08404337096360034, 0.08717936821609054, 0.08958168319561663, 0.09120744653445707] + [0.09202764644731523] * 2 + [0.09120744653445707, 0.08958168319561663, 0.08717936821609056, 0.08404337096360037, 0.08022965338340991, 0.07580627135608638, 0.07085216023869917, 0.06545572626150313, 0.05971326891666526, 0.05372726249154549, 0.04760452741261123, 0.041454324032396336, 0.035386402875921784, 0.0295090461399766, 0.02392713539475084, 0.01874027996973099, 0.014041039422855426, 0.009913271813010195, 0.006430637250981692, 0.0036552834330343814, 0.0016367366137989168, 0.0004110178090848089, -1.0897430918231721e-34],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001843833750893711, 0.0003654764244821492, 0.0005400475384217462, 0.0007049814912442433, 0.0008573350326541654, 0.00099438941009573, 0.0011136988849566136, 0.0012131343768314305, 0.0012909214570120033, 0.0013456720132097, 0.0013764090204521078, 0.0013825839761168128, 0.0013640866879736909, 0.0013212472405678645, 0.0012548301048531769, 0.0011660204961899071, 0.00105640322414859, 0.0009279344115456843, 0.000782906587385572, 0.0006239077766261625, 0.00045377531681220886, 0.00027554522571960575, 9.23980235462481e-05, -9.239802354624212e-05, -0.0002755452257195998, -0.00045377531681220365, -0.0006239077766261563, -0.0007829065873855661, -0.0009279344115456794, -0.001056403224148585, -0.0011660204961899024, -0.0012548301048531728, -0.001321247240567861, -0.0013640866879736874, -0.0013825839761168097, -0.0013764090204521052, -0.0013456720132096979, -0.0012909214570120018, -0.0012131343768314296, -0.001113698884956613, -0.0009943894100957295, -0.0008573350326541643, -0.0007049814912442433, -0.0005400475384217463, -0.0003654764244821495, -0.0001843833750893715, 8.898427633027693e-19],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020550890454240186, 0.0008183683068994558, 0.001827641716517188, 0.003215318625490841, 0.004956635906505103, 0.007020519711427703, 0.009370139984865479, 0.011963567697375404, 0.014754523069988288, 0.017693201437960892, 0.020727162016198168, 0.023802263706305615, 0.026863631245772745, 0.029856634458332622, 0.03272786313075156, 0.03542608011934957, 0.03790313567804318, 0.04011482669170496, 0.04202168548180017, 0.04358968410804527, 0.044790841597808315, 0.04560372326722854] + [0.046013823223657616] * 2 + [0.04560372326722854, 0.044790841597808315, 0.04358968410804528, 0.042021685481800186, 0.040114826691704956, 0.03790313567804319, 0.035426080119349584, 0.032727863130751565, 0.02985663445833263, 0.026863631245772745, 0.023802263706305615, 0.020727162016198168, 0.017693201437960892, 0.0147545230699883, 0.01196356769737542, 0.009370139984865494, 0.007020519711427713, 0.004956635906505098, 0.003215318625490846, 0.0018276417165171907, 0.0008183683068994584, 0.00020550890454240444, -5.448715459115861e-35],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001843833750893711, -0.0003654764244821491, -0.000540047538421746, -0.0007049814912442429, -0.0008573350326541647, -0.0009943894100957291, -0.0011136988849566123, -0.0012131343768314292, -0.0012909214570120016, -0.0013456720132096979, -0.0013764090204521052, -0.0013825839761168097, -0.0013640866879736874, -0.001321247240567861, -0.001254830104853173, -0.0011660204961899028, -0.0010564032241485851, -0.0009279344115456793, -0.0007829065873855668, -0.0006239077766261571, -0.00045377531681220333, -0.0002755452257196001, -9.239802354624246e-05, 9.239802354624776e-05, 0.0002755452257196054, 0.0004537753168122092, 0.0006239077766261618, 0.0007829065873855713, 0.0009279344115456844, 0.0010564032241485897, 0.0011660204961899067, 0.0012548301048531767, 0.0013212472405678645, 0.0013640866879736909, 0.0013825839761168128, 0.0013764090204521078, 0.0013456720132097, 0.0012909214570120035, 0.001213134376831431, 0.0011136988849566143, 0.0009943894100957304, 0.0008573350326541649, 0.0007049814912442438, 0.0005400475384217465, 0.0003654764244821496, 0.0001843833750893715, -8.898427633027693e-19],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020550890454240186, -0.0008183683068994558, -0.001827641716517188, -0.003215318625490841, -0.004956635906505103, -0.007020519711427703, -0.009370139984865479, -0.011963567697375404, -0.014754523069988288, -0.017693201437960892, -0.020727162016198168, -0.023802263706305615, -0.026863631245772745, -0.029856634458332622, -0.03272786313075156, -0.03542608011934957, -0.03790313567804318, -0.04011482669170496, -0.04202168548180017, -0.04358968410804527, -0.044790841597808315, -0.04560372326722854] + [-0.046013823223657616] * 2 + [-0.04560372326722854, -0.044790841597808315, -0.04358968410804528, -0.042021685481800186, -0.040114826691704956, -0.03790313567804319, -0.035426080119349584, -0.032727863130751565, -0.02985663445833263, -0.026863631245772745, -0.023802263706305615, -0.020727162016198168, -0.017693201437960892, -0.0147545230699883, -0.01196356769737542, -0.009370139984865494, -0.007020519711427713, -0.004956635906505098, -0.003215318625490846, -0.0018276417165171907, -0.0008183683068994584, -0.00020550890454240444, -5.448715459115861e-35],
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.02393249586119253,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00026232853701164846, 0.0010446328890889476, 0.0023329528165359397, 0.004104298219726469, 0.0063270593979766485, 0.008961571125402416, 0.011960820477815111, 0.015271285779467403, 0.01883389169862492, 0.02258506344826059, 0.026457861279635272, 0.030383175023699794, 0.034290957363698915, 0.038111473831198256, 0.04177654721932559, 0.04522077420664258, 0.04838269248096531, 0.051205877535781257, 0.0536399495669047, 0.05564147250127606, 0.05717472911471448, 0.05821235840662964] + [0.05873584385772543] * 2 + [0.05821235840662964, 0.05717472911471448, 0.05564147250127607, 0.05363994956690472, 0.05120587753578125, 0.04838269248096532, 0.04522077420664259, 0.0417765472193256, 0.03811147383119826, 0.034290957363698915, 0.030383175023699794, 0.026457861279635272, 0.022585063448260594, 0.018833891698624938, 0.015271285779467424, 0.011960820477815132, 0.008961571125402428, 0.0063270593979766416, 0.004104298219726475, 0.0023329528165359427, 0.0010446328890889509, 0.00026232853701165177, 0.0],
        },
        "q3.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020591122426341646, -0.0004081479578517248, -0.0006031012814629645, -0.000787292248418763, -0.000957433966550229, -0.0011104902528665743, -0.0012437298143125133, -0.0013547749877575392, -0.0014416441694508166, -0.0015027871767870596, -0.0015371129113518484, -0.0015440088295986826, -0.00152335187370308, -0.0014755106675323703, -0.0014013389385440485, -0.0013021602829990724, -0.0011797445463552284, -0.0010362762403330079, -0.0008743155602522055, -0.0006967526982857819, -0.0005067562679120699, -0.0003077167599321896, -0.00010318603908137324, 0.00010318603908137285, 0.0003077167599321892, 0.0005067562679120703, 0.0006967526982857809, 0.0008743155602522045, 0.0010362762403330079, 0.0011797445463552281, 0.0013021602829990722, 0.0014013389385440483, 0.0014755106675323703, 0.00152335187370308, 0.0015440088295986826, 0.0015371129113518484, 0.0015027871767870596, 0.0014416441694508168, 0.0013547749877575398, 0.001243729814312514, 0.0011104902528665751, 0.0009574339665502285, 0.0007872922484187634, 0.000603101281462965, 0.00040814795785172527, 0.00020591122426341692, -9.9373716694796e-19],
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04512714510853295,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006672932696453106, 0.0026572652143759634, 0.005934404737694919, 0.010440231207171679, 0.016094338042713416, 0.022795827573891616, 0.03042511156126116, 0.038846045251326365, 0.04790835688289238, 0.057450329290203744, 0.0673016857495985, 0.07728662857167577, 0.08722697621522789, 0.09694534294106444, 0.10626830426473052, 0.11502949172054025, 0.12307256171078834, 0.13025398546095493, 0.13644561029408714, 0.14153694651835555, 0.14543713911822198, 0.1480765890643446] + [0.1494081953099051] * 2 + [0.1480765890643446, 0.14543713911822198, 0.14153694651835555, 0.13644561029408717, 0.1302539854609549, 0.12307256171078837, 0.11502949172054029, 0.10626830426473054, 0.09694534294106445, 0.08722697621522789, 0.07728662857167577, 0.0673016857495985, 0.05745032929020375, 0.047908356882892425, 0.038846045251326414, 0.030425111561261212, 0.02279582757389165, 0.0160943380427134, 0.010440231207171694, 0.005934404737694928, 0.0026572652143759716, 0.000667293269645319, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0008777138199601045, -0.0017397648160095947, -0.0025707696677016003, -0.003355899073770806, -0.004081142381365847, -0.004733557606481357, -0.005301502383969145, -0.005774841725820081, -0.006145128880265217, -0.006405756064261216, -0.006552072379535292, -0.006581466807975087, -0.006493414805308723, -0.006289487661609771, -0.005973324461588665, -0.005550567145039826, -0.005028759826292374, -0.004417214169311202, -0.003726843220832927, -0.0029699666667883325, -0.0021600909872150804, -0.0013116684328014752, -0.0004398391241305228, 0.0004398391241305211, 0.0013116684328014737, 0.0021600909872150817, 0.002969966666788328, 0.0037268432208329236, 0.004417214169311203, 0.005028759826292372, 0.005550567145039824, 0.005973324461588665, 0.006289487661609771, 0.006493414805308723, 0.006581466807975087, 0.006552072379535292, 0.006405756064261216, 0.006145128880265219, 0.005774841725820083, 0.005301502383969149, 0.004733557606481359, 0.004081142381365845, 0.0033558990737708088, 0.0025707696677016024, 0.001739764816009597, 0.0008777138199601066, -4.2358878101876744e-18],
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003336466348226553, 0.0013286326071879817, 0.0029672023688474595, 0.005220115603585839, 0.008047169021356708, 0.011397913786945808, 0.01521255578063058, 0.019423022625663183, 0.02395417844144619, 0.028725164645101872, 0.03365084287479925, 0.038643314285837886, 0.043613488107613944, 0.04847267147053222, 0.05313415213236526, 0.057514745860270125, 0.06153628085539417, 0.06512699273047746, 0.06822280514704357, 0.07076847325917777, 0.07271856955911099, 0.0740382945321723] + [0.07470409765495255] * 2 + [0.0740382945321723, 0.07271856955911099, 0.07076847325917777, 0.06822280514704358, 0.06512699273047745, 0.061536280855394185, 0.057514745860270146, 0.05313415213236527, 0.048472671470532226, 0.043613488107613944, 0.038643314285837886, 0.03365084287479925, 0.028725164645101876, 0.023954178441446212, 0.019423022625663207, 0.015212555780630606, 0.011397913786945825, 0.0080471690213567, 0.005220115603585847, 0.002967202368847464, 0.0013286326071879858, 0.0003336466348226595, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00043885690998005225, -0.0008698824080047974, -0.0012853848338508001, -0.001677949536885403, -0.0020405711906829236, -0.0023667788032406783, -0.0026507511919845726, -0.0028874208629100406, -0.0030725644401326086, -0.003202878032130608, -0.003276036189767646, -0.0032907334039875436, -0.0032467074026543614, -0.0031447438308048856, -0.0029866622307943326, -0.002775283572519913, -0.002514379913146187, -0.002208607084655601, -0.0018634216104164636, -0.0014849833333941663, -0.0010800454936075402, -0.0006558342164007376, -0.0002199195620652614, 0.00021991956206526055, 0.0006558342164007368, 0.0010800454936075409, 0.001484983333394164, 0.0018634216104164618, 0.0022086070846556016, 0.002514379913146186, 0.002775283572519912, 0.0029866622307943326, 0.0031447438308048856, 0.0032467074026543614, 0.0032907334039875436, 0.003276036189767646, 0.003202878032130608, 0.0030725644401326095, 0.0028874208629100415, 0.0026507511919845743, 0.0023667788032406796, 0.0020405711906829227, 0.0016779495368854044, 0.0012853848338508012, 0.0008698824080047984, 0.0004388569099800533, -2.1179439050938372e-18],
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00033364663482265527, -0.0013286326071879817, -0.0029672023688474595, -0.005220115603585839, -0.008047169021356708, -0.011397913786945808, -0.01521255578063058, -0.019423022625663183, -0.02395417844144619, -0.028725164645101872, -0.03365084287479925, -0.038643314285837886, -0.043613488107613944, -0.04847267147053222, -0.05313415213236526, -0.057514745860270125, -0.06153628085539417, -0.06512699273047746, -0.06822280514704357, -0.07076847325917777, -0.07271856955911099, -0.0740382945321723] + [-0.07470409765495255] * 2 + [-0.0740382945321723, -0.07271856955911099, -0.07076847325917777, -0.06822280514704358, -0.06512699273047745, -0.061536280855394185, -0.057514745860270146, -0.05313415213236527, -0.048472671470532226, -0.043613488107613944, -0.038643314285837886, -0.03365084287479925, -0.028725164645101876, -0.023954178441446212, -0.019423022625663207, -0.015212555780630606, -0.011397913786945825, -0.0080471690213567, -0.005220115603585847, -0.002967202368847464, -0.0013286326071879858, -0.00033364663482265955, 2.5937332241468132e-34],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004388569099800523, 0.0008698824080047976, 0.0012853848338508006, 0.0016779495368854037, 0.0020405711906829244, 0.0023667788032406796, 0.0026507511919845743, 0.002887420862910043, 0.0030725644401326116, 0.0032028780321306113, 0.0032760361897676503, 0.0032907334039875484, 0.0032467074026543666, 0.0031447438308048917, 0.002986662230794339, 0.00277528357251992, 0.0025143799131461943, 0.002208607084655609, 0.001863421610416472, 0.001484983333394175, 0.0010800454936075491, 0.0006558342164007467, 0.00021991956206527055, -0.0002199195620652514, -0.0006558342164007277, -0.001080045493607532, -0.0014849833333941554, -0.0018634216104164534, -0.0022086070846555938, -0.0025143799131461786, -0.002775283572519905, -0.002986662230794326, -0.0031447438308048795, -0.003246707402654356, -0.003290733403987539, -0.0032760361897676417, -0.0032028780321306043, -0.0030725644401326064, -0.0028874208629100393, -0.0026507511919845726, -0.0023667788032406783, -0.002040571190682922, -0.0016779495368854037, -0.0012853848338508008, -0.0008698824080047982, -0.0004388569099800532, 2.1179439050938372e-18],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008777138199601045, 0.001739764816009595, 0.0025707696677016007, 0.0033558990737708066, 0.004081142381365848, 0.004733557606481358, 0.005301502383969147, 0.005774841725820084, 0.00614512888026522, 0.006405756064261219, 0.006552072379535296, 0.006581466807975092, 0.006493414805308728, 0.006289487661609777, 0.005973324461588672, 0.005550567145039833, 0.005028759826292382, 0.00441721416931121, 0.0037268432208329354, 0.0029699666667883412, 0.0021600909872150896, 0.0013116684328014843, 0.00043983912413053195, -0.00043983912413051194, -0.0013116684328014646, -0.0021600909872150726, -0.0029699666667883195, -0.0037268432208329154, -0.004417214169311195, -0.005028759826292364, -0.005550567145039817, -0.005973324461588658, -0.006289487661609765, -0.006493414805308718, -0.006581466807975083, -0.006552072379535288, -0.006405756064261212, -0.006145128880265216, -0.00577484172582008, -0.005301502383969147, -0.0047335576064813575, -0.0040811423813658446, -0.0033558990737708083, -0.002570769667701602, -0.0017397648160095967, -0.0008777138199601066, 4.2358878101876744e-18],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006672932696453106, 0.0026572652143759634, 0.005934404737694919, 0.010440231207171679, 0.016094338042713416, 0.022795827573891616, 0.03042511156126116, 0.038846045251326365, 0.04790835688289238, 0.057450329290203744, 0.0673016857495985, 0.07728662857167577, 0.08722697621522789, 0.09694534294106444, 0.10626830426473052, 0.11502949172054025, 0.12307256171078834, 0.13025398546095493, 0.13644561029408714, 0.14153694651835555, 0.14543713911822198, 0.1480765890643446] + [0.1494081953099051] * 2 + [0.1480765890643446, 0.14543713911822198, 0.14153694651835555, 0.13644561029408717, 0.1302539854609549, 0.12307256171078837, 0.11502949172054029, 0.10626830426473054, 0.09694534294106445, 0.08722697621522789, 0.07728662857167577, 0.0673016857495985, 0.05745032929020375, 0.047908356882892425, 0.038846045251326414, 0.030425111561261212, 0.02279582757389165, 0.0160943380427134, 0.010440231207171694, 0.005934404737694928, 0.0026572652143759716, 0.000667293269645319, -2.5937332241468132e-34],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00043885690998005225, 0.0008698824080047975, 0.0012853848338508003, 0.0016779495368854033, 0.002040571190682924, 0.002366778803240679, 0.0026507511919845734, 0.002887420862910042, 0.00307256444013261, 0.0032028780321306095, 0.003276036189767648, 0.003290733403987546, 0.003246707402654364, 0.0031447438308048886, 0.002986662230794336, 0.0027752835725199164, 0.002514379913146191, 0.002208607084655605, 0.0018634216104164677, 0.0014849833333941706, 0.0010800454936075448, 0.0006558342164007422, 0.00021991956206526597, -0.00021991956206525597, -0.0006558342164007323, -0.0010800454936075363, -0.0014849833333941598, -0.0018634216104164577, -0.0022086070846555977, -0.002514379913146182, -0.0027752835725199086, -0.002986662230794329, -0.0031447438308048825, -0.003246707402654359, -0.0032907334039875414, -0.003276036189767644, -0.003202878032130606, -0.003072564440132608, -0.00288742086291004, -0.0026507511919845734, -0.0023667788032406788, -0.0020405711906829223, -0.0016779495368854042, -0.001285384833850801, -0.0008698824080047983, -0.0004388569099800533, 2.1179439050938372e-18],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003336466348226553, 0.0013286326071879817, 0.0029672023688474595, 0.005220115603585839, 0.008047169021356708, 0.011397913786945808, 0.01521255578063058, 0.019423022625663183, 0.02395417844144619, 0.028725164645101872, 0.03365084287479925, 0.038643314285837886, 0.043613488107613944, 0.04847267147053222, 0.05313415213236526, 0.057514745860270125, 0.06153628085539417, 0.06512699273047746, 0.06822280514704357, 0.07076847325917777, 0.07271856955911099, 0.0740382945321723] + [0.07470409765495255] * 2 + [0.0740382945321723, 0.07271856955911099, 0.07076847325917777, 0.06822280514704358, 0.06512699273047745, 0.061536280855394185, 0.057514745860270146, 0.05313415213236527, 0.048472671470532226, 0.043613488107613944, 0.038643314285837886, 0.03365084287479925, 0.028725164645101876, 0.023954178441446212, 0.019423022625663207, 0.015212555780630606, 0.011397913786945825, 0.0080471690213567, 0.005220115603585847, 0.002967202368847464, 0.0013286326071879858, 0.0003336466348226595, -1.2968666120734066e-34],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00043885690998005225, -0.0008698824080047973, -0.0012853848338508, -0.0016779495368854029, -0.002040571190682923, -0.0023667788032406775, -0.0026507511919845717, -0.0028874208629100393, -0.0030725644401326073, -0.003202878032130606, -0.003276036189767644, -0.0032907334039875414, -0.003246707402654359, -0.0031447438308048825, -0.002986662230794329, -0.0027752835725199094, -0.002514379913146183, -0.0022086070846555972, -0.0018634216104164594, -0.001484983333394162, -0.0010800454936075357, -0.000655834216400733, -0.0002199195620652568, 0.00021991956206526513, 0.0006558342164007414, 0.0010800454936075454, 0.0014849833333941684, 0.001863421610416466, 0.0022086070846556055, 0.00251437991314619, 0.0027752835725199155, 0.002986662230794336, 0.0031447438308048886, 0.003246707402654364, 0.003290733403987546, 0.003276036189767648, 0.0032028780321306095, 0.0030725644401326108, 0.002887420862910043, 0.002650751191984575, 0.0023667788032406805, 0.002040571190682923, 0.0016779495368854046, 0.0012853848338508014, 0.0008698824080047986, 0.0004388569099800533, -2.1179439050938372e-18],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003336466348226553, -0.0013286326071879817, -0.0029672023688474595, -0.005220115603585839, -0.008047169021356708, -0.011397913786945808, -0.01521255578063058, -0.019423022625663183, -0.02395417844144619, -0.028725164645101872, -0.03365084287479925, -0.038643314285837886, -0.043613488107613944, -0.04847267147053222, -0.05313415213236526, -0.057514745860270125, -0.06153628085539417, -0.06512699273047746, -0.06822280514704357, -0.07076847325917777, -0.07271856955911099, -0.0740382945321723] + [-0.07470409765495255] * 2 + [-0.0740382945321723, -0.07271856955911099, -0.07076847325917777, -0.06822280514704358, -0.06512699273047745, -0.061536280855394185, -0.057514745860270146, -0.05313415213236527, -0.048472671470532226, -0.043613488107613944, -0.038643314285837886, -0.03365084287479925, -0.028725164645101876, -0.023954178441446212, -0.019423022625663207, -0.015212555780630606, -0.011397913786945825, -0.0080471690213567, -0.005220115603585847, -0.002967202368847464, -0.0013286326071879858, -0.0003336466348226595, -1.2968666120734066e-34],
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.05874563732883068,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001338376776782979, 0.005329623741843514, 0.011902516998535683, 0.02093976311097909, 0.03228009220820085, 0.045721135848803655, 0.0610230382905967, 0.07791273672199743, 0.09608883407437308, 0.11522697745987073, 0.13498564625638523, 0.15501224655115117, 0.17494940318746952, 0.1944413371328451, 0.2131402143642502, 0.23071235297450587, 0.24684417773382034, 0.26124781584719364, 0.273666234051264, 0.28387782537898215, 0.2917003637411878, 0.296994255755488] + [0.299665031793473] * 2 + [0.296994255755488, 0.2917003637411878, 0.2838778253789822, 0.27366623405126406, 0.2612478158471936, 0.2468441777338204, 0.23071235297450593, 0.21314021436425026, 0.19444133713284512, 0.17494940318746952, 0.15501224655115117, 0.13498564625638523, 0.11522697745987075, 0.09608883407437316, 0.07791273672199753, 0.0610230382905968, 0.045721135848803725, 0.032280092208200814, 0.020939763110979125, 0.0119025169985357, 0.0053296237418435305, 0.0013383767767829956, 0.0],
        },
        "q4.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0019460019684250582, -0.003857277485621928, -0.0056997197947072755, -0.007440450469027202, -0.009048406128459795, -0.010494892766169302, -0.011754097793837893, -0.0128035506679157, -0.013624523877002805, -0.014202367134733834, -0.01452676881448521, -0.014591939960596559, -0.014396717592421586, -0.013944585457745276, -0.013243611865222143, -0.01230630570521713, -0.011149393228360723, -0.009793519565210188, -0.008262880313405696, -0.006584789766657208, -0.00478919349052615, -0.0029081339430985635, -0.0009751786765614058, 0.0009751786765614021, 0.0029081339430985604, 0.004789193490526152, 0.006584789766657199, 0.008262880313405687, 0.00979351956521019, 0.01114939322836072, 0.012306305705217128, 0.013243611865222143, 0.013944585457745276, 0.014396717592421586, 0.014591939960596559, 0.01452676881448521, 0.014202367134733834, 0.013624523877002807, 0.012803550667915706, 0.0117540977938379, 0.010494892766169309, 0.00904840612845979, 0.007440450469027208, 0.005699719794707281, 0.003857277485621933, 0.0019460019684250625, -9.391496213455544e-18],
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.05076885771950357,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q0.wf": {
            "type": "arbitrary",
            "samples": [0.1582597749869456] * 34 + [0.0] * 2,
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q1.wf": {
            "type": "arbitrary",
            "samples": [0.13336658450497493] * 33 + [0.0] * 3,
        },
        "q3.z.Cz_unipolar.flux_pulse_control_q2.wf": {
            "type": "arbitrary",
            "samples": [0.05985679743848572] * 27 + [0.0],
        },
        "q4.z.Cz_unipolar.flux_pulse_control_q2.wf": {
            "type": "arbitrary",
            "samples": [0.05821385620271752] * 32 + [0.0] * 4,
        },
        "twpa.const.wf.I": {
            "type": "constant",
            "sample": 0.954992586021436,
        },
        "twpa.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q0.resonator.readout.iw1": {
            "cosine": [(-0.8609312725526928, 2000)],
            "sine": [(0.5087212831608298, 2000)],
        },
        "q0.resonator.readout.iw2": {
            "cosine": [(-0.5087212831608298, 2000)],
            "sine": [(-0.8609312725526928, 2000)],
        },
        "q0.resonator.readout.iw3": {
            "cosine": [(0.5087212831608298, 2000)],
            "sine": [(0.8609312725526928, 2000)],
        },
        "q1.resonator.readout.iw1": {
            "cosine": [(-0.9402280715861902, 2000)],
            "sine": [(0.34054540578506437, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.34054540578506437, 2000)],
            "sine": [(-0.9402280715861902, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.34054540578506437, 2000)],
            "sine": [(0.9402280715861902, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.33859897789400223, 2000)],
            "sine": [(0.9409307796905876, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.9409307796905876, 2000)],
            "sine": [(-0.33859897789400223, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.9409307796905876, 2000)],
            "sine": [(0.33859897789400223, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9483381547556964, 2000)],
            "sine": [(0.3172613185286868, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(-0.3172613185286868, 2000)],
            "sine": [(0.9483381547556964, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(0.3172613185286868, 2000)],
            "sine": [(-0.9483381547556964, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(0.9743052291294593, 2000)],
            "sine": [(-0.22523170400943088, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.22523170400943088, 2000)],
            "sine": [(0.9743052291294593, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.22523170400943088, 2000)],
            "sine": [(-0.9743052291294593, 2000)],
        },
    },
    "mixers": {},
    "oscillators": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 174,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 172,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 174,
                            "shareable": False,
                            "filter": {
                                "feedforward": [0.930566753281534, -1.99, 1.5555096131158408, -0.5663963111589002, 0.025217290417050606, 0.06075559088850318, 0.03375358974167169, -0.07057910169815002, 0.034284390746336005, 0.0020385711162261132, 0.003614667597226243, -0.034421462769617994, 0.022513274875880437, 0.04552318000189783, -0.06044323534122823, 0.01960355211152274, -0.025801154962076748, 0.020784734817433544, 0.02640072988181348, -0.04036221849512527, 0.0430548424440775, -0.04112524269212112, -0.012927313928236006, 0.06353596748352627, -0.053949828249563535, 0.014346142950503217, 0.04516400193430306, -0.08431492230979887, 0.055842531915586587, -0.01282744479378403],
                                "feedback": [0.9556355411471746, 0.5045807850848327],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 175,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 170,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -8,
                            "band": 3,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7550000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4560000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 1,
                            "delay": 20,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4710000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4980000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5690000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5660000000.0,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6000000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6125000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7550000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "q0.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q0.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q0.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q0.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q0.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q0.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q0.xy.-y90_DragCosine.pulse",
                "x180_Square": "q0.xy.x180_Square.pulse",
                "x90_Square": "q0.xy.x90_Square.pulse",
                "-x90_Square": "q0.xy.-x90_Square.pulse",
                "y180_Square": "q0.xy.y180_Square.pulse",
                "y90_Square": "q0.xy.y90_Square.pulse",
                "-y90_Square": "q0.xy.-y90_Square.pulse",
                "x180": "q0.xy.x180_DragCosine.pulse",
                "x90": "q0.xy.x90_DragCosine.pulse",
                "-x90": "q0.xy.-x90_DragCosine.pulse",
                "y180": "q0.xy.y180_DragCosine.pulse",
                "y90": "q0.xy.y90_DragCosine.pulse",
                "-y90": "q0.xy.-y90_DragCosine.pulse",
                "saturation": "q0.xy.saturation.pulse",
                "EF_x180": "q0.xy.EF_x180.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -34697346.90529516,
        },
        "q0.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q0.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 1),
            },
        },
        "q0.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q0.resonator.readout.pulse",
                "const": "q0.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "intermediate_frequency": -301969911.0,
        },
        "q1.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
                "EF_x180": "q1.xy.EF_x180.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -38385086.07454129,
        },
        "q1.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 2),
            },
        },
        "q1.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "intermediate_frequency": -174879836.0,
        },
        "q2.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
                "EF_x180": "q2.xy.EF_x180.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 267804596.93315327,
        },
        "q2.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q2.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q0": "q2.z.Cz_unipolar.flux_pulse_control_q0.pulse",
                "Cz_unipolar.flux_pulse_control_q1": "q2.z.Cz_unipolar.flux_pulse_control_q1.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 3),
            },
        },
        "q2.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "intermediate_frequency": -40794189.0,
        },
        "q3.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
                "EF_x180": "q3.xy.EF_x180.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 185345952.95870727,
        },
        "q3.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q3.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q2": "q3.z.Cz_unipolar.flux_pulse_control_q2.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 4),
            },
        },
        "q3.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "intermediate_frequency": 126195431.0,
        },
        "q4.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
                "EF_x180": "q4.xy.EF_x180.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 231635990.26926282,
        },
        "q4.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q4.z.const.pulse",
                "Cz_unipolar.flux_pulse_control_q2": "q4.z.Cz_unipolar.flux_pulse_control_q2.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 2, 5),
            },
        },
        "q4.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 376,
            "intermediate_frequency": 348301377.0,
        },
        "twpa": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "twpa.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 1000,
            },
            "thread": "twpa",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q0.xy.x180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.x180_DragCosine.wf.I",
                "Q": "q0.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.x90_DragCosine.wf.I",
                "Q": "q0.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.-x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.-x90_DragCosine.wf.I",
                "Q": "q0.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.y180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.y180_DragCosine.wf.I",
                "Q": "q0.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.y90_DragCosine.wf.I",
                "Q": "q0.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.-y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.-y90_DragCosine.wf.I",
                "Q": "q0.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.x180_Square.wf.I",
                "Q": "q0.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.x90_Square.wf.I",
                "Q": "q0.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.-x90_Square.wf.I",
                "Q": "q0.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.y180_Square.wf.I",
                "Q": "q0.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.y90_Square.wf.I",
                "Q": "q0.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q0.xy.-y90_Square.wf.I",
                "Q": "q0.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q0.xy.saturation.wf.I",
                "Q": "q0.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.xy.EF_x180.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q0.xy.EF_x180.wf.I",
                "Q": "q0.xy.EF_x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q0.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q0.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q0.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q0.resonator.readout.wf.I",
                "Q": "q0.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q0.resonator.readout.iw1",
                "iw2": "q0.resonator.readout.iw2",
                "iw3": "q0.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q0.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q0.resonator.const.wf.I",
                "Q": "q0.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.EF_x180.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q1.xy.EF_x180.wf.I",
                "Q": "q1.xy.EF_x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q1.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.EF_x180.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q2.xy.EF_x180.wf.I",
                "Q": "q2.xy.EF_x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q2.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.EF_x180.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q3.xy.EF_x180.wf.I",
                "Q": "q3.xy.EF_x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q3.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.EF_x180.pulse": {
            "length": 48,
            "waveforms": {
                "I": "q4.xy.EF_x180.wf.I",
                "Q": "q4.xy.EF_x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.resonator.readout.pulse": {
            "length": 2000,
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q4.resonator.const.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q0.pulse": {
            "length": 36,
            "waveforms": {
                "single": "q2.z.Cz_unipolar.flux_pulse_control_q0.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q1.pulse": {
            "length": 36,
            "waveforms": {
                "single": "q2.z.Cz_unipolar.flux_pulse_control_q1.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.z.Cz_unipolar.flux_pulse_control_q2.pulse": {
            "length": 28,
            "waveforms": {
                "single": "q3.z.Cz_unipolar.flux_pulse_control_q2.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.z.Cz_unipolar.flux_pulse_control_q2.pulse": {
            "length": 36,
            "waveforms": {
                "single": "q4.z.Cz_unipolar.flux_pulse_control_q2.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "twpa.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "twpa.const.wf.I",
                "Q": "twpa.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001084800925224461, 0.0004319845402687823, 0.0009647403987050108, 0.0016972406269161174, 0.002616413740976422, 0.0037058570748899036, 0.004946129486553483, 0.006315098285398428, 0.007788334190777875, 0.009339547273058718, 0.010941056098038743, 0.01256428170279573, 0.01418025758795786, 0.015760146625571233, 0.017275755658331376, 0.01870003860714324, 0.02000757910904339, 0.021175044072799208, 0.022181600058474703, 0.023009285050659755, 0.02364332899106059, 0.02407241735053998] + [0.02428889303715773] * 2 + [0.02407241735053998, 0.02364332899106059, 0.02300928505065976, 0.022181600058474707, 0.021175044072799205, 0.020007579109043397, 0.018700038607143248, 0.01727575565833138, 0.015760146625571236, 0.01418025758795786, 0.01256428170279573, 0.010941056098038743, 0.00933954727305872, 0.007788334190777881, 0.0063150982853984365, 0.004946129486553492, 0.003705857074889909, 0.0026164137409764193, 0.0016972406269161202, 0.0009647403987050122, 0.00043198454026878365, 0.00010848009252244746, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.993916645243644e-05, -0.00011880871705954394, -0.00017555812329609315, -0.00022917469066337438, -0.0002787016302465185, -0.00032325513263534926, -0.000362040139524246, -0.00039436453154644246, -0.00041965147916052343, -0.0004374497361872568, -0.00044744169230835184, -0.0004494490408301139, -0.0004434359605706172, -0.00042950975508954483, -0.0004079189378536246, -0.0003790487975079273, -0.00034341452239086836, -0.00030165200698610334, -0.00025450650437040264, -0.00020281932715484106, -0.00014751283424132203, -8.957397130612306e-05, -3.003665873091936e-05, 3.0036658730919247e-05, 8.957397130612294e-05, 0.0001475128342413221, 0.00020281932715484079, 0.0002545065043704024, 0.0003016520069861034, 0.0003434145223908683, 0.0003790487975079272, 0.0004079189378536245, 0.00042950975508954483, 0.0004434359605706172, 0.0004494490408301139, 0.00044744169230835184, 0.0004374497361872568, 0.00041965147916052354, 0.0003943645315464426, 0.0003620401395242462, 0.0003232551326353495, 0.00027870163024651834, 0.0002291746906633745, 0.00017555812329609328, 0.00011880871705954408, 5.993916645243658e-05, -2.892692113931008e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.424004626122305e-05, 0.00021599227013439115, 0.0004823701993525054, 0.0008486203134580587, 0.001308206870488211, 0.0018529285374449518, 0.0024730647432767414, 0.003157549142699214, 0.0038941670953889377, 0.004669773636529359, 0.005470528049019372, 0.006282140851397865, 0.00709012879397893, 0.007880073312785616, 0.008637877829165688, 0.00935001930357162, 0.010003789554521695, 0.010587522036399604, 0.011090800029237352, 0.011504642525329878, 0.011821664495530295, 0.01203620867526999] + [0.012144446518578865] * 2 + [0.01203620867526999, 0.011821664495530295, 0.01150464252532988, 0.011090800029237353, 0.010587522036399602, 0.010003789554521698, 0.009350019303571624, 0.00863787782916569, 0.007880073312785618, 0.00709012879397893, 0.006282140851397865, 0.005470528049019372, 0.00466977363652936, 0.0038941670953889407, 0.0031575491426992183, 0.002473064743276746, 0.0018529285374449544, 0.0013082068704882096, 0.0008486203134580601, 0.0004823701993525061, 0.00021599227013439183, 5.424004626122373e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -2.996958322621822e-05, -5.940435852977197e-05, -8.777906164804657e-05, -0.00011458734533168719, -0.00013935081512325925, -0.00016162756631767463, -0.000181020069762123, -0.00019718226577322123, -0.00020982573958026172, -0.0002187248680936284, -0.00022372084615417592, -0.00022472452041505695, -0.0002217179802853086, -0.00021475487754477241, -0.0002039594689268123, -0.00018952439875396366, -0.00017170726119543418, -0.00015082600349305167, -0.00012725325218520132, -0.00010140966357742053, -7.375641712066101e-05, -4.478698565306153e-05, -1.501832936545968e-05, 1.5018329365459623e-05, 4.478698565306147e-05, 7.375641712066105e-05, 0.00010140966357742039, 0.0001272532521852012, 0.0001508260034930517, 0.00017170726119543415, 0.0001895243987539636, 0.00020395946892681226, 0.00021475487754477241, 0.0002217179802853086, 0.00022472452041505695, 0.00022372084615417592, 0.0002187248680936284, 0.00020982573958026177, 0.0001971822657732213, 0.0001810200697621231, 0.00016162756631767474, 0.00013935081512325917, 0.00011458734533168726, 8.777906164804664e-05, 5.940435852977204e-05, 2.996958322621829e-05, -1.446346056965504e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -5.4240046261223045e-05, -0.00021599227013439115, -0.0004823701993525054, -0.0008486203134580587, -0.001308206870488211, -0.0018529285374449518, -0.0024730647432767414, -0.003157549142699214, -0.0038941670953889377, -0.004669773636529359, -0.005470528049019372, -0.006282140851397865, -0.00709012879397893, -0.007880073312785616, -0.008637877829165688, -0.00935001930357162, -0.010003789554521695, -0.010587522036399604, -0.011090800029237352, -0.011504642525329878, -0.011821664495530295, -0.01203620867526999] + [-0.012144446518578865] * 2 + [-0.01203620867526999, -0.011821664495530295, -0.01150464252532988, -0.011090800029237353, -0.010587522036399602, -0.010003789554521698, -0.009350019303571624, -0.00863787782916569, -0.007880073312785618, -0.00709012879397893, -0.006282140851397865, -0.005470528049019372, -0.00466977363652936, -0.0038941670953889407, -0.0031575491426992183, -0.002473064743276746, -0.0018529285374449544, -0.0013082068704882096, -0.0008486203134580601, -0.0004823701993525061, -0.00021599227013439183, -5.4240046261223736e-05, 1.7712630691222e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.9969583226218226e-05, 5.9404358529771995e-05, 8.777906164804663e-05, 0.0001145873453316873, 0.00013935081512325942, 0.00016162756631767485, 0.0001810200697621233, 0.0001971822657732216, 0.0002098257395802622, 0.00021872486809362896, 0.0002237208461541766, 0.0002247245204150577, 0.00022171798028530946, 0.0002147548775447734, 0.00020395946892681334, 0.0001895243987539648, 0.0001717072611954354, 0.00015082600349305297, 0.00012725325218520268, 0.00010140966357742194, 7.375641712066246e-05, 4.478698565306301e-05, 1.5018329365461167e-05, -1.5018329365458136e-05, -4.478698565305999e-05, -7.37564171206596e-05, -0.00010140966357741898, -0.00012725325218519986, -0.0001508260034930504, -0.00017170726119543293, -0.00018952439875396246, -0.0002039594689268112, -0.00021475487754477144, -0.00022171798028530773, -0.0002247245204150562, -0.00022372084615417524, -0.00021872486809362783, -0.00020982573958026128, -0.00019718226577322093, -0.0001810200697621228, -0.00016162756631767452, -0.000139350815123259, -0.00011458734533168715, -8.777906164804659e-05, -5.9404358529772015e-05, -2.9969583226218284e-05, 1.446346056965504e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.9939166452436446e-05, 0.00011880871705954396, 0.0001755581232960932, 0.00022917469066337449, 0.00027870163024651867, 0.0003232551326353495, 0.0003620401395242463, 0.00039436453154644284, 0.0004196514791605239, 0.0004374497361872574, 0.0004474416923083525, 0.00044944904083011467, 0.00044343596057061805, 0.0004295097550895458, 0.00040791893785362566, 0.00037904879750792845, 0.0003434145223908696, 0.00030165200698610464, 0.000254506504370404, 0.00020281932715484247, 0.00014751283424132346, 8.957397130612454e-05, 3.0036658730920846e-05, -3.003665873091776e-05, -8.957397130612146e-05, -0.00014751283424132067, -0.00020281932715483938, -0.00025450650437040107, -0.0003016520069861021, -0.00034341452239086706, -0.00037904879750792607, -0.00040791893785362344, -0.00042950975508954385, -0.0004434359605706163, -0.00044944904083011315, -0.0004474416923083512, -0.0004374497361872562, -0.00041965147916052305, -0.00039436453154644225, -0.0003620401395242459, -0.00032325513263534926, -0.0002787016302465182, -0.0002291746906633744, -0.00017555812329609323, -0.00011880871705954406, -5.9939166452436575e-05, 2.892692113931008e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001084800925224461, 0.0004319845402687823, 0.0009647403987050108, 0.0016972406269161174, 0.002616413740976422, 0.0037058570748899036, 0.004946129486553483, 0.006315098285398428, 0.007788334190777875, 0.009339547273058718, 0.010941056098038743, 0.01256428170279573, 0.01418025758795786, 0.015760146625571233, 0.017275755658331376, 0.01870003860714324, 0.02000757910904339, 0.021175044072799208, 0.022181600058474703, 0.023009285050659755, 0.02364332899106059, 0.02407241735053998] + [0.02428889303715773] * 2 + [0.02407241735053998, 0.02364332899106059, 0.02300928505065976, 0.022181600058474707, 0.021175044072799205, 0.020007579109043397, 0.018700038607143248, 0.01727575565833138, 0.015760146625571236, 0.01418025758795786, 0.01256428170279573, 0.010941056098038743, 0.00933954727305872, 0.007788334190777881, 0.0063150982853984365, 0.004946129486553492, 0.003705857074889909, 0.0026164137409764193, 0.0016972406269161202, 0.0009647403987050122, 0.00043198454026878365, 0.00010848009252244746, -1.7712630691222e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.9969583226218223e-05, 5.940435852977198e-05, 8.77790616480466e-05, 0.00011458734533168724, 0.00013935081512325934, 0.00016162756631767474, 0.00018102006976212316, 0.00019718226577322142, 0.00020982573958026196, 0.0002187248680936287, 0.00022372084615417625, 0.00022472452041505733, 0.00022171798028530903, 0.0002147548775447729, 0.00020395946892681283, 0.00018952439875396423, 0.0001717072611954348, 0.00015082600349305232, 0.000127253252185202, 0.00010140966357742123, 7.375641712066173e-05, 4.478698565306227e-05, 1.5018329365460423e-05, -1.501832936545888e-05, -4.478698565306073e-05, -7.375641712066034e-05, -0.00010140966357741969, -0.00012725325218520053, -0.00015082600349305105, -0.00017170726119543353, -0.00018952439875396303, -0.00020395946892681172, -0.00021475487754477193, -0.00022171798028530816, -0.00022472452041505657, -0.0002237208461541756, -0.0002187248680936281, -0.00020982573958026153, -0.00019718226577322112, -0.00018102006976212294, -0.00016162756631767463, -0.0001393508151232591, -0.0001145873453316872, -8.777906164804661e-05, -5.940435852977203e-05, -2.9969583226218287e-05, 1.446346056965504e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.424004626122305e-05, 0.00021599227013439115, 0.0004823701993525054, 0.0008486203134580587, 0.001308206870488211, 0.0018529285374449518, 0.0024730647432767414, 0.003157549142699214, 0.0038941670953889377, 0.004669773636529359, 0.005470528049019372, 0.006282140851397865, 0.00709012879397893, 0.007880073312785616, 0.008637877829165688, 0.00935001930357162, 0.010003789554521695, 0.010587522036399604, 0.011090800029237352, 0.011504642525329878, 0.011821664495530295, 0.01203620867526999] + [0.012144446518578865] * 2 + [0.01203620867526999, 0.011821664495530295, 0.01150464252532988, 0.011090800029237353, 0.010587522036399602, 0.010003789554521698, 0.009350019303571624, 0.00863787782916569, 0.007880073312785618, 0.00709012879397893, 0.006282140851397865, 0.005470528049019372, 0.00466977363652936, 0.0038941670953889407, 0.0031575491426992183, 0.002473064743276746, 0.0018529285374449544, 0.0013082068704882096, 0.0008486203134580601, 0.0004823701993525061, 0.00021599227013439183, 5.424004626122373e-05, -8.856315345611e-36],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -2.9969583226218216e-05, -5.9404358529771954e-05, -8.777906164804655e-05, -0.00011458734533168713, -0.00013935081512325917, -0.00016162756631767452, -0.00018102006976212283, -0.00019718226577322104, -0.00020982573958026147, -0.0002187248680936281, -0.0002237208461541756, -0.00022472452041505657, -0.00022171798028530816, -0.00021475487754477193, -0.00020395946892681175, -0.0001895243987539631, -0.00017170726119543356, -0.00015082600349305102, -0.00012725325218520064, -0.00010140966357741982, -7.37564171206603e-05, -4.478698565306079e-05, -1.5018329365458936e-05, 1.5018329365460367e-05, 4.478698565306221e-05, 7.375641712066177e-05, 0.0001014096635774211, 0.0001272532521852019, 0.00015082600349305235, 0.00017170726119543478, 0.00018952439875396417, 0.0002039594689268128, 0.0002147548775447729, 0.00022171798028530903, 0.00022472452041505733, 0.00022372084615417625, 0.0002187248680936287, 0.00020982573958026201, 0.0001971822657732215, 0.00018102006976212327, 0.00016162756631767485, 0.00013935081512325925, 0.00011458734533168731, 8.777906164804667e-05, 5.9404358529772056e-05, 2.9969583226218294e-05, -1.446346056965504e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.424004626122305e-05, -0.00021599227013439115, -0.0004823701993525054, -0.0008486203134580587, -0.001308206870488211, -0.0018529285374449518, -0.0024730647432767414, -0.003157549142699214, -0.0038941670953889377, -0.004669773636529359, -0.005470528049019372, -0.006282140851397865, -0.00709012879397893, -0.007880073312785616, -0.008637877829165688, -0.00935001930357162, -0.010003789554521695, -0.010587522036399604, -0.011090800029237352, -0.011504642525329878, -0.011821664495530295, -0.01203620867526999] + [-0.012144446518578865] * 2 + [-0.01203620867526999, -0.011821664495530295, -0.01150464252532988, -0.011090800029237353, -0.010587522036399602, -0.010003789554521698, -0.009350019303571624, -0.00863787782916569, -0.007880073312785618, -0.00709012879397893, -0.006282140851397865, -0.005470528049019372, -0.00466977363652936, -0.0038941670953889407, -0.0031575491426992183, -0.002473064743276746, -0.0018529285374449544, -0.0013082068704882096, -0.0008486203134580601, -0.0004823701993525061, -0.00021599227013439183, -5.424004626122373e-05, -8.856315345611e-36],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q0.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q0.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q0.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q0.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q0.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q0.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q0.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q0.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.012252345344633875,
        },
        "q0.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 8.075257200585712e-05, 0.0003215692564629215, 0.0007181526739320024, 0.001263425783933129, 0.0019476581749005714, 0.0027586397036077496, 0.0036818983854623737, 0.004700958647414346, 0.005797635334947146, 0.0069523582265909965, 0.008144521264988623, 0.009352850272476954, 0.010555782589291511, 0.011731851859740742, 0.012860071099831885, 0.013920307210497503, 0.014893640253225308, 0.015762701076809136, 0.016511981270263695, 0.01712810991078602, 0.017600092168189623, 0.017919505507909675] + [0.018080649991331826] * 2 + [0.017919505507909675, 0.017600092168189623, 0.017128109910786022, 0.0165119812702637, 0.015762701076809136, 0.014893640253225312, 0.013920307210497506, 0.012860071099831887, 0.011731851859740744, 0.010555782589291511, 0.009352850272476954, 0.008144521264988623, 0.006952358226590997, 0.005797635334947151, 0.004700958647414352, 0.0036818983854623798, 0.0027586397036077535, 0.0019476581749005694, 0.0012634257839331312, 0.0007181526739320034, 0.0003215692564629225, 8.075257200585813e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.2202485249474724e-05, -8.365186614987714e-05, -0.0001236084775170855, -0.00016135929267466228, -0.00019623064743178707, -0.0002276002616367013, -0.0002549083437807583, -0.0002776675804911569, -0.0002954718326496237, -0.0003080033829546004, -0.0003150386055940164, -0.0003164519568532043, -0.00031221821544546064, -0.0003024129325865059, -0.00028721108378124957, -0.00026688394638176, -0.0002417942586364898, -0.00021238974661763916, -0.00017919513453879029, -0.0001428027810388851, -0.00010386210852828016, -6.30680142304493e-05, -2.1148469724566943e-05, 2.114846972456686e-05, 6.306801423044923e-05, 0.00010386210852828022, 0.0001428027810388849, 0.00017919513453879012, 0.0002123897466176392, 0.00024179425863648976, 0.0002668839463817599, 0.00028721108378124957, 0.0003024129325865059, 0.00031221821544546064, 0.0003164519568532043, 0.0003150386055940164, 0.0003080033829546004, 0.0002954718326496238, 0.00027766758049115704, 0.00025490834378075845, 0.00022760026163670146, 0.00019623064743178698, 0.00016135929267466236, 0.00012360847751708562, 8.365186614987723e-05, 4.220248524947482e-05, -2.03671161103514e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q0.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q0.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.012326234261830727,
        },
        "q0.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q0.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q0.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 8.852263618998774e-05, 0.0003525108562200021, 0.000787253784049609, 0.0013849934218324387, 0.002135063091571541, 0.0030240777822409426, 0.004036173005624497, 0.005153287898483947, 0.00635548751909127, 0.007621318586736088, 0.008928192316028191, 0.010252787514307945, 0.011571466748881805, 0.012860698157568703, 0.014097475375338174, 0.015259728083439316, 0.016326715854761795, 0.017279398267248947, 0.018100774680680467, 0.018776187613499914, 0.019293584305920285, 0.019643731801707986] + [0.019820381710505545] * 2 + [0.019643731801707986, 0.019293584305920285, 0.018776187613499914, 0.01810077468068047, 0.017279398267248943, 0.016326715854761798, 0.015259728083439322, 0.014097475375338175, 0.012860698157568707, 0.011571466748881805, 0.010252787514307945, 0.008928192316028191, 0.007621318586736089, 0.006355487519091275, 0.005153287898483953, 0.004036173005624504, 0.003024077782240947, 0.002135063091571539, 0.0013849934218324409, 0.0007872537840496101, 0.0003525108562200032, 8.852263618998885e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.7220298797756847e-05, -9.359795024479807e-05, -0.00013830534405234428, -0.000180544675718762, -0.00021956218336979558, -0.00025466159865707047, -0.0002852165716832647, -0.0003106818482308651, -0.000330602999836596, -0.00034462453307811244, -0.00035249623336254315, -0.00035407763001182857, -0.00034934050296529806, -0.00033836938636732164, -0.00032136006005350083, -0.0002986160558548641, -0.00027054324106515166, -0.0002376425757293432, -0.00020050117299978755, -0.0001597818220880897, -0.00011621116077592803, -7.056670854662671e-05, -2.366299173155436e-05, 2.366299173155427e-05, 7.056670854662665e-05, 0.00011621116077592811, 0.00015978182208808945, 0.00020050117299978738, 0.00023764257572934323, 0.00027054324106515155, 0.00029861605585486406, 0.0003213600600535008, 0.00033836938636732164, 0.00034934050296529806, 0.00035407763001182857, 0.00035249623336254315, 0.00034462453307811244, 0.00033060299983659605, 0.0003106818482308652, 0.0002852165716832649, 0.00025466159865707063, 0.00021956218336979545, 0.00018054467571876207, 0.0001383053440523444, 9.359795024479818e-05, 4.722029879775695e-05, -2.2788736319536312e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.426131809499387e-05, 0.00017625542811000106, 0.0003936268920248045, 0.0006924967109162194, 0.0010675315457857706, 0.0015120388911204713, 0.0020180865028122485, 0.0025766439492419736, 0.003177743759545635, 0.003810659293368044, 0.004464096158014096, 0.005126393757153972, 0.005785733374440902, 0.006430349078784352, 0.007048737687669087, 0.007629864041719658, 0.008163357927380897, 0.008639699133624473, 0.009050387340340233, 0.009388093806749957, 0.009646792152960142, 0.009821865900853993] + [0.009910190855252772] * 2 + [0.009821865900853993, 0.009646792152960142, 0.009388093806749957, 0.009050387340340235, 0.008639699133624472, 0.008163357927380899, 0.007629864041719661, 0.007048737687669088, 0.006430349078784353, 0.005785733374440902, 0.005126393757153972, 0.004464096158014096, 0.0038106592933680444, 0.0031777437595456376, 0.0025766439492419767, 0.002018086502812252, 0.0015120388911204735, 0.0010675315457857695, 0.0006924967109162204, 0.00039362689202480504, 0.0001762554281100016, 4.4261318094994425e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -2.3610149398878423e-05, -4.6798975122399034e-05, -6.915267202617214e-05, -9.0272337859381e-05, -0.00010978109168489779, -0.00012733079932853523, -0.00014260828584163236, -0.00015534092411543255, -0.000165301499918298, -0.00017231226653905622, -0.00017624811668127158, -0.00017703881500591429, -0.00017467025148264903, -0.00016918469318366082, -0.00016068003002675041, -0.00014930802792743206, -0.00013527162053257583, -0.0001188212878646716, -0.00010025058649989377, -7.989091104404485e-05, -5.8105580387964014e-05, -3.528335427331336e-05, -1.183149586577718e-05, 1.1831495865777136e-05, 3.528335427331332e-05, 5.8105580387964055e-05, 7.989091104404473e-05, 0.00010025058649989369, 0.00011882128786467161, 0.00013527162053257578, 0.00014930802792743203, 0.0001606800300267504, 0.00016918469318366082, 0.00017467025148264903, 0.00017703881500591429, 0.00017624811668127158, 0.00017231226653905622, 0.00016530149991829802, 0.0001553409241154326, 0.00014260828584163244, 0.00012733079932853532, 0.00010978109168489772, 9.027233785938104e-05, 6.91526720261722e-05, 4.679897512239909e-05, 2.3610149398878474e-05, -1.1394368159768156e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -4.426131809499387e-05, -0.00017625542811000106, -0.0003936268920248045, -0.0006924967109162194, -0.0010675315457857706, -0.0015120388911204713, -0.0020180865028122485, -0.0025766439492419736, -0.003177743759545635, -0.003810659293368044, -0.004464096158014096, -0.005126393757153972, -0.005785733374440902, -0.006430349078784352, -0.007048737687669087, -0.007629864041719658, -0.008163357927380897, -0.008639699133624473, -0.009050387340340233, -0.009388093806749957, -0.009646792152960142, -0.009821865900853993] + [-0.009910190855252772] * 2 + [-0.009821865900853993, -0.009646792152960142, -0.009388093806749957, -0.009050387340340235, -0.008639699133624472, -0.008163357927380899, -0.007629864041719661, -0.007048737687669088, -0.006430349078784353, -0.005785733374440902, -0.005126393757153972, -0.004464096158014096, -0.0038106592933680444, -0.0031777437595456376, -0.0025766439492419767, -0.002018086502812252, -0.0015120388911204735, -0.0010675315457857695, -0.0006924967109162204, -0.00039362689202480504, -0.0001762554281100016, -4.4261318094994425e-05, 1.395407649516659e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.361014939887843e-05, 4.6798975122399055e-05, 6.91526720261722e-05, 9.027233785938108e-05, 0.00010978109168489793, 0.00012733079932853542, 0.0001426082858416326, 0.00015534092411543287, 0.00016530149991829838, 0.00017231226653905668, 0.00017624811668127212, 0.0001770388150059149, 0.00017467025148264973, 0.0001691846931836616, 0.00016068003002675128, 0.00014930802792743298, 0.00013527162053257683, 0.00011882128786467266, 0.00010025058649989488, 7.9890911044046e-05, 5.810558038796519e-05, 3.528335427331456e-05, 1.1831495865778393e-05, -1.1831495865775923e-05, -3.528335427331212e-05, -5.8105580387962876e-05, -7.989091104404357e-05, -0.00010025058649989258, -0.00011882128786467056, -0.00013527162053257477, -0.0001493080279274311, -0.00016068003002674952, -0.00016918469318366003, -0.00017467025148264832, -0.00017703881500591366, -0.00017624811668127103, -0.00017231226653905576, -0.00016530149991829764, -0.00015534092411543228, -0.0001426082858416322, -0.00012733079932853513, -0.00010978109168489759, -9.027233785938095e-05, -6.915267202617214e-05, -4.679897512239907e-05, -2.3610149398878467e-05, 1.1394368159768156e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.722029879775685e-05, 9.35979502447981e-05, 0.00013830534405234434, 0.00018054467571876207, 0.00021956218336979572, 0.00025466159865707063, 0.000285216571683265, 0.0003106818482308654, 0.00033060299983659637, 0.00034462453307811293, 0.0003524962333625437, 0.0003540776300118292, 0.00034934050296529876, 0.00033836938636732245, 0.0003213600600535017, 0.00029861605585486503, 0.00027054324106515264, 0.00023764257572934426, 0.00020050117299978866, 0.00015978182208809083, 0.00011621116077592921, 7.056670854662792e-05, 2.3662991731555572e-05, -2.366299173155306e-05, -7.056670854662544e-05, -0.00011621116077592693, -0.0001597818220880883, -0.00020050117299978627, -0.00023764257572934217, -0.0002705432410651506, -0.00029861605585486314, -0.0003213600600534999, -0.0003383693863673208, -0.00034934050296529735, -0.0003540776300118279, -0.0003524962333625426, -0.00034462453307811195, -0.00033060299983659567, -0.0003106818482308649, -0.0002852165716832646, -0.00025466159865707047, -0.0002195621833697953, -0.000180544675718762, -0.00013830534405234434, -9.359795024479815e-05, -4.722029879775694e-05, 2.2788736319536312e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 8.852263618998774e-05, 0.0003525108562200021, 0.000787253784049609, 0.0013849934218324387, 0.002135063091571541, 0.0030240777822409426, 0.004036173005624497, 0.005153287898483947, 0.00635548751909127, 0.007621318586736088, 0.008928192316028191, 0.010252787514307945, 0.011571466748881805, 0.012860698157568703, 0.014097475375338174, 0.015259728083439316, 0.016326715854761795, 0.017279398267248947, 0.018100774680680467, 0.018776187613499914, 0.019293584305920285, 0.019643731801707986] + [0.019820381710505545] * 2 + [0.019643731801707986, 0.019293584305920285, 0.018776187613499914, 0.01810077468068047, 0.017279398267248943, 0.016326715854761798, 0.015259728083439322, 0.014097475375338175, 0.012860698157568707, 0.011571466748881805, 0.010252787514307945, 0.008928192316028191, 0.007621318586736089, 0.006355487519091275, 0.005153287898483953, 0.004036173005624504, 0.003024077782240947, 0.002135063091571539, 0.0013849934218324409, 0.0007872537840496101, 0.0003525108562200032, 8.852263618998885e-05, -1.395407649516659e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.3610149398878427e-05, 4.679897512239905e-05, 6.915267202617217e-05, 9.027233785938104e-05, 0.00010978109168489786, 0.00012733079932853532, 0.0001426082858416325, 0.0001553409241154327, 0.00016530149991829819, 0.00017231226653905646, 0.00017624811668127185, 0.0001770388150059146, 0.00017467025148264938, 0.00016918469318366123, 0.00016068003002675085, 0.00014930802792743252, 0.00013527162053257632, 0.00011882128786467213, 0.00010025058649989433, 7.989091104404542e-05, 5.8105580387964604e-05, 3.528335427331396e-05, 1.1831495865777786e-05, -1.183149586577653e-05, -3.528335427331272e-05, -5.8105580387963465e-05, -7.989091104404416e-05, -0.00010025058649989314, -0.00011882128786467108, -0.0001352716205325753, -0.00014930802792743157, -0.00016068003002674995, -0.0001691846931836604, -0.00017467025148264868, -0.00017703881500591396, -0.0001762481166812713, -0.00017231226653905598, -0.00016530149991829783, -0.00015534092411543244, -0.0001426082858416323, -0.00012733079932853523, -0.00010978109168489765, -9.0272337859381e-05, -6.915267202617217e-05, -4.6798975122399075e-05, -2.361014939887847e-05, 1.1394368159768156e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.426131809499387e-05, 0.00017625542811000106, 0.0003936268920248045, 0.0006924967109162194, 0.0010675315457857706, 0.0015120388911204713, 0.0020180865028122485, 0.0025766439492419736, 0.003177743759545635, 0.003810659293368044, 0.004464096158014096, 0.005126393757153972, 0.005785733374440902, 0.006430349078784352, 0.007048737687669087, 0.007629864041719658, 0.008163357927380897, 0.008639699133624473, 0.009050387340340233, 0.009388093806749957, 0.009646792152960142, 0.009821865900853993] + [0.009910190855252772] * 2 + [0.009821865900853993, 0.009646792152960142, 0.009388093806749957, 0.009050387340340235, 0.008639699133624472, 0.008163357927380899, 0.007629864041719661, 0.007048737687669088, 0.006430349078784353, 0.005785733374440902, 0.005126393757153972, 0.004464096158014096, 0.0038106592933680444, 0.0031777437595456376, 0.0025766439492419767, 0.002018086502812252, 0.0015120388911204735, 0.0010675315457857695, 0.0006924967109162204, 0.00039362689202480504, 0.0001762554281100016, 4.4261318094994425e-05, -6.977038247583294e-36],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -2.361014939887842e-05, -4.679897512239902e-05, -6.915267202617211e-05, -9.027233785938095e-05, -0.00010978109168489772, -0.00012733079932853515, -0.00014260828584163222, -0.00015534092411543238, -0.0001653014999182978, -0.00017231226653905598, -0.0001762481166812713, -0.00017703881500591396, -0.00017467025148264868, -0.0001691846931836604, -0.00016068003002674998, -0.0001493080279274316, -0.00013527162053257534, -0.00011882128786467107, -0.00010025058649989322, -7.989091104404428e-05, -5.8105580387963425e-05, -3.5283354273312754e-05, -1.1831495865776573e-05, 1.1831495865777742e-05, 3.5283354273313926e-05, 5.8105580387964644e-05, 7.98909110440453e-05, 0.00010025058649989425, 0.00011882128786467214, 0.00013527162053257626, 0.0001493080279274325, 0.00016068003002675082, 0.00016918469318366123, 0.00017467025148264938, 0.0001770388150059146, 0.00017624811668127185, 0.00017231226653905646, 0.0001653014999182982, 0.00015534092411543276, 0.00014260828584163258, 0.0001273307993285354, 0.00010978109168489779, 9.027233785938108e-05, 6.915267202617222e-05, 4.67989751223991e-05, 2.3610149398878478e-05, -1.1394368159768156e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -4.426131809499387e-05, -0.00017625542811000106, -0.0003936268920248045, -0.0006924967109162194, -0.0010675315457857706, -0.0015120388911204713, -0.0020180865028122485, -0.0025766439492419736, -0.003177743759545635, -0.003810659293368044, -0.004464096158014096, -0.005126393757153972, -0.005785733374440902, -0.006430349078784352, -0.007048737687669087, -0.007629864041719658, -0.008163357927380897, -0.008639699133624473, -0.009050387340340233, -0.009388093806749957, -0.009646792152960142, -0.009821865900853993] + [-0.009910190855252772] * 2 + [-0.009821865900853993, -0.009646792152960142, -0.009388093806749957, -0.009050387340340235, -0.008639699133624472, -0.008163357927380899, -0.007629864041719661, -0.007048737687669088, -0.006430349078784353, -0.005785733374440902, -0.005126393757153972, -0.004464096158014096, -0.0038106592933680444, -0.0031777437595456376, -0.0025766439492419767, -0.002018086502812252, -0.0015120388911204735, -0.0010675315457857695, -0.0006924967109162204, -0.00039362689202480504, -0.0001762554281100016, -4.4261318094994425e-05, -6.977038247583294e-36],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.006053569048419676,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.35962527755611e-05, 0.00029307168422793825, 0.0006545097500833932, 0.0011514605794941091, 0.0017750560731362678, 0.002514168154652574, 0.0033556073514384773, 0.004284358161093272, 0.00528384700341615, 0.006336237976337529, 0.007422751138014025, 0.008523997635335545, 0.009620325698468372, 0.010692171327153404, 0.011720407410754268, 0.012686685051999737, 0.013573761003490246, 0.01436580537385623, 0.015048684112544617, 0.01561021123228583, 0.016040366268325255, 0.016331473093854205] + [0.01647833690067467] * 2 + [0.016331473093854205, 0.016040366268325255, 0.015610211232285832, 0.015048684112544623, 0.014365805373856228, 0.01357376100349025, 0.012686685051999741, 0.01172040741075427, 0.010692171327153405, 0.009620325698468372, 0.008523997635335545, 0.007422751138014025, 0.00633623797633753, 0.005283847003416155, 0.004284358161093277, 0.003355607351438483, 0.0025141681546525774, 0.0017750560731362658, 0.0011514605794941109, 0.0006545097500833941, 0.00029307168422793917, 7.359625277556202e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -5.13971009767718e-05, -0.00010187701946899316, -0.000150538940135279, -0.00019651448984851706, -0.0002389832338348936, -0.00027718731635186856, -0.00031044498464185503, -0.0003381627548263294, -0.0003598460026397035, -0.00037510779001106206, -0.00038367576998320457, -0.0003853970467505492, -0.0003802409040884047, -0.0003682993534847284, -0.0003497854921929434, -0.0003250297005064032, -0.0002944737461142297, -0.0002586629007464352, -0.00021823620978698278, -0.00017391508849376978, -0.00012649044832626033, -7.680858311175474e-05, -2.5756066911990623e-05, 2.5756066911990528e-05, 7.680858311175466e-05, 0.0001264904483262604, 0.00017391508849376954, 0.0002182362097869826, 0.00025866290074643523, 0.0002944737461142296, 0.0003250297005064031, 0.0003497854921929434, 0.0003682993534847284, 0.0003802409040884047, 0.0003853970467505492, 0.00038367576998320457, 0.00037510779001106206, 0.00035984600263970354, 0.0003381627548263295, 0.0003104449846418552, 0.0002771873163518688, 0.00023898323383489346, 0.00019651448984851717, 0.00015053894013527912, 0.00010187701946899331, 5.139710097677191e-05, -2.4804480521497145e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.01650896347294208,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002569747209338718, 0.0010233131637525828, 0.0022853400007891342, 0.00402053433323864, 0.006197931577131021, 0.00877867602706552, 0.011716714237194083, 0.014959616846053556, 0.018449514179763045, 0.022124128937725293, 0.025917887532531245, 0.029763090252180772, 0.03359111936304718, 0.03733366359495935, 0.040923937157436314, 0.04429787153370051, 0.047395258784877506, 0.050160825962091586, 0.05254522145354784, 0.054505895665213897, 0.05600786031933331, 0.057024312821071114] + [0.05753711455145361] * 2 + [0.057024312821071114, 0.05600786031933331, 0.0545058956652139, 0.052545221453547855, 0.05016082596209158, 0.04739525878487752, 0.04429787153370052, 0.04092393715743632, 0.037333663594959356, 0.03359111936304718, 0.029763090252180772, 0.025917887532531245, 0.022124128937725297, 0.01844951417976306, 0.014959616846053575, 0.011716714237194103, 0.008778676027065533, 0.006197931577131014, 0.004020534333238646, 0.0022853400007891373, 0.001023313163752586, 0.00025697472093387497, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00027342744852201155, -0.0005419755777475313, -0.0008008521399485067, -0.0010454374767395614, -0.001271366956991325, -0.0014746088637763361, -0.0016515363404531259, -0.0017989921120089077, -0.001914344826706976, -0.0019955360126207877, -0.002041116811114255, -0.0020502738317584343, -0.002022843667302995, -0.001959315809682478, -0.0018608239150211235, -0.0017291255735124803, -0.0015665709451807616, -0.0013760608212195374, -0.0011609948593041652, -0.0009252109166200308, -0.0006729165632101575, -0.0004086139977881113, -0.00013701970589529013, 0.00013701970589528962, 0.00040861399778811087, 0.0006729165632101581, 0.0009252109166200296, 0.0011609948593041641, 0.0013760608212195376, 0.0015665709451807613, 0.0017291255735124799, 0.0018608239150211233, 0.001959315809682478, 0.002022843667302995, 0.0020502738317584343, 0.002041116811114255, 0.0019955360126207877, 0.0019143448267069764, 0.0017989921120089084, 0.001651536340453127, 0.001474608863776337, 0.0012713669569913244, 0.001045437476739562, 0.0008008521399485073, 0.000541975577747532, 0.0002734274485220122, -1.3195736125218487e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001284873604669359, 0.0005116565818762914, 0.0011426700003945671, 0.00201026716661932, 0.0030989657885655106, 0.00438933801353276, 0.005858357118597042, 0.007479808423026778, 0.009224757089881522, 0.011062064468862647, 0.012958943766265623, 0.014881545126090386, 0.01679555968152359, 0.018666831797479674, 0.020461968578718157, 0.022148935766850255, 0.023697629392438753, 0.025080412981045793, 0.02627261072677392, 0.027252947832606948, 0.028003930159666655, 0.028512156410535557] + [0.028768557275726806] * 2 + [0.028512156410535557, 0.028003930159666655, 0.02725294783260695, 0.026272610726773928, 0.02508041298104579, 0.02369762939243876, 0.02214893576685026, 0.02046196857871816, 0.018666831797479678, 0.01679555968152359, 0.014881545126090386, 0.012958943766265623, 0.011062064468862648, 0.00922475708988153, 0.007479808423026787, 0.005858357118597051, 0.0043893380135327665, 0.003098965788565507, 0.002010267166619323, 0.0011426700003945686, 0.000511656581876293, 0.00012848736046693749, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00013671372426100577, -0.00027098778887376567, -0.00040042606997425334, -0.0005227187383697807, -0.0006356834784956625, -0.0007373044318881681, -0.0008257681702265629, -0.0008994960560044539, -0.000957172413353488, -0.0009977680063103938, -0.0010205584055571276, -0.0010251369158792171, -0.0010114218336514974, -0.000979657904841239, -0.0009304119575105617, -0.0008645627867562402, -0.0007832854725903808, -0.0006880304106097687, -0.0005804974296520826, -0.0004626054583100154, -0.00033645828160507876, -0.00020430699889405565, -6.850985294764507e-05, 6.850985294764481e-05, 0.00020430699889405543, 0.00033645828160507903, 0.0004626054583100148, 0.0005804974296520821, 0.0006880304106097688, 0.0007832854725903807, 0.0008645627867562399, 0.0009304119575105616, 0.000979657904841239, 0.0010114218336514974, 0.0010251369158792171, 0.0010205584055571276, 0.0009977680063103938, 0.0009571724133534882, 0.0008994960560044542, 0.0008257681702265635, 0.0007373044318881685, 0.0006356834784956622, 0.000522718738369781, 0.00040042606997425366, 0.000270987788873766, 0.0001367137242610061, -6.597868062609244e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00012848736046693586, -0.0005116565818762914, -0.0011426700003945671, -0.00201026716661932, -0.0030989657885655106, -0.00438933801353276, -0.005858357118597042, -0.007479808423026778, -0.009224757089881522, -0.011062064468862647, -0.012958943766265623, -0.014881545126090386, -0.01679555968152359, -0.018666831797479674, -0.020461968578718157, -0.022148935766850255, -0.023697629392438753, -0.025080412981045793, -0.02627261072677392, -0.027252947832606948, -0.028003930159666655, -0.028512156410535557] + [-0.028768557275726806] * 2 + [-0.028512156410535557, -0.028003930159666655, -0.02725294783260695, -0.026272610726773928, -0.02508041298104579, -0.02369762939243876, -0.02214893576685026, -0.02046196857871816, -0.018666831797479678, -0.01679555968152359, -0.014881545126090386, -0.012958943766265623, -0.011062064468862648, -0.00922475708988153, -0.007479808423026787, -0.005858357118597051, -0.0043893380135327665, -0.003098965788565507, -0.002010267166619323, -0.0011426700003945686, -0.000511656581876293, -0.0001284873604669375, 8.080058004070959e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001367137242610058, 0.0002709877888737657, 0.0004004260699742535, 0.0005227187383697809, 0.000635683478495663, 0.0007373044318881686, 0.0008257681702265637, 0.0008994960560044547, 0.0009571724133534891, 0.0009977680063103951, 0.001020558405557129, 0.0010251369158792189, 0.0010114218336514994, 0.0009796579048412413, 0.0009304119575105642, 0.0008645627867562429, 0.0007832854725903837, 0.0006880304106097717, 0.0005804974296520859, 0.0004626054583100188, 0.00033645828160508217, 0.00020430699889405915, 6.850985294764859e-05, -6.850985294764129e-05, -0.00020430699889405194, -0.0003364582816050756, -0.00046260545831001146, -0.0005804974296520788, -0.0006880304106097658, -0.0007832854725903777, -0.0008645627867562372, -0.0009304119575105591, -0.0009796579048412365, -0.0010114218336514955, -0.0010251369158792154, -0.001020558405557126, -0.0009977680063103925, -0.0009571724133534871, -0.0008994960560044533, -0.0008257681702265627, -0.000737304431888168, -0.0006356834784956618, -0.0005227187383697808, -0.0004004260699742535, -0.00027098778887376594, -0.00013671372426100607, 6.597868062609244e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00027342744852201155, 0.0005419755777475314, 0.0008008521399485068, 0.0010454374767395616, 0.0012713669569913255, 0.0014746088637763366, 0.0016515363404531265, 0.0017989921120089086, 0.001914344826706977, 0.001995536012620789, 0.002041116811114257, 0.002050273831758436, 0.002022843667302997, 0.00195931580968248, 0.001860823915021126, 0.0017291255735124831, 0.0015665709451807644, 0.0013760608212195404, 0.0011609948593041684, 0.0009252109166200342, 0.000672916563210161, 0.00040861399778811477, 0.00013701970589529366, -0.0001370197058952861, -0.0004086139977881074, -0.0006729165632101546, -0.0009252109166200263, -0.0011609948593041609, -0.0013760608212195346, -0.0015665709451807585, -0.001729125573512477, -0.0018608239150211207, -0.0019593158096824757, -0.0020228436673029927, -0.0020502738317584326, -0.0020411168111142534, -0.0019955360126207864, -0.0019143448267069753, -0.0017989921120089075, -0.0016515363404531263, -0.0014746088637763366, -0.001271366956991324, -0.0010454374767395619, -0.0008008521399485072, -0.0005419755777475319, -0.0002734274485220122, 1.3195736125218487e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002569747209338718, 0.0010233131637525828, 0.0022853400007891342, 0.00402053433323864, 0.006197931577131021, 0.00877867602706552, 0.011716714237194083, 0.014959616846053556, 0.018449514179763045, 0.022124128937725293, 0.025917887532531245, 0.029763090252180772, 0.03359111936304718, 0.03733366359495935, 0.040923937157436314, 0.04429787153370051, 0.047395258784877506, 0.050160825962091586, 0.05254522145354784, 0.054505895665213897, 0.05600786031933331, 0.057024312821071114] + [0.05753711455145361] * 2 + [0.057024312821071114, 0.05600786031933331, 0.0545058956652139, 0.052545221453547855, 0.05016082596209158, 0.04739525878487752, 0.04429787153370052, 0.04092393715743632, 0.037333663594959356, 0.03359111936304718, 0.029763090252180772, 0.025917887532531245, 0.022124128937725297, 0.01844951417976306, 0.014959616846053575, 0.011716714237194103, 0.008778676027065533, 0.006197931577131014, 0.004020534333238646, 0.0022853400007891373, 0.001023313163752586, 0.00025697472093387497, -8.080058004070959e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00013671372426100577, 0.0002709877888737657, 0.0004004260699742534, 0.0005227187383697808, 0.0006356834784956627, 0.0007373044318881683, 0.0008257681702265633, 0.0008994960560044543, 0.0009571724133534885, 0.0009977680063103945, 0.0010205584055571284, 0.001025136915879218, 0.0010114218336514985, 0.00097965790484124, 0.000930411957510563, 0.0008645627867562416, 0.0007832854725903822, 0.0006880304106097702, 0.0005804974296520842, 0.0004626054583100171, 0.0003364582816050805, 0.00020430699889405739, 6.850985294764683e-05, -6.850985294764305e-05, -0.0002043069988940537, -0.0003364582816050773, -0.00046260545831001314, -0.0005804974296520804, -0.0006880304106097673, -0.0007832854725903793, -0.0008645627867562385, -0.0009304119575105603, -0.0009796579048412378, -0.0010114218336514963, -0.0010251369158792163, -0.0010205584055571267, -0.0009977680063103932, -0.0009571724133534877, -0.0008994960560044537, -0.0008257681702265632, -0.0007373044318881683, -0.000635683478495662, -0.0005227187383697809, -0.0004004260699742536, -0.00027098778887376594, -0.0001367137242610061, 6.597868062609244e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001284873604669359, 0.0005116565818762914, 0.0011426700003945671, 0.00201026716661932, 0.0030989657885655106, 0.00438933801353276, 0.005858357118597042, 0.007479808423026778, 0.009224757089881522, 0.011062064468862647, 0.012958943766265623, 0.014881545126090386, 0.01679555968152359, 0.018666831797479674, 0.020461968578718157, 0.022148935766850255, 0.023697629392438753, 0.025080412981045793, 0.02627261072677392, 0.027252947832606948, 0.028003930159666655, 0.028512156410535557] + [0.028768557275726806] * 2 + [0.028512156410535557, 0.028003930159666655, 0.02725294783260695, 0.026272610726773928, 0.02508041298104579, 0.02369762939243876, 0.02214893576685026, 0.02046196857871816, 0.018666831797479678, 0.01679555968152359, 0.014881545126090386, 0.012958943766265623, 0.011062064468862648, 0.00922475708988153, 0.007479808423026787, 0.005858357118597051, 0.0043893380135327665, 0.003098965788565507, 0.002010267166619323, 0.0011426700003945686, 0.000511656581876293, 0.00012848736046693749, -4.0400290020354793e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00013671372426100577, -0.0002709877888737656, -0.0004004260699742533, -0.0005227187383697806, -0.0006356834784956623, -0.0007373044318881678, -0.0008257681702265626, -0.0008994960560044534, -0.0009571724133534875, -0.0009977680063103932, -0.0010205584055571267, -0.0010251369158792163, -0.0010114218336514963, -0.0009796579048412378, -0.0009304119575105604, -0.0008645627867562388, -0.0007832854725903794, -0.0006880304106097672, -0.000580497429652081, -0.00046260545831001374, -0.000336458281605077, -0.00020430699889405392, -6.85098529476433e-05, 6.850985294764657e-05, 0.00020430699889405717, 0.00033645828160508076, 0.0004626054583100165, 0.0005804974296520837, 0.0006880304106097703, 0.0007832854725903821, 0.0008645627867562414, 0.0009304119575105629, 0.00097965790484124, 0.0010114218336514985, 0.001025136915879218, 0.0010205584055571284, 0.0009977680063103945, 0.0009571724133534888, 0.0008994960560044546, 0.0008257681702265638, 0.0007373044318881687, 0.0006356834784956624, 0.0005227187383697811, 0.0004004260699742537, 0.00027098778887376605, 0.0001367137242610061, -6.597868062609244e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001284873604669359, -0.0005116565818762914, -0.0011426700003945671, -0.00201026716661932, -0.0030989657885655106, -0.00438933801353276, -0.005858357118597042, -0.007479808423026778, -0.009224757089881522, -0.011062064468862647, -0.012958943766265623, -0.014881545126090386, -0.01679555968152359, -0.018666831797479674, -0.020461968578718157, -0.022148935766850255, -0.023697629392438753, -0.025080412981045793, -0.02627261072677392, -0.027252947832606948, -0.028003930159666655, -0.028512156410535557] + [-0.028768557275726806] * 2 + [-0.028512156410535557, -0.028003930159666655, -0.02725294783260695, -0.026272610726773928, -0.02508041298104579, -0.02369762939243876, -0.02214893576685026, -0.02046196857871816, -0.018666831797479678, -0.01679555968152359, -0.014881545126090386, -0.012958943766265623, -0.011062064468862648, -0.00922475708988153, -0.007479808423026787, -0.005858357118597051, -0.0043893380135327665, -0.003098965788565507, -0.002010267166619323, -0.0011426700003945686, -0.000511656581876293, -0.00012848736046693749, -4.0400290020354793e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.0192265628415506,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001602185393266137, 0.0006380150536765267, 0.0014248632529319527, 0.0025067218123364, 0.0038642849402675903, 0.005473326890546326, 0.007305134271450967, 0.009327018436872956, 0.011502898815981004, 0.013793946771862364, 0.016159278499468407, 0.018556684598084253, 0.020943383299084496, 0.023276783907607835, 0.0255152468345159, 0.027618826655847837, 0.02954998493985725, 0.031274260121216, 0.03276088246846389, 0.033983323170595575, 0.03491976774432133, 0.035553505314038246] + [0.0358732268178012] * 2 + [0.035553505314038246, 0.03491976774432133, 0.033983323170595575, 0.0327608824684639, 0.031274260121215994, 0.029549984939857256, 0.027618826655847844, 0.025515246834515903, 0.023276783907607842, 0.020943383299084496, 0.018556684598084253, 0.016159278499468407, 0.013793946771862365, 0.011502898815981013, 0.009327018436872966, 0.007305134271450979, 0.0054733268905463334, 0.0038642849402675864, 0.002506721812336404, 0.0014248632529319546, 0.0006380150536765286, 0.0001602185393266157, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.000214939951450731, -0.00042604429437580177, -0.0006295458667745597, -0.000821813178266507, -0.000999415214123173, -0.0011591826618072248, -0.00129826446742978, -0.0014141787128745943, -0.0015048569056856458, -0.0015686808913640152, -0.001604511729373253, -0.001611710017560237, -0.0015901473023017397, -0.0015402083707623784, -0.001462784384358549, -0.0013592569759618357, -0.001231473594627688, -0.001081714537823258, -0.0009126522594650794, -0.0007273036799156127, -0.0005289763489679071, -0.00032120942254118805, -0.00010771050635962845, 0.00010771050635962804, 0.00032120942254118773, 0.0005289763489679074, 0.0007273036799156117, 0.0009126522594650787, 0.0010817145378232583, 0.0012314735946276877, 0.0013592569759618355, 0.0014627843843585486, 0.0015402083707623784, 0.0015901473023017397, 0.001611710017560237, 0.001604511729373253, 0.0015686808913640152, 0.0015048569056856462, 0.0014141787128745947, 0.0012982644674297806, 0.0011591826618072257, 0.0009994152141231723, 0.0008218131782665075, 0.0006295458667745601, 0.0004260442943758023, 0.00021493995145073152, -1.0373102252324863e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0204578599682783,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004110178090848037, 0.0016367366137989116, 0.003655283433034376, 0.006430637250981682, 0.009913271813010206, 0.014041039422855405, 0.018740279969730957, 0.023927135394750807, 0.029509046139976576, 0.035386402875921784, 0.041454324032396336, 0.04760452741261123, 0.05372726249154549, 0.059713268916665244, 0.06545572626150312, 0.07085216023869914, 0.07580627135608636, 0.08022965338340993, 0.08404337096360034, 0.08717936821609054, 0.08958168319561663, 0.09120744653445707] + [0.09202764644731523] * 2 + [0.09120744653445707, 0.08958168319561663, 0.08717936821609056, 0.08404337096360037, 0.08022965338340991, 0.07580627135608638, 0.07085216023869917, 0.06545572626150313, 0.05971326891666526, 0.05372726249154549, 0.04760452741261123, 0.041454324032396336, 0.035386402875921784, 0.0295090461399766, 0.02392713539475084, 0.01874027996973099, 0.014041039422855426, 0.009913271813010195, 0.006430637250981692, 0.0036552834330343814, 0.0016367366137989168, 0.0004110178090848089, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003687667501787422, -0.0007309528489642983, -0.0010800950768434922, -0.0014099629824884862, -0.00171467006530833, -0.001988778820191459, -0.002227397769913226, -0.0024262687536628596, -0.002581842914024005, -0.002691344026419398, -0.002752818040904213, -0.0027651679522336225, -0.0027281733759473782, -0.0026424944811357255, -0.00250966020970635, -0.00233204099237981, -0.002112806448297175, -0.0018558688230913636, -0.0015658131747711389, -0.0012478155532523196, -0.0009075506336244122, -0.0005510904514392059, -0.00018479604709249056, 0.00018479604709248988, 0.0005510904514392052, 0.0009075506336244128, 0.001247815553252318, 0.0015658131747711373, 0.0018558688230913638, 0.0021128064482971746, 0.002332040992379809, 0.0025096602097063494, 0.0026424944811357255, 0.0027281733759473782, 0.0027651679522336225, 0.002752818040904213, 0.002691344026419398, 0.0025818429140240053, 0.0024262687536628605, 0.0022273977699132272, 0.00198877882019146, 0.0017146700653083292, 0.0014099629824884871, 0.0010800950768434928, 0.0007309528489642991, 0.000368766750178743, -1.7796855266055385e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020550890454240186, 0.0008183683068994558, 0.001827641716517188, 0.003215318625490841, 0.004956635906505103, 0.007020519711427703, 0.009370139984865479, 0.011963567697375404, 0.014754523069988288, 0.017693201437960892, 0.020727162016198168, 0.023802263706305615, 0.026863631245772745, 0.029856634458332622, 0.03272786313075156, 0.03542608011934957, 0.03790313567804318, 0.04011482669170496, 0.04202168548180017, 0.04358968410804527, 0.044790841597808315, 0.04560372326722854] + [0.046013823223657616] * 2 + [0.04560372326722854, 0.044790841597808315, 0.04358968410804528, 0.042021685481800186, 0.040114826691704956, 0.03790313567804319, 0.035426080119349584, 0.032727863130751565, 0.02985663445833263, 0.026863631245772745, 0.023802263706305615, 0.020727162016198168, 0.017693201437960892, 0.0147545230699883, 0.01196356769737542, 0.009370139984865494, 0.007020519711427713, 0.004956635906505098, 0.003215318625490846, 0.0018276417165171907, 0.0008183683068994584, 0.00020550890454240444, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001843833750893711, -0.00036547642448214913, -0.0005400475384217461, -0.0007049814912442431, -0.000857335032654165, -0.0009943894100957295, -0.001113698884956613, -0.0012131343768314298, -0.0012909214570120025, -0.001345672013209699, -0.0013764090204521065, -0.0013825839761168112, -0.0013640866879736891, -0.0013212472405678627, -0.001254830104853175, -0.001166020496189905, -0.0010564032241485875, -0.0009279344115456818, -0.0007829065873855694, -0.0006239077766261598, -0.0004537753168122061, -0.0002755452257196029, -9.239802354624528e-05, 9.239802354624494e-05, 0.0002755452257196026, 0.0004537753168122064, 0.000623907776626159, 0.0007829065873855687, 0.0009279344115456819, 0.0010564032241485873, 0.0011660204961899045, 0.0012548301048531747, 0.0013212472405678627, 0.0013640866879736891, 0.0013825839761168112, 0.0013764090204521065, 0.001345672013209699, 0.0012909214570120027, 0.0012131343768314303, 0.0011136988849566136, 0.00099438941009573, 0.0008573350326541646, 0.0007049814912442436, 0.0005400475384217464, 0.00036547642448214957, 0.0001843833750893715, -8.898427633027693e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020550890454240183, -0.0008183683068994558, -0.001827641716517188, -0.003215318625490841, -0.004956635906505103, -0.007020519711427703, -0.009370139984865479, -0.011963567697375404, -0.014754523069988288, -0.017693201437960892, -0.020727162016198168, -0.023802263706305615, -0.026863631245772745, -0.029856634458332622, -0.03272786313075156, -0.03542608011934957, -0.03790313567804318, -0.04011482669170496, -0.04202168548180017, -0.04358968410804527, -0.044790841597808315, -0.04560372326722854] + [-0.046013823223657616] * 2 + [-0.04560372326722854, -0.044790841597808315, -0.04358968410804528, -0.042021685481800186, -0.040114826691704956, -0.03790313567804319, -0.035426080119349584, -0.032727863130751565, -0.02985663445833263, -0.026863631245772745, -0.023802263706305615, -0.020727162016198168, -0.017693201437960892, -0.0147545230699883, -0.01196356769737542, -0.009370139984865494, -0.007020519711427713, -0.004956635906505098, -0.003215318625490846, -0.0018276417165171907, -0.0008183683068994584, -0.00020550890454240446, 1.0897430918231721e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00018438337508937112, 0.00036547642448214924, 0.0005400475384217463, 0.0007049814912442436, 0.0008573350326541657, 0.0009943894100957304, 0.001113698884956614, 0.0012131343768314313, 0.0012909214570120042, 0.0013456720132097011, 0.001376409020452109, 0.001382583976116814, 0.0013640866879736924, 0.0013212472405678664, 0.0012548301048531788, 0.0011660204961899093, 0.001056403224148592, 0.0009279344115456867, 0.0007829065873855745, 0.0006239077766261651, 0.00045377531681221157, 0.0002755452257196085, 9.239802354625092e-05, -9.23980235462393e-05, -0.000275545225719597, -0.00045377531681220094, -0.0006239077766261537, -0.0007829065873855636, -0.000927934411545677, -0.0010564032241485828, -0.0011660204961899002, -0.0012548301048531708, -0.001321247240567859, -0.0013640866879736859, -0.0013825839761168084, -0.0013764090204521039, -0.0013456720132096968, -0.001290921457012001, -0.0012131343768314287, -0.0011136988849566125, -0.0009943894100957291, -0.000857335032654164, -0.0007049814912442431, -0.0005400475384217462, -0.00036547642448214946, -0.00018438337508937147, 8.898427633027693e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003687667501787422, 0.0007309528489642984, 0.0010800950768434924, 0.0014099629824884867, 0.0017146700653083307, 0.00198877882019146, 0.0022273977699132272, 0.002426268753662861, 0.0025818429140240066, 0.0026913440264194, 0.0027528180409042155, 0.0027651679522336255, 0.0027281733759473817, 0.002642494481135729, 0.0025096602097063538, 0.0023320409923798142, 0.00211280644829718, 0.0018558688230913686, 0.001565813174771144, 0.001247815553252325, 0.0009075506336244177, 0.0005510904514392115, 0.0001847960470924962, -0.00018479604709248425, -0.0005510904514391996, -0.0009075506336244073, -0.0012478155532523127, -0.0015658131747711321, -0.0018558688230913588, -0.00211280644829717, -0.0023320409923798047, -0.0025096602097063455, -0.002642494481135722, -0.0027281733759473748, -0.0027651679522336194, -0.0027528180409042103, -0.0026913440264193958, -0.0025818429140240036, -0.002426268753662859, -0.002227397769913226, -0.001988778820191459, -0.0017146700653083286, -0.0014099629824884867, -0.0010800950768434926, -0.000730952848964299, -0.000368766750178743, 1.7796855266055385e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004110178090848037, 0.0016367366137989116, 0.003655283433034376, 0.006430637250981682, 0.009913271813010206, 0.014041039422855405, 0.018740279969730957, 0.023927135394750807, 0.029509046139976576, 0.035386402875921784, 0.041454324032396336, 0.04760452741261123, 0.05372726249154549, 0.059713268916665244, 0.06545572626150312, 0.07085216023869914, 0.07580627135608636, 0.08022965338340993, 0.08404337096360034, 0.08717936821609054, 0.08958168319561663, 0.09120744653445707] + [0.09202764644731523] * 2 + [0.09120744653445707, 0.08958168319561663, 0.08717936821609056, 0.08404337096360037, 0.08022965338340991, 0.07580627135608638, 0.07085216023869917, 0.06545572626150313, 0.05971326891666526, 0.05372726249154549, 0.04760452741261123, 0.041454324032396336, 0.035386402875921784, 0.0295090461399766, 0.02392713539475084, 0.01874027996973099, 0.014041039422855426, 0.009913271813010195, 0.006430637250981692, 0.0036552834330343814, 0.0016367366137989168, 0.0004110178090848089, -1.0897430918231721e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001843833750893711, 0.0003654764244821492, 0.0005400475384217462, 0.0007049814912442433, 0.0008573350326541654, 0.00099438941009573, 0.0011136988849566136, 0.0012131343768314305, 0.0012909214570120033, 0.0013456720132097, 0.0013764090204521078, 0.0013825839761168128, 0.0013640866879736909, 0.0013212472405678645, 0.0012548301048531769, 0.0011660204961899071, 0.00105640322414859, 0.0009279344115456843, 0.000782906587385572, 0.0006239077766261625, 0.00045377531681220886, 0.00027554522571960575, 9.23980235462481e-05, -9.239802354624212e-05, -0.0002755452257195998, -0.00045377531681220365, -0.0006239077766261563, -0.0007829065873855661, -0.0009279344115456794, -0.001056403224148585, -0.0011660204961899024, -0.0012548301048531728, -0.001321247240567861, -0.0013640866879736874, -0.0013825839761168097, -0.0013764090204521052, -0.0013456720132096979, -0.0012909214570120018, -0.0012131343768314296, -0.001113698884956613, -0.0009943894100957295, -0.0008573350326541643, -0.0007049814912442433, -0.0005400475384217463, -0.0003654764244821495, -0.0001843833750893715, 8.898427633027693e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020550890454240186, 0.0008183683068994558, 0.001827641716517188, 0.003215318625490841, 0.004956635906505103, 0.007020519711427703, 0.009370139984865479, 0.011963567697375404, 0.014754523069988288, 0.017693201437960892, 0.020727162016198168, 0.023802263706305615, 0.026863631245772745, 0.029856634458332622, 0.03272786313075156, 0.03542608011934957, 0.03790313567804318, 0.04011482669170496, 0.04202168548180017, 0.04358968410804527, 0.044790841597808315, 0.04560372326722854] + [0.046013823223657616] * 2 + [0.04560372326722854, 0.044790841597808315, 0.04358968410804528, 0.042021685481800186, 0.040114826691704956, 0.03790313567804319, 0.035426080119349584, 0.032727863130751565, 0.02985663445833263, 0.026863631245772745, 0.023802263706305615, 0.020727162016198168, 0.017693201437960892, 0.0147545230699883, 0.01196356769737542, 0.009370139984865494, 0.007020519711427713, 0.004956635906505098, 0.003215318625490846, 0.0018276417165171907, 0.0008183683068994584, 0.00020550890454240444, -5.448715459115861e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0001843833750893711, -0.0003654764244821491, -0.000540047538421746, -0.0007049814912442429, -0.0008573350326541647, -0.0009943894100957291, -0.0011136988849566123, -0.0012131343768314292, -0.0012909214570120016, -0.0013456720132096979, -0.0013764090204521052, -0.0013825839761168097, -0.0013640866879736874, -0.001321247240567861, -0.001254830104853173, -0.0011660204961899028, -0.0010564032241485851, -0.0009279344115456793, -0.0007829065873855668, -0.0006239077766261571, -0.00045377531681220333, -0.0002755452257196001, -9.239802354624246e-05, 9.239802354624776e-05, 0.0002755452257196054, 0.0004537753168122092, 0.0006239077766261618, 0.0007829065873855713, 0.0009279344115456844, 0.0010564032241485897, 0.0011660204961899067, 0.0012548301048531767, 0.0013212472405678645, 0.0013640866879736909, 0.0013825839761168128, 0.0013764090204521078, 0.0013456720132097, 0.0012909214570120035, 0.001213134376831431, 0.0011136988849566143, 0.0009943894100957304, 0.0008573350326541649, 0.0007049814912442438, 0.0005400475384217465, 0.0003654764244821496, 0.0001843833750893715, -8.898427633027693e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020550890454240186, -0.0008183683068994558, -0.001827641716517188, -0.003215318625490841, -0.004956635906505103, -0.007020519711427703, -0.009370139984865479, -0.011963567697375404, -0.014754523069988288, -0.017693201437960892, -0.020727162016198168, -0.023802263706305615, -0.026863631245772745, -0.029856634458332622, -0.03272786313075156, -0.03542608011934957, -0.03790313567804318, -0.04011482669170496, -0.04202168548180017, -0.04358968410804527, -0.044790841597808315, -0.04560372326722854] + [-0.046013823223657616] * 2 + [-0.04560372326722854, -0.044790841597808315, -0.04358968410804528, -0.042021685481800186, -0.040114826691704956, -0.03790313567804319, -0.035426080119349584, -0.032727863130751565, -0.02985663445833263, -0.026863631245772745, -0.023802263706305615, -0.020727162016198168, -0.017693201437960892, -0.0147545230699883, -0.01196356769737542, -0.009370139984865494, -0.007020519711427713, -0.004956635906505098, -0.003215318625490846, -0.0018276417165171907, -0.0008183683068994584, -0.00020550890454240444, -5.448715459115861e-35],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.02393249586119253,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00026232853701164846, 0.0010446328890889476, 0.0023329528165359397, 0.004104298219726469, 0.0063270593979766485, 0.008961571125402416, 0.011960820477815111, 0.015271285779467403, 0.01883389169862492, 0.02258506344826059, 0.026457861279635272, 0.030383175023699794, 0.034290957363698915, 0.038111473831198256, 0.04177654721932559, 0.04522077420664258, 0.04838269248096531, 0.051205877535781257, 0.0536399495669047, 0.05564147250127606, 0.05717472911471448, 0.05821235840662964] + [0.05873584385772543] * 2 + [0.05821235840662964, 0.05717472911471448, 0.05564147250127607, 0.05363994956690472, 0.05120587753578125, 0.04838269248096532, 0.04522077420664259, 0.0417765472193256, 0.03811147383119826, 0.034290957363698915, 0.030383175023699794, 0.026457861279635272, 0.022585063448260594, 0.018833891698624938, 0.015271285779467424, 0.011960820477815132, 0.008961571125402428, 0.0063270593979766416, 0.004104298219726475, 0.0023329528165359427, 0.0010446328890889509, 0.00026232853701165177, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00020591122426341646, -0.0004081479578517248, -0.0006031012814629645, -0.000787292248418763, -0.000957433966550229, -0.0011104902528665743, -0.0012437298143125133, -0.0013547749877575392, -0.0014416441694508166, -0.0015027871767870596, -0.0015371129113518484, -0.0015440088295986826, -0.00152335187370308, -0.0014755106675323703, -0.0014013389385440485, -0.0013021602829990724, -0.0011797445463552284, -0.0010362762403330079, -0.0008743155602522055, -0.0006967526982857819, -0.0005067562679120699, -0.0003077167599321896, -0.00010318603908137324, 0.00010318603908137285, 0.0003077167599321892, 0.0005067562679120703, 0.0006967526982857809, 0.0008743155602522045, 0.0010362762403330079, 0.0011797445463552281, 0.0013021602829990722, 0.0014013389385440483, 0.0014755106675323703, 0.00152335187370308, 0.0015440088295986826, 0.0015371129113518484, 0.0015027871767870596, 0.0014416441694508168, 0.0013547749877575398, 0.001243729814312514, 0.0011104902528665751, 0.0009574339665502285, 0.0007872922484187634, 0.000603101281462965, 0.00040814795785172527, 0.00020591122426341692, -9.9373716694796e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04512714510853295,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006672932696453106, 0.0026572652143759634, 0.005934404737694919, 0.010440231207171679, 0.016094338042713416, 0.022795827573891616, 0.03042511156126116, 0.038846045251326365, 0.04790835688289238, 0.057450329290203744, 0.0673016857495985, 0.07728662857167577, 0.08722697621522789, 0.09694534294106444, 0.10626830426473052, 0.11502949172054025, 0.12307256171078834, 0.13025398546095493, 0.13644561029408714, 0.14153694651835555, 0.14543713911822198, 0.1480765890643446] + [0.1494081953099051] * 2 + [0.1480765890643446, 0.14543713911822198, 0.14153694651835555, 0.13644561029408717, 0.1302539854609549, 0.12307256171078837, 0.11502949172054029, 0.10626830426473054, 0.09694534294106445, 0.08722697621522789, 0.07728662857167577, 0.0673016857495985, 0.05745032929020375, 0.047908356882892425, 0.038846045251326414, 0.030425111561261212, 0.02279582757389165, 0.0160943380427134, 0.010440231207171694, 0.005934404737694928, 0.0026572652143759716, 0.000667293269645319, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0008777138199601045, -0.0017397648160095947, -0.0025707696677016003, -0.003355899073770806, -0.004081142381365847, -0.004733557606481357, -0.005301502383969145, -0.005774841725820081, -0.006145128880265217, -0.006405756064261216, -0.006552072379535292, -0.006581466807975087, -0.006493414805308723, -0.006289487661609771, -0.005973324461588665, -0.005550567145039826, -0.005028759826292374, -0.004417214169311202, -0.003726843220832927, -0.0029699666667883325, -0.0021600909872150804, -0.0013116684328014752, -0.0004398391241305228, 0.0004398391241305211, 0.0013116684328014737, 0.0021600909872150817, 0.002969966666788328, 0.0037268432208329236, 0.004417214169311203, 0.005028759826292372, 0.005550567145039824, 0.005973324461588665, 0.006289487661609771, 0.006493414805308723, 0.006581466807975087, 0.006552072379535292, 0.006405756064261216, 0.006145128880265219, 0.005774841725820083, 0.005301502383969149, 0.004733557606481359, 0.004081142381365845, 0.0033558990737708088, 0.0025707696677016024, 0.001739764816009597, 0.0008777138199601066, -4.2358878101876744e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003336466348226553, 0.0013286326071879817, 0.0029672023688474595, 0.005220115603585839, 0.008047169021356708, 0.011397913786945808, 0.01521255578063058, 0.019423022625663183, 0.02395417844144619, 0.028725164645101872, 0.03365084287479925, 0.038643314285837886, 0.043613488107613944, 0.04847267147053222, 0.05313415213236526, 0.057514745860270125, 0.06153628085539417, 0.06512699273047746, 0.06822280514704357, 0.07076847325917777, 0.07271856955911099, 0.0740382945321723] + [0.07470409765495255] * 2 + [0.0740382945321723, 0.07271856955911099, 0.07076847325917777, 0.06822280514704358, 0.06512699273047745, 0.061536280855394185, 0.057514745860270146, 0.05313415213236527, 0.048472671470532226, 0.043613488107613944, 0.038643314285837886, 0.03365084287479925, 0.028725164645101876, 0.023954178441446212, 0.019423022625663207, 0.015212555780630606, 0.011397913786945825, 0.0080471690213567, 0.005220115603585847, 0.002967202368847464, 0.0013286326071879858, 0.0003336466348226595, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00043885690998005225, -0.0008698824080047974, -0.0012853848338508001, -0.001677949536885403, -0.0020405711906829236, -0.0023667788032406783, -0.0026507511919845726, -0.0028874208629100406, -0.0030725644401326086, -0.003202878032130608, -0.003276036189767646, -0.0032907334039875436, -0.0032467074026543614, -0.0031447438308048856, -0.0029866622307943326, -0.002775283572519913, -0.002514379913146187, -0.002208607084655601, -0.0018634216104164636, -0.0014849833333941663, -0.0010800454936075402, -0.0006558342164007376, -0.0002199195620652614, 0.00021991956206526055, 0.0006558342164007368, 0.0010800454936075409, 0.001484983333394164, 0.0018634216104164618, 0.0022086070846556016, 0.002514379913146186, 0.002775283572519912, 0.0029866622307943326, 0.0031447438308048856, 0.0032467074026543614, 0.0032907334039875436, 0.003276036189767646, 0.003202878032130608, 0.0030725644401326095, 0.0028874208629100415, 0.0026507511919845743, 0.0023667788032406796, 0.0020405711906829227, 0.0016779495368854044, 0.0012853848338508012, 0.0008698824080047984, 0.0004388569099800533, -2.1179439050938372e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00033364663482265527, -0.0013286326071879817, -0.0029672023688474595, -0.005220115603585839, -0.008047169021356708, -0.011397913786945808, -0.01521255578063058, -0.019423022625663183, -0.02395417844144619, -0.028725164645101872, -0.03365084287479925, -0.038643314285837886, -0.043613488107613944, -0.04847267147053222, -0.05313415213236526, -0.057514745860270125, -0.06153628085539417, -0.06512699273047746, -0.06822280514704357, -0.07076847325917777, -0.07271856955911099, -0.0740382945321723] + [-0.07470409765495255] * 2 + [-0.0740382945321723, -0.07271856955911099, -0.07076847325917777, -0.06822280514704358, -0.06512699273047745, -0.061536280855394185, -0.057514745860270146, -0.05313415213236527, -0.048472671470532226, -0.043613488107613944, -0.038643314285837886, -0.03365084287479925, -0.028725164645101876, -0.023954178441446212, -0.019423022625663207, -0.015212555780630606, -0.011397913786945825, -0.0080471690213567, -0.005220115603585847, -0.002967202368847464, -0.0013286326071879858, -0.00033364663482265955, 2.5937332241468132e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004388569099800523, 0.0008698824080047976, 0.0012853848338508006, 0.0016779495368854037, 0.0020405711906829244, 0.0023667788032406796, 0.0026507511919845743, 0.002887420862910043, 0.0030725644401326116, 0.0032028780321306113, 0.0032760361897676503, 0.0032907334039875484, 0.0032467074026543666, 0.0031447438308048917, 0.002986662230794339, 0.00277528357251992, 0.0025143799131461943, 0.002208607084655609, 0.001863421610416472, 0.001484983333394175, 0.0010800454936075491, 0.0006558342164007467, 0.00021991956206527055, -0.0002199195620652514, -0.0006558342164007277, -0.001080045493607532, -0.0014849833333941554, -0.0018634216104164534, -0.0022086070846555938, -0.0025143799131461786, -0.002775283572519905, -0.002986662230794326, -0.0031447438308048795, -0.003246707402654356, -0.003290733403987539, -0.0032760361897676417, -0.0032028780321306043, -0.0030725644401326064, -0.0028874208629100393, -0.0026507511919845726, -0.0023667788032406783, -0.002040571190682922, -0.0016779495368854037, -0.0012853848338508008, -0.0008698824080047982, -0.0004388569099800532, 2.1179439050938372e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008777138199601045, 0.001739764816009595, 0.0025707696677016007, 0.0033558990737708066, 0.004081142381365848, 0.004733557606481358, 0.005301502383969147, 0.005774841725820084, 0.00614512888026522, 0.006405756064261219, 0.006552072379535296, 0.006581466807975092, 0.006493414805308728, 0.006289487661609777, 0.005973324461588672, 0.005550567145039833, 0.005028759826292382, 0.00441721416931121, 0.0037268432208329354, 0.0029699666667883412, 0.0021600909872150896, 0.0013116684328014843, 0.00043983912413053195, -0.00043983912413051194, -0.0013116684328014646, -0.0021600909872150726, -0.0029699666667883195, -0.0037268432208329154, -0.004417214169311195, -0.005028759826292364, -0.005550567145039817, -0.005973324461588658, -0.006289487661609765, -0.006493414805308718, -0.006581466807975083, -0.006552072379535288, -0.006405756064261212, -0.006145128880265216, -0.00577484172582008, -0.005301502383969147, -0.0047335576064813575, -0.0040811423813658446, -0.0033558990737708083, -0.002570769667701602, -0.0017397648160095967, -0.0008777138199601066, 4.2358878101876744e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006672932696453106, 0.0026572652143759634, 0.005934404737694919, 0.010440231207171679, 0.016094338042713416, 0.022795827573891616, 0.03042511156126116, 0.038846045251326365, 0.04790835688289238, 0.057450329290203744, 0.0673016857495985, 0.07728662857167577, 0.08722697621522789, 0.09694534294106444, 0.10626830426473052, 0.11502949172054025, 0.12307256171078834, 0.13025398546095493, 0.13644561029408714, 0.14153694651835555, 0.14543713911822198, 0.1480765890643446] + [0.1494081953099051] * 2 + [0.1480765890643446, 0.14543713911822198, 0.14153694651835555, 0.13644561029408717, 0.1302539854609549, 0.12307256171078837, 0.11502949172054029, 0.10626830426473054, 0.09694534294106445, 0.08722697621522789, 0.07728662857167577, 0.0673016857495985, 0.05745032929020375, 0.047908356882892425, 0.038846045251326414, 0.030425111561261212, 0.02279582757389165, 0.0160943380427134, 0.010440231207171694, 0.005934404737694928, 0.0026572652143759716, 0.000667293269645319, -2.5937332241468132e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00043885690998005225, 0.0008698824080047975, 0.0012853848338508003, 0.0016779495368854033, 0.002040571190682924, 0.002366778803240679, 0.0026507511919845734, 0.002887420862910042, 0.00307256444013261, 0.0032028780321306095, 0.003276036189767648, 0.003290733403987546, 0.003246707402654364, 0.0031447438308048886, 0.002986662230794336, 0.0027752835725199164, 0.002514379913146191, 0.002208607084655605, 0.0018634216104164677, 0.0014849833333941706, 0.0010800454936075448, 0.0006558342164007422, 0.00021991956206526597, -0.00021991956206525597, -0.0006558342164007323, -0.0010800454936075363, -0.0014849833333941598, -0.0018634216104164577, -0.0022086070846555977, -0.002514379913146182, -0.0027752835725199086, -0.002986662230794329, -0.0031447438308048825, -0.003246707402654359, -0.0032907334039875414, -0.003276036189767644, -0.003202878032130606, -0.003072564440132608, -0.00288742086291004, -0.0026507511919845734, -0.0023667788032406788, -0.0020405711906829223, -0.0016779495368854042, -0.001285384833850801, -0.0008698824080047983, -0.0004388569099800533, 2.1179439050938372e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003336466348226553, 0.0013286326071879817, 0.0029672023688474595, 0.005220115603585839, 0.008047169021356708, 0.011397913786945808, 0.01521255578063058, 0.019423022625663183, 0.02395417844144619, 0.028725164645101872, 0.03365084287479925, 0.038643314285837886, 0.043613488107613944, 0.04847267147053222, 0.05313415213236526, 0.057514745860270125, 0.06153628085539417, 0.06512699273047746, 0.06822280514704357, 0.07076847325917777, 0.07271856955911099, 0.0740382945321723] + [0.07470409765495255] * 2 + [0.0740382945321723, 0.07271856955911099, 0.07076847325917777, 0.06822280514704358, 0.06512699273047745, 0.061536280855394185, 0.057514745860270146, 0.05313415213236527, 0.048472671470532226, 0.043613488107613944, 0.038643314285837886, 0.03365084287479925, 0.028725164645101876, 0.023954178441446212, 0.019423022625663207, 0.015212555780630606, 0.011397913786945825, 0.0080471690213567, 0.005220115603585847, 0.002967202368847464, 0.0013286326071879858, 0.0003336466348226595, -1.2968666120734066e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00043885690998005225, -0.0008698824080047973, -0.0012853848338508, -0.0016779495368854029, -0.002040571190682923, -0.0023667788032406775, -0.0026507511919845717, -0.0028874208629100393, -0.0030725644401326073, -0.003202878032130606, -0.003276036189767644, -0.0032907334039875414, -0.003246707402654359, -0.0031447438308048825, -0.002986662230794329, -0.0027752835725199094, -0.002514379913146183, -0.0022086070846555972, -0.0018634216104164594, -0.001484983333394162, -0.0010800454936075357, -0.000655834216400733, -0.0002199195620652568, 0.00021991956206526513, 0.0006558342164007414, 0.0010800454936075454, 0.0014849833333941684, 0.001863421610416466, 0.0022086070846556055, 0.00251437991314619, 0.0027752835725199155, 0.002986662230794336, 0.0031447438308048886, 0.003246707402654364, 0.003290733403987546, 0.003276036189767648, 0.0032028780321306095, 0.0030725644401326108, 0.002887420862910043, 0.002650751191984575, 0.0023667788032406805, 0.002040571190682923, 0.0016779495368854046, 0.0012853848338508014, 0.0008698824080047986, 0.0004388569099800533, -2.1179439050938372e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003336466348226553, -0.0013286326071879817, -0.0029672023688474595, -0.005220115603585839, -0.008047169021356708, -0.011397913786945808, -0.01521255578063058, -0.019423022625663183, -0.02395417844144619, -0.028725164645101872, -0.03365084287479925, -0.038643314285837886, -0.043613488107613944, -0.04847267147053222, -0.05313415213236526, -0.057514745860270125, -0.06153628085539417, -0.06512699273047746, -0.06822280514704357, -0.07076847325917777, -0.07271856955911099, -0.0740382945321723] + [-0.07470409765495255] * 2 + [-0.0740382945321723, -0.07271856955911099, -0.07076847325917777, -0.06822280514704358, -0.06512699273047745, -0.061536280855394185, -0.057514745860270146, -0.05313415213236527, -0.048472671470532226, -0.043613488107613944, -0.038643314285837886, -0.03365084287479925, -0.028725164645101876, -0.023954178441446212, -0.019423022625663207, -0.015212555780630606, -0.011397913786945825, -0.0080471690213567, -0.005220115603585847, -0.002967202368847464, -0.0013286326071879858, -0.0003336466348226595, -1.2968666120734066e-34],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.05874563732883068,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.EF_x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001338376776782979, 0.005329623741843514, 0.011902516998535683, 0.02093976311097909, 0.03228009220820085, 0.045721135848803655, 0.0610230382905967, 0.07791273672199743, 0.09608883407437308, 0.11522697745987073, 0.13498564625638523, 0.15501224655115117, 0.17494940318746952, 0.1944413371328451, 0.2131402143642502, 0.23071235297450587, 0.24684417773382034, 0.26124781584719364, 0.273666234051264, 0.28387782537898215, 0.2917003637411878, 0.296994255755488] + [0.299665031793473] * 2 + [0.296994255755488, 0.2917003637411878, 0.2838778253789822, 0.27366623405126406, 0.2612478158471936, 0.2468441777338204, 0.23071235297450593, 0.21314021436425026, 0.19444133713284512, 0.17494940318746952, 0.15501224655115117, 0.13498564625638523, 0.11522697745987075, 0.09608883407437316, 0.07791273672199753, 0.0610230382905968, 0.045721135848803725, 0.032280092208200814, 0.020939763110979125, 0.0119025169985357, 0.0053296237418435305, 0.0013383767767829956, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.EF_x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0019460019684250582, -0.003857277485621928, -0.0056997197947072755, -0.007440450469027202, -0.009048406128459795, -0.010494892766169302, -0.011754097793837893, -0.0128035506679157, -0.013624523877002805, -0.014202367134733834, -0.01452676881448521, -0.014591939960596559, -0.014396717592421586, -0.013944585457745276, -0.013243611865222143, -0.01230630570521713, -0.011149393228360723, -0.009793519565210188, -0.008262880313405696, -0.006584789766657208, -0.00478919349052615, -0.0029081339430985635, -0.0009751786765614058, 0.0009751786765614021, 0.0029081339430985604, 0.004789193490526152, 0.006584789766657199, 0.008262880313405687, 0.00979351956521019, 0.01114939322836072, 0.012306305705217128, 0.013243611865222143, 0.013944585457745276, 0.014396717592421586, 0.014591939960596559, 0.01452676881448521, 0.014202367134733834, 0.013624523877002807, 0.012803550667915706, 0.0117540977938379, 0.010494892766169309, 0.00904840612845979, 0.007440450469027208, 0.005699719794707281, 0.003857277485621933, 0.0019460019684250625, -9.391496213455544e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.05076885771950357,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q0.wf": {
            "type": "arbitrary",
            "samples": [0.1582597749869456] * 34 + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.z.Cz_unipolar.flux_pulse_control_q1.wf": {
            "type": "arbitrary",
            "samples": [0.13336658450497493] * 33 + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.z.Cz_unipolar.flux_pulse_control_q2.wf": {
            "type": "arbitrary",
            "samples": [0.05985679743848572] * 27 + [0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.z.Cz_unipolar.flux_pulse_control_q2.wf": {
            "type": "arbitrary",
            "samples": [0.05821385620271752] * 32 + [0.0] * 4,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "twpa.const.wf.I": {
            "type": "constant",
            "sample": 0.954992586021436,
        },
        "twpa.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q0.resonator.readout.iw1": {
            "cosine": [(-0.8609312725526928, 2000)],
            "sine": [(0.5087212831608298, 2000)],
        },
        "q0.resonator.readout.iw2": {
            "cosine": [(-0.5087212831608298, 2000)],
            "sine": [(-0.8609312725526928, 2000)],
        },
        "q0.resonator.readout.iw3": {
            "cosine": [(0.5087212831608298, 2000)],
            "sine": [(0.8609312725526928, 2000)],
        },
        "q1.resonator.readout.iw1": {
            "cosine": [(-0.9402280715861902, 2000)],
            "sine": [(0.34054540578506437, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.34054540578506437, 2000)],
            "sine": [(-0.9402280715861902, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.34054540578506437, 2000)],
            "sine": [(0.9402280715861902, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.33859897789400223, 2000)],
            "sine": [(0.9409307796905876, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.9409307796905876, 2000)],
            "sine": [(-0.33859897789400223, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.9409307796905876, 2000)],
            "sine": [(0.33859897789400223, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9483381547556964, 2000)],
            "sine": [(0.3172613185286868, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(-0.3172613185286868, 2000)],
            "sine": [(0.9483381547556964, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(0.3172613185286868, 2000)],
            "sine": [(-0.9483381547556964, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(0.9743052291294593, 2000)],
            "sine": [(-0.22523170400943088, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.22523170400943088, 2000)],
            "sine": [(0.9743052291294593, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.22523170400943088, 2000)],
            "sine": [(-0.9743052291294593, 2000)],
        },
    },
    "mixers": {},
}


qmm = QuantumMachinesManager(host="172.16.33.107", port=9510, cluster_name="Cluster_1")
qmm.close_all_qms()

with qm_session(qmm, config, timeout=100) as qm:
    job = qm.execute(prog)
    num_qubits = 5
    for i in range(num_qubits):
        results = fetching_tool(job, ["n"], mode="live")
        while results.is_processing():
            n = results.fetch_all()[0]
            progress_counter(n, 5000, start_time=results.start_time)
