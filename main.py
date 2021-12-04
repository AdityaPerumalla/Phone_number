import phonenumbers
from phonenumbers import geocoder, carrier

# Parsing String to Phone number
ph_number = phonenumbers.parse('+919440750032')

# Getting carrier of a phone number
Carrier = carrier.name_for_number(ph_number, 'en')

# Getting region information
Region = geocoder.description_for_number(ph_number, 'en')
# Printing the carrier and region of a phone number
print(Carrier)
print(Region)
