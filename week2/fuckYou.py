from foaas import fuck
import subprocess

shell = True

def speak(this):
    # print(this)
    this = this.replace("-", ". From; ")
    # print(this)
    subprocess.run(['flite', '-voice', 'file://cmu_us_aew.flitevox', '-t', str(this)])

speak(str(fuck.random(from_='tinkermind').text))
