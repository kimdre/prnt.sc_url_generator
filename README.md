# prnt.sc Link Generator

[![Build Status](https://drone.pyas.de/api/badges/Kim/prnt.sc_url_generator/status.svg)](https://drone.pyas.de/Kim/prnt.sc_url_generator)

## Info

prnt.sc is a web frontend for third-party screenshot software that automatically uploads the user's screenshot and
returns a url of the image to the clipboard so that users can share their screenshot with others via the url.

This is a generator that uses the url scheme to randomly search through the uploaded images.

[Also available as Gist.](https://gist.github.com/kimdre/664f29b7556cb4c26a89315761e6c55d)

## Install and Usage

### Executable file (.exe)

- Just [download](https://git.pyas.de/Kim/prnt.sc_url_generator/raw/branch/master/prnt.sc_link_generator.exe) the
  prepared/standalone file and you are done.
- For downloads see also the [release page](https://git.pyas.de/Kim/prnt.sc_url_generator/releases).

### Python script

#### Requirements

- Python 3 required
- No additional modules required, only built-ins are used.

#### Usage

1. Set the 3 variables in the script to your desired state:
    - `NUMBER_OF_LINKS_TO_GENERATE`: Generates X urls at a time
    - `URL_AUTO_OPEN`: If set to *True* the script opens the URLs automatically in your browser
    - `CLOSE_WINDOW_AFTER`: If set to True the Python window (if run in an desktop environment) won't close after the
      script ends (keeps open to see/copy the original URL)
2. Run the script
3. Have fun searching through random screenshots
