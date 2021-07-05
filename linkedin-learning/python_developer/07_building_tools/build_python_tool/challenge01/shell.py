import subprocess

get_free_space = "df -h / | awk 'NR==2 {print $4}'"

fs_stdout, fs_stderr = subprocess.Popen(
    get_free_space,
    universal_newlines=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
).communicate()

if fs_stderr:
    print("An error occurred retreiving free space.")
else:
    print("The free space is: ", fs_stdout)