# Multiple moments
# Circuit is an iterable of Moments

import cirq

qubits = [cirq.GridQubit(i, j)
          for i in range(2) for j in range(2)]

cz01 = cirq.CZ(qubits[0], qubits[1])
x2 = cirq.X(qubits[2])
cz12 = cirq.CZ(qubits[1], qubits[2])

moment0 = cirq.Moment([cz01, x2])
moment1 = cirq.Moment([cz12])

circuit = cirq.Circuit((moment0, moment1))

print(circuit)

# (0, 0): ───@───────
#            │
# (0, 1): ───@───@───
#                │
# (1, 0): ───X───@───
