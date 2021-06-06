from termcolor import colored as color
import statistics
import math
from scipy import stats
import matplotlib.pyplot as plt

 
def getStats (medias):
  var = statistics.variance(medias)
  mean = statistics.mean(medias)
  stdev = statistics.stdev(medias)
  
  print(color("Variância: ", 'cyan')+ str(var))
  print(color("Média: ", 'cyan') + str(mean))
  print(color("Desvio padrão: ", 'cyan') + str(stdev))
  # Gera o intervalo de 95% ao redor da média de uma distribuição normal com escala pelo desvio padrão sobre as amostras. 
  # Esta é a z-score das amostras das médias
  print(color("Intervalo de Confiança da Média (95%): ", 'cyan') + str(stats.norm.interval(0.95, loc=mean, scale = stdev / math.sqrt(len(medias)) )))
  plt.hist(medias)
