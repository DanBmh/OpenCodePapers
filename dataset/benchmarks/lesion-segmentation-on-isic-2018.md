# lesion-segmentation-on-isic-2018

[Dataset Link]() \
Task Hierarchy: ['Medical Image Segmentation', 'Lesion Segmentation']

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
      "label": "mean Dice",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "F1-Score",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Mean IoU",
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
      "p": "[Training on Polar Image Transformations Improves Biomedical Image Segmentation](https://ieeexplore.ieee.org/document/9551998)",
      "c": "[&check;&nbsp;Link](https://github.com/marinbenc/medical-polar-training)",
      "n": "Polar Res-U-Net++",
      "d": "2021-09-29",
      "m1": "0.9253"
    },
    {
      "p": "[DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation](https://arxiv.org/abs/2212.11677v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Barrett-python/DuAT)",
      "n": "DuAT",
      "d": "2022-12-21",
      "m1": "0.923",
      "m3": "0.867"
    },
    {
      "p": "[ProMISe: Promptable Medical Image Segmentation using SAM](https://arxiv.org/abs/2403.04164v3)",
      "c": "[&check;&nbsp;Link](https://github.com/xinkunwang111/promise)",
      "n": "ProMISe",
      "d": "2024-03-07",
      "m1": "0.921",
      "m3": "0.850"
    },
    {
      "p": "[Automated skin lesion segmentation using multi-scale feature extraction scheme and dual-attention mechanism](https://arxiv.org/abs/2111.08708v3)",
      "c": "",
      "n": "RMSM UNet + DF-RAM +EF-RAM",
      "d": "2021-11-16",
      "m1": "0.9152"
    },
    {
      "p": "[Boundary-aware Transformers for Skin Lesion Segmentation](https://arxiv.org/abs/2110.03864v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jcwang123/BA-Transformer)",
      "n": "BAT",
      "d": "2021-10-08",
      "m1": "0.912",
      "m3": "0.843"
    },
    {
      "p": "[From Semantic Segmentation of Natural Images to Medical Image Segmentation Using ViT-Based Architectures](https://link.springer.com/chapter/10.1007/978-3-031-80507-3_12)",
      "c": "",
      "n": "SegMed",
      "d": "2025-01-31",
      "m1": "0.911",
      "m3": "0.841"
    },
    {
      "p": "[MobileUNETR: A Lightweight End-To-End Hybrid Vision Transformer For Efficient Medical Image Segmentation](https://arxiv.org/abs/2409.03062v1)",
      "c": "[&check;&nbsp;Link](https://github.com/osupcvlab/mobileunetr)",
      "n": "MobileUNETR",
      "d": "2024-09-04",
      "m1": "0.9074",
      "m3": "0.8456"
    },
    {
      "p": "[DermoSegDiff: A Boundary-aware Segmentation Diffusion Model for Skin Lesion Delineation](https://arxiv.org/abs/2308.02959v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mindflow-institue/dermosegdiff)",
      "n": "DermoSegDiff-A",
      "d": "2023-08-05",
      "m1": "0.9005"
    },
    {
      "p": "[DoubleU-Net: A Deep Convolutional Neural Network for Medical Image Segmentation](https://arxiv.org/abs/2006.04868v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DebeshJha/2020-CBMS-DoubleU-Net)",
      "n": "DoubleU-Net",
      "d": "2020-06-08",
      "m1": "0.8962"
    },
    {
      "p": "[Multi-level Context Gating of Embedded Collective Knowledge for Medical Image Segmentation](https://arxiv.org/abs/2003.05056v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rezazad68/BCDU-Net)",
      "n": "MCGU-Net",
      "d": "2020-03-10",
      "m1": "0.895"
    },
    {
      "p": "[MSRF-Net: A Multi-Scale Residual Fusion Network for Biomedical Image Segmentation](https://arxiv.org/abs/2105.07451v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NoviceMAn-prog/MSRF-Net)",
      "n": "MSRF-Net",
      "d": "2021-05-16",
      "m1": "0.8813"
    },
    {
      "p": "[A Novel Focal Tversky loss function with improved Attention U-Net for lesion segmentation](http://arxiv.org/abs/1810.07842v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nabsabraham/focal-tversky-unet)",
      "n": "Attn U-Net + Multi-Input + FTL",
      "d": "2018-10-18",
      "m1": "0.856"
    },
    {
      "p": "[Inconsistency Masks: Removing the Uncertainty from Input-Pseudo-Label Pairs](https://arxiv.org/abs/2401.14387v2)",
      "c": "[&check;&nbsp;Link](https://github.com/michaelvorndran/inconsistencymasks)",
      "n": "AIM++ (256x256, 1.5m parameters, 10% labeled data, no pretraining)",
      "d": "2024-01-25",
      "m1": "0.85"
    },
    {
      "p": "[Bi-Directional ConvLSTM U-Net with Densley Connected Convolutions](https://arxiv.org/abs/1909.00166v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rezazad68/BCDU-Net)",
      "n": "BCDU-net",
      "d": "2019-08-31",
      "m1": "0.847"
    },
    {
      "p": "[A Novel Focal Tversky loss function with improved Attention U-Net for lesion segmentation](http://arxiv.org/abs/1810.07842v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nabsabraham/focal-tversky-unet)",
      "n": "U-Net + FTL",
      "d": "2018-10-18",
      "m1": "0.829"
    },
    {
      "p": "[A Novel Focal Tversky loss function with improved Attention U-Net for lesion segmentation](http://arxiv.org/abs/1810.07842v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nabsabraham/focal-tversky-unet)",
      "n": "Attn U-Net + DL",
      "d": "2018-10-18",
      "m1": "0.806"
    },
    {
      "p": "[Bi-Directional ConvLSTM U-Net with Densley Connected Convolutions](https://arxiv.org/abs/1909.00166v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rezazad68/BCDU-Net)",
      "n": "BCDU-Net (d=3)",
      "d": "2019-08-31",
      "m2": "0.851"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
