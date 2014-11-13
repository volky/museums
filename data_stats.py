import pandas as pd
import numpy as np
%matplotlib inline

import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', 200)

fname = 'moma_insta_data_clean.csv'

df = pd.read_csv(fname, sep='\t', 
                 names=['picture_id', 'uid', 'lat', 'long', 'filter_used', 'caption', 'comment_count', 
                        'favorite_count', 'link', 'created_time', 'media_type', 'all_hashtags_in_string'])

df['created_time'] = pd.to_datetime(df['created_time'], unit='s', utc=True)
df = df.set_index('created_time')
df = df.sort()
df = df.tz_localize('UTC')
df = df.tz_convert('US/Eastern')

print len(df)
