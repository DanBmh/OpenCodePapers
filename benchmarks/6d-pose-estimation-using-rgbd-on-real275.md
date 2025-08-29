# 6d-pose-estimation-using-rgbd-on-real275

[Dataset Link](https://geometry.stanford.edu/projects/NOCS_CVPR2019/) \
Task Hierarchy: ['1 Image, 2*2 Stitchi', 'Pose Estimation', '6D Pose Estimation using RGBD']

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
      "label": "mAP 10, 5cm",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "mAP 10, 10cm",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "mAP 3DIou@25",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "mAP 3DIou@50",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "mAP 5, 5cm",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "mAP 3DIou@75",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "mAP 5, 2cm",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "FPS",
      "sortable": "true"
    },
    {
      "key": "m9",
      "label": "Rerr",
      "sortable": "true"
    },
    {
      "key": "m10",
      "label": "Terr",
      "sortable": "true"
    },
    {
      "key": "m11",
      "label": "mAP 10, 2cm",
      "sortable": "true"
    },
    {
      "key": "m12",
      "label": "mAP 15, 5cm",
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
      "p": "[GenPose: Generative Category-level Object Pose Estimation via Diffusion Models](https://arxiv.org/abs/2306.10531v3)",
      "c": "",
      "n": "GenPose https://github.com/Jiyao06/GenPose",
      "d": "2023-06-18",
      "m1": "84.0",
      "m5": "60.9",
      "m7": "52.1",
      "m11": "72.4"
    },
    {
      "p": "[Generative Category-Level Shape and Pose Estimation with Semantic Primitives](https://arxiv.org/abs/2210.01112v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zju3dv/gcasp)",
      "n": "gcasp",
      "d": "2022-10-03",
      "m1": "76.3",
      "m4": "79.0",
      "m5": "54.7",
      "m6": "65.3",
      "m7": "46.9",
      "m11": "64.2"
    },
    {
      "p": "[GPV-Pose: Category-level Object Pose Estimation via Geometry-guided Point-wise Voting](https://arxiv.org/abs/2203.07918v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lolrudy/gpv_pose)",
      "n": "GPV-Pose",
      "d": "2022-03-15",
      "m1": "73.3",
      "m2": "74.6",
      "m3": "84.2",
      "m4": "83",
      "m5": "42.9",
      "m6": "64.4",
      "m7": "32",
      "m8": "20"
    },
    {
      "p": "[DualPoseNet: Category-level 6D Object Pose and Size Estimation Using Dual Pose Network with Refined Learning of Pose Consistency](https://arxiv.org/abs/2103.06526v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Gorilla-Lab-SCUT/DualPoseNet)",
      "n": "DualPoseNet",
      "d": "2021-03-11",
      "m1": "66.8",
      "m4": "79.8",
      "m5": "35.9",
      "m11": "50"
    },
    {
      "p": "[UDA-COPE: Unsupervised Domain Adaptation for Category-level Object Pose Estimation](https://arxiv.org/abs/2111.12580v2)",
      "c": "",
      "n": "UDA-COPE",
      "d": "2021-11-24",
      "m1": "66.0",
      "m4": "82.6",
      "m5": "34.8",
      "m6": "62.5",
      "m7": "30.4",
      "m11": "56.9"
    },
    {
      "p": "[CenterSnap: Single-Shot Multi-Object 3D Shape Reconstruction and Categorical 6D Pose and Size Estimation](https://arxiv.org/abs/2203.01929v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zubair-irshad/CenterSnap)",
      "n": "CenterSnap",
      "d": "2022-03-03",
      "m1": "64.3",
      "m2": "70.9",
      "m3": "83.5",
      "m4": "80.2",
      "m5": "29.1"
    },
    {
      "p": "[FS-Net: Fast Shape-based Network for Category-Level 6D Object Pose Estimation with Decoupled Rotation Mechanism](https://arxiv.org/abs/2103.07054v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DC1991/FS-Net)",
      "n": "FS-Net",
      "d": "2021-03-12",
      "m1": "60.8",
      "m2": "64.6",
      "m3": "95.1",
      "m4": "92.2",
      "m5": "28.2",
      "m6": "63.5",
      "m8": "20"
    },
    {
      "p": "[CPPF: Towards Robust Category-Level 9D Pose Estimation in the Wild](https://arxiv.org/abs/2203.03089v2)",
      "c": "[&check;&nbsp;Link](https://github.com/qq456cvb/cppf)",
      "n": "CPPF",
      "d": "2022-03-07",
      "m1": "44.9",
      "m3": "78.2",
      "m4": "26.4",
      "m5": "16.9",
      "m12": "50.8"
    },
    {
      "p": "[Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation](https://arxiv.org/abs/1901.02970v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wenbowen123/BundleTrack)",
      "n": "NOCS (128 bins)",
      "d": "2019-01-09",
      "m1": "26.7",
      "m2": "26.7",
      "m3": "84.9",
      "m4": "80.5",
      "m5": "9.5"
    },
    {
      "p": "[BundleTrack: 6D Pose Tracking for Novel Objects without Instance or Category-Level 3D Models](https://arxiv.org/abs/2108.00516v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wenbowen123/BundleTrack)",
      "n": "BundleTrack",
      "d": "2021-08-01",
      "m3": "99.9",
      "m5": "87.4",
      "m9": "2.4",
      "m10": "2.1"
    },
    {
      "p": "[6-PACK: Category-level 6D Pose Tracker with Anchor-Based Keypoints](https://arxiv.org/abs/1910.10750v1)",
      "c": "[&check;&nbsp;Link](https://github.com/j96w/6-PACK)",
      "n": "6-PACK",
      "d": "2019-10-23",
      "m3": "94.2",
      "m5": "33.3",
      "m9": "16.0",
      "m10": "3.5"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
