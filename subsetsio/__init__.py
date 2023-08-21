import requests
import pandas as pd
import time

class SubsetsError(Exception):
    pass

BASE_URL = 'https://server.subsets.io'

def query(sql, api_key):
    if not sql or sql.strip() == '':
        raise SubsetsError("Query cannot be empty.")
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key 
    }

    response = requests.post(f'{BASE_URL}/engine/submit', 
                             headers=headers,
                             json={'query': sql})

    if response.status_code != 200:
        raise SubsetsError(response.text)
    
    signed_url = response.text
    
    # load parquet file
    df = pd.read_parquet(signed_url)

    return df
