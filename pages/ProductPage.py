import sys, os

# from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# import allure
import time
import pathlib
from pages.base_page import BasePage
from pages.welcome_page import WelcomePage
from utils import ExcelUtils
from utils.locators import AddProductsLocator
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import *



class ProductPage(BasePage):
    def __init__(self, driver):
        self.locator = AddProductsLocator
        super(ProductPage, self).__init__(driver)

    def click_product(self):
        self.find_element(*self.locator.productsMenuLocator).click()

    def click_add_new(self):
        self.find_element(*self.locator.addNewLocator).click()

    def click_addNew2(self):
        self.find_element(*self.locator.aDDnewLocator).click()

    def input_productName(self, productName):
        self.find_element(*self.locator.productNameLocator).send_keys(productName)

    def input_primaryNumber(self, primaryNumber):
        self.find_element(*self.locator.primaryNumber).send_keys(primaryNumber)

    def Click_Save_Button(self):
        self.find_element(*self.locator.buttonSaveLocatorforProducts).click()

    def click_cancel_btn(self):
        self.find_element(*self.locator.buttonCancelLocatorProducts).click()

    def click_category(self):
        self.find_element(*self.locator.productCategoryLocator).click()

    def input_category(self, cat):
        self.find_element(*self.locator.categoryName).send_keys(cat)

    def input_catDescription(self, catdesc):
        self.find_element(*self.locator.categoryDescription).send_keys(catdesc)

    def click_showAll(self):
        self.find_element(*self.locator.showAll).click()

    def check_box_linked_to_product(self, linked):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*self.locator.linkedToProductLocator(linked)))
        time.sleep(2)
        self.find_element(*self.locator.linkedToProductLocator(linked)).click()

    def check_box_linked_to_category(self, linked):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*self.locator.linkedtoCategoryLocator(linked)))
        time.sleep(2)
        self.find_element(*self.locator.linkedtoCategoryLocator(linked)).click()

    def check_box_linked_to_sub_category(self, linked):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*self.locator.linkedtoSubCategoryLocator(linked)))
        time.sleep(2)
        self.find_element(*self.locator.linkedtoSubCategoryLocator(linked)).click()

    def click_subcategory(self):
        self.find_element(*self.locator.productSubCategoryLocator).click()

    def input_subcategory(self, subcat):
        self.find_element(*self.locator.subCategoryNameLocator).send_keys(subcat)

    def input_subcatDescription(self, subcatdesc):
        self.find_element(*self.locator.subCategoryDescriptionLocator).send_keys(subcatdesc)

    def click_article(self):
        self.find_element(*self.locator.productArticlesLocator).click()

    def input_article(self, article):
        self.find_element(*self.locator.articleNameLocator).send_keys(article)

    def input_articledesc(self, articledesc):
        self.find_element(*self.locator.articleDesciptionLocator).send_keys(articledesc)

    def fill_up_add_product(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForProduct)
        for r in range(2, row + 1):
            try:
                productName = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 1)
                primaryNumber = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 2)
                catName = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 3)
                catDesc = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 4)
                linkedToProduct = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 5)
                subCat = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 6)
                subCatDesc = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 7)
                linkedToCat = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 8)
                article = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 9)
                articleDesc = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 10)
                linkedTosubCat = ExcelUtils.readData(clientPath, sheetNameForProduct, r, 11)
                page1 = WelcomePage(self.driver)
                self.driver.get(ExcelUtils.readData(clientPath, sheetNameForLogin, 2, 3))
                time.sleep(2)
                page1.click_ip_and_Products_tab()
                time.sleep(5)
                self.driver.switch_to_default_content()
                time.sleep(2)
                self.click_product()
                time.sleep(2)
                self.click_add_new()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(5)
                self.driver.switch_to.frame(0)

                time.sleep(3)
                self.input_productName(productName)

                time.sleep(2)
                self.input_primaryNumber(primaryNumber)

                time.sleep(2)
                self.Click_Save_Button()

                time.sleep(2)
                self.click_cancel_btn()

                time.sleep(5)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_category()

                time.sleep(5)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_addNew2()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(5)
                self.driver.switch_to.frame(0)

                time.sleep(2)
                self.input_category(catName)

                time.sleep(2)
                self.input_catDescription(catDesc)

                time.sleep(2)
                self.click_showAll()

                time.sleep(3)
                self.check_box_linked_to_product(linkedToProduct)

                time.sleep(2)
                self.Click_Save_Button()

                time.sleep(2)
                self.click_cancel_btn()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_subcategory()

                time.sleep(5)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_addNew2()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(5)
                self.driver.switch_to.frame(0)

                time.sleep(2)
                self.input_subcategory(subCat)

                time.sleep(2)
                self.input_subcatDescription(subCatDesc)

                time.sleep(2)
                self.click_showAll()

                time.sleep(2)
                self.check_box_linked_to_category(linkedToCat)

                time.sleep(2)
                self.Click_Save_Button()

                time.sleep(2)
                self.click_cancel_btn()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_article()

                time.sleep(5)
                self.driver.switch_to_default_content()

                time.sleep(2)
                self.click_addNew2()

                time.sleep(2)
                self.driver.switch_to_default_content()

                time.sleep(5)
                self.driver.switch_to.frame(0)

                time.sleep(2)
                self.input_article(article)

                time.sleep(2)
                self.input_articledesc(articleDesc)

                time.sleep(2)
                self.click_showAll()

                time.sleep(2)
                self.check_box_linked_to_sub_category(linkedTosubCat)

                time.sleep(2)
                self.Click_Save_Button()

                time.sleep(2)
                self.click_cancel_btn()
                time.sleep(3)
                ExcelUtils.writeData(clientPath, sheetNameForProduct, r, 12, 1)
                time.sleep(3)
            except Exception as e:
                # allure.attach(self.driver.get_screenshot_as_png(), name=f"failed_screenshot",
                #               attachment_type=AttachmentType.PNG)
                # allure.attach(f"Problem Happened, {e}")
                ExcelUtils.writeData(clientPath, sheetNameForProduct, r, 12, 0)
                time.sleep(3)
                continue
