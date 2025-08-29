# arrhythmia-detection-on-mit-bih-ar

[Dataset Link](https://physionet.org/content/mitdb/1.0.0/) \
Task Hierarchy: ['Medical waveform analysis', 'Electrocardiography (ECG)', 'Arrhythmia Detection']

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
      "label": "Accuracy (Inter-Patient)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy (Intra-Patient)",
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
      "p": "[Inter- and intra- patient ECG heartbeat classification for arrhythmia detection: a sequence to sequence deep learning approach](http://arxiv.org/abs/1812.07421v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SajadMo/SleepEEGNet)",
      "n": "BiRNN",
      "d": "2018-12-09",
      "m1": "99.53%",
      "m2": "99.92%"
    },
    {
      "p": "[Interpretability Analysis of Heartbeat Classification Based on Heartbeat Activity\u2019s Global Sequence Features and BiLSTM-Attention Neural Network](https://doi.org/10.1109/ACCESS.2019.2933473)",
      "c": "",
      "n": "BiLSTM-Attention",
      "d": "2019-08-07",
      "m1": "99.47%"
    },
    {
      "p": "[Reservoir Computing Models for Patient-Adaptable ECG Monitoring in Wearable Devices](https://arxiv.org/abs/1907.09504v1)",
      "c": "",
      "n": "ESN+Reservoir Computing",
      "d": "2019-07-22",
      "m1": "99.11%"
    },
    {
      "p": "[ECG Heartbeat Classification: A Deep Transferable Representation](http://arxiv.org/abs/1805.00794v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CVxTz/ECG_Heartbeat_Classification)",
      "n": "Deep residual CNN",
      "d": "2018-04-19",
      "m1": "93.4%"
    },
    {
      "p": "[Inter-Patient ECG Heartbeat Classification with Temporal VCG Optimized by PSO](https://doi.org/10.1038/s41598-017-09837-3)",
      "c": "",
      "n": "TVCG_PSO",
      "d": "2017-09-05",
      "m1": "92.4%"
    },
    {
      "p": "[Support vector machine based arrhythmia classification using reduced features](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.463.8764)",
      "c": "",
      "n": "SVM",
      "d": "2005-01-01",
      "m1": "76.3%",
      "m2": "98.7%"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
