# 10-sensor-data

This is the 10th project from this link: https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea

I created a datapipeline to load sensor data from a csv file and do some transformation.

step 1: load the csv file into a dataframe
step 2: 3 columns have same value so I removed 2 of them to make the dataframe lighter
step 3: rename column name(replace space with underline) so i can use it as a object
step 4: split time stamp to date , time , AM/PM to use date to sort the data
step 5: convert date into correct format
step 6: sort dataframe first by date, if date was the same for two or more values sort them by time
step 7: drop duplicate columns
step 8: reindex the dataframe
step 9: create a local database and load the dataframe into it