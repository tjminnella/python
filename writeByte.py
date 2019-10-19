import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 1)              #open spi port 0, device (CS) 1


def ReverseBits(byte):
    byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4))
    byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2))
    byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1))
    return byte

def BytesToHex(byte):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

try:
    while True:
        resp = spi.xfer2([0xAA]) # transfer one byte
        time.sleep(0.1)
    #end while
except KeyboardInterrupt:
    print "hello"
    spi.close()
#end try
