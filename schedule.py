# Schedule
# contains more timing information above and beyond that which is provided by the Moment structure of a Circuit

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
# circuit.append([cirq.CZ(device.qubits[0], device.qubits[2])])
circuit.append([cirq.CZ(device.qubits[0], device.qubits[1]), cirq.X(device.qubits[0])])
print(circuit)

try:
  # device.validate_circuit(circuit)
  schedule = cirq.moment_by_moment_schedule(device, circuit)


  # Schedules support helpers for querying about the time-space layout of the schedule
  print(schedule[cirq.Timestamp(nanos=5)])
  print(schedule[cirq.Timestamp(nanos=15)])

  # slice
  slice = schedule[cirq.Timestamp(nanos=5):cirq.Timestamp(nanos=15)]
  slice_schedule = cirq.Schedule(device, slice)
  print(slice_schedule == schedule)

except ValueError as e:
  print(e)