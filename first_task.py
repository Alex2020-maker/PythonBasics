seconds = int(input("Enter a number of seconds: "))

secondsInDay = 86400

days = seconds // secondsInDay
seconds = seconds - (days * secondsInDay)

secondsInHour = 3600

hours = seconds // secondsInHour
seconds = seconds - (hours * secondsInHour)

secondsInMinute = 60

minutes = seconds // secondsInMinute
seconds = seconds - (minutes * secondsInMinute)

print("%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
