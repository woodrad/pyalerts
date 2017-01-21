# Import smtplib for the actual sending function.
import smtplib

# Import the needed modules for email formatting.
from email.mime.text import MIMEText

# Create a text/plain formatted email.
msg = MIMEText('Rootfs usage over alert threshold')

# Add SMTP elements needed for send_message later.
msg['Subject'] = 'Rootfs usage alert'
msg['From'] = 'jersey-server@dephekt.net'
msg['To'] = 'cellphone@txt.att.net'

# Send the message via our own SMTP server
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
