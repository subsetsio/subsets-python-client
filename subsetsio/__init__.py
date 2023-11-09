import requests

class Client:
    def __init__(self, api_key, base_url='https://server.subsets.io'):
        self.api_key = api_key
        self.base_url = base_url

    def search_tables(self, query, n=3):
        response = requests.get(
            f"{self.base_url}/deep_search",
            params={'query': query, 'n': n, 'api_key': self.api_key}
        )
        response.raise_for_status()
        return response.json()

    def query(self, sql_query):
        data = {'query': sql_query, 'api_key': self.api_key}
        response = requests.post(
            f"{self.base_url}/execute",
            json=data
        )
        response.raise_for_status()
        return response.json()
