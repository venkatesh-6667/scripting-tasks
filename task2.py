import requests
import csv

def fetch_data_to_csv(api_url, csv_filename):
    # Fetch data from the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        universities_data = response.json()  # Parse JSON response

        # Define CSV headers
        csv_headers = ['Name', 'Country', 'Domain', 'Web Page']

        # Write data to CSV file
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()

            for university in universities_data:
                # Extract necessary data from the JSON response
                university_data = {
                    'Name': university.get('name', ''),
                    'Country': university.get('country', ''),
                    'Domain': university.get('domains', [''])[0],  # Assuming a single domain
                    'Web Page': university.get('web_pages', [''])[0]  # Assuming a single web page
                }
                writer.writerow(university_data)

        print(f"Data written to {csv_filename}")
    else:
        print("Failed to fetch data from the API")

# API endpoint and CSV filename
api_url = 'http://universities.hipolabs.com/search?country=Canada'
csv_filename = 'universities_canada.csv'

# Fetch data and write to CSV
fetch_data_to_csv(api_url, csv_filename)

