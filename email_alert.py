#!/usr/bin/env python3
from subprocess import check_output
import re
import smtplib
from email.mime.text import MIMEText


def high_disk_use(threshold=90):
    """ Checks to see whether disk use is above the given threshold.
    Args:
        threshold: the disk utilization threshold to trigger an alert.
    Returns:
        A boolean indicating whether disk usage is over `threshold`.
        True when disk usage is over `threshold`, False otherwise.
    """
    df_output = check_output(["df", "/"])
    find_usage = re.findall(b"(\d+)%", df_output)
    disk_usage_percent = int(find_usage[0])

    if disk_usage_percent > threshold:
        return True
    else:
        return False


if __name__ == "__main__":
    if high_disk_use():
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
