from parseData import *

def genSample():
    with open("diseases.txt") as f:
        reader = csv.reader(f, delimiter="\t")
        cuiNum = list(reader)


    newD = open("results.txt", "r+")
    newD.truncate(0)
    newD.write("CUI1\tCUI2\tDisease1\tDisease2\tPubMed1\tPubMed2\tCommon_PubMed_IDs\tLevel_of_similarity\tLevel_of_confidence\tRelated By Papers\tRelated By Name\tRelated By IDs\tDirectly Related\tRelated By Relations\tRelated By Relations IDs\tCommonaility in Relations Relation\n");


    inputSam = open("sample.txt", "r+")
    inputSam.truncate(0)
    inputSam.write("CUI1\tCUI2\tDisease1\tDisease2\tPubMed1\tPubMed2\tCommon_PubMed_IDs\tLevel_of_similarity\tLevel_of_confidence\n");
    
    
    

    sampleRows = []
    
    for num in range(250):
        if(num < 75):
            sampleRows.append(randint(0,2000))
        elif(num < 125):
            sampleRows.append(randint(0,3000)+2000)
        elif(num < 175):
            sampleRows.append(randint(0,7000)+5000)
        else:
            sampleRows.append(randint(0,37000)+12000)
            
            
            
    index = 0
    for row in sampleRows:
        row -=1
        index += 1
        print "SAMPLE " + str(index) + "  ROW " + str(row)
        print cuiNum[row][2] +"\t" + cuiNum[row][3]
        for x in cuiNum[row]:
            newD.write(str(x) + "\t")
            inputSam.write(str(x) + "\t")
        relatedByConcept(cuiNum[row], newD)
        newD.write("\n")
        inputSam.write("\n")
            
    newD.close()
    inputSam.close()
