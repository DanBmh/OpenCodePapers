# multi-hypotheses-3d-human-pose-estimation-on

[Dataset Link](http://vision.imar.ro/human3.6m/description.php) \
Task Hierarchy: ['Pose Estimation', '3D Human Pose Estimation', 'Multi-Hypotheses 3D Human Pose Estimation']

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
      "label": "Average MPJPE (mm)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Average PMPJPE (mm)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Average MPJPE (mm) for occluded Joints",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Expected Calibration Error",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Using 2D ground-truth joints",
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
      "p": "[Disentangled Diffusion-Based 3D Human Pose Estimation with Hierarchical Spatial and Temporal Denoiser](https://arxiv.org/abs/2403.04444v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Andyen512/DDHPose)",
      "n": "DDHPose (H=20, W=10, J-Best)",
      "d": "2024-03-07",
      "m1": "33.62",
      "m2": "26.48"
    },
    {
      "p": "[GFPose: Learning 3D Human Pose Prior with Gradient Fields](https://arxiv.org/abs/2212.08641v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Embracing/GFPose)",
      "n": "GFPose (HPJ2D-010, S=200)",
      "d": "2022-12-16",
      "m1": "35.1"
    },
    {
      "p": "[Diffusion-Based 3D Human Pose Estimation with Multi-Hypothesis Aggregation](https://arxiv.org/abs/2303.11579v2)",
      "c": "[&check;&nbsp;Link](https://github.com/patrick-swk/d3dp)",
      "n": "D3DP",
      "d": "2023-03-21",
      "m1": "35.4",
      "m5": "No"
    },
    {
      "p": "[GFPose: Learning 3D Human Pose Prior with Gradient Fields](https://arxiv.org/abs/2212.08641v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Embracing/GFPose)",
      "n": "GFPose (HPJ2D-000, S=200)",
      "d": "2022-12-16",
      "m1": "35.6",
      "m2": "30.5",
      "m5": "16.9"
    },
    {
      "p": "[Disentangled Diffusion-Based 3D Human Pose Estimation with Hierarchical Spatial and Temporal Denoiser](https://arxiv.org/abs/2403.04444v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Andyen512/DDHPose)",
      "n": "DDHPose (H=20, W=10, P-Best)",
      "d": "2024-03-07",
      "m1": "39.0",
      "m2": "31.2"
    },
    {
      "p": "[GraphMDN: Leveraging graph structure and deep learning to solve inverse problems](https://arxiv.org/abs/2010.13668v1)",
      "c": "",
      "n": "GraphMDN",
      "d": "2020-10-26",
      "m1": "46.2",
      "m2": "36.3"
    },
    {
      "p": "[Monocular 3D Human Pose Estimation by Generation and Ordinal Ranking](https://arxiv.org/abs/1904.01324v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ssfootball04/generative_pose)",
      "n": "Sharma et al.",
      "d": "2019-04-02",
      "m1": "46.8",
      "m2": "37.3"
    },
    {
      "p": "[Multi-hypothesis 3D human pose estimation metrics favor miscalibrated distributions](https://arxiv.org/abs/2210.11179v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sinzlab/cgnf)",
      "n": "cGNF xlarge w Lsample",
      "d": "2022-10-20",
      "m1": "48.5"
    },
    {
      "p": "[Generating Multiple Hypotheses for 3D Human Pose Estimation with Mixture Density Network](http://arxiv.org/abs/1904.05547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chaneyddtt/Generating-Multiple-Hypotheses-for-3D-Human-Pose-Estimation-with-Mixture-Density-Network)",
      "n": "MDN",
      "d": "2019-04-11",
      "m1": "52.7",
      "m2": "42.6"
    },
    {
      "p": "[Multi-hypothesis 3D human pose estimation metrics favor miscalibrated distributions](https://arxiv.org/abs/2210.11179v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sinzlab/cgnf)",
      "n": "cGNF w Lsample",
      "d": "2022-10-20",
      "m1": "53",
      "m3": "41.8",
      "m4": "0.08"
    },
    {
      "p": "[Weakly Supervised Generative Network for Multiple 3D Human Pose Hypotheses](https://arxiv.org/abs/2008.05770v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chaneyddtt/weakly-supervised-3d-pose-generator)",
      "n": "Li et al.",
      "d": "2020-08-13",
      "m1": "73.9",
      "m2": "44.3"
    },
    {
      "p": "[MHEntropy: Entropy Meets Multiple Hypotheses for Pose and Shape Recovery](http://openaccess.thecvf.com//content/ICCV2023/html/Chen_MHEntropy_Entropy_Meets_Multiple_Hypotheses_for_Pose_and_Shape_Recovery_ICCV_2023_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/GloryyrolG/MHEntropy)",
      "n": "MHEntropy",
      "d": "2023-01-01",
      "m2": "36.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
