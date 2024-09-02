import os
import subprocess

def run_rd_command(drive_letter, folder_names):
    for folder_name in folder_names:
        command = f'RD "{drive_letter}:\\{folder_name}" /S /Q'
        try:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(f"Deleted {drive_letter}:\\{folder_name} successfully")
        except subprocess.CalledProcessError:
            pass

drives = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
folders = ["Recycler", "$RECYCLE.BIN"]

for drive in drives:
    if os.path.exists(f"{drive}:\\"):  # Check if the drive exists
        run_rd_command(drive, folders)
