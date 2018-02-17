# Voioce Interface

For [Voice interface class Spring 2018, ITP](https://github.com/juxtapix/ExpressiveInterfaces_Voice/wiki)

# Week 1 : chattyBot

This is a voice-output interface for CleverBot, a chatbot. 

![chattyBot](https://github.com/tinkrmind/voiceInterfaces/blob/master/week1/chattyBotDemo.gif)

### [Demo Video](https://vimeo.com/256171663)

Needs python3, cleverwrap and flite chattyto run python should be present in a unix terminal

    pip install cleverwrap

    sudo apt-get install flite

Usage:

    python chatBot.py
    
then just type after the > prompt.

To exit, type > I'm leaving

# Week 2 : fuckOff

![fuckOff](https://github.com/tinkrmind/voiceInterfaces/blob/master/week2/fuckOff.gif)

## [Demo Video](https://vimeo.com/256171889)

fuckOff affords you a terminal interface to tell people to stop disturbing you when you're in the zone. After you're done setting it up, typing fuckOff speaks a random fuck you.

The code is fairly self-explanatory. The simple python script uses [foaas-python](https://github.com/dmpayton/foaas-python), a python wrapper for [foaas API](https://www.foaas.com/) which returns a string saying fuck off in a random way. This string is then spoken by [flite](http://www.festvox.org/flite/), a command line TTS tool. 

Needs foaas-python and python3

     pip install foaas


A good way to use this is to set up an alias for the python file execution.
Eg. 

    $ echo "alias fuckOff=python3 ~/PROJECTS/voiceInterface/foaas/fuckYou.py" >> ~/.bash_aliases && source ~/.bash_aliases
    
    $ fuckOff
    
    * computer tells everyone to fOff in a random way *  

# Week 3 : Electron

![Electron](https://github.com/tinkrmind/voiceInterfaces/blob/master/week3/simpleDemoGIF.gif)

## [Demo Video](https://vimeo.com/255838314)

Meet electron, your electronics help assistant. Right now, he can make some small talk and decode resistor values from the color bands. But soon he'll be able to help you design circuits, decide component values, translate obscure smd codes, read pinouts and more!
