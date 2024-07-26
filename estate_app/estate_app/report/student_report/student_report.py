import frappe

def execute(filters=None):
    columns = [
        {"label": "Student Name", "fieldname": "stud_name", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Registration Number", "fieldname": "regno", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "mob_no", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "dept", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
        {"label": "Subjects", "fieldname": "subjects", "fieldtype": "Text"},
        {"label": "Total Marks Obtained", "fieldname": "total_marks_obtained", "fieldtype": "Float"},
        {"label": "Total Maximum Marks", "fieldname": "total_max_marks", "fieldtype": "Float"},
        {"label": "Overall Percentage", "fieldname": "overall_percentage", "fieldtype": "Float"}
    ]

    data = []

    student_filters = {}
    if filters:
        if filters.get("regno"):
            student_filters["regno"] = filters.get("regno")
        if filters.get("stud_name"):
            student_filters["stud_name"] = ["like", f"%{filters.get('stud_name')}%"]
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email"):
            student_filters["email"] = ["like", f"%{filters.get('email')}%"]
        if filters.get("mob_no"):
            student_filters["mob_no"] = ["like", f"%{filters.get('mob_no')}%"]
        if filters.get("dept"):
            student_filters["dept"] = ["like", f"%{filters.get('dept')}%"]
        if filters.get("course"):
            student_filters["course"] = ["like", f"%{filters.get('course')}%"]
        if filters.get("dob"):
            if filters.get("dob").strip():  # Check if dob is not empty or just spaces
                student_filters["dob"] = filters.get("dob")  # Exact match for date

    students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    student_data = {}

    for student in students:
        if student.name not in student_data:
            student_data[student.name] = {
                "stud_name": student.stud_name,
                "status": student.status,
                "regno": student.regno,
                "gender": student.gender,
                "email": student.email,
                "mob_no": student.mob_no,
                "dept": student.dept,
                "course": student.course,
                "dob": student.dob,
                "subjects": [],
                "total_marks_obtained": 0.0,
                "total_max_marks": 0.0,
                "overall_percentage": 0.0
            }

        marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
        for mark in marks:
            marks_obtained = float(mark.marks_obtained) if mark.marks_obtained else 0.0
            total_marks = float(mark.total_marks) if mark.total_marks else 0.0
            subject_info = f"{mark.subject_code} - {mark.subject_name}"
            student_data[student.name]["subjects"].append(subject_info)
            student_data[student.name]["total_marks_obtained"] += marks_obtained
            student_data[student.name]["total_max_marks"] += total_marks

    for student in student_data.values():
        if student["total_max_marks"] > 0:
            student["overall_percentage"] = (student["total_marks_obtained"] / student["total_max_marks"]) * 100
        student["subjects"] = "\n".join(student["subjects"])
        data.append(student)

    # Add chart to the report
    chart = {
        "type": "bar",
        "data": {
            "labels": [student["stud_name"] for student in student_data.values()],
            "datasets": [
                {
                    "name": "Total Marks Obtained",
                    "values": [student["total_marks_obtained"] for student in student_data.values()]
                },
                {
                    "name": "Total Maximum Marks",
                    "values": [student["total_max_marks"] for student in student_data.values()]
                }
            ]
        },
        "fieldnames": ["stud_name", "total_marks_obtained", "total_max_marks"]
    }

    return columns, data, None, chart
