import datetime

now = datetime.datetime.now()
alarm = now + datetime.timedelta(hours=8, minutes=30)

curr_time = str(now.hour) + ':' + str(now.minute)
alarm_time = str(alarm.hour) + ':' + str(alarm.minute)

# curr_time = f'{now.hour}:{now.minute}'
# alarm_time = f'{alarm.hour}:{alarm.minute}'

print('Now: ' + curr_time + '\n' + 'Alarm: ' + alarm_time)


