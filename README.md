# Subsets Python Client

Easily access the Subsets data warehouse using Python. For more details and features, visit [subsets.io](https://www.subsets.io)

## Installation

Run the following command to install the API:

```pip install subsetsio```
## Usage
```python
import subsetsio

client = subsetsio.Client(api_key="YOUR_API_KEY")
df = client.query(sql_query)
```

## License

[MIT Licensed](LICENSE.md)