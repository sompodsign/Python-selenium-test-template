from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name


class LoginPageLocators(object):
    input_username = (By.ID, "ctl00_ctl00_Main_BoxContent_txtUserName")
    input_password = (By.ID, "ctl00_ctl00_Main_BoxContent_txtPassword")
    login_button = (By.ID, "ctl00_ctl00_Main_BoxContent_BtnAuthenticate")
    escapeLocator = (By.XPATH, '//*[@id="divHeader"]')


# all the xpath should be redefined according client requirement

class WelcomePageLocators(object):
    AdminLocator = (By.CLASS_NAME, "primaryMenuItemSel")
    CompaniesAndContactsLocator = (By.XPATH, '//a[contains(text(), "Companies & Contacts")]')
    IPAndProductsLocator = (By.XPATH, '//a[contains(text(), "IP & Products")]')
    ParticipationManagerLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[3]")
    ReceivablesLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[4]")
    ContractApprovalsLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[5]")
    ApprovalWorkflowLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[6]")
    ContentLibraryLocator = (By.XPATH, "(//*[@class='primaryMenuItem'])[7]")


class CompaniesAndContactPageLocators(object):
    addNewCompanyLocator = (By.ID, "ctl00_ActionsContent_idAddNewLink")

    # assert compny info
    def assertComapnyName(searchname):
        companyNametoAssert = (By.XPATH, f'//*[contains(text(),"{searchname}")]//ancestor::td[@class="DataCell"]/div')
        return companyNametoAssert

    # Company Info
    searchCompany = (By.ID, "ctl00_FilteringContent_txtSearch")
    searchGo = (By.ID, "ctl00_FilteringContent_btnGO")
    CompanyName = (By.ID, "txtCompanyName")
    # CompanyName = (By.ID, "txtCompanyNme")
    AboutTextBox = (By.ID, "txtAbout")
    companyCode = (By.ID, "txtAbbrev")
    ParentCompany = (By.ID, "ddlParentComp")
    owned = (By.ID, "cbOwned")
    TaxID = (By.ID, "txtTaxId")
    TaxID2 = (By.ID, "txtTaxId2")
    companyStatus = (By.ID, "ddlCompanyStatus")
    BusinessCategory = (By.ID, "msBusinesCategory_hrefOnItemsList")
    SearchBusinessCategory = (By.ID, "msBusinesCategory_txtSearch")

    # BusinessCategoryCheckBox = (By.ID, "checkbox_msBusinesCategory_gridItems_Incl_1")
    def checkBusinessCategory(BusinessCategory):
        checkBusinessCategory = (By.XPATH,
                                 f'//*[@title="{BusinessCategory}"]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return checkBusinessCategory

    BusinessCategoryDone = (By.ID, "msBusinesCategory_btnDone")

    addLink = (By.ID, "msBusinesCategory_hrefOnItemsList")
    phoneNum = (By.ID, "txtPhone")
    faxNum = (By.ID, "txtFax")
    emailAddress = (By.ID, "txtEmailId")
    website = (By.ID, "txtWebsite")
    doingBusinessAs = (By.ID, "txtDoingBusinessAs")

    # Company User's Part
    canEditUsersCheckbox = (By.ID, "cbCanUsersEditData")
    SelectAddress = (By.ID, "ddlExistingAddressForDisplay")

    # Address
    AddressField1 = (By.ID, "txtAddress1")
    AddressField2 = (By.ID, "txtAddress2")
    cityInput = (By.ID, "txtCity")
    CountrySelect = (By.ID, "ddlCountry")
    StateSelect = (By.ID, "ddlState")
    zipCode = (By.ID, "txtPostCode")

    editCompany = (By.XPATH, '//*[@id="gridCompanies_cell_0_14"]/div/a[3]')
    addCompanyPhoto = (By.XPATH, '//*[@id="DRMImgCtrl1_tdAddNewDelete"]/a[1]')
    chooseCompanyPhoto = (By.ID, "DRMImgCtrl1_FileUpload1")
    uploadcompanyPhoto = (By.ID, "DRMImgCtrl1_BtnUpload")

    # Save / Cancel
    saveButton = (By.ID, "btnSave")
    cancelButton = (By.ID, "btnCancel")
    uploadButton = (By.ID, "btnUpload")


class IPandProductsPageLocators(object):
    addNewIP = (By.ID, "ctl00_ActionsContent_idAddNewLink")
    addNewProduct = (By.ID, "ctl00_ContentPlaceHolder1_idAddNewLink")

    addLicensor = (By.ID, "msLicensor_hrefOnItemsList")

    searchLicensor = (By.ID, "msLicensor_txtSearch")

    # searchLicensor = (By.ID, "msLicensor_txtSearc")

    def checklicensors(licensor):
        checklicensor = (By.XPATH,
                         f'//*[@title="{licensor}"]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return checklicensor

    LicensorCheckDone = (By.ID, "msLicensor_btnDone")

    intellectualProperty = (By.ID, "txtIPName")
    primaryID = (By.ID, "txtPrimaryID")
    owner = (By.ID, "IPStringSelector0_ListItem_search")
    property = (By.ID, "IPStringSelector1_ListItem_search")
    collection = (By.ID, "IPStringSelector2_ListItem_search")
    EAN = (By.ID, "IPStringSelector3_ListItem_search")

    addIPType = (By.ID, "msIPType_hrefOnItemsList")
    searchIPType = (By.ID, "msIPType_txtSearch")

    # checkIPType = (By.ID, "checkbox_msIPType_gridItems_Incl_1")
    def checkIpType(ipType):
        IpTypeLocator = (By.XPATH,
                         f'//*[@title="{ipType}"]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return IpTypeLocator

    checkIPTypeDone = (By.ID, "msIPType_btnDone")

    Language = (By.ID, "ddlLanguage")
    Status = (By.ID, "ddlStatus")
    Created = (By.ID, "dtCreated_txtDate")
    released = (By.ID, "dtReleased_txtDate")
    GLAcntCode = (By.ID, "txtGLAccountCode")
    accuralRate = (By.ID, "txtAccrualRate")
    Notes = (By.ID, "txtNote")

    addIpPhoto = (By.XPATH, '//*[@id="DRMImgCtrl1_tdAddNewDelete"]/a')
    chooseIpPhoto = (By.ID, "DRMImgCtrl1_FileUpload1")
    uplaodIpPhoto = (By.ID, "DRMImgCtrl1_BtnUpload")

    # save/cancel
    saveButton2 = (By.ID, "btnSaveCheck")
    cancelButton2 = (By.ID, "btnCancel")


class ContactsLocator(object):
    addContactsLocator = (By.XPATH, '//div[@title="Add Contact"]/ancestor::a')
    situation = (By.ID, "ddlSalutation")
    firstName = (By.ID, "txtFirstName")
    # firstName = (By.ID, "txtFirstNme")
    MiddleName = (By.ID, "txtMiddleName")
    LastName = (By.ID, "txtLastName")
    JobTitle = (By.ID, "txtJobTitle")
    DisplayName = (By.ID, "txtDisplayName")
    referenceCode = (By.ID, "txtReferenceCode")
    email = (By.ID, "txtEmail")
    website = (By.ID, "txtWebsite")
    IMAddress = (By.ID, "txtIMAddress")

    # Phones
    businessPhone = (By.ID, "txtPhoneBus")
    homePhone = (By.ID, "txtPhoneHome")
    mobilePhone = (By.ID, "txtPhoneCell")
    businessFax = (By.ID, "txtBusinessFax")

    # Roles
    addRoles = (By.ID, "msRoles_hrefOnItemsList")
    searchRole = (By.ID, "msRoles_txtSearch")

    def checkRoles(role):
        checkRole = (By.XPATH,
                     f'//*[@title="{role}"]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return checkRole

    checkRoleDone = (By.ID, "msRoles_btnDone")

    # image upload
    def editContacts(contactName):
        editContactLocator = (By.XPATH,
                              f'//span[contains(text(), "{contactName}")]/ancestor::td[@class="DataCell"]/following-sibling::td[@class="DataCell"]/div/a[3]')

        return editContactLocator

    # editContacts = (By.XPATH, '//*[@id="gridCompanies_cell_0_0_14"]/div/a[3]')
    addPhoto = (By.ID, "aAddPhoto")
    fileUpload = (By.ID, "FileUpload1")
    buttonUplaod = (By.ID, "btnUpload")
    systemUser = (By.ID, "cbSysUser")
    externalUser = (By.ID, "rbExtUser")
    internalUser = (By.ID, "rbIntUser")

    # save/cancel
    saveBtn3 = (By.ID, "btnSave")
    cancelBtn3 = (By.ID, "btnCancel")


class AddProductsLocator(object):
    productsMenuLocator = (By.ID, "wsSecondaryMenuItem_302")
    # productsMenuLocator = (By.ID, "wsSecondaryMenuItem_")
    productCategoryLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_1"]/nobr')
    productSubCategoryLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_2"]/nobr')
    productArticlesLocator = (By.XPATH, '//*[@id="ctl00_caLeftMenu_3"]/nobr')
    productName = '167 Product'
    listProductName = (By.XPATH,
                       f'//div[contains(text(),"{productName}")]/ancestor::td[@class="DataCell"]/following-sibling::td[@align="center"]/div/a/div[@title="Delete"]')

    frameLocator = (By.ID, "ctl00_ContentPlaceHolder1_WndHostctrl1_ifrm")
    productNameLocator = (By.ID, "txtProductName")
    primaryNumber = (By.ID, "txtPrimaryNumber")
    addNewLocator = (By.ID, "ctl00_ContentPlaceHolder1_idAddNewLink")
    categoryName = (By.ID, "txtName")
    categoryDescription = (By.ID, "txtDescr")
    showAll = (By.ID, "cbShowAll")

    # linkedToProductLocator = (By.ID, "checkbox_gridIncl_Incl_0")
    def linkedToProductLocator(product):
        linkedToProduct = (By.XPATH,
                           f'//*[contains(text(),"{product}")]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return linkedToProduct

    aDDnewLocator = (By.ID, "ctl00_MainContent_DefaultsCtrl1_idAddNewLink")
    subCategoryNameLocator = (By.ID, "txtName")
    subCategoryDescriptionLocator = (By.ID, "txtDescr")

    def linkedtoCategoryLocator(category):
        linkedtoCategory = (By.XPATH,
                            f'//*[contains(text(),"{category}")]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return linkedtoCategory

    articleNameLocator = (By.ID, "txtName")
    articleDesciptionLocator = (By.ID, "txtDescr")

    # linkedTosubCategoryLocator = (By.ID, "checkbox_gridIncl_Incl_0")
    def linkedtoSubCategoryLocator(subCategory):
        linkedtoSubCategory = (By.XPATH,
                               f'//*[contains(text(),"{subCategory}")]//ancestor::td[@class="DataCell"]//preceding-sibling::td[@class="DataCell"]/div/input')
        return linkedtoSubCategory

    buttonSaveLocatorforProducts = (By.ID, "btnSave")
    buttonCancelLocatorProducts = (By.ID, "btnCancel")


# started new test cases

class ContentLib(object):
    menu_option = (By.XPATH,
                   '//a[contains(text(),"Content Library")]')
    sidebarMenu = (By.XPATH, "//tbody/tr[1]/td[2]/div[2]/div[2]/div[1]")
    sidebarMenu2 = (By.XPATH, "//div[@id='side-menu-left']")
    sidebarStatus = (By.XPATH, "//div[@id='pin']")
    pinMode = (By.XPATH, "//div[@id='pin']")
    newFolder = (By.XPATH, "//tbody/tr/td[@id='pageContentMain']/div[@id='mainContentContainer']/div[@id='content']/div[@id='side-menu-left']/div[@class='catalog-menu-container']/div/a[@href='#']/img[1]")
    catlogName = (By.XPATH, "//input[@id='catalogName']")
    catDescription = (By.XPATH, "//textarea[@id='catalogDescription']")
    expirationDate = (By.XPATH, "//input[@id='catalogExpiration']")
    okButton = (By.XPATH, "//button[contains(text(),'OK')]")
    folderName = (By.XPATH, "//div[@id='selectedCatalogLabel']")


class contentLibraryImageUpload(object):
    searchBarField = (By.XPATH, "//input[@id='criteria']")
    searchBtn = (By.XPATH, '//img[@src="Images/futures/search24.png"]')
    searchCatalog = (By.XPATH, "//span[@title='Search for catalogs.']")
    searchFolderFound = (By.XPATH,
                         "//body[1]/form[1]/div[4]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]")
    datasearchedFolder = (By.XPATH,
                          "//a[@data-name='DemoData']//div")

    searchedFolder = (By.XPATH,
                      "//a[@data-name='DemoData']")

    uploadImageIcon = (By.CSS_SELECTOR, "#uploadbar")

    uploadInputBtn = (By.XPATH, "//input[@id='file-upload']")

    uploadStatus = (By.XPATH, "//div[@id='progress_0']")

    ImageUploadOkBtn = (By.XPATH, "//button[contains(text(),'OK')]")


class imageDownload(object):
    clickOnimage = (By.XPATH,
                    "//body[1]/form[1]/div[4]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/div[3]/div[1]/div[4]/div[2]/div[1]")
    clickOnDownloadIcon = (By.XPATH, '//img[@title="Download"]')
    clickOnDownloadIcon2 = (By.XPATH, '//div[@title="Download image"]')
    deleteicon = (By.XPATH, '//img[@title="Delete"]')
    deleteicon2 = (By.XPATH, '//div[@title="Delete image information"]')


class CatalogDelete(object):
    catalog = (By.XPATH,
               "//body[1]/form[1]/div[4]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]/div[2]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/a[1]")

    rightclickoncatalogOption = (By.XPATH, "//li[@id='delete-context-menu-li']")


class addNewContactPageForReceivables(object):
    clickOnReceivables = (By.XPATH, "//a[contains(text(),'Receivables')]")
    clickOnAddNewContact = (By.XPATH, "// a[ @ id = 'ctl01_ContentPlaceHolder1_idAddNewLink']")
    inputContractName = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_txtContractName']")

    # inputContractNumber = (By.XPATH, "") //select[@id='ctl01_ContentPlaceHolder1_ddlContrType']
    def contractType(name):
        selectContractType = (By.XPATH, f"//option[contains(text(),'{name}')]")
        return selectContractType

    AddLicensor = (By.XPATH, "//span[@id='ctl01_ContentPlaceHolder1_msLicensors_linkAddNew']")
    AddLicensorInputField = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_msLicensors_txtSearch']")

    def LicensorCheckBox(Licensor):
        AddLicensorCheckboxSelect = (By.XPATH, f'//span[@title="{Licensor}"]/..//..//..//td//input')
        return AddLicensorCheckboxSelect

    AddLicensorClickDoneOption = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_msLicensors_btnDone']")

    AddLicensee = (By.XPATH, "//a[@id='ctl01_ContentPlaceHolder1_msLicensee_hrefOnItemsList']")
    AddLicenseeInputField = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_msLicensee_txtSearch']")

    def LicenseeCheckBox(Licensee):
        AddLicenseeCheckboxSelect = (By.XPATH, f'//span[@title="{Licensee}"]/..//..//..//td//input')
        return AddLicenseeCheckboxSelect

    AddLicenseeClickDoneOption2 = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_msLicensee_btnDone']")

    def contract_status(status):
        SelectStatus = (By.XPATH, f"//option[contains(text(),'{status}')]")
        return SelectStatus

    TermFromInput = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_dtTermFrom_txtDate']")
    TermToInput = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_dtTermTo_txtDate']")

    save = (By.XPATH, "//input[@id='ctl01_ContentPlaceHolder1_btnSave']")

    # 2ndPage
    assertionExecuted = (By.XPATH, "//select[@id='ContractCtrl1_ddlStatus']")

    def select_currency(currencyName):
        SelectCurrencyUsDollar = (
            By.XPATH, f'//select[@id="ContractCtrl1_ddlCurrency"]//option[contains(text(),"{currencyName}")]')
        return SelectCurrencyUsDollar

    SelectCheckBoxExecuted = (By.XPATH, "//input[@id='ContractCtrl1_dtExecuted_cbActive']")
    ExecuteDateInput = (By.XPATH, "//input[@id='ContractCtrl1_dtExecuted_txtDate']")

    def accounting_cycle(cycle_name):
        SelectAccountingCycle = (
            By.XPATH, f'//select[@id="ContractCtrl1_ddlAcctCycle"]//option[contains(text(),"{cycle_name}")]')
        return SelectAccountingCycle

    selectRadioButtonOK = (By.XPATH, "//input[@id='ContractCtrl1_rbReturnsCapYes']")
    EnterReturnCaps = (By.XPATH, "//input[@id='ContractCtrl1_txtReturnsCap']")

    def return_cap_calculation(calculation_name):
        CalculatedAccountingCycle = (By.XPATH, "//option[contains(text(),'calculated by accounting cycle')]")
        return CalculatedAccountingCycle

    Savebtnfor2ndPage = (By.XPATH, "//input[@id='btnSave']")

    # fILLING UP IP
    IpTab = (By.XPATH, '//div[@id="ctl00_TabsContent_t1"]')
    addNewIp = (By.XPATH, "//div[@id='idAddNewLink']//a")

    def selectIpName(ipname):
        ip_name = (By.XPATH, f'(//div[contains(text(),"{ipname}")])[1]/..//..//td//input')
        return ip_name

    firstRateInputField = (By.XPATH, "//input[@id='txtRate']")

    def rateType(text):
        selectRateType = (By.XPATH, f"//option[contains(text(),'{text}')]")
        return selectRateType

    ipTabFrame = "ctl00_ContentPlaceHolder1_ifrmContr"
    ipFormFrame = "ctl00_ContentPlaceHolder1_WndHostctrl1_ifrm"
    saveIpForm = (By.XPATH, "//input[@id='btnSave']")
    tableRow = (By.XPATH, "//tbody/tr[starts-with(@id, 'gridIPs_row')]")
    # filling up product
    productTab = (By.XPATH, '//div[@title="Contract Products"]')
    productIframe = "ctl00_ContentPlaceHolder1_ifrmContr"
    addNewProduct = (By.XPATH, "//div[@id='idAddNewLink']//a")
    productPageIframe = "ctl00_ContentPlaceHolder1_WndHostctrl1_ifrm"

    def UncheckCheckbox(name):
        Option = (By.XPATH, f"//label[contains(text(),'{name}')]/..//input")
        return Option

    def SelectProductName(text):
        selectRateType = (By.XPATH, f"//option[contains(text(),'{text}')]")
        return selectRateType

    def SelectCategory(text):
        selectRateType = (By.XPATH, f"//option[contains(text(),'{text}')]")
        return selectRateType

    addSubCategoryButton = (By.XPATH, "//a[@id='msSubcat_hrefOnItemsList']")
    ProductSave = (By.XPATH, "//input[@id='btnSave']")
    subClassAllChecked = (By.XPATH, "//tbody/tr[@id='msSubcat_gridItems_top_head']/td[1]/div[1]/input[1]")
    articleAllChecked = (By.XPATH, "//tbody/tr[@id='msArticle_gridItems_top_head']/td[1]/div[1]/input[1]")
    subcategorySearchingField = (By.XPATH, '//input[@id="msSubcat_txtSearch"]')

    def select_sub_category(name):
        select_sub_category = (By.XPATH, f"//span[@title='{name}']/../../..//input")
        return select_sub_category

    subcategoryDone = (By.XPATH, "//input[@id='msSubcat_btnDone']")
    addArticleButton = (By.XPATH, "//span[@id='msArticle_linkAddNew']//a")
    articleDone = (By.XPATH, "//input[@id='msArticle_btnDone']")
    articleSearchField = (By.XPATH, '//input[@id="msArticle_txtSearch"]')

    def select_article(name):
        select_article = (By.XPATH, f'//span[@title="{name}"]/../../..//input')
        return select_article

    btnClose = (By.XPATH, '//div[@class="btn_CloseWnd"]')
