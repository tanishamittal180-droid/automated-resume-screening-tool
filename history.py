import pandas as pd
import os

FILE = "history/logs.csv"

os.makedirs("history", exist_ok=True)

def save_history(data):

    df = pd.DataFrame([data])

    if os.path.exists(FILE):
        old = pd.read_csv(FILE)
        df = pd.concat([old, df], ignore_index=True)

    df.to_csv(FILE, index=False)

def load_history():

    if os.path.exists(FILE):
        return pd.read_csv(FILE)

    return pd.DataFrame()