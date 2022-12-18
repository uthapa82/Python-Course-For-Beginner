import json
import pygal

from country_code import get_country_code

filename = '../dataset/electric data.json'
with open(filename) as f:
    ag_data = json.load(f)

cc_ag = {}
for ag_dict in ag_data:
    if ag_dict['Year'] == '2014':
        country_code = ag_dict['Country Code']
        country_name = ag_dict['Country Name']
        ag = int(float(ag_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_ag[code] = ag

cc_ag_1, cc_ag_2, cc_ag3 = {}, {}, {}
for cc, ag in cc_ag.items():
    if ag < 5000000000:
        cc_ag_1[cc] = round(ag / 1000000000)
    elif ag < 5000000000:
        cc_ag_2[cc] = round(ag / 1000000000)
    else:
        cc_ag3[cc] = round(ag / 1000000000)
      
wm = pygal.maps.world.World()
wm.title = 'Agricultural Land'
wm.add('0-10m', cc_ag_1)
wm.add('10m-1bn', cc_ag_2)
wm.add('>1bn', cc_ag3)

wm.render_to_file('Agricultural Land.svg')