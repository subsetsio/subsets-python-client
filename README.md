# Subsets Python Client

Easily access the Subsets data warehouse using Python. For more details and features, visit [subsets.io](https://www.subsets.io)

## Installation

Run the following command to install the API:

```pip install subsetsio```
## Usage

At the moment, you can only use the SDK for querying. To explore datasets, checking quotas, and viewing past queries, visit the [subsets.io](https://www.subsets.io) web interface.

```python
import subsets

# Temp API Key. Sign up for a free permanent key.
client = subsets.client(api_key="YOUR_API_KEY")

user_query = "apple stock price"
# Search for tables, and rows within the table
response = client.search_tables(user_query, n=3)
# TODO: implement LLM function to convert text to sql
sql_query = text2sql(user_query, response.tables)
# Execute the query
df = client.query(sql_query)
```

## License

[MIT Licensed](LICENSE.md)