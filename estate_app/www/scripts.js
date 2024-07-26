document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('student-registration-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        const studentData = {
            regno: formData.get('regno'),
            stud_name: formData.get('stud_name'),
            gender: formData.get('gender'),
            dob: formData.get('dob'),
            dept: formData.get('dept'),
            course: formData.get('course'),
            email: formData.get('email'),
            mob_no: formData.get('mob_no'),
            fathers_name: formData.get('fathers_name'),
            mothers_name: formData.get('mothers_name'),
            address: formData.get('address'),
            status: formData.get('status'),
            admission_fees: formData.get('admission_fees')
        };

        console.log('Submitting student data:', studentData);

        // Make an API call to save the data
        fetch('http://localhost:8000/api/method/estate_app.www.api.register_student', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + btoa('03d776654d221ec:3d71c451b3d7161')
            },
            body: JSON.stringify(studentData)
        })
        .then(response => {
            console.log('Response received:', response);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Response data:', data);
            if (data.status === 'success') {
                // Send email to the student
                sendEmail(studentData.email, studentData.stud_name, studentData.regno);
                alert('Registration successful and email sent!');
            } else {
                alert('Registration failed. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });

    function sendEmail(email, studentName, regNo) {
        console.log('Sending email to:', email);

        fetch('http://localhost:8000/api/method/frappe.core.doctype.communication.email.make', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + btoa('03d776654d221ec:3d71c451b3d7161')
            },
            body: JSON.stringify({
                recipients: email,
                subject: 'Registration Confirmation',
                content: `Dear ${studentName},<br><br>Thank you for registering. Your registration number is ${regNo}.`,
                doctype: 'Student',
                name: regNo
            })
        })
        .then(response => {
            console.log('Email response received:', response);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Email sent successfully:', data);
        })
        .catch(error => {
            console.error('Error sending email:', error);
        });
    }
});
