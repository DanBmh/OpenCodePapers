# depth-estimation-on-nyu-depth-v2

[Dataset Link](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) \
Task Hierarchy: ['Depth Estimation']

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
      "label": "RMS",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "RMSE",
      "sortable": "true"
    },
    {
      "key": "m3",
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
      "p": "[EVP: Enhanced Visual Perception using Inverse Multi-Attentive Feature Refinement and Regularized Image-Text Alignment](https://arxiv.org/abs/2312.08548v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lavreniuk/evp)",
      "n": "EVP",
      "d": "2023-12-13",
      "m1": "0.224"
    },
    {
      "p": "[DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DINOv2 (ViT-g/14 frozen, w/ DPT decoder)",
      "d": "2023-04-14",
      "m1": "0.279"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-L 1K-MIM",
      "d": "2022-05-26",
      "m1": "0.287"
    },
    {
      "p": "[3D Ken Burns Effect from a Single Image](https://arxiv.org/abs/1909.05483v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sniklaus/3d-ken-burns)",
      "n": "Semantic-aware NN",
      "d": "2019-09-12",
      "m1": "0.30"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-B 1K-MIM",
      "d": "2022-05-26",
      "m1": "0.304"
    },
    {
      "p": "[P3Depth: Monocular Depth Estimation with a Piecewise Planarity Prior](https://arxiv.org/abs/2204.02091v1)",
      "c": "[&check;&nbsp;Link](https://github.com/syscv/p3depth)",
      "n": "P3Depth",
      "d": "2022-04-05",
      "m1": "0.356"
    },
    {
      "p": "[AdaBins: Depth Estimation using Adaptive Bins](https://arxiv.org/abs/2011.14141v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shariqfarooq123/AdaBins)",
      "n": "AdaBins",
      "d": "2020-11-28",
      "m1": "0.364"
    },
    {
      "p": "[Transformer-Based Attention Networks for Continuous Pixel-Wise Prediction](https://arxiv.org/abs/2103.12091v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ygjwd12345/TransDepth)",
      "n": "TransDepth (AGD+ ViT)",
      "d": "2021-03-22",
      "m1": "0.365"
    },
    {
      "p": "[From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation](https://arxiv.org/abs/1907.10326v6)",
      "c": "[&check;&nbsp;Link](https://github.com/cleinc/bts)",
      "n": "BTS",
      "d": "2019-07-24",
      "m1": "0.407"
    },
    {
      "p": "[Enforcing geometric constraints of virtual normal for depth prediction](https://arxiv.org/abs/1907.12209v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aim-uofa/AdelaiDepth)",
      "n": "VNL",
      "d": "2019-07-29",
      "m1": "0.416"
    },
    {
      "p": "[Deep Optics for Monocular Depth Estimation and 3D Object Detection](http://arxiv.org/abs/1904.08601v1)",
      "c": "",
      "n": "Optimized, freeform",
      "d": "2019-04-18",
      "m1": "0.4325"
    },
    {
      "p": "[Deep Optics for Monocular Depth Estimation and 3D Object Detection](http://arxiv.org/abs/1904.08601v1)",
      "c": "",
      "n": "Freeform",
      "d": "2019-04-18",
      "m1": "0.433"
    },
    {
      "p": "[Deep Ordinal Regression Network for Monocular Depth Estimation](http://arxiv.org/abs/1806.02446v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hufu6371/DORN)",
      "n": "DORN",
      "d": "2018-06-06",
      "m1": "0.509"
    },
    {
      "p": "[Multi-Scale Continuous CRFs as Sequential Deep Networks for Monocular Depth Estimation](http://arxiv.org/abs/1704.02157v1)",
      "c": "[&check;&nbsp;Link](https://github.com/danxuhk/ContinuousCRF-CNN)",
      "n": "MS-CRF",
      "d": "2017-04-07",
      "m1": "0.586"
    },
    {
      "p": "[PAD-Net: Multi-Tasks Guided Prediction-and-Distillation Network for Simultaneous Depth Estimation and Scene Parsing](http://arxiv.org/abs/1805.04409v1)",
      "c": "",
      "n": "PAD-Net",
      "d": "2018-05-11",
      "m1": "0.792"
    },
    {
      "p": "[Focus on defocus: bridging the synthetic to real domain gap for depth estimation](https://arxiv.org/abs/2005.09623v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dvl-tum/defocus-net)",
      "n": "Defocus/DepthNet (Normalized)",
      "d": "2020-05-19",
      "m2": "0.013"
    },
    {
      "p": "[A2J: Anchor-to-Joint Regression Network for 3D Articulated Pose Estimation from a Single Depth Image](https://arxiv.org/abs/1908.09999v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zhangboshen/A2J)",
      "n": "A2J",
      "d": "2019-08-27",
      "m3": "8.61"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
