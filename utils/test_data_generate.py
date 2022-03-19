import pathlib
from utils import CompanyDataConfigForExcel
from conf_test import testData_configuration_for_run_test
import utils.excel_utils
from utils.excel_utils import *


class generalData(object):
    file_name = pathlib.Path(
        __file__).parent.parent / f"TestData/{testData_configuration_for_run_test.File_Name_of_the_instance}"
    sheetpath = CompanyDataConfigForExcel.sheetNameForReceivables
    contract_type = readData(file_name, sheetpath, 2, 2)
    Licensor = readData(file_name, sheetpath, 3, 2)
    Licensee = readData(file_name, sheetpath, 4, 2)
    status = readData(file_name, sheetpath, 5, 5)
    TimeFrom = str(readData(file_name, sheetpath, 5, 2))
    TimeTo = str(readData(file_name, sheetpath, 6, 2))
    ExecutionDate = readData(file_name, sheetpath, 7, 2)
    ReturnCapitals = readData(file_name, sheetpath, 8, 2)
    currency = readData(file_name, sheetpath, 2, 5)
    accounting_cycle = readData(file_name, sheetpath, 3, 5)
    return_cap_calculation_option = readData(file_name, sheetpath, 4, 5)


class AddingUpIp(object):
    file_name = pathlib.Path(
        __file__).parent.parent / f"TestData/{testData_configuration_for_run_test.File_Name_of_the_instance}"
    sheetpath = CompanyDataConfigForExcel.sheetNameForReceivables
    FirstRateData1 = readData(file_name, sheetpath, 10, 2)
    SecondRateData = readData(file_name, sheetpath, 11, 2)
    RateType = readData(file_name, sheetpath, 12, 2)
    IpName1 = readData(file_name, sheetpath, 13, 2)
    IpName2 = readData(file_name, sheetpath, 14, 2)
    ct1 = 1

    checkbox1 = readData(file_name, sheetpath, 16, 2)
    checkbox2 = readData(file_name, sheetpath, 17, 2)

    producttype = readData(file_name, sheetpath, 18, 2)
    producttype2 = readData(file_name, sheetpath, 19, 2)
    productcategory = readData(file_name, sheetpath, 20, 2)
    productcategory2 = readData(file_name, sheetpath, 21, 2)
    subcategory_name = readData(file_name, sheetpath, 22, 2)
    subcategory_name2 = readData(file_name, sheetpath, 23, 2)
    article = readData(file_name, sheetpath, 24, 2)
    article2 = readData(file_name, sheetpath, 25, 2)


class TestCaseNumber(object):
    file_name = pathlib.Path(
        __file__).parent.parent / f"TestData/{testData_configuration_for_run_test.File_Name_of_the_instance}"
    sheetpath = CompanyDataConfigForExcel.sheetNameForLogin
    TotalData = readData(file_name, sheetpath, 2, 4)
