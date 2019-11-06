import time
from pathlib import Path

class primeGen:
    def __init__(self, upper_bound=0, runtime=0, timetrigger=1):
        print('start')
        self.upper_bound = upper_bound
        self.rt = runtime
        self.tt = timetrigger
        self.arr = []
        if (upper_bound < 2 and runtime <= 0):
            print('invaild input!')
            
    def __initPrimeNumFile(self):
        file = Path("primeNum.data")
        if file.exists():
            return
        else:
            with open('primeNum.data','w') as f:
                f.write('2\t3\t5\t7\t11')
            print('creat file')

    def getPrimeArr(self):
        with open('primeNum.data') as f:
            line=f.read()
            for x in line.split('\t'):
                self.arr.append(int(x))

    def __isPrime(self,i):
        for j in range(0,round(pow(len(self.arr),0.5))):
            if (i%self.arr[j]==0):
                return False
        return True

    def __timeStop(self,i,beginning):
        elapse = 0
        with open('primeNum.data','a') as f:
            while elapse<self.tt:
                i=i+2
                if self.__isPrime(i):
                    self.arr.append(i)
                    f.write('\t'+str(i))
                elapse = time.time() - beginning

    def __upperBoundStop(self,i):
        with open('primeNum.data','a') as f:
            while i<self.upper_bound:
                i=i+2
                if self.__isPrime(i):
                    self.arr.append(i)
                    f.write('\t'+str(i))
        with open('prime_Nums_Under_'+str(self.upper_bound)+'.data','w') as f:
            print('creat file')
            for x in self.arr:
                if x<self.upper_bound:
                    f.write('\t'+str(x))
                else:
                    return

    def getinfo(self):
        self.info='Generator has not started yet!'
        if len(self.arr)!=0:
            initPoint = self.arr[-1]
            startCount = len(self.arr);
            endPoint = self.arr[-1]
            self.info=('\nThere were '+str(startCount)+\
                ' prime numbers in primeNum.data, ending in ' \
                    + str(endPoint))
            if self.upper_bound!=0 and \
                Path('prime_Nums_Under_'+str(self.upper_bound)+'.data').exists():
                    self.info=self.info+'\nprime_Nums_Under_'+str(self.upper_bound)+\
                        '.data is generated, which contains all prime numbers under '\
                            +str(self.upper_bound)
        return self.info

    def timeTrigger(self):
        elapse = 0
        beginning = time.time()
        while elapse<self.rt:
            self.__timeStop(self.arr[-1],time.time())
            elapse = time.time() - beginning
            print(self.getinfo())
    
    def run(self):
        self.__initPrimeNumFile()
        self.getPrimeArr()
        if self.rt >0:
            self.timeTrigger()
        if self.upper_bound > 1 :
            self.__upperBoundStop(self.arr[-1])
        self.getinfo()

def getInput():
    timePeriod = int(input('Please input running time (s) :'))
    timetrigger = int(input('Please input time trigger(s) :'))
    upper_bound=int(input('Please input upper bound(integer): '))
    return (timePeriod,timetrigger,upper_bound)

if __name__=='__main__':
    (a,b,c) = getInput()
    pm = primeGen(upper_bound=c, runtime=a,timetrigger=b)
    pm.run()
    print(pm.info)
    del pm