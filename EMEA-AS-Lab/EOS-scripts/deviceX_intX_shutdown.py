import pyeapi

# Define the eAPI connection parameters
hostname = "your_eos_device_ip"
username = "your_username"
password = "your_password"

# Define the interface you want to shut down
interface = "Ethernet1"

# Create an eAPI connection
connection = pyeapi.client.connect(
    transport='https',
    host=hostname,
    username=username,
    password=password,
    return_node=True,
)

# Create a node object for the device
node = pyeapi.client.Node(connection)

try:
    # Execute the configuration commands to shut down the interface
    commands = [
        'enable',
        f'configure terminal',
        f'interface {interface}',
        'shutdown',
        'end',
    ]

    result = node.config(commands)

    # Check if the commands were successful
    if not result:
        print(f"Failed to configure interface {interface}.")
    else:
        print(f"Interface {interface} has been shut down.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
