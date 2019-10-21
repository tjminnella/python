import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# create multipart email
msg = MIMEMultipart()
msg['Subject'] = 'Lily'
msg['From'] = 'My RPi <my_rpi@example.com>'
msg['To'] = 'you@yourdomain.com'
msg.preamble = 'This is a multi-part message in MIME format.'
	# attach email text
message = """This is a test of using Python on Raspberry Pi
to send an email. This email also includes a picture as an
email attachment. Have fun!"""
	msg.attach(MIMEText(message))
	# attach a JPG file
	filename = 'picture.jpg'
with open(filename, 'rb') as f:
 img = MIMEImage(f.read())
img.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(img)
# send email
s = smtplib.SMTP('smtpserver')
s.login('username', 'password')
s.send_message(msg)
s.quit()