# Received, Error, and Lost Frames

This folder contains details of the artifacts related to Section 2 (in **T3**, BER). We provide details of the dataset, analysis scripts, and plotting scripts to generate Figure 4.

It is important to note that these data pertain to the side lobe  tracked by **T3** , which differs significantly in error patterns from **T1** and **T2**. If necessary, you can refer to `exp`:2024-03-26-23_12_39(**T1**) and 2024-03-24-22_31_21(**T2**) to compare the error situations of **T1** and **T2**.

## Folder structure
| Foldername/Filename       | Description                      |
| ------------------------- | -------------------------------- |
| plots-section3-figure4.py | Scripts for generating figure 4. |

---

## Dataset Description

The dataset file `HSB_2024-03-29-22_32_10.csv` contains serveral fields. We provide description for each field below.

| Field name        | Description of the field                 |
| ----------------- | ---------------------------------------- |
| `Time`            | Timestamp (e.g. 2024-03-26 23:18:11.439) |
| `Received Frames` | Cumulative number of received frames     |
| `Error Frames`    | Cumulative number of error frames        |
| `Loss Frames`     | Cumulative number of lost frames         |


## Requirements

* Python (>=3.7.4)
* Numpy (>=1.19.5)
* Matplotlib (>=3.3.4)
* Pandas(>=1.1.5)

---

## Generating Plots

Use the following bash command to generate results/plots

```bash
python3 plots-section3-figure4.py longest
```
The generated results will be saved in the current folder.