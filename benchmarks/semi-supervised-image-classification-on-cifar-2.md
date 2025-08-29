# semi-supervised-image-classification-on-cifar-2

[Dataset Link](https://www.cs.toronto.edu/~kriz/cifar.html) \
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
      "m1": "13.50\u00b10.14"
    },
    {
      "p": "[SST: Self-training with Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2506.00467v1)",
      "c": "",
      "n": "Super-SST (ViT-Small)",
      "d": "2025-05-31",
      "m1": "14.20\u00b10.17"
    },
    {
      "p": "[Class-Aware Contrastive Semi-Supervised Learning](https://arxiv.org/abs/2203.02261v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tencentyouturesearch/classification-semicls)",
      "n": "CCSSL(FixMatch)",
      "d": "2022-03-04",
      "m1": "19.32"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "FixMatch+DM",
      "d": null,
      "m1": "20.42\u00b10.17"
    },
    {
      "p": "[SimMatch: Semi-supervised Learning with Similarity Matching](https://arxiv.org/abs/2203.06915v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kylezheng1997/simmatch)",
      "n": "SimMatch",
      "d": "2022-03-14",
      "m1": "20.58"
    },
    {
      "p": "[Contrastive Regularization for Semi-Supervised Learning](https://arxiv.org/abs/2201.06247v2)",
      "c": "",
      "n": "FixMatch+CR",
      "d": "2022-01-17",
      "m1": "21.03"
    },
    {
      "p": "[DoubleMatch: Improving Semi-Supervised Learning with Self-Supervision](https://arxiv.org/abs/2205.05575v1)",
      "c": "[&check;&nbsp;Link](https://github.com/walline/doublematch)",
      "n": "DoubleMatch",
      "d": "2022-05-11",
      "m1": "21.22\u00b1 0.17"
    },
    {
      "p": "[NP-Match: When Neural Processes meet Semi-Supervised Learning](https://arxiv.org/abs/2207.01066v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jianf-wang/np-match)",
      "n": "NP-Match",
      "d": "2022-07-03",
      "m1": "21.22"
    },
    {
      "p": "[Self Meta Pseudo Labels: Meta Pseudo Labels Without The Teacher](https://arxiv.org/abs/2212.13420v1)",
      "c": "",
      "n": "SMPL (WRN-28-8)",
      "d": "2022-12-27",
      "m1": "21.68"
    },
    {
      "p": "[FreeMatch: Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2205.07246v3)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/semi-supervised-learning)",
      "n": "FreeMatch",
      "d": "2022-05-15",
      "m1": "21.68"
    },
    {
      "p": "[SimPLE: Similar Pseudo Label Exploitation for Semi-Supervised Classification](https://arxiv.org/abs/2103.16725v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zijian-hu/SimPLE)",
      "n": "SimPLE (WRN-28-8)",
      "d": "2021-03-30",
      "m1": "21.89"
    },
    {
      "p": "[FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo Labeling](https://arxiv.org/abs/2110.08263v3)",
      "c": "[&check;&nbsp;Link](https://github.com/torchssl/torchssl)",
      "n": "FlexMatch",
      "d": "2021-10-15",
      "m1": "21.90\u00b10.15"
    },
    {
      "p": "[Dash: Semi-Supervised Learning with Dynamic Thresholding](https://arxiv.org/abs/2109.00650v1)",
      "c": "",
      "n": "Dash (RA, WRN-28-8)",
      "d": "2021-09-01",
      "m1": "21.97\u00b10.14"
    },
    {
      "p": "[LaplaceNet: A Hybrid Graph-Energy Neural Network for Deep Semi-Supervised Classification](https://arxiv.org/abs/2106.04527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/psellcam/LaplaceNet)",
      "n": "LaplaceNet (WRN-28-8)",
      "d": "2021-06-08",
      "m1": "22.11\u00b1 0.23"
    },
    {
      "p": "[DP-SSL: Towards Robust Semi-supervised Learning with A Few Labeled Samples](https://arxiv.org/abs/2110.13740v1)",
      "c": "",
      "n": "DP-SSL",
      "d": "2021-10-26",
      "m1": "22.24\u00b10.31"
    },
    {
      "p": "[FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence](https://arxiv.org/abs/2001.07685v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/fixmatch)",
      "n": "FixMatch (RA, WRN-28-8)",
      "d": "2020-01-21",
      "m1": "22.6"
    },
    {
      "p": "[EnAET: A Self-Trained framework for Semi-Supervised and Supervised Learning with Ensemble Transformations](https://arxiv.org/abs/1911.09265v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maple-research-lab/EnAET)",
      "n": "EnAET (WRN-28-2-Large)",
      "d": "2019-11-21",
      "m1": "22.92"
    },
    {
      "p": "[Milking CowMask for Semi-Supervised Image Classification](https://arxiv.org/abs/2003.12022v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/milking_cowmask)",
      "n": "CowMix (WRN-28-96x2d)",
      "d": "2020-03-26",
      "m1": "23.07\u00b10.30"
    },
    {
      "p": "[FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence](https://arxiv.org/abs/2001.07685v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/fixmatch)",
      "n": "FixMatch (CTA, WRN-28-8)",
      "d": "2020-01-21",
      "m1": "23.18\u00b10.11"
    },
    {
      "p": "[LiDAM: Semi-Supervised Learning with Localized Domain Adaptation and Iterative Matching](https://arxiv.org/abs/2010.06668v2)",
      "c": "",
      "n": "LiDAM",
      "d": "2020-10-13",
      "m1": "23.22"
    },
    {
      "p": "[All Labels Are Not Created Equal: Enhancing Semi-supervision via Label Grouping and Co-training](https://arxiv.org/abs/2104.05248v1)",
      "c": "[&check;&nbsp;Link](https://github.com/islam-nassar/semco)",
      "n": "SemCo (\u03bc=7)",
      "d": "2021-04-12",
      "m1": "24.45\u00b10.12"
    },
    {
      "p": "[SHOT-VAE: Semi-supervised Deep Generative Models With Label-aware ELBO Approximations](https://arxiv.org/abs/2011.10684v4)",
      "c": "[&check;&nbsp;Link](https://github.com/FengHZ/AAAI2021-260)",
      "n": "SHOT-VAE",
      "d": "2020-11-21",
      "m1": "25.3"
    },
    {
      "p": "[EnAET: A Self-Trained framework for Semi-Supervised and Supervised Learning with Ensemble Transformations](https://arxiv.org/abs/1911.09265v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maple-research-lab/EnAET)",
      "n": "EnAET (WRN-28-2)",
      "d": "2019-11-21",
      "m1": "26.93\u00b10.21"
    },
    {
      "p": "[In Defense of Pseudo-Labeling: An Uncertainty-Aware Pseudo-label Selection Framework for Semi-Supervised Learning](https://arxiv.org/abs/2101.06329v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nayeemrizve/ups)",
      "n": "UPS (CNN-13)",
      "d": "2021-01-15",
      "m1": "32"
    },
    {
      "p": "[Dual Student: Breaking the Limits of the Teacher in Semi-supervised Learning](https://arxiv.org/abs/1909.01804v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ZHKKKe/DualStudent)",
      "n": "Dual Student (480)",
      "d": "2019-09-03",
      "m1": "32.77"
    },
    {
      "p": "[Repetitive Reprediction Deep Decipher for Semi-Supervised Learning](https://arxiv.org/abs/1908.04345v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DoctorKey/R2D2.pytorch)",
      "n": "R2-D2 (CNN-13)",
      "d": "2019-08-09",
      "m1": "32.87"
    },
    {
      "p": "[Temporal Ensembling for Semi-Supervised Learning](http://arxiv.org/abs/1610.02242v3)",
      "c": "[&check;&nbsp;Link](https://github.com/benathi/fastswa-semi-sup)",
      "n": "Temporal ensembling",
      "d": "2016-10-07",
      "m1": "38.65"
    },
    {
      "p": "[Exploring Self-Supervised Regularization for Supervised and Semi-Supervised Learning](https://arxiv.org/abs/1906.10343v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vuptran/sesemi)",
      "n": "SESEMI SSL (ConvNet)",
      "d": "2019-06-25",
      "m1": "38.7"
    },
    {
      "p": "[Regularization With Stochastic Transformations and Perturbations for Deep Semi-Supervised Learning](http://arxiv.org/abs/1606.04586v1)",
      "c": "",
      "n": "\u2161-Model",
      "d": "2016-06-14",
      "m1": "39.19"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
