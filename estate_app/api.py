# erpnext/accounts/doctype/sales_invoice/api.py
import frappe
import requests
import json
@frappe.whitelist(allow_guest=True)
def fetch_custom_extended_grand_total(doc,id):
    #Example API endpoint and parameters
    api_url = "http://localhost:8000/api/method/erpnext.accounts.doctype.sales_invoice.api.fetch_custom_extended_grand_total"
    doc=frappe.get_doc('Sales Invoice',"ACC-SINV-2024-00015")
    frappe.throw("hai")


    d=doc.as_dict()
    frappe.throw(d.get("grand_total"))






















    # # Fetch data from the external API
    # try:
    #     response = requests.get(api_url, params=params)
    #     # response.raise_for_status()
    #     # print(response.status_code)
        

    #     data = response.json()
    #     custom_extended_grand_total = data.get("grand_total")
    #     frappe.throw("hai 1")
    #     frappe.throw(custom_extended_grand_total)
    #     # print(f"API Response: {data}")

    #     # Update the Sales Invoice with the fetched grand total
    #     if custom_extended_grand_total is not None:
    #         doc.custom_extended_grand_total = 125
    # except requests.exceptions.RequestException as e:
    #     frappe.throw(f"Failed to fetch grand total from external API: {e}")






'''
    subject= frappe.get_doc('Sales Invoice', ID)
    
    

    # Save the document
    
    return subject.as_dict()



# import frappe
# import requests

# def fetch_custom_extended_grand_total(doc, method):
#     # Example API endpoint and parameters
#     api_url = "http://192.168.1.43:8000/get_total"
    
#     # Retrieve the actual invoice_id from the Sales Invoice document
#     invoice_id = frappe.get_value("Sales Invoice", doc.name, "invoice_id")
#     if not invoice_id:
#         frappe.throw(f"Invoice ID not found for Sales Invoice {doc.name}")

#     params = {
#         "invoice_id": invoice_id
#     }

#     # Fetch data from the external API
#     try:
#         response = requests.get(api_url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         custom_extended_grand_total = data.get("grand_total")

#         # Update the Sales Invoice with the fetched grand total
#         if custom_extended_grand_total is not None:
#             doc.custom_extended_grand_total = custom_extended_grand_total
#     except requests.exceptions.RequestException as e:
#         frappe.throw(f"Failed to fetch grand total from external API: {e}")
'''