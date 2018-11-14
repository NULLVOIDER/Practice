import cirq
import numpy as numpy
from cirq.devices import GridQubit
from cirq.google import XmonSimulator
length = 4
qubits = [cirq.GridQubit(x,y) for x in range(length) for y in range(length)]
print("qubits")

circuit = cirq.Circuit()
H1 = cirq.H(qubits[2])
TOFFOLI = cirq.TOFFOLI(qubits[2], qubits[3], qubits[4])
H2 = cirq.H(qubits[1])
H3 = cirq.H(qubits[2])
H4 = cirq.H(qubits[3])
CZ1 = cirq.CZ(qubits[2], qubits[1])
CZ2 = cirq.CZ(qubits[2], qubits[3])
moment1 = cirq.moment([H1])
moment2 = cirq.moment([TOFFOLI])
moment3 = cirq.moment([H1])
moment4 = cirq.moment([H2, H3, H4])
moment5 = cirq.moment([CZ1])
moment6 = cirq.moment([CZ2])
moment7 = cirq.moment([H2, H3, H4])

circuit = cirq.Circuit((moment1, moment2, moment3, moment4, moment5, moment6, moment7))
print(circuit)
simulator = Xmonsimulator()
result = simulator.simulate(circuit)
print(result)