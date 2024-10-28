import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('paygap.csv')

# List of countries to compare
countries = ["Brazil", "Argentina", "Chile"]

# Plot the wage gap over time for each country
for country in countries:
    country_data = data[data['country'] == country]
    plt.plot(country_data['Year'], country_data['Gender wage gap %'], label=country)

# Add labels and legend
plt.title("Gender Wage Gap Comparison")
plt.xlabel("Year")
plt.ylabel("Wage Gap (%)")
plt.legend()
plt.grid(True)
plt.show()
