import fastf1 as f1
from fastf1 import plotting
from fastf1.plotting import get_driver_style
from matplotlib import pyplot as plt
f1.Cache.enable_cache('C:/Users/Admin/OneDrive/Documents/Coding/Python/Learning_data_science/cache')

# Enable Matplotlib patches for plotting timedelta values and load
# FastF1's dark color scheme
plotting.setup_mpl(
    mpl_timedelta_support=True,
    color_scheme='fastf1'
)

#loading the session
session = f1.get_session(2025,'Monza','Race')
session.load()

#Race results
result = session.results

#Filtering the data
filtered_result = result.loc[:,['BroadcastName','Abbreviation','Position','TeamName']]

#Top 10 of the race
top10 = filtered_result.head(10)
top10['Position'] = top10['Position'].astype(int)

#Plot the data
plt.figure(figsize=(12,6))

for i, (_, row) in enumerate(top10.iterrows()):
    abv = row['Abbreviation']

    style = get_driver_style(abv, style=['color', 'linestyle'] ,session=session)

    drv_laps = session.laps.pick_driver(abv).copy()
    # Convert lap times to seconds
    drv_laps['LapTimeSeconds'] = drv_laps['LapTime'].dt.total_seconds()

    #Filter pitstops
    clean_laps = drv_laps[drv_laps['PitInTime'].isna() &
                      drv_laps['PitOutTime'].isna()
                      ]
    
    plt.plot(
        clean_laps['LapNumber'],
        clean_laps['LapTimeSeconds'],
        label=row['BroadcastName'],
        **style
    )

plt.title("Top 10 Drivers: Lap By Lap Race Pace ")
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
