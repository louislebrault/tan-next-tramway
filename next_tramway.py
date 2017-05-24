import time
import tan_plug

response = tan_plug.requestAPI("MDOU", 1, 1)
direction = response[0]
schedules = response[1]
localMinutes = time.localtime()[3] * 60 + time.localtime()[4]
results = []
for val in schedules:
	schedule = tan_plug.scheduleToString(val)
	gap = tan_plug.getGap(tan_plug.scheduleToMinutes(val), localMinutes)
	results.append([schedule, gap])

print('Direction : ' + direction)
print(tan_plug.formatAnswer(results))


input("Appuyez sur ENTREE pour fermer ce programme...")
