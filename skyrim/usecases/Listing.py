from skyrim.domain.Listing import *

def GetPlayerByUser(id):
    return PlayerListQuery(id)
    

def GetPlayer(id:int):
    return PlayerQuery(id)

def GetBeastList(id):
    return BeastListQuery(id)
    

def GetBeast(id):
    return BeastQuery(id)