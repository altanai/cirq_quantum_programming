# Run Pure State simulation

import cirq
from cirq import Simulator

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
circuit.append(basic_circuit())

print(circuit)

simulator = Simulator()
result = simulator.run(circuit)

print(result)

# Circuit :
# (0, 0): ───X^0.5───@───X^0.5───M('q0')───
#                    │
# (1, 0): ───X^0.5───@───X^0.5───M('q1')───

# Result
# q0=0
# q1=1
