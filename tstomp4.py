import os
import subprocess
import sys

# Get the directory where the script is running
script_directory = os.getcwd()
# Iterate through all files in the directory
for filename in os.listdir(script_directory):
    if filename.endswith('.ts'):
        ts_file = os.path.join(script_directory, filename)
        mp4_file = os.path.join(script_directory, f"{os.path.splitext(filename)[0]}.mp4")
        
        # Construct the ffmpeg command
        command = f'ffmpeg -i "{ts_file}" "{mp4_file}"'
        
        # Run the command
        subprocess.run(command, shell=True)
        os.remove(ts_file)
        print(f'Converted {ts_file} to {mp4_file}')

print('Conversion completed!')
