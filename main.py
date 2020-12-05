from point import *
from mathTools import *
from geoTools import *
from ihm import *


def main():
    printChoices(0)
    fstAddr = input("Enter 1st adress: ")
    sndAddr = input("Enter 2nd adress: ")
    p1 = getLonLatFromAdress(fstAddr)
    p2 = getLonLatFromAdress(sndAddr)
    dist = getDistance(p1,p2)
    print("Distance between "+fstAddr+" and "+sndAddr+" is "+str(dist) )
    
main()