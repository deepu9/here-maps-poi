#HERE Maps Point Of Interets(POI)

###Install
* Add HERE map API keys in `config.json` in the root folder.
* Run `pip install -e .` from the root folder. This will install all the requirements needed for the task to run.
* Run `export FLASK_APP=here-maps-poi`, then
* Run `export FLASK_ENV=development` and finally
* Run `flask run` to spin up the server.
* You'll see a web URL generated from the above URL. Copy & paste it in the browser.

###Technologies
1. HERE API - https://developer.here.com/develop/rest-apis
2. Flask - https://flask.palletsprojects.com/en/1.1.x/
3. Geopy - https://geopy.readthedocs.io/en/stable/
4. Python v3.7

###Code
Code is separated into two folders
1. **hereAPI** - This is a module and heart of the app, which requests HERE maps API and get the data needed.
It has two files:
    * GeocodeAPI.py - It has only one method, which takes an address as input and spits the Geopy.Location.Location object.
    This object has all the data of the address like coordinates, full address and soon...
    * PlacesAPI - Takes output of Geocode API, which is location object, prepares the request URL with any additional
    parameters passed to it and finally gets the nearby restaurants of the location coordinates.

2. **py-nearest-poi** - This is a Flask app, which has the following routes:
    * index.py - Displays the form with a field to input address and a button.
    * restaurants.py - This does the following:
        - will send the data to GeocodeAPI and gets the location object
        - takes the location object and feed it into PlacesAPI to get the restaurants near the address and
        - finally display them on the map with custom markers. Markers are feeded with the place information.
    
###TODO
1. Need to add:
    * Add other POI's in frontend as a dropdown
    * Add other POI's in backend
2. Tests
    * Mock the **hereAPI** module
    * Add test cases covering the following scenarios:
        - without address
        - with a valid address
        - with a invalid address like Antarctica ocean
3. Need to learn on how to make the `setup.py` run the commands to setup `FLASK_APP` and `FLASK_ENV`