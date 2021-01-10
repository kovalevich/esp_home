from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
	o = OTAUpdater('https://github.com/kovalevich/esp_home')
	o.install_update_if_available_after_boot('inet5', '68005705')


def start():
	from main import core as c
	core = c.Core()
	core.run()


def boot():
	download_and_install_update_if_available()
	start()


boot()
