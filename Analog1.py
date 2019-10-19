#!/usr/bin/python3
import spidev
spi = SpiDev()
spi.open(0,0)
channel = 0
vRef = 3300
result = spi.xfer2([1, (8 + channel) << 4, 0])
adcValue = ((result[1] & 3) << 8) + result[2]
mVolts = round((adcValue * (vRef / 1024.0)),2)
tempC = round(((mVolts - 500) / 10.0), 2)
tempF = round((tempC * (9.0/5.0) + 32.0), 2)
print('Content-Type: text/html')
print('')
print('<html>')
print('<head>')
print('<title>Temperature Sensor</title>')
print('</head>')
print('<body>')
print('<h2>Current Temperature Sensor Info</h2>')
print('The ADC value is:', data, '<br />')
print('The voltage is:', mVolts,'millivolts<br />')
print('The temperature is:',tempC,'degrees C<br />')
print('The temperature is:',tempF,'degrees F')
print('</body>')
print('</html>')
spi.close()
