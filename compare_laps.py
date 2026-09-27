import fastf1
import pandas as pd
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2024, 'Silverstone', 'Q')
session.load()
fastest_lap = session.laps.pick_fastest()
telemetry = fastest_lap.get_car_data().add_distance()

matlab_data = pd.read_csv('matlab_lap_data.csv')

# Normalize both to % of lap distance
telemetry['pct_distance'] = telemetry['Distance'] / telemetry['Distance'].max() * 100
matlab_data['pct_distance'] = matlab_data['Distance'] / matlab_data['Distance'].max() * 100

plt.figure(figsize=(10, 6))
plt.plot(telemetry['pct_distance'], telemetry['Speed'], label=f"Real F1 ({fastest_lap['Driver']}, Silverstone)")
plt.plot(matlab_data['pct_distance'], matlab_data['Speed'], label='MATLAB Simplified Model')
plt.xlabel('Lap Distance (%)')
plt.ylabel('Speed (km/h)')
plt.title('Simplified Model vs Real F1 Telemetry')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
