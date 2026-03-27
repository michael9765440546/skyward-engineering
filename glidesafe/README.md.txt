# GlideSafe – Emergency Glide Decision Tool

 Overview

This is a simple Python-based project that simulates an emergency situation where an aircraft loses engine power and has to rely on gliding.

Some aircraft operate with a single engine, while most commercial aircraft have two engines. In rare cases, both engines can fail, and in such situations the aircraft must glide to a safe landing location. This program is built around that idea.

It helps estimate whether the aircraft can reach nearby airports based on its current position, altitude, and glide capability, and suggests the most suitable option.

---

 How the Program Works

The program takes a few basic inputs from the user:

* Current latitude and longitude (aircraft position)
* Altitude (in meters)
* Glide ratio (efficiency of the aircraft)
* Current heading (direction the aircraft is facing)
* Wind condition (no wind, headwind, or tailwind)

---

 Glide Distance Calculation

First, the program calculates the theoretical glide distance using:

* Altitude
* Glide ratio

Then it adjusts the distance based on:

* Wind effect (reduces or increases distance)
* Safety margin (only 80% of total glide is considered usable)

---

 Direction and Navigation

For each airport, the program:

* Calculates distance using geographic coordinates
* Finds the direction (e.g., North-East, South-West)
* Computes the heading required to reach the airport

---

 Turn Penalty

If the aircraft needs to turn to align with the airport:

* A turn angle is calculated
* A penalty is applied (larger turns reduce glide efficiency)

This represents the loss of efficiency during maneuvering.

---

 Decision Logic

For every airport, the program checks whether it is within the adjusted glide distance.

It then classifies the result as:

* **Safe** – comfortably reachable
* **Risky** – just within range
* **Not Reachable** – outside glide capability

Finally, it suggests the best airport based on distance.

---

Visualization

The program also generates a simple map using matplotlib:

* Aircraft position
* Airport locations
* Paths between them

This helps visualize the situation more clearly.

---

 How to Run

1. Make sure Python is installed on your system.
2. Install the required library:

   ```bash
   pip install matplotlib
   ```
3. Open terminal or command prompt.
4. Navigate to the project folder:

   ```bash
   cd glidesafe
   ```
5. Run the program:

   ```bash
   python glidesafe.py
   ```
6. Enter the required inputs when prompted.

---

 Limitations

This is a simplified simulation and does not include:

* Terrain (mountains, obstacles)
* Weather variations beyond basic wind
* Aircraft weight and configuration
* Real-time aerodynamics

The goal is to understand the concept, not to provide real-world flight decisions.
