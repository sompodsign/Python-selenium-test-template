import datetime


class ApplicationSettings:
    file_ext = ""
    browser_name = "chrome"
    url = ""
    image_folder_path = ""
    start_time = datetime.datetime.now()

    # Environment details
    production_url = ""
    dev_url = ""
    qa_url = "https://demoqa.com/"
    dev_test_data_file_path = ""
    production_test_data_file_path = ""
    qa_test_data_file_path = ""

    def get_browser_name(self):
        return self.browser_name

    def get_url(self):
        return self.url

    def get_qa_url(self):
        return self.qa_url

    def get_image_folder_path(self):
        return self.image_folder_path

    def get_start_time(self):
        return self.start_time

    def get_file_ext(self):
        return self.file_ext

    def set_browser_name(self, browser_name):
        self.browser_name = browser_name

    def set_url(self, url):
        self.url = url

    def set_image_folder_path(self, image_folder_path):
        self.image_folder_path = image_folder_path
