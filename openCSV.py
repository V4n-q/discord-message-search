import os
import json
from directMessage import searchRecipients
from serverMessage import searchServerName
import unicodedata


def open_csv_files(subdirs, keywords,usrStat):
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
    folderList =[]
    userSet=set()
    serverInfo={}
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
                            #splits the folder path for the message.csv file 
                            folderName=csv_file.split("\\")
                            #appends the folder name
                            folderList.append(folderName[3])
                            #check if the search is for dm or server
                            if usrStat[0]==1:
                                user=searchRecipients(data,usrStat[1])
                                userSet.update(user)
                            else:
                                guildName, channelName=searchServerName(data)
                                if channelName is not None:
                                    #removing all the characters in channelName and guildName that have the Unicode category "Cs" (Surrogates) using a list comprehension and the join() method
                                    channelName = ''.join(c for c in channelName if unicodedata.category(c) != "Cs")
                                    guildName = ''.join(c for c in guildName if unicodedata.category(c) != "Cs")
                                    serverInfo.setdefault(guildName, []).append(channelName)
                            found = True

    print(f'\nFound Total {counter} Folder which has "{", ".join(keywords)}"\n')
    displayFolder=input("Do you want to view the Folder Names? (y/n): ").lower().strip()
    if displayFolder == 'y':
        print(f'\n{len(folderList)} Folder')
        for item in folderList:
            print(f'\t{item}')
    if usrStat[0]==1:
        print(f"\n{len(userSet)} Ids")
        for item in userSet:
            print(f'\t{item}')
    if usrStat[0]==0:
        print(f'\n{len(serverInfo)} Servers')
        for guildName, channelName in serverInfo.items():
            print(f'\tServer Name:- {guildName} \n\t\t Channel Name:- {", ".join([item for item in channelName])}\n')
    
    if not found:
        print("Not Found")
