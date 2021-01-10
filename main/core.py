import sensors


class Core(object):
	"""docstring for Core"""
	def __init__(self):
		self.sensors = {}

		# 28a19379a2010328
		self._onewire_driver = sensors.OneWireDriver(4)
		self._radiator = sensors.ds18b20('radiators', self._onewire_driver, '28a19379a2010328')

	def add_sensor(self, sensor):
		self.sensors[sensor.name] = sensor

	def run(self):
		self._onewire_driver.update()
		return self._radiator.temperature()
