# scene-text-detection-on-scut-ctw1500

[Dataset Link](https://github.com/Yuliang-Liu/Curve-Text-Detector) \
Task Hierarchy: ['Scene Text Detection']

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
      "label": "F-Measure",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Precision",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Recall",
      "sortable": "true"
    },
    {
      "key": "m4",
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
      "p": "[MixNet: Toward Accurate Detection of Challenging Scene Text in the Wild](https://arxiv.org/abs/2308.12817v2)",
      "c": "[&check;&nbsp;Link](https://github.com/D641593/MixNet)",
      "n": "MixNet",
      "d": "2023-08-23",
      "m1": "89.8",
      "m2": "91.4",
      "m3": "88.3",
      "m4": "15.2"
    },
    {
      "p": "[SRFormer: Text Detection Transformer with Incorporated Segmentation and Regression](https://arxiv.org/abs/2308.10531v2)",
      "c": "[&check;&nbsp;Link](https://github.com/opendrivelab/elm)",
      "n": "SRFormer (ResNet-50)",
      "d": "2023-08-21",
      "m1": "89.6",
      "m2": "91.6",
      "m3": "87.7"
    },
    {
      "p": "[DPText-DETR: Towards Better Scene Text Detection with Dynamic Points in Transformer](https://arxiv.org/abs/2207.04491v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ymy-k/dptext-detr)",
      "n": "DPText-DETR (ResNet50)",
      "d": "2022-07-10",
      "m1": "88.8",
      "m2": "91.7",
      "m3": "86.2"
    },
    {
      "p": "[TextFuseNet: Scene Text Detection with Richer Fused Features](https://doi.org/10.24963/ijcai.2020/72)",
      "c": "[&check;&nbsp;Link](https://github.com/ying09/TextFuseNet)",
      "n": "TextFuseNet (ResNeXt-101)",
      "d": "2020-05-17",
      "m1": "87.4",
      "m2": "89.7",
      "m3": "85.1"
    },
    {
      "p": "[I3CL:Intra- and Inter-Instance Collaborative Learning for Arbitrary-shaped Scene Text Detection](https://arxiv.org/abs/2108.01343v3)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-scene-text-detection)",
      "n": "I3CL + SSL",
      "d": "2021-08-03",
      "m1": "86.5",
      "m2": "88.4",
      "m3": "84.6"
    },
    {
      "p": "[Mask R-CNN with Pyramid Attention Network for Scene Text Detection](http://arxiv.org/abs/1811.09058v1)",
      "c": "",
      "n": "PAN",
      "d": "2018-11-22",
      "m1": "85",
      "m2": "86.8",
      "m3": "83.2",
      "m4": "65.2"
    },
    {
      "p": "[FAST: Faster Arbitrarily-Shaped Text Detector with Minimalist Kernel Representation](https://arxiv.org/abs/2111.02394v2)",
      "c": "[&check;&nbsp;Link](https://github.com/whai362/pan_pp.pytorch)",
      "n": "FAST-B-640",
      "d": "2021-11-03",
      "m1": "84.2",
      "m2": "87.8",
      "m3": "80.9",
      "m4": "66.5"
    },
    {
      "p": "[Efficient and Accurate Arbitrary-Shaped Text Detection with Pixel Aggregation Network](https://arxiv.org/abs/1908.05900v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmocr)",
      "n": "PAN-640",
      "d": "2019-08-16",
      "m1": "83.7",
      "m2": "86.4",
      "m3": "81.2"
    },
    {
      "p": "[Character Region Awareness for Text Detection](http://arxiv.org/abs/1904.01941v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JaidedAI/EasyOCR)",
      "n": "CRAFT",
      "d": "2019-04-03",
      "m1": "83.5",
      "m2": "86",
      "m3": "81.1"
    },
    {
      "p": "[Real-time Scene Text Detection with Differentiable Binarization](https://arxiv.org/abs/1911.08947v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleOCR)",
      "n": "DB-ResNet50 (1024)",
      "d": "2019-11-20",
      "m1": "83.4"
    },
    {
      "p": "[FAST: Faster Arbitrarily-Shaped Text Detector with Minimalist Kernel Representation](https://arxiv.org/abs/2111.02394v2)",
      "c": "[&check;&nbsp;Link](https://github.com/whai362/pan_pp.pytorch)",
      "n": "FAST-B-512",
      "d": "2021-11-03",
      "m1": "82.9",
      "m2": "85.7",
      "m3": "80.2",
      "m4": "92.6"
    },
    {
      "p": "[Shape Robust Text Detection with Progressive Scale Expansion Network](https://arxiv.org/abs/1903.12473v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleOCR)",
      "n": "PSENet-1s",
      "d": "2019-03-28",
      "m1": "82.2",
      "m2": "84.8",
      "m3": "79.7"
    },
    {
      "p": "[FAST: Faster Arbitrarily-Shaped Text Detector with Minimalist Kernel Representation](https://arxiv.org/abs/2111.02394v2)",
      "c": "[&check;&nbsp;Link](https://github.com/whai362/pan_pp.pytorch)",
      "n": "FAST-S-512",
      "d": "2021-11-03",
      "m1": "82",
      "m2": "85.6",
      "m3": "78.7",
      "m4": "112.9"
    },
    {
      "p": "[FAST: Faster Arbitrarily-Shaped Text Detector with Minimalist Kernel Representation](https://arxiv.org/abs/2111.02394v2)",
      "c": "[&check;&nbsp;Link](https://github.com/whai362/pan_pp.pytorch)",
      "n": "FAST-T-512",
      "d": "2021-11-03",
      "m1": "81.5",
      "m2": "85.5",
      "m3": "77.9",
      "m4": "129.1"
    },
    {
      "p": "[Shape Robust Text Detection with Progressive Scale Expansion Network](http://arxiv.org/abs/1806.02559v1)",
      "c": "[&check;&nbsp;Link](https://github.com/whai362/PSENet)",
      "n": "PSENet-1s",
      "d": "2018-06-07",
      "m1": "81.17",
      "m2": "82.5",
      "m3": "79.89"
    },
    {
      "p": "[TextSnake: A Flexible Representation for Detecting Text of Arbitrary Shapes](https://arxiv.org/abs/1807.01544v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmocr)",
      "n": "TextSnake",
      "d": "2018-07-04",
      "m1": "75.6",
      "m2": "67.9",
      "m3": "85.3"
    },
    {
      "p": "[Sliding Line Point Regression for Shape Robust Scene Text Detection](http://arxiv.org/abs/1801.09969v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Shualite/UBNet)",
      "n": "SLPR",
      "d": "2018-01-30",
      "m1": "74.8",
      "m2": "80.1",
      "m3": "70.1"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
