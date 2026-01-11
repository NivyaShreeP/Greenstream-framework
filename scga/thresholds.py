MAX_VALUES = {
    "CIC": 500,
    "NHC": 5,
    "DLW": 5,
    "FCL": 20,
    "RSI": 10,
    "COI": 10
}

def normalize_negative(actual, max_value):
    score = 1 - (actual / max_value)
    return max(0, min(score, 1))

def normalize_positive(actual, max_value):
    score = actual / max_value
    return max(0, min(score, 1))
