# cell-segmentation-on-fluo-n2dl-hela

[Dataset Link](http://celltrackingchallenge.net/2d-datasets/) \
Task Hierarchy: ['Medical Image Segmentation', 'Cell Segmentation']

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
      "label": "SEG (~Mean IoU)",
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
      "p": "[Cell Segmentation and Tracking using CNN-Based Distance Predictions and a Graph-Based Matching Strategy](https://arxiv.org/abs/2004.01486v4)",
      "c": "[&check;&nbsp;Link](https://bitbucket.org/t_scherr/cell-segmentation-and-tracking)",
      "n": "Dual U-Net (Neighbor distances)",
      "d": "2020-04-03",
      "m1": "0.895"
    },
    {
      "p": "[Microscopy Cell Segmentation via Convolutional LSTM Networks](http://arxiv.org/abs/1805.11247v2)",
      "c": "[&check;&nbsp;Link](https://github.com/arbellea/LSTM-UNet)",
      "n": "DecLSTM",
      "d": "2018-05-29",
      "m1": "0.839"
    },
    {
      "p": "[Microscopy Cell Segmentation via Convolutional LSTM Networks](http://arxiv.org/abs/1805.11247v2)",
      "c": "[&check;&nbsp;Link](https://github.com/arbellea/LSTM-UNet)",
      "n": "EncLSTM",
      "d": "2018-05-29",
      "m1": "0.811"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
