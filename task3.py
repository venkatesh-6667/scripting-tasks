import csv
import requests

# Function to update records via the provided API endpoint
def update_records_via_api(csv_filename, api_endpoint):
    # Read data from CSV file
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Process data from CSV (modify as per your CSV structure)
            university_name = row['Name']  # Assuming 'Name' as a field in your CSV
            country = row['Country']  # Assuming 'Country' as a field in your CSV
            domain = row['Domain']  # Assuming 'Domain' as a field in your CSV
            web_page = row['Web Page']  # Assuming 'Web Page' as a field in your CSV

            # Prepare payload for POST request (example payload)
            payload = {
                'name': university_name,
                'country': country,
                'domain': domain,
                'web_pages': [web_page]
            }

            # Check if the university already exists via API (assuming GET request)
            response = requests.get(api_endpoint, params={'name': university_name})

            if response.status_code == 200:
                # University exists, perform PUT/PATCH request to update
                update_url = f"{api_endpoint}/{university_name}"  # Replace with actual update URL
                update_response = requests.put(update_url, json=payload)  # Use PUT or PATCH as required
                if update_response.status_code == 200:
                    print(f"University {university_name} updated successfully.")
                else:
                    print(f"Failed to update university {university_name}.")
            elif response.status_code == 404:
                # University doesn't exist, perform POST request to create
                create_response = requests.post(api_endpoint, json=payload)
                if create_response.status_code == 201:
                    print(f"University {university_name} created successfully.")
                else:
                    print(f"Failed to create university {university_name}.")

# CSV filename and API endpoint
csv_filename = '/root/datalogixs/universities_canada.csv'  # Replace with your CSV filename and path
api_endpoint = 'http://universities.hipolabs.com/search'  # Your API endpoint

# Update records via API
update_records_via_api(csv_filename, api_endpoint)

