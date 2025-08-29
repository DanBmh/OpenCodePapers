# sleep-arousal-detection-on-mesa

[Dataset Link](https://sleepdata.org/datasets/mesa) \
Task Hierarchy: ['Sleep Quality', 'Sleep Arousal Detection']

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
      "label": "event-based F1 score",
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
      "p": "[DOSED: a deep learning approach to detect multiple sleep micro-events in EEG signal](http://arxiv.org/abs/1812.04079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Dreem-Organization/dosed)",
      "n": "DOSED (3 EEG + 2 EOG)",
      "d": "2018-12-07",
      "m1": "0.71"
    },
    {
      "p": "[DOSED: a deep learning approach to detect multiple sleep micro-events in EEG signal](http://arxiv.org/abs/1812.04079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Dreem-Organization/dosed)",
      "n": "DOSED (1 EEG)",
      "d": "2018-12-07",
      "m1": "0.61"
    },
    {
      "p": "[State-of-the-art sleep arousal detection evaluated on a comprehensive clinical dataset](https://www.nature.com/articles/s41598-024-67022-9)",
      "c": "[&check;&nbsp;Link](https://gitlab.com/sleep-is-all-you-need/arousaldetector)",
      "n": "U-Net",
      "d": "2024-07-14",
      "m2": "0.81"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
