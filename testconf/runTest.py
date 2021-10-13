import pathlib
from datetime import datetime
import os
from writeToExcel import writetoToExcel
from utils import Test_data

time = str(datetime.today().strftime('%Y-%m-%d'))
print(time)
pathOfNew = pathlib.Path(__file__).parent / "new.txt"


def readWrite(pathOfFile):
    fileToRead = open(pathOfFile, 'r+')
    data = int(fileToRead.read())
    # print(type(data))
    newData = (data + 1)
    fileToRead.seek(0)
    fileToRead.write(str(newData))
    fileToRead.truncate()
    fileToRead.close()
    fileToReadForNewData = open(pathOfFile, 'r')
    readNewDatanum = fileToReadForNewData.read()
    fileToReadForNewData.close()
    return readNewDatanum


readNewData = readWrite(pathOfNew)

writetoToExcel()
if str(Test_data.TestCaseNumber.TotalData) == "suite2":
    print("run2")
    command = "pytest --html=ReportHtml/report_" + time + "_" + readNewData + ".html --self-contained-html" + " " + "tests_2"
    os.system(command)
elif str(Test_data.TestCaseNumber.TotalData) == "suite1":
    print("run1")
    command = "pytest --html=ReportHtml/report_" + time + "_" + readNewData + ".html --self-contained-html" + " " + "tests"
    os.system(command)
