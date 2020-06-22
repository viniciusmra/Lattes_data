import xml.etree.ElementTree as ET
import requests

import csv

import glob

def getLattesData(file):
    data = []
    tree_lattes =  ET.parse(file)

    root_lattes = tree_lattes.getroot()
    data = [root_lattes.find('DADOS-GERAIS').get('NOME-COMPLETO'), root_lattes.get('NUMERO-IDENTIFICADOR')]

    for artigo in root_lattes.iter("ARTIGO-PUBLICADO"):
        # Tag
        sequencia = artigo.get('SEQUENCIA-PRODUCAO')
        ordem_importancia = artigo.get('ORDEM-IMPORTANCIA')

        # Dados Básicos
        natureza = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('NATUREZA')
        idioma = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('IDIOMA')
        flag_divulgacao = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('FLAG-DIVULGACAO-CIENTIFICA')
        doi = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('DOI')
        flag_relevancia = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('FLAG-RELEVANCIA')
        homepage = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('HOME-PAGE-DO-TRABALHO')
        meio_divulgacao = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('MEIO-DE-DIVULGACAO')
        titulo_ingles = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('TITULO-DO-ARTIGO-INGLES')
        pais = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('PAIS-DE-PUBLICACAO')
        ano = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('ANO-DO-ARTIGO')
        titulo = artigo.find('DADOS-BASICOS-DO-ARTIGO').get('TITULO-DO-ARTIGO')
        # Detalhamento do artigo
        pag_inicial = artigo.find('DETALHAMENTO-DO-ARTIGO').get('PAGINA-INICIAL')
        pag_final = artigo.find('DETALHAMENTO-DO-ARTIGO').get('PAGINA-FINAL')
        serie = artigo.find('DETALHAMENTO-DO-ARTIGO').get('SERIE')
        fasciculo = artigo.find('DETALHAMENTO-DO-ARTIGO').get('FASCICULO')
        volume = artigo.find('DETALHAMENTO-DO-ARTIGO').get('VOLUME')
        local = artigo.find('DETALHAMENTO-DO-ARTIGO').get('LOCAL-DE-PUBLICACAO')
        issn = artigo.find('DETALHAMENTO-DO-ARTIGO').get('ISSN')
        titulo_revista = artigo.find('DETALHAMENTO-DO-ARTIGO').get('TITULO-DO-PERIODICO-OU-REVISTA')
        
        paperData = [sequencia, titulo, idioma, issn]
        data.append(paperData)
    return data

all = []
for lattes in glob.glob("lattesXML/*.xml"):
    all.append(getLattesData(lattes))

qualis = []

with open('qualis/qualis3.csv', newline='') as csvfile:
    count = 0
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        for i in range(len(row)):
            if i > 1:
                if row[i] != '':
                    qualis.append([row[0].replace('-',''),row[1],row[i]])
                    break

qualis.remove(['ISSN', 'TITULO', 'ESTRATO'])
for i in all:
    match = 0
    dismatch = 0
    for j in range(2,len(i)):
        found = False
        for line in qualis:
            if line[0] == i[j][3]:
                #print(i[j][3] + ' ' + line[2] + ' ' + line[1])
                found = True
                match +=1
                break
        if found == False:
            #print(i[j][3] + ' ' + line[1] + ' Não encontrado')
            dismatch += 1
    print(i[0])
    print('Numero de publicações: ' + str(len(i)-2))
    print('Com issn: ' + str(match))
    print('Sem issn: ' + str(dismatch))
    print('')

            
        


#lista1 = getLattesData("lattes_pages/curriculo.xml")
#lista2 = getLattesData("lattes_pages/curriculo2.xml")
#print(lista1)

#qualis = "qualis.xml"
#tree_qualis =  ET.parse(qualis)
#root_qualis = tree_qualis.getroot()
#print(root_qualis)
#for linha in root_qualis.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
#    print(linha.find("{urn:schemas-microsoft-com:office:spreadsheet}Cell").get("{urn:schemas-microsoft-com:office:spreadsheet}ss:Index"))
#    for celula in linha.findall("Cell"):
#        print(celula.get("ss:Index"))
    