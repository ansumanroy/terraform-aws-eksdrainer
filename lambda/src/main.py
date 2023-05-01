import json
import pandas as pd

def handle(event, context):
    MyEmptydf = pd.DataFrame({'A' : []})
    return MyEmptydf.to_string()

