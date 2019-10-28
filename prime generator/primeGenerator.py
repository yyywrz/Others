import time
from pathlib import Path

class primeGen:
    def __init__(self,runtime,timetrigger):
        print('start')
        self.rt = runtime;
        self.tt = timetrigger;
        self.arr = []

    def initPrimeNumFile(self):
        file = Path("primeNum.txt")
        if file.exists():
            return
        else:
            with open('primeNum.txt','w') as f:
                f.write('2 3 5 7 11')
            print('creat file')

    def getPrevious(self):
        with open('primeNum.txt') as f:
            line=f.read()
            for x in line.split(' '):
                self.arr.append(int(x))

    def isPrime(self,i):
        for x in self.arr:
            if (i%x==0):
                return False
        return True

    def calculatePrime(self):
        elapse = 0
        beginning = time.time()
        initPoint = self.arr[-1]
        startCount = len(self.arr);
        i = initPoint
        while elapse<self.tt:
            i=i+2
            if self.isPrime(i):
                self.arr.append(i)
                with open('primeNum.txt','a') as f:
                    f.write(' '+str(i))
            elapse = time.time() - beginning
        endCount = len(self.arr);
        endPoint = self.arr[-1]
        print('\nThere were already '+str(startCount)+\
        ' prime numbers. Start from '+str(initPoint)+\
            ', end in '+str(endPoint)+', with '+\
                str(self.tt)+' seconds, '+\
                    str(endCount-startCount)+\
                        ' prime numbers are added. Now there are '\
                            +str(endCount)+' prime numbers\n')

    def timeTrigger(self):
        elapse = 0
        beginning = time.time()
        while elapse<self.rt:
            self.calculatePrime()
            elapse = time.time() - beginning
    
    def run(self):
        self.initPrimeNumFile()
        self.getPrevious()
        self.timeTrigger()



def getInput():
    timePeriod = int(input('Please input running time (s) :'))
    timetrigger = int(input('Please input time trigger(s) :'))
    return (timePeriod,timetrigger)

if __name__=='__main__':
    (a,b) = getInput()
    pm = primeGen(a,b)
    pm.run()
