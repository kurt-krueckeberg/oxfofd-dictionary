# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '3946d338'
app_key = 'ed3b30b2cee9bc736eb9d6ed63873c24'

language = 'de'
word_id = 'Handeln'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/lemmas/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
