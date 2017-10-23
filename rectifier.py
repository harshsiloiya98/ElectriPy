from ahkab import run, new_dc, new_tran, diode
from ahkab.circuit import Circuit
from ahkab.plotting import plot_results
from ahkab import circuit, printing, time_functions
import numpy as np
import pylab as plt
PI = 3.14159

if __name__ == "__main__":
	cir = Circuit("TEST")
	r0 = 500
	rl = 1000
	c = 1
	gnd = cir.get_ground_node()
	voltage_func = time_functions.sin(vo = 0, va = 10, freq = 0.05)
	cir.add_vsource('V', 'n1', 'n2', 1, function = voltage_func)
	cir.add_model(model_type = "diode", model_label = 'x', model_parameters = {"name": "rect"})
	cir.add_diode('D1', gnd, 'n1', model_label = 'x')
	cir.add_diode('D2', 'n1', 'n3', model_label = 'x')
	cir.add_diode('D3', gnd, 'n2', model_label = 'x')
	cir.add_diode('D4', 'n2', 'n3', model_label = 'x')
	#cir.add_resistor('R', 'gnd', 'n1', r0)
	cir.add_resistor('R_L', 'n3', gnd, rl)
	#cir.add_capacitor('C', 'n3', gnd, c)
	analysis = new_tran(0, 100, 10000, x0 = None)
	r = run(cir, analysis)
	print(r['tran'].keys())
	fig = plt.figure()
	plt.plot(r['tran']['T'], r['tran']['Vn3'], label = "Output Voltage")
	plt.legend()
	plt.plot()
	plt.grid(True)
	plt.ylabel('V [V]')
	plt.xlabel('T [s]')
	fig.savefig('Voltage4.png')