import csv

# Define the headers for the CSV file
headers = [
    'image',
    'first_name',
    'last_name',
    'joiningDate',
    'mobile',
    'gender',
    'status',
    'designation',
    'department',
    'dateOfBirth',
    'education',
    'user_id',
    'email'
]

# Sample data for demonstration purposes
teachers_data = [
    {
        'image': 'image1.jpg',
        'first_name': 'John',
        'last_name': 'Doe',
        'joiningDate': '2020-01-15',
        'mobile': '1234567890',
        'gender': 'Male',
        'status': 'Active',
        'designation': 'Professor',
        'department': 'Computer Science',
        'dateOfBirth': '1980-05-12',
        'education': 'PhD',
        'user_id': '001',
        'email': 'john.doe@example.com'
    },
    {
        'image': 'image2.jpg',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'joiningDate': '2019-08-23',
        'mobile': '0987654321',
        'gender': 'Female',
        'status': 'Active',
        'designation': 'Assistant Professor',
        'department': 'Mathematics',
        'dateOfBirth': '1985-09-20',
        'education': 'MSc',
        'user_id': '002',
        'email': 'jane.smith@example.com'
    }
]

# Specify the file name
file_name = 'teachers.csv'

# Write the data to the CSV file
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for teacher in teachers_data:
        writer.writerow(teacher)

print(f"CSV file '{file_name}' created successfully.")
