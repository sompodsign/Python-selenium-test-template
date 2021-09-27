import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib
from pages.base_page import BasePage
from utils import ExcelUtils
from utils import locators
from utils.CompanyDataConfigForExcel import *
from testconf.testData_configuration_for_run_test import File_Name_of_the_instance
from utils.Functions import userdefined


class ContentLibImageUpload(BasePage):

    def __init__(self, driver):
        self.locator = locators.ContentLib
        self.locatorforImageUpload = locators.contentLibraryImageUpload
        super(ContentLibImageUpload, self).__init__(driver)

    def input_search_data(self, Data):
        self.find_element(*self.locatorforImageUpload.searchBarField).send_keys(Data)

    def click_catalog_menu(self):
        self.find_element(*self.locatorforImageUpload.searchCatalog).click()

    def click_search_option(self):
        self.find_element(*self.locatorforImageUpload.searchBtn).click()

    def search_folder_found(self, folderName):
        try:
            data = self.find_element(*self.locatorforImageUpload.datasearchedFolder).text
            if data == folderName:
                self.find_element(*self.locatorforImageUpload.searchedFolder).click()
                folderName2 = self.find_element(*self.locator.folderName).text
                if folderName2 == data:
                    print("*****************************")
                    print("Folder clicked")
                else:
                    print("*****************************")
                    print("Folder not clicked")
                    print(folderName)
            else:
                assert data == ""
                message = "Folder Not found"
                return message
        except:
            print("No Folder Found")

    def click_searched_folder(self):
        self.find_element(*self.locatorforImageUpload.searchFolderFound).click()

    def click_image_icon(self):
        self.find_element(*self.locatorforImageUpload.uploadImageIcon).click()

    def input_image(self):
        # os.chdir("..")
        print("*" * 80)
        print(os.getcwd())
        funci = userdefined
        name= funci.ChangingimgFileName(1)
        imageField = self.find_element(*self.locatorforImageUpload.uploadInputBtn)
        print("this is from input image file {0}" .format(os.path.abspath("/photos/"+name)))
        imageField.send_keys(os.path.abspath("photos/"+name))

    # def click_classic_version(self):
    #     self.find_element(*self.locatorforImageUpload.classic_version)

    def click_upload_image_ok_button(self):
        self.find_element(*self.locatorforImageUpload.ImageUploadOkBtn).click()

    def checking_upload_status(self):
        status = self.find_element(*self.locatorforImageUpload.uploadStatus).text
        if "Upload Complete." in status:
            self.click_upload_image_ok_button()
        else:
            self.click_upload_image_ok_button()

    def remove_attribute(self):
        js = 'document.getElementById("upload-button").removeAttribute("onclick");'
        self.driver.execute_script(js)

    def search_folder(self):
        clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
        row = ExcelUtils.getRowCount(clientPath, sheetNameForCatalog)
        folder_name = ExcelUtils.readData(clientPath, sheetNameForCatalog, 2, 1)
        time.sleep(5)
        self.input_search_data(folder_name)
        time.sleep(5)
        self.click_catalog_menu()
        time.sleep(5)
        self.click_search_option()
        time.sleep(5)
        self.search_folder_found(folder_name)
        time.sleep(5)

    def upload_image(self):
        self.click_image_icon()
        time.sleep(2)
        self.input_image()
        time.sleep(5)
        self.checking_upload_status()
        time.sleep(2)

    def path(self):
        print(os.path.abspath("../photos"))
# new = ContentLibImageUpload
# new.input_image(1)
