# scripting-tasks
#This repo consists of two tasks
1. Fetch Data from API and Write to CSV.
2. Update Records via API from CSV.

#Task2-Description:

This script retrieves data from below API endpoint and writes the fetched information to a CSV file. 
# http://universities.hipolabs.com/search?country=Canada
The data fetched from the API pertains to universities in Canada and includes fields such as 'Name', 'Country', 'Domain', and 'Web Page'. The script processes the JSON response received from the API and writes it into a  below CSV file
# universities_canada.csv

To get data from API and write it into csv file run the following command on task2 file.

```python3 ./task2
```
After executing the script it will create the csv file



##Task3:
#Description:

In this task we are using the csv file that we created in task 2 #universities_canada.csv

task3.py script facilitates updating or creating records in API endpoint below using data from a CSV file.
# http://universities.hipolabs.com/search?country=Canada

To get the record from the csv file via API, Execute the following command 

```
python3 ./task3.py
```
Note: We are unable to update or post records in the Above API as we don't have full cotrol over the site. 
I create a sample script 'task3.py' on how to update and create records.
