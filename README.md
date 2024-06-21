## Introduction of LEO Satellite-Terrestrial Data Links tools and dataset
This dataset supports the submission to SIGCOMM2024 for the poster "[POSTER: An End-to-End Study on Performance and Reliability of LEO Satellite-Terrestrial Data Links](https://doi.org/10.1145/3672202.3673755)." With the anticipated surge in future spacecraft launches, the demand for data transmission will intensify, making efficient and reliable downlinks crucial for various Low Earth Orbit (LEO) satellite applications. 

This poster measures and explores the urgent issues in data transmission currently faced by remote sensing satellites, providing valuable insights for improving data transmission strategies for LEO satellites. The dataset from this paper is derived from link measurements between the [BUPT-1](http://www.tiansuan.org.cn/sate-b1.html) satellite, which is part of the [TianSuan Constellation](http://www.tiansuan.org.cn/index.html) project and uses X-Band for downlink data transmission, and a ground station located in Tongchuan, Shaanxi. 

The typical communication window between the satellite and the ground station lasts only about 500 seconds. Each time the satellite passes the ground station, the communication link is established. During this period, the Pi-4B continuously sends 1060-byte packets as the UDP payload. The ground station demodulates the signal upon reception and forwards the decoded result to the server. This process is repeated, continuously recording key metrics, including information about the radio link and payload data.


#### Dataset Structure 
The data is categorized into two types: **physical layer data**, which is collected by the ground station's antenna and baseband, and **application layer data**, which consists of  real application data from the **TCP** flow connection between the ground server and the ground baseband.
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

As always, if there are any questions, feel free to reach out to us ([zhuzuo@bupt.edu.cn](mailto:zhuzuo@bupt.edu.cn), [xrl@bupt.edu.cn](mailto:xrl@bupt.edu.cn))!
