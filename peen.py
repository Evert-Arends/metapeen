import requests

jsonUrl = 'https://metapeen.nl/hackflag/scoreboard.json'  # should be json (duh) and is the scoreboard url.


def print_scores():
    blob = requests.get(jsonUrl).json()

    for key, value in sorted(blob.iteritems(), reverse=True, key=lambda (k, v): (v, k)):
        print "%s: %s" % (key, value)

if __name__ == "__main__":
    print_scores()