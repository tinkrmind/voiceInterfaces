import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

import config as config
clientAccessToken = config.dialogflow['clientAccessToken']
CLIENT_ACCESS_TOKEN = clientAccessToken

import json
import codecs

reader = codecs.getreader("utf-8")

def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    # request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "newLaptop"

    request.query = "whats the vlaue of resistor red brown gold"

    response = request.getresponse()

    temp = str(response.read().decode('utf-8'))

    responseJSON = json.loads(temp)

    print (json.dumps(responseJSON, indent = 4, sort_keys = True))
    successString = 'Decoding resistor'
    responseString = str(responseJSON["result"]["fulfillment"]["messages"][1]["speech"])
    if successString in responseString:
        print('Success')
    else:
        print(responseString)
    


if __name__ == '__main__':
    main()