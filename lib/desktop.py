import notify2


def desktop_notify(message):
	#Initialise the d-bus connection.
	notify2.init('Process ending notification')

	#Create notification object.
	noti = notify2.Notification(message)

	#Set urgency level.
	noti.set_urgency(notify2.URGENCY_CRITICAL)

	#Show notification.
	noti.show()

