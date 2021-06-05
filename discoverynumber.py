# Descobrir a operadora e região através do numero do celular

import phonenumbers
from phonenumbers import geocoder, carrier

# Digite seu número com codigo do país e ddd #
phoneNumer = phonenumbers.parse(input('Digite seu numero: '))
#phoneNumer = phonenumbers.parse("+5521996396102")

# Captura a operadora #
Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

# Captura a região #
Region = geocoder.description_for_number(phoneNumer, 'pt-br')

# Mostra o resultado #

print('A operadora é: ' + Carrier)
print('O estado é: ' + Region)
