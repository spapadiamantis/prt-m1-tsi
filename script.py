"""This is a script that contains the filter"""
import sys
from scipy.io import wavfile
from scipy import signal
import numpy as np


if __name__ == "__main__":
    
    # Read wave file
    samplerate,signal =  wavfile.read(sys.argv[0], mmap=False)
    