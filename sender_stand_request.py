import requests
import configuration
import data
def order_create(order_body):
    return requests.post(url=configuration.URL + configuration.ORDER, json=order_body)
