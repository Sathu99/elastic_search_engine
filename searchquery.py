import os
from query import basic_search
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

client = Elasticsearch(hosts=["http://localhost"], http_auth=("elastic", os.getenv('ELASTCSEARCH_PASSWORD')), port=os.getenv('ELASTCSEARCH_PORT'))

INDEX = os.getenv('ELASTCSEARCH_INDEX')

def search(query):
    query_body = basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
