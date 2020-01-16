import json
import os

from flask import (
    Blueprint, render_template, request, redirect, url_for
)


from hereAPI import GeocodeAPI, PlacesAPI

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')


@bp.route('/map-view', methods=('GET', 'POST'))
def map_view():
    if request.method == 'POST':
        address = request.form['address']
        places_data = {}

        with open(os.path.join(os.getcwd(), 'config.json')) as json_data_file:
            config = json.load(json_data_file)

        here_api_creds = config['here_api']
        app_id = here_api_creds['APP_ID']
        app_code = here_api_creds['APP_CODE']

        res = GeocodeAPI.GeocodeAPI(app_id, app_code)
        location_obj = res.get_geo_coordinates_from_address(address)

        near_by_places = PlacesAPI.PlacesAPI(app_id, app_code, location_obj) \
            .get_near_by_places({'cat': 'restaurant'})

        for place in near_by_places['results']['items']:
            places_data.update({place['id']: {
                'title': place['title'],
                'icon': place['icon'],
                'position': place['position'],
                'opening_status': ('Open' if place['openingHours']['isOpen'] else 'Closed') if place.get('openingHours') else None,
                'opening_hours': place['openingHours']['text'] if place.get('openingHours') else None,
                'distance': '%.2f km' % (place['distance'] / 100)
            }})

        return render_template(
            'map.html',
            near_by_places=list(places_data.values()),
            here_api_creds=here_api_creds,
            base_position=near_by_places['search']['context']['location']['position']
        )

    return redirect(url_for('index'))
