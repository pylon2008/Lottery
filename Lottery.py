# coding=gbk

class Lottery(object):
    def __init__(self, time, num, moneyIn, moneyOut):
        """
        time:中奖期数,str
        num:中奖号码,str
        moneyIn:投注总额,int
        moneyOut:奖额,int
        """
        self.time = time
        self.num = num
        self.moneyIn = moneyIn
        self.moneyOut = moneyOut

    def getTime(self):
        return self.time

    def getNum(self):
        return self.num
    
    def getNumElement(self, elementIndex):
        realIdx = 3 - emementIndex
        if realIdx>=2 and realIdx < 2:
            element = self.num[realIdx-1:realIdx]
            return element
        else:
            raise KeyError('Lottery getNumElement error' + str(elementIndex))

    def getNumElementSum(self):
        eleSum = 0
        for idx in range(3):
            eleSum += self.getNumElementValue(idx)
        return eleSum
        
    def getNumElementValue(self, elementIndex):
        realIdx = 3 - elementIndex
        if realIdx>=1 and realIdx < 4:
            element = self.num[realIdx-1:realIdx]
            try:
                return (int)(element)
            except:
                return 200
        else:
            raise KeyError('Lottery getNumElement error' + str(elementIndex))

    def getNumValue(self):
        try:
            return (int)(self.num)
        except:
            return 2000

    def getMoneyIn(self):
        return self.moneyIn
    
    def getMoneyOut(self):
        return self.moneyOut

    def __str__(self):
        strLottery = ''
        strIn = str(self.moneyIn)
        strOut = str(self.moneyOut)
        strLottery = strLottery + '第' + self.time + '中奖号码:' + self.num \
                     + '\t本期投注总额:' + strIn \
                     + '\t奖额:' + strOut
        return strLottery


class LotteryPaiLie3(Lottery):
    def __init__(self, time, num, moneyIn, \
                 numDanXuan, moneyDanXuan,\
                 numZuXuan3, moneyZuXuan3,\
                 numZuXuan6, moneyZuXuan6):
        """
        numDanXuan:单选中奖数,int
        moneyDanXuan:单选中奖金额,int
        numZuXuan3:组选3中奖数,int
        moneyZuXuan3:组选3中奖金额,int
        numZuXuan6:组选6中奖数,int
        moneyZuXuan6:组选6中奖金额,int
        """
        totalMoneyOut = moneyDanXuan + moneyZuXuan3 + moneyZuXuan6
        Lottery.__init__(self, time, num, moneyIn, totalMoneyOut)
        self.numDanXuan = numDanXuan
        self.moneyDanXuan = moneyDanXuan
        self.numZuXuan3 = numZuXuan3
        self.moneyZuXuan3 = moneyZuXuan3
        self.numZuXuan6 = numZuXuan6
        self.moneyZuXuan6 = moneyZuXuan6

    def getDanXuan(self):
        return self.numDanXuan, self.moneyDanXuan

    def getZuXuan3(self):
        return self.numZuXuan3, self.moneyZuXuan3

    def getZuXuan6(self):
        return self.numZuXuan6, self.moneyZuXuan6

    def getNumValue(self):
        value = Lottery.getNumValue(self)
        if value>=0 and value<1000:
            return value
        else:
            return 2000

    def __str__(self):
        strLottery = Lottery.__str__(self)
        strLottery = strLottery + '('\
                     + '<' + str(self.numDanXuan) + ',' + str(self.moneyDanXuan) + '>、'\
                     + '<' + str(self.numZuXuan3) + ',' + str(self.moneyZuXuan3) + '>、'\
                     + '<' + str(self.numZuXuan6) + ',' + str(self.moneyZuXuan6) + '>'\
                     + ')'
        return strLottery
