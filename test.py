from ahkab import new_ac, run, new_dc , new_tran
from ahkab.circuit import Circuit
from ahkab.plotting import plot_results # calls matplotlib for you
from ahkab import circuit, printing, time_functions
import numpy as np
import pylab as plt

cir=Circuit('Dc_circuit with series components')
#r1=input("Value of Resistor: ")
#c1=input("Value of Capacitor: ")
#v1=input("Initial DC Voltage: ")
r1 = 500
gnd = cir.get_ground_node()
cir.add_vsource('V1','n1',gnd,dc_value=20,ac_value=0)
cir.add_resistor('R1','n1','n2',r1)
cir.add_capacitor('C1','n2',gnd,0.05)
tran_analysis=new_tran(0,100,10000,x0=None)
r=run(cir,tran_analysis)
fig = plt.figure() 
plt.plot(r['tran']['T'], r['tran']['Vn2'], label="Voltage across capacitor")

plt.legend()
plt.plot()
plt.grid(True)
plt.ylabel('Voltage')
plt.xlabel('Time [s]')
fig.savefig('Volatge.png')

fig = plt.figure() 
plt.plot(r['tran']['T'], (r['tran']['Vn1']-r['tran']['Vn2'])/r1 , label="Current through circuit")

plt.legend()
plt.plot()
plt.grid(True)
plt.ylabel('Current')
plt.xlabel('Time [s]')
fig.savefig('Current.png')