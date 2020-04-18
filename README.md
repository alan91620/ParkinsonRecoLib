# ParkinsonRecoLib

Machine learning library to load a trained model and make predictions on user's WAV file to know if he got parkinson
Project also include jupyter notebook to build dataset, train and export model.

Our project use classification through Linear Regression

We built our dataset by measuring localJjitter ; absoluteJitter ; RAPJitter ; JitterPPQ ; localShimmer ; localShimmer dB ; Shimmer APQ3 ; Shimmer APQ5 ; Shimmer APQ11 ; hnr05 ; hnr15 ; hnr25 on many WAV audio file of healthy and parkinson patients. https://zenodo.org/record/2867216#.XpuGXsgzaUl

Measure was taken with parselmouth which is a python module for audio measuring. https://parselmouth.readthedocs.io/en/stable/

Once dataset created and model trained we used a cross validation test wich gave us ~0,7% of accuracy

## Installation

For the full project refeer to https://github.com/Milkad0/ParkinsonIA

## Usage example

/src/lib/libImpl.py is an example of lib usage

## Development setup

```sh
pip install joblib praat-parselmouth pandas numpy sklearn
```

## Meta

Alan MARTHINEAU - Vincent ETHEVE - Augustin LOLLIVIER
