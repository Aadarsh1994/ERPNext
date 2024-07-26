// Copyright (c) 2024, Adarsh and contributors
// For license information, please see license.txt

frappe.query_reports["Student Report"] = {
    "filters": [
        {
            "fieldname": "regno",
            "label": __("Reg No."),
            "fieldtype": "Link",
            "options":"Student",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "stud_name",
            "label": __("Name"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options": ["Female", "Male", " "],
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "email",
            "label": __("Email"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "mob_no",
            "label": __("Phone"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "dept",
            "label": __("Department"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "course",
            "label": __("Course"),
            "fieldtype": "Data",
            "reqd": 0,
            "hidden": 0
        },
        {
            "fieldname": "dob",
            "label": __("DOB"),
            "fieldtype": "Date",
            "reqd": 0,
            "hidden": 0
        }
    ],
    onload: function(report) {
        report.page.add_inner_button(__("Clear Filters"), function() {
            // Clear all filters
            frappe.query_report_filters_by_name.regno.set_input("");
            frappe.query_report_filters_by_name.stud_name.set_input("");
            frappe.query_report_filters_by_name.gender.set_input("");
            frappe.query_report_filters_by_name.email.set_input("");
            frappe.query_report_filters_by_name.mob_no.set_input("");
            frappe.query_report_filters_by_name.dept.set_input("");
            frappe.query_report_filters_by_name.course.set_input("");
            frappe.query_report_filters_by_name.dob.set_input("");
            // Refresh the report to load all data
            report.refresh();
        });
    }
};
