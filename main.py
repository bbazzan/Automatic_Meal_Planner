import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2 import service_account
import config as cfg

creds = service_account.Credentials.from_service_account_file('automatic-meal-planner-345619-c7654b74a820.json', scopes=cfg.SCOPES)


