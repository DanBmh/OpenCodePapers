# image-to-image-translation-on-coco-stuff

[Dataset Link](https://github.com/nightrome/cocostuff) \
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
      "label": "FID",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "mIoU",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "LPIPS",
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
      "p": "[Unlocking Pre-trained Image Backbones for Semantic Image Synthesis](https://arxiv.org/abs/2312.13314v2)",
      "c": "",
      "n": "DP-SIMS (ConvNext-XL)",
      "d": "2023-12-20",
      "m1": "13.3"
    },
    {
      "p": "[Unlocking Pre-trained Image Backbones for Semantic Image Synthesis](https://arxiv.org/abs/2312.13314v2)",
      "c": "",
      "n": "DP-SIMS (ConvNext-L)",
      "d": "2023-12-20",
      "m1": "13.6"
    },
    {
      "p": "[Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis](https://arxiv.org/abs/2402.16506v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/scdm)",
      "n": "SCDM",
      "d": "2024-02-26",
      "m1": "15.3",
      "m3": "38.1",
      "m4": "0.519"
    },
    {
      "p": "[Pretraining is All You Need for Image-to-Image Translation](https://arxiv.org/abs/2205.12952v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PITI-Synthesis/PITI)",
      "n": "PITI",
      "d": "2022-05-25",
      "m1": "15.6"
    },
    {
      "p": "[Multimodal Conditional Image Synthesis with Product-of-Experts GANs](https://arxiv.org/abs/2112.05130v1)",
      "c": "",
      "n": "PoE-GAN",
      "d": "2021-12-09",
      "m1": "15.8"
    },
    {
      "p": "[You Only Need Adversarial Supervision for Semantic Image Synthesis](https://arxiv.org/abs/2012.04781v3)",
      "c": "[&check;&nbsp;Link](https://github.com/boschresearch/OASIS)",
      "n": "OASIS",
      "d": "2020-12-08",
      "m1": "17.0",
      "m3": "44.1"
    },
    {
      "p": "[Improving Augmentation and Evaluation Schemes for Semantic Image Synthesis](https://arxiv.org/abs/2011.12636v3)",
      "c": "",
      "n": "CC-FPSE-AUG",
      "d": "2020-11-25",
      "m1": "19.1",
      "m2": "71.5",
      "m3": "42.1"
    },
    {
      "p": "[Learning to Predict Layout-to-image Conditional Convolutions for Semantic Image Synthesis](https://arxiv.org/abs/1910.06809v3)",
      "c": "[&check;&nbsp;Link](https://github.com/xh-liu/CC-FPSE)",
      "n": "CC-FPSE",
      "d": "2019-10-15",
      "m1": "19.2",
      "m2": "70.7%",
      "m3": "41.6"
    },
    {
      "p": "[Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841v3)",
      "c": "[&check;&nbsp;Link](https://github.com/CompVis/taming-transformers)",
      "n": "VQGAN+Transformer",
      "d": "2020-12-17",
      "m1": "22.4"
    },
    {
      "p": "[Semantic Image Synthesis with Spatially-Adaptive Normalization](https://arxiv.org/abs/1903.07291v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/SPADE)",
      "n": "SPADE",
      "d": "2019-03-18",
      "m1": "22.6",
      "m2": "67.9%",
      "m3": "37.4"
    },
    {
      "p": "[USIS: Unsupervised Semantic Image Synthesis](https://arxiv.org/abs/2109.14715v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GeorgeEskandar/USIS-Unsupervised-Semantic-Image-Synthesis)",
      "n": "USIS",
      "d": "2021-09-29",
      "m1": "27.8",
      "m3": "14.06"
    },
    {
      "p": "[Wavelet-based Unsupervised Label-to-Image Translation](https://arxiv.org/abs/2305.09647v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GeorgeEskandar/USIS-Unsupervised-Semantic-Image-Synthesis)",
      "n": "USIS-Wavelet",
      "d": "2023-05-16",
      "m1": "28.6",
      "m3": "13.4"
    },
    {
      "p": "[Improving Augmentation and Evaluation Schemes for Semantic Image Synthesis](https://arxiv.org/abs/2011.12636v3)",
      "c": "",
      "n": "Pix2PixHD-AUG",
      "d": "2020-11-25",
      "m1": "54.2",
      "m2": "54.1",
      "m3": "21.9"
    },
    {
      "p": "[Photographic Image Synthesis with Cascaded Refinement Networks](http://arxiv.org/abs/1707.09405v1)",
      "c": "",
      "n": "CRN",
      "d": "2017-07-28",
      "m1": "70.4",
      "m2": "40.4%",
      "m3": "23.7"
    },
    {
      "p": "[High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](http://arxiv.org/abs/1711.11585v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/pix2pixHD)",
      "n": "pix2pixHD",
      "d": "2017-11-30",
      "m1": "111.5",
      "m2": "45.8%",
      "m3": "14.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
