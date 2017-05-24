import urllib.request
import json

def requestAPI(codeArret, ligne, sens):
	url = "http://open_preprod.tan.fr/ewp/horairesarret.json/" + codeArret + "/" + str(ligne) + "/" + str(sens)
	res = urllib.request.urlopen(url).read().decode('cp1252')
	jsonRes = json.loads(res)
	sens = jsonRes['ligne']['directionSens' + str(sens)]
	schedules = []
	for val in jsonRes['prochainsHoraires']:
		schedule = {}
		schedule['hours'] = int(val['heure'].replace('h', ''))
		# Parfois l'api met un a ou un d après les minutes pour dire genre la direction
		schedule['minutes'] = int(val['passages'][0].replace('d', '').replace('a', ''))
		schedules.append(schedule)
	result = [sens, schedules]
	return result

def scheduleToMinutes(schedule):
	return schedule['hours'] * 60 + schedule['minutes']

def getGap(minutes, localMinutes):
	if (minutes < localMinutes):
		minutes += 1440
	gap = minutes - localMinutes
	return gap

def scheduleToString(schedule):
	if (schedule['hours']< 10):
		hours = "0" + str(schedule['hours'])
	else:
		hours = str(schedule['hours'])

	if (schedule['minutes']< 10):
		minutes = "0" + str(schedule['minutes'])
	else:
		minutes = str(schedule['minutes'])

	return hours + "h" + minutes

def formatAnswer(results):
	answer = ""
	for result in results:
		answer += result[0] + ", passe dans " + str(result[1]) + " minutes \n"
	return answer
