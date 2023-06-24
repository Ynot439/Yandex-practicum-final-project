import helper
import sender_stand_request
import data
import configuration
import requests
import pytest
@pytest.mark.parametrize("track",
                         [
                            pytest.param(
                               helper.get_new_order_track(), id="1gfdgd"
                            ),
                            pytest.param(
                               454554, id="1000"
                            ),
                         ])
def test_kit_order_watching(track):
   act_code = requests.get(url=configuration.URL + configuration.TRACK + str(track)).status_code
   exp_code = 200
   assert act_code == exp_code

#Надеюсь правильно понял идею функции-запроса
# Нашел ошибку в ссылке конфигурации(отсутствовала часть ссылки,программа принимал любой трек и успешно проходила с ним тест)
# трэк 454554 добавил для себя, чтоб видеть,что функция принимает  не любое значение как было до этого.

#Добжов Никита 5ая когорта Финальный проект. Инженер по тестированию плюс