# coding=gbk
import sys  
import urllib
import urllib2
import re
import time
from Lottery import*

def getUrlHtmlString_urllib(strUrl):
    wp = urllib.urlopen(strUrl)
    strHtml = wp.read()
    pos = strHtml.find('排列3第处理 URL 时服务器出错。请与系统管理员联系。')
    if pos != -1:
        return None
    return strHtml

def getUrlHtmlString_urllib2(strUrl):
    headers = {'User-Agent':'Mozilla/5.0 （Windows； U； Windows NT 6.1； en-US； rv：1.9.1.6） Gecko/20091201 Firefox/3.5.6'}   
    req = urllib2.Request(strUrl, headers=headers)
    fd = urllib2.urlopen(req)
    strHtml = fd.read()
    return strHtml

def getKeyNum(strHtml, strKey, beginPos = 0):
    startPos = strHtml.find(strKey, beginPos)
    strNum = ''
    while True:
        leftPos = strHtml.find('>', startPos)
        if leftPos == -1:
            break
        rightPos = strHtml.find('<', leftPos)
        if rightPos == -1:
            break
        strNum = strHtml[leftPos+1:rightPos]
        if strNum!='':
            break
        startPos = rightPos
    return strNum

def getZhongJiangHaoMa(strHtml):
    strZhongJiangHaoMa = getKeyNum(strHtml, "中奖号码：")
    return strZhongJiangHaoMa

def getTouZhuZongE(strHtml):
    strTouZhuZongE = getKeyNum(strHtml, "本期投注总额：")
    return strTouZhuZongE

def getDanXuan(strHtml):
    strDanXuanNum = getKeyNum(strHtml, "单选：")
    pos = strHtml.find("单选：")
    strDanXuanMoney = getKeyNum(strHtml, "奖额：", pos)
    return strDanXuanNum, strDanXuanMoney

def getZuXuan3(strHtml):
    strZuXuan3Num = getKeyNum(strHtml, "组选3：")
    pos = strHtml.find("组选3：")
    strZuXuan3Money = getKeyNum(strHtml, "奖额：", pos)
    return strZuXuan3Num, strZuXuan3Money

def getZuXuan6(strHtml):
    strZuXuan6Num = getKeyNum(strHtml, "组选6：")
    pos = strHtml.find("组选6：")
    strZuXuan6Money = getKeyNum(strHtml, "奖额：", pos)
    return strZuXuan6Num, strZuXuan6Money

def getLotteryPaiLie3(time):
    strUrl = "http://www.16788.cn/pl3/not5.asp?qishu=" + time
    strHtml = getUrlHtmlString_urllib(strUrl)
    if strHtml == None:
        return None
    lottery = None
    try:
        strHtml = strHtml.replace('\r','')
        strHtml = strHtml.replace('\n','')
        strHtml = strHtml.replace('\t','')
        strHtml = strHtml.replace(' ','')
        num = getZhongJiangHaoMa(strHtml)
        moneyIn = getTouZhuZongE(strHtml)
        strDanXuanNum, strDanXuanMoney = getDanXuan(strHtml)
        strZuXuan3Num, strZuXuan3Money = getZuXuan3(strHtml)
        strZuXuan6Num, strZuXuan6Money = getZuXuan6(strHtml)
        lottery = LotteryPaiLie3(time, num, (int)(moneyIn),\
                                 (int)(strDanXuanNum), (int)(strDanXuanMoney),\
                                 (int)(strZuXuan3Num), (int)(strZuXuan3Money),\
                                 (int)(strZuXuan6Num), (int)(strZuXuan6Money))
    except:
        print strUrl, '\t has a error'
    return lottery


def readHistoryPaiLie3File(filePath):
    """"""
    allLottery = []
    f = open(filePath, 'a+b')
    for line in f:
        val = line.split()
        lottery = LotteryPaiLie3(val[0], val[1], (int)(val[2]),\
                             (int)(val[3]), (int)(val[4]),\
                             (int)(val[5]), (int)(val[6]),\
                             (int)(val[7]), (int)(val[8]))
        allLottery.append(lottery)

    lastYear = 2004
    lastTime = 0
    if len(allLottery) > 0:
        last = int(allLottery[-1].getTime())
        lastYear = last // 1000
        lastTime = last % 1000
    #print lastYear, lastTime
    curTime = time.localtime(time.time())
    curYear = curTime[0]

##    for year in range(lastYear, curYear+1):
##        begTime = 0
##        endTime = 366
##        if year==lastYear:
##            begTime = lastTime+1
##        if year==curYear:
##            endTime = curTime[1] * 31 + curTime[2]
##        #print begTime, endTime
##        for day in range(begTime, endTime):
##            lotteryTime = str(year*1000 + day)
##            print lotteryTime
##            lottery = getLotteryPaiLie3(lotteryTime)
##            if lottery!=None:
##                allLottery.append(lottery)
##
##                numDanXuan, moneyDanXuan = lottery.getDanXuan()
##                numZuXuan3, moneyZuXuan3 = lottery.getZuXuan3()
##                numZuXuan6, moneyZuXuan6 = lottery.getZuXuan6()
##                fileLotteryText = ''
##                fileLotteryText = fileLotteryText + lottery.getTime() + ' ' +\
##                                  lottery.getNum() + ' ' + \
##                                  str(lottery.getMoneyIn()) + ' ' +  \
##                                  str(numDanXuan) + ' ' +  \
##                                  str(moneyDanXuan) + ' ' +  \
##                                  str(numZuXuan3) + ' ' +  \
##                                  str(moneyZuXuan3) + ' ' +  \
##                                  str(numZuXuan6) + ' ' +  \
##                                  str(moneyZuXuan6) + '\n'
##                f.write(fileLotteryText)
##                #print fileLotteryText
                                  
    f.close()
    return allLottery

def getPaiLie3NumValueSet():
    allLottery = readHistoryPaiLie3File('排列3.txt')
    valSet = []
    for lottery in allLottery:
        valSet.append(lottery.getNumValue())
    return valSet

def getPaiLie3NumSumValueSet():
    allLottery = readHistoryPaiLie3File('排列3.txt')
    valSet = []
    for lottery in allLottery:
        valSet.append(lottery.getNumElementSum())
    return valSet

def getPaiLie3NumGeWeiValueSet():
    allLottery = readHistoryPaiLie3File('排列3.txt')
    valSet = []
    for lottery in allLottery:
        valSet.append(lottery.getNumElementValue(0))
    return valSet

def getPaiLie3NumShiWeiValueSet():
    allLottery = readHistoryPaiLie3File('排列3.txt')
    valSet = []
    for lottery in allLottery:
        valSet.append(lottery.getNumElementValue(1))
    return valSet

def getPaiLie3NumBaiWeiValueSet():
    allLottery = readHistoryPaiLie3File('排列3.txt')
    valSet = []
    for lottery in allLottery:
        valSet.append(lottery.getNumElementValue(2))
    return valSet
