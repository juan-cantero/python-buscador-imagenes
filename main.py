import logging
from api import PixabayAPI
import threading
import time

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'computadoras'
api = PixabayAPI('15310730-4b58aad1f4a3657eafdaf8dd6', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 10)


for u in urls:
  t1 = threading.Thread(target=api.descargar_imagen,args=(u,))
  t1.start()





