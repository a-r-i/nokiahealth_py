import requests

def get_accesstoken(client_id, client_secret, code, redirect_uri):
    url = "https://account.health.nokia.com/oauth2/token"

    payload = {
                "grant_type": "authorization_code",
                "client_id": client_id,
                "client_secret": client_secret,
                "code": code,
                "redirect_uri": redirect_uri
              }

    r = requests.post(url, data=payload)

    return r.json()

def refresh_accesstoken(client_id, client_secret, refresh_token):
    url = "https://account.health.nokia.com/oauth2/token"

    payload = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
              }

    r = requests.post(url, data=payload)

    return r.json()

def refresh_accesstoken(client_id, client_secret, refresh_token):
    url = "https://account.health.nokia.com/oauth2/token"

    payload = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
              }

    r = requests.post(url, data=payload)

    return r.json()

def get_sleep(access_token, startdate, enddate):
    url = "https://api.health.nokia.com/v2/sleep?action=get"

    payload = {
               "access_token": access_token,
               "startdate": startdate, # UNIXタイムスタンプで指定
               "enddate": enddate # UNIXタイムスタンプで指定
              }

    r = requests.get(url, params=payload)

    return r.json()

def get_summary(access_token, startdateymd, enddateymd):
    url = "https://api.health.nokia.com/v2/sleep?action=getsummary"

    payload = {
               "access_token": access_token,
               "startdateymd": startdateymd, # YYYY-MM-DD形式で指定
               "enddateymd": enddateymd # YYYY-MM-DD形式で指定
              }

    r = requests.get(url, params=payload)

    return r.json()

def get_meas(access_token, startdate, enddate):
    url = "https://api.health.nokia.com/measure?action=getmeas"

    payload = {
                "access_token": access_token,
                "startdate": startdate, # UNIXタイムスタンプで指定
                "enddate": enddate # UNIXタイムスタンプで指定
              }

    r = requests.get(url, params=payload)

    return r.json()
