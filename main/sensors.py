from machine import Pin
import onewire
import time, ds18x20
import binascii


class Sensor(object):
	"""docstring for Sensor"""
	def __init__(self, name, driver, address = '', important = False):
		self._driver = driver
		self.name = name
		self.address = address
		self.important = important
		self._temperature = None


class ds18b20(Sensor):
	"""docstring for ds18b20"""
	def __init__(self, name, driver, address, important = False):
		super(ds18b20, self).__init__(name, driver, address, important)
		self._type = 'ds18b20'

	def temperature(self):
		return self._driver.sensor(self.address)
		

class OneWireDriver(object):
	"""docstring for Sensors"""
	def __init__(self, pin):
		self._ow = onewire.OneWire(Pin(pin))
		self._ds = ds18x20.DS18X20(self._ow)
		self._roms = self._ds.scan()
		self._sensors = {}

	def update(self):
		self._ds.convert_temp()
		time.sleep_ms(750)
		for rom in self._roms:
			self._sensors[self._address(rom)] = self._ds.read_temp(rom)

	def print_all(self):
		self.update()
		for rom in self._roms:
			print(self._ds.read_temp(rom))
	
	def devices(self):
		self.update()
		return list(map(lambda rom: self._rom_to_sensor(rom), self._roms))

	def _address(self, rom):
		return ''.join('{:02x}'.format(x) for x in rom)

	def sensor(self, address):
		return self._sensors[address]	

	def _rom_to_sensor(self, rom):
		return { 'addr': self._address(rom), 'temp': self._rom_temperature(rom)}

	def _rom_temperature(self, rom):
		return self._ds.read_temp(rom)