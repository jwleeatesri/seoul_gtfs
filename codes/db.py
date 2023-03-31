import pandas as pd
import sqlite3
import os

from codes import DB_DIR

from datetime import datetime


def start_db():
    conn = sqlite3.connect()
