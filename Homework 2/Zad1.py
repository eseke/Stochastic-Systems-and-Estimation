import csv
import numpy
import matplotlib.pyplot as plt

def Newton(N,TetaSt,tol,maxIt,i):
    iter = numpy.zeros(11)
    iter[0] = TetaSt
    cnt=0
    lastTeta = TetaSt
    while cnt<maxIt :
        cnt = cnt + 1
        teta = 0
        for ii in range(0,9):
            teta = teta + 2*(result1[i,ii]-lastTeta)/(1+numpy.power(result1[i,ii]-lastTeta,2))

        tetaIz = 0
        for ii in range(0,9):
            tetaIz = tetaIz + 2*(numpy.power(result1[i,ii]-lastTeta,2)-1)/numpy.power(1+numpy.power(result1[i,ii]-lastTeta,2),2)

        if lastTeta<-15 :
            return [-2,iter]
        if lastTeta>15:
            return [6,iter]
        
        currTeta = lastTeta - teta/tetaIz
        iter[cnt] = currTeta
        if numpy.abs(lastTeta-currTeta)<tol :
            return [currTeta,iter]
        else:
            lastTeta = currTeta
    return [lastTeta,iter]


result1 = numpy.array(list(csv.reader(open("dom2_zad1.csv")))).astype("float")
result2 = numpy.zeros(100001)
teta = numpy.linspace(-15,15,100001)

k = 20
for ii in range(0,9):
    result2 = result2 + numpy.log(1/(numpy.pi*(1+numpy.power(result1[k,ii]-teta,2))))
plt.figure(1)
plt.plot(teta,result2)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l(θ)')
plt.title('Log-verodostojnosti')

result3 = numpy.zeros(100001)
for ii in range(0,9):
    result3 = result3 + 2*(result1[k,ii]-teta)/(1+numpy.power(result1[k,ii]-teta,2))
plt.figure(2)
plt.plot(teta,result3)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'(θ)')
plt.title('Prvi izvod log-verodostojnosti')

result4 = numpy.zeros(100001)
for ii in range(0,9):
    result4 = result4 + 2*(numpy.power(result1[k,ii]-teta,2)-1)/numpy.power(1+numpy.power(result1[k,ii]-teta,2),2)
plt.figure(3)
plt.plot(teta,result4)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'\'(θ)')
plt.title('Drugi izvod log-verodostojnosti')

k = 45
for ii in range(0,9):
    result2 = result2 + numpy.log(1/(numpy.pi*(1+numpy.power(result1[k,ii]-teta,2))))
plt.figure(4)
plt.plot(teta,result2)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l(θ)')
plt.title('Log-verodostojnosti')

result3 = numpy.zeros(100001)
for ii in range(0,9):
    result3 = result3 + 2*(result1[k,ii]-teta)/(1+numpy.power(result1[k,ii]-teta,2))
plt.figure(5)
plt.plot(teta,result3)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'(θ)')
plt.title('Prvi izvod log-verodostojnosti')

result4 = numpy.zeros(100001)
for ii in range(0,9):
    result4 = result4 + 2*(numpy.power(result1[k,ii]-teta,2)-1)/numpy.power(1+numpy.power(result1[k,ii]-teta,2),2)
plt.figure(6)
plt.plot(teta,result4)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'\'(θ)')
plt.title('Drugi izvod log-verodostojnosti')

k = 83
for ii in range(0,9):
    result2 = result2 + numpy.log(1/(numpy.pi*(1+numpy.power(result1[k,ii]-teta,2))))
plt.figure(7)
plt.plot(teta,result2)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l(θ)')
plt.title('Log-verodostojnosti')

result3 = numpy.zeros(100001)
for ii in range(0,9):
    result3 = result3 + 2*(result1[k,ii]-teta)/(1+numpy.power(result1[k,ii]-teta,2))
plt.figure(8)
plt.plot(teta,result3)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'(θ)')
plt.title('Prvi izvod log-verodostojnosti')

result4 = numpy.zeros(100001)
for ii in range(0,9):
    result4 = result4 + 2*(numpy.power(result1[k,ii]-teta,2)-1)/numpy.power(1+numpy.power(result1[k,ii]-teta,2),2)
plt.figure(9)
plt.plot(teta,result4)
plt.grid()
plt.xlabel('θ')
plt.ylabel('l\'\'(θ)')
plt.title('Drugi izvod log-verodostojnosti')

d = Newton(10,2.4,0.005,10,46)
plt.figure(10)
plt.stem(d[1],use_line_collection='true')
plt.xlabel('broj iteracije i')
plt.ylabel('Vrednost θ u i-toj iteraciji')
plt.title('Promena vrednostu θ pri Newton-Raphsonove metodi')

d = Newton(10,2.4,0.005,10,93)
plt.figure(11)
plt.stem(d[1],use_line_collection='false')
plt.xlabel('broj iteracije i')
plt.ylabel('Vrednost θ u i-toj iteraciji')
plt.title('Promena vrednostu θ pri Newton-Raphsonove metodi')

d = Newton(10,2.4,0.005,10,23)
plt.figure(12)
plt.stem(d[1],use_line_collection='true')
plt.xlabel('broj iteracije i')
plt.ylabel('Vrednost θ u i-toj iteraciji')
plt.title('Promena vrednostu θ pri Newton-Raphsonove metodi')
#a = Newton(10,1.8,0.005,10,result3,result4,k)

#result4 = numpy.zeros(101)

#for i in range(0,101):
#    tmp = 0;
#    for ii in range(0,9):
#        tmp = tmp + 2*(result1[k,ii]-teta[i])/(1+numpy.power(result1[k,ii]-teta[i],2))
#    result4[i] = tmp;

#plt.subplot(313)
#plt.plot(teta,result4)
#plt.show()

hist = numpy.zeros(100)
for i in range(0,100):
    d = Newton(10,2.4,0.005,10,i)
    hist[i] = d[0]
plt.figure(13)
plt.hist(numpy.array(hist),bins = 100,range=(-2,6))
plt.axvline(numpy.array(hist).mean(),color='r',linewidth =2)
plt.xlabel('θ')
plt.ylabel('Broj eksperimenata')
plt.title('Histogram estimiranih vrednosti θ')
plt.show()