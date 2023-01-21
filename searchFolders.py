import os
import json

def search_folders(folderPath,channel):
    """
    This function takes in the root directory and channel as arguments and 
    returns a list of subdirectories that contain json files with the type 
    matching the channel
    """
    subdirs = []
    for subdir, dirs, files in os.walk(folderPath):
        for file in files:
            if file.endswith('.json'):
                # Joining the subdirectory path with the file name
                jsonFile = os.path.join(subdir, file)
                with open(jsonFile) as f:
                    data = json.load(f)
                    # Checking if the json file has the type matching the channel
                    if data.get('type') == channel:
                        subdirs.append(subdir)
    return subdirs