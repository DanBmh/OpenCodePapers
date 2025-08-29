# monocular-3d-human-pose-estimation-on-human3

[Dataset Link](http://vision.imar.ro/human3.6m/description.php) \
Task Hierarchy: ['1 Image, 2*2 Stitchi', 'Pose Estimation', '3D Human Pose Estimation', 'Monocular 3D Human Pose Estimation']

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
      "label": "Use Video Sequence",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Frames Needed",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Need Ground Truth 2D Pose",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "PA-MPJPE",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "2D detector",
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
      "p": "[MotionBERT: A Unified Perspective on Learning Human Motion Representations](https://arxiv.org/abs/2210.06551v5)",
      "c": "[&check;&nbsp;Link](https://github.com/Walter0807/MotionBERT)",
      "n": "MotionBERT (Finetune)",
      "d": "2022-10-12",
      "m1": "37.5",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer-GCNFormer Network](https://arxiv.org/abs/2310.16288v1)",
      "c": "[&check;&nbsp;Link](https://github.com/taatiteam/motionagformer)",
      "n": "MotionAGFormer-L",
      "d": "2023-10-25",
      "m1": "38.4",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer-GCNFormer Network](https://arxiv.org/abs/2310.16288v1)",
      "c": "[&check;&nbsp;Link](https://github.com/taatiteam/motionagformer)",
      "n": "MotionAGFormer-B",
      "d": "2023-10-25",
      "m1": "38.4",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[MotionBERT: A Unified Perspective on Learning Human Motion Representations](https://arxiv.org/abs/2210.06551v5)",
      "c": "[&check;&nbsp;Link](https://github.com/Walter0807/MotionBERT)",
      "n": "MotionBERT (Scratch)",
      "d": "2022-10-12",
      "m1": "39.2",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[Diffusion-Based 3D Human Pose Estimation with Multi-Hypothesis Aggregation](https://arxiv.org/abs/2303.11579v2)",
      "c": "[&check;&nbsp;Link](https://github.com/patrick-swk/d3dp)",
      "n": "D3DP",
      "d": "2023-03-21",
      "m1": "39.5",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[Disentangled Diffusion-Based 3D Human Pose Estimation with Hierarchical Spatial and Temporal Denoiser](https://arxiv.org/abs/2403.04444v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Andyen512/DDHPose)",
      "n": "DDHPose",
      "d": "2024-03-07",
      "m1": "39.7",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[MixSTE: Seq2seq Mixed Spatio-Temporal Encoder for 3D Human Pose Estimation in Video](https://arxiv.org/abs/2203.00859v4)",
      "c": "[&check;&nbsp;Link](https://github.com/JinluZhang1126/MixSTE)",
      "n": "MixSTE (HRNet, T=243)",
      "d": "2022-03-02",
      "m1": "39.8",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "HRNet"
    },
    {
      "p": "[HEMlets Pose: Learning Part-Centric Heatmap Triplets for Accurate 3D Human Pose Estimation](https://arxiv.org/abs/1910.12032v1)",
      "c": "",
      "n": "HEMlets Pose (H36M+MPII)",
      "d": "2019-10-26",
      "m1": "39.9",
      "m3": "1",
      "m5": "27.9"
    },
    {
      "p": "[3D Human Pose Estimation using Spatio-Temporal Networks with Explicit Occlusion Training](https://arxiv.org/abs/2004.11822v1)",
      "c": "",
      "n": "Spatio-Temporal Network (T=128)",
      "d": "2020-04-07",
      "m1": "40.1",
      "m2": "Yes",
      "m3": "128",
      "m4": "No",
      "m5": "30.7"
    },
    {
      "p": "[KTPFormer: Kinematics and Trajectory Prior Knowledge-Enhanced Transformer for 3D Human Pose Estimation](https://arxiv.org/abs/2404.00658v2)",
      "c": "[&check;&nbsp;Link](https://github.com/JihuaPeng/KTPFormer)",
      "n": "KTPFormer",
      "d": "2024-03-31",
      "m1": "40.1",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[GenHMR: Generative Human Mesh Recovery](https://arxiv.org/abs/2412.14444v1)",
      "c": "",
      "n": "GenHMR",
      "d": "2024-12-19",
      "m1": "41.2",
      "m5": "29.8"
    },
    {
      "p": "[P-STMO: Pre-Trained Spatial Temporal Many-to-One Model for 3D Human Pose Estimation](https://arxiv.org/abs/2203.07628v2)",
      "c": "[&check;&nbsp;Link](https://github.com/patrick-swk/p-stmo)",
      "n": "P-STMO (N=243)",
      "d": "2022-03-15",
      "m1": "42.1",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer-GCNFormer Network](https://arxiv.org/abs/2310.16288v1)",
      "c": "[&check;&nbsp;Link](https://github.com/taatiteam/motionagformer)",
      "n": "MotionAGFormer-S",
      "d": "2023-10-25",
      "m1": "42.5",
      "m2": "Yes",
      "m3": "81",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[Anatomy-aware 3D Human Pose Estimation with Bone-based Pose Decomposition](https://arxiv.org/abs/2002.10322v5)",
      "c": "[&check;&nbsp;Link](https://github.com/sunnychencool/Anatomy3D)",
      "n": "Anatomy3D",
      "d": "2020-02-24",
      "m1": "44.1",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[3D Human Pose Estimation with Spatial and Temporal Transformers](https://arxiv.org/abs/2103.10455v3)",
      "c": "[&check;&nbsp;Link](https://github.com/zczcwh/PoseFormer)",
      "n": "PoseFormer (T=81)",
      "d": "2021-03-18",
      "m1": "44.3",
      "m3": "81",
      "m6": "CPN"
    },
    {
      "p": "[Improving Robustness and Accuracy via Relative Information Encoding in 3D Human Pose Estimation](https://arxiv.org/abs/2107.13994v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paTRICK-swk/Pose3D-RIE)",
      "n": "RIE (T=243 CPN)",
      "d": "2021-07-29",
      "m1": "44.3",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[MotionAGFormer: Enhancing 3D Human Pose Estimation with a Transformer-GCNFormer Network](https://arxiv.org/abs/2310.16288v1)",
      "c": "[&check;&nbsp;Link](https://github.com/taatiteam/motionagformer)",
      "n": "MotionAGFormer-XS",
      "d": "2023-10-25",
      "m1": "45.1",
      "m2": "Yes",
      "m3": "27",
      "m4": "No",
      "m6": "SH"
    },
    {
      "p": "[Attention Mechanism Exploits Temporal Contexts: Real-Time 3D Human Pose Reconstruction](http://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Attention_Mechanism_Exploits_Temporal_Contexts_Real-Time_3D_Human_Pose_Reconstruction_CVPR_2020_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/lrxjason/Attention3DHumanPose)",
      "n": "Attention3DHumanPose",
      "d": "2020-06-01",
      "m1": "45.1",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[Trajectory Space Factorization for Deep Video-Based 3D Human Pose Estimation](https://arxiv.org/abs/1908.08289v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jiahaoLjh/trajectory-pose-3d)",
      "n": "Trajectory Space Factorization (50 frames)",
      "d": "2019-08-22",
      "m1": "46.6",
      "m2": "Yes",
      "m3": "50",
      "m4": "No"
    },
    {
      "p": "[3D human pose estimation in video with temporal convolutions and semi-supervised training](http://arxiv.org/abs/1811.11742v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "VideoPose3D (T=243)",
      "d": "2018-11-28",
      "m1": "46.8",
      "m2": "Yes",
      "m3": "243",
      "m4": "No",
      "m6": "CPN"
    },
    {
      "p": "[Sampling is Matter: Point-guided 3D Human Mesh Reconstruction](https://arxiv.org/abs/2304.09502v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DCVL-3D/PointHMR_release)",
      "n": "PointHMR",
      "d": "2023-04-19",
      "m1": "48.3",
      "m5": "32.9"
    },
    {
      "p": "[SRNet: Improving Generalization in 3D Human Pose Estimation with a Split-and-Recombine Approach](https://arxiv.org/abs/2007.09389v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ailingzengzzz/Split-and-Recombine-Net)",
      "n": "SRNET",
      "d": "2020-07-18",
      "m1": "49.9",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[PoseAug: A Differentiable Pose Augmentation Framework for 3D Human Pose Estimation](https://arxiv.org/abs/2105.02465v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jfzhang95/PoseAug)",
      "n": "HR-Net+VPose+PoseAug",
      "d": "2021-05-06",
      "m1": "50.2",
      "m5": "39.1"
    },
    {
      "p": "[Cascaded deep monocular 3D human pose estimation with evolutionary training data](https://arxiv.org/abs/2006.07778v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Nicholasli1995/EvoSkeleton)",
      "n": "TAG-Net",
      "d": "2020-06-14",
      "m1": "50.9",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Predicting Camera Viewpoint Improves Cross-dataset Generalization for 3D Human Pose Estimation](https://arxiv.org/abs/2004.03143v1)",
      "c": "",
      "n": "cross-dataset-evaluation",
      "d": "2020-04-07",
      "m1": "52.0",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Learning 3D Human Pose from Structure and Motion](http://arxiv.org/abs/1711.09250v2)",
      "c": "[&check;&nbsp;Link](https://github.com/anuragmundhada/3dpose-demo-iitb)",
      "n": "TP-Net",
      "d": "2017-11-25",
      "m1": "52.1",
      "m2": "Yes",
      "m3": "20",
      "m4": "No"
    },
    {
      "p": "[Generating Multiple Hypotheses for 3D Human Pose Estimation with Mixture Density Network](http://arxiv.org/abs/1904.05547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chaneyddtt/Generating-Multiple-Hypotheses-for-3D-Human-Pose-Estimation-with-Mixture-Density-Network)",
      "n": "Multimodal Mixture Density Networks",
      "d": "2019-04-11",
      "m1": "52.7",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Semantic Graph Convolutional Networks for 3D Human Pose Regression](https://arxiv.org/abs/1904.03345v3)",
      "c": "[&check;&nbsp;Link](https://github.com/garyzhao/SemGCN)",
      "n": "SemGCN",
      "d": "2019-04-06",
      "m1": "57.6",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Monocular 3D Human Pose Estimation by Generation and Ordinal Ranking](https://arxiv.org/abs/1904.01324v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ssfootball04/generative_pose)",
      "n": "MultiPoseNet",
      "d": "2019-04-02",
      "m1": "58.0",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Monocular Total Capture: Posing Face, Body, and Hands in the Wild](http://arxiv.org/abs/1812.01598v1)",
      "c": "[&check;&nbsp;Link](https://github.com/CMU-Perceptual-Computing-Lab/MonocularTotalCapture)",
      "n": "Monocular Total Capture",
      "d": "2018-12-04",
      "m1": "58.3",
      "m2": "NO",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[A simple yet effective baseline for 3d human pose estimation](http://arxiv.org/abs/1705.03098v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "SIM (SH detections FT) (MA)",
      "d": "2017-05-08",
      "m1": "62.9",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Exploiting temporal context for 3D human pose estimation in the wild](https://arxiv.org/abs/1905.04266v1)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/Temporal-3D-Pose-Kinetics)",
      "n": "Bundle Adjustment (GTi)",
      "d": "2019-05-10",
      "m1": "63.3"
    },
    {
      "p": "[XNect: Real-time Multi-Person 3D Motion Capture with a Single RGB Camera](https://arxiv.org/abs/1907.00837v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "SelecSLS",
      "d": "2019-07-01",
      "m1": "63.6",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Towards 3D Human Pose Estimation in the Wild: a Weakly-supervised Approach](http://arxiv.org/abs/1704.02447v2)",
      "c": "[&check;&nbsp;Link](https://github.com/xingyizhou/pytorch-pose-hg-3d)",
      "n": "Weakly Supervised Transfer Learning",
      "d": "2017-04-08",
      "m1": "64.9",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[VIBE: Video Inference for Human Body Pose and Shape Estimation](https://arxiv.org/abs/1912.05656v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mkocabas/VIBE)",
      "n": "VIBE",
      "d": "2019-12-11",
      "m1": "65.6",
      "m2": "Yes",
      "m3": "16",
      "m4": "No"
    },
    {
      "p": "[Convolutional Mesh Regression for Single-Image Human Shape Reconstruction](https://arxiv.org/abs/1905.03244v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nkolot/GraphCMR)",
      "n": "GraphCMR",
      "d": "2019-05-08",
      "m1": "74.7",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Lifting from the Deep: Convolutional 3D Pose Estimation from a Single Image](http://arxiv.org/abs/1701.00295v4)",
      "c": "[&check;&nbsp;Link](https://github.com/DenisTome/Lifting-from-the-Deep-release)",
      "n": "Projected-pose belief maps + 2D fusion layers",
      "d": "2017-01-01",
      "m1": "88.39",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[RepNet: Weakly Supervised Training of an Adversarial Reprojection Network for 3D Human Pose Estimation](http://arxiv.org/abs/1902.09868v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bastianwandt/RepNet)",
      "n": "RepNet",
      "d": "2019-02-26",
      "m1": "89.9",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[A Dual-Source Approach for 3D Human Pose Estimation from a Single Image](http://arxiv.org/abs/1705.02883v2)",
      "c": "",
      "n": "Dual-source approach",
      "d": "2017-05-08",
      "m1": "97.39",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Sparseness Meets Deepness: 3D Human Pose Estimation from Monocular Video](http://arxiv.org/abs/1511.09439v2)",
      "c": "[&check;&nbsp;Link](https://github.com/chuxiaoselena/SparsenessMeetsDeepness)",
      "n": "Sparseness Meets Deepness",
      "d": "2015-11-30",
      "m1": "113.01",
      "m2": "Yes",
      "m3": "300",
      "m4": "No"
    },
    {
      "p": "[End-to-end Recovery of Human Shape and Pose](http://arxiv.org/abs/1712.06584v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "HMR",
      "d": "2017-12-18",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Neural Body Fitting: Unifying Deep Learning and Model-Based Human Pose and Shape Estimation](http://arxiv.org/abs/1808.05942v1)",
      "c": "[&check;&nbsp;Link](https://github.com/andrewjong/SwapNet)",
      "n": "Neural Body Fitting\n(NBF)",
      "d": "2018-08-17",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Unite the People: Closing the Loop Between 3D and 2D Human Representations](http://arxiv.org/abs/1701.02468v3)",
      "c": "[&check;&nbsp;Link](https://github.com/MandyMo/pytorch_HMR)",
      "n": "SMPLify\n(dense)",
      "d": "2017-01-10",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Ordinal Depth Supervision for 3D Human Pose Estimation](http://arxiv.org/abs/1805.04095v1)",
      "c": "[&check;&nbsp;Link](https://github.com/geopavlakos/ordinal-pose3d)",
      "n": "Ordinal Depth Supervision",
      "d": "2018-05-10",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[3D Human Pose Estimation in the Wild by Adversarial Learning](http://arxiv.org/abs/1803.09722v2)",
      "c": "",
      "n": "Adversarial Learning",
      "d": "2018-03-26",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Camera Distance-aware Top-down Approach for 3D Multi-person Pose Estimation from a Single RGB Image](https://arxiv.org/abs/1907.11346v2)",
      "c": "[&check;&nbsp;Link](https://github.com/mks0601/3DMPPE_POSENET_RELEASE)",
      "n": "Moon et. al.",
      "d": "2019-07-26",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[PoseAug: A Differentiable Pose Augmentation Framework for 3D Human Pose Estimation](https://arxiv.org/abs/2105.02465v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jfzhang95/PoseAug)",
      "n": "PoseAug",
      "d": "2021-05-06",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[HEMlets Pose: Learning Part-Centric Heatmap Triplets for Accurate 3D Human Pose Estimation](https://arxiv.org/abs/1910.12032v1)",
      "c": "",
      "n": "HEMlets Pose",
      "d": "2019-10-26",
      "m2": "No",
      "m3": "1",
      "m4": "No"
    },
    {
      "p": "[Ray3D: ray-based 3D human pose estimation for monocular absolute 3D localization](https://arxiv.org/abs/2203.11471v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YxZhxn/Ray3D)",
      "n": "Ray3D",
      "d": "2022-03-22",
      "m2": "Yes",
      "m3": "9",
      "m4": "No"
    },
    {
      "p": "[Exploiting temporal context for 3D human pose estimation in the wild](https://arxiv.org/abs/1905.04266v1)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/Temporal-3D-Pose-Kinetics)",
      "n": "Bundle Adjustment",
      "d": "2019-05-10",
      "m2": "Yes",
      "m3": "190",
      "m4": "No"
    },
    {
      "p": "[Neural Body Fitting: Unifying Deep Learning and Model-Based Human Pose and Shape Estimation](http://arxiv.org/abs/1808.05942v1)",
      "c": "[&check;&nbsp;Link](https://github.com/andrewjong/SwapNet)",
      "n": "Neural Body Fitting (NBF)",
      "d": "2018-08-17",
      "m5": "59.9"
    },
    {
      "p": "[Unite the People: Closing the Loop Between 3D and 2D Human Representations](http://arxiv.org/abs/1701.02468v3)",
      "c": "[&check;&nbsp;Link](https://github.com/MandyMo/pytorch_HMR)",
      "n": "SMPLify (dense)",
      "d": "2017-01-10",
      "m5": "80.7"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
