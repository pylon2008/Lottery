# coding=gbk
from GetWebLotteries import *
import pylab

def plotPaiLie3NumValue(valSet, begTime, endTime):
    pylab.figure()
    pylab.title('Pailie3 Lottery History Number'+\
                '(' + begTime + '-' + endTime + ')')
    pylab.xlabel('Lottery Period')
    pylab.ylabel('Lottery Number')
    pylab.plot(range(len(valSet)), valSet, 'b-')


def histPaiLie3NumValue(valSet, begTime, endTime):
    pylab.figure()
    pylab.title('Pailie3 Lottery History Number'+\
                '(' + begTime + '-' + endTime + ')')
    pylab.xlabel('Lottery Period')
    pylab.ylabel('Lottery Number')
    pylab.hist(valSet, 1000)
    
def histPaiLie3NumElementValue(valSet, begTime, endTime):
    pylab.figure()
    pylab.title('Distribution of Pailie3 Lottery History Number Element'+\
                '(' + begTime + '-' + endTime + ')')
    pylab.xlabel('Lottery Number Element')
    pylab.ylabel('Numbers')
    pylab.hist(valSet, 10)
    
def histPaiLie3NumElementSumValue(valSet, begTime, endTime):
    pylab.figure()
    pylab.title('Distribution of Pailie3 Lottery History Number Element Sum'+\
                '(' + begTime + '-' + endTime + ')')
    pylab.xlabel('Lottery Number Element Sum')
    pylab.ylabel('Numbers')
    pylab.hist(valSet, 30)

if __name__ =="__main__":
    begTime = '2012001'
    endTime = '2012365'
    bunValSet = getPaiLie3NumValueSet(begTime, endTime)
#    plotPaiLie3NumValue(bunValSet, begTime, endTime)
    histPaiLie3NumValue(bunValSet, begTime, endTime)

##    gewei = getPaiLie3NumGeWeiValueSet(begTime, endTime)
##    histPaiLie3NumElementValue(gewei, begTime, endTime)
##    shiwei = getPaiLie3NumShiWeiValueSet(begTime, endTime)
##    histPaiLie3NumElementValue(shiwei, begTime, endTime)
##    baiwei = getPaiLie3NumBaiWeiValueSet(begTime, endTime)
##    histPaiLie3NumElementValue(baiwei, begTime, endTime)
##
##    eleSum = getPaiLie3NumSumValueSet(begTime, endTime)
##    histPaiLie3NumElementSumValue(eleSum, begTime, endTime)
##
    pylab.show()
    

