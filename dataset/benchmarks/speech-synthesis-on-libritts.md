# speech-synthesis-on-libritts

[Dataset Link](http://www.openslr.org/60) \
Task Hierarchy: ['Accented Speech Recognition', 'Speech Synthesis']

<br>

```json:table
{
  "fields": [
    {
      "key": "p",
      "label": "Paper"
    },
    {
      "key": "c",
      "label": "Code"
    },
    {
      "key": "m1",
      "label": "PESQ",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "M-STFT",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "MCD",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Periodicity",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "V/UV F1",
      "sortable": "true"
    },
    {
      "key": "n",
      "label": "ModelName"
    },
    {
      "key": "d",
      "label": "ReleaseDate",
      "sortable": "true"
    }
  ],
  "items": [
    {
      "p": "[Accelerating High-Fidelity Waveform Generation via Adversarial Flow Matching Optimization](https://arxiv.org/abs/2408.08019v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sh-lee-prml/periodwave)",
      "n": "PeriodWave-Turbo-L",
      "d": "2024-08-15",
      "m1": "4.454",
      "m2": "0.7358",
      "m4": "0.0528",
      "m5": "0.9756"
    },
    {
      "p": "[BigVGAN: A Universal Neural Vocoder with Large-Scale Training](https://arxiv.org/abs/2206.04658v2)",
      "c": "[&check;&nbsp;Link](https://github.com/IAHispano/Applio/tree/exp/vocoders/rvc/lib/algorithm)",
      "n": "BigVGAN-v2",
      "d": "2022-06-09",
      "m1": "4.362",
      "m2": "0.7026",
      "m3": "0.2903",
      "m4": "0.0593",
      "m5": "0.9793"
    },
    {
      "p": "[EVA-GAN: Enhanced Various Audio Generation via Scalable Generative Adversarial Networks](https://arxiv.org/abs/2402.00892v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fishaudio/vocoder)",
      "n": "EVA-GAN-big",
      "d": "2024-01-31",
      "m1": "4.3536",
      "m2": "0.7982",
      "m4": "0.0751",
      "m5": "0.9745"
    },
    {
      "p": "[PeriodWave: Multi-Period Flow Matching for High-Fidelity Waveform Generation](https://arxiv.org/abs/2408.07547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sh-lee-prml/periodwave)",
      "n": "PeriodWave + FreeU",
      "d": "2024-08-14",
      "m1": "4.248",
      "m2": "1.0269",
      "m4": "0.0765",
      "m5": "0.9651"
    },
    {
      "p": "[RFWave: Multi-band Rectified Flow for Audio Waveform Reconstruction](https://arxiv.org/abs/2403.05010v3)",
      "c": "[&check;&nbsp;Link](https://github.com/bfs18/rfwave)",
      "n": "RFWave",
      "d": "2024-03-08",
      "m1": "4.228",
      "m4": "0.090",
      "m5": "0.968"
    },
    {
      "p": "[BigVSAN: Enhancing GAN-based Neural Vocoders with Slicing Adversarial Network](https://arxiv.org/abs/2309.02836v2)",
      "c": "[&check;&nbsp;Link](https://github.com/IAHispano/Applio/tree/exp/vocoders/rvc/lib/algorithm)",
      "n": "BigVSAN (w/ snakebeta)",
      "d": "2023-09-06",
      "m1": "4.120",
      "m2": "0.7992",
      "m3": "0.4129",
      "m4": "0.0924",
      "m5": "0.9644"
    },
    {
      "p": "[BigVSAN: Enhancing GAN-based Neural Vocoders with Slicing Adversarial Network](https://arxiv.org/abs/2309.02836v2)",
      "c": "[&check;&nbsp;Link](https://github.com/IAHispano/Applio/tree/exp/vocoders/rvc/lib/algorithm)",
      "n": "BigVSAN",
      "d": "2023-09-06",
      "m1": "4.116",
      "m2": "0.7881",
      "m3": "0.3381",
      "m4": "0.0935",
      "m5": "0.9635"
    },
    {
      "p": "[EVA-GAN: Enhanced Various Audio Generation via Scalable Generative Adversarial Networks](https://arxiv.org/abs/2402.00892v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fishaudio/vocoder)",
      "n": "EVA-GAN-base",
      "d": "2024-01-31",
      "m1": "4.0330",
      "m2": "0.9485",
      "m4": "0.0942",
      "m5": "0.9658"
    },
    {
      "p": "[BigVGAN: A Universal Neural Vocoder with Large-Scale Training](https://arxiv.org/abs/2206.04658v2)",
      "c": "[&check;&nbsp;Link](https://github.com/IAHispano/Applio/tree/exp/vocoders/rvc/lib/algorithm)",
      "n": "BigVGAN",
      "d": "2022-06-09",
      "m1": "4.027",
      "m2": "0.7997",
      "m3": "0.3745",
      "m4": "0.1018",
      "m5": "0.9598"
    },
    {
      "p": "[Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis](https://arxiv.org/abs/2306.00814v3)",
      "c": "[&check;&nbsp;Link](https://github.com/collabora/whisperspeech)",
      "n": "Vocos",
      "d": "2023-06-01",
      "m1": "3.70",
      "m4": "0.101",
      "m5": "0.9582"
    },
    {
      "p": "[BigVGAN: A Universal Neural Vocoder with Large-Scale Training](https://arxiv.org/abs/2206.04658v2)",
      "c": "[&check;&nbsp;Link](https://github.com/IAHispano/Applio/tree/exp/vocoders/rvc/lib/algorithm)",
      "n": "BigVGAN-base",
      "d": "2022-06-09",
      "m1": "3.519",
      "m2": "0.8788",
      "m3": "0.4564",
      "m4": "0.1287",
      "m5": "0.9459"
    },
    {
      "p": "[WaveGlow: A Flow-based Generative Network for Speech Synthesis](http://arxiv.org/abs/1811.00002v1)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/waveglow)",
      "n": "WaveGlow",
      "d": "2018-10-31",
      "m1": "3.138",
      "m2": "1.3099",
      "m3": "2.3591",
      "m4": "0.1485",
      "m5": "0.9378"
    },
    {
      "p": "[WaveFlow: A Compact Flow-based Model for Raw Audio](https://arxiv.org/abs/1912.01219v4)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/Parakeet)",
      "n": "WaveFlow",
      "d": "2019-12-03",
      "m1": "3.027",
      "m2": "1.1120",
      "m3": "1.2455",
      "m4": "0.1416",
      "m5": "0.9410"
    },
    {
      "p": "[HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis](https://arxiv.org/abs/2010.05646v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/DeepLearningExamples)",
      "n": "HiFi-GAN",
      "d": "2020-10-12",
      "m1": "2.947",
      "m2": "1.0017",
      "m3": "0.6603",
      "m4": " 0.1565",
      "m5": "0.9300"
    },
    {
      "p": "[Speaker Conditional WaveRNN: Towards Universal Neural Vocoder for Unseen Speaker and Recording Conditions](https://arxiv.org/abs/2008.05289v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dipjyoti92/SC-WaveRNN)",
      "n": "SC-WaveRNN",
      "d": "2020-08-09",
      "m1": "1.701",
      "m2": "2.2358",
      "m3": "1.8854",
      "m4": "0.3044",
      "m5": "0.8144"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
