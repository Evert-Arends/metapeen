"""
====================================
     METAPEENER
====================================
Written by @Evert-Arends, functional adjustments @MRS (personal peen)
"""

import requests


class MetaPener():
    def __init__(self):
        pass

    jsonURL = 'https://metapeen.nl/hackflag/scoreboard.json'

    def print_all_scores(self):
        blob = requests.get(self.jsonURL).json()

        for key, value in sorted(blob.iteritems(), reverse=True, key=lambda (k, v): (v, k)):
            print "%s: %s" % (key, value)

    def print_specific_score(self, user):
        blob = requests.get(self.jsonURL).json()

        if user in blob.keys():
            print "Score for %s: %s" % (user, blob.get(user, "ERROR"))
        else:
            print "User doesn't exist."


if __name__ == "__main__":
    m = MetaPener()  # Create instance of the MetaPener class
    m.print_specific_score("bermdingetje")  # Print score of bermdingetje
