#################################################################################################
# usage of the script
# usage: python retrieve-cui-or-code.py -k APIKEY -v VERSION -i IDENTIFIER -s SOURCE
# If you do not provide the -s parameter, the script assumes you are retrieving information for a
# known UMLS CUI
#################################################################################################
from parseData import *

disease_file = "diseases.txt"

with open(disease_file) as f:
    reader = csv.reader(f, delimiter="\t")
    cuiNum = list(reader)

output_file = "remake.txt"
ostream = open(output_file, "r+")
ostream.truncate(0)
print cuiNum[0]
for x in cuiNum[0]:
    ostream.write(str(x) + "\t")
#ostream.write(cuiNum[0] + "\n")

ostream.write("\n")
#errors = []


#def getConfidence(row):

rowsParsed = len(cuiNum)

start = 8000

for index in range(start,rowsParsed):
    ostream.close()
    ostream = open(output_file, "a+b")

    print "TRIAL: " + str(index)
    
    row = cuiNum[index]
    for x in row:
        ostream.write(str(x) + "\t")

    decision = getConfidence(row)
    
    ostream.write(str(decision[0])+ "\t" + str(decision[1]) + "\n")
    
    """
    if(int(row[7]) != decision[0]):
        accuracy+=1
    else:
        errors.append(row)
    """
    
    print row[2] + "\t" + row[3]
    print decision

    #print "POSITIVE: " + str(int(row[7]) != decision[0])
    


ostream.close()
