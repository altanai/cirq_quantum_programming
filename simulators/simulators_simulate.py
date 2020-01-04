# run methods (run and run_sweep) on the simulator do not give access to the wave function of the quantum computer
# simulate methods (simulate, simulate_sweep, simulate_moment_steps) should be used if one wants to debug the circuit and get access to the full wave function

import cirq
from cirq import Simulator
import numpy as np

simulator = Simulator()

q0 = cirq.GridQubit(0, 0)
q1 = cirq.GridQubit(1, 0)

def basic_circuit(meas=True):
    sqrt_x = cirq.X**0.5
    yield sqrt_x(q0), sqrt_x(q1)
    yield cirq.CZ(q0, q1)
    yield sqrt_x(q0), sqrt_x(q1)
    if meas:
        yield cirq.measure(q0, key='q0'), cirq.measure(q1, key='q1')

circuit = cirq.Circuit()
circuit.append(basic_circuit(False))

print(circuit)

result = simulator.simulate(circuit, qubit_order=[q0, q1])

print(np.around(result.final_state, 3))


# Circuit :
# (0, 0): ───X^0.5───@───X^0.5───
#                    │
# (1, 0): ───X^0.5───@───X^0.5───
#

# Result
# [0.5+0.j  0. +0.5j 0. +0.5j 0.5+0.j ]
