# coding=gbk
from GetWebLotteries import *
import pylab

def getMoneyInOut(begTime, endTime):
    """
    ����ĳʱ����ڵĽ��Ͷע�ܶ��
    http://blog.sina.com.cn/s/blog_74a7e56e010177l8.html
    http://wenku.baidu.com/view/583a5604eff9aef8941e060a.html
    http://www.douban.com/group/topic/16780820/
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    val = 0.0
    for lottery in allLottery:
        time = lottery.getTime()
        if time>= begTime and time<=endTime:
            numAll += 1
            thisVal = ( (float)(lottery.getMoneyOut()) / lottery.getMoneyIn() )
            val += thisVal
            #print lottery.getMoneyOut(), lottery.getMoneyIn(), thisVal
    accuracy = val * 100.0 / float(numAll)
    return accuracy

def testMoneyInOut():
    print 'getMoneyInOut():'
    allYear = [('2004001', '2004365'),\
               ('2005001', '2005365'),\
               ('2006001', '2006365'),\
               ('2007001', '2007365'),\
               ('2008001', '2008365'),\
               ('2009001', '2009365'),\
               ('2010001', '2010365'),\
               ('2011001', '2011365'),\
               ('2012001', '2012365'),\
               ('2013001', '2013365'),\
               ('2004001', '2013365')
               ]
    for year in allYear:
        print year[0], '->', year[1], ':', getMoneyInOut(year[0], year[1])

def getKNATimeEnding(begTime, endTime):
    """
    1.ɱ�����ں�β�����07098��ɱ8��07098�ڿ�����679����ȷ��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
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

def testGetKNATimeEnding():
    print 'getKNATimeEnding():'
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
        print year[0], '->', year[1], ':', getKNATimeEnding(year[0], year[1])

def getKNALast2ElementCutSumEnding(begTime, endTime):
    """
    4.ɱ�����ڰ�ʮ��λλ���β����07096�ڿ�����967��07097�ڿ�����532��
    9-5=4��6-3=3��7-2=5��4+3+5=12��ɱ2;��07098�ڿ�����679����ȷ��
    """ 
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    for idx in range(2,len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time>= begTime and time<=endTime:
            numAll += 1
            last2 = allLottery[idx-2]
            last1 = allLottery[idx-1]
            elementCutSum = \
                          (last2.getNumElementValue(0)-last1.getNumElementValue(0))+\
                          (last2.getNumElementValue(1)-last1.getNumElementValue(1))+\
                          (last2.getNumElementValue(2)-last1.getNumElementValue(2))
            strelementCutSum = str(elementCutSum)
            if strelementCutSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, numSumSum, lottery.getNum()
            else:
                numRight += 1
    if numAll == 0:
        return 0
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNALast2ElementCutSumEnding():
    print 'getKNALast2ElementCutSumEnding():'
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
        print year[0], '->', year[1], ':', getKNALast2ElementCutSumEnding(year[0], year[1])

def getKNALast2ElementAddSumEnding(begTime, endTime, numTime):
    """
    5.ɱ�����ڰ�ʮ��λ�ֱ����֮β����07096�ڿ�����967��07097�ڿ�����532��
    9+5=14��6+3=9��7+2=9��ɱ4��9��07098�ڿ�����679��4�ԣ�9��
    """
    """
    ֧��ɱ����numTime
    """
    def getMulAdd(curTime, numTime, allLottery):
        val = 0
        for idx in range(numTime):
            realIdx = curTime - idx - 1
            if realIdx<0:
                break
            val += allLottery[realIdx].getNumElementSum()
        return val
            
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    for idx in range(2,len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time>= begTime and time<=endTime:
            numAll += 1
            elementCutSum = getMulAdd(idx, numTime, allLottery)
##            last2 = allLottery[idx-2]
##            last1 = allLottery[idx-1]
##            elementCutSum = \
##                          (last2.getNumElementValue(0)+last1.getNumElementValue(0))+\
##                          (last2.getNumElementValue(1)+last1.getNumElementValue(1))+\
##                          (last2.getNumElementValue(2)+last1.getNumElementValue(2))
            strelementCutSum = str(elementCutSum)
            if strelementCutSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, numSumSum, lottery.getNum()
            else:
                numRight += 1
    if numAll == 0:
        return 0
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNALast2ElementAddSumEnding():
    print 'getKNALast2ElementAddSumEnding():'
##    allYear = [('2004001', '2004365'),\
##               ('2005001', '2005365'),\
##               ('2006001', '2006365'),\
##               ('2007001', '2007365'),\
##               ('2008001', '2008365'),\
##               ('2009001', '2009365'),\
##               ('2010001', '2010365'),\
##               ('2011001', '2011365'),\
##               ('2012001', '2012365'),\
##               ('2013001', '2013365')
##               ]
##    for year in allYear:
##        print year[0], '->', year[1], ':', getKNALast2ElementAddSumEnding(year[0], year[1], 4)
    allYear = [\
           ('2004001', '2013365')\
           ]
    year = allYear[0]
    for idx in range(1,1000):
        print year[0], '->', year[1], ':', getKNALast2ElementAddSumEnding(year[0], year[1], idx)


def getKNASumEnding(begTime, endTime):
    """
    6.ɱ��ֵβ����07097�ں�ֵ10��ɱ0��07098�ڿ�����679����ȷ��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
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

def getKNAWeightedAverage(begTime, endTime):
    """
    7����λ��7+��λ��5ɱβ����07097�ڿ�����532��5��7+2��5=45��ɱ5��07098�ڿ�����679����ȷ��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numAll += 1
            numSum = allLottery[idx-1].getNumElementValue(2)*7 + \
                     allLottery[idx-1].getNumElementValue(0)*5
            strSum = str(numSum)
            if strSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, lottery.getNum()
            else:
                numRight += 1
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNAWeightedAverage():
    print 'getKNAWeightedAverage():'
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
        print year[0], '->', year[1], ':', getKNAWeightedAverage(year[0], year[1])

def getKNAWeightedAverage2(begTime, endTime):
    """
    8����λ��7+��λ��4+��λ��2+4ɱβ����07097�ڿ�����532��
    5��7+3��4+2��2+4=55��ɱ5��07098�ڿ�����679����ȷ��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numAll += 1
            numSum = allLottery[idx-1].getNumElementValue(2)*7 + \
                     allLottery[idx-1].getNumElementValue(1)*4 + \
                     allLottery[idx-1].getNumElementValue(0)*2 + 4
            strSum = str(numSum)
            if strSum[-1] in lottery.getNum():
                numRight += 0
                #print strSum, lottery.getNum()
            else:
                numRight += 1
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNAWeightedAverage2():
    print 'getKNAWeightedAverage2():'
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
        print year[0], '->', year[1], ':', getKNAWeightedAverage2(year[0], year[1])

def getKNACorresponding(begTime, endTime):
    """
    9.������0123456789 ��Ӧɱ��
���� ��Ӧ��8527419630 ����2������07096�ڿ�����967��ɱ��Ӧ��096��07097�ڿ�����532����ȷ��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numAll += 1
            corresponding = '8527419630'
            a = corresponding[allLottery[idx-1].getNumElementValue(2)]
            b = corresponding[allLottery[idx-1].getNumElementValue(1)]
            c = corresponding[allLottery[idx-1].getNumElementValue(0)]
            if a in lottery.getNum() and b in lottery.getNum() and c in lottery.getNum() :
                numRight += 0
                #print allLottery[idx-1].getNum(),a,b,c, lottery.getNum()
            else:
                numRight += 1
    accuracy = float(numRight) / float(numAll)
    return accuracy

def testGetKNACorresponding():
    print 'getKNACorresponding():'
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
        print year[0], '->', year[1], ':', getKNACorresponding(year[0], year[1])

def getKNASumSum(begTime, endTime):
    """
    10.ɱ���ں�ֵ��������07096�ں�ֵ22��2+2=4��07097�ڿ�����532����ȷ��
    """ 
    allLottery = readHistoryPaiLie3File('����3.txt')
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

def getKNADoubleElementCorresponding(begTime, endTime):
    """
    pylon.ǰ�ڿ�������д���2��һ����ֵ��ʱ�򣬶�Ӧ�Ŷ�������
���� ��Ӧ��8527419630 ����2��
    """
    allLottery = readHistoryPaiLie3File('����3.txt')
    numAll = 0
    numRight = 0
    numTotal = 0
    for idx in range(len(allLottery)):
        lottery = allLottery[idx]
        time = lottery.getTime()
        if time> begTime and time<=endTime:
            numTotal += 1
            corresponding = '8527419630'
            if allLottery[idx-1].getNumElementValue(0)==allLottery[idx-1].getNumElementValue(1):
                #print allLottery[idx-1].getNum()
                numAll += 1
                if corresponding[allLottery[idx-1].getNumElementValue(0)] in lottery.getNum():
                    numRight += 1
                    #print allLottery[idx-1].getNum(), lottery.getNum()
                else:
                    numRight += 0
            elif allLottery[idx-1].getNumElementValue(0)==allLottery[idx-1].getNumElementValue(2):
                #print allLottery[idx-1].getNum()
                numAll += 1
                if corresponding[allLottery[idx-1].getNumElementValue(0)] in lottery.getNum():
                    numRight += 1
                    #print allLottery[idx-1].getNum(), lottery.getNum()
                else:
                    numRight += 0
            elif allLottery[idx-1].getNumElementValue(1)==allLottery[idx-1].getNumElementValue(2):
                #print allLottery[idx-1].getNum()
                numAll += 1
                if corresponding[allLottery[idx-1].getNumElementValue(1)] in lottery.getNum():
                    numRight += 1
                    #print allLottery[idx-1].getNum(), lottery.getNum()
                else:
                    numRight += 0
            else:
                a = 0
                #print allLottery[idx-1].getNum()
    accuracy = float(numRight) / float(numAll)
    #print float(numAll) / float(numTotal)
    #print numRight, numAll
    return accuracy

def testGetKNADoubleElementCorresponding():
    print 'getKNADoubleElementCorresponding():'
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
        print year[0], '->', year[1], ':', getKNADoubleElementCorresponding(year[0], year[1])

if __name__ =="__main__":
    testMoneyInOut()
##    testGetKNATimeEnding()
##    testGetKNALast2ElementCutSumEnding()
##    testGetKNALast2ElementAddSumEnding()
##    testGetKNASumEnding()
##    testGetKNAWeightedAverage()
##    testGetKNAWeightedAverage2()
##    testGetKNACorresponding()
##    testGetKNASumSum()
##    testGetKNADoubleElementCorresponding()
