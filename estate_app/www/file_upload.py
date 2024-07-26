# import frappe
# from frappe.utils.file_manager import save_file

# @frappe.whitelist(allow_guest=True)
# def upload_file():
#     try:
#         uploaded_file = frappe.request.files['file']
#         file_url = save_file(uploaded_file.filename, uploaded_file.stream.read(), 'Subject', 'new', is_private=0)
#         # Ensure file_url is returned in the expected format
#         return frappe._dict(message={'file_url': file_url})
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), str(e))
#         # Log the error and return a consistent error response
#         return frappe._dict(exception=str(e), exc_type=type(e).__name__, exc=frappe.get_traceback())





import frappe
from frappe.utils.file_manager import save_file

@frappe.whitelist(allow_guest=True)
def upload_file():
    try:
        uploaded_file = frappe.request.files['file']
        file_url = save_file(uploaded_file.filename, uploaded_file.stream.read(), 'Subject', 'new', is_private=0)
        # Ensure file_url is returned in the expected format
        return frappe._dict(message={'file_url': file_url})
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), str(e))
        # Log the error and return a consistent error response
        return frappe._dict(exception=str(e), exc_type=type(e).__name__, exc=frappe.get_traceback())
