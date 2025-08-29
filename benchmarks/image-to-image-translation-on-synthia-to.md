# image-to-image-translation-on-synthia-to

[Dataset Link](https://synthia-dataset.net/) \
Task Hierarchy: ['1 Image, 2*2 Stitching', 'Image-to-Image Translation']

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
      "label": "mIoU (13 classes)",
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
      "p": "[PiPa: Pixel- and Patch-wise Self-supervised Learning for Domain Adaptative Semantic Segmentation](https://arxiv.org/abs/2211.07609v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chen742/PiPa)",
      "n": "HRDA + PiPa",
      "d": "2022-11-14",
      "m1": "74.8"
    },
    {
      "p": "[MIC: Masked Image Consistency for Context-Enhanced Domain Adaptation](https://arxiv.org/abs/2212.01322v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/mic)",
      "n": "MIC",
      "d": "2022-12-02",
      "m1": "74.0"
    },
    {
      "p": "[HRDA: Context-Aware High-Resolution Domain-Adaptive Semantic Segmentation](https://arxiv.org/abs/2204.13132v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/hrda)",
      "n": "HRDA",
      "d": "2022-04-27",
      "m1": "72.4"
    },
    {
      "p": "[SePiCo: Semantic-Guided Pixel Contrast for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2204.08808v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bit-da/sepico)",
      "n": "SePiCo",
      "d": "2022-04-19",
      "m1": "71.4"
    },
    {
      "p": "[Context-Aware Mixup for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2108.03557v3)",
      "c": "[&check;&nbsp;Link](https://github.com/qianyuzqy/CAMix)",
      "n": "CAMix (w DAFormer)",
      "d": "2021-08-08",
      "m1": "69.2"
    },
    {
      "p": "[ProCST: Boosting Semantic Segmentation Using Progressive Cyclic Style-Transfer](https://arxiv.org/abs/2204.11891v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shahaf1313/procst)",
      "n": "DAFormer + ProCST",
      "d": "2022-04-25",
      "m1": "68.2"
    },
    {
      "p": "[DAFormer: Improving Network Architectures and Training Strategies for Domain-Adaptive Semantic Segmentation](https://arxiv.org/abs/2111.14887v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lhoyer/DAFormer)",
      "n": "DAFormer",
      "d": "2021-11-29",
      "m1": "67.4"
    },
    {
      "p": "[Smoothing Matters: Momentum Transformer for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2203.07988v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alpc91/transda)",
      "n": "TransDA-B",
      "d": "2022-03-15",
      "m1": "66.3"
    },
    {
      "p": "[Class-Balanced Pixel-Level Self-Labeling for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2203.09744v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lslrh/cpsl)",
      "n": "CPSL",
      "d": "2022-03-18",
      "m1": "65.3"
    },
    {
      "p": "[Cross-Region Domain Adaptation for Class-level Alignment](https://arxiv.org/abs/2109.06422v2)",
      "c": "",
      "n": "ProDA+CRA",
      "d": "2021-09-14",
      "m1": "63.7"
    },
    {
      "p": "[Prototypical Pseudo Label Denoising and Target Structure Learning for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2101.10979v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/ProDA)",
      "n": "ProDA",
      "d": "2021-01-26",
      "m1": "62.0"
    },
    {
      "p": "[Context-Aware Mixup for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2108.03557v3)",
      "c": "[&check;&nbsp;Link](https://github.com/qianyuzqy/CAMix)",
      "n": "CAMix (w Deeplabv2 ResNet 101)",
      "d": "2021-08-08",
      "m1": "59.7"
    },
    {
      "p": "[Instance Adaptive Self-Training for Unsupervised Domain Adaptation](https://arxiv.org/abs/2008.12197v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bupt-ai-cz/IAST-ECCV2020)",
      "n": "IAST(ResNet-101)",
      "d": "2020-08-27",
      "m1": "57.0"
    },
    {
      "p": "[Constructing Self-motivated Pyramid Curriculums for Cross-Domain Semantic Segmentation: A Non-Adversarial Approach](https://arxiv.org/abs/1908.09547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lianqing11/pycda)",
      "n": "PyCDA (ResNet-101)",
      "d": "2019-08-26",
      "m1": "53.3"
    },
    {
      "p": "[Classes Matter: A Fine-grained Adversarial Approach to Cross-domain Semantic Segmentation](https://arxiv.org/abs/2007.09222v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JDAI-CV/FADA)",
      "n": "FADA (ResNet-101)",
      "d": "2020-07-17",
      "m1": "52.5"
    },
    {
      "p": "[Bidirectional Learning for Domain Adaptation of Semantic Segmentation](http://arxiv.org/abs/1904.10620v1)",
      "c": "[&check;&nbsp;Link](https://github.com/liyunsheng13/BDL)",
      "n": "Bidirectional Learning (ResNet-101)",
      "d": "2019-04-24",
      "m1": "51.4"
    },
    {
      "p": "[DADA: Depth-aware Domain Adaptation in Semantic Segmentation](https://arxiv.org/abs/1904.01886v3)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/ADVENT)",
      "n": "DADA (ResNet-101)",
      "d": "2019-04-03",
      "m1": "49.8"
    },
    {
      "p": "[Confidence Regularized Self-Training](https://arxiv.org/abs/1908.09822v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yzou2/CRST)",
      "n": "LRENT (DeepLabv2)",
      "d": "2019-08-26",
      "m1": "48.7"
    },
    {
      "p": "[Sliced Wasserstein Discrepancy for Unsupervised Domain Adaptation](http://arxiv.org/abs/1903.04064v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kevinmusgrave/pytorch-adapt)",
      "n": "SWD",
      "d": "2019-03-10",
      "m1": "48.1"
    },
    {
      "p": "[ADVENT: Adversarial Entropy Minimization for Domain Adaptation in Semantic Segmentation](http://arxiv.org/abs/1811.12833v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thuml/Transfer-Learning-Library)",
      "n": "ADVENT",
      "d": "2018-11-30",
      "m1": "48"
    },
    {
      "p": "[Learning to Adapt Structured Output Space for Semantic Segmentation](https://arxiv.org/abs/1802.10349v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wasidennis/AdaptSegNet)",
      "n": "Multi-level Adaptation",
      "d": "2018-02-28",
      "m1": "46.7"
    },
    {
      "p": "[Domain Adaptation for Structured Output via Discriminative Patch Representations](https://arxiv.org/abs/1901.05427v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wasidennis/AdaptSegNet)",
      "n": "Discriminative Patch (ResNet-101)",
      "d": "2019-01-16",
      "m1": "46.5"
    },
    {
      "p": "[Learning to Adapt Structured Output Space for Semantic Segmentation](https://arxiv.org/abs/1802.10349v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wasidennis/AdaptSegNet)",
      "n": "Single-level Adaptation",
      "d": "2018-02-28",
      "m1": "45.9"
    },
    {
      "p": "[Category Anchor-Guided Unsupervised Domain Adaptation for Semantic Segmentation](https://arxiv.org/abs/1910.13049v2)",
      "c": "[&check;&nbsp;Link](https://github.com/RogerZhangzz/CAG_UDA)",
      "n": "CAG-UDA",
      "d": "2019-10-29",
      "m1": "44.5"
    },
    {
      "p": "[All about Structure: Adapting Structural Information across Domains for Boosting Semantic Segmentation](http://arxiv.org/abs/1903.12212v1)",
      "c": "[&check;&nbsp;Link](https://github.com/a514514772/DISE-Domain-Invariant-Structure-Extraction)",
      "n": "Domain Invariant Structure Extraction",
      "d": "2019-03-26",
      "m1": "41.5"
    },
    {
      "p": "[A Curriculum Domain Adaptation Approach to the Semantic Segmentation of Urban Scenes](http://arxiv.org/abs/1812.09953v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YangZhang4065/AdaptationSeg)",
      "n": "superpixel + color constancy",
      "d": "2018-12-24",
      "m1": "29.7"
    },
    {
      "p": "[Curriculum Domain Adaptation for Semantic Segmentation of Urban Scenes](http://arxiv.org/abs/1707.09465v5)",
      "c": "[&check;&nbsp;Link](https://github.com/YangZhang4065/AdaptationSeg)",
      "n": "CDA",
      "d": "2017-07-29",
      "m1": "29.0"
    },
    {
      "p": "[FCNs in the Wild: Pixel-level Adversarial and Constraint-based Adaptation](http://arxiv.org/abs/1612.02649v1)",
      "c": "[&check;&nbsp;Link](https://github.com/stu92054/Domain-adaptation-on-segmentation)",
      "n": "FCNs in the wild",
      "d": "2016-12-08",
      "m1": "20.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
