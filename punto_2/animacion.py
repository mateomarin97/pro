import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("./graficas")
x=np.linspace(0,100,1000)
datos= np.loadtxt("datos.dat")
for i in range(100000):
    if i%100==0:
        plt.figure(figsize=(10,10))
        plt.plot(x,datos[i,:])
        plt.xlim((0,100))
        plt.ylim((-5,5))
        plt.savefig("./graficas/"+str(i)+".jpg")
        plt.close()

os.system("sudo apt-get install imagemagick")
os.chdir("./graficas")
os.system("convert -delay 20 -loop 0 *.jpg cuerda.gif")
os.system("mv cuerda.gif ..")
os.chdir("..")
os.system("rm -rf graficas")
