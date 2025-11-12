import fastf1 as f1
from fastf1 import plotting
from matplotlib import pyplot as plt
f1.Cache.enable_cache('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/cache')

#loading the session
session = f1.get_session(2025,'Netherlands','Race')
telemetary = session.load()

#Race results
result = session.results

#Filtering the data
filtered_result = result.loc[:,['BroadcastName','DriverNumber','Abbreviation','FirstName','TeamName','Position','Status']]

#Top 3 of the race
top3 = filtered_result.head(3)
top3['Position'] = top3['Position'].astype(int)


#Rename columns
top3.rename(columns={
    'BroadcastName' : 'Driver',
    'DriverNumber' : 'Driver.No'
}, inplace=True)


#Plot the data
colors = ['orange','blue','cyan']

plt.figure(figsize=(10,6))

for i, (_, row) in enumerate(top3.iterrows()):
    drv_no = row['Abbreviation']
    driver_laps = session.laps.pick_driver(drv_no)
    fast_lap = driver_laps.pick_fastest()
    tel = fast_lap.get_telemetry()

    plt.plot(tel['Distance'], tel['Speed'], label=drv_no, color=colors[i])


plt.title("Top 3 Drivers: Fastest Lap Speed Comparison")
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.legend()
plt.grid(True)
plt.show()
