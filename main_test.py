import helper
import sender_stand_request
import data
import configuration
import requests

def test_kit_order_watching():
   track = helper.get_new_order_track()
   act_code = requests.get(url=configuration.URL + configuration.TRACK + track).status_code
   exp_code = 200
   assert act_code == exp_code

   #Добжов Никита 5ая когорта Финальный проект .Инженер по тестированию плюс