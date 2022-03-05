import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier

countryCode = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(countryCode, "en"))

serviceProvider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(serviceProvider, "en"))