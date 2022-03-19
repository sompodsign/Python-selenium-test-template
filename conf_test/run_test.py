import subprocess
import sys

from utils.general_functions import read_date, read_time, get_html_report
from send_mail import send_report

report_folder_name = f"{read_date()}_{read_date()}_{read_time()}"

command = f"pytest -s --alluredir=report_allure/{report_folder_name} " \
          f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"

subprocess.run(command, shell=True)

# send report if generated
html_report = get_html_report()
if html_report:
    print("Sending report...")
    report = html_report
    send_report("sompod123@gmail.com", report)
else:
    print("Something went wrong while generating html report.")

## allure serve
# command = f"allure serve report_allure/{report_folder_name}"
# subprocess.run(command, shell=True)
