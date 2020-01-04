# Moment
# collection of operations, each of which operates on a different set of qubits,
# and which conceptually represents these operations as occurring during this abstract time slice.

import cirq

qubits = [cirq.GridQubit(i, j)
          for i in range(2) for j in range(2)]

cz = cirq.CZ(qubits[0], qubits[1])
x = cirq.X(qubits[2])

moment = cirq.Moment([x, cz])

print(moment)
