"""Test all aspects of input/output within DAFNI

- input environment variables
- input parameter files??
- input files (from datasets)
- output STDOUT/STDERR logs??
- output files (to datasets)

"""
import logging
import os

import pandas

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# read environment variable
env_value = os.getenv('MULTIPLE', 3)
logging.info(f"Read MULTIPLE as {env_value}")

# read file
df = pandas.read_csv('/data/inputs/test.csv')
logging.info(f"Read {len(df)} rows from /data/inputs/test.csv")

# write file
df['value'] *= int(env_value)
df.to_csv('/data/outputs/test.csv', index=False)
logging.info(f"Wrote {len(df)} rows to /data/outputs/test.csv")
