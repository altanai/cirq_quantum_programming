# Schedule and Circuit are the two major container classes for quantum circuits.

import cirq
from cirq.devices import GridQubit

class Xmon10Device(cirq.Device):

  def __init__(self):
      self.qubits = [GridQubit(i, 0) for i in range(10)]

  def duration_of(self, operation):
      return cirq.Duration(nanos=10)

  def validate_operation(self, operation):
      if not isinstance(operation, cirq.GateOperation):
          raise ValueError('{!r} is not a supported operation'.format(operation))

      if not isinstance(operation.gate, (cirq.CZPowGate,
                                         cirq.XPowGate,
                                         cirq.PhasedXPowGate,
                                         cirq.YPowGate)):
          raise ValueError('{!r} is not a supported gate'.format(operation.gate))

      if len(operation.qubits) == 2:
          p, q = operation.qubits
          if not p.is_adjacent(q):
            raise ValueError('Non-local interaction: {}'.format(repr(operation)))

  def validate_scheduled_operation(self, schedule, scheduled_operation):
      self.validate_operation(scheduled_operation.operation)

  def validate_circuit(self, circuit):
      for moment in circuit:
          for operation in moment.operations:
              self.validate_operation(operation)

  def validate_schedule(self, schedule):
      for scheduled_operation in schedule.scheduled_operations:
          self.validate_scheduled_operation(schedule, scheduled_operation)


device = Xmon10Device()
circuit = cirq.Circuit()
circuit.append([cirq.CZ(device.qubits[0], device.qubits[2])])
print(circuit)
try:
  device.validate_circuit(circuit)
except ValueError as e:
  print(e)