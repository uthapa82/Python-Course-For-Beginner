import json
import pygal

from pygal_maps_world import World
from country_code import get_country_code

filename = 'global_gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2010':
        #country_code = gdp_dict['Country Code']
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdps[code] = gdp

cc_gdps_1, cc_gdps_2, cc_gdps3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc] = round(gdp / 1000000000)
    elif gdp < 5000000000:
        cc_gdps_2[cc] = round(gdp / 1000000000)
    else:
        cc_gdps3[cc] = round(gdp / 1000000000)
      
wm = pygal.maps.world.World()
wm.title = 'Global GDP'
wm.add('0-10m', cc_gdps_1)
wm.add('10m-1bn', cc_gdps_2)
wm.add('>1bn', cc_gdps3)

wm.render_to_file('Global GDP.svg')