import os
from datetime import datetime
from lib.desktop import desktop_notify

"""
Main function which calls the desktop notification method.
- If no message is passed, it is assumed that the objective of the message is to notify the end of the process.
- If a message is passed, the user will get it.
Date and time always appear, at the end of the notification's message.
"""
def notify(message_sent=''):
	message_to_send = 'Process {} ended'.format(str(os.getpid())) if message_sent == '' else message_sent
	desktop_notify('{} at {}'.format(message_to_send, str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))))
notify('hello')	
