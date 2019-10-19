from time import sleep

import subprocess

# to prevent from spi failures reload spi driver at the beginning
unload_spi=subprocess.Popen('sudo rmmod spi_bcm2708', shell=True, stdout=subprocess.PIPE)
start_spi=subprocess.Popen('sudo modprobe spi_bcm2708', shell=True, stdout=subprocess.PIPE)
sleep(3)

#import spidev and open SPI to work with ADC on Gerboard
import spidev

loops = 600

spi=spidev.SpiDev()
#the ADC of the Gerboard is on SPI channel 0
spi.open(0,0)

#depending on the Pin you use on Gerboard select 0 (for AD0) or 1 (for AD1)
channel = 1

#if variable loops is 600, there are 600 values printed out before the program ends
while loops > 0:
    #send start bit, sql/diff, odd/sign, MSBF to SPI
    r = spi.xfer2([1,(2+channel)<<6,0])
    #spi.xfer2 returns same number of 8-bit bytes as sent
    #we parse out the part of bits which includes the changing value of the sensor
    adc_value = ((r[1]&31) << 6) + (r[2] >> 2)
    #print the value
    print(adc_value)
    #delay after each print
    sleep(0.05)
    #decrease variable loop
    loops -= 1
