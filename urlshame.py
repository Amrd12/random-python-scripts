import sys
import subprocess

# The rest of the elements are the arguments passed to the script
arguments = sys.argv[1:]

# print("Script name:", script_name)
# print("Arguments:", arguments)
url= arguments[0][6:]

print(url)
input("download?")
command_to_run = f'yt-dlp {url} -P "C:/Users/elnba/Music/download yt-dlp"'

# Opening cmd and executing the command
subprocess.call(['cmd.exe', '/K', command_to_run])
input()