print("SCGA runner started")

from scga.file_reader import read_python_files

from scga.metrics.cic import calculate_cic
from scga.metrics.nhc import calculate_nhc
from scga.metrics.dlw import calculate_dlw
from scga.metrics.fcl import calculate_fcl
from scga.metrics.rsi import calculate_rsi
from scga.metrics.coi import calculate_coi

from scga.scorer import calculate_gcs


def run_scga(target_folder):
    code = read_python_files(target_folder)

    metrics = {
        "CIC": calculate_cic(code),
        "NHC": calculate_nhc(code),
        "DLW": calculate_dlw(code),
        "FCL": calculate_fcl(code),
        "RSI": calculate_rsi(code),
        "COI": calculate_coi(code)
    }

    gcs, normalized = calculate_gcs(metrics)
    return metrics, normalized, gcs


if __name__ == "__main__":
    print("Running SCGA on baseline_app")
    base_metrics, _, base_gcs = run_scga("baseline_app")

    print("Running SCGA on greenstream_app")
    green_metrics, _, green_gcs = run_scga("greenstream_app")

    print("\n=== BASELINE RESULTS ===")
    print(base_metrics)
    print("GCS:", round(base_gcs,2))

    print("\n=== GREENSTREAM RESULTS ===")
    print(green_metrics)
    print("GCS:", round(green_gcs,2))

    THRESHOLD = 80

    print("\n=== SUSTAINABILITY GATE ===")
    if green_gcs >= THRESHOLD:
        print("GreenStream compliance PASSED")
    else:
        print("GreenStream compliance FAILED")
        exit(1)

