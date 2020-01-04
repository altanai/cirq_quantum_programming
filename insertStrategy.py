# circuit to add gates based on position of qubits
# 4 such strategies:
# - InsertStrategy.EARLIEST,
# - InsertStrategy.NEW,
# - InsertStrategy.INLINE and
# - InsertStrategy.NEW_THEN_INLINE

import cirq

# define the length of the grid.
length = 3
# define qubits on the grid.
qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]

circuit = cirq.Circuit()

#InsertStrategys describe how new insertions into Circuits place their gates

# apply the Hadamard gate H to every qubit whose row index plus column index is even
# InsertStrategys- Earliest ,  X gates sliding over to act at the earliest Moment
circuit.append([cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0],
               strategy=cirq.InsertStrategy.EARLIEST)

#  X gate to every qubit whose row index plus column index is odd
# InsertStrategys- NEW_THEN_INLINE ,  insert the gates so that they form individual Moment
circuit.append([cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1],
               strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

# print(circuit)

# staggered gates created by two Moments.
for i, m in enumerate(circuit):
    print('Moment {}: {}'.format(i, m))

# prints
# Moment 0: H((0, 0)) and H((0, 2)) and H((1, 1)) and H((2, 0)) and H((2, 2))
# Moment 1: X((0, 1)) and X((1, 0)) and X((1, 2)) and X((2, 1))

