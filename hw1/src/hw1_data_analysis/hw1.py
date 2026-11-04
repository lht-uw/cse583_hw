# Load libraries 
import pandas as pd # For data manipulation, cleaning, and analysis 
import matplotlib.pyplot as plt # For data visualization 

# Question 1: 
# Read the CSV file into a dataframe
df = pd.read_csv("bicycle_data.csv")

# Question 2: 
# Describe the columns in the dataframe and what data types they should be:
# The columns of the csv file are: "Date", "Fremont Bridge Sidewalks, south of N 34th St Total", "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk", 
# "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk" contained the following data types (in order): str, float64, float64, and float64.                                                                                                                                                                    
# It makes sense that the "Date" column would be a string because it contains mixed data, date and time, which are formatted differently. However, the 3 other columns
# should not be float64, which are decimals. Instead, they should be integers because these columns are counting bicycles/scooters and they should always be whole 
# numbers, so that is why I converted them from float64 to int64.

# Print out the column names of the bicycle data frame 
print(df.columns)

# Convert the data type from float64 (decimal) to int64 (integers)
# Used Int64 to handle any blank spaces or missing numbers
df['Fremont Bridge Sidewalks, south of N 34th St Total'] = df['Fremont Bridge Sidewalks, south of N 34th St Total'].astype('Int64')

# Convert the data type from float64 (decimal) to int64 (integers)
df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'].astype('Int64')

# Convert the data type from float64 (decimal) to int64 (integers)
df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'].astype('Int64')

# Question 3:
# Add a new column to the dataframe: The total (West + East) bicycle count
df['West + East Bicycle Count'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'] + df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk']
# Convert the Date column to datetime to use the Pandas Accessor to pull the hour and year
df['Date'] = pd.to_datetime(df['Date'])
# Add a new column to the dataframe: The hour of the day 
df['Hour of the Day'] = df['Date'].dt.hour
# Add a new column to the dataframe: The year 
df['Year'] = df['Date'].dt.year

# Question 4:
# Create a new dataframe with only the subset of data from the year 2016
df_2016 = df[df['Year'] == 2016]
# Output the first five rows of the 2016 dataframe 
print(df_2016.head())

# Question 5: 
# Find and extract all rows that contain at least one missing value (NaN)
rows_with_missing_data = df_2016[df_2016.isna().any(axis =1)]
# Print the row(s) with missing values
print(rows_with_missing_data)
# There is one row with missing data; 2016-03-13 02:00: there are missing values for both the West and East. 

# Question 6:  
# Plot hour of day (x axis) vs. total daily counts (y-axis)
plt.plot(df_2016['Hour of the Day'], df_2016['West + East Bicycle Count'])
plt.xlabel('Hours')
plt.ylabel('Total')
plt.title('Bicycle Counts By Hour')
plt.show
plt.savefig('counts_by_hour.png')

# Question 7: 
# Calculate the mean for each hour of the day 
hourly_averages = df_2016.groupby('Hour of the Day')['West + East Bicycle Count'].mean()
# Find the hour with the highest average 
busiest_hour = hourly_averages.idxmax()
# Finds the highest average number
highest_average_value = hourly_averages.max()

print(f"The busiest hour on average is: {busiest_hour}")
print(f"It had an average total of: {highest_average_value}")

# The busiest hour on average is 17. 