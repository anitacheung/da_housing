from email import header


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utils.py

Gets data from api

__author__ = Anita Cheung
__copyright__ = Copyright 2021
__version__ = 1.0
__maintainer__ = Anita Cheung
__status__ = Dev
"""

import pandas as pd
import numpy as np
import datetime as date
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns
import requests

def get():
    response = requests.get("www.attomdata.com/solutions/property-data-api/")
    print(response)

def main():
   get()

if __name__ == '__main__':
    main()