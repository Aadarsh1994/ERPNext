# Copyright (c) 2024, Adarsh and contributors
# For license information, please see license.txt

# # import frappe
# # from frappe.model.document import Document



# from frappe.model.document import Document

# class StudentDetails(Document):
#     pass


from frappe.model.document import Document
import re
import frappe

class StudentDetails(Document):
    def after_insert(self):
        self.send_welcome_email()

    def after_save(self):
        self.check_completion_status()

    def validate_email(self, error_messages):
        if self.email:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, self.email):
                error_messages.append("Please enter a valid email address")

    def send_welcome_email(self):
        if not self.email:
            frappe.msgprint("Email not provided for the student.")
            return

        subject = "Welcome to Our Institute"
        message = f"""
        Dear {self.name1},

        Welcome to our institute! Your registration number is {self.reg_no}.

        Best Regards,
        The Institute Team
        """

        try:
            frappe.sendmail(
                recipients=[self.email],
                subject=subject,
                message=message,
                now=True
            )
            frappe.msgprint(f"Email sent to {self.email}")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Email Sending Failed")
            frappe.throw(f"An error occurred while sending the email: {str(e)}")

    def check_completion_status(self):
        required_fields = [
            'reg_no',
            'name1',
            'dob',
            'gender',
            'email',
            'phone',
            'dept',
            'course',
            'mark'
        ]

        all_fields_filled = True

        for field in required_fields:
            if not getattr(self, field):
                all_fields_filled = False

        if all_fields_filled:
            self.status = 'Completed'
        
        self.save()