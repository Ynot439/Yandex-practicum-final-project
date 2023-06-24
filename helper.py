import data
import configuration
import requests
import sender_stand_request
def get_new_order_track():
   track = str(sender_stand_request.order_create(data.order_body).json()["track"])
   return track
