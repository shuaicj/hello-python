#!/usr/bin/env python3

from datetime import datetime, timedelta, timezone

dt = datetime(2018, 9, 30, 11, 40, 42, 921871)
print(type(dt))
print(dt)

now = datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

ts = now.timestamp()
print('timestamp', ts)
print('fromtimestamp', datetime.fromtimestamp(ts))

s = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print('strftime', s)
print('strptime', datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f'))

print('timedelta', now + timedelta(days=3))

utc = datetime.now(timezone.utc)
print('utc      ', utc)
print('utc+03:00', utc.astimezone(timezone(timedelta(hours=3))))
print('local tz ', utc.astimezone())

