import matplotlib.pyplot as plt

baseline_gcs = None
greenstream_gcs = None

# Read SCGA results (same folder)
with open("scga_results.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if "=== BASELINE RESULTS ===" in line:
        for j in range(i, i + 5):
            if j < len(lines) and "GCS:" in lines[j]:
                baseline_gcs = float(lines[j].split(":")[1].strip())

    if "=== GREENSTREAM RESULTS ===" in line:
        for j in range(i, i + 5):
            if j < len(lines) and "GCS:" in lines[j]:
                greenstream_gcs = float(lines[j].split(":")[1].strip())

if baseline_gcs is None or greenstream_gcs is None:
    raise ValueError("GCS values not found in scga_results.txt")

# Calculate improvement %
improvement = ((greenstream_gcs - baseline_gcs) / baseline_gcs) * 100

applications = ['Baseline', 'GreenStream']
gcs_scores = [baseline_gcs, greenstream_gcs]

plt.figure(figsize=(7, 4.5))

bars = plt.bar(
    applications,
    gcs_scores,
    color=['#c7e9c0', '#41ab5d'],  # light → dark green
    edgecolor='black',
    linewidth=1.2
)

plt.xlabel('Application Version', fontsize=11)
plt.ylabel('Green Code Score (GCS)', fontsize=11)
plt.title('Green Code Score Comparison', fontsize=13, fontweight='bold')

plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Annotate bar values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.1f}",
        ha='center',
        fontsize=10,
        fontweight='bold'
    )

# Annotate improvement
plt.text(
    0.5,
    max(gcs_scores) + 6,
    f"↑ {improvement:.2f}% improvement",
    ha='center',
    fontsize=11,
    fontweight='bold',
    color='#006d2c'
)

plt.tight_layout()
plt.savefig("gcs_comparison.png", dpi=300)
plt.show()
