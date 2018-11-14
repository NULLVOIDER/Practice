from projectq.ops import  H, Measure
from projectq import MainEngine
def get_random_number(quantum_engine):
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number
random_numbers_list = []
quantum_engine = MainEngine()
for i in range(10):
    random_numbers_list.append(get_random_number(quantum_engine))
quantum_engine.flush()
print('Random numbers', random_numbers_list)