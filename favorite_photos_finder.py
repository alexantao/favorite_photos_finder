#! /usr/bin/env python
# This Python file uses the following encoding: utf-8

##################################################
#
#   By: Alex Antão
#
#   Script para separar as imagens FAVORITAS
#  em um diretório ou subdiretorios, criando
#  hardlinks em um diretório específico.
#
#   Útil quando você tem uma biblioteca e quer
#  uma relação das imagens favoritas para utilizar
#  em outra aplicação, como papeis de parede.
#
##################################################
#
#  Uso: lista_favorios.py -c <classif. minima> [-s <diretorio de saida>] [-r] <diretorio>
#
#	-c: classificação minima, 0-5
#	-o: diretorio onde os hardlinks serão criados
#	-r: recursivo, entra nos subdiretórios
#	<diretório> : onde serão criados os links (tem que ser no mesmo FS!)
#
##################################################


import argparse
import os
import sys
import glob
import shortuuid
import pyexiv2
import gettext
from pyexiv2 import XmpValueError

##############################################################################################################
DEBUG = 0   # Just for DEBUG porposes
_ = gettext.gettext

##############################################################################################################
# VERSÃO MÍNIMA DO PYTHON
current_maj_version = sys.version_info.major
if current_maj_version <= 2:
    print(_('Este script deve ser rodado em Python 3.x'))
    exit()

##############################################################################################################
# OPÇÕES DA LINHA DE COMANDO [-r] <diretorio>
parser = argparse.ArgumentParser(description=_('Lista Imagens Favoritas'))

parser.add_argument('-c', '--classificacao', dest='classificacao', type=int, default=5,
                    help=_('Classificação Mínima'))
parser.add_argument('-s', '--saida', dest='dir_saida', type=str, default="./", help=_('Diretório de Saída'))
parser.add_argument('-r', '-recursivo', dest='recursivo', action='store_true', default=False, help=_('Entra nos Subdiretórios?'))
parser.add_argument('dir_imagens', help=_('Diretório das Imagens'))

args = parser.parse_args()

if not len(sys.argv) > 1:
    parser.print_help()
    exit()

##############################################################################################################
# MENSAGENS DE DEBUG
def meuprint(message=""):
    if DEBUG == 1:
        print(message)

##############################################################################################################
# Procura no diretório se existe um link para o arquivo passado.
def procura_arquivo_igual(original, diretorio):
    arquivos = glob.glob(diretorio + "/*")
    meuprint(_("\tArquivos encontrados em ") + diretorio + ": " + str(arquivos))
    for arquivo in arquivos:
        if  os.path.samefile(arquivo, original): return True
    return False

##############################################################################################################
# Encontra as imagens com o Rating acima ou igual ao passado
def processa_imagem(nome_imagem, classificacao, dir_destino):
    # Descobre a classificação da imagem
    img_classific = 0

    # ---------  METODO EXIV2 ---------------
    try:
        img_meta = pyexiv2.ImageMetadata(nome_imagem)
        img_meta.read()

        tag = img_meta['Xmp.xmp.Rating']
        img_classific = int(tag.raw_value)

    except (KeyError, XmpValueError):
        img_classific = 0

    #-------------------------------------------
    # Dir destino: Cria e testa se não é um arquivo
    if not os.path.exists(dir_destino):
        os.mkdir(dir_destino)
    elif os.path.isfile(dir_destino):
        print(_("Diretório de destino existe como ARQUIVO"))
        exit(1)

    # Agora se a classificação for maior ou igual à passada, criamos o link
    if img_classific >= classificacao:
        nome_img = os.path.basename(nome_imagem)
        nome_copia = os.path.join(dir_destino, nome_img)

        #---------------   NOVA ABORDAGEM ----------------
        # Procura pela copia já existente
        if procura_arquivo_igual(nome_imagem, os.path.dirname(nome_copia)):
            meuprint(_("\tImagem já existe no destino..."))
            return
        else: # arquivo não existe
            #  Mesmo se não existe, pode ter um arquivo diferente com o mesmo nome
            if os.path.exists(nome_copia):  # Existe Arquivo com mesmo nome, vamos gerar um novo para o nosso.
                nome_arq, extensao = os.path.splitext(nome_img)
                nome_copia = os.path.join(dir_destino, nome_arq + "-" + shortuuid.uuid() + extensao)

        # Cria os links
        meuprint(_("\tCriando link: ") + nome_imagem + " -> " + nome_copia)
        os.link(nome_imagem, nome_copia)

    return 0


##############################################################################################################
# Lista todas as imagens do diretorio passado, recursivamente ou nao
def lista_imagens(diretorio, recursivo):
    ext_imagens = ['[pP][nN][gG]', '[jJ][pP][gG]', '[jJ][pP][eE][gG]', '[cC][rR][2]', '[nN][eE][fF]']
    imagens = []

    str_search = '/**/*.' if recursivo == True else '/*.'
    [imagens.extend(glob.glob(diretorio + str_search + ext, recursive=recursivo)) for ext in ext_imagens]

    return imagens


##############################################################################################################
if __name__ == '__main__':

    print(_("Procurando as imagens no diretório (Recursivo = ") + str(args.recursivo) + _(")... aguarde..."))

    if args.recursivo:
        print(_("(Pode demorar, dependendo do tamanho da biblioteca.)"))

    imagens = lista_imagens(args.dir_imagens, args.recursivo)
    for imagem in imagens:
        processa_imagem(imagem, args.classificacao, args.dir_saida)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/