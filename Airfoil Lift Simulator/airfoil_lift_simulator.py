import numpy as np
import matplotlib.pyplot as plt

# Constants
rho = 1.225  # Air density at sea level (kg/m^3)

# User inputs
wing_area = float(input("Enter wing area (m^2): "))
cl = float(input("Enter lift coefficient (Cl): "))

# Specific velocity for single-point calculation
v_specific = float(input("Enter a specific velocity (m/s) to calculate lift: "))
lift_specific = 0.5 * rho * v_specific**2 * wing_area * cl
print(f"Lift at {v_specific} m/s = {lift_specific:.2f} N")

# Velocity range for graph
v_min = float(input("Enter minimum velocity for graph (m/s): "))
v_max = float(input("Enter maximum velocity for graph (m/s): "))
v_steps = int(input("Enter number of points in velocity range: "))

velocities = np.linspace(v_min, v_max, v_steps)
lift = 0.5 * rho * velocities**2 * wing_area * cl

# Plot lift vs velocity
plt.plot(velocities, lift, label=f"Cl={cl}, Wing Area={wing_area} m²")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift Force (N)")
plt.title("Airfoil Lift vs Velocity")
plt.grid(True)
plt.legend()
plt.show()