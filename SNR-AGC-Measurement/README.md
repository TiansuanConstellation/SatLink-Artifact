# Signal-to-Noise Ratio (Eb/N0) and Antenna Gain (AGC)

This folder contains details of the artifacts related to Section 2 (in T1、T2、T3, SNR and AGC). We provide details of the dataset, analysis scripts, and plotting scripts to generate Figure 2.

## Folder structure

| Foldername/Filename       | Description                      |
| ------------------------- | -------------------------------- |
| plots-section3-figure2.py | Scripts for generating figure 2. |

------

## Dataset Description

The dataset file `HSB_ + exp +.csv` contains serveral fields. We provide description for each field below.

| Field name          | Description of the field                 |
| ------------------- | ---------------------------------------- |
| `Time`              | Timestamp (e.g. 2024-03-26 23:18:11.439) |
| `Eb/No (Decode dB)` | Signal-to-Noise Ratio（dB）               |                    |

The dataset file `ACU_TY28_ + exp +.mae` contains serveral fields. We provide description for each field below.

| Field name              | Description of the field      |
| ----------------------- | ----------------------------- |
| `Date`                  | Date (e.g. 2024-03-29)        |
| `Time`                  | Timestamp (e.g. 22:39:07.000) |
| `Data Transmission AGC` | Antenna Gain Control (dB)     |


## Requirements

- Python (>=3.7.4)
- Numpy (>=1.19.5)
- Matplotlib (>=3.3.4)
- Pandas(>=1.1.5)

------

## Generating Plots

Use the following bash command to generate results/plots

```bash
python3 plots-section3-figure2.py longest
```

The generated results will be saved in the current folder.