import json
filename='data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

all_eq_dicts=all_eq_data['features']
mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

with open('data/data_lons.json','w') as f:
    json.dump(lons,f)
with open('data/data_lats.json','w') as f:
    json.dump(lats,f)
with open('data/data_titles.json','w') as f:
    json.dump(titles,f)
with open('data/data_mags.json', 'w') as f:
    json.dump(mags, f)