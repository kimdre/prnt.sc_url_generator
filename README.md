# prnt.sc Link Generator

## Info
prnt.sc is a web frontend for third-party screenshot software that automatically uploads the user's screenshot and returns a url of the image to the clipboard
so that users can share their screenshot with others via the url.

This is a generator that uses the url scheme to randomly search through the uploaded images.

## Requirements / Install
- Python 3 required
- No additional Modules required, only Built-ins are used.

## Usage
1. Set the 3 Variables in the Script to your desired State:
   - NUMBER_OF_LINKS_TO_GENERATE: Generates X urls at a time
   - URL_AUTO_OPEN: If set to True the Script opens the URLs automatically in your Browser
   - CLOSE_WINDOW_AFTER: If set to True the Python Window (if run in an Desktop Environment) won't close after the Script ends (keeps open to see/copy the original url)
2. Run the Script
3. Have fun searching through random screenshots
