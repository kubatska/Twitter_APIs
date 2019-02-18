import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

# Ignore SSL certificate errors


def inform_friends(acct):
    """
    Return a information about the account followers in json format.
    """
    while True:
        # acct = input('Enter Twitter Account:')
        # acct = str(acct)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

        if (len(acct) < 1): break
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '25'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js = json.loads(data)

        headers = dict(connection.getheaders())
        print('Remaining', headers['x-rate-limit-remaining'])

        return js

