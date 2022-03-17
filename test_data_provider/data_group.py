from application_settings.application_settings import ApplicationSettings


class TestDataGroup:

    @staticmethod
    def check_for_credentials(group):
        table_name = None

        if group.lower() == "test_login_functionality":
            table_name = ApplicationSettings.get_login_credentials_table_name()
        elif group.lower() == "test_signup_functionality":
            table_name = ApplicationSettings.get_signup_data_table_name()
