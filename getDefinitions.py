from parseData import *

        
with open("withRelations.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    cuiNum = list(reader)

start = 248

for x in range(start, len(cuiNum)):
    print "\n\n\n\n"
    print "ROW: " + str(x+1)
    print cuiNum[x][4] + "\t" + cuiNum[x][5]
    print "\n" + cuiNum[x][4]

    getDefinitions(cuiNum[x][2])
    print "\n" + cuiNum[x][5]
    getDefinitions(cuiNum[x][3])
    raw_input("Press Enter to Continue")
    
