#! /usr/bin/python3

"""
Generate reports after running these commands:

```python
python train.py -s $INPUT_NAME -m $OUTPUT_NAME --eval && \
python render.py -m $OUTPUT_NAME && \
python metrics.py -m $OUTPUT_NAME
```
"""

from datetime import timedelta
from json import load as load_json
from pathlib import Path
from sys import stderr, stdout
from typing import TextIO

# Constants
PROJECT_PATH = (Path(__file__) / "../..").resolve()
REPORT_DIR_PATHS = sorted(PROJECT_PATH.glob("output/*/"))
OUTPUT_STREAM: TextIO = stdout

# Parameters
REPORT_NAME_METRICS = "results.json"
REPORT_NAME_PERFORMANCE = "perf_report.json"

# [Loop] Collect reports
reports: dict[str, dict[str]] = {}

for report_dir_path in REPORT_DIR_PATHS:
    report_id = report_dir_path.name

    # Read files with parameters
    report_metrics_path = report_dir_path / REPORT_NAME_METRICS
    report_performance_path = report_dir_path / REPORT_NAME_PERFORMANCE
    try:
        with report_metrics_path.open("r") as report_metrics_file:
            report_metrics: dict = load_json(report_metrics_file)
        with report_performance_path.open("r") as report_performance_file:
            report_performance: dict = load_json(report_performance_file)
    except FileNotFoundError:
        continue

    # Transform schema
    report_metrics = report_metrics.get("ours_30000")
    if not report_metrics:
        continue
    report_metrics["METRIC_LPIPS"] = f"{report_metrics.pop('LPIPS'):.4f}"
    report_metrics["METRIC_PSNR"] = f"{report_metrics.pop('PSNR'):.4f}"
    report_metrics["METRIC_SSIM"] = f"{report_metrics.pop('SSIM'):.4f}"

    report_performance["TRAIN_TIME"] = str(
        timedelta(seconds=report_performance.pop("train_duration_sec"))
    )
    report_performance["TRAIN_VRAM"] = (
        f"{report_performance.pop('train_vram_avg_mb')} MiB "
        "("
        f"{report_performance.pop('train_vram_p05_mb')} ~ "
        f"{report_performance.pop('train_vram_p95_mb')}"
        ")"
    )
    report_performance["MODEL_SIZE"] = (
        f"{report_performance.pop('train_model_size_i30000_mb')} MiB"
    )
    report_performance.pop("train_model_size_i7000_mb")

    # Update records
    report_recombined = dict(
        sorted(
            {
                **report_metrics,
                **report_performance,
            }.items()
        )
    )
    report_id = report_dir_path.name

    reports[report_id] = report_recombined

# Format reports into GitHub-flavored Markdown table
reports_repr_gfm_table = ""

reports_repr_gfm_table += "| MODEL_ID |"
for report_attrkey in next(iter(reports.values())).keys():
    reports_repr_gfm_table += f" {report_attrkey} |"
reports_repr_gfm_table += "\n"

reports_repr_gfm_table += f"| {'-' * len('MODEL_ID')} |"
for report_attrkey in next(iter(reports.values())).keys():
    reports_repr_gfm_table += f" {'-' * len(report_attrkey)} |"
reports_repr_gfm_table += "\n"

for id, report in reports.items():
    reports_repr_gfm_table += f"| {id} |"
    for report_attrval in report.values():
        reports_repr_gfm_table += f" {report_attrval} |"
    reports_repr_gfm_table += "\n"

# Print the report
print(reports_repr_gfm_table, end="", file=OUTPUT_STREAM)
