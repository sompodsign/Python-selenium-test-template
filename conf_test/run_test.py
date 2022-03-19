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
test_item = configuration_data["test_item"]

report_folder_name = f"{read_date()}_{read_date()}_{read_time()}"

# Individually will run each test case
individual_ui_run_command = f"pytest -s --alluredir=report_allure/{report_folder_name} " \
                            f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"

# Individually will run each api test case
individual_api_run_command = f"pytest -s --alluredir=report_allure/{report_folder_name} " \
                             f"--html=api_report_html/report_{report_folder_name}.html --self-contained-html api_tests"

# Test cases will run based on the amount of threads available
parallel_ui_run_command = f"pytest -s -n auto --alluredir=report_allure/{report_folder_name} " \
                          f"--html=report_html/report_{report_folder_name}.html --self-contained-html tests"

# Test cases will run based on the amount of threads available
parallel_api_run_command = f"pytest -s -n auto --alluredir=report_allure/{report_folder_name} " \
                           f"--html=api_report_html/report_{report_folder_name}.html --self-contained-html api_tests"

if parallel == "yes" and test_item == "ui":
    subprocess.run(parallel_ui_run_command, shell=True)
elif parallel == "yes" and test_item == "api":
    subprocess.run(parallel_api_run_command, shell=True)
elif test_item == "ui" and parallel == "no":
    subprocess.run(individual_ui_run_command, shell=True)
else:
    subprocess.run(individual_api_run_command, shell=True)

# send report if generated
html_report = get_html_report(test_item)
if html_report:
    print("Sending report...")
    report = html_report
    send_report("sompod123@gmail.com", report)
else:
    print("Something went wrong while generating html report.")

# allure report serve
# ui_allure_serve_command = f"allure serve report_allure/{report_folder_name}"
# api_allure_serve_command = f"allure serve api_report_allure/{report_folder_name}"
#
# if test_item == "ui":
#     subprocess.run(ui_allure_serve_command, shell=True)
# else:
#     subprocess.run(api_allure_serve_command, shell=True)
