# Invertible gates and operations
# cirq.inverse has a default parameter used as a fallback when value isn’t invertable.
# cirq.inverse(value, default=None) returns the inverse of value, or else returns None if value isn’t invertable.

import cirq

def main():
    # Pick a qubit.
    qubit = cirq.GridQubit(0, 0)

    # Create a circuit
    circuit = cirq.Circuit(
        # cirq.X(qubit),  # NOT.
        cirq.X(qubit) ** -1,  # __pow__ -1.
        # cirq.X(qubit) ** 0.5,  # Square root of NOT.
        cirq.measure(qubit, key='m')  # Measurement.
    )
    print("Circuit:")
    print(circuit)

    # Simulate the circuit several times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=5)
    print("Results:")
    print(result)


if __name__ == '__main__':
    main()
