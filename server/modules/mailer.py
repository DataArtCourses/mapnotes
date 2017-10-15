import asyncio
import aiosmtplib

from email.mime.text import MIMEText

from .config import Config


class Mailer:

    loop = asyncio.get_event_loop()
    server = aiosmtplib.SMTP(hostname=Config.get('email', 'host'),
                             port=int(Config.get('email', 'port')),
                             loop=loop)

    @classmethod
    async def send_mail(cls, subject, body, receiver):

        message = MIMEText(body)
        message['From'] = Config.get('email', 'user')
        message['To'] = receiver
        message['Subject'] = subject

        await cls.server.connect()
        await cls.server.starttls()
        await cls.server.login(username=Config.get('email', 'user'),
                               password=Config.get('email', 'password'))
        await cls.server.ehlo()
        await cls.server.send_message(message)
