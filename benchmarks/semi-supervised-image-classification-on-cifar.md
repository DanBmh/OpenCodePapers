# semi-supervised-image-classification-on-cifar

[Dataset Link](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf) \
Task Hierarchy: ['Semi-Supervised Image Classification']

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
      "label": "Percentage error",
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
      "p": "[SST: Self-training with Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2506.00467v1)",
      "c": "",
      "n": "Semi-SST (ViT-Small)",
      "d": "2025-05-31",
      "m1": "1.41\u00b10.10"
    },
    {
      "p": "[SST: Self-training with Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2506.00467v1)",
      "c": "",
      "n": "Super-SST (ViT-Small)",
      "d": "2025-05-31",
      "m1": "1.61\u00b10.18"
    },
    {
      "p": "[Diff-SySC: An Approach Using Diffusion Models for Semi-Supervised Image Classification](https://www.scitepress.org/PublicationsDetail.aspx?ID=8MzrzMi7kMs%3d&t=1)",
      "c": "",
      "n": "Diff-SySC",
      "d": "2025-02-25",
      "m1": "3.26\u00b10.06"
    },
    {
      "p": "[All Labels Are Not Created Equal: Enhancing Semi-supervision via Label Grouping and Co-training](https://arxiv.org/abs/2104.05248v1)",
      "c": "[&check;&nbsp;Link](https://github.com/islam-nassar/semco)",
      "n": "SemCo (\u03bc=7)",
      "d": "2021-04-12",
      "m1": "3.8\u00b10.08"
    },
    {
      "p": "[Meta Pseudo Labels](https://arxiv.org/abs/2003.10580v4)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/meta_pseudo_labels)",
      "n": "Meta Pseudo Labels (WRN-28-2)",
      "d": "2020-03-23",
      "m1": "3.89\u00b1 0.07"
    },
    {
      "p": "[SimMatch: Semi-supervised Learning with Similarity Matching](https://arxiv.org/abs/2203.06915v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kylezheng1997/simmatch)",
      "n": "SimMatch",
      "d": "2022-03-14",
      "m1": "3.96"
    },
    {
      "p": "[Semi-Supervised Learning of Visual Features by Non-Parametrically Predicting View Assignments with Support Samples](https://arxiv.org/abs/2104.13963v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/suncet)",
      "n": "PAWS-NN (WRN-28-2)",
      "d": "2021-04-28",
      "m1": "4.0 \u00b1 0.25"
    },
    {
      "p": "[SelfMatch: Combining Contrastive Self-Supervision and Consistency for Semi-Supervised Learning](https://arxiv.org/abs/2101.06480v1)",
      "c": "",
      "n": "SelfMatch",
      "d": "2021-01-16",
      "m1": "4.06\u00b10.08"
    },
    {
      "p": "[Dash: Semi-Supervised Learning with Dynamic Thresholding](https://arxiv.org/abs/2109.00650v1)",
      "c": "",
      "n": "Dash (RA, ours)",
      "d": "2021-09-01",
      "m1": "4.08\u00b10.06"
    },
    {
      "p": "[Self Meta Pseudo Labels: Meta Pseudo Labels Without The Teacher](https://arxiv.org/abs/2212.13420v1)",
      "c": "",
      "n": "Self Meta Pseudo Labels",
      "d": "2022-12-27",
      "m1": "4.09"
    },
    {
      "p": "[NP-Match: When Neural Processes meet Semi-Supervised Learning](https://arxiv.org/abs/2207.01066v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jianf-wang/np-match)",
      "n": "NP-Match",
      "d": "2022-07-03",
      "m1": "4.11\u00b10.02"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "FixMatch+DM",
      "d": null,
      "m1": "4.13\u00b10.11"
    },
    {
      "p": "[Contrastive Regularization for Semi-Supervised Learning](https://arxiv.org/abs/2201.06247v2)",
      "c": "",
      "n": "FixMatch+CR",
      "d": "2022-01-17",
      "m1": "4.16"
    },
    {
      "p": "[EnAET: A Self-Trained framework for Semi-Supervised and Supervised Learning with Ensemble Transformations](https://arxiv.org/abs/1911.09265v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maple-research-lab/EnAET)",
      "n": "EnAET",
      "d": "2019-11-21",
      "m1": "4.18"
    },
    {
      "p": "[FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo Labeling](https://arxiv.org/abs/2110.08263v3)",
      "c": "[&check;&nbsp;Link](https://github.com/torchssl/torchssl)",
      "n": "FlexMatch",
      "d": "2021-10-15",
      "m1": "4.19\u00b10.01"
    },
    {
      "p": "[DP-SSL: Towards Robust Semi-supervised Learning with A Few Labeled Samples](https://arxiv.org/abs/2110.13740v1)",
      "c": "",
      "n": "DP-SSL",
      "d": "2021-10-26",
      "m1": "4.23\u00b10.20"
    },
    {
      "p": "[NP-Match: When Neural Processes meet Semi-Supervised Learning](https://arxiv.org/abs/2207.01066v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jianf-wang/np-match)",
      "n": "UPS (wrn-28-2)",
      "d": "2022-07-03",
      "m1": "4.25"
    },
    {
      "p": "[FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence](https://arxiv.org/abs/2001.07685v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/fixmatch)",
      "n": "FixMatch (CTA)",
      "d": "2020-01-21",
      "m1": "4.31"
    },
    {
      "p": "[LaplaceNet: A Hybrid Graph-Energy Neural Network for Deep Semi-Supervised Classification](https://arxiv.org/abs/2106.04527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/psellcam/LaplaceNet)",
      "n": "LaplaceNet (WRN-28-2)",
      "d": "2021-06-08",
      "m1": "4.35\u00b10.10"
    },
    {
      "p": "[DoubleMatch: Improving Semi-Supervised Learning with Self-Supervision](https://arxiv.org/abs/2205.05575v1)",
      "c": "[&check;&nbsp;Link](https://github.com/walline/doublematch)",
      "n": "DoubleMatch",
      "d": "2022-05-11",
      "m1": "4.65\u00b10.17"
    },
    {
      "p": "[In Defense of Pseudo-Labeling: An Uncertainty-Aware Pseudo-label Selection Framework for Semi-Supervised Learning](https://arxiv.org/abs/2101.06329v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nayeemrizve/ups)",
      "n": "UPS (Shake-Shake)",
      "d": "2021-01-15",
      "m1": "4.86"
    },
    {
      "p": "[LaplaceNet: A Hybrid Graph-Energy Neural Network for Deep Semi-Supervised Classification](https://arxiv.org/abs/2106.04527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/psellcam/LaplaceNet)",
      "n": "LaplaceNet (CNN-13)",
      "d": "2021-06-08",
      "m1": "4.99\u00b10.08"
    },
    {
      "p": "[There Are Many Consistent Explanations of Unlabeled Data: Why You Should Average](http://arxiv.org/abs/1806.05594v3)",
      "c": "[&check;&nbsp;Link](https://github.com/benathi/fastswa-semi-sup)",
      "n": "SWSA",
      "d": "2018-06-14",
      "m1": "5"
    },
    {
      "p": "[ReMixMatch: Semi-Supervised Learning with Distribution Alignment and Augmentation Anchoring](https://arxiv.org/abs/1911.09785v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/mixmatch)",
      "n": "ReMixMatch",
      "d": "2019-11-21",
      "m1": "5.14"
    },
    {
      "p": "[Unsupervised Data Augmentation for Consistency Training](https://arxiv.org/abs/1904.12848v6)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/uda)",
      "n": "UDA",
      "d": "2019-04-29",
      "m1": "5.27"
    },
    {
      "p": "[Repetitive Reprediction Deep Decipher for Semi-Supervised Learning](https://arxiv.org/abs/1908.04345v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DoctorKey/R2D2.pytorch)",
      "n": "R2-D2 (Shake-Shake)",
      "d": "2019-08-09",
      "m1": "5.72"
    },
    {
      "p": "[DMT: Dynamic Mutual Training for Semi-Supervised Learning](https://arxiv.org/abs/2004.08514v4)",
      "c": "[&check;&nbsp;Link](https://github.com/voldemortX/DST-CBC)",
      "n": "DMT (WRN-28-2)",
      "d": "2020-04-18",
      "m1": "5.79"
    },
    {
      "p": "[Adaptive Boosting for Domain Adaptation: Towards Robust Predictions in Scene Segmentation](https://arxiv.org/abs/2103.15685v3)",
      "c": "[&check;&nbsp;Link](https://github.com/layumi/AdaBoost_Seg)",
      "n": "Adaboost",
      "d": "2021-03-29",
      "m1": "6.05\u00b10.12"
    },
    {
      "p": "[SHOT-VAE: Semi-supervised Deep Generative Models With Label-aware ELBO Approximations](https://arxiv.org/abs/2011.10684v4)",
      "c": "[&check;&nbsp;Link](https://github.com/FengHZ/AAAI2021-260)",
      "n": "SHOT-VAE",
      "d": "2020-11-21",
      "m1": "6.11"
    },
    {
      "p": "[MixMatch: A Holistic Approach to Semi-Supervised Learning](https://arxiv.org/abs/1905.02249v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/mixmatch)",
      "n": "MixMatch",
      "d": "2019-05-06",
      "m1": "6.24"
    },
    {
      "p": "[Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results](http://arxiv.org/abs/1703.01780v6)",
      "c": "[&check;&nbsp;Link](https://github.com/CuriousAI/mean-teacher)",
      "n": "Mean Teacher",
      "d": "2017-03-06",
      "m1": "6.28"
    },
    {
      "p": "[RealMix: Towards Realistic Semi-Supervised Deep Learning Algorithms](https://arxiv.org/abs/1912.08766v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uizard-technologies/realmix)",
      "n": "RealMix",
      "d": "2019-12-18",
      "m1": "6.38"
    },
    {
      "p": "[In Defense of Pseudo-Labeling: An Uncertainty-Aware Pseudo-label Selection Framework for Semi-Supervised Learning](https://arxiv.org/abs/2101.06329v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nayeemrizve/ups)",
      "n": "UPS (CNN-13)",
      "d": "2021-01-15",
      "m1": "6.39\u00b10.02"
    },
    {
      "p": "[Triple Generative Adversarial Networks](https://arxiv.org/abs/1912.09784v2)",
      "c": "[&check;&nbsp;Link](https://github.com/taufikxu/Triple-GAN)",
      "n": "Triple-GAN-V2 (ResNet-26)",
      "d": "2019-12-20",
      "m1": "6.54"
    },
    {
      "p": "[Interpolation Consistency Training for Semi-Supervised Learning](https://arxiv.org/abs/1903.03825v5)",
      "c": "[&check;&nbsp;Link](https://github.com/vikasverma1077/ICT)",
      "n": "ICT (CNN-13)",
      "d": "2019-03-09",
      "m1": "7.29"
    },
    {
      "p": "[LiDAM: Semi-Supervised Learning with Localized Domain Adaptation and Iterative Matching](https://arxiv.org/abs/2010.06668v2)",
      "c": "",
      "n": "LiDAM",
      "d": "2020-10-13",
      "m1": "7.48"
    },
    {
      "p": "[Interpolation Consistency Training for Semi-Supervised Learning](https://arxiv.org/abs/1903.03825v5)",
      "c": "[&check;&nbsp;Link](https://github.com/vikasverma1077/ICT)",
      "n": "ICT (WRN-28-2)",
      "d": "2019-03-09",
      "m1": "7.66"
    },
    {
      "p": "[Semi-Supervised Learning by Augmented Distribution Alignment](https://arxiv.org/abs/1905.08171v2)",
      "c": "[&check;&nbsp;Link](https://github.com/qinenergy/adanet)",
      "n": "ADA-Net (ConvNet)",
      "d": "2019-05-20",
      "m1": "8.72"
    },
    {
      "p": "[Dual Student: Breaking the Limits of the Teacher in Semi-supervised Learning](https://arxiv.org/abs/1909.01804v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ZHKKKe/DualStudent)",
      "n": "Dual Student (600)",
      "d": "2019-09-03",
      "m1": "8.89"
    },
    {
      "p": "[Triple Generative Adversarial Networks](https://arxiv.org/abs/1912.09784v2)",
      "c": "[&check;&nbsp;Link](https://github.com/taufikxu/Triple-GAN)",
      "n": "Triple-GAN-V2 (CNN-13)",
      "d": "2019-12-20",
      "m1": "10.01"
    },
    {
      "p": "[Virtual Adversarial Training: A Regularization Method for Supervised and Semi-Supervised Learning](http://arxiv.org/abs/1704.03976v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/neural-structured-learning)",
      "n": "VAT+EntMin",
      "d": "2017-04-13",
      "m1": "10.55"
    },
    {
      "p": "[Global-Local Regularization Via Distributional Robustness](https://arxiv.org/abs/2203.00553v3)",
      "c": "[&check;&nbsp;Link](https://github.com/viethoang1512/glot)",
      "n": "GLOT-DR",
      "d": "2022-03-01",
      "m1": "10.6"
    },
    {
      "p": "[Virtual Adversarial Training: A Regularization Method for Supervised and Semi-Supervised Learning](http://arxiv.org/abs/1704.03976v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/neural-structured-learning)",
      "n": "VAT",
      "d": "2017-04-13",
      "m1": "11.36"
    },
    {
      "p": "[Exploring Self-Supervised Regularization for Supervised and Semi-Supervised Learning](https://arxiv.org/abs/1906.10343v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vuptran/sesemi)",
      "n": "SESEMI SSL (ConvNet)",
      "d": "2019-06-25",
      "m1": "11.65"
    },
    {
      "p": "[Temporal Ensembling for Semi-Supervised Learning](http://arxiv.org/abs/1610.02242v3)",
      "c": "[&check;&nbsp;Link](https://github.com/benathi/fastswa-semi-sup)",
      "n": "Pi Model",
      "d": "2016-10-07",
      "m1": "12.16"
    },
    {
      "p": "[Triple Generative Adversarial Networks](https://arxiv.org/abs/1912.09784v2)",
      "c": "[&check;&nbsp;Link](https://github.com/taufikxu/Triple-GAN)",
      "n": "Triple-GAN-V2 (CNN-13, no aug)",
      "d": "2019-12-20",
      "m1": "12.41"
    },
    {
      "p": "[Good Semi-supervised Learning that Requires a Bad GAN](http://arxiv.org/abs/1705.09783v3)",
      "c": "[&check;&nbsp;Link](https://github.com/kimiyoung/ssl_bad_gan)",
      "n": "Bad GAN",
      "d": "2017-05-27",
      "m1": "14.41"
    },
    {
      "p": "[Improved Techniques for Training GANs](http://arxiv.org/abs/1606.03498v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/gan)",
      "n": "GAN",
      "d": "2016-06-10",
      "m1": "15.59"
    },
    {
      "p": "[Semi-Supervised Learning with Ladder Networks](http://arxiv.org/abs/1507.02672v2)",
      "c": "[&check;&nbsp;Link](https://github.com/arasmus/ladder)",
      "n": "\u0393-model",
      "d": "2015-07-09",
      "m1": "20.4"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
