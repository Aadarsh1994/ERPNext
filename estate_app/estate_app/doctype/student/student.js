frappe.ui.form.on("Student", {
    refresh(frm) {

    },
});

frappe.ui.form.on('Student', {
    validate: function(frm) {
        let error_messages = [];
        validate_date_of_birth(frm, error_messages);
        validate_phone(frm, error_messages);
        validate_email(frm, error_messages);

        if (error_messages.length > 0) {
            frappe.throw(error_messages.join('<br>'));
        }
    },
    dob: function(frm) {
        // Check if a date of birth is selected
        if (frm.doc.dob) {
            // Display an alert
            frappe.msgprint(`Date of Birth added: ${frm.doc.dob}`);
        }
    }
});

function validate_date_of_birth(frm, error_messages) {
    if (frm.doc.dob) {
        let today = frappe.datetime.get_today();
        if (frm.doc.dob >= today) {
            error_messages.push("Date of Birth cannot be in the future from js");
        }

        let dob = new Date(frm.doc.dob);
        let age = (new Date() - dob) / (365.25 * 24 * 60 * 60 * 1000);
        if (age > 120) {
            error_messages.push("Date of Birth indicates an age greater than 120 years");
        }
    }
}

function validate_phone(frm, error_messages) {
    if (frm.doc.mob_no) {
        let phone_pattern = /^[0-9]{10}$/;  // Adjust the regex pattern according to your requirements
        if (!phone_pattern.test(frm.doc.mob_no)) {
            error_messages.push("Please enter a valid phone number with 10 digits from js");
        }
    }
}

function validate_email(frm, error_messages) {
    if (frm.doc.email) {
        let email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!email_pattern.test(frm.doc.email)) {
            error_messages.push("Please enter a valid email address from js");
        }
    }
}


