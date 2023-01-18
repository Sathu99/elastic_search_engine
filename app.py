import subprocess

# List of Python scripts to run
scripts = ["updatedata.py", "route.py"]

try:
    # Loop through the list of scripts and run them
    for script in scripts:
        try:
            subprocess.run(["python", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running {script}: {e}")
            exit(1)
except KeyboardInterrupt:
    print("Script execution interrupted by user.")
