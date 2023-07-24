import math
import os
import time
from datetime import datetime
from pathlib import Path
import shutil


# List of Directories
home = str(Path.home())
dirs = [
    os.path.join(home, "Downloads"),
    [os.path.join(home, "Documents"), ("doc", "docx", "xls", "xlsx", "ppt",
                                       "pptx", "pdf", "odt", "ods", "txt")],
    [os.path.join(home, "/Pictures"), ("png", "jpg")],
    [os.path.join(home, "/Music"), ("mp3")],
    [os.path.join(home, "/Videos"), ("mp4")],
    os.path.join(home, "/Others")
]

first_date = 30
second_date = 60
third_date = 90

# Make sure Others folder exists
if not os.path.isdir(dirs[5]):
    os.makedirs(dirs[5])


def file_age(filepath):
    """ Get the age of the file by days """
    time_stamp = time.time() - os.path.getmtime(filepath)
    return math.floor(int(time_stamp) / 86400)


def clean_downloads():
    """
    Cleans the Downloads folder. Moving all its file that is atleast 7 week
    old to the allocated folder (Documents/Pictures/Music/Videos/Others)
    depending on its file type.
    """

    f = open(os.path.join(home, "action-history.log"), 'a')

    for file in os.listdir(dirs[0]):

        # Variables
        file_path = dirs[0] + "/" + file
        age = file_age(file_path)
        log = str(datetime.now().strftime(
            "%d-%m-%Y %H:%M")) + ": " + file_path + " -> "

        # Move each file to the new path
        if age >= 7:

            # Document/Pictures/Music/Videos
            for i in range(1, len(dirs) - 1):
                if file.endswith(dirs[i][1]):
                    new_path = os.path.join(dirs[i][0], file)

            # Others files
            if os.path.exists(file_path) and not new_path:
                new_path = os.path.join(dirs[5], file)

            shutil.move(file_path, new_path)

            log += new_path + "\n"

            # Append new history
            f.write(log)

    f.close()


if __name__ == "__main__":
    clean_downloads()
