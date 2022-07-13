import pandas as pd
import datetime as dt
from random import choice
import smtplib, ssl
import os

LETTERS_FILE_NAME_LIST = ['letter_1', 'letter_2', 'letter_3']
LETTER_EXTENSION = '.txt'
LETTERS_TEMPLATE_PATH = os.getcwd() + '/letter_templates/'
EMAILS_PATH = os.getcwd() + '/birthdays.csv'
USER = 'backstercorp@gmail.com'
PASSWORD = 'wftopukyxaqlhbaz'

# GET date
now = dt.datetime.now()

# Read emails
emails_df = pd.read_csv(EMAILS_PATH)

# Check if has birthday today
for index, row in emails_df.iterrows():
    if row.month == now.month and row.day == now.day:
        letter_file_name = LETTERS_TEMPLATE_PATH + choice(LETTERS_FILE_NAME_LIST) + LETTER_EXTENSION
        with open(letter_file_name) as letter_file:
            letter = letter_file.read().replace('[NAME]', row['name'])

        message = f'Subject:Happy Birthday\n\n{letter}'

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as connection:
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER, to_addrs=row.email, msg=message)



