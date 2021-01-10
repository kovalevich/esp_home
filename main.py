from ota_updater.app.ota_updater import OTAUpdater


def download_and_install_update_if_available():
	o = OTAUpdater('url-to-your-github-project')
	o.install_update_if_available_after_boot('inet5', '68005705')


def start():
	pass
	# your custom code goes here. Something like this: ...
	# from main.x import YourProject
	# project = YourProject()
	# ...


def boot():
	download_and_install_update_if_available()
	start()


boot()
