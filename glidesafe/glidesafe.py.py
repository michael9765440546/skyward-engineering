import math
import matplotlib.pyplot as plt


# --- basic distance using haversine ---
def distance_km(lat1, lon1, lat2, lon2):
    R = 6371  # earth radius

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# --- just to know direction in simple words ---
def direction(lat1, lon1, lat2, lon2):
    vertical = "North" if lat2 > lat1 else "South"
    horizontal = "East" if lon2 > lon1 else "West"
    return f"{vertical}-{horizontal}"


# --- bearing (direction in degrees) ---
def bearing(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    dlon = math.radians(lon2 - lon1)

    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)

    angle = math.degrees(math.atan2(x, y))
    return (angle + 360) % 360


# --- turn logic ---
def turn_angle(current, target):
    angle = abs(current - target)
    if angle > 180:
        angle = 360 - angle
    return angle


def turn_penalty(angle):
    if angle < 30:
        return 0.95
    elif angle < 90:
        return 0.9
    else:
        return 0.85


# --- airports (simple and real) ---
airports = [
    {"name": "Kathmandu", "lat": 27.697, "lon": 85.359},
    {"name": "Pokhara", "lat": 28.200, "lon": 83.982},
    {"name": "Simara", "lat": 27.159, "lon": 84.981},
    {"name": "Biratnagar", "lat": 26.481, "lon": 87.263},
    {"name": "Lukla", "lat": 27.688, "lon": 86.732},
]


print("GlideSafe – simple glide checker")
print("---------------------------------")


# --- inputs ---
lat = float(input("Current latitude: "))
lon = float(input("Current longitude: "))
altitude = float(input("Altitude (meters): "))
glide_ratio = float(input("Glide ratio (e.g. 15): "))
current_heading = float(input("Current heading (0–360): "))


# --- wind input ---
print("\nWind?")
print("1. No wind")
print("2. Headwind")
print("3. Tailwind")

wind = int(input("Choose: "))


# --- basic glide calculation ---
glide = (altitude / 1000) * glide_ratio

if wind == 2:
    glide *= 0.9
elif wind == 3:
    glide *= 1.1

usable = glide * 0.8


print("\nGlide distance:", round(glide, 2), "km")
print("Usable distance:", round(usable, 2), "km")


reachable = []


print("\n--- results ---")

for a in airports:
    dist = distance_km(lat, lon, a["lat"], a["lon"])

    target_head = bearing(lat, lon, a["lat"], a["lon"])
    turn = turn_angle(current_heading, target_head)

    penalty = turn_penalty(turn)

    adjusted_glide = usable * penalty

    status = "Not Reachable"
    if dist <= adjusted_glide:
        status = "Reachable"
    elif dist <= adjusted_glide * 0.7:
        status = "Risky"

    time = (dist / 200) * 60

    print(
        f"{a['name']} | "
        f"Dist: {round(dist,2)} km | "
        f"{direction(lat, lon, a['lat'], a['lon'])} | "
        f"Head: {round(target_head,1)}° | "
        f"Turn: {round(turn,1)}° | "
        f"Penalty: {penalty} | "
        f"Glide: {round(adjusted_glide,2)} km | "
        f"Time: {round(time,1)} min | "
        f"{status}"
    )

    if status != "Not Reachable":
        reachable.append((a["name"], dist))


# --- best option ---
if reachable:
    best = min(reachable, key=lambda x: x[1])
    print("\nBest airport to aim for:", best[0])
else:
    print("\nNo safe airport in reach.")


# --- simple map ---
plt.figure()

plt.scatter(lon, lat)
plt.text(lon, lat, "You")

for a in airports:
    plt.scatter(a["lon"], a["lat"])
    plt.text(a["lon"], a["lat"], a["name"])

    plt.plot([lon, a["lon"]], [lat, a["lat"]], linestyle="--")

plt.title("GlideSafe Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.grid()
plt.show()