# multi-person-pose-estimation-on-crowdpose

[Dataset Link](https://github.com/Jeff-sjtu/CrowdPose) \
Task Hierarchy: ['1 Image, 2*2 Stitchi', 'Pose Estimation', 'Multi-Person Pose Estimation']

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
      "label": "mAP @0.5:0.95",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "AP Easy",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "AP Medium",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "AP Hard",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "FPS",
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
      "p": "[RTMO: Towards High-Performance One-Stage Real-Time Multi-Person Pose Estimation](https://arxiv.org/abs/2312.07526v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "RTMO-l",
      "d": "2023-12-12",
      "m1": "83.8",
      "m2": "88.8",
      "m3": "84.7",
      "m4": "77.2",
      "m5": "52.4"
    },
    {
      "p": "[Rethinking pose estimation in crowds: overcoming the detection information-bottleneck and ambiguity](https://arxiv.org/abs/2306.07879v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amathislab/BUCTD)",
      "n": "BUCTD-W48 (w/cond. input from PETR, and generative sampling)",
      "d": "2023-06-13",
      "m1": "78.5",
      "m2": "83.9",
      "m3": "79.0",
      "m4": "72.3"
    },
    {
      "p": "[I^2R-Net: Intra- and Inter-Human Relation Network for Multi-Person Pose Estimation](https://arxiv.org/abs/2206.10892v2)",
      "c": "[&check;&nbsp;Link](https://github.com/leijue222/Intra-and-Inter-Human-Relation-Network-for-MPEE)",
      "n": "I\u00b2R-Net (1st stage: HRFormer-B)",
      "d": "2022-06-22",
      "m1": "77.4",
      "m2": "83.8",
      "m3": "78.1",
      "m4": "69.3"
    },
    {
      "p": "[Explicit Box Detection Unifies End-to-End Multi-Person Pose Estimation](https://arxiv.org/abs/2302.01593v1)",
      "c": "[&check;&nbsp;Link](https://github.com/idea-research/ed-pose)",
      "n": "ED-Pose (Swin-L)",
      "d": "2023-02-03",
      "m1": "76.6",
      "m2": "83.0",
      "m3": "77.3",
      "m4": "68.3"
    },
    {
      "p": "[DETRPose: Real-time end-to-end transformer model for multi-person pose estimation](https://arxiv.org/abs/2506.13027v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SebastianJanampa/DETRPose)",
      "n": "DETRPose-X",
      "d": "2025-06-16",
      "m1": "75.1",
      "m2": "81.3",
      "m3": "75.7",
      "m4": "68.1"
    },
    {
      "p": "[DETRPose: Real-time end-to-end transformer model for multi-person pose estimation](https://arxiv.org/abs/2506.13027v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SebastianJanampa/DETRPose)",
      "n": "DETRPose-L",
      "d": "2025-06-16",
      "m1": "73.3",
      "m2": "79.5",
      "m3": "74.0",
      "m4": "66.1"
    },
    {
      "p": "[HRFormer: High-Resolution Transformer for Dense Prediction](https://arxiv.org/abs/2110.09408v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HRNet/HRFormer)",
      "n": "HRFormer-B",
      "d": "2021-10-18",
      "m1": "72.4",
      "m2": "80.0",
      "m3": "73.5",
      "m4": "62.4"
    },
    {
      "p": "[BAPose: Bottom-Up Pose Estimation with Disentangled Waterfall Representations](https://arxiv.org/abs/2112.10716v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bmartacho/BAPose)",
      "n": "BAPose (W32)",
      "d": "2021-12-20",
      "m1": "72.2",
      "m2": "79.9",
      "m3": "73.4",
      "m4": "61.3"
    },
    {
      "p": "[DETRPose: Real-time end-to-end transformer model for multi-person pose estimation](https://arxiv.org/abs/2506.13027v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SebastianJanampa/DETRPose)",
      "n": "DETRPose-M",
      "d": "2025-06-16",
      "m1": "72.0",
      "m2": "78.6",
      "m3": "72.6",
      "m4": "64.5"
    },
    {
      "p": "[TransPose: Keypoint Localization via Transformer](https://arxiv.org/abs/2012.14214v5)",
      "c": "[&check;&nbsp;Link](https://github.com/yangsenius/TransPose)",
      "n": "TransPose-H",
      "d": "2020-12-28",
      "m1": "71.8",
      "m2": "79.5",
      "m3": "72.9",
      "m4": "62.2"
    },
    {
      "p": "[Self-Constrained Inference Optimization on Structural Groups for Human Pose Estimation](https://arxiv.org/abs/2207.02425v1)",
      "c": "",
      "n": "SCIO (HRNet-48)",
      "d": "2022-07-06",
      "m1": "71.5",
      "m3": "72.2"
    },
    {
      "p": "[ScaleNAS: One-Shot Learning of Scale-Aware Representations for Visual Recognition](https://arxiv.org/abs/2011.14584v1)",
      "c": "",
      "n": "HigherHRNet (ScaleNet_P4)",
      "d": "2020-11-30",
      "m1": "71.3"
    },
    {
      "p": "[Multi-Instance Pose Networks: Rethinking Top-Down Pose Estimation](https://arxiv.org/abs/2101.11223v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rawalkhirodkar/MIPNet)",
      "n": "MIPNet (HRNet-W48)",
      "d": "2021-01-27",
      "m1": "70.0",
      "m2": "78.1",
      "m3": "71.1",
      "m4": "59.4"
    },
    {
      "p": "[The Center of Attention: Center-Keypoint Grouping via Attention for Multi-Person Pose Estimation](https://arxiv.org/abs/2110.05132v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dvl-tum/center-group)",
      "n": "CenterGroup",
      "d": "2021-10-11",
      "m1": "69.4",
      "m2": "76.6",
      "m3": "70.0",
      "m4": "61.5"
    },
    {
      "p": "[HigherHRNet: Scale-Aware Representation Learning for Bottom-Up Human Pose Estimation](https://arxiv.org/abs/1908.10357v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "HigherHRNet(HR-Net-48)",
      "d": "2019-08-27",
      "m1": "67.6",
      "m2": "75.8",
      "m3": "68.1",
      "m4": "58.9",
      "m5": "-"
    },
    {
      "p": "[DETRPose: Real-time end-to-end transformer model for multi-person pose estimation](https://arxiv.org/abs/2506.13027v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SebastianJanampa/DETRPose)",
      "n": "DETRPose-S",
      "d": "2025-06-16",
      "m1": "67.4",
      "m2": "74.7",
      "m3": "68.1",
      "m4": "59.3"
    },
    {
      "p": "[CrowdPose: Efficient Crowded Scenes Pose Estimation and A New Benchmark](http://arxiv.org/abs/1812.00324v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "Joint-candidate SPPE +",
      "d": "2018-12-02",
      "m1": "66.0",
      "m2": "75.5",
      "m3": "66.3",
      "m4": "57.4",
      "m5": "10.1"
    },
    {
      "p": "[Human Pose Estimation for Real-World Crowded Scenarios](https://arxiv.org/abs/1907.06922v1)",
      "c": "[&check;&nbsp;Link](https://github.com/thomasgolda/Human-Pose-Estimation-for-Real-World-Crowded-Scenarios)",
      "n": "OccNet",
      "d": "2019-07-16",
      "m1": "65.5",
      "m2": "75.2",
      "m3": "66.6",
      "m4": "53.1"
    },
    {
      "p": "[Greedy Offset-Guided Keypoint Grouping for Human Pose Estimation](https://arxiv.org/abs/2107.03098v2)",
      "c": "[&check;&nbsp;Link](https://github.com/hellojialee/OffsetGuided)",
      "n": "Hourglass-104",
      "d": "2021-07-07",
      "m1": "65.2",
      "m2": "73.8",
      "m3": "66.2",
      "m4": "54.8",
      "m5": "14.7 (21.4)"
    },
    {
      "p": "[Single-Stage Multi-Person Pose Machines](https://arxiv.org/abs/1908.09220v1)",
      "c": "[&check;&nbsp;Link](https://github.com/murdockhou/Single-Stage-Multi-person-Pose-Machines)",
      "n": "SPM",
      "d": "2019-08-24",
      "m1": "63.7",
      "m2": "70.3",
      "m3": "64.5",
      "m4": "55.7"
    },
    {
      "p": "[RMPE: Regional Multi-person Pose Estimation](http://arxiv.org/abs/1612.00137v5)",
      "c": "[&check;&nbsp;Link](https://github.com/MVIG-SJTU/AlphaPose)",
      "n": "AlphaPose",
      "d": "2016-12-01",
      "m1": "61.0",
      "m2": "71.2",
      "m3": "61.4",
      "m4": "51.1"
    },
    {
      "p": "[Simple Baselines for Human Pose Estimation and Tracking](http://arxiv.org/abs/1804.06208v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "Simple baseline",
      "d": "2018-04-17",
      "m1": "60.8",
      "m2": "71.4",
      "m3": "61.2",
      "m4": "51.2"
    },
    {
      "p": "[Monocular, One-stage, Regression of Multiple 3D People](https://arxiv.org/abs/2008.12272v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Arthur151/ROMP)",
      "n": "ROMP+CAR",
      "d": "2020-08-27",
      "m1": "58.6"
    },
    {
      "p": "[Lite Pose: Efficient Architecture Design for 2D Human Pose Estimation](https://arxiv.org/abs/2205.01271v4)",
      "c": "[&check;&nbsp;Link](https://github.com/mit-han-lab/litepose)",
      "n": "LitePose-S",
      "d": "2022-05-03",
      "m1": "58.3"
    },
    {
      "p": "[Mask R-CNN](http://arxiv.org/abs/1703.06870v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/official/vision)",
      "n": "Mask R-CNN",
      "d": "2017-03-20",
      "m1": "57.2",
      "m2": "69.4",
      "m3": "57.9",
      "m4": "45.8"
    },
    {
      "p": "[DETRPose: Real-time end-to-end transformer model for multi-person pose estimation](https://arxiv.org/abs/2506.13027v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SebastianJanampa/DETRPose)",
      "n": "DETRPose-N",
      "d": "2025-06-16",
      "m1": "56.0",
      "m2": "65.0",
      "m3": "56,6",
      "m4": "46,6"
    },
    {
      "p": "[Monocular, One-stage, Regression of Multiple 3D People](https://arxiv.org/abs/2008.12272v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Arthur151/ROMP)",
      "n": "ROMP",
      "d": "2020-08-27",
      "m1": "55.6"
    },
    {
      "p": "[OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields](https://arxiv.org/abs/1812.08008v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CMU-Perceptual-Computing-Lab/openpose)",
      "n": "OpenPose",
      "d": "2018-12-18",
      "m2": "62.7",
      "m3": "58.7",
      "m4": "32.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
