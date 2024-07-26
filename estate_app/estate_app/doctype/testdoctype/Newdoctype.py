import requests
import json

# Define the Frappe API endpoint and authentication details
base_url = 'http://localhost:8000/api/resource/DocType'
auth = ('03d776654d221ec', '4310883ab7a8714')

# Define the new DocType properties
doctype_payload = {
    "doctype": "DocType",
    "name": "Newdoctype",
    "module": "Estate App",
    "custom": 1,
    "fields": [
    {
        "fieldname": "title",
        "fieldtype": "Data",
        "label": "Title",
        "reqd": 1
    },
    {
        "fieldname": "description",
        "fieldtype": "Text",
        "label": "Description"
    },
    {
        "fieldname": "age",
        "fieldtype": "Int",
        "label": "Age"
    },
    {
        "fieldname": "birth_date",
        "fieldtype": "Date",
        "label": "Birth Date"
    },
    {
        "fieldname": "is_active",
        "fieldtype": "Check",
        "label": "Is Active"
    },
    {
        "fieldname": "status",
        "fieldtype": "Select",
        "label": "Status",
        "options": "Active\nInactive\nPending"
    }
    ],
    "permissions": [
        {
            "role": "System Manager",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        }
    ]
}

# Send a POST request to create the new DocType
response = requests.post(base_url, json=doctype_payload, auth=auth)

# Check the response
if response.status_code == 200:
    print("DocType 'Newdoctype' created successfully.")
else:
    print("Failed to create DocType. Response:", response.json())
