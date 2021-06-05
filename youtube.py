from pytube import YouTube

# Digite o link do video e o local que deseja salvar o video #
link = input('Digite o link do video que deseja baixar: ')
path = input('Digite o diretorio que deseja salva o video: ')
yt = YouTube(link)

# Mostrar os detalhes do video #
print('Titulo ', yt.title)
print('Numero de views: ', yt.views)
print('Tananho do video: ', yt.length, 'segundos')
print('Avaliação do video: ', yt.rating)

# Usar a maior resolução do video #
ys = yt.streams.get_highest_resolution()

# Começa o download do video #
print('Baixando...')
ys.download(path)
print('Download completo!')
