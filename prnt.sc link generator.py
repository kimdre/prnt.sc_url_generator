import random
import string
import webbrowser

"""
prnt.sc is a web frontend for a third-party screenshot software
that automatically uploads the users screenshot and returns a url to the image to the clipboard
so that users can share their screenshot via the url with other people

This is a url generator that takes advantage of the url scheme to search randomly through the uploaded images
"""

NUMBER_OF_LINKS_TO_GENERATE = 5  # generates X urls at a time
URL_AUTO_OPEN = True  # Open the URL automatically in your Browser
CLOSE_WINDOW_AFTER = True  # Closes window at Script end (keep open to see/copy the original url)

##############


def generate_url(base_url: str = 'https://prnt.sc/'):
    random_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
    random_digits = ''.join(random.choice(string.digits) for _ in range(4))

    return f"{base_url}{random_chars}{random_digits}"


for _ in range(NUMBER_OF_LINKS_TO_GENERATE):
    URL = generate_url()
    print(URL)
    if URL_AUTO_OPEN is True:
        webbrowser.open(URL)

if CLOSE_WINDOW_AFTER:
    input('\nPress Enter to Exit...')
