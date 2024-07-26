document.addEventListener("DOMContentLoaded", function() {
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Student",
            fields: ["regno", "stud_name", "dob", "gender", "mob_no", "email"],
            limit_page_length: 100
        },
        callback: function(response) {
            var students = response.message;
            var studentTable = document.getElementById("student-table");
            students.forEach(function(student) {
                var row = studentTable.insertRow();
                row.insertCell(0).innerHTML = student.regno;
                row.insertCell(1).innerHTML = student.stud_name;
                row.insertCell(2).innerHTML = student.dob;
                row.insertCell(3).innerHTML = student.gender;
                row.insertCell(4).innerHTML = student.mob_no;
                row.insertCell(5).innerHTML = student.email;
            });
        }
    });
});
