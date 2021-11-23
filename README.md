# favorite_photos_finder

## English:

This script scans a given directory containing photos (JPEG, PNG, NEF and CR2),
reads itś Rating from EXIF and generates a link to the original photo
on a directory given if the Rating found is higher or equal to the minimum passed.

The script will check if the file (link to the file) already exists and will not 
duplicate if there's already a link to that file. Also, if there's a file with the
same name, linking to another file, a link will be created with a random name attached to it. 

This script was created for me to make be able to configure a wallpaper changer
so that it could finds all my favorites photos in one point.

    Ps.: 
       - no extra disk space are taken, hard links are used.
       - not tested yet on a huge library, may take a while to complete


    Usage: 
       favorite_photos_finder [-r] [-c rating] -s <output_directory> <library directory>
        * -r: recursive into subdirectories (default=off)
        * -c: minimum Rating to consider
        * -s: output directory where the links will be created
        * <library directory>: where your photos are located

-------------

# Português

Este script escaneia um diretório contendo fotos (JPEG, PNG, NEF e CR2), 
recupera a Classificação (Rating) de cada foto e gera um link em um diretório
passado para a foto caso esta tenha uma Classificação igual ou maior 
que a solicitada.

O script verificará se o arquivo de link já existe para a foto. Caso exista, o link
não será criado. Mas se já existir um link para outra foto, mas com o mesmo nome
do que se estiver tentando criar, o script irá gerar um sufixo aleatório para criar
o novo link. 

Criei este script para basicamente permitir configurar mais facilmente 
programas, como um Trocador de Papel de Parede que recebe um diretório 
único. Assim somente as minhas fotos favoritas serão mostradas. 

     Ps.: 
       - nenhum espaço extra é ocupado, são usados hard links
       - não foi testado ainda em bibliotecas muito grandes


# Python Modules used/Módulos do Python Utilizados:
   - Python 3
   - py3exiv2
   - glob
   - shortuuid
   - pyexiv2
   - gettext
   - XmpValueError