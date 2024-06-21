# TCP Connection Performance

This folder contains details of the artifacts related to Section 2 (in **T1**、**T2**, Throughput). We provide details of the dataset, analysis scripts, and plotting scripts to generate Figure 3.

## Folder structure
| Foldername/Filename       | Description                      |
| ------------------------- | -------------------------------- |
| plots-section3-figure3.py | Scripts for generating figure 3. |

---

## Dataset Description

The dataset file `logfile_[TcpOriLenData]_ + exp + .txt` contains serveral fields. We provide description for each field below.

| Field name | Description of the field                               |
| ---------- | ------------------------------------------------------ |
| `Time`     | Timestamp (e.g. 2024-03-24 23:21:04.490)               |
| `data_len` | The amount of data received at each timestamp（bytes） |



## Requirements

* Python (>=3.7.4)
* Numpy (>=1.19.5)
* Matplotlib (>=3.3.4)
* Pandas(>=1.1.5)

---

## Generating Plots

Use the following bash command to generate results/plots

```bash
python3 plots-section3-figure3.py
```
The generated results will be saved in the current folder.