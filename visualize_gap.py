import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('paygap.csv')

# Choose a country to analyze (e.g., Brazil)
country = "Brazil"
country_data = data[data['country'] == country]

# Plot the wage gap over time for the selected country
plt.plot(country_data['Year'], country_data['Gender wage gap %'], marker='o')
plt.title(f"Gender Wage Gap in {country} Over Time")
plt.xlabel("Year")
plt.ylabel("Wage Gap (%)")
plt.grid(True)
plt.show()
