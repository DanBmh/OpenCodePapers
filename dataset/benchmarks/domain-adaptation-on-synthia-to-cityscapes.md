# domain-adaptation-on-synthia-to-cityscapes

[Dataset Link](https://synthia-dataset.net/) \
Task Hierarchy: ['Domain Adaptation']

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
      "label": "mIoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Extra Manual Annotation",
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
      "p": "[Hyperbolic Active Learning for Semantic Segmentation under Domain Shift](https://arxiv.org/abs/2306.11180v5)",
      "c": "[&check;&nbsp;Link](https://github.com/paolomandica/HALO)",
      "n": "HALO",
      "d": "2023-06-19",
      "m1": "78.1",
      "m2": "Yes"
    },
    {
      "p": "[Iterative Loop Method Combining Active and Semi-Supervised Learning for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2301.13361v4)",
      "c": "[&check;&nbsp;Link](https://github.com/licongguan/ilm-assl)",
      "n": "ILM-ASSL",
      "d": "2023-01-31",
      "m1": "76.6",
      "m2": "Yes"
    },
    {
      "p": "[Transferring to Real-World Layouts: A Depth-aware Framework for Scene Adaptation](https://arxiv.org/abs/2311.12682v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chen742/PiPa)",
      "n": "DCF",
      "d": "2023-11-21",
      "m1": "69.3"
    },
    {
      "p": "[PiPa: Pixel- and Patch-wise Self-supervised Learning for Domain Adaptative Semantic Segmentation](https://arxiv.org/abs/2211.07609v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chen742/PiPa)",
      "n": "HRDA+PiPa",
      "d": "2022-11-14",
      "m1": "68.2"
    },
    {
      "p": "[MIC: Masked Image Consistency for Context-Enhanced Domain Adaptation](https://arxiv.org/abs/2212.01322v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/mic)",
      "n": "MIC",
      "d": "2022-12-02",
      "m1": "67.3"
    },
    {
      "p": "[FREDOM: Fairness Domain Adaptation Approach to Semantic Scene Understanding](https://arxiv.org/abs/2304.02135v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uark-cviu/fredom)",
      "n": "FREDOM - Transformer",
      "d": "2023-04-04",
      "m1": "67"
    },
    {
      "p": "[HRDA: Context-Aware High-Resolution Domain-Adaptive Semantic Segmentation](https://arxiv.org/abs/2204.13132v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/hrda)",
      "n": "HRDA",
      "d": "2022-04-27",
      "m1": "65.8"
    },
    {
      "p": "[SePiCo: Semantic-Guided Pixel Contrast for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2204.08808v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bit-da/sepico)",
      "n": "SePiCo",
      "d": "2022-04-19",
      "m1": "64.3"
    },
    {
      "p": "[Improve Cross-domain Mixed Sampling with Guidance Training for Adaptive Segmentation](https://arxiv.org/abs/2403.14995v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wenlve-zhou/guidance-training)",
      "n": "MIC + Guidance Training",
      "d": "2024-03-22",
      "m1": "63.8"
    },
    {
      "p": "[ProCST: Boosting Semantic Segmentation Using Progressive Cyclic Style-Transfer](https://arxiv.org/abs/2204.11891v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shahaf1313/procst)",
      "n": "DAFormer + ProCST",
      "d": "2022-04-25",
      "m1": "61.6"
    },
    {
      "p": "[DAFormer: Improving Network Architectures and Training Strategies for Domain-Adaptive Semantic Segmentation](https://arxiv.org/abs/2111.14887v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/DAFormer)",
      "n": "DAFormer",
      "d": "2021-11-29",
      "m1": "60.9"
    },
    {
      "p": "[Generalize then Adapt: Source-Free Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2108.11249v1)",
      "c": "[&check;&nbsp;Link](https://github.com/val-iisc/SFDA-Seg)",
      "n": "GtA-SFDA (DeepLabv2-ResNet101)",
      "d": "2021-08-25",
      "m1": "60.1"
    },
    {
      "p": "[FREDOM: Fairness Domain Adaptation Approach to Semantic Scene Understanding](https://arxiv.org/abs/2304.02135v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uark-cviu/fredom)",
      "n": "FREDOM - DeepLabV2",
      "d": "2023-04-04",
      "m1": "59.1"
    },
    {
      "p": "[SePiCo: Semantic-Guided Pixel Contrast for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2204.08808v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bit-da/sepico)",
      "n": "SePiCo (DeepLabv2-ResNet-101)",
      "d": "2022-04-19",
      "m1": "58.1"
    },
    {
      "p": "[Cross-Region Domain Adaptation for Class-level Alignment](https://arxiv.org/abs/2109.06422v2)",
      "c": "",
      "n": "ProDA+CRA",
      "d": "2021-09-14",
      "m1": "56.9"
    },
    {
      "p": "[Domain Adaptive Semantic Segmentation with Self-Supervised Depth Estimation](https://arxiv.org/abs/2104.13613v2)",
      "c": "[&check;&nbsp;Link](https://github.com/qinenergy/corda)",
      "n": "CorDA (ResNet-101)",
      "d": "2021-04-28",
      "m1": "55.0"
    },
    {
      "p": "[Self-supervised Augmentation Consistency for Adapting Semantic Segmentation](https://arxiv.org/abs/2105.00097v1)",
      "c": "[&check;&nbsp;Link](https://github.com/visinf/da-sac)",
      "n": "SAC (ResNet-101)",
      "d": "2021-04-30",
      "m1": "52.6"
    },
    {
      "p": "[Spatio-Temporal Pixel-Level Contrastive Learning-based Source-Free Domain Adaptation for Video Semantic Segmentation](https://arxiv.org/abs/2303.14361v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shaoyuanlo/stpl)",
      "n": "STPL",
      "d": "2023-03-25",
      "m1": "51.8"
    },
    {
      "p": "[Transferring and Regularizing Prediction for Semantic Segmentation](https://arxiv.org/abs/2006.06570v1)",
      "c": "",
      "n": "RPT (ResNet-101)",
      "d": "2020-06-11",
      "m1": "51.2"
    },
    {
      "p": "[Instance Adaptive Self-Training for Unsupervised Domain Adaptation](https://arxiv.org/abs/2008.12197v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bupt-ai-cz/IAST-ECCV2020)",
      "n": "IAST (ResNet-101)",
      "d": "2020-08-27",
      "m1": "49.8"
    },
    {
      "p": "[Self-supervised Augmentation Consistency for Adapting Semantic Segmentation](https://arxiv.org/abs/2105.00097v1)",
      "c": "[&check;&nbsp;Link](https://github.com/visinf/da-sac)",
      "n": "SAC (VGG-16)",
      "d": "2021-04-30",
      "m1": "49.1"
    },
    {
      "p": "[Constructing Self-motivated Pyramid Curriculums for Cross-Domain Semantic Segmentation: A Non-Adversarial Approach](https://arxiv.org/abs/1908.09547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lianqing11/pycda)",
      "n": "PyCDA (ResNet-101)",
      "d": "2019-08-26",
      "m1": "46.7"
    },
    {
      "p": "[BiMaL: Bijective Maximum Likelihood Approach to Domain Adaptation in Semantic Scene Segmentation](https://arxiv.org/abs/2108.03267v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uark-cviu/bimal)",
      "n": "BiMaL",
      "d": "2021-08-06",
      "m1": "46.2"
    },
    {
      "p": "[Classes Matter: A Fine-grained Adversarial Approach to Cross-domain Semantic Segmentation](https://arxiv.org/abs/2007.09222v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JDAI-CV/FADA)",
      "n": "FADA (ResNet-101)",
      "d": "2020-07-17",
      "m1": "45.2"
    },
    {
      "p": "[Cross-Domain Semantic Segmentation via Domain-Invariant Interactive Relation Transfer](http://openaccess.thecvf.com/content_CVPR_2020/html/Lv_Cross-Domain_Semantic_Segmentation_via_Domain-Invariant_Interactive_Relation_Transfer_CVPR_2020_paper.html)",
      "c": "",
      "n": "PIT (ResNet-101)",
      "d": "2020-06-01",
      "m1": "44.0"
    },
    {
      "p": "[Semantically Adaptive Image-to-image Translation for Domain Adaptation of Semantic Segmentation](https://arxiv.org/abs/2009.01166v1)",
      "c": "",
      "n": "SA-I2I (VGG-16)",
      "d": "2020-09-02",
      "m1": "41.5"
    },
    {
      "p": "[ADVENT: Adversarial Entropy Minimization for Domain Adaptation in Semantic Segmentation](http://arxiv.org/abs/1811.12833v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thuml/Transfer-Learning-Library)",
      "n": "ADVENT (ResNet-101)",
      "d": "2018-11-30",
      "m1": "41.2"
    },
    {
      "p": "[Label-Driven Reconstruction for Domain Adaptation in Semantic Segmentation](https://arxiv.org/abs/2003.04614v3)",
      "c": "",
      "n": "LDR (VGG-16)",
      "d": "2020-03-10",
      "m1": "41.1"
    },
    {
      "p": "[Context-Aware Domain Adaptation in Semantic Segmentation](https://arxiv.org/abs/2003.04010v1)",
      "c": "",
      "n": "CD-AM (VGG-16)",
      "d": "2020-03-09",
      "m1": "40.8"
    },
    {
      "p": "[FDA: Fourier Domain Adaptation for Semantic Segmentation](https://arxiv.org/abs/2004.05498v1)",
      "c": "[&check;&nbsp;Link](https://github.com/albumentations-team/albumentations)",
      "n": "FDA (VGG-16)",
      "d": "2020-04-11",
      "m1": "40.5"
    },
    {
      "p": "[Classes Matter: A Fine-grained Adversarial Approach to Cross-domain Semantic Segmentation](https://arxiv.org/abs/2007.09222v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JDAI-CV/FADA)",
      "n": "FADA (VGG-16)",
      "d": "2020-07-17",
      "m1": "39.5"
    },
    {
      "p": "[Cross-Domain Semantic Segmentation via Domain-Invariant Interactive Relation Transfer](http://openaccess.thecvf.com/content_CVPR_2020/html/Lv_Cross-Domain_Semantic_Segmentation_via_Domain-Invariant_Interactive_Relation_Transfer_CVPR_2020_paper.html)",
      "c": "",
      "n": "PIT (VGG-16)",
      "d": "2020-06-01",
      "m1": "38.1"
    },
    {
      "p": "[Constructing Self-motivated Pyramid Curriculums for Cross-Domain Semantic Segmentation: A Non-Adversarial Approach](https://arxiv.org/abs/1908.09547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lianqing11/pycda)",
      "n": "PyCDA (VGG-16)",
      "d": "2019-08-26",
      "m1": "35.9"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
