import requests
import pandas as pd

class Client:
    def __init__(self, api_key: str, base_url: str = 'http://services.subsets.io'):
        self.api_key: str = api_key
        self.base_url: str = base_url

    def query(self, sql_query: str) -> pd.DataFrame:
        data = {'query': sql_query, 'api_key': self.api_key}
        response = requests.post(
            f"{self.base_url}/sql/query",
            json=data
        )
        response.raise_for_status()
        response_body = response.json()
        return pd.DataFrame(columns=response_body['columns'], data=response_body['data'])