
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import os

inputfile_dir='./inputfile'
outputfile='all2.csv'
for inputfile in os.listdir(inputfile_dir):
    inputfile1=os.path.join("./inputfile",inputfile)
    df = pd.read_csv(inputfile1)
    df.to_csv(outputfile,index=False, header=False, mode='a+')
