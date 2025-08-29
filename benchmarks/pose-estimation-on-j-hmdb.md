# pose-estimation-on-j-hmdb

[Dataset Link](http://jhmdb.is.tue.mpg.de/) \
Task Hierarchy: ['1 Image, 2*2 Stitchi', 'Pose Estimation']

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
      "label": "Mean PCK@0.2",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Mean PCK@0.1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Mean PCK@0.05",
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
      "p": "[Kinematic-aware Hierarchical Attention Network for Human Pose Estimation in Videos](https://arxiv.org/abs/2211.15868v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kyungminjin/hanet)",
      "n": "SimpleBaseline + HANet",
      "d": "2022-11-29",
      "m1": "99.6",
      "m2": "98.3",
      "m3": "91.9"
    },
    {
      "p": "[DeciWatch: A Simple Baseline for 10x Efficient 2D and 3D Pose Estimation](https://arxiv.org/abs/2203.08713v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cure-lab/DeciWatch)",
      "n": "DeciWatch",
      "d": "2022-03-16",
      "m1": "99.0",
      "m2": "94.6",
      "m3": "80.6"
    },
    {
      "p": "[LSTM Pose Machines](http://arxiv.org/abs/1712.06316v4)",
      "c": "[&check;&nbsp;Link](https://github.com/lawy623/LSTM_Pose_Machines)",
      "n": "LSTM PM",
      "d": "2017-12-18",
      "m1": "93.6"
    },
    {
      "p": "[Convolutional Pose Machines](http://arxiv.org/abs/1602.00134v4)",
      "c": "[&check;&nbsp;Link](https://github.com/CMU-Perceptual-Computing-Lab/openpose)",
      "n": "CPM",
      "d": "2016-01-30",
      "m1": "91.9"
    },
    {
      "p": "[Do Different Tracking Tasks Require Different Appearance Models?](https://arxiv.org/abs/2107.02156v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Zhongdao/UniTrack)",
      "n": "UniTrack_i18",
      "d": "2021-07-05",
      "m1": "80.5",
      "m2": "58.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
