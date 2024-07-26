#!/usr/bin/env python3
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now_datetime, get_datetime

def create_test_doctype():
    # Define the DocType properties
    doctype = {
        "doctype": "DocType",
        "name": "Testdoctype",
        "module": "Estate App",  # Change module to 'Estate App'
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

    # Check if DocType already exists
    if not frappe.db.exists("DocType", "Testdoctype"):
        # Insert the new DocType
        doc = frappe.get_doc(doctype)
        doc.insert()
        print("DocType 'Testdoctype' created successfully.")
    else:
        print("DocType 'Testdoctype' already exists.")

# Run the function to create the DocType
if __name__ == "__main__":
    create_test_doctype()
