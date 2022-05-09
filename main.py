import pandas as p


df = p.read_csv("salaries_by_college_major.csv")

clean_df = df.dropna()  # cleans the dataframe from all the unwanted or empty data cells

# what is the highest starting salary major
highest_starting_salary_major = clean_df["Starting Median Salary"].idxmax()

major1 = clean_df["Undergraduate Major"].loc[highest_starting_salary_major]

# what college major has the highest mid_career salary
highest_mid_career_salary = clean_df["Mid-Career Median Salary"].idxmax()

major2 = clean_df["Undergraduate Major"].loc[highest_mid_career_salary]

# which college major has the lowest starting salary and how much do graduates earn after university
lowest_starting_salary = clean_df["Starting Median Salary"].idxmin()

major3 = clean_df["Undergraduate Major"].loc[lowest_starting_salary]

earining_after_university = clean_df["Starting Median Salary"].loc[lowest_starting_salary]

# which college major has the lowest mid-career salary and how much can people expect to earn with this degree

lowest_mid_career_salary = clean_df["Mid-Career Median Salary"].idxmax()

major4 = clean_df["Undergraduate Major"].loc[lowest_mid_career_salary]

# how much can people expect to earn with this degree
starting = clean_df.loc[lowest_mid_career_salary]["Starting Median Salary"]
mid = clean_df.loc[lowest_mid_career_salary]["Mid-Career Median Salary"]
mid_10 = clean_df.loc[lowest_mid_career_salary]["Mid-Career 10th Percentile Salary"]
mid_90 = clean_df.loc[lowest_mid_career_salary]["Mid-Career 90th Percentile Salary"]

avarage_salary = ((starting + mid + mid_10 + mid_90) / 4)

# find the lowest risk majors
'''
A low-risk major is a degree where there is a small difference between the lowest and highest salaries. 
In other words, if the difference between the 10th percentile and the 90th percentile earnings of your
major is small, then you can be more certain about your salary after you graduate.

How would we calculate the difference between the earnings of the 10th and 90th percentile?
Well, Pandas allows us to do simple arithmetic with entire columns, so all we need to do is
take the difference between the two columns:
'''
difference = clean_df["Mid-Career 90th Percentile Salary"].subtract(
    clean_df["Mid-Career 10th Percentile Salary"])
the_lowest_difference = difference.idxmin()
major5 = clean_df["Undergraduate Major"].loc[the_lowest_difference]

# inserting the new difference column to the existing data frame
clean_df.insert(1, "Difference (between mid_10, mid90)", difference)


# Sorting by the Lowest difference
low_risk = clean_df.sort_values('Difference (between mid_10, mid90)')


# Find the top 5 degrees with the highest values in the 90th percentile
top_5_90th_percentile = clean_df.sort_values(
    ["Mid-Career 90th Percentile Salary"])
top_5 = top_5_90th_percentile.tail()


# find the degrees with the greatest difference in salaries. Which majors have the largest difference between high and low earners after graduation.
greatest_differences = clean_df.sort_values(
    "Difference (between mid_10, mid90)")
top_5_differences = greatest_differences.tail()

# count how many majors we have in each category
count = clean_df.groupby("Group").count()

# Now can you use the .mean() method to find the average salary by group
avg_salary_per_group = clean_df.groupby("Group").mean()


# Number formats in the Output: The above is a little hard to read, isn't it? We can tell Pandas to print the numbers in our notebook to look like 1,012.45 with the following line
p.options.display.float_format = '{:,.2f}'.format
print(avg_salary_per_group)
