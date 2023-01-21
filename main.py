import sys
from openCSV import open_csv_files
from searchFolders import search_folders
# import unicodedata


print("\n")
if len(sys.argv) > 1:
    folderPath = sys.argv[1]
else:
    folderPath = input("Enter the folder path: ")
channel = int(input("Enter '0' for Server and '1' for DM: "))
if channel==1:
    try:
        user=int(input("Enter your discord Id: "))
    except:
        user = None
else:
    user = None
keywords = input("Enter Keywords separated by commas: ").lower()
usrStat=[channel, user]
#Getting the list of subdirectories that match the channel type
subdirs = search_folders(folderPath,channel)
#Opening the csv files in the subdirectories and searching for keywords
open_csv_files(subdirs, keywords,usrStat)