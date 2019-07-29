import requests, json
from urllib.parse import urlparse, parse_qs


def buscaProposicaoAno(ano, pagina=1, ordenarPor='id', itens=100):

    url = f'https://dadosabertos.camara.leg.br/api/v2/proposicoes?ano={ano}&ordem=ASC&ordenarPor={ordenarPor}&pagina={pagina}&itens={itens}'

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.get(url, headers=headers)

    json_data = json.loads(r.text)
    data = json_data['dados']
    
    return data


    # RREO
    'http://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo?an_exercicio=2019&nr_periodo=1&co_tipo_demonstrativo=RREO&no_anexo=RREO-Anexo%2001&id_ente=53'

    # RGF
    'http://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf?an_exercicio=2019&in_periodicidade=Q&nr_periodo=1&co_tipo_demonstrativo=RGF&no_anexo=RGF-Anexo%2001&co_poder=E&id_ente=53'

    # DCA
    'http://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2017&no_anexo=Anexo%20I-AB&id_ente=53'
    'http://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2017&no_anexo=DCA-Anexo%20I-AB&id_ente=53'