## CirQ Quantum programmming

CirQ is a python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.

Install

```bash
python3 -m pip install --upgrade pip
python3 -m pip install cirq 
```

dependencies 

For witing to pdf 
```bash
brew cask install mactex
```

### Circuis 

Can be either 

**Circuit**
Circuit is a collection of Moments. A Moment is a collection of Operations that all act during the same abstract time slice.

**schedule**
Schedules offer more control over quantum gates and circuits at the timing level




## Variational quantum algorithms

The variational method in quantum theory is a classical method for finding low energy states of a quantum system. 

In classical variational method to a system of n qubits, an exponential number (in n) of complex numbers are necessary to generically represent the wave function of the system. 

However with a quantum computer one can directly produce this state using a parameterized quantum circuit, and then by repeated measurements estimate the expectation value of the energy.