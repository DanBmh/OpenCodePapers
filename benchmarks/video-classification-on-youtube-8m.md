# video-classification-on-youtube-8m

[Dataset Link](https://research.google.com/youtube8m/) \
Task Hierarchy: ['Video Classification']

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
      "label": "Hit@1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "PERR",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Hit@5",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Global Average Precision",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "mAP",
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
      "p": "[Hierarchical Video Frame Sequence Representation with Deep Convolutional Graph Network](https://arxiv.org/abs/1906.00377v1)",
      "c": "",
      "n": "DCGN (self-attention graph pooling)",
      "d": "2019-06-02",
      "m1": "87.7"
    },
    {
      "p": "[Efficient Video Classification Using Fewer Frames](http://arxiv.org/abs/1902.10640v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shwetabhardwaj44/EfficentVideoClassification_Youtube8M)",
      "n": "Hierarchical LSTM with MoE",
      "d": "2019-02-27",
      "m1": "86.8",
      "m4": "81.1",
      "m5": "41.4"
    },
    {
      "p": "[YouTube-8M: A Large-Scale Video Classification Benchmark](http://arxiv.org/abs/1609.08675v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google/youtube-8m)",
      "n": "Mixture-of-2-Experts",
      "d": "2016-09-27",
      "m1": "70.1",
      "m2": "29.1",
      "m3": "84.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
