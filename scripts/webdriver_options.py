import json


# Set options for hiding window
def hide_browser_window(options):
    # Check what is the parameter if hiding
    with open('config.json') as file:
        json_result = json.loads(file.read())
    if json_result['chromeWindowSettings']['hideWindow'] == True:
        options.headless = True
    return options
