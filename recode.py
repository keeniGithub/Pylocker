import sys
import os

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)

def check_pass():
    with open (resource_path('code.txt'), 'r') as f:
        data = f.read()
    return data

def recode(new_pass):
    with open (resource_path('code.txt'), 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(old_data, new_pass)

    with open ('code.txt', 'w') as f:
        f.write(new_data)       