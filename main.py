import os
import json
import sys

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

def open_csv_files(subdirs, keywords):
    """
    This function takes in the list of subdirectories and keywords as arguments and
    opens the csv files in the subdirectories and searches for the keywords,
    returns the folder name and the Id of the user
    """
    # Checking if the keywords entered by user is only one or multiple
    if ',' not in keywords:
        keywords = [keywords]
    else:
        keywords = keywords.split(',')
    found = False
    counter=0
    for subdir in subdirs:
        for file in os.listdir(subdir):
            if file.endswith('.csv'):
                csv_file = os.path.join(subdir, file)
                with open(csv_file, encoding='utf-8-sig') as f:
                    text = f.read().lower()
                    for keyword in keywords:
                        if keyword in text:
                            counter=counter+1
                            jsonFile=None
                            for subfile in os.listdir(subdir):
                                if subfile.endswith('.json'):
                                    jsonFile=os.path.join(subdir,subfile)
                            with open(jsonFile) as f:
                                data = json.load(f)
                            folder=csv_file.split("\\")
                            recipients = data.get("recipients")
                            # Converting the recipients list to integer
                            recipients = [int(x) for x in recipients]
                            # Using list comprehension to filter out the user
                            filteredList = [x for x in recipients if x != user]
                            print(f'Found {keyword} in {folder[3]}, Discord Id is {filteredList[0]}')
                            found = True
    print(f'\nFound Total {counter} Ids\n')
    if not found:
        print("Not Found")


if len(sys.argv) > 1:
    folderPath = sys.argv[1]
    print(folderPath)
else:
    folderPath = input("\nEnter the folder path: ")
user=int(input("Enter your discord Id: "))
channel = int(input("Enter '0' for Server and '1' for DM: "))
keywords = input("Enter Keywords separated by commas: ").lower()
print("\n")
#Getting the list of subdirectories that match the channel type
subdirs = search_folders(folderPath,channel)
#Opening the csv files in the subdirectories and searching for keywords
open_csv_files(subdirs, keywords)
