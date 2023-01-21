def searchServerName(data):
    channelName=data.get('name', None)
    guildName=data.get('guild', {}).get('name', None)
    return guildName,channelName
    