import cirq

qubits = [cirq.GridQubit(i, j)
for i in range(2) for j in range(2)]

# Pauli-X gate apply
# (   0 1
#     1 0  )

print("before operation -")
print(qubits[2])

x_gate = cirq.X
# Applying it to the qubit at location (1, 0)
x_op = x_gate(qubits[2])
print("after x_gate operation -")
print(x_op)

y_gate = cirq.Y
y_op = y_gate(qubits[2])
print("after y_gate operation -")
print(y_op)

z_gate = cirq.Z
z_op = z_gate(qubits[2])
print("after z_gate operation -")
print(z_op)