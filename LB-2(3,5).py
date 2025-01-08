import json
import requests
from bottle import route, run, request
from datetime import datetime

def form2(date_str_form):
    date_str_form2 = ""
    for i in range(6, 8):
        date_str_form2 += date_str_form[i]
    date_str_form2 += "."
    for i in range(4, 6):
        date_str_form2 += date_str_form[i]
    date_str_form2 += "."
    for i in range(0, 4):
        date_str_form2 += date_str_form[i]
    return date_str_form2

@route('/currency')
def get_currency():
    current_date = datetime.now().date()
    current_date_str = str(current_date)
    current_date_str_form = ""
    nums = [0, 1, 2, 3, 5, 6, 8, 9]
    for i in nums:
        current_date_str_form += current_date_str[i]
    yesterday_date_int = int(current_date_str_form) - 1
    yesterday_date_str_form = str(yesterday_date_int)
    current_date_str_form2 = form2(current_date_str_form)
    yesterday_date_str_form2 = form2(yesterday_date_str_form)
    reply = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=" + yesterday_date_str_form + "&end=" + current_date_str_form + "&valcode=usd&json")
    reply_json = json.loads(reply.text)
    exchange_rate = {}
    for item in reply_json:
        exchange_rate[item['exchangedate']] = item['rate']
    if 'today' in request.query:
        return "Today's (" + current_date_str_form2 + ") USD exchange rate is " + str(exchange_rate[current_date_str_form2])
    if 'yesterday' in request.query:
        return "Yesterday's (" + yesterday_date_str_form2 + ") USD exchange rate is " + str(exchange_rate[yesterday_date_str_form2])

if __name__ == '__main__':
    run(host='localhost', port=8000)
