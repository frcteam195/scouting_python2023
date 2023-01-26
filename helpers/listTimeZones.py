import pytz

print('US TimeZones')
for timeZone in pytz.country_timezones['US']:
    print(timeZone)