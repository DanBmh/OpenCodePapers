# face-alignment-on-cofw

[Dataset Link](http://www.vision.caltech.edu/xpburgos/ICCV13/#dataset) \
Task Hierarchy: ['3D Face Reconstruction', 'Facial Recognition and Modelling', 'Face Alignment']

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
      "label": "NME (inter-ocular)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Recall at 80% precision (Landmarks Visibility)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "NME (inter-pupil)",
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
      "p": "[Fiducial Focus Augmentation for Facial Landmark Detection](https://arxiv.org/abs/2402.15044v1)",
      "c": "",
      "n": "FiFA",
      "d": "2024-02-23",
      "m1": "2.96"
    },
    {
      "p": "[Subpixel Heatmap Regression for Facial Landmark Localization](https://arxiv.org/abs/2111.02360v1)",
      "c": "",
      "n": "SH-FAN",
      "d": "2021-11-03",
      "m1": "3.02%"
    },
    {
      "p": "[Towards Accurate Facial Landmark Detection via Cascaded Transformers](https://arxiv.org/abs/2208.10808v1)",
      "c": "",
      "n": "DTLD+",
      "d": "2022-08-23",
      "m1": "3.02%"
    },
    {
      "p": "[Pixel-in-Pixel Net: Towards Efficient Facial Landmark Detection in the Wild](https://arxiv.org/abs/2003.03771v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jhb86253817/PIPNet)",
      "n": "PIPNet (ResNet-101)",
      "d": "2020-03-08",
      "m1": "3.08%"
    },
    {
      "p": "[When Liebig's Barrel Meets Facial Landmark Detection: A Practical Model](https://arxiv.org/abs/2105.13150v2)",
      "c": "",
      "n": "BarrelNet (ResNet-101)",
      "d": "2021-05-27",
      "m1": "3.1%"
    },
    {
      "p": "[STAR Loss: Reducing Semantic Ambiguity in Facial Landmark Detection](https://arxiv.org/abs/2306.02763v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zhenglinzhou/star)",
      "n": "STAR",
      "d": "2023-06-05",
      "m1": "3.21%",
      "m3": "4.62"
    },
    {
      "p": "[HIH: Towards More Accurate Face Alignment via Heatmap in Heatmap](https://arxiv.org/abs/2104.03100v2)",
      "c": "[&check;&nbsp;Link](https://github.com/starhiking/HeatmapInHeatmap)",
      "n": "HIH",
      "d": "2021-04-07",
      "m1": "3.21%"
    },
    {
      "p": "[Revisiting Quantization Error in Face Alignment](https://openaccess.thecvf.com/content/ICCV2021W/MFR/html/Lan_Revisting_Quantization_Error_in_Face_Alignment_ICCVW_2021_paper.html)",
      "c": "",
      "n": "HIH w. MSE(2 stack)",
      "d": "2021-09-13",
      "m1": "3.28%"
    },
    {
      "p": "[Sparse Local Patch Transformer for Robust Face Alignment and Landmarks Inherent Relation Learning](https://arxiv.org/abs/2203.06541v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiahao-uts/slpt-master)",
      "n": "SLPT",
      "d": "2022-03-13",
      "m1": "3.32",
      "m3": "4.79"
    },
    {
      "p": "[Pre-training strategies and datasets for facial representation learning](https://arxiv.org/abs/2103.16554v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tomas-gajarsky/facetorch)",
      "n": "Ours (VGG-F)",
      "d": "2021-03-30",
      "m1": "3.32"
    },
    {
      "p": "[ATF: Towards Robust Face Alignment via Leveraging Similarity and Diversity across Different Datasets](https://dl.acm.org/doi/10.1145/3394171.3414037)",
      "c": "[&check;&nbsp;Link](https://github.com/starhiking/ATF)",
      "n": "ATF",
      "d": "2020-10-12",
      "m1": "3.32%"
    },
    {
      "p": "[High-Resolution Representations for Labeling Pixels and Regions](http://arxiv.org/abs/1904.04514v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "HRNet",
      "d": "2019-04-09",
      "m1": "3.45%"
    },
    {
      "p": "[Deep High-Resolution Representation Learning for Visual Recognition](https://arxiv.org/abs/1908.07919v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmdetection)",
      "n": "HRNet",
      "d": "2019-08-20",
      "m1": "3.45"
    },
    {
      "p": "[ACR Loss: Adaptive Coordinate-based Regression Loss for Face Alignment](https://arxiv.org/abs/2203.15835v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aliprf/acr-loss)",
      "n": "EF-3ACR",
      "d": "2022-03-29",
      "m1": "3.47%"
    },
    {
      "p": "[Fast and Accurate: Structure Coherence Component for Face Alignment](https://arxiv.org/abs/2006.11697v1)",
      "c": "",
      "n": "SCC",
      "d": "2020-06-21",
      "m1": "3.63%"
    },
    {
      "p": "[PropagationNet: Propagate Points to Curve to Learn Structure Information](https://arxiv.org/abs/2006.14308v1)",
      "c": "",
      "n": "PropNet",
      "d": "2020-06-25",
      "m1": "3.71%"
    },
    {
      "p": "[Facial Landmark Points Detection Using Knowledge Distillation-Based Neural Networks](https://arxiv.org/abs/2111.07047v1)",
      "c": "[&check;&nbsp;Link](https://github.com/aliprf/kd-loss)",
      "n": "EfficientNet",
      "d": "2021-11-13",
      "m1": "3.81%"
    },
    {
      "p": "[Look at Boundary: A Boundary-Aware Face Alignment Algorithm](http://arxiv.org/abs/1805.10483v1)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "LAB (w/ B)",
      "d": "2018-05-26",
      "m1": "3.92%"
    },
    {
      "p": "[Facial Landmark Points Detection Using Knowledge Distillation-Based Neural Networks](https://arxiv.org/abs/2111.07047v1)",
      "c": "[&check;&nbsp;Link](https://github.com/aliprf/kd-loss)",
      "n": "MobileNetV2+KD-Loss",
      "d": "2021-11-13",
      "m1": "4.11%"
    },
    {
      "p": "[Wing Loss for Robust Facial Landmark Localisation with Convolutional Neural Networks](http://arxiv.org/abs/1711.06753v5)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "Wing (Feng et al., 2018)",
      "d": "2017-11-17",
      "m1": "5.07"
    },
    {
      "p": "[Look at Boundary: A Boundary-Aware Face Alignment Algorithm](http://arxiv.org/abs/1805.10483v1)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpose)",
      "n": "LAB",
      "d": "2018-05-26",
      "m1": "5.58%"
    },
    {
      "p": "[Disentangling 3D Pose in A Dendritic CNN for Unconstrained 2D Face Alignment](http://arxiv.org/abs/1802.06713v3)",
      "c": "",
      "n": "PCD-CNNCVPR 18",
      "d": "2018-02-19",
      "m1": "5.77%"
    },
    {
      "p": "[Multi-task head pose estimation in-the-wild](https://arxiv.org/abs/2202.02299v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bobetocalo/bobetocalo_pami20)",
      "n": "MNN+OR (Inter-pupils Norm)",
      "d": "2020-12-22",
      "m2": "72.12",
      "m3": "5.04%"
    },
    {
      "p": "[Face Alignment using a 3D Deeply-initialized Ensemble of Regression Trees](https://arxiv.org/abs/1902.01831v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bobetocalo/bobetocalo_eccv18)",
      "n": "3DDE (Inter-pupil Norm)",
      "d": "2019-02-05",
      "m2": "63.89",
      "m3": "5.11%"
    },
    {
      "p": "[Cascade of Encoder-Decoder CNNs with Learned Coordinates Regressor for Robust Facial Landmarks Detection](https://doi.org/10.1016/j.patrec.2019.10.012)",
      "c": "[&check;&nbsp;Link](https://github.com/bobetocalo/bobetocalo_prl19)",
      "n": "CHR2C (Inter-pupils Norm)",
      "d": "2019-10-15",
      "m3": "5.09%"
    },
    {
      "p": "[A Deeply-initialized Coarse-to-fine Ensemble of Regression Trees for Face Alignment](http://openaccess.thecvf.com/content_ECCV_2018/html/Roberto_Valle_A_Deeply-initialized_Coarse-to-fine_ECCV_2018_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/bobetocalo/bobetocalo_eccv18)",
      "n": "DCFE",
      "d": "2018-09-01",
      "m3": "5.27%"
    },
    {
      "p": "[Stacked Dense U-Nets with Dual Transformers for Robust Face Alignment](http://arxiv.org/abs/1812.01936v1)",
      "c": "[&check;&nbsp;Link](https://github.com/deepinsight/insightface)",
      "n": "DenseU-Net + Dual Transformer",
      "d": "2018-12-05",
      "m3": "5.55%"
    },
    {
      "p": "[Multi-task head pose estimation in-the-wild](https://arxiv.org/abs/2202.02299v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bobetocalo/bobetocalo_pami20)",
      "n": "MNN (Inter-pupil Norm)",
      "d": "2020-12-22",
      "m3": "5.65%"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
