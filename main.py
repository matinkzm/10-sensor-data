import pandas as pd
import sqlite3

# convert the csv file into a dataframe
df = pd.read_csv("beach-water-quality-automated-sensors-1.csv")

# remove columns that have same value and just keep one of them
df.drop(["Measurement Timestamp Label", "Measurement ID"], axis=1, inplace=True)

# rename column name to use it as an object
df.rename(columns={"Measurement Timestamp": "Measurement_Timestamp"}, inplace=True)

# split the time stamp to sort the data using date only
df[['date', 'time', "AM/PM"]] = df.Measurement_Timestamp.str.split(expand=True)

# drop redundant columns
df.drop(['time', 'AM/PM'], axis=1, inplace=True)

# convert date into corrct format
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# dort by date column
df.sort_values(by="date", inplace=True)

# reindex the dataframe
df = df.reset_index(drop=True)

print(df.head(1000).to_string())
