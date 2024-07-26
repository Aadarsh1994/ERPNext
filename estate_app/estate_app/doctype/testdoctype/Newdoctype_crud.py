import requests

# Configuration
base_url = 'http://localhost:8000/api/resource/Newdoctype'  # Updated base URL
auth = ('03d776654d221ec', '4310883ab7a8714')
newdoctype_name = None  # Variable to store the created Newdoctype's name

def create_newdoctype():
    global newdoctype_name
    data = {
        "title": "Custom Title",
        "description": "A description of the new doctype.",
        "field1": "Value 1",
        "field2": "Value 2",
        "is_active": 1,
        "status": "Active"
    }
    response = requests.post(base_url, json=data, auth=auth)
    if response.status_code == 200:
        print("Create:", response.json())
    
        newdoctype_name = response.json().get('data', {}).get('name')
    else:
        print("Failed to create Newdoctype:", response.json())

def read_newdoctype():
    if newdoctype_name:
        response = requests.get(f"{base_url}/{newdoctype_name}", auth=auth)
        print("Read:", response.json())
    else:
        print("Newdoctype name not defined. Create a Newdoctype first.")

def update_newdoctype():
    if newdoctype_name:
        data = {
            "field1": "Updated Value 1"
        }
        response = requests.put(f"{base_url}/{newdoctype_name}", json=data, auth=auth)
        print("Update:", response.json())
    else:
        print("Newdoctype name not defined. Create a Newdoctype first.")

def delete_newdoctype():
    if newdoctype_name:
        response = requests.delete(f"{base_url}/{newdoctype_name}", auth=auth)
        print("Delete:", response.status_code)  # 204 indicates success
    else:
        print("Newdoctype name not defined. Create a Newdoctype first.")

# Main function to orchestrate the operations
def main():
    input("Press Enter to create Newdoctype...")
    create_newdoctype()
    
    input("Press Enter to read Newdoctype...")
    read_newdoctype()
    
    input("Press Enter to update Newdoctype...")
    update_newdoctype()
    
    input("Press Enter to delete Newdoctype...")
    delete_newdoctype()

if __name__ == "__main__":
    main()
