# conditional-image-generation-on-cifar-10

[Dataset Link](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf) \
Task Hierarchy: ['Conditional Image Generation']

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
      "label": "Inception score",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Intra-FID",
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
      "p": "[Refining Generative Process with Discriminator Guidance in Score-based Diffusion Models](https://arxiv.org/abs/2211.17091v4)",
      "c": "[&check;&nbsp;Link](https://github.com/alsdudrla10/DG)",
      "n": "EDM-G++ (conditional)",
      "d": "2022-11-28",
      "m1": "1.64"
    },
    {
      "p": "[Denoising Likelihood Score Matching for Conditional Score-based Data Generation](https://arxiv.org/abs/2203.14206v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chen-hao-chao/dlsm)",
      "n": "DLSM",
      "d": "2022-03-27",
      "m1": "2.25",
      "m2": "9.90"
    },
    {
      "p": "[Rebooting ACGAN: Auxiliary Classifier GANs with Stable Training](https://arxiv.org/abs/2111.01118v1)",
      "c": "[&check;&nbsp;Link](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)",
      "n": "StyleGAN2 + DiffAugment + D2D-CE",
      "d": "2021-11-01",
      "m1": "2.26",
      "m2": "10.51"
    },
    {
      "p": "[Training Generative Adversarial Networks with Limited Data](https://arxiv.org/abs/2006.06676v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/stylegan2-ada-pytorch)",
      "n": "StyleGAN2-ADA",
      "d": "2020-06-11",
      "m1": "2.42",
      "m2": "10.14"
    },
    {
      "p": "[Lessons Learned from the Training of GANs on Artificial Datasets](https://arxiv.org/abs/2007.06418v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tsc2017/MIX-GAN)",
      "n": "MIX-MHingeGAN",
      "d": "2020-07-13",
      "m1": "3.6",
      "m2": "10.21"
    },
    {
      "p": "[Feature Quantization Improves GAN Training](https://arxiv.org/abs/2004.02088v2)",
      "c": "[&check;&nbsp;Link](https://github.com/YangNaruto/FQ-GAN)",
      "n": "FQ-GAN",
      "d": "2020-04-05",
      "m1": "5.34",
      "m2": "8.50"
    },
    {
      "p": "[Conditional GANs with Auxiliary Discriminative Classifier](https://arxiv.org/abs/2107.10060v5)",
      "c": "[&check;&nbsp;Link](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)",
      "n": "ADC-GAN",
      "d": "2021-07-21",
      "m1": "5.66",
      "m3": "40.45"
    },
    {
      "p": "[Adaptive Weighted Discriminator for Training Generative Adversarial Networks](https://arxiv.org/abs/2012.03149v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vasily789/adaptive-weighted-gans)",
      "n": "aw-BigGAN",
      "d": "2020-12-05",
      "m1": "6.89",
      "m2": "9.52"
    },
    {
      "p": "[cGANs with Multi-Hinge Loss](https://arxiv.org/abs/1912.04216v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ilyakava/BigGAN-PyTorch)",
      "n": "MHingeGAN",
      "d": "2019-12-09",
      "m1": "7.5",
      "m2": "9.58"
    },
    {
      "p": "[Adaptive Weighted Discriminator for Training Generative Adversarial Networks](https://arxiv.org/abs/2012.03149v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vasily789/adaptive-weighted-gans)",
      "n": "aw-SN-GAN",
      "d": "2020-12-05",
      "m1": "8.03",
      "m2": "9"
    },
    {
      "p": "[Negative Data Augmentation](https://arxiv.org/abs/2102.05113v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ermongroup/NDA)",
      "n": "NDA",
      "d": "2021-02-09",
      "m1": "9.42"
    },
    {
      "p": "[ContraGAN: Contrastive Learning for Conditional Image Generation](https://arxiv.org/abs/2006.12681v3)",
      "c": "[&check;&nbsp;Link](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)",
      "n": "ContraGAN",
      "d": "2020-06-23",
      "m1": "10.30"
    },
    {
      "p": "[Consistency Regularization for Generative Adversarial Networks](https://arxiv.org/abs/1910.12027v2)",
      "c": "",
      "n": "CR-BigGAN",
      "d": "2019-10-26",
      "m1": "11.67"
    },
    {
      "p": "[Large Scale GAN Training for High Fidelity Natural Image Synthesis](http://arxiv.org/abs/1809.11096v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ajbrock/BigGAN-PyTorch)",
      "n": "BigGAN",
      "d": "2018-09-28",
      "m1": "14.73",
      "m2": "9.22"
    },
    {
      "p": "[cGANs with Projection Discriminator](http://arxiv.org/abs/1802.05637v2)",
      "c": "[&check;&nbsp;Link](https://github.com/pfnet-research/sngan_projection)",
      "n": "Projection Discriminator",
      "d": "2018-02-15",
      "m1": "17.5",
      "m2": "8.62"
    },
    {
      "p": "[Deep Polynomial Neural Networks](https://arxiv.org/abs/2006.13026v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Faceplugin-ltd/FaceRecognition-Android)",
      "n": "ProdPoly no activation functions",
      "d": "2020-06-20",
      "m1": "36.77",
      "m2": "7.5"
    },
    {
      "p": "[Class-Splitting Generative Adversarial Networks](http://arxiv.org/abs/1709.07359v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CIFASIS/splitting_gan)",
      "n": "Splitting GAN",
      "d": "2017-09-21",
      "m2": "8.87"
    },
    {
      "p": "[Improved Training of Wasserstein GANs](http://arxiv.org/abs/1704.00028v3)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "WGAN-GP",
      "d": "2017-03-31",
      "m2": "8.67"
    },
    {
      "p": "[Stacked Generative Adversarial Networks](http://arxiv.org/abs/1612.04357v4)",
      "c": "[&check;&nbsp;Link](https://github.com/xunhuang1995/SGAN)",
      "n": "SGAN",
      "d": "2016-12-13",
      "m2": "8.59"
    },
    {
      "p": "[Conditional Image Synthesis With Auxiliary Classifier GANs](http://arxiv.org/abs/1610.09585v4)",
      "c": "[&check;&nbsp;Link](https://github.com/eriklindernoren/PyTorch-GAN)",
      "n": "AC-GAN",
      "d": "2016-10-30",
      "m2": "8.25"
    },
    {
      "p": "[Improved Techniques for Training GANs](http://arxiv.org/abs/1606.03498v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/gan)",
      "n": "Improved GAN",
      "d": "2016-06-10",
      "m2": "8.09"
    },
    {
      "p": "[LR-GAN: Layered Recursive Generative Adversarial Networks for Image Generation](http://arxiv.org/abs/1703.01560v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jwyang/lr-gan.pytorch)",
      "n": "LR-GAN",
      "d": "2017-03-05",
      "m2": "7.17"
    },
    {
      "p": "[Calibrating Energy-based Generative Adversarial Networks](http://arxiv.org/abs/1702.01691v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zihangdai/cegan_iclr2017)",
      "n": "EGAN-Ent-VI",
      "d": "2017-02-06",
      "m2": "7.07"
    },
    {
      "p": "[Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](http://arxiv.org/abs/1511.06434v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/blob/master/research/slim/nets/dcgan.py)",
      "n": "DCGAN",
      "d": "2015-11-19",
      "m2": "6.58"
    },
    {
      "p": "[Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning](http://arxiv.org/abs/1611.01722v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DartML/SteinGAN)",
      "n": "SteinGAN",
      "d": "2016-11-06",
      "m2": "6.35"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
