# optimization/mix_optimizer.py

from pulp import *
import csv

# Create the optimization model
model = LpProblem("Energy Optimization", LpMinimize)

# Decision variables: Energy share (0 to 1)
solar = LpVariable('solar', 0, 1)
wind = LpVariable('wind', 0, 1)
coal = LpVariable('coal', 0, 1)

# Emission per source (gCO2/kWh)
emissions = {'solar': 50, 'wind': 20, 'coal': 900}

# Objective: minimize total emissions
model += emissions['solar'] * solar + emissions['wind'] * wind + emissions['coal'] * coal

# Constraints: energy needs and total mix
model += solar + wind + coal == 1
model += 0.04*solar + 0.06*wind + 0.1*coal <= 0.07  # Cost constraint (sample)

# Solve the optimization problem
model.solve()

# Save the optimization results to a CSV file
optimized_data = {
    'Energy Source': ['Solar', 'Wind', 'Coal'],
    'Share': [solar.varValue, wind.varValue, coal.varValue],
    'Emissions (gCO2/kWh)': [emissions['solar'], emissions['wind'], emissions['coal']]
}

# Define the CSV file path
csv_file_path = "optimized_energy_mix.csv"

# Write results to CSV
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Energy Source', 'Share', 'Emissions (gCO2/kWh)'])
    writer.writeheader()
    for i in range(len(optimized_data['Energy Source'])):
        writer.writerow({
            'Energy Source': optimized_data['Energy Source'][i],
            'Share': optimized_data['Share'][i],
            'Emissions (gCO2/kWh)': optimized_data['Emissions (gCO2/kWh)'][i]
        })

# Print the results to console as well
for v in model.variables():
    print(f"{v.name}: {v.varValue}")

print(f"\nOptimization results saved to {csv_file_path}")
