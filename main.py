from requests import post
from json import loads


def share(ttl, secret, password=None):
    open_url = 'https://onetimesecret.com/secret/'
    url = 'https://onetimesecret.com/api/v1/share'
    data = {'secret': secret, 'ttl': ttl}

    if password:
        data.update({'passphrase': password})

    res = loads(post(url, data=data).text)

    if 'message' in res.keys():
        return 0

    open_url = open_url + res['secret_key']

    return open_url


print(share(7200, 'This is the secret', 'This is the password'))
