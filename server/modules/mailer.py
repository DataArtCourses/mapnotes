import asyncio
import aiosmtplib
import logging

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import Config

log = logging.getLogger('application')


class Mailer:

    loop = asyncio.get_event_loop()
    server = aiosmtplib.SMTP(hostname=Config.get('email', 'host'),
                             port=int(Config.get('email', 'port')),
                             loop=loop)

    @staticmethod
    async def send_mail(subject, body, receiver, _charset='utf-8'):
        log.info(f'Sending mail to {receiver}')
        await Mailer.server.connect()
        await Mailer.server.starttls()
        await Mailer.server.login(username=Config.get('email', 'user'),
                                  password=Config.get('email', 'password'))
        message = MIMEMultipart('alternative')
        message['From'] = Config.get('email', 'user')
        message['To'] = receiver
        message['Subject'] = subject

        text = MIMEText(body, 'text', _charset=_charset)
        html = MIMEText(body, 'html', _charset=_charset)
        message.attach(html)
        message.attach(text)
        await Mailer.server.send_message(message)
        log.info(f'Successfuly sent mail to {receiver}, shutting down SMTP')
        Mailer.server.close()
