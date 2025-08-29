# pose-estimation-on-crowdpose

[Dataset Link](https://github.com/Jeff-sjtu/CrowdPose) \
Task Hierarchy: ['Pose Estimation']

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
      "label": "AP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "AP50",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "AP75",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "APM",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Test",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "AP Hard",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "AP Easy",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "AP Medium",
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
      "p": "[Rethinking pose estimation in crowds: overcoming the detection information-bottleneck and ambiguity](https://arxiv.org/abs/2306.07879v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amathislab/BUCTD)",
      "n": "BUCTD-W48 (w/cond. input from PETR, and generative sampling)",
      "d": "2023-06-13",
      "m1": "78.5",
      "m6": "72.3",
      "m7": "83.9",
      "m8": "79.0"
    },
    {
      "p": "[ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation](https://arxiv.org/abs/2204.12484v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ViTPose-G",
      "d": "2022-04-26",
      "m1": "78.3",
      "m2": "85.3",
      "m3": "81.4",
      "m4": "86.6",
      "m6": "67.9"
    },
    {
      "p": "[Rethinking pose estimation in crowds: overcoming the detection information-bottleneck and ambiguity](https://arxiv.org/abs/2306.07879v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amathislab/BUCTD)",
      "n": "BUCTD-W48 (w/cond. input from PETR)",
      "d": "2023-06-13",
      "m1": "76.7"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-L 1K-MIM",
      "d": "2022-05-26",
      "m1": "75.5"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-B 1K-MIM",
      "d": "2022-05-26",
      "m1": "74.9"
    },
    {
      "p": "[Rethinking pose estimation in crowds: overcoming the detection information-bottleneck and ambiguity](https://arxiv.org/abs/2306.07879v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amathislab/BUCTD)",
      "n": "BUCTD-W48",
      "d": "2023-06-13",
      "m1": "72.9"
    },
    {
      "p": "[OpenPifPaf: Composite Fields for Semantic Keypoint Detection and Spatio-Temporal Association](https://arxiv.org/abs/2103.02440v2)",
      "c": "[&check;&nbsp;Link](https://github.com/openpifpaf/openpifpaf)",
      "n": "OpenPifPaf",
      "d": "2021-03-03",
      "m1": "70.5",
      "m2": "89.1",
      "m3": "76.1",
      "m6": "63.8",
      "m7": "78.4",
      "m8": "72.1"
    },
    {
      "p": "[Multi-Instance Pose Networks: Rethinking Top-Down Pose Estimation](https://arxiv.org/abs/2101.11223v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rawalkhirodkar/MIPNet)",
      "n": "MIPNet (HRNet-W48)",
      "d": "2021-01-27",
      "m1": "70.0",
      "m4": "71.1",
      "m6": "59.4"
    },
    {
      "p": "[Rethinking Keypoint Representations: Modeling Keypoints and Poses as Objects for Multi-Person Human Pose Estimation](https://arxiv.org/abs/2111.08557v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wmcnally/kapao)",
      "n": "KAPAO-L",
      "d": "2021-11-16",
      "m1": "68.9",
      "m2": "89.4",
      "m3": "75.6",
      "m4": "69.9",
      "m5": "76.6"
    },
    {
      "p": "[Rethinking Keypoint Representations: Modeling Keypoints and Poses as Objects for Multi-Person Human Pose Estimation](https://arxiv.org/abs/2111.08557v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wmcnally/kapao)",
      "n": "KAPAO-M",
      "d": "2021-11-16",
      "m1": "67.1",
      "m2": "88.8",
      "m3": "73.4",
      "m4": "68.1",
      "m5": "75.2"
    },
    {
      "p": "[Greedy Offset-Guided Keypoint Grouping for Human Pose Estimation](https://arxiv.org/abs/2107.03098v2)",
      "c": "[&check;&nbsp;Link](https://github.com/hellojialee/OffsetGuided)",
      "n": "Hourglass-104",
      "d": "2021-07-07",
      "m1": "65.2",
      "m2": "85.9",
      "m3": "69.5",
      "m4": "66.2"
    },
    {
      "p": "[Rethinking Keypoint Representations: Modeling Keypoints and Poses as Objects for Multi-Person Human Pose Estimation](https://arxiv.org/abs/2111.08557v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wmcnally/kapao)",
      "n": "KAPAO-S",
      "d": "2021-11-16",
      "m1": "63.8",
      "m2": "87.7",
      "m3": "69.4",
      "m4": "64.8",
      "m5": "72.1"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
