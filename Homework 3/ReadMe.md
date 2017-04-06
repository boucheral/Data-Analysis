# Homework 3

*All .py files assume there is a folder Homework3/Data with the csv files in the data structure*

## Question 1 - Part 1

* Downloaded csv with `pd.read_csv()`
* Created 2 functions `countM(x)` and `percent(x)` to use for calculations
* Created `df16` from `df` with only the dates in 2016
* Created function `months(x)` to figure out which month the date was in
* Added a new column with the month
* used `groupby()` to group by the month and `agg()` with 'count' and the functions I defined to get the calculations I needed
* `result.to_csv()` to save


## Question 1 - Part 2

* Downloaded csv with `pd.read_csv()`
* Added columns for each of the categories
* Iterated through rows to find out the number of cars and update the row
* Converted columns to numeric
* Used `pd.pivot_table(df, index='BOROUGH',aggfunc='sum')` to add up the number of crashes in each category
* `result.to_csv()` to save

## Question 2 - Part 1

* Downloaded csv with `pd.read_csv()`
* Replaced na with 'missing' in columns I was interested in
* Selected the columns I was interested in, pivoted the table on 'Organization Group' and 'Department', aggfunc='mean', and sorted by 'Total Compensation'
* `result.to_csv()` to save

## Question 2 - Part 2

* Downloaded csv with `pd.read_csv()`
* Filtered data by `df['Year Type'] == 'Calendar'`
* Grouped result by 'Employee Identifier' and calculated the averages for that employee
* Selected all rows where `df['Overtime'] / df['Salaries'] >= 0.05`
* Added a new column where the value was the percent of benefits based off total compensation
* Selected the columns I was interested in, grouped by 'Job Family', and calculated mean
* `result.to_csv()` to save

## Question 3

* Downloaded csv with `pd.read_csv()`
* Filtered results so that I was working with only the rows where `df['home'] == df['winner']`
* Created function `winningScore()` to figure out what the score of the winning team was.
* Used `df.apply()` to add a column for the winning team's score
* Selected the columns I was interested in, pivoted the table on 'home', and used `aggfunc='mean'` to calculate the averaged
* `result.to_csv()` to save

*I know literally nothing about cricket. What I was able to tell from the assignment and the internet I took the score to be the number of runs the winning team scored in the inning they played. If that is incorrect, please take mercy on me. I tried!*

## Question 4

* Downloaded csv with `pd.read_csv()`
* Created various functions to extract the values I needed from the string in `pd['Awards']`
* Used `df.apply()` to create new columns with the values in each award section
* joined the original table with new columns
* `result.to_csv()` to save




