import requests

base_url = 'http://localhost:8000/api/resource/Student'
auth = ('03d776654d221ec', '3d71c451b3d7161')

regno = "0000000"

# Check if the student already exists
response = requests.get(f"{base_url}/{regno}", auth=auth)
if response.status_code == 200:
    print("Student already exists:", response.json())
else:
    # Create
    data = {
        "regno": regno,
        "stud_name": "arun kumar",
        "dob": "2000-01-01",
        "gender": "Male",
        "mob_no": "7894561235",
        "email":"asdrfr@gmail.com"
    }
    response = requests.post(base_url, json=data, auth=auth)
    print("Create:", response.json())

# Read
response = requests.get(f"{base_url}/{regno}", auth=auth)
print("Read:", response.json())

# Update
data = {
    "dob": "2000-01-02"
}
response = requests.put(f"{base_url}/{regno}", json=data, auth=auth)
print("Update:", response.json())

# Delete
response = requests.delete(f"{base_url}/{regno}", auth=auth)
print("Delete:", response.status_code)  # 204 indicates success
