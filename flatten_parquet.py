import numpy as numpy
import pandas as pd
import pyarrow.parquet as pq
import os
import re
import glob


yellow_taxi_path = r'C:\Users\PC\Documents\Data Engineering Projects\NYC Taxi Trip Data\Yellow'
yellow_taxi_files = glob.glob(f'{yellow_taxi_path}\*\*.parquet')

for i in yellow_taxi_files:
    trips = pq.read_table(i)
    trips = trips.to_pandas()
    
