import os
import re
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from query import basic_search, multi_match, wildcard_search, search_with_fields

load_dotenv()

client = Elasticsearch(
    hosts=["http://localhost"],
    http_auth=("elastic", os.getenv("ELASTCSEARCH_PASSWORD")),
    port=os.getenv("ELASTCSEARCH_PORT"),
)

INDEX = os.getenv("ELASTCSEARCH_INDEX")


def search(query, fields, operator="or"):
    if len(fields) == 0:
        query_body = basic_search(query, "or" if operator == "not" else operator)
    elif re.search(r"[^.]\*", query) and len(fields) != 0:
        query_body = wildcard_search(query, fields)
    elif len(fields) > 0 and operator == "not":
        query_body = search_with_fields(query, fields)
    else:
        query_body = multi_match(query, fields, "or" if operator == "not" else operator)

    print("Query Processing...", query_body)

    res = client.search(index=INDEX, body=query_body, size=120)

    return res
