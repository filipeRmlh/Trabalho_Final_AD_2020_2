from termcolor import colored as color
import statistics
import math
from scipy import stats
import matplotlib.pyplot as plt
import pylab

 
def getStats (samble_means):
    variance = statistics.variance(samble_means)
    mean = statistics.mean(samble_means)
    stdev = statistics.stdev(samble_means)
    confidence = str(stats.norm.interval(0.95, loc=mean, scale = stdev / math.sqrt(len(samble_means)) ))
    return {
        "variance": variance,
        "mean": mean,
        "stdev": stdev,
        "confidence": confidence
    }


def printStats(stats):
  print(color('Variance: ', 'cyan'), str(stats['variance']))
  print(color('Mean: ', 'cyan'), str(stats['mean']))
  print(color('Standard deviation: ', 'cyan'), str(stats['stdev']))
  # Generates the 95% interval around the mean of a normal distribution scaled by the standard deviation over the standards.
  # This is the z-score measure from stats means sample
  print(color('Confidence Interval (95%): ', 'cyan'), str(stats['confidence']))


def plotSamples(samples):
    plt.hist(samples)
    pylab.show()