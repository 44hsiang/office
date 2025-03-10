# QoP Simulator as a Service

Run QoP simulator instances at scale.

## Supported versions
 * v3_1_0
 * v2_2_2
 * v2_2_0
 * v2_1_3

## Installation

In order to run the example use a python3 virtual environment and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now you can run any example.

# Authentication

Your QoPSaaS administrator should provide you an email and password to access the service. You can use these credentials to authenticate to the service the following way:

```python
client = QoPSaaS(host="my_simulator.quantum-machines.co",
                 port=9000,
                 email="your@email.com",
                 password="password")
```

# Contents

`test1.py` - This example shows how to use the QoP Simulator, a trivial hello world example using the simulator.

`test2.py` - This example shows how to use the QoP Simulator, it displays how to serialize instances of the simulator and how to deserialize them as well and handle manually the cleanaup of the simulator.

Remember to modify the host and port, as well as your credentials in the example file to match your QoPSaaS instance.

# Execute the example

Then run the example:

```bash
python3 test1.py
```

# Troubleshooting

## Dependency issues

Make sure you are using `python 3.10` and the requirements file.

If you get an error with dependencies an exhaust frozen list of dependencies is `requirements.frozen.txt`. This could be useful
for developers who want to install the most precise version of the dependencies.

## Security concerns

Serialization of instances will contain login information for the QoPSaaS platform. Be careful not to distribute
the credentials to the public.

## Report issues

If you find any issue, please report it to the QoPSaaS administrator by serializing your instance and sending it to them. You can do this by running the following code:

```python
client = QoPSaaS("....",
                 9000)

qopsass = client.simulator(QoPVersion.v2_2_0)
qopsass.spawn()

json = qopsass.to_dict()

# Send the following json to your QoPSaaS administrator
print(json)
```
