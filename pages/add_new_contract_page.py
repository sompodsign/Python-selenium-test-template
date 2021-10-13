from selenium.webdriver.common.by import By
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import datetime
import time
from pages.base_page import BasePage
from datetime import datetime
from utils import locators
from utils import Test_data


class addContract(BasePage):
    def __init__(self, driver):
        self.locator = locators.addNewContactPageForReceivables
        self.data = Test_data.AddingUpIp
        self.general_data = Test_data.generalData
        super(addContract, self).__init__(driver)

    def goto_Receivables_Tab(self):
        self.find_element(*self.locator.clickOnReceivables).click()
        current_url = str(self.get_url())
        mainURL = "ContractFind.aspx?Type=1&MenuOptionID=6002"
        assert mainURL in current_url

    def click_add_new_contact(self):
        self.find_element(*self.locator.clickOnAddNewContact).click()
        current_url = str(self.get_url())
        mainURL = "/ContractNew.aspx"
        assert mainURL in current_url

    def chooseContractType(self, type):
        self.click(*self.locator.contractType(type))

    def checkLicensee(self, Lincesee):
        self.click(*self.locator.LicenseeCheckBox(Lincesee))

    def checkLicensor(self, Licensor):
        self.click(*self.locator.LicensorCheckBox(Licensor))

    def selectCurrency(self, currency_name):
        self.click(*self.locator.select_currency(currency_name))

    def select_account_cycle(self, account_cycle):
        self.click(*self.locator.accounting_cycle(account_cycle))

    def returns_cap_accounting_cycle(self, calculation_option):
        self.click(*self.locator.return_cap_calculation(calculation_option))

    def select_status(self, status):
        self.click(*self.locator.contract_status(status))

    def fill_up_form_general(self, contract_type, licensor_name, licensee_name, TimeFrom, TimeTo, ExecutionDate,
                             ReturnCapitals, currency, account_cycle, cap_accounting_option, status):
        self.time1 = str(datetime.now())
        contractName = "Test contract ABC" + self.time1
        self.find_element(*self.locator.inputContractName).send_keys(contractName)
        # self.sendkeys(self.locator.inputContractName, "TEST")
        time.sleep(5)
        self.chooseContractType(contract_type)
        time.sleep(5)
        # Licensor
        self.find_element(*self.locator.AddLicensor).click()
        time.sleep(5)
        self.find_element(*self.locator.AddLicensorInputField).send_keys(licensor_name)
        time.sleep(5)
        self.checkLicensor(licensor_name)
        time.sleep(5)
        self.find_element(*self.locator.AddLicensorClickDoneOption).click()
        time.sleep(5)
        # LICENSEE
        self.find_element(*self.locator.AddLicensee).click()
        time.sleep(5)
        self.find_element(*self.locator.AddLicenseeInputField).send_keys(licensee_name)
        time.sleep(5)
        self.checkLicensee(licensee_name)
        time.sleep(5)
        self.find_element(*self.locator.AddLicenseeClickDoneOption2).click()
        # SelectStatus
        self.select_status(status)
        time.sleep(5)
        # Select Date
        self.find_element(*self.locator.TermFromInput).clear()
        self.find_element(*self.locator.TermFromInput).send_keys(TimeFrom)
        time.sleep(5)
        # Select Term
        self.find_element(*self.locator.TermToInput).clear()
        self.find_element(*self.locator.TermToInput).send_keys(TimeTo)
        time.sleep(5)
        # saving the form
        self.find_element(*self.locator.save).click()
        time.sleep(5)
        # accept alert
        try:
            self.driver.switch_to.alert.accept()
        except:
            self.driver.execute_script("window.confirm = function(){return true;}")
        time.sleep(5)
        # self.driver.switch_to.frame("ctl00_ContentPlaceHolder1_ifrmContr")
        self.driver.switch_to.frame('ctl01_ContentPlaceHolder1_ifrmContr')
        time.sleep(4)
        self.selectCurrency(currency)
        time.sleep(4)
        text = self.find_element(*self.locator.assertionExecuted).text
        # assert text == "Executed"
        print("*" * 80)
        print(text)
        time.sleep(2)
        self.find_element(*self.locator.SelectCheckBoxExecuted).click()
        time.sleep(4)
        self.find_element(*self.locator.ExecuteDateInput).send_keys(ExecutionDate)
        time.sleep(5)
        self.select_account_cycle(account_cycle)
        time.sleep(4)
        self.find_element(*self.locator.selectRadioButtonOK).click()
        time.sleep(4)
        self.find_element(*self.locator.EnterReturnCaps).clear()
        self.find_element(*self.locator.EnterReturnCaps).send_keys(ReturnCapitals)
        time.sleep(5)
        self.returns_cap_accounting_cycle(cap_accounting_option)
        time.sleep(5)
        self.find_element(*self.locator.Savebtnfor2ndPage).click()
        time.sleep(5)

    def inputRate(self, rate):
        self.find_element(*self.locator.firstRateInputField).send_keys(rate)

    def enterRateType(self, data):
        self.click(*self.locator.rateType(data))

    def select_ip_name(self, name):
        self.click(*self.locator.selectIpName(name))

    def click_ip_tab(self):
        self.driver.switch_to.default_content()
        self.click(*self.locator.IpTab)

    def click_product_tab(self):
        self.driver.switch_to.default_content()
        self.click(*self.locator.productTab)

    def uncheck_product(self, name):
        element = self.find_element(*self.locator.UncheckCheckbox(name))
        if element.is_selected():
            element.click()

    def select_product(self, name):
        element = self.find_element(*self.locator.SelectProductName(name))
        if element.is_selected():
            pass
        else:
            element.click()

    def select_category(self, name):
        element = self.find_element(*self.locator.SelectCategory(name))
        if element.is_selected():
            pass
        else:
            element.click()

    def checkboxstatus(self):
        self.driver.switch_to.default_content()
        self.change_frame(self.locator.productPageIframe)
        self.click(*self.locator.addSubCategoryButton)
        time.sleep(3)
        element = self.driver.find_elements(By.XPATH,
                                            '//table[@id="msSubcat_gridItems"]//tr//td[@id="msSubcat_gridItems_dom"]//tr//input')
        for ele in element:
            if ele.is_selected():
                ele.click()

    def select_all_sub_category(self):
        self.click(*self.locator.addSubCategoryButton)
        time.sleep(2)
        self.click(*self.locator.subClassAllChecked)

    def select_sub_category(self, data):
        self.click(*self.locator.select_sub_category(data))

    def select_all_article(self):
        self.click(*self.locator.addArticleButton)
        time.sleep(2)
        self.click(*self.locator.articleAllChecked)

    def select_article(self, data):
        self.click(*self.locator.select_article(data))

    def closeButton(self):
        self.driver.switch_to.default_content()
        self.click(*self.locator.btnClose)

    def fill_up_form_ip(self, ipnamerow, firstrate, ratetype):
        self.driver.switch_to.default_content()
        # Tabname or path
        time.sleep(5)
        self.change_frame(self.locator.ipTabFrame)
        time.sleep(5)
        self.click(*self.locator.addNewIp)
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.change_frame(self.locator.ipFormFrame)
        time.sleep(5)
        # input text
        self.inputRate(firstrate)
        # input text end
        self.select_ip_name(ipnamerow)
        time.sleep(5)
        self.enterRateType(ratetype)
        time.sleep(5)
        self.click(*self.locator.saveIpForm)

    def search_for_subcategory(self, subcategory):
        self.input_text(subcategory, *self.locator.subcategorySearchingField)

    def search_for_article(self, article):
        self.input_text(article, *self.locator.articleSearchField)

    # fill up product
    def fill_up_product(self, productName, producttype, category, subcategory, article):
        self.change_to_default_frame()
        time.sleep(5)
        self.change_frame(self.locator.productIframe)
        time.sleep(3)
        self.click(*self.locator.addNewProduct)
        time.sleep(3)
        self.change_to_default_frame()
        self.change_frame(self.locator.productPageIframe)
        time.sleep(5)
        self.uncheck_product(productName)
        time.sleep(1)
        self.select_product(producttype)
        time.sleep(1)
        self.select_category(category)
        time.sleep(2)
        self.select_all_sub_category()
        time.sleep(2)
        self.select_all_sub_category()
        time.sleep(2)
        # here goes sub category searching
        self.search_for_subcategory(subcategory)
        time.sleep(1)
        self.select_sub_category(subcategory)
        time.sleep(2)
        self.click(*self.locator.subcategoryDone)
        time.sleep(2)
        self.select_all_article()
        time.sleep(2)
        self.select_all_article()
        time.sleep(2)
        # here goes article searching
        self.search_for_article(article)
        time.sleep(1)
        self.select_article(article)
        time.sleep(1)
        self.click(*self.locator.articleDone)
        time.sleep(1)
        self.click(*self.locator.ProductSave)
        time.sleep(2)
        self.closeButton()
        time.sleep(2)

    def checktablerow(self, row1):
        self.change_to_default_frame()
        self.change_frame(self.locator.ipTabFrame)
        row = self.find_all_element(*self.locator.tableRow)
        countrow = len(row)
        print("countrow= {0} and row= {1}".format(countrow, row1))
        assert row1 == countrow

    def add_new_contract(self):
        self.goto_Receivables_Tab()
        # print('clicking add new contact')
        self.click_add_new_contact()
        self.fill_up_form_general(self.general_data.contract_type, self.general_data.Licensor,
                                  self.general_data.Licensee, self.general_data.TimeFrom, self.general_data.TimeTo,
                                  self.general_data.ExecutionDate, self.general_data.ReturnCapitals,
                                  self.general_data.currency,
                                  self.general_data.accounting_cycle,
                                  self.general_data.return_cap_calculation_option,
                                  self.general_data.status)
        self.click_ip_tab()
        self.fill_up_form_ip(self.data.IpName1, self.data.FirstRateData1, self.data.RateType)
        time.sleep(5)
        self.checktablerow(self.data.ct1)
        time.sleep(5)
        self.fill_up_form_ip(self.data.IpName2, self.data.SecondRateData, self.data.RateType)
        # self.checktablerow(self.data.ct2)
        time.sleep(3)
        self.click_product_tab()
        time.sleep(5)
        self.fill_up_product(self.data.checkbox1, self.data.producttype, self.data.productcategory,
                             self.data.subcategory_name, self.data.article)
        time.sleep(2)
        self.fill_up_product(self.data.checkbox2, self.data.producttype, self.data.productcategory,
                             self.data.subcategory_name2, self.data.article2)
