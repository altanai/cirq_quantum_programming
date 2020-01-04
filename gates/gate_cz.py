# CZ or controlled-Z  phase gate
# 2 qubit gate
import cirq
from cirq.ops import CZ, H

q0, q1, q2 = [cirq.GridQubit(i, 0) for i in range(3)]
circuit = cirq.Circuit()
circuit.append([CZ(q0, q1), H(q2)])

print(circuit)
