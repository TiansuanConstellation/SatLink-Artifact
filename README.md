## Introduction of LEO Satellite-Terrestrial Data Links tools and dataset
This dataset supports the submission to SIGCOMM2024 for the poster "POSTER: An End-to-End Study on Performance and Reliability of LEO Satellite-Terrestrial Data Links," which is currently under review. With the anticipated surge in future spacecraft launches, the demand for data transmission will intensify, making efficient and reliable downlinks crucial for various Low Earth Orbit (LEO) satellite applications. 
This poster measures and explores the urgent issues in data transmission currently faced by remote sensing satellites, providing valuable insights for improving data transmission strategies for LEO satellites. The dataset from this paper is derived from link measurements between the BUPT-1 satellite and an actual ground station.

#### Dataset Structure 
The data is categorized into two types: **physical layer data**, which is collected by the ground station's antenna and baseband, and **application layer data**, which consists of data from the TCP flow connection between the ground server and the ground baseband.
The repository is organized around the key metrics types mentioned in the paper to facilitate easy navigation and understanding of different sections. For each figure, we have created separate folders. Inside each folder, there is a README file that provides instructions specific to validating the experimental items related to that figure.

#### Getting Started

##### Environment Setup

Before you begin, you can set up the required Python environment with the following commands:

```shell
# Makesure $PWD is the root directory of the repo
# Create a Conda environment with Python 3.7.4 dependencies
conda env create -n artifact python=3.7.4
conda activate artifact
# Install additional Python dependencies
pip install -r requirements.txt
```

##### Cloning Our Repository

To clone the repository, use:

```shell
git clone https://github.com/TiansuanConstellation/SatLink-Artifact.git
cd SatLink-Artifact 
```

##### Generating Figures

To generate all figures, run:

```shell
bash build_all.sh
```


---

#### Paper Structure to Folder Structure

|   Content in Paper    |                       Folder in Repo.                        | Description                                                  |
| :-------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| Figures 2 (Section 2) |          [SNR-AGC-Measurement](SNR-AGC-Measurement)          | Measurements and analysis of baseband decoded signal-to-noise ratio (Eb/N0) and antenna gain (AGC). |
| Figures3 (Section 2)  |     [Satellite-TCP-Throughput](Satellite-TCP-Throughput)     | Performance of satellite downlink TCP throughput             |
| Figures 4 (Section 2) | [Frame-Error-Time-Distribution](Frame-Error-Time-Distribution) | Analysis of time distribution of frame errors and miscode rates during data transmission. |

---

#### Support

As always, if there are any questions, feel free to reach out to us ([zhuzuo@bupt.edu.cn](mailto:zhuzuo@bupt.edu.cn),[xrl@bupt.edu.cn](mailto:xrl@bupt.edu.cn))!
