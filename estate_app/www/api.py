import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def register_student():
    import json
    from werkzeug.wrappers import Response

    data = frappe.local.form_dict

    try:
        student = frappe.get_doc({
            "doctype": "Student",
            "regno": data.get('regno'),
            "stud_name": data.get('stud_name'),
            "gender": data.get('gender'),
            "dob": data.get('dob'),
            "dept": data.get('dept'),
            "course": data.get('course'),
            "email": data.get('email'),
            "mob_no": data.get('mob_no'),
            "fathers_name": data.get('fathers_name'),
            "mothers_name": data.get('mothers_name'),
            "address": data.get('address'),
            "status": data.get('status'),
            "admission_fees": data.get('admission_fees')
        })
        student.insert()
        frappe.db.commit()
        response = {
            "status": "success",
            "message": _("Student registered successfully.")
        }
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Student Registration Failed"))
        response = {
            "status": "error",
            "message": str(e)
        }

    return Response(json.dumps(response), content_type='application/json')
