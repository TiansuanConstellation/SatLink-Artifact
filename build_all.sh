#!/usr/bin/bash

echo "Running tests under Frame-Error-Time-Distribution"
cd Frame-Error-Time-Distribution
python3 plots-section3-figure4.py

echo "Running tests under Satellite-TCP-Throughput"
cd ../Satellite-TCP-Throughput
python3 plots-section3-figure3.py

echo "Running tests under SNR-AGC-Measurement"
cd ../SNR-AGC-Measurement
python3 plots-section3-figure2.py

echo "All tests completed."
