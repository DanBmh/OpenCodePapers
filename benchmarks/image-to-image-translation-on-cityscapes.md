# image-to-image-translation-on-cityscapes

[Dataset Link](https://www.cityscapes-dataset.com/dataset-overview/) \
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
      "label": "mIoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "FID",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Class IOU",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Per-class Accuracy",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Per-pixel Accuracy",
      "sortable": "true"
    },
    {
      "key": "m7",
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
      "n": "DP-SIMS (ConvNext-L)",
      "d": "2023-12-20",
      "m1": "76.3",
      "m2": "38.2"
    },
    {
      "p": "[Dual Pyramid Generative Adversarial Networks for Semantic Image Synthesis](https://arxiv.org/abs/2210.04085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sj-li/dp_gan)",
      "n": "DP-GAN",
      "d": "2022-10-08",
      "m1": "73.6",
      "m2": "44.1"
    },
    {
      "p": "[You Only Need Adversarial Supervision for Semantic Image Synthesis](https://arxiv.org/abs/2012.04781v3)",
      "c": "[&check;&nbsp;Link](https://github.com/boschresearch/OASIS)",
      "n": "OASIS",
      "d": "2020-12-08",
      "m1": "69.3",
      "m2": "47.7",
      "m7": "0.275"
    },
    {
      "p": "[SESAME: Semantic Editing of Scenes by Adding, Manipulating or Erasing Objects](https://arxiv.org/abs/2004.04977v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vglsd/OpenSESAME)",
      "n": "SPADE + SESAME",
      "d": "2020-04-10",
      "m1": "66",
      "m2": "54.2",
      "m6": "82.5%"
    },
    {
      "p": "[Learning to Predict Layout-to-image Conditional Convolutions for Semantic Image Synthesis](https://arxiv.org/abs/1910.06809v3)",
      "c": "[&check;&nbsp;Link](https://github.com/xh-liu/CC-FPSE)",
      "n": "CC-FPSE",
      "d": "2019-10-15",
      "m1": "65.5",
      "m2": "54.3",
      "m6": "82.3%",
      "m7": "0.073"
    },
    {
      "p": "[Focal Frequency Loss for Image Reconstruction and Synthesis](https://arxiv.org/abs/2012.12821v3)",
      "c": "[&check;&nbsp;Link](https://github.com/EndlessSora/focal-frequency-loss)",
      "n": "SPADE + FFL",
      "d": "2020-12-23",
      "m1": "64.2",
      "m2": "59.5",
      "m6": "82.5%"
    },
    {
      "p": "[Improving Augmentation and Evaluation Schemes for Semantic Image Synthesis](https://arxiv.org/abs/2011.12636v3)",
      "c": "",
      "n": "CC-FPSE-AUG",
      "d": "2020-11-25",
      "m1": "63.1",
      "m2": "52.1",
      "m3": "93.5"
    },
    {
      "p": "[Semantic Image Synthesis with Spatially-Adaptive Normalization](https://arxiv.org/abs/1903.07291v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/SPADE)",
      "n": "SPADE",
      "d": "2019-03-18",
      "m1": "62.3",
      "m2": "71.8",
      "m6": "81.9%"
    },
    {
      "p": "[High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](http://arxiv.org/abs/1711.11585v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/pix2pixHD)",
      "n": "pix2pixHD",
      "d": "2017-11-30",
      "m1": "58.3",
      "m2": "95",
      "m6": "81.4%"
    },
    {
      "p": "[Improving Augmentation and Evaluation Schemes for Semantic Image Synthesis](https://arxiv.org/abs/2011.12636v3)",
      "c": "",
      "n": "Pix2PixHD-AUG",
      "d": "2020-11-25",
      "m1": "58",
      "m2": "72.7",
      "m3": "92.7"
    },
    {
      "p": "[Photographic Image Synthesis with Cascaded Refinement Networks](http://arxiv.org/abs/1707.09405v1)",
      "c": "",
      "n": "CRN",
      "d": "2017-07-28",
      "m1": "52.4",
      "m2": "104.7",
      "m6": "77.1%"
    },
    {
      "p": "[Semi-parametric Image Synthesis](http://arxiv.org/abs/1804.10992v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xjqicuhk/SIMS)",
      "n": "SIMS",
      "d": "2018-04-29",
      "m1": "47.2",
      "m2": "49.7",
      "m6": "75.5%"
    },
    {
      "p": "[USIS: Unsupervised Semantic Image Synthesis](https://arxiv.org/abs/2109.14715v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GeorgeEskandar/USIS-Unsupervised-Semantic-Image-Synthesis)",
      "n": "USIS",
      "d": "2021-09-29",
      "m1": "44.78",
      "m2": "53.67"
    },
    {
      "p": "[Wavelet-based Unsupervised Label-to-Image Translation](https://arxiv.org/abs/2305.09647v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GeorgeEskandar/USIS-Unsupervised-Semantic-Image-Synthesis)",
      "n": "USIS-Wavelet",
      "d": "2023-05-16",
      "m1": "42.32",
      "m2": "50.14"
    },
    {
      "p": "[Semantic Bottleneck Scene Generation](https://arxiv.org/abs/1911.11357v1)",
      "c": "[&check;&nbsp;Link](https://github.com/azadis/SB-GAN)",
      "n": "SB-GAN",
      "d": "2019-11-26",
      "m2": "60.39"
    },
    {
      "p": "[Image-to-Image Translation with Conditional Adversarial Networks](http://arxiv.org/abs/1611.07004v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/gan)",
      "n": "pix2pix",
      "d": "2016-11-21",
      "m4": "0.18",
      "m5": "25.0",
      "m6": "71.0",
      "m7": "0"
    },
    {
      "p": "[Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593v7)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "CycleGAN",
      "d": "2017-03-30",
      "m4": " 0.11",
      "m5": "17%",
      "m6": "52%"
    },
    {
      "p": "[Coupled Generative Adversarial Networks](http://arxiv.org/abs/1606.07536v2)",
      "c": "[&check;&nbsp;Link](https://github.com/eriklindernoren/PyTorch-GAN)",
      "n": "CoGAN",
      "d": "2016-06-24",
      "m4": "0.06",
      "m5": "10%",
      "m6": "40%"
    },
    {
      "p": "[Learning from Simulated and Unsupervised Images through Adversarial Training](http://arxiv.org/abs/1612.07828v2)",
      "c": "[&check;&nbsp;Link](https://github.com/carpedm20/simulated-unsupervised-tensorflow)",
      "n": "SimGAN",
      "d": "2016-12-22",
      "m4": "0.04",
      "m5": "10%",
      "m6": "20%"
    },
    {
      "p": "[Adversarially Learned Inference](http://arxiv.org/abs/1606.00704v3)",
      "c": "[&check;&nbsp;Link](https://github.com/MaximeVandegar/Papers-in-100-Lines-of-Code/tree/main/Adversarially_Learned_Inference)",
      "n": "BiGAN",
      "d": "2016-06-02",
      "m4": " 0.02",
      "m5": "6%",
      "m6": "19%"
    },
    {
      "p": "[Diverse Semantic Image Synthesis via Probability Distribution Modeling](https://arxiv.org/abs/2103.06878v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tzt101/INADE)",
      "n": "INADE",
      "d": "2021-03-11",
      "m7": "0.248"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
