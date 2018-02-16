#!/usr/bin/env python

import logging
import subprocess
import sys
import random

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType

# ApiAI
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
sessionID = random.randint(0, 999999999999)

import json
import time

#################################IMPORT COMPLETE###########################################    

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white'];
fancyColors =['gold', 'silver', 'unknown'];

def getPosition(list, item):
    return [(i, sublist.index(item)) for i, sublist in enumerate(list) if item in sublist]

def decodeResistor(band1, band2, band3, band4):
    responseString = '';
    
    resistorValue = 0;

    v1 = getPosition(colors, band1)[0][0]
    v2 = getPosition(colors, band2)[0][0]
    v3 = getPosition(colors, band3)[0][0]
    v4 = getPosition(fancyColors, band4)[0][0]
    #print(v1, v2, v3, v4);
    resistorValue = (v1*10+v2)*pow(10, v3)

    responseString = str(resistorValue) + 'ohms';
    print("Resistance:", resistorValue)
    if v3 > 1:
        responseString = str('{:g}'.format((v1*10+v2)*pow(10, (v3-3)))) + 'K ohms';
    if v3 > 4:
        responseString = str('{:g}'.format((v1*10+v2)*pow(10, (v3-6)))) + ' mega Ohms ';
    if v3 > 7:
        responseString = str('{:g}'.format((v1*10+v2)*pow(10, (v3-9)))) + ' giga Ohms ';
    
    if v4 == 0:
        if random.randint(0, 1):
            responseString += 'plus minus five percent';
        else:
            responseString += 'tolerance five percent';
    if v4 == 1:
        if random.randint(0,1):
            responseString += 'plus minus ten percent';
        else:
            responseString += 'tolerance ten percent';

    return responseString

def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('See you in a bit!')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

def getDialogflowResponse(text):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request() 

    # if continue_session == False:
    request.session_id = sessionID
    #random.randint(0,999999999999) 
    
    request.query = text

    response = request.getresponse()

    return response

def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')   

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        assistant.stop_conversation()
        print('You said:', event.args['text'])
        text = event.args['text'].lower()

        # if text == 'power off':
        #     assistant.stop_conversation()
        #     power_off_pi()
        # elif text == 'reboot':
        #     assistant.stop_conversation()
        #     reboot_pi()
        # elif text == 'ip address':
        #     assistant.stop_conversation()
        #     say_ip()
        
        response = getDialogflowResponse(text)
        responseString = response.read().decode('utf-8')
        responseJSON = json.loads(responseString);
        print (json.dumps(responseJSON, indent = 4, sort_keys = False))
        responseSpeech = str(responseJSON["result"]["fulfillment"]["messages"][0]["speech"])
        print(responseSpeech)
        
        successString = 'Decoding resistor'            
        
        if successString in responseSpeech:
            responseSpeech = decodeResistor(responseJSON["result"]["parameters"]["BandColor1"].lower(),
                                        responseJSON["result"]["parameters"]["BandColor2"].lower(),
                                        responseJSON["result"]["parameters"]["BandColor3"].lower(),
                                        responseJSON["result"]["parameters"]["ToleranceColor"].lower())                
            aiy.audio.say(responseSpeech)            
            main()
        else:
            aiy.audio.say(responseSpeech)
            global sessionID
            sessionID = random.randint(0, 999999999999)
            assistant.start_conversation();       

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    print("loop")  

    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
           process_event(assistant, event)     


if __name__ == '__main__':
    main()
