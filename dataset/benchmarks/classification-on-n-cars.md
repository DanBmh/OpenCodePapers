# classification-on-n-cars

[Dataset Link](https://www.prophesee.ai/2018/03/13/dataset-n-cars/) \
Task Hierarchy: ['Classification']

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
      "label": "Accuracy (%)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Architecture",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Representation",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Representation Time( ms / 100ms events)",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Inference Time",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Params (M)",
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
      "p": "[Masked Event Modeling: Self-Supervised Pretraining for Event Cameras](https://arxiv.org/abs/2212.10368v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tum-vision/mem)",
      "n": "MEM",
      "d": "2022-12-20",
      "m1": "98.55",
      "m2": "Transformer",
      "m3": "Event Histogram"
    },
    {
      "p": "[GET: Group Event Transformer for Event-Based Vision](https://arxiv.org/abs/2310.02642v1)",
      "c": "[&check;&nbsp;Link](https://github.com/peterande/get-group-event-transformer)",
      "n": "GET",
      "d": "2023-10-04",
      "m1": "96.7",
      "m2": "Transformer",
      "m3": "Token",
      "m6": "4.5"
    },
    {
      "p": "[End-to-End Learning of Representations for Asynchronous Event-Based Data](https://arxiv.org/abs/1904.08245v4)",
      "c": "[&check;&nbsp;Link](https://github.com/uzh-rpg/rpg_event_representation_learning)",
      "n": "ResNet34 + EST",
      "d": "2019-04-17",
      "m1": "92.5",
      "m2": "CNN",
      "m3": "EST",
      "m4": "0.38",
      "m5": "6.47",
      "m6": "21.8"
    },
    {
      "p": "[Object Detection with Spiking Neural Networks on Automotive Event Data](https://arxiv.org/abs/2205.04339v1)",
      "c": "[&check;&nbsp;Link](https://github.com/loiccordone/object-detection-with-spiking-neural-networks)",
      "n": "Spiking VGG-11",
      "d": "2022-05-09",
      "m1": "92.4",
      "m2": "SNN",
      "m3": "VoxelCube",
      "m6": "9.23"
    },
    {
      "p": "[Object Detection with Spiking Neural Networks on Automotive Event Data](https://arxiv.org/abs/2205.04339v1)",
      "c": "[&check;&nbsp;Link](https://github.com/loiccordone/object-detection-with-spiking-neural-networks)",
      "n": "Spiking MobileNet-64",
      "d": "2022-05-09",
      "m1": "91.7",
      "m2": "SNN",
      "m3": "VoxelCube",
      "m6": "18.81"
    },
    {
      "p": "[Object Detection with Spiking Neural Networks on Automotive Event Data](https://arxiv.org/abs/2205.04339v1)",
      "c": "[&check;&nbsp;Link](https://github.com/loiccordone/object-detection-with-spiking-neural-networks)",
      "n": "Spiking DenseNet121-24",
      "d": "2022-05-09",
      "m1": "90.4",
      "m2": "SNN",
      "m3": "VoxelCube",
      "m6": "3.93"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
