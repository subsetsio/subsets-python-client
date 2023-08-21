# Subsets Python Client

Easily access the Subsets data warehouse using Python. For more details and features, visit [subsets.io](https://www.subsets.io)

## Installation

Run the following command to install the API:

```pip install subsetsio```
## Usage

At the moment, you can only use the SDK for querying. To explore datasets, checking quotas, and viewing past queries, visit the [subsets.io](https://www.subsets.io) web interface.

```python
from subsetsio import query

df = query(sql="YOUR_SQL_QUERY_HERE", api_key="YOUR_API_KEY")
```

## License

[MIT Licensed](LICENSE.md)