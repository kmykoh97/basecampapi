import requests
from ..basecamp import Basecamp


class Cards(Basecamp):

    def __init__(self, project_id: int, completed_cards_id: int, incomplete_cards_id: int):
        '''
        Interacts with Basecamp Todolists.

        Parameters:
            project_id (int): The ID the Basecamp project.
            cards_id (int): ID of the Cards you wish to target.
        '''
        self.__base_url = Basecamp._Basecamp__base_url
        self.__credentials = Basecamp._Basecamp__credentials
        self.project_id = project_id
        self.completed_cards_id = completed_cards_id
        self.incomplete_cards_id = incomplete_cards_id
        self.__headers = {
            'Authorization': 'Bearer ' + self.__credentials['access_token'],
            "Content-Type": "application/json"
        }

        self.info = "ok"

    def get_completed(self) -> list:
        '''
        Returns:
            list: A list of completed cards.
        '''
        get_lines_url = f"{self.__base_url}/buckets/{self.project_id}/card_tables/lists/{self.completed_cards_id}/cards.json?completed=true"
        response = requests.get(get_lines_url, headers=self.__headers)
        if not response.ok:
            raise Exception(
                f"Status code: {response.status_code}. {response.reason}. Error text: {response.text}.")
        else:
            return response.json()

    def get_incomplete(self) -> list:
        '''
        Returns:
            list: A list of incomplete cards.
        '''
        get_lines_url = f"{self.__base_url}/buckets/{self.project_id}/card_tables/lists/{self.incomplete_cards_id}/cards.json?completed=false"
        response = requests.get(get_lines_url, headers=self.__headers)
        if not response.ok:
            raise Exception(
                f"Status code: {response.status_code}. {response.reason}. Error text: {response.text}.")
        else:
            return response.json()
