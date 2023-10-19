import subprocess
import datetime

# Open the file containing the list of devices to ping
with open('hostpinger_devices.txt') as f:
    devices = f.read().splitlines()

# Create a timestamp string for the current time
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Open a file to write the ping results to
with open('results/hostpinger_results.txt', 'a') as f:
    # Loop through each device and ping it
    for device in devices:
        ping_result = subprocess.run(['ping', '-c', '2', '-w', '1', device])
        print(ping_result)
        # Check if the ping was successful or not
        if ping_result.returncode == 0:
            status = 'Success'
        else:
            status = 'Failed'
        # Write the result to the file with a timestamp
        f.write(f'{timestamp} - {device} - {status}\n')
print('+++++++Results written to file+++++++')
