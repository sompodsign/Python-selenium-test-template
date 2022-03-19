import glob
import os
from datetime import datetime


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# function to read current date and time
def read_datetime():
    return str(datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))


# function to read raw time
def get_raw_time():
    return str(datetime.today().strftime('%Y%d%H%M%S'))


def read_time():
    return str(datetime.today().strftime('%H-%M-%S'))


def get_html_report(report_type):
    directory = None
    if report_type == 'ui':
        directory = ''
    elif report_type == 'api':
        directory = 'api_report_html'
    try:
        report = os.path.abspath(glob.glob(f"{directory}report_html/*.html")[-1])
        return report
    except Exception as e:
        print("Report not ready, Error", e)
        return False
