from ahkab import run, new_dc, new_tran, diode
from ahkab.circuit import Circuit
from ahkab.plotting import plot_results
from ahkab import circuit, printing, time_functions
import numpy as np
import pylab as plt
#import diodemodel.py

PI = 3.14159

if __name__ == "__main__":
	cir = Circuit('LCR AC')
	#r1 = float(input("Resistance: ").strip())
	#c1 = float(input("Capacitor: ").strip())
	#l1 = float(input("Inductor: ").strip())
	#v = float(input("Voltage amplitude: ").strip())
	#f = float(input("Voltage frequency: ").strip())
	gnd = cir.get_ground_node()
	voltage_func = time_functions.sin(vo = 0, va = 5, freq = 0.05)
	cir.add_vsource('V', 'n1', gnd, 1, function = voltage_func)
	cir.add_resistor('R', 'n1', gnd, 100)
	cir.add_capacitor('C', 'n1', 'gnd', 5)
	cir.add_inductor('L', 'gnd', gnd, 5)
	analysis = new_tran(0, 100, 1000, x0 = None)
	r = run(cir, analysis)
	print(r['tran'].keys())
	fig = plt.figure()
	plt.plot(r['tran']['T'], r['tran'][''], label = "Plot")
	plt.legend()
	plt.plot()
	plt.grid(True)
	plt.ylabel('Voltage')
	plt.xlabel('Time [s]')
	fig.savefig('Volatge.png')