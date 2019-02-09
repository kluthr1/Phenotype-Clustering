from getData import *
import ast


#HELPER METHODS

#returns if common data exist between two list
def common_data(list1, list2): 
    result = False
  
    # traverse in the 1st list 
    for x in list1: 
  
        # traverse in the 2nd list 
        for y in list2: 
    
            # if one common 
            if x == y: 
                result = True
                return result  
                  
    return result

def typeSame(cui1, cui2):
    print cui1
    return (getType(cui1) == getType(cui2))

def commonDataWithRelations(list1, list2): 
    data = []
    if list1 is not None and list2 is not None:
        # traverse in the 1st list 
        for x in list1: 
            
            # traverse in the 2nd list 
            for y in list2: 
                
                # if one common 
                if x[1] == y[1]: 
                    data.append(x)
                  
    return data

def getCommonData(list1, list2):
    data = []
    if list1 is not None and list2 is not None:
        # traverse in the 1st list 
        for x in list1: 
            
            # traverse in the 2nd list 
            for y in list2: 
                
                # if one common 
                if x == y: 
                    data.append(x)
                  
    return data

#returns all unique elements in a list
def uncommons(dataA, new):
    for x in list(new):
        if x in dataA:
            new.remove(x)
    return new


def rmDuplicates(duplicate):
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

#determines if two papers are related by         
def relatedByPapers(num1, num2, numC):
    if(min(num1, num2) > 0):
        return numC*100/min(num1, num2)
    return 0

#Determines if the two diseases have similar names
def relatedByName(name1, name2):
    stringA = re.findall(r"[\w']+", name1.lower())
    stringB = re.findall(r"[\w']+", name2.lower())
    commons = list(set(stringB).intersection(stringA))
    ignores = ["disorder", "disease", "symptom", "syndrome", "carcinoma" , "disability", "gene", "primary","deficiency", "maligant", "of", "type", "congenital", "abnormality","diseases", "familiar","somatic" ]

    for x in list(commons):
        for y in ignores:
            if x == y:
                commons.remove(x)
    
    if "without" in stringB:
        for x in list(commons):
            if(stringB.index(x) > stringB.index("without")):
               commons.remove(x)

    if len(commons)>0:
        return len(commons)
    
    return 0


#Determines if two cuis are related by IDs
def relatedByIDs(cui1, cui2):
    dataA = getIDs(cui1)
    dataB = getIDs(cui2)
    if common_data(dataA, dataB):
        return True
    return False
    

def contained(cui1, cui2, dataA, dataB):
    if dataA is not None:
        if cui2 in dataA:
            return True

        
    if dataB is not None:
        if cui1 in dataB:
            return True
    return False



def extendData(data):
    dataA = list(data)
    index = 0
    if dataA is not None:
        for x in list(dataA):
            index +=1
            newObjects = getRelations(x)
            if newObjects is not None:
                dataA.extend(newObjects)
                        
    return rmDuplicates(dataA)
        
def extendDataWithRelations(data):
    dataA = list(data)
    index = 0
    if dataA is not None:
        for x in list(dataA):
            index +=1
            newObjects = getRelationsWithType(x[1])
            if newObjects is not None:
                dataA.extend(newObjects)
            
    return rmDuplicates(dataA)


def extendIDsWithRelations(dataA, cui1):
    newList = dataA
    extension = getRelations(cui1)
    index = 0
    if extension is not None:
        for x in list(extension):
            index +=1
            newObjects = getIDs(x)
            if newObjects is not None:
                newList.extend(newObjects)

    return rmDuplicates(newList)


def commonIDWithList(data, cui):
    if data is not None:
        for x in data:
            if relatedByIDs(x, cui):
                return True

    return False

def unCommonPapers(num1, num2, numC):
    minNum = min(num1, num2)
    if minNum > 500:
        if (numC/1.0)/minNum < .01:
            return True
    if minNum > 100:
        if numC == 0:
            return True
    return False







#getRelationsWithType
def relationTypeAndConfidence(cui1, cui2):
    print cui1 + "    " + cui2
    dataA = getRelationsWithType(cui1)
    dataB = getRelationsWithType(cui2)
    checkNext = True
    relation = ""
    confidence  = 10
    strongRelations = ["SY","RL", "RQ", "RN"]
    neutralRelations = ["CHD", "PAR", "RB", "SIB"]
    weakRelations = ["AQ", "DEL", "QB", "RU", "RO"]
    if dataA is not None:
        for x in dataA:
            if cui2 == x[1]:
                relation = x[0]
                checkNext = False
    else:    
        if dataB is not None:
            for x in dataB:
                if cui2 == x[1]:
                    relation = x[0]
                    checkNext = False
                                    
    if(checkNext == False):
        confidence = 3
        for x in strongRelations:
            if x == relation:
                confidence = 1
                return [relation, confidence]
        for x in neutralRelations:
            if x == relation:
                confidence = 2
                return [relation, confidence]    
        return[relation, confidence]

    #SECONDARY CONFIDENCES

    if (checkNext):
       dataA =  extendDataWithRelations(dataA)
       dataB =  extendDataWithRelations(dataB)
       if dataA is not None:
        for x in dataA:
            if cui2 == x[1]:
                relation = x[0]
                checkNext = False
        else:    
            if dataB is not None:
                for x in dataB:
                    if cui2 == x[1]:
                        relation = x[0]
                        checkNext = False
    
                                     
        if(checkNext == False):
            confidence = 6
            for x in strongRelations:
                if x == relation:
                    confidence = 4
                    return [relation + "2", confidence]
            for x in neutralRelations:
                if x == relation:
                    confidence = 5
                    return [relation + "2", confidence]    
            return[relation, confidence]

    if(checkNext):
        commons = commonDataWithRelations(dataA, dataB)
        if(len(commons) > 1):
            confidence = 7
            return [commons[0][0] + "3", confidence]
        if(len(commons) == 1):
            confidence = 9
            relation = commons[0][0]
            for x in strongRelations:
                if x == relation:
                    confidence = 7
                    return [relation + "3", confidence]
            for x in neutralRelations:
                if x == relation:
                    confidence = 8
                    return [relation + "3", confidence]    
            return[relation, confidence]

    return ["N/A", "10"]





def numAtomRelations(cui1, cui2):
    print cui1
    return [min(len(getRelations(cui1)), len(getRelations(cui2))), min(len(getIDs(cui1)), len(getIDs(cui2)))]




def getAtomConfidence(cui1, cui2):
    dataA = getIDs(cui1)
    dataB = getIDs(cui2)
    confidence = 10
    print cui1
    print cui2
    print "RUN"
    commons = rmDuplicates(getCommonData(dataA, dataB))
    print commons
    percentPoints = min(len(dataB), len(dataA))
    if(len(commons) > 0 and percentPoints > 0):
        percents = len(commons)*100/percentPoints
        if(percents > 25):
            return [percents, 1]
        if(percents > 3):
            return [percents, 2]
        return [percents, 3]

    
    #SECONDARY CONFIDENCE
    newDataA = rmDuplicates(extendIDsWithRelations(dataA, cui1))
    newDataB = rmDuplicates(extendIDsWithRelations(dataB, cui2))
    
    print "LIST A"
    print newDataA
    print "LIST B"
    print newDataB
    
    print "Run1"
    commons = getCommonData(newDataA, dataB)
    commons.extend(getCommonData(dataA, newDataB))
    commons = rmDuplicates(commons)
    print commons
    percentPoints = min(len(newDataA), len(newDataB))
    if(len(commons) > 0 and percentPoints > 0):
        percents = len(commons)*100/percentPoints
        if(percents > 25):
            return [percents, 4]
        if(percents > 5):
            return [percents, 5]
        return [percents, 6]

    
    commons = getCommonData(newDataA, newDataB)
    print "RUN2"
    print commons 
    if(len(commons) > 0 and percentPoints > 0):
        percents = len(commons)*100/percentPoints
        if(percents > 25):
            return [percents, 7]
        if(percents > 5):
            return [percents, 8]
        return [percents, 9]
        
    return [0, 10]



#Determining Full Data
def detailingParsing(row):
    cui1 = row[0]
    cui2 = row[1]
    name1 = row[2]
    name2 = row[3]
    num1 = int(row[4])
    num2 = int(row[5])
    numC = int(row[6])
    decision = [0,3]
    
    relatedPapers =  relatedByPapers(num1, num2, numC)
    namesC = relatedByName(name1, name2)
    relations = relationTypeAndConfidence(cui1, cui2)
    relationsIDs = getAtomConfidence(cui1, cui2)

    




def simpleRelation(relations):
    print relations
    newArr = ast.literal_eval(relations)
    print newArr[1]
    value = int(newArr[1])
    if value <= 3:
        return 1
    elif value <=6:
        return 2
    elif value <=9:
        return 3
    return 0

def getValueA(relations):
    newArr = ast.literal_eval(relations)
    return int(newArr[0])
    
def getValueB(relations):
    newArr = ast.literal_eval(relations)
    return int(newArr[1])





#ORIGINAL GET CONFIDENCE METHOD
def getConfidence(row):
    cui1 = row[0]
    cui2 = row[1]
    name1 = row[2]
    name2 = row[3]
    num1 = int(row[4])
    num2 = int(row[5])
    numC = int(row[6])

    decision = [0,3]
    
    relatedPapers =  relatedByPapers(num1, num2, numC)
    namesC = relatedByName(name1, name2)
    relatedByRelations = False
    relatedIDs = relatedByIDs(cui1, cui2) 
    directlyRelated = False
    commonality = False
    relationsIDs = False
    unlike = unCommonPapers(num1, num2, numC)
    
    dataA = getRelations(cui1)
    dataB = getRelations(cui2)
    checkNext = True
    directlyRelated = contained(cui1, cui2, dataA, dataB)
    checkNext = not directlyRelated and not relatedIDs

    if(checkNext):
        dataA = extendData(dataA)
        dataB = extendData(dataB)
        relatedByRelations = contained(cui1, cui2, dataA, dataB)
        relationsIDs = commonIDWithList(cui1, dataB) or commonIDWithList(cui2, dataA)
        checkNext = not relatedByRelations and not relationsIDs
    if (checkNext):
        if( dataA is not None and dataB is not None):
            commonality = common_data(dataA, dataB)


    if relatedIDs or relatedPapers or directlyRelated:
        return [0,1]
 
    if namesC >= 1:
        if relatedByRelations:
            return [0,2]
        if relationsIDs:
            return [0,1]
        if namesC > 1:
            if commonality:
                return [0,1]
            return [0,2]
        if namesC == 1:
            if commonality:
                return [0,2]
            return [0,3]


    if relatedByRelations:
        return [0,3]
    if relationsIDs:
        return [0,2]
    if commonality:
        return [1,3]
    if unlike:
        return [1,1]
    return [1,2]









def ioDecisionTree(row, iostream):

    
    cui1 = row[0]
    cui2 = row[1]
    name1 = row[2]
    name2 = row[3]
    num1 = int(row[4])
    num2 = int(row[5])
    numC = int(row[6])
    true = "1\t"
    false = "0\t"
    
    if relatedByPapers(num1, num2, numC):
        print "Related By Papers"
        iostream.write(true)
    else:
        iostream.write(false)
    
    if relatedByName(name1, name2):
        print "Related By Name"
        iostream.write(true)
    else:
        iostream.write(false)

    dataA = getRelations(cui1)
    dataB = getRelations(cui2)
    checkNext = False
    
    if relatedByIDs(cui1, cui2):
        print "Related By IDs"
        checkNext = True
        iostream.write(true)
    else:
        iostream.write(false)

    if contained(cui1, cui2, dataA, dataB):
        print "Directly Related"
        checkNext = True
        iostream.write(true)
    else:
        iostream.write(false)

        
    if not checkNext:    
        dataA = extendData(dataA)
        dataB = extendData(dataB)

        if contained(cui1, cui2, dataA, dataB):
            print "Related By Relations"
            checkNext = True
            iostream.write(true)
        else:
            iostream.write(false)

            
        if commonIDWithList(cui1, dataB):
            print "Related By Relations IDs"
            iostream.write(true)
        elif commonIDWithList(cui2, dataA):
            print "Related By Relations IDs" 
            iostream.write(true)
        else:
            iostream.write(false)

          
    if not checkNext:
        if( dataA is not None and dataB is not None):
            if common_data(dataA, dataB):
                print "Commonaility in Relations Relations"
                iostream.write(true)
            else:
                iostream.write(false)
            
    return 0
            
            

