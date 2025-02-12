import matplotlib
matplotlib.use('Agg')  # Force Matplotlib to use a non-interactive backend
import matplotlib.pyplot as plt

import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Pharmacokinetic model: Single-compartment IV bolus
def drug_model(t, y, k_elim):
    # dy/dt = -k_elim * y (exponential decay)
    dydt = -k_elim * y
    return dydt

# Parameters
k_elim = 0.1  # Elimination rate constant (per hour)
dose = 100     # Initial dose (mg)
t_span = (0, 24)  # Simulation time: 0 to 24 hours

# Initial condition (drug concentration at t=0)
y0 = [dose]

# Solve the differential equation
solution = solve_ivp(
    drug_model,
    t_span,
    y0,
    args=(k_elim,),
    dense_output=True,
    t_eval=np.linspace(0, 24, 100)
)

# Extract results
t = solution.t
concentration = solution.y[0]

# Plot results
# Plot results
fig = plt.figure(figsize=(10, 6))
plt.plot(t, concentration, 'b-', linewidth=2, label='Drug Concentration')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (mg/L)')
plt.title('Drug Concentration Over Time (IV Bolus)')
plt.grid(True)
plt.legend()

# Tight layout to prevent clipped labels
plt.tight_layout()

# Save the plot
output_dir = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(output_dir, exist_ok=True)

# Save with high resolution and explicit format
plt.savefig(
    os.path.join(output_dir, 'drug_concentration_plot.png'),
    dpi=300,
    bbox_inches='tight'
)
plt.close(fig)  # Close the figure explicitly

##Chnage##