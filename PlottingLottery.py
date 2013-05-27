# coding=gbk
from GetWebLotteries import *
import pylab

def plotPaiLie3NumValue(valSet):
    pylab.figure()
    pylab.title('Pailie3 Lottery History Number')
    pylab.xlabel('Lottery Period')
    pylab.ylabel('Lottery Number')
    pylab.plot(range(len(valSet)), valSet, 'b-')


def histPaiLie3NumValue(valSet):
    pylab.figure()
    pylab.title('Pailie3 Lottery History Number')
    pylab.xlabel('Lottery Period')
    pylab.ylabel('Lottery Number')
    pylab.hist(valSet, 1000)
    
def histPaiLie3NumElementValue(valSet):
    pylab.figure()
    pylab.title('Distributiong of Pailie3 Lottery History Number Element')
    pylab.xlabel('Lottery Number Element')
    pylab.ylabel('Numbers')
    pylab.hist(valSet, 10)
    
def histPaiLie3NumElementSumValue(valSet):
    pylab.figure()
    pylab.title('Distributiong of Pailie3 Lottery History Number Element Sum')
    pylab.xlabel('Lottery Number Element Sum')
    pylab.ylabel('Numbers')
    pylab.hist(valSet, 30)

if __name__ =="__main__":
##    bunValSet = getPaiLie3NumValueSet()
##    plotPaiLie3NumValue(bunValSet)
##    histPaiLie3NumValue(bunValSet)

##    gewei = getPaiLie3NumGeWeiValueSet()
##    histPaiLie3NumElementValue(gewei)
##    shiwei = getPaiLie3NumShiWeiValueSet()
##    histPaiLie3NumElementValue(shiwei)
##    baiwei = getPaiLie3NumBaiWeiValueSet()
##    histPaiLie3NumElementValue(baiwei)

    eleSum = getPaiLie3NumSumValueSet()
    histPaiLie3NumElementSumValue(eleSum)

    pylab.show()
    

