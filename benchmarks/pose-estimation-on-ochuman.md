# pose-estimation-on-ochuman

[Dataset Link](https://github.com/liruilong940607/OCHumanApi) \
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
      "label": "Test AP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Validation AP",
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
      "p": "[ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation](https://arxiv.org/abs/2204.12484v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ViTPose (ViTAE-G, GT bounding boxes)",
      "d": "2022-04-26",
      "m1": "93.3",
      "m2": "92.8"
    },
    {
      "p": "[UniHCP: A Unified Model for Human-Centric Perceptions](https://arxiv.org/abs/2303.02936v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/unihcp)",
      "n": "UniHCP (direct eval)",
      "d": "2023-03-06",
      "m1": "87.4"
    },
    {
      "p": "[PoseBH: Prototypical Multi-Dataset Training Beyond Human Pose Estimation](https://arxiv.org/abs/2505.17475v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uyoung-jeong/PoseBH)",
      "n": "PoseBH-H",
      "d": "2025-05-23",
      "m1": "87.0",
      "m2": "86.0"
    },
    {
      "p": "[RTMPose: Real-Time Multi-Person Pose Estimation based on MMPose](https://arxiv.org/abs/2303.07399v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "RTMPose(RTMPose-l, GT bounding boxes)",
      "d": "2023-03-13",
      "m1": "80.3",
      "m2": "80.5"
    },
    {
      "p": "[Detection, Pose Estimation and Segmentation for Multiple Bodies: Closing the Virtuous Circle](https://arxiv.org/abs/2412.01562v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MiraPurkrabek/BBoxMaskPose)",
      "n": "BBox-Mask-Pose 2x",
      "d": "2024-12-02",
      "m1": "48.3",
      "m2": "48.6"
    },
    {
      "p": "[Rethinking pose estimation in crowds: overcoming the detection information-bottleneck and ambiguity](https://arxiv.org/abs/2306.07879v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amathislab/BUCTD)",
      "n": "BUCTD (CID-W32)",
      "d": "2023-06-13",
      "m1": "47.2",
      "m2": "47.7"
    },
    {
      "p": "[You Only Learn One Query: Learning Unified Human Query for Single-Stage Multi-Person Multi-Task Human-Centric Perception](https://arxiv.org/abs/2312.05525v3)",
      "c": "[&check;&nbsp;Link](https://github.com/lishuhuai527/coco-unihuman)",
      "n": "HQNet (ViT-L)",
      "d": "2023-12-09",
      "m1": "45.6"
    },
    {
      "p": "[Contextual Instance Decoupling for Robust Multi-Person Pose Estimation](http://openaccess.thecvf.com//content/CVPR2022/html/Wang_Contextual_Instance_Decoupling_for_Robust_Multi-Person_Pose_Estimation_CVPR_2022_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/kennethwdk/cid)",
      "n": "CID (HRNet-W48)",
      "d": "2022-01-01",
      "m1": "45.0",
      "m2": "46.1"
    },
    {
      "p": "[Detection, Pose Estimation and Segmentation for Multiple Bodies: Closing the Virtuous Circle](https://arxiv.org/abs/2412.01562v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MiraPurkrabek/BBoxMaskPose)",
      "n": "MaskPose-b",
      "d": "2024-12-02",
      "m1": "45.0",
      "m2": "45.3"
    },
    {
      "p": "[Multi-Instance Pose Networks: Rethinking Top-Down Pose Estimation](https://arxiv.org/abs/2101.11223v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rawalkhirodkar/MIPNet)",
      "n": "MIPNet (HRNet-W48)",
      "d": "2021-01-27",
      "m1": "42.5",
      "m2": "42.0"
    },
    {
      "p": "[You Only Learn One Query: Learning Unified Human Query for Single-Stage Multi-Person Multi-Task Human-Centric Perception](https://arxiv.org/abs/2312.05525v3)",
      "c": "[&check;&nbsp;Link](https://github.com/lishuhuai527/coco-unihuman)",
      "n": "HQNet (ResNet-50)",
      "d": "2023-12-09",
      "m1": "40.0"
    },
    {
      "p": "[Multi-Instance Pose Networks: Rethinking Top-Down Pose Estimation](https://arxiv.org/abs/2101.11223v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rawalkhirodkar/MIPNet)",
      "n": "HRNet-W48",
      "d": "2021-01-27",
      "m1": "37.2",
      "m2": "37.8"
    },
    {
      "p": "[Differentiable Hierarchical Graph Grouping for Multi-Person Pose Estimation](https://arxiv.org/abs/2007.11864v1)",
      "c": "",
      "n": "HGG (AE+)",
      "d": "2020-07-23",
      "m1": "36.0",
      "m2": "41.8"
    },
    {
      "p": "[Simple Baselines for Human Pose Estimation and Tracking](http://arxiv.org/abs/1804.06208v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "ResNet-152",
      "d": "2018-04-17",
      "m1": "33.3",
      "m2": "41.0"
    },
    {
      "p": "[Associative Embedding: End-to-End Learning for Joint Detection and Grouping](http://arxiv.org/abs/1611.05424v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "Associative Embedding+",
      "d": "2016-11-16",
      "m1": "32.8",
      "m2": "40.0"
    },
    {
      "p": "[RMPE: Regional Multi-person Pose Estimation](http://arxiv.org/abs/1612.00137v5)",
      "c": "[&check;&nbsp;Link](https://github.com/MVIG-SJTU/AlphaPose)",
      "n": "RMPE",
      "d": "2016-12-01",
      "m1": "30.7",
      "m2": "38.8"
    },
    {
      "p": "[Simple Baselines for Human Pose Estimation and Tracking](http://arxiv.org/abs/1804.06208v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "ResNet-50",
      "d": "2018-04-17",
      "m1": "29.5",
      "m2": "32.1"
    },
    {
      "p": "[Associative Embedding: End-to-End Learning for Joint Detection and Grouping](http://arxiv.org/abs/1611.05424v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "Associative Embedding",
      "d": "2016-11-16",
      "m1": "29.5",
      "m2": "32.1"
    },
    {
      "p": "[TransPose: Keypoint Localization via Transformer](https://arxiv.org/abs/2012.14214v5)",
      "c": "[&check;&nbsp;Link](https://github.com/yangsenius/TransPose)",
      "n": "TransPose-H",
      "d": "2020-12-28",
      "m2": "62.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
