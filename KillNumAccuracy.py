# coding=gbk
from GetWebLotteries import *
import pylab

def getKNATimeEnding(begTime, endTime):
    """
    杀当期期号尾。如测07098期杀8，07098期开奖号679，正确。
    """
    allLottery = readHistoryPaiLie3File('排列3.txt')
    numAll = 0
    numRight = 0
    for lottery in allLottery:
        time = lottery.getTime()
        if time>= begTime and time<=endTime:
            numAll += 1
            if time[-1] in lottery.getNum():
                numRight += 0
                #print lottery
            else:
                numRight += 1
    accuracy = float(numRight) / float(numAll)
    return accuracy

def getKNASumEnding(begTime, endTime):
    """
    杀和值尾。如07097期和值10，杀0，07098期开奖号679，正确。
    """
    allLottery = readHistoryPaiLie3File('排列3.txt')
    numAll = 0
    numRight = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numAll += 1
            numSum = allLottery[idx-1].getNumElementSum()
            strSum = str(numSum)
            if strSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, lottery.getNum()
            else:
                numRight += 1
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNASumEnding():
    print 'getKNASumEnding():'
    allYear = [('2004001', '2004365'),\
               ('2005001', '2005365'),\
               ('2006001', '2006365'),\
               ('2007001', '2007365'),\
               ('2008001', '2008365'),\
               ('2009001', '2009365'),\
               ('2010001', '2010365'),\
               ('2011001', '2011365'),\
               ('2012001', '2012365'),\
               ('2013001', '2013365')
               ]
    for year in allYear:
        print year[0], '->', year[1], ':', getKNASumEnding(year[0], year[1])

def getKNASumSum(begTime, endTime):
    """
    杀上期和值合数。如07096期和值22，2+2=4，07097期开奖号532，正确。
    """ 
    allLottery = readHistoryPaiLie3File('排列3.txt')
    numAll = 0
    numRight = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numAll += 1
            numSum = allLottery[idx-1].getNumElementSum()
            strSum = str(numSum)
            numSumSum = 0
            for c in strSum:
                numSumSum += (int)(c)
            strSumSum = str(numSumSum)
            if strSumSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, numSumSum, lottery.getNum()
            else:
                numRight += 1
    if numAll == 0:
        return 0
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNASumSum():
    print 'getKNASumSum():'
    allYear = [('2004001', '2004365'),\
               ('2005001', '2005365'),\
               ('2006001', '2006365'),\
               ('2007001', '2007365'),\
               ('2008001', '2008365'),\
               ('2009001', '2009365'),\
               ('2010001', '2010365'),\
               ('2011001', '2011365'),\
               ('2012001', '2012365'),\
               ('2013001', '2013365')
               ]
    for year in allYear:
        print year[0], '->', year[1], ':', getKNASumSum(year[0], year[1])

if __name__ =="__main__":
    testGetKNASumSum()
    testGetKNASumEnding()
