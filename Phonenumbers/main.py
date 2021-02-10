import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder

number=str(input("Enter the number: "))
ch_number=ph.parse(number, "CH")
print(geocoder.description_for_number(ch_number,'en'))

ser_number=ph.parse(number, "RO")
print(carrier.name_for_number(ser_number,"en"))
