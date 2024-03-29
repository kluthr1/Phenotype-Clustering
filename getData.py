from Authentication import *
import requests
import json
import csv
from random import *
import re


def getValue(cui, concept):
    try:
        apikey = "86a68870-ddd3-40d5-8454-de804bffd1b3"
        identifier = cui
        AuthClient = Authentication(apikey)
        tgt = AuthClient.gettgt()
        uri = "https://uts-ws.nlm.nih.gov"
        content_endpoint = "/rest/content/current/CUI/"+str(identifier)+"/" + concept
        query = {'ticket':AuthClient.getst(tgt)}
        r = requests.get(uri+content_endpoint,params=query)
        r.encoding = 'utf-8'
        items  = json.loads(r.text)
        jsonData = items["result"]
        return jsonData
    except:
        return {}
    
    



def getDefinitions(cui):   
    try:
        jsonData = getValue(cui, "definitions")
        index = 0
        defs = []
        for x in jsonData:
            index+=1
            print "DEFINTION "+str(index)
            defs.append( x["value"] )
            parsed = x["value"].replace("<p>" , "\n")
            parsed = parsed.replace("<li>", "\n \t")
            parsed = parsed.replace("<ul>", "\n")
            parsed = parsed.replace("</p>", "\n")
            parsed  = parsed.replace("</li>", "")
            parsed = parsed.replace("</ul", "\n")
            print parsed + "\n"
            
        return defs
    except:
        print "Either No Definitions Exist or You have inputted an incorrect value"

def getType(cui):
    try:
        jsonData = getValue(cui, "")
        return jsonData["semanticTypes"][0]['name']
    except:
        "No Semantic Type"
        
        
        


def getIDs(cui):
    try:
        jsonData = getValue(cui, "atoms")
        atoms = []
        for x in jsonData:
            unparsed = x["code"].split("/")
            newAtom = unparsed[len(unparsed)-2]+  str(unparsed[len(unparsed)-1])
            if(not newAtom.endswith("NOCODE")):
                atoms.append(newAtom)
        return atoms
    except:
        print "Either No Atoms Exist or You have inputted an incorrect value"


        
def getRelations(cui):
    try:
        jsonData = getValue(cui, "relations")
        #print identifier
        relatedData = []
        for x in jsonData:
            parsed = x["relatedId"].split('/')
            relatedData.append(parsed[len(parsed)-1]) 
        return relatedData
    except:
        print "Either No Relations Exist or You have inputted an incorrect value"

        
def getRelationsWithType(cui):
    try:
        jsonData = getValue(cui, "relations")
        #print identifier
        relatedData = []
        for x in jsonData:
            parsed = x["relatedId"].split('/')
            relatedData.append([x["relationLabel"], parsed[len(parsed)-1]]) 
        return relatedData
    except:
        print "Either No Relations Exist or You have inputted an incorrect value"
