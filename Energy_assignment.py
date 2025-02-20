import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns

# Load the CSV file into a DataFrame
energy_data = pd.read_csv(r"C:\Users\kolan\Documents\2025_Spring\ME5920\energydata_complete.csv")

energy_data['date'] = pd.to_datetime(energy_data['date'])

energy_data['day'] = energy_data['date'].dt.date  
energy_data['hour'] = energy_data['date'].dt.hour

# Compute NSM (Number of Seconds from Midnight)
energy_data['NSM'] = (
    energy_data['date'].dt.hour * 3600 +  # Convert hours to seconds
    energy_data['date'].dt.minute * 60 +  # Convert minutes to seconds
    energy_data['date'].dt.second  # Keep seconds
)

# Plot the data
plt.figure(figsize=(15, 7))
ax = plt.gca()
plt.plot(energy_data['date'], energy_data['Appliances'], linestyle='-')
plt.title('Energy over full period')
plt.xlabel('Dates')
plt.ylabel('energy usage')

plt.xticks(rotation=25, ha = 'right')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=14)) 
ax.xaxis.set_minor_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %H:%M'))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
plt.show()


# Ensure unique dates are in Timestamp format (not Python date)
unique_dates = pd.to_datetime(energy_data['date'].dt.date).unique()

# Pick a random start date from the available unique dates
random_index = np.random.randint(0, len(unique_dates) - 6)
start_date = unique_dates[random_index]
end_date = start_date + pd.Timedelta(days=7)

closer_look = energy_data[(energy_data['date'] >= start_date) & (energy_data['date'] < end_date)]

plt.figure(figsize=(12, 6))
ax = plt.gca()  # Get current axis

plt.plot(closer_look['date'], closer_look['T1'], linestyle='-')
plt.title(f"Appliance energy usage: {start_date.date()} to {end_date.date()}")

# X-axis formatting
plt.xlabel('Date & Time')
plt.ylabel('Energy usage')

plt.xticks(rotation=25, ha='right')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d %H:%M')) 




plt.show()

## part 2

# Aggregate hourly appliance consumption per day
heatmap_data = closer_look.groupby(['hour', 'day'])['Appliances'].mean().unstack()

# Plot the heatmap
plt.figure()
sns.heatmap(heatmap_data, cmap="coolwarm", annot=False, fmt=".1f", linewidths=0.5)

plt.title(f'Hourly Appliance Consumption for {start_date} to {end_date}')
plt.ylabel('Hour of the Day')
plt.xlabel('Day')
plt.xticks(rotation=25)
plt.yticks(rotation=0)
plt.show()

## part 3

#histogram
#plot hist
plt.figure(figsize=(8, 5))
plt.hist(energy_data['Appliances'], edgecolor='black')
#plt.xticks(range(10))
plt.xlabel("Consumption")
plt.ylabel("Frequency")
plt.title("Histogram of energy consumption")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


## Part 4

plt.figure(figsize=(10, 5))
plt.scatter(energy_data['NSM'], energy_data['Appliances'], alpha=0.5, color='b', s=10)  # Scatter plot

# Formatting
plt.xlabel("NSM (Seconds from Midnight)")
plt.ylabel("Energy Consumption (Appliances)")
plt.title("Energy Consumption vs. NSM")
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()


## Part 5

# Plot the data
plt.figure(figsize=(15, 7))
ax = plt.gca()
plt.plot(energy_data['Press_mm_hg'], energy_data['Appliances'], linestyle=':')
plt.title('Energy over Prssure')
plt.xlabel('mm_Hg')
plt.ylabel('energy usage')
plt.show()