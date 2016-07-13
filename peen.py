import requests

JSONURL = 'https://metapeen.nl/hackflag/scoreboard.json'

if __name__ == "__main__":
    pass

class Peen:
    def __init__(self):
        self.getpeen()

    def getpeen(self):
        blob = requests.get('https://metapeen.nl/hackflag/scoreboard.json').json()

        for key, value in sorted(blob.iteritems(), reverse=True, key=lambda (k, v): (v, k)):
            print "%s: %s" % (key, value)
