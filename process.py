#!-*- coding:utf-8 -*-
import scikits
import scipy.io.wavfile as wav 
from numpy.fft import rfft, irfft
from numpy import argmax, sqrt, mean, diff, log
from matplotlib.mlab import find
from scipy.signal import blackmanharris, fftconvolve
from time import time
import sys

def freq_from_autocorr(sig, fs):
    """Estimate frequency using autocorrelation
    
    """
    # Calculate autocorrelation (same thing as convolution, but with 
    # one input reversed in time), and throw away the negative lags
    corr = fftconvolve(sig, sig[::-1], mode='full')
    corr = corr[len(corr)/2:]
    
    # Find the first low point
    d = diff(corr)
    start = find(d > 0)[0]
    
    # Find the next peak after the low point (other than 0 lag).  This bit is 
    # not reliable for long signals, due to the desired peak occurring between 
    # samples, and other peaks appearing higher.
    # Should use a weighting function to de-emphasize the peaks at longer lags.
    peak = argmax(corr[start:]) + start
    px, py = parabolic(corr, peak)
    
    return fs / px
    
    
def hamming(n):
    """Generate a hamming window of n points as a numpy array."""
    return 0.54 - 0.46 * numpy.cos(2 * numpy.pi / n * (numpy.arange(n) + 0.5))

test_filename = 'elo4ka.wav'

rate,data = wav.read(test_filename)

data = [x[0] for x in data]

NFFT = 2048
noverlap = 512
THRESHOLD_RMS = 0.5

Pxx, freqs, t, image = specgram(data, Fs=rate, detrend = mlab.detrend_mean,noverlap=noverlap,NFFT=NFFT)
Pxx = Pxx.transpose()

print len(Pxx)