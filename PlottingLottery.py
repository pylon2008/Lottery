# coding=gbk
from GetWebLotteries import *
import pylab

def plotPaiLie3NumValue(valSet):
    print len(valSet)
    #pylab.figure()
    pylab.title('排列三历史中奖号码')
    pylab.xlabel('期数')
    pylab.ylabel('中奖号码')
##    pylab.semilogx()
##    pylab.semilogy()
    pylab.plot(range(len(valSet)), valSet, 'bo')
    pylab.show()

if __name__ =="__main__":
    valSet = getPaiLie3NumValueSet()
    print valSet
    #plotPaiLie3NumValue(valSet)
    

