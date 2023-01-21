def searchRecipients(data,usrStat):
    recipients = data.get("recipients")
    # Converting the recipients list to integer
    recipients = [int(x) for x in recipients]
    #returns all the userid/recipients
    if not usrStat:
        return recipients
    #Filter out the user id, removing the id inputed by you and returns the value
    else:
        filteredUser=[item for item in recipients if item!=usrStat]
        return filteredUser
