# CNOT gate


from cirq.ops import CNOT
from cirq.devices import GridQubit

q0, q1 = (GridQubit(0, 0), GridQubit(0, 1))

print(q0 , q1)

print(CNOT.on(q0, q1))
print(CNOT(q0, q1))
# prints
# CNOT((0, 0), (0, 1))
# CNOT((0, 0), (0, 1))