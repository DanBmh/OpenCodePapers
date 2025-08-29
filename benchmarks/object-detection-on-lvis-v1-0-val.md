# object-detection-on-lvis-v1-0-val

[Dataset Link](https://www.lvisdataset.org/dataset) \
Task Hierarchy: ['16k', 'Object Detection']

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
      "label": "box AP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "box APr",
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
      "p": "[DETRs with Collaborative Hybrid Assignments Training](https://arxiv.org/abs/2211.12860v5)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmdetection)",
      "n": "Co-DETR (single-scale)",
      "d": "2022-11-22",
      "m1": "68.0"
    },
    {
      "p": "[Grounding DINO 1.5: Advance the \"Edge\" of Open-Set Object Detection](https://arxiv.org/abs/2405.10300v2)",
      "c": "[&check;&nbsp;Link](https://github.com/mit-han-lab/efficientvit)",
      "n": "Grounding DINO 1.5 Pro",
      "d": "2024-05-16",
      "m1": "63.5",
      "m2": "64.0"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-H",
      "d": "2022-11-10",
      "m1": "63.2"
    },
    {
      "p": "[EVA: Exploring the Limits of Masked Visual Representation Learning at Scale](https://arxiv.org/abs/2211.07636v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EVA",
      "d": "2022-11-14",
      "m1": "62.2",
      "m2": "55.1"
    },
    {
      "p": "[Learning from Rich Semantics and Coarse Locations for Long-tailed Object Detection](https://arxiv.org/abs/2310.12152v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MengLcool/RichSem)",
      "n": "RichSem (Focal-H + ImageNet as weakly-supervised extra data)",
      "d": "2023-10-18",
      "m1": "61.2",
      "m2": "61.2"
    },
    {
      "p": "[General Object Foundation Model for Images and Videos at Scale](https://arxiv.org/abs/2312.09158v1)",
      "c": "[&check;&nbsp;Link](https://github.com/FoundationVision/GLEE)",
      "n": "GLEE-Pro",
      "d": "2023-12-14",
      "m1": "55.7"
    },
    {
      "p": "[Exploring Plain Vision Transformer Backbones for Object Detection](https://arxiv.org/abs/2203.16527v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/detectron2/tree/main/projects/ViTDet)",
      "n": "ViTDet-H",
      "d": "2022-03-30",
      "m1": "53.4"
    },
    {
      "p": "[SimLTD: Simple Supervised and Semi-Supervised Long-Tailed Object Detection](https://arxiv.org/abs/2412.20047v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lexisnexis-risk-open-source/simltd)",
      "n": "SimLTD w/MixPL (Swin-L + COCO unlabeled images)",
      "d": "2024-12-28",
      "m1": "51.5"
    },
    {
      "p": "[DiverGen: Improving Instance Segmentation by Learning Wider Data Distribution with More Diverse Generative Data](https://arxiv.org/abs/2405.10185v1)",
      "c": "[&check;&nbsp;Link](https://github.com/aim-uofa/DiverGen)",
      "n": "DiverGen (Swin-L)",
      "d": "2024-05-16",
      "m1": "51.2",
      "m2": "50.1"
    },
    {
      "p": "[Exploring Plain Vision Transformer Backbones for Object Detection](https://arxiv.org/abs/2203.16527v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/detectron2/tree/main/projects/ViTDet)",
      "n": "ViTDet-L",
      "d": "2022-03-30",
      "m1": "51.2"
    },
    {
      "p": "[X-Paste: Revisiting Scalable Copy-Paste for Instance Segmentation using CLIP and StableDiffusion](https://arxiv.org/abs/2212.03863v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aim-uofa/DiverGen)",
      "n": "CenterNet2 (Swin-L w/ X-Paste + Copy-Paste)",
      "d": "2022-12-07",
      "m1": "50.9",
      "m2": "48.7"
    },
    {
      "p": "[SimLTD: Simple Supervised and Semi-Supervised Long-Tailed Object Detection](https://arxiv.org/abs/2412.20047v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lexisnexis-risk-open-source/simltd)",
      "n": "SimLTD Fully Supervised (Swin-L)",
      "d": "2024-12-28",
      "m1": "49.8",
      "m2": "42.4"
    },
    {
      "p": "[Simple Copy-Paste is a Strong Data Augmentation Method for Instance Segmentation](https://arxiv.org/abs/2012.07177v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleOCR)",
      "n": "Eff-B7 NAS-FPN (1280, Copy-Paste pre-training))",
      "d": "2020-12-13",
      "m1": "41.6"
    },
    {
      "p": "[Exploring Classification Equilibrium in Long-Tailed Object Detection](https://arxiv.org/abs/2108.07507v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fcjian/loce)",
      "n": "R101-MaskRCNN-LOCE",
      "d": "2021-08-17",
      "m1": "29"
    },
    {
      "p": "[Exploring Classification Equilibrium in Long-Tailed Object Detection](https://arxiv.org/abs/2108.07507v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fcjian/loce)",
      "n": "R50-MaskRCNN-LOCE",
      "d": "2021-08-17",
      "m1": "27.4"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
