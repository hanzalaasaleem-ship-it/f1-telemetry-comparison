import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache')

# 2024 Silverstone Quali
session = fastf1.get_session(2024, 'Silverstone', 'Q')
session.load()

fastest_lap = session.laps.pick_fastest()
telemetry = fastest_lap.get_car_data().add_distance()

print(f"Driver: {fastest_lap['Driver']}")
print(f"Lap Time: {fastest_lap['LapTime']}")
print(telemetry[['Distance', 'Speed']].head(10))

plt.plot(telemetry['Distance'], telemetry['Speed'])
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.title(f"{fastest_lap['Driver']} - Silverstone 2024 Q - Fastest Lap")
plt.show()
