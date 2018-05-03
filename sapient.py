minCost = 0;
def main() :
    firstladder = input()
    flx1, fly1, flx2, fly2 = firstladder.split();
    findCostAndSetMin(flx1, fly1, flx2, fly2);
    findCostAndSetMin(flx2, fly2, flx1, fly1);

    secondLadder = input()
    secx1, secy1, secx2, secy2 = secondLadder.split();
    findCostAndSetMin(secx1, secy1, secx2, secy2);
    findCostAndSetMin(secx2, secy2, secx1, secy1);
    

    thirdLadder = input()
    thirx1, thiry1, thirx2, thiry2 = thirdLadder.split();
    findCostAndSetMin(thirx1, thiry1, thirx2, thiry2);
    findCostAndSetMin(thirx2, thiry2, thirx1, thiry1);


def findCostAndSetMin(ladderx1, laddery1, ladderx2, laddery2):
    global minCost;
    costOcurred = abs(int(ladderx1) - int(fromX)) + abs(int(laddery1) - int(fromY)) + 10 + abs(int(ladderx2)-int(toX)) + abs(int(laddery2)-int(toY)); 
    if costOcurred < minCost :
        minCost = costOcurred;
        

mainCo = input();
fromX, fromY, toX, toY = mainCo.split()
minCost = abs(int(fromX)-int(toX)) + abs(int(fromY)-int(toY));
main();
print(minCost);
