Skyward Engineering - Takeoff Distance Simulator

Project Overview:
This Python-based Takeoff Distance Simulator estimates how much runway an aircraft needs to take off. Enter the aircraft weight, wing area, lift coefficient, drag coefficient, thrust, and rolling resistance, and the program calculates stall speed, takeoff speed, initial acceleration, and runway distance. It also plots a velocity vs distance graph to show how the aircraft accelerates along the runway, giving a simple visual understanding of takeoff physics.

Formula Used:
The program uses basic physics equations:

Lift Equation: L = 0.5 × ρ × V² × S × Cl (for stall speed)

Acceleration: a = (thrust – drag – rolling resistance) / mass

Runway Distance: s = V² / (2 × a) (simplified kinematics)

Where:

L = lift force in Newtons (N)

ρ = air density (1.225 kg/m³ at sea level)

V = velocity in m/s

S = wing area in m²

Cl = lift coefficient
Drag = aerodynamic drag

Thrust = engine force in N

Rolling resistance = friction of wheels

Mass = aircraft mass in kg

Graph Explanation:
The graph shows how the aircraft’s velocity increases along the runway.

X-axis: runway distance in meters

Y-axis: aircraft velocity in m/s

It demonstrates how the plane accelerates from zero up to takeoff speed and helps visualize how drag and rolling resistance affect acceleration.

How to Run:
Run the program using:
python "takeoff distance simulator.py"

Enter the aircraft parameters when prompted. The program will calculate speeds, runway distance, and save the velocity vs distance graph automatically.

This project gives a practical look at how engineers estimate takeoff distances. While simplified, it’s a clear and visual way to understand aircraft physics.
