# favorite_photos_finder
## English:

This script scans a given directory containing photos (JPEG, PNG, NEF and CR2),
reads itś Rating from EXIF and generates a link to the original photo
on a directory given if the Rating found is higher or equal to the minimum passed.

This script was created for me to make be able to configure a wallpaper changer
so that it could finds all my favorites photos in one point.

    Ps.: 
       - no extra disk space are taken, hard links are used.
       - not tested yet on a huge library, may take a while to complete

-------------

# Português

Este script escaneia um diretório contendo fotos (JPEG, PNG, NEF e CR2), 
recupera a Classificação (Rating) de cada foto e gera um link em um diretório
passado para a foto caso esta tenha uma Classificação igual ou maior 
que a solicitada.

Criei este script para basicamente permitir configurar mais facilmente 
programas, como um Trocador de Papel de Parede que recebe um diretório 
único. Assim somente as minhas fotos favoritas serão mostradas. 

     Ps.: 
       - nenhum espaço extra é ocupado, são usados hard links
       - não foi testado ainda em bibliotecas muito grandes


# Dependencies/Dependências:
   - Python 3
   - py3exiv2