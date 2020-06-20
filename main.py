import xml.etree.ElementTree as ET
import requests

import csv

lattes = "curriculo.xml"
tree_lattes =  ET.parse(lattes)

root_lattes = tree_lattes.getroot()
print(root_lattes)
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

    #with open(r'curriculo_cimini.csv', mode='a', newline='') as employee_file:
    #    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #    employee_writer.writerow([sequencia, natureza ,titulo, ano])

qualis = "qualis.xml"
tree_qualis =  ET.parse(qualis)
root_qualis = tree_qualis.getroot()
print(root_qualis)
for linha in root_qualis.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
    print(linha.find("{urn:schemas-microsoft-com:office:spreadsheet}Cell").get("{urn:schemas-microsoft-com:office:spreadsheet}ss:Index"))
    for celula in linha.findall("Cell"):
        print(celula.get("ss:Index"))
    