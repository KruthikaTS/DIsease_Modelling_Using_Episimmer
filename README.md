# Disease Modelling Epidemic Simulation 


This project demonstrates how epidemic progression can be modelled using a
simplified version of the Episimmer framework.

Episimmer is an epidemic simulation platform that allows users to define
agents, locations, policies, events, and disease models to study how infections
spread under different scenarios. This project recreates the essential
components required to run a minimal epidemic simulation, including:

- **Agent definitions**
- **Location definitions**
- **Daily event schedules**
- **Policy functions**
- **A custom disease progression model**
- **A stochastic SIR-based simulation with visualization**

---

## 🔬 Overview

This project models a population of agents who move between different
locations based on daily schedules. A disease model governs how individuals 
transition between health states (e.g., normal → bitten → dead → zombie),
with transitions occurring probabilistically.

A policy module allows lockdown rules to be applied on certain days of the
week, mimicking real-world interventions such as school closures or weekend
lockdowns.

The simulation produces a **time-series graph** showing how the number of
individuals in each state changes over time.

---

## 📁 Project Structure

```

.
├── agents.txt                # List of agents and their attributes
├── locations.txt             # List of locations in the system
├── event_files_list.txt      # Index of all daily event files
│
├── monday.txt                # Daily schedule: location -> agents
├── tuesday.txt
├── wednesday.txt
├── thursday.txt
├── friday.txt
├── saturday.txt
├── sunday.txt
│
├── UserModel.py              # Disease model (state transitions + infection rules)
├── Generate_policy.py        # Lockdown policy implementation
├── generate_files.py         # Script to regenerate agents, locations & event files
├── main.py                   # Runs the simulation & produces the epidemic curve
│
└── results/
└── stochastic_sir_plot.png   # Output graph of epidemic progression

```

---

## 🧠 Key Components

### **1. Disease Model (`UserModel.py`)**
Defines:
- health states (`normal`, `bitten`, `dead`, `zombie`)
- state transition probabilities
- event contribution & infection functions

This governs how the disease spreads and progresses.

---

### **2. Policy Module (`Generate_policy.py`)**
Implements a weekly lockdown rule.  
Lockdown is triggered on selected days based on:

```

time_step % 7 in [0, 3, 5]

```

Policies can restrict movement or modify infection spread.

---

### **3. Event & Schedule Files**
Each weekday file (e.g., `wednesday.txt`) defines:
- number of locations
- which agents visit each location on that day

These files determine how agents interact each day.

---

### **4. Stochastic SIR Simulation (`main.py`)**
A standalone simulation that:
- initializes a population
- applies infection logic
- models state transitions stochastically
- generates a line plot of:
  - normal
  - bitten
  - dead
  - zombie populations

Uses:
- **NumPy** for stochastic sampling  
- **Matplotlib** for visualization

---

## ▶ How to Run

### **1. Create & Activate Virtual Environment**
```

python -m venv venv
venv\Scripts\activate

```

### **2. Install Dependencies**
```

pip install numpy matplotlib

```

### **3. Run Simulation**
```

python main.py

```

Output:
- A graph window showing disease spread over time.
- A saved image at:
```

results/stochastic_sir_plot.png

```

## 📌 Future Extensions

You can extend this project by:
- Adding real Episimmer engine components
- Simulating multiple worlds
