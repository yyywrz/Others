import time

def initPrimeNumFile():
    from pathlib import Path
    file = Path("primeNum.txt")
    if file.exists():
        return
    else:
        with open('primeNum.txt','w') as f:
            f.write('2 3 5 7 11')

def getPrevious():
    arr=[]
    with open('primeNum.txt') as f:
        line=f.read()
        for x in line.split(' '):
            arr.append(int(x))
    return arr

def isPrime(i,a):
    for x in a:
        if (i%x==0):
            return False
    return True


def calculatePrime(a,i,t):
    elapse = 0
    beginning = time.time()
    while elapse<t:
        i=i+2
        if isPrime(i,a):
            a.append(i)
            with open('primeNum.txt','a') as f:
                f.write(' '+str(i))
        elapse = time.time() - beginning

if __name__=='__main__':
    initPrimeNumFile()
    primeArr = getPrevious()
    initPoint = primeArr[-1]
    timePeriod = 2*60*60
    calculatePrime(primeArr,initPoint,timePeriod)
