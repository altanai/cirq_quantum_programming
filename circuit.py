# circuit to add gates based on position of qubits

import cirq

# define the length of the grid.
length = 3
# define qubits on the grid.
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]

circuit = cirq.Circuit()

# apply the Hadamard gate H to every qubit whose row index plus column index is even
circuit.append(cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0)

#  X gate to every qubit whose row index plus column index is odd
circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1)

print(circuit)
# (0, 0): ───H───   (0, 1): ───X───   (0, 2): ───H───
#
# (1, 0): ───X───   (1, 1): ───H───   (1, 2): ───X───
#
# (2, 0): ───H───   (2, 1): ───X───   (2, 2): ───H───