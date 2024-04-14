#! /usr/bin/env python

ID = "train"
print("""\
## Dataset: `TRAIN`

| Ground Truth | Rendered - Original | Rendered - Modified |
|--------------|---------------------|---------------------|""")
for i in range(0, 263, 16):
    print(
        f"| ![](../output/{ID}-original/train/ours_30000/gt/{i:05d}.png) "
        f"| ![](../output/{ID}-original/train/ours_30000/renders/{i:05d}.png) "
        f"| ![](../output/{ID}-modified/train/ours_30000/renders/{i:05d}.png) |"
    )
for i in range(0, 38, 4):
    print(
        f"| ![](../output/{ID}-original/test/ours_30000/gt/{i:05d}.png) "
        f"| ![](../output/{ID}-original/test/ours_30000/renders/{i:05d}.png) "
        f"| ![](../output/{ID}-modified/test/ours_30000/renders/{i:05d}.png) |"
    )
print()

ID = "truck"
print("""\
## Dataset: `TRUCK`

| Ground Truth | Rendered - Original | Rendered - Modified |
|--------------|---------------------|---------------------|""")
for i in range(0, 219, 16):
    print(
        f"| ![](../output/{ID}-original/train/ours_30000/gt/{i:05d}.png) "
        f"| ![](../output/{ID}-original/train/ours_30000/renders/{i:05d}.png) "
        f"| ![](../output/{ID}-modified/train/ours_30000/renders/{i:05d}.png) |"
    )
for i in range(0, 32, 4):
    print(
        f"| ![](../output/{ID}-original/test/ours_30000/gt/{i:05d}.png) "
        f"| ![](../output/{ID}-original/test/ours_30000/renders/{i:05d}.png) "
        f"| ![](../output/{ID}-modified/test/ours_30000/renders/{i:05d}.png) |"
    )
print()
