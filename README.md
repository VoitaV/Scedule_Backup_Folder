# Automatic Backup Python Script

This script facilitates automatic backup of a specified folder to a destination directory at a scheduled time using Python.

## Usage
1. Update source_dir and destination_dir with the source and destination directory paths.
2. Schedule the backup time using schedule.every().day.at('HH:MM').do(lambda: copy_folder_to_dir(source_dir, destination_dir)), where 'HH:MM' represents the time in 24-hour format.
3. Run the script and the backup will be automatically performed at the scheduled time.

## Functionality
The script uses the shutil library to copy the entire source directory to the destination directory, creating a new folder named with the current date. 

## Requirements
- Python 3.x
- schedule library (install using pip install schedule)

Feel free to modify the script as per your requirements.
