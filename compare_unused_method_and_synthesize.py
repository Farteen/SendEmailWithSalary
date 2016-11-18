import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# addressbook list you will send to
address_book = ['xxx@xxx.com']
msg = MIMEMultipart()
# sender
sender = 'xxx@xxx.com'
subject = "subject"
body = "email body"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()

s = smtplib.SMTP('microsoft_exchange_domain', 587)
s.starttls()
s.login('USERNAME','PASSWORD')
s.sendmail(sender,address_book, text)
s.quit()