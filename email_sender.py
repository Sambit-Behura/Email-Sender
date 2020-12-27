import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text()) 
email = EmailMessage()
email['from'] = "Sambit Kumar Behura"
email['to'] = 'smrutiamlandas@gmail.com'
email['subject'] = "CSS Gradient color Generator!"

email.set_content(html.substitute({'name':'Mikun'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('1841012028.d.sambitkumarbehur@gmail.com','Sambit@7884')
    smtp.send_message(email)
    print("Working fine")