import cirq
import random

def rand2d(rows, cols):
    return [[random.choice([+1, -1]) for _ in range(cols)] for _ in range(rows)]

def random_instance(length):
    # transverse field terms
    h = rand2d(length, length)
    # links within a row
    jr = rand2d(length - 1, length)
    # links within a column
    jc = rand2d(length, length - 1)
    return (h, jr, jc)

def rot_x_layer(length, half_turns):
    """Yields X rotations by half_turns on a square grid of given length."""
    rot = cirq.XPowGate(exponent=half_turns)
    for i in range(length):
        for j in range(length):
            yield rot(cirq.GridQubit(i, j))

def rot_z_layer(h, half_turns):
    """Yields Z rotations by half_turns conditioned on the field h."""
    gate = cirq.ZPowGate(exponent=half_turns)
    for i, h_row in enumerate(h):
        for j, h_ij in enumerate(h_row):
            if h_ij == 1:
                yield gate(cirq.GridQubit(i, j))

def rot_11_layer(jr, jc, half_turns):
    """Yields rotations about |11> conditioned on the jr and jc fields."""
    gate = cirq.CZPowGate(exponent=half_turns)
    for i, jr_row in enumerate(jr):
        for j, jr_ij in enumerate(jr_row):
            if jr_ij == -1:
                yield cirq.X(cirq.GridQubit(i, j))
                yield cirq.X(cirq.GridQubit(i + 1, j))
            yield gate(cirq.GridQubit(i, j),
                       cirq.GridQubit(i + 1, j))
            if jr_ij == -1:
                yield cirq.X(cirq.GridQubit(i, j))
                yield cirq.X(cirq.GridQubit(i + 1, j))

    for i, jc_row in enumerate(jc):
        for j, jc_ij in enumerate(jc_row):
            if jc_ij == -1:
                yield cirq.X(cirq.GridQubit(i, j))
                yield cirq.X(cirq.GridQubit(i, j + 1))
            yield gate(cirq.GridQubit(i, j),
                       cirq.GridQubit(i, j + 1))
            if jc_ij == -1:
                yield cirq.X(cirq.GridQubit(i, j))
                yield cirq.X(cirq.GridQubit(i, j + 1))

def one_step(h, jr, jc, x_half_turns, h_half_turns, j_half_turns):
    length = len(h)
    yield rot_x_layer(length, x_half_turns)
    yield rot_z_layer(h, h_half_turns)
    yield rot_11_layer(jr, jc, j_half_turns)

h, jr, jc = random_instance(3)

circuit = cirq.Circuit()
circuit.append(one_step(h, jr, jc, 0.1, 0.2, 0.3),
               strategy=cirq.InsertStrategy.EARLIEST)
print(circuit)

#                   ┌──────────┐       ┌──────────┐       ┌──────────┐
# (0, 0): ───X^0.1────X──────────────────@─────────────X────@─────────────────────────────────────────
#                                        │                  │
# (0, 1): ───X^0.1─────────@─────────────┼──────────────────@^0.3─────────X───────@───────X───────────
#                          │             │                                        │
# (0, 2): ───X^0.1────X────┼─────────────┼────@────────X────X─────────────────────@^0.3───X───────────
#                          │             │    │
# (1, 0): ───X^0.1────Z^0.2┼────────X────@^0.3┼────────X────@─────────────X───────@───────X───────────
#                          │                  │             │                     │
# (1, 1): ───X^0.1─────────@^0.3────X────@────┼────────X────┼────X────────────────@^0.3───X───@───────
#                                        │    │             │                                 │
# (1, 2): ───X^0.1────Z^0.2─────────X────┼────@^0.3────X────┼────@────────────────────────────@^0.3───
#                                        │                  │    │
# (2, 0): ───X^0.1────Z^0.2──────────────┼──────────────────@^0.3┼────────@───────────────────────────
#                                        │                       │        │
# (2, 1): ───X^0.1────X──────────────────@^0.3─────────X─────────┼────────@^0.3───@───────────────────
#                                                                │                │
# (2, 2): ───X^0.1────Z^0.2──────────────────────────────────────@^0.3────────────@^0.3───────────────
#                    └──────────┘       └──────────┘       └──────────┘
