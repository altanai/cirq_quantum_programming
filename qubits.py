# Cirq has built in GridQubits

import cirq

# define the length of the grid.
length = 3
# define qubits on the grid.
qubits = [cirq.GridQubit(i, j)
for i in range(length) for j in range(length)]
print(qubits)

# prints
# [cirq.GridQubit(0, 0), cirq.GridQubit(0, 1), cirq.GridQubit(0, 2),
# cirq.GridQubit(1, 0), cirq.GridQubit(1, 1), cirq.GridQubit(1, 2),
# cirq.GridQubit(2, 0), cirq.GridQubit(2, 1), cirq.GridQubit(2, 2)]
