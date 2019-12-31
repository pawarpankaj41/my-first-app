import re
from datetime import datetime

def valid_string(name):
    return ({True: True, False: False}[name != None and name != "" and isinstance(name, str)])

def valid_int(input):
    return ({True: True, False: False}[isinstance(input, int) and input != None])

def valid_float(input):
    return ({True: True, False: False}[isinstance(input, float) and input != None])

def valid_email(email):
    if email is not None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            # email._errors.append("{} ({}) should be a valid email".format(email.key_name, email.value))
            return False
    return True

def valid_username(username):
    if username is not None:
        if not re.match("[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]", username):
            return False
    return True
    
def valid_date_format(date):
    try:
       if datetime.strptime(date, "%Y-%m-%d"):
           return True
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return False

def valid_phone(phone):
    return ({True: True, False: False}[isinstance(phone, int) and len(str(phone)) == 10 ])

def valid_gstin(input):
    if input is not None:
        if not re.match("\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}", input):
            return False
    return True

def valid_fssai(input):
    return ({True: True, False: False}[isinstance(input, int) and len(str(input)) == 14 ])

def valid_csv_format(input):
    return ({True: True, False: False}[str(input).endswith(('.csv'))])
    # x = input.endswith(('.csv'))
    # if x== True:
    #     return True
    # else:
    #     return False
def valid_image_format(input):
    return ({True: True, False: False}[str(input).endswith(('.jpeg', '.jpg', '.png', '.webp'))])
    # x = input.endswith(('.jpeg', '.jpg', '.png', '.webp'))
    # if x== True:
    #     return True
    # else:
    #     return False