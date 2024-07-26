# Copyright (c) 2024, Adarsh and contributors
# For license information, please see license.txt

# import frappe
# student.py

from frappe.model.document import Document
import frappe
import re
from frappe.utils import today, date_diff

class Student(Document):
    pass
#     def validate(self):
#         error_messages = []
#         self.validate_date_of_birth(error_messages)
#         self.validate_phone_number(error_messages)
#         self.validate_email(error_messages)

#         if error_messages:
#             error_message_str = "<br>".join(error_messages)
#             frappe.throw(error_message_str)

#             try:
#                 frappe.db.sql("""SELECT hai FROM tabStudent;""")
#             except Exception as e:
#                 frappe.log_error(frappe.get_traceback(), str(e))
#                 print(e)
                



#     def validate_date_of_birth(self, error_messages):
#         if self.dob:
#             if self.dob >= today():
#                 error_messages.append(("Date of Birth cannot be in the future"))
#                 error_messages.append(("\n"))
#             if date_diff(today(), self.dob) / 365.25 > 120:
#                 error_messages.append(("Date of Birth indicates an age greater than 120 years"))
#                 error_messages.append(("\n"))

#     def validate_phone_number(self, error_messages):
#         if self.mob_no:
#             phone_pattern = r'^[0-9]{10}$'  # Adjust the regex pattern according to your requirements
#             if not re.match(phone_pattern, self.mob_no):
#                 error_messages.append(("Please enter a valid phone number with 10 digits"))
#                 error_messages.append(("\n"))

#     def validate_email(self, error_messages):
#         if self.email:
#             email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#             if not re.match(email_pattern, self.email):
#                 error_messages.append(("Please enter a valid email address"))
#                 error_messages.append(("\n"))



# # Import necessary Frappe modules

# # Import necessary Frappe modules



# #class Student(Document):
#     def before_save(self):
#         self.calculate_percentages()

#     def calculate_percentages(self):
#         for mark in self.mark:
#             if mark.total_marks and mark.marks_obtained:
#                 try:
#                     mark.percentage = (float(mark.marks_obtained) / float(mark.total_marks)) * 100
#                 except ValueError:
#                     mark.percentage = 0
#             else:
#                 mark.percentage = 0
