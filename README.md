# Speech_Analysis

This package provides an implementation of two different Speech Analysis. 
The first one is to transcribe various Korean, English mixed audio clip, 
and the second one is to catch the time intervals between the beep sound and the answer of the subject throughout the experiment.

## Overview

This repository is based on the [Google Cloud Service] for transcription and [Crepe](https://arxiv.org/abs/1802.06182) for pitch recognition.
The following notebook files `Beep_Recognition.ipynb`, `SpeechRecognitionProject.ipynb` can give the specific examples for each purpose. 
`Beep_Recognition.ipynb` shows how to catch the timelines of beep sound and subject's answers. `SpeechRecognitionProject.ipynb` refers TowardDataScience publication[https://towardsdatascience.com/how-to-use-google-speech-to-text-api-to-transcribe-long-audio-files-1c886f4eb3e9] and gives an example how to transcribe Korean, English mixed audio clip.

The tree structure of this project is given as follows:

``` Unicode
Speech_Analysis
  ├── audio
  │    └── audioclips.wav 
  ├── Transcripts
  │    └── transcript.txt  
  ├── Timelines
  │    └── timeline.csv 
  ├── Beep_Recognition.ipynb
  ├── SpeechRecognitionProject.ipynb
  └── run_glue_benchmark.py: comprehensive prediction file for teacher and student models
```

#### Data description
- audio clips

* Note that: 
    * You can use your own audio clips.
    * Sample audio clips are not provided because of copyright issue.
   
#### Output
* The transcripts will be saved in `Transcripts/{transripts.txt}` after the audio clips are transcribed.
* The timelines will be saved in `Timeline/{timeline.csv}` after the audio clips are analyzed.

## Install

#### Environment 
* Python 3.8
* numpy
* crepe
* scipy
* wave
* resampy
* pydub 
* tensorflow
* google cloud 
* ffmpeg

## How to Run

### Clone the repository

```
git clone https://github.com/bjpark0805/Speech_Analysis.git
cd Speech_Analysis
```

## Contact

- Bumjoon Park (qkrskaqja@snu.ac.kr)
- KiTaek Kim (kitaek@snu.ac.kr)

*This software may be used only for research evaluation purposes.*  
*For other purposes (e.g., commercial), please contact the authors.*
