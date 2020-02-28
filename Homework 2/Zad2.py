import csv
import numpy
import math
import matplotlib.pyplot as plt

result1 = numpy.array(list(csv.reader(open("gnss_data.csv")))).astype("float")

#parametri
Ts = 1

#matrice
A = numpy.matrix([[1, 1, 3/2],[0, 1, 1],[0, 0, 1]])
B = numpy.matrix([[3/2],[1],[1]])
C = numpy.matrix(100) 
H = numpy.matrix([1,0,0])
rez = numpy.zeros((100,9))

#iniclijalizacija
Spp = numpy.matrix([[0],[0],[0]])
Mpp = numpy.matrix([[10,0,0],[0,10,0],[0,0,10]])

for i in range(0,100):
    
    #predikcija
    Snp = A*Spp
    #varijansa predikcije
    if i <30:
        Q = 25
    elif i<70:
        Q = 0.25
    else:
        Q = 25
    Mnp = A*Mpp*numpy.matrix.transpose(A)+ B*Q*numpy.matrix.transpose(B)
    if math.isnan(result1[i]):
        #Kalmanovo pojacanje
        Kn = numpy.matrix([[0],[0],[0]])
        #korekcija
        Snn = Snp
        Spp = Snn
    else :
        #Kalmanovo pojacanje
        Kn = Mnp*numpy.matrix.transpose(H)*numpy.linalg.inv(C+H*Mnp*numpy.matrix.transpose(H))
        #korekcija
        Snn = Snp + Kn*(result1[i]-H*Snp)
        Spp = Snn
    #varijansa korekcije
    Mnn = (numpy.identity(3)-Kn*H)*Mnp
    Mpp = Mnn
    rez[i,:] = numpy.array([Spp[0,0],Spp[1,0],Spp[2,0],math.sqrt(Mpp[0,0]),math.sqrt(Mpp[1,1]),math.sqrt(Mpp[2,2]),Kn[0,0],Kn[1,0],Kn[2,0]])

plt.figure(1)
plt.plot(rez[:,0])
#plt.plot(result1)


plt.figure(1)
plt.plot(result1,label='izmereno')
plt.plot(rez[:,0],label='estimirano')
plt.plot(rez[:,0]+2*rez[:,3])
plt.plot(rez[:,0]-2*rez[:,3])
plt.xlabel('vreme t[s]')
plt.ylabel('polozaj p[m]')
plt.title('Izmerena i estimitana vrednost polozaja')
plt.legend()
plt.grid()

plt.figure(2)
plt.plot(rez[:,1])
plt.plot(rez[:,1]+2*rez[:,4])
plt.plot(rez[:,1]-2*rez[:,4])
plt.xlabel('vreme t[s]')
plt.ylabel('brzina v[m/s]')
plt.title('Estimitana vrednost brzine')
plt.grid()

plt.figure(3)
plt.plot(rez[:,2])
plt.plot(rez[:,2]+2*rez[:,5])
plt.plot(rez[:,2]-2*rez[:,5])
plt.xlabel('vreme t[s]')
plt.ylabel('ubrzanje a[m/s^2]')
plt.title('Estimitana vrednost ubrzanja')
plt.grid()

plt.figure(4)
plt.plot(rez[:,6],label='polozaja')
plt.plot(rez[:,7],label='brzine')
plt.plot(rez[:,8],label='ubrzanja')
plt.xlabel('vreme t[s]')
plt.title('Kalmanovo pojacanje')
plt.legend()
plt.grid()

plt.show()