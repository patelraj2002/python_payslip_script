# Python Email Script for Sending Pay Slips

This script sends personalized email pay slips to employees using Gmail's SMTP server. It reads employee details from an Excel file and attaches the respective pay slip PDF to each email.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
- **Pandas library**: Install using `pip install pandas`.
- **OpenPyXL library**: Install using `pip install openpyxl` (required for reading `.xlsx` files).
- **Email account with app password**: Set up an "app password" for Gmail and ensure your account settings allow access from less secure apps if necessary.(ref. for APP PASSWORD : https://www.youtube.com/watch?v=vtYrT-de9eY )

## Setup

1. **Clone or download the repository**:
   ```bash
   git clone https://github.com/patelraj2002/python_payslip_script.git
   cd your-repository
Update the script with your credentials and file paths:

Open a.py in a text editor.
Replace the sender_email and password variables with your Gmail address and app password.
Update the employee_file variable with the path to your Excel file.
Prepare the Excel file:

Ensure your Excel file (employee_emails.xlsx) has the following columns:
Employee Code: Unique code for each employee (e.g., mrcl01).
Name: Employee's full name.
Email: Employee's email address.
PaySlip: File path to the employee's pay slip PDF.
Example:

plaintext
Copy code
| Employee Code | Name         | Email                | PaySlip                  |
|---------------|--------------|----------------------|--------------------------|
| mrcl01        | John Doe     | john.doe@example.com | /path/to/john_payslip.pdf|
| mrcl02        | Jane Smith   | jane.smith@example.com | /path/to/jane_payslip.pdf|
| mrcl03        | Alice Johnson | alice.johnson@example.com | /path/to/alice_payslip.pdf|
Running the Script
To execute the script, run:

bash
Copy code
python a.py
Notes
Ensure that the paths to the pay slip PDFs in the Excel file are correct and accessible.
The script sends emails one by one and prints the status of each email sent to the console.
Troubleshooting
If you encounter authentication issues, verify that your app password is correctly entered and that your Gmail account settings allow access from less secure apps.
Check the console output for error messages and adjust your file paths or data as needed.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, please contact rajchovatiya70@gmail.com.
