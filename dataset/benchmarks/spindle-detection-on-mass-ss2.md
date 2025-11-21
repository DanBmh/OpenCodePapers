# spindle-detection-on-mass-ss2

[Dataset Link](http://ceams-carsm.ca/mass/) \
Task Hierarchy: ['Sleep Quality', 'Spindle Detection']

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
      "label": "F1-score (@IoU = 0.3)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "F1-score (@IoU = 0.2)",
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
      "p": "[RED: Deep Recurrent Neural Networks for Sleep EEG Event Detection](https://arxiv.org/abs/2005.07795v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nicolasigor/cmorlet-tensorflow)",
      "n": "RED-Time",
      "d": "2020-05-15",
      "m1": "0.812"
    },
    {
      "p": "[RED: Deep Recurrent Neural Networks for Sleep EEG Event Detection](https://arxiv.org/abs/2005.07795v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nicolasigor/cmorlet-tensorflow)",
      "n": "RED-CWT",
      "d": "2020-05-15",
      "m1": "0.809",
      "m2": "0.812"
    },
    {
      "p": "[DOSED: a deep learning approach to detect multiple sleep micro-events in EEG signal](http://arxiv.org/abs/1812.04079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Dreem-Organization/dosed)",
      "n": "DOSED",
      "d": "2018-12-07",
      "m1": "0.75"
    },
    {
      "p": "[Multichannel sleep spindle detection using sparse low-rank optimization](https://doi.org/10.1016/j.jneumeth.2017.06.004)",
      "c": "[&check;&nbsp;Link](https://github.com/aparek/mcsleep)",
      "n": "Multichannel Low-Rank",
      "d": "2017-08-15",
      "m1": "0.50"
    },
    {
      "p": "[Meet Spinky: An Open-Source Spindle and K-Complex Detection Toolbox Validated on the Open-Access Montreal Archive of Sleep Studies (MASS).](https://doi.org/10.3389/fninf.2017.00015)",
      "c": "[&check;&nbsp;Link](https://github.com/TarekLaj/SPINKY)",
      "n": "Spinky",
      "d": "2017-03-02",
      "m1": "0.46"
    },
    {
      "p": "[A single channel sleep-spindle detector based on multivariate classification of EEG epochs: MUSSDET.](https://doi.org/10.1016/j.jneumeth.2017.12.023)",
      "c": "",
      "n": "MUSSDET",
      "d": "2018-03-01",
      "m1": "0.39"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
