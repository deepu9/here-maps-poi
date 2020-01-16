#! python
# PlacesAPI.py - Takes geo coordinates and returns the restaurants near by
import geopy
import json
import requests


class PlacesAPI:
    baseUrl = 'https://places.cit.api.here.com/places/v1'
    app_id = ''
    app_code = ''

    def __init__(self, app_id, app_code, location: geopy.Location):
        self.location = location
        self.app_id = app_id
        self.app_code = app_code

    '''
    Prepare coordinates string taken from Location object
    
    :param string delimiter: Delimiter string, of which the coordinates string should be concat
    :returns: String type of concatenated coordinates
    '''

    def format_coordinates_as_string(self, delimiter=','):
        return delimiter.join([str(self.location.latitude), str(self.location.longitude)])

    '''
    Prepare discovery/explore url with additional parameters(if provided) attached
    
    :param dict request_params: Additional parameters for adding to places endpoint
    :returns: String formatted places endpoint
    '''
    def prepare_discover_explore_url(self, request_params: dict = None):
        request_url = '%s/discover/explore?app_id=%s&app_code=%s&at=%s&pretty' % (
            self.baseUrl,
            self.app_id,
            self.app_code,
            self.format_coordinates_as_string()
        )

        if request_params is None:
            return request_url

        for key, value in request_params.items():
            request_url += '&{key}={value}'.format(key=key, value=value)

        return request_url

    '''
    Send a request to HERE maps Places API and get the near by places response back
    
    :param dict request_params: Additional parameters for adding to places endpoint
    :returns: Json formatted places api response, which are near by restaurants of an address
    '''
    def get_near_by_places(self, request_params: dict = None):
        if request_params is None:
            request_params = {}

        response = requests.get(self.prepare_discover_explore_url(request_params))
        response.raise_for_status()

        return json.loads(response.text)
