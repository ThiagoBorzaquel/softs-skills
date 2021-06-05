# Descobrindo o ip dos sites

import socket as s

# Host que deseja descobrir o ip #
#host = 'google.com'
host = input('insera seu site: ')

# captura do ip do host desejado #
Ip = s.gethostbyname(host)

# Mostra resultado #
print('O ip do host "' + host + '" é: ' + Ip)