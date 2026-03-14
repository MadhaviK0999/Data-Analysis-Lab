# HW 1 example : Calculate total revenue of the week

#from Creating_Dataframe_Coffeesolddata import Creating_Dataframe_Coffeesolddata
import Creating_Dataframe_Coffeesolddata as coffee

def calculate_total_revenue(revenue):
    total_revenue = sum(revenue)
    return total_revenue
print("Total revenue of the week : $", calculate_total_revenue(coffee.df['Revenue']))

#HW 2 example : Calculate daily average revenue
def calculate_daily_average_revenue(revenue):
    daily_average_revenue = sum(revenue) / len(revenue)
    return daily_average_revenue
print("Daily average revenue : $", calculate_daily_average_revenue(coffee.df['Revenue']))

#HW 3 example : Calculate max sales on the day of the week
def calculate_max_sales(coffee_sold):
    max_sales = max(coffee_sold)
    return max_sales
print("Max sales on the day of the week : ",calculate_max_sales(coffee.df['Coffee_Sold']), 'cups' )