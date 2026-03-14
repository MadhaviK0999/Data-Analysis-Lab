import Creating_Dataframe_Coffeesolddata as coffee
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

# Create Scatter Plot

plt.scatter(coffee.df['Temperature_F'], coffee.df['Coffee_Sold'], color='brown', s=100)

plt.title('Temperature vs. Coffee Sales')
plt.xlabel('Temperature (F)')
plt.ylabel('Cups of Coffee Sold')
plt.grid(True) # Adds a grid for easier reading

plt.show()

# Calculate the precise correlation number (-1 to 1)
correlation = coffee.df['Temperature_F'].corr(coffee.df['Coffee_Sold'])
print(f"Correlation Coefficient: {correlation:.2f}")