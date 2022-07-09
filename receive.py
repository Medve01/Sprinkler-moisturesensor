import serial
import json

with open('config.json') as configfile:
	config = json.load(configfile)

dry_value = int(config['min'])
wet_value = int(config['max'])
value_range = dry_value - wet_value


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.050)
fetched_data = []
while len(fetched_data) < 5:
	while ser.in_waiting:
		data_in = ser.readline().decode('UTF-8')
		data = int(data_in)-wet_value
		moisture_value = value_range-data
		moisture_percent = (moisture_value / value_range) * 100
		if moisture_percent < 0:
			moisture_percent = 0
		fetched_data.append(moisture_percent)
#		print('Data from pico', str(data_in).replace('\r\n', ''), int(moisture_percent))
print(json.dumps({'Sampled moisture:':int(sum(fetched_data) / len(fetched_data))}))
