from scga.thresholds import MAX_VALUES, normalize_negative, normalize_positive

WEIGHTS = {
    "CIC": 0.25,
    "NHC": 0.15,
    "DLW": 0.15,
    "FCL": 0.15,
    "RSI": 0.15,
    "COI": 0.15
}

def calculate_gcs(metrics):
    scores = {
        "CIC": normalize_negative(metrics["CIC"], MAX_VALUES["CIC"]),
        "NHC": normalize_negative(metrics["NHC"], MAX_VALUES["NHC"]),
        "DLW": normalize_negative(metrics["DLW"], MAX_VALUES["DLW"]),
        "FCL": normalize_negative(metrics["FCL"], MAX_VALUES["FCL"]),
        "RSI": normalize_negative(metrics["RSI"], MAX_VALUES["RSI"]),
        "COI": normalize_positive(metrics["COI"], MAX_VALUES["COI"]),
    }

    gcs = sum(WEIGHTS[k] * scores[k] for k in scores)
    return round(gcs * 100, 2), scores
