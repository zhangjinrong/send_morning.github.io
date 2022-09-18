from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import time

today = datetime.now()


start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]
user_id1 = os.environ["USER_ID"]
#user_id2 = os.environ["USER_ID2"]
template_id = os.environ["TEMPLATE_ID"]

start_date = '2022-03-19'
city = '北京'
birthday = '04-06'
app_id = 'wx4abfbd3e393507e7'
app_secret = '037be9a91ee6c7203536049dbc73df10'
template_id = 'zxO6WSWCw68ZjoefFWTDvnYhOfsf08-2ZeBZzyLlpSI'
user_id1 =  'opet-6VCWWvyzsfu_WwEtERBEaoo'
user_id2 =  'opet-6VmFGa3nWfqo2dgOeSljk1w'

def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)

client = WeChatClient(app_id, app_secret)
wm = WeChatMessage(client)

while 1:
  if(datetime.now().strftime('%H')=='01'):
    user_id =  user_id1
    wea, temperature = get_weather()
    data = {"weather":{"value":wea},"temperature":{"value":os.environ['USER_ID']},"love_days":{"value":get_count()},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
    res = wm.send_template(user_id, template_id, data)
    #user_id =  user_id2
    #res = wm.send_template(user_id, template_id, data)
    time.sleep(60*61)
  elif(datetime.now().strftime('%H')=='22'):
    time.sleep(60*10)
  else:
    time.sleep(60*40)
    
  
