import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.excel_utils import read_data_from_excel
from utils.json_utils import json_reader
from utils.general_functions import read_date, read_time, get_html_report
from send_mail import send_report

test_environment_type = json_reader("conf_test/configuration.json")['settings']["environmentType"]
configuration_data = read_data_from_excel("./test_data/{}_test_data.xlsx".format(test_environment_type),
                                          sheet_name="configuration")
parallel = configuration_data["parallel_run"]

report_folder_name = f"{read_date()}_{read_date()}_{read_time()}"

# Individually will run each test case
individual_run_command = f"pytest -s --alluredir=report_allure/{report_folder_name} " \
                         f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"

# Test cases will run based on the amount of threads available
parallel_run_command = f"pytest -s -n auto --alluredir=report_allure/{report_folder_name} " \
                       f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"

if parallel == "yes":
    subprocess.run(parallel_run_command, shell=True)
else:
    subprocess.run(individual_run_command, shell=True)

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
