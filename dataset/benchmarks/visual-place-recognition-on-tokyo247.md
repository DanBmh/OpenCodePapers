# visual-place-recognition-on-tokyo247

[Dataset Link]() \
Task Hierarchy: ['Visual Place Recognition']

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
      "label": "Recall@1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Recall@5",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Recall@10",
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
      "p": "[Pair-VPR: Place-Aware Pre-training and Contrastive Pair Classification for Visual Place Recognition with Vision Transformers](https://arxiv.org/abs/2410.06614v2)",
      "c": "[&check;&nbsp;Link](https://github.com/csiro-robotics/Pair-VPR)",
      "n": "Pair-VPR-p",
      "d": "2024-10-09",
      "m1": "100",
      "m2": "100",
      "m3": "100"
    },
    {
      "p": "[EffoVPR: Effective Foundation Model Utilization for Visual Place Recognition](https://arxiv.org/abs/2405.18065v2)",
      "c": "",
      "n": "EffoVPR",
      "d": "2024-05-28",
      "m1": "98.7",
      "m2": "98.7",
      "m3": "98.7"
    },
    {
      "p": "[Focus on Local: Finding Reliable Discriminative Regions for Visual Place Recognition](https://arxiv.org/abs/2504.09881v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chenshunpeng/FoL)",
      "n": "FoL",
      "d": "2025-04-14",
      "m1": "98.4",
      "m2": "99.1",
      "m3": "99.4"
    },
    {
      "p": "[Query-Based Adaptive Aggregation for Multi-Dataset Joint Training Toward Universal Visual Place Recognition](https://arxiv.org/abs/2507.03831v1)",
      "c": "",
      "n": "QAA-DINOv2-B-8192",
      "d": "2025-07-04",
      "m1": "98.4"
    },
    {
      "p": "[Pair-VPR: Place-Aware Pre-training and Contrastive Pair Classification for Visual Place Recognition with Vision Transformers](https://arxiv.org/abs/2410.06614v2)",
      "c": "[&check;&nbsp;Link](https://github.com/csiro-robotics/Pair-VPR)",
      "n": "Pair-VPR-s",
      "d": "2024-10-09",
      "m1": "98.1",
      "m2": "98.4",
      "m3": "98.7"
    },
    {
      "p": "[BoQ: A Place is Worth a Bag of Learnable Queries](https://arxiv.org/abs/2405.07364v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amaralibey/bag-of-queries)",
      "n": "BoQ",
      "d": "2024-05-12",
      "m1": "98.1",
      "m2": "98.1",
      "m3": "98.7"
    },
    {
      "p": "[Focus on Local: Finding Reliable Discriminative Regions for Visual Place Recognition](https://arxiv.org/abs/2504.09881v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chenshunpeng/FoL)",
      "n": "FoL-global",
      "d": "2025-04-14",
      "m1": "96.2",
      "m2": "98.7",
      "m3": "98.7"
    },
    {
      "p": "[Towards Seamless Adaptation of Pre-trained Models for Visual Place Recognition](https://arxiv.org/abs/2402.14505v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Lu-Feng/SelaVPR)",
      "n": "SelaVPR",
      "d": "2024-02-22",
      "m1": "94.0",
      "m2": "97.5",
      "m3": "96.8"
    },
    {
      "p": "[EigenPlaces: Training Viewpoint Robust Models for Visual Place Recognition](https://arxiv.org/abs/2308.10832v1)",
      "c": "[&check;&nbsp;Link](https://github.com/stschubert/vpr_tutorial)",
      "n": "EigenPlaces",
      "d": "2023-08-21",
      "m1": "93"
    },
    {
      "p": "[ProGEO: Generating Prompts through Image-Text Contrastive Learning for Visual Geo-localization](https://arxiv.org/abs/2406.01906v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chain-mao/progeo)",
      "n": "ProGEO",
      "d": "2024-06-04",
      "m1": "88.6",
      "m2": "93.3"
    },
    {
      "p": "[Patch-NetVLAD: Multi-Scale Fusion of Locally-Global Descriptors for Place Recognition](https://arxiv.org/abs/2103.01486v1)",
      "c": "[&check;&nbsp;Link](https://github.com/QVPR/Patch-NetVLAD)",
      "n": "Patch-NetVLAD",
      "d": "2021-03-02",
      "m1": "86",
      "m2": "88.6",
      "m3": "90.5"
    },
    {
      "p": "[Rethinking Visual Geo-localization for Large-Scale Applications](https://arxiv.org/abs/2204.02287v2)",
      "c": "[&check;&nbsp;Link](https://github.com/gmberton/cosplace)",
      "n": "CosPlace",
      "d": "2022-04-05",
      "m1": "82.2"
    },
    {
      "p": "[Generalized Contrastive Optimization of Siamese Networks for Place Recognition](https://arxiv.org/abs/2103.06638v4)",
      "c": "[&check;&nbsp;Link](https://github.com/marialeyvallina/generalized_contrastive_loss)",
      "n": "GCL [trained only on MSLS]",
      "d": "2021-03-11",
      "m1": "69.84",
      "m2": "84.76",
      "m3": "80.63"
    },
    {
      "p": "[Rethinking Visual Geo-localization for Large-Scale Applications](https://arxiv.org/abs/2204.02287v2)",
      "c": "[&check;&nbsp;Link](https://github.com/gmberton/cosplace)",
      "n": "CosPlace (ResNet-101 2048-D)",
      "d": "2022-04-05",
      "m2": "95.9",
      "m3": "96.5"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
