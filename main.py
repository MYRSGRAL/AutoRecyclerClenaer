import os
import subprocess

def run_rd_command(drive_letter, folder_names):
    """Runs the RD command for the given drive and multiple folders."""
    for folder_name in folder_names:
        command = f'RD "{drive_letter}:\\{folder_name}" /S /Q'
        try:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.DEVNULL)
            print(f"Deleted {drive_letter}:\\{folder_name} successfully")
        except subprocess.CalledProcessError:
            # Silently ignore errors, as the folder might not exist
            pass

# Use string formatting to dynamically create drive letters
drives = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
folders = ["Recycler", "$RECYCLE.BIN"]

# Run the RD command for each drive
for drive in drives:
    if os.path.exists(f"{drive}:\\"):  # Check if the drive exists
        run_rd_command(drive, folders)
