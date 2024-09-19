import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your_mail"
password = "your password"  # Your app password

employee_file = 'employee_emails.xlsx'  # replace with your file path
employees = pd.read_excel(employee_file)

subject = "Your Monthly Pay Slip"
body = """
Dear [Employee Name],

Please find attached your pay slip for this month. If you have any questions, feel free to contact the HR department.

Best Regards,
Your Company"""

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, password)

for index, row in employees.iterrows():
    employee_email = row['Email']  # assuming 'Email' is the column name
    employee_name = row['Name']    # assuming 'Name' is the column name
    payslip_path = row['PaySlip']  # assuming 'PaySlip' is the column name for the PDF file path

    personalized_body = body.replace("[Employee Name]", employee_name)
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = employee_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(personalized_body, 'plain'))
    
    filename = os.path.basename(payslip_path)
    
    try:
        with open(payslip_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {filename}')
            msg.attach(part)

        server.sendmail(sender_email, employee_email, msg.as_string())
        print(f"Email with pay slip sent to {employee_name} at {employee_email}")
    except Exception as e:
        print(f"Failed to send email to {employee_name}. Error: {str(e)}")

server.quit()
