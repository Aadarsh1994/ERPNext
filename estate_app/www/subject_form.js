// Function to get the CSRF token from cookies
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Function to handle file upload
function handleFileUpload(file, csrfToken) {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('is_private', 0); // set to 1 if you want the file to be private

    // Upload the file
    return fetch('http://localhost:8000/api/method/estate_app.www.file_upload.upload_file', {
        method: 'POST',
        headers: {
            'X-Frappe-CSRF-Token': csrfToken
        },
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to upload file.');
        }
        return response.json();
    })
    .catch(error => {
        console.error('Error uploading file:', error);
        throw error; // Rethrow the error for further handling
    });
}

// Function to create Subject document
function createSubjectDocument(subjectCode, subjectName, totalMarks, fileUrl, csrfToken) {
    const subjectData = {
        doctype: 'Subject',
        subject_code: subjectCode,
        subject_name: subjectName,
        total_marks: totalMarks,
        image: fileUrl // Assuming fileUrl is passed from successful file upload
    };

    // Create the Subject document
    return fetch('http://localhost:8000/api/resource/Subject', {
        method: 'POST',
        headers: {
            'X-Frappe-CSRF-Token': csrfToken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(subjectData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to create Subject.');
        }
        return response.json();
    })
    .then(data => {
        console.log('Subject created successfully:', data);
        alert('Subject created successfully!');
    })
    .catch(error => {
        console.error('Error creating Subject:', error);
        throw error; // Rethrow the error for further handling
    });
}

// Example usage with error handling
document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    
    // Event listener for file selection
    fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        const csrfToken = getCookie('sid');

        if (file) {
            handleFileUpload(file, csrfToken)
                .then(uploadResult => {
                    console.log('Upload Result:', uploadResult); // Debugging line
                    console.log(uploadResult)
                    if (uploadResult.message && uploadResult.message.file_url) {
                        return createSubjectDocument('yourSubjectCode', 'yourSubjectName', 'yourTotalMarks', uploadResult.message.file_url, csrfToken);
                    } else {
                        throw new Error('File upload did not return expected data.');
                    }
                })
                .catch(error => {
                    console.error('Error handling file upload and subject creation:', error);
                    alert('Error handling file upload and subject creation.');
                });
        } else {
            alert('No file selected.');
        }
    });
});
