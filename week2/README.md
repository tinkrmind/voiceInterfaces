# fuckOff

For [Voice interface class Spring 2018, ITP](https://github.com/juxtapix/ExpressiveInterfaces_Voice/wiki) Week 2

fuckOff affords you a terminal interface to tell people to stop disturbing you when you're in the zone. After you're done setting it up, typing fuckOff speaks a random fuck you.

The code is fairly self-explanatory. The simple python script uses [foaas-python](https://github.com/dmpayton/foaas-python), a python wrapper for [foaas API](https://www.foaas.com/) which returns a string saying fuck off in a random way. This string is then spoken by [flite](http://www.festvox.org/flite/), a command line TTS tool. 

Needs foaas-python and python3

     pip install foaas


A good way to use this is to set up an alias for the python file execution.
Eg. 

    $ echo "alias fuckOff=python3 ~/PROJECTS/voiceInterface/foaas/fuckYou.py" >> ~/.bash_aliases && source ~/.bash_aliases
    
    $ fuckOff
    
    * computer tells everyone to fOff in a random way *  
