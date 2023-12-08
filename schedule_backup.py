import os
import shutil
import datetime
import schedule
import time

source_dir = 'C:/PyBackup'
destination_dir = 'C:/PyBackupfin'

def copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f'Copied to {dest_dir}')
    except FileExistsError:
        print(f'Foulder already exists in {dest_dir}')

schedule.every().day.at('13:53').do(lambda: copy_folder_to_dir(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)