# main.py
"""
Stochastic SIR-style simulation (4 states: normal, bitten, dead, zombie)
Produces a plot similar to the image you provided.

How it works (matching the UserModel shown in your screenshots):
- Start population with proportions:
    normal = 0.92, bitten = 0.08, dead = 0.0, zombie = 0.0
- Per-step events:
    - Infection pressure: bitten individuals contribute to ambient infection,
      and susceptibles (normal) receive infection with a probability proportional
      to ambient * beta.
    - State transitions:
        normal -> bitten   with p = 0.10
        bitten -> dead     with p = 0.099
        dead   -> zombie   with p = 0.07
- All transitions are applied stochastically (binomial draws).
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import random

# ---- Simulation parameters ----
SEED = 42                 # reproducible
np.random.seed(SEED)
random.seed(SEED)

POPULATION = 50           # matches agents.txt (50) from video screenshot
DAYS = 30                 # 0..30
BETA = 0.45               # infection intensity (tune to produce similar curves)
# The "UserModel" transition probabilities from screenshots:
P_NORMAL_TO_BITTEN = 0.10
P_BITTEN_TO_DEAD = 0.099
P_DEAD_TO_ZOMBIE = 0.07

# Starting proportions from UserModel (screenshot)
PROP_NORMAL = 0.92
PROP_BITTEN = 0.08
PROP_DEAD = 0.0
PROP_ZOMBIE = 0.0

# ---- Initialize populations ----
init_bitten = int(round(POPULATION * PROP_BITTEN))
init_normal = POPULATION - init_bitten  # dead/zombie are zero initially
init_dead = 0
init_zombie = 0

# arrays to store time series
t = np.arange(DAYS + 1)
normal_ts = np.zeros(DAYS + 1, dtype=float)
bitten_ts = np.zeros(DAYS + 1, dtype=float)
dead_ts = np.zeros(DAYS + 1, dtype=float)
zombie_ts = np.zeros(DAYS + 1, dtype=float)

normal_ts[0] = init_normal
bitten_ts[0] = init_bitten
dead_ts[0] = init_dead
zombie_ts[0] = init_zombie

# helper: ambient infection contributed by bitten agents
def compute_ambient(bitten_count):
    # Each bitten contributes 1 unit to ambient (this is arbitrary scale)
    return float(bitten_count)

# simulation loop (stochastic)
for day in range(DAYS):
    S = int(round(normal_ts[day]))
    I = int(round(bitten_ts[day]))
    D = int(round(dead_ts[day]))
    Z = int(round(zombie_ts[day]))

    # 1) Infection pressure: susceptibles can become bitten due to ambient
    ambient = compute_ambient(I)
    # per-susceptible infection probability (mass-action style)
    if POPULATION > 0:
        # use BETA*(ambient / POPULATION) as force of infection
        inf_prob = 1.0 - np.exp(-BETA * (ambient / float(POPULATION)))
        inf_prob = min(max(inf_prob, 0.0), 1.0)
    else:
        inf_prob = 0.0

    new_infections = np.random.binomial(S, inf_prob) if S > 0 else 0

    # 2) Natural disease progression (stochastic transitions)
    new_dead = np.random.binomial(I, P_BITTEN_TO_DEAD) if I > 0 else 0
    new_zombie = np.random.binomial(D, P_DEAD_TO_ZOMBIE) if D > 0 else 0

    # 3) (Optional) background infection: some small fraction of normals spontaneously bitten
    #    Not necessary, commented out. Uncomment to add background noise.
    # background = np.random.binomial(S, 0.001)

    # update counts
    S_next = S - new_infections
    I_next = I + new_infections - new_dead
    D_next = D + new_dead - new_zombie
    Z_next = Z + new_zombie

    # numerical safety: don't go negative
    S_next = max(0, S_next)
    I_next = max(0, I_next)
    D_next = max(0, D_next)
    Z_next = max(0, Z_next)

    normal_ts[day + 1] = S_next
    bitten_ts[day + 1] = I_next
    dead_ts[day + 1] = D_next
    zombie_ts[day + 1] = Z_next

# ---- Plotting ----
plt.figure(figsize=(14,7))
plt.plot(t, normal_ts, label='normal', linewidth=2)
plt.plot(t, bitten_ts, label='bitten', linewidth=2)
plt.plot(t, dead_ts, label='dead', linewidth=2)
plt.plot(t, zombie_ts, label='zombie', linewidth=2)

plt.title('Stochastic SIR Plot', fontsize=16)
plt.xlabel('Time Steps (in unit steps)', fontsize=12)
plt.ylabel('Population', fontsize=12)
plt.grid(True, which='both', linestyle='-', linewidth=0.6, alpha=0.6)
plt.legend(frameon=True)

# style tweaks to more closely match your screenshot
ax = plt.gca()
ax.set_axisbelow(True)
ax.set_yticks(np.arange(0, max(50, int(POPULATION*0.9)) + 1, 5))
ax.set_xticks(np.arange(0, DAYS+1, 2))
ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()

# Save and show
out_dir = "results"
os.makedirs(out_dir, exist_ok=True)
png_path = os.path.join(out_dir, "stochastic_sir_plot.png")
plt.savefig(png_path, dpi=150)
print("Saved plot to:", png_path)
plt.show()
