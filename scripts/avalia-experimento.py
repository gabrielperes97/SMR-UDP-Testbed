import csv
import statistics
import math
import numpy
from sys import argv

LIMITE_AMOSTRAS=10000

def caracteriza_amostra(amostra):
   print(str(len(amostra)) + ' amostras')
   print('MEDIA = ' + str(statistics.mean(amostra)).replace(".",","))
   media = statistics.mean(amostra)
   print('desv.padrao = ' + str(statistics.stdev(amostra)))
   desviop = statistics.stdev(amostra)

   # parametro z para intervalo de confianca de 95% e distribuicao normal
   z = 1.96
   tam_pop = len(amostra)
   erro = z * desviop / math.sqrt(tam_pop)
   print('Margem de erro = ' + str(erro) + ' - ' + '{:.2f}'.format(100*erro/media) + '%')

   # amostras fora da margem de erro
   # fora = [o for o in amostra if o < (media-desviop) or o > (media+desviop)]
   # print('amostras fora: ' + str(len(fora)) + ' ou ' + str(100*len(fora)/len(amostra)) + '%')





with open(argv[1]) as dados_csv:
   leitorcsv = csv.reader(dados_csv, delimiter=',')
   medicoes_raw = [float(x[1]) for x in leitorcsv]
   medicoes = medicoes_raw[:LIMITE_AMOSTRAS]

   print("\n**********************************************************")

   caracteriza_amostra(medicoes)

   # remocao de outliers
   menores = numpy.percentile(medicoes, 10)
   maiores = numpy.percentile(medicoes, 90)

   medicoes_noout = [x for x in medicoes if x > menores and x < maiores]

   print('-------')
   caracteriza_amostra(medicoes_noout)

   
   

