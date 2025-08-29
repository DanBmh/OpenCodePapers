# semantic-segmentation-on-isprs-potsdam

[Dataset Link](https://www2.isprs.org/commissions/comm2/wg4/benchmark/2d-sem-label-potsdam/) \
Task Hierarchy: ['10-shot image generation', 'Semantic Segmentation']

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
      "label": "Overall Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Mean F1",
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
      "p": "[AerialFormer: Multi-resolution Transformer for Aerial Image Segmentation](https://arxiv.org/abs/2306.06842v2)",
      "c": "[&check;&nbsp;Link](https://github.com/UARK-AICV/AerialFormer)",
      "n": "AerialFormer-B",
      "d": "2023-06-12",
      "m1": "93.9",
      "m2": "94.1",
      "m3": "89.1"
    },
    {
      "p": "[A Billion-scale Foundation Model for Remote Sensing Images](https://arxiv.org/abs/2304.05215v4)",
      "c": "",
      "n": "ViT-G12X4",
      "d": "2023-04-11",
      "m1": "92.58",
      "m2": "92.12"
    },
    {
      "p": "[UNetFormer: A UNet-like Transformer for Efficient Semantic Segmentation of Remote Sensing Urban Scene Imagery](https://arxiv.org/abs/2109.08937v4)",
      "c": "[&check;&nbsp;Link](https://github.com/WangLibo1995/GeoSeg)",
      "n": "FT-UNetFormer",
      "d": "2021-09-18",
      "m1": "92.0",
      "m2": "93.3",
      "m3": "87.5"
    },
    {
      "p": "[A Novel Transformer Based Semantic Segmentation Scheme for Fine-Resolution Remote Sensing Images](https://arxiv.org/abs/2104.12137v6)",
      "c": "[&check;&nbsp;Link](https://github.com/WangLibo1995/GeoSeg)",
      "n": "DC-Swin",
      "d": "2021-04-25",
      "m1": "92.0",
      "m2": "93.25",
      "m3": "87.56"
    },
    {
      "p": "[LSKNet: A Foundation Lightweight Backbone for Remote Sensing](https://arxiv.org/abs/2403.11735v5)",
      "c": "[&check;&nbsp;Link](https://github.com/zcablii/lsknet)",
      "n": "LSKNet-S",
      "d": "2024-03-18",
      "m1": "92.0",
      "m2": "93.1",
      "m3": "87.2"
    },
    {
      "p": "[Semantic Labeling of High Resolution Images Using EfficientUNets and Transformers](https://arxiv.org/abs/2206.09731v2)",
      "c": "",
      "n": "EfficientUNets and Transformers",
      "d": "2022-06-20",
      "m1": "91.8",
      "m2": "93.7"
    },
    {
      "p": "[An Empirical Study of Remote Sensing Pretraining](https://arxiv.org/abs/2204.02825v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "IMP-ViTAEv2-S-UperNet",
      "d": "2022-04-06",
      "m1": "91.6"
    },
    {
      "p": "[Multiattention network for semantic segmentation of fine-resolution remote sensing images](https://ieeexplore.ieee.org/abstract/document/9487010)",
      "c": "[&check;&nbsp;Link](https://github.com/lironui/Multi-Attention-Network)",
      "n": "MANet",
      "d": "2021-05-15",
      "m1": "91.318"
    },
    {
      "p": "[UNetFormer: A UNet-like Transformer for Efficient Semantic Segmentation of Remote Sensing Urban Scene Imagery](https://arxiv.org/abs/2109.08937v4)",
      "c": "[&check;&nbsp;Link](https://github.com/WangLibo1995/GeoSeg)",
      "n": "UNetFormer",
      "d": "2021-09-18",
      "m1": "91.3",
      "m2": "92.8",
      "m3": "86.8"
    },
    {
      "p": "[ABCNet: Attentive Bilateral Contextual Network for Efficient Semantic Segmentation of Fine-Resolution Remote Sensing Images](https://arxiv.org/abs/2102.02531v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lironui/ABCNet)",
      "n": "ABCNet",
      "d": "2021-02-04",
      "m1": "91.3"
    },
    {
      "p": "[Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model](https://arxiv.org/abs/2208.03987v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "ViTAE-B + RVSA -UperNet",
      "d": "2022-08-08",
      "m1": "91.22"
    },
    {
      "p": "[An Empirical Study of Remote Sensing Pretraining](https://arxiv.org/abs/2204.02825v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "RSP-ViTAEv2-S-UperNet",
      "d": "2022-04-06",
      "m1": "91.21"
    },
    {
      "p": "[Transformer Meets Convolution: A Bilateral Awareness Network for Semantic Segmentation of Very Fine Resolution Urban Scene Images](https://arxiv.org/abs/2106.12413v2)",
      "c": "[&check;&nbsp;Link](https://github.com/WangLibo1995/GeoSeg)",
      "n": "BANet",
      "d": "2021-06-23",
      "m1": "91.06"
    },
    {
      "p": "[An Empirical Study of Remote Sensing Pretraining](https://arxiv.org/abs/2204.02825v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "RSP-Swin-T-UperNet",
      "d": "2022-04-06",
      "m1": "90.78"
    },
    {
      "p": "[Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model](https://arxiv.org/abs/2208.03987v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "ViT-B + RVSA-UperNet",
      "d": "2022-08-08",
      "m1": "90.77"
    },
    {
      "p": "[An Empirical Study of Remote Sensing Pretraining](https://arxiv.org/abs/2204.02825v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vitae-transformer/vitae-transformer-remote-sensing)",
      "n": "RSP-ResNet-50-UperNet",
      "d": "2022-04-06",
      "m1": "90.61"
    },
    {
      "p": "[Stochastic Subsampling With Average Pooling](https://arxiv.org/abs/2409.16630v1)",
      "c": "",
      "n": "PSPNet (SAP)",
      "d": "2024-09-25",
      "m1": "88.56",
      "m3": "74.3"
    },
    {
      "p": "[Dynamic Dictionary Learning for Remote Sensing Image Segmentation](https://arxiv.org/abs/2503.06683v1)",
      "c": "[&check;&nbsp;Link](https://github.com/XavierJiezou/D2LS)",
      "n": "D2LS",
      "d": "2025-03-09",
      "m2": "94.7"
    },
    {
      "p": "[SFA-Net: Semantic Feature Adjustment Network for Remote Sensing Image Segmentation](https://www.mdpi.com/2072-4292/16/17/3278)",
      "c": "[&check;&nbsp;Link](https://github.com/j2jeong/priv)",
      "n": "SFA-Net",
      "d": "2024-09-03",
      "m2": "93.5"
    },
    {
      "p": "[U-Net Ensemble for Enhanced Semantic Segmentation in Remote Sensing Imagery](https://www.mdpi.com/2072-4292/16/12/2077)",
      "c": "",
      "n": "U-Net (ConvFormer-M36)",
      "d": "2024-06-08",
      "m3": "89.45"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
