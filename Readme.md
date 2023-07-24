# Automated File Management System

A Python script that manages files automatically to reduce the number of files stored in the Download folders.

The download folder is known to be messy over time due to all files being downloaded from the web being stored in this folder automatically and becoming tedious to manage manually because it is not mandatory and an important task to focus on, at least to me hehe.

This Python script automatically manages the files in the download folders that are a week old. It is expected for the user to only remember that the file he downloaded stores in the download folder, and I assume that a week-old file tends to be forgotten, at least to me hehe.

Storing each file in the allocated folder (Documents, Music, Videos, Pictures), depending on its file extension. An unrelated file type like ".exe" will be stored in a specific folder that will be located in the home directory. A folder will be considered a single document and will be stored in the Documents folder.

To avoid allocated folders being messy, storing files that are a month old will be stored in a new folder called "last month" in that folder. This will also be applicable if it's 2 months or 3 months. Files that are 4 months old or older will be stored in a single folder called "Archived".

The use of tags can be helpful to identify the file's purpose, whether it is school, work, personal, etc. Any word that starts with a hash sign "#" at the end of the filename will create a new folder using the word as the folder name if it does not already exist and will be stored there.

Of course, everything can be reconfigured, like the tag symbol and the dates.

Every action taken by the script will be recorded and stored in "changes.log" which will be located in the Home folder.

## List of Features
- [X] Move files in the download folders to the respective folders (Document, Pictures, Music, Videos).
- [ ] Move more than a month old file to a specific folder (one month, two months, 3 months, Archived).
- [ ] Use of tags
- [ ] Make a config file
