#! python
# GeocodeAPI - Sends a request in the form of address and gets the geo coordinates
from geopy.geocoders import Here


class GeocodeAPI:
    app_id = ''
    app_code = ''

    def __init__(self, app_id, app_code):
        self.app_id = app_id
        self.app_code = app_code

    '''
    Get coordinates for an address
    
    :param string address: Addresses of a place in string
    :returns: A Geopy location object
    
    References
    ===========
    .. https://geopy.readthedocs.io/en/stable/#geopy.location.Location
    '''
    def get_geo_coordinates_from_address(self, address):
        if not address:
            return {
                'error': True,
                'message': 'Address is required'
            }

        geocoder = Here(self.app_id, self.app_code)
        response = geocoder.geocode(address)

        return response
