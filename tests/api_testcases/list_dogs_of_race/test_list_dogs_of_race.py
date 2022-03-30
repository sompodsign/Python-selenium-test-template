import allure
from application_settings.api_application_settings import ApiTestApplicationSettingsProvider
from test_data.api_test_data.game_api_data import GameData
from utils.logger import CustomLogger

logger = CustomLogger('api_test').get_logger()


class TestListDogsOfRace(GameData):

    next_match_api = ApiTestApplicationSettingsProvider('/game/api/match')

    @allure.step('Successful retrieve list of dogs races')
    def test_list_of_dogs_race(self):
        random_match_id = self.next_match_api.get_request()['response']['matchId']
        api = ApiTestApplicationSettingsProvider('/game/api/dog/{}'.format(random_match_id))
        result = api.get_request()
        try:
            assert result['status_code'] == 200
            assert len(result['response']) == 8
            logger.info("Dogs of a match retrieved successfully")
        except Exception as e:
            logger.error(f"Failed retrieving dog list {e}")
            raise AssertionError
