import json
import pandas as pd

df = pd.read_csv('Rat_Sightings_New.csv')
jsonfile = open('rat_sightings.json', 'w')

def get_nested_rec(key, grp):
	rec = {}
	rec['dateCreated'] = key[1]
	rec['locationType'] = key[2]
	rec['incidentZip'] = key[3]
	rec['incidentAddress'] = key[4]
	rec['city'] = key[5]
	rec['borough'] = key[6]
	rec['latitude'] = key[7]
	rec['longitude'] = key[8]

	return rec

records = {}
for key, grp in df.groupby(['key', 'dateCreated', 'locationType', 'incidentZip', 'incidentAddress', 'city', 'borough', 'latitude', 'longitude']):
	report_key = key[0]
	rec = get_nested_rec(key, grp)
	records[report_key] = rec

records = dict(reports = records)

jsonfile.write(json.dumps(records, indent=4))