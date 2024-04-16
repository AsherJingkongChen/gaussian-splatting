#! /usr/bin/env python

from pathlib import Path

PROJECT_ROOT = (Path(__file__) / "../../").resolve()

def print_section(id: str) -> None:
    print(f"""\
## Dataset: `{id.upper()}`

| Ground Truth | Rendered - Original | Rendered - Modified |
|--------------|---------------------|---------------------|\
""")
    for part in ("train", "test"):
        for img_id, _ in enumerate(PROJECT_ROOT.glob(f"output/{id}-original/{part}/ours_30000/gt/*.png")):
            if img_id % 20 != 0:
                continue
            print(
                f"| ![](../output/{id}-original/{part}/ours_30000/gt/{img_id:05d}.png) "
                f"| ![](../output/{id}-original/{part}/ours_30000/renders/{img_id:05d}.png) "
                f"| ![](../output/{id}-modified/{part}/ours_30000/renders/{img_id:05d}.png) |"
            )
    print()

for input_dir in sorted(PROJECT_ROOT.glob("input/*")):
    id = input_dir.name
    print_section(id)
