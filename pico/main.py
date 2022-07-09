import machine
import utime

sensor = machine.ADC(28)
led = machine.Pin(25, machine.Pin.OUT)
while True:
	sensor_value = sensor.read_u16()
	print(sensor_value)
	led.value(1)
	utime.sleep(0.1)
	led.value(0)
	utime.sleep(0.9)
