import math
import matplotlib.pyplot as plt

print("Aircraft Takeoff Runway Distance Calculator")

weight = float(input("Enter aircraft weight (Newtons): "))
wing_area = float(input("Enter wing area (m^2): "))
lift_coefficient = float(input("Enter lift coefficient (Cl): "))
drag_coefficient = float(input("Enter drag coefficient (Cd): "))
thrust = float(input("Enter engine thrust (Newtons): "))
rolling_resistance = float(input("Enter rolling resistance coefficient: "))

air_density = 1.225
gravity = 9.81
mass = weight / gravity

# Stall speed
stall_speed = math.sqrt((2 * weight) / (air_density * wing_area * lift_coefficient))
print(f"\nStall speed: {stall_speed:.2f} m/s ({stall_speed * 1.944:.2f} knots)")

takeoff_speed = 1.2 * stall_speed
print(f"Takeoff speed: {takeoff_speed:.2f} m/s ({takeoff_speed * 1.944:.2f} knots)")

# Initial rolling resistance
rolling_resistance_force = rolling_resistance * weight

initial_net_force = thrust - rolling_resistance_force
if initial_net_force <= 0:
    print("\nError: Thrust is not enough to overcome rolling resistance.")
    exit()

initial_acceleration = initial_net_force / mass
print(f"Initial acceleration: {initial_acceleration:.2f} m/s²")

# Estimate runway distance using simulation
distances = []
velocities = []

dt = 0.1
current_velocity = 0
current_distance = 0

while current_velocity < takeoff_speed:
    distances.append(current_distance)
    velocities.append(current_velocity)

    # Drag increases with velocity
    drag_force = 0.5 * air_density * current_velocity**2 * wing_area * drag_coefficient

    # Rolling resistance decreases slightly as speed increases (approximation)
    rolling_force = rolling_resistance_force * (1 - 0.1 * (current_velocity / takeoff_speed))

    net_force = thrust - drag_force - rolling_force
    acceleration = net_force / mass

    # Update motion
    current_velocity = current_velocity + acceleration * dt
    current_distance = current_distance + current_velocity * dt

runway_distance = current_distance
print(f"Estimated runway distance: {runway_distance:.2f} m ({runway_distance/1000:.3f} km)")

# Plot
plt.figure(figsize=(10,6))
plt.plot(distances, velocities, linewidth=2)
plt.axhline(y=takeoff_speed, linestyle='--', label=f"Takeoff Speed ({takeoff_speed:.1f} m/s)")
plt.axvline(x=runway_distance, linestyle='--', label=f"Runway Distance ({runway_distance:.1f} m)")
plt.xlabel("Runway Distance (m)")
plt.ylabel("Velocity (m/s)")
plt.title("Takeoff Roll Simulation: Velocity vs Runway Distance")
plt.grid(True)
plt.legend()
plt.savefig("takeoff_plot.png", dpi=150)
print("Graph saved as takeoff_plot.png")
plt.show()