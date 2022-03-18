import glob
import os
from datetime import datetime

# Read current date
import pdfkit


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


def get_html_report():
    try:
        report = os.path.abspath(glob.glob("report_html/*.html")[-1])
        return report
    except Exception as e:
        print("Report not ready, Error", e)
        return False


def html_to_pdf(read_new_data_1, time1):
    read_new_data = str(read_new_data_1)
    time = str(time1)
    html_path = os.getcwd() + "/ReportHtml/report_" + time + "_" + read_new_data + ".html"
    pdfkit.from_file(html_path, "report_" + time + "_" + read_new_data + ".pdf")
