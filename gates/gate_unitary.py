import cirq

print(cirq.X)
print(cirq.inverse(cirq.X, default=None))

print(cirq.unitary(cirq.X))

# [[0.+0.j 1.+0.j]
#  [1.+0.j 0.+0.j]]

sqrt_x = cirq.X**0.5
print(cirq.unitary(sqrt_x))

# [[0.5+0.5j 0.5-0.5j]
#  [0.5-0.5j 0.5+0.5j]]
