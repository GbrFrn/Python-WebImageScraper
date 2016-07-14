from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll("img", {"class":"thumb-veiculo"})]
    print (str(len(images)) + "imagens encontradas")
    print ('Baixando imagens para o diretório.')
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)
    return image_links


entrada = input("Digite a URL do site:")

get_images(entrada)

import os
import shutil
sourcepath="C:\\Users\\Gabriel Fernandes\\Desktop\\Script"
source = os.listdir(sourcepath)

pasta = input("Cole o caminho da pasta de destino:")

destinationpath = pasta
for files in source:
    if files.endswith('.jpg'):
        shutil.move(os.path.join(sourcepath,files), os.path.join(destinationpath,files))


k=input("Pressione qualquer tecla para sair.")
