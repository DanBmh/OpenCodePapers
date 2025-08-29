# semi-supervised-image-classification-on-cifar-6

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
      "m1": "2.42\u00b10.13"
    },
    {
      "p": "[SST: Self-training with Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2506.00467v1)",
      "c": "",
      "n": "Super-SST (ViT-Small)",
      "d": "2025-05-31",
      "m1": "3.37\u00b10.22"
    },
    {
      "p": "[ViTSGMM: A Robust Semi-Supervised Image Recognition Network Using Sparse Labels](https://arxiv.org/abs/2506.03582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Shu1L0n9/SemiOccam)",
      "n": "SemiOccam",
      "d": "2025-06-04",
      "m1": "3.47"
    },
    {
      "p": "[Diff-SySC: An Approach Using Diffusion Models for Semi-Supervised Image Classification](https://www.scitepress.org/PublicationsDetail.aspx?ID=8MzrzMi7kMs%3d&t=1)",
      "c": "",
      "n": "Diff-SySC",
      "d": "2025-02-25",
      "m1": "3.65\u00b10.10"
    },
    {
      "p": "[Dash: Semi-Supervised Learning with Dynamic Thresholding](https://arxiv.org/abs/2109.00650v1)",
      "c": "",
      "n": "Dash (RA)",
      "d": "2021-09-01",
      "m1": "4.56\u00b10.13"
    },
    {
      "p": "[Debiased Learning from Naturally Imbalanced Pseudo-Labels](https://arxiv.org/abs/2201.01490v2)",
      "c": "[&check;&nbsp;Link](https://github.com/frank-xwang/debiased-pseudo-labeling)",
      "n": "DebiasPL (w/ FixMatch)",
      "d": "2022-01-05",
      "m1": "4.6"
    },
    {
      "p": "[Shrinking Class Space for Enhanced Certainty in Semi-Supervised Learning](https://arxiv.org/abs/2308.06777v1)",
      "c": "[&check;&nbsp;Link](https://github.com/LiheYoung/ShrinkMatch)",
      "n": "ShrinkMatch",
      "d": "2023-08-13",
      "m1": "4.74"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "FixMatch+DM",
      "d": null,
      "m1": "4.77\u00b10.09"
    },
    {
      "p": "[DP-SSL: Towards Robust Semi-supervised Learning with A Few Labeled Samples](https://arxiv.org/abs/2110.13740v1)",
      "c": "",
      "n": "DP-SSL",
      "d": "2021-10-26",
      "m1": "4.78\u00b10.26"
    },
    {
      "p": "[FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo Labeling](https://arxiv.org/abs/2110.08263v3)",
      "c": "[&check;&nbsp;Link](https://github.com/torchssl/torchssl)",
      "n": "FlexMatch",
      "d": "2021-10-15",
      "m1": "4.8\u00b10.06"
    },
    {
      "p": "[SimMatch: Semi-supervised Learning with Similarity Matching](https://arxiv.org/abs/2203.06915v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kylezheng1997/simmatch)",
      "n": "SimMatch",
      "d": "2022-03-14",
      "m1": "4.84"
    },
    {
      "p": "[SelfMatch: Combining Contrastive Self-Supervision and Consistency for Semi-Supervised Learning](https://arxiv.org/abs/2101.06480v1)",
      "c": "",
      "n": "SelfMatch",
      "d": "2021-01-16",
      "m1": "4.87\u00b10.26"
    },
    {
      "p": "[NP-Match: When Neural Processes meet Semi-Supervised Learning](https://arxiv.org/abs/2207.01066v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jianf-wang/np-match)",
      "n": "NP-Match",
      "d": "2022-07-03",
      "m1": "4.87"
    },
    {
      "p": "[FreeMatch: Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2205.07246v3)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/semi-supervised-learning)",
      "n": "FreeMatch",
      "d": "2022-05-15",
      "m1": "4.88"
    },
    {
      "p": "[Contrastive Regularization for Semi-Supervised Learning](https://arxiv.org/abs/2201.06247v2)",
      "c": "",
      "n": "FixMatch+CR",
      "d": "2022-01-17",
      "m1": "5.04"
    },
    {
      "p": "[FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence](https://arxiv.org/abs/2001.07685v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/fixmatch)",
      "n": "FixMatch (CTA)",
      "d": "2020-01-21",
      "m1": "5.07\u00b10.33"
    },
    {
      "p": "[Boosting the Performance of Semi-Supervised Learning with Unsupervised Clustering](https://arxiv.org/abs/2012.00504v1)",
      "c": "[&check;&nbsp;Link](https://github.com/boazlern/SSClustering)",
      "n": "Semi-MMDC",
      "d": "2020-12-01",
      "m1": "5.51\u00b10.25"
    },
    {
      "p": "[DoubleMatch: Improving Semi-Supervised Learning with Self-Supervision](https://arxiv.org/abs/2205.05575v1)",
      "c": "[&check;&nbsp;Link](https://github.com/walline/doublematch)",
      "n": "DoubleMatch",
      "d": "2022-05-11",
      "m1": "5.56\u00b10.42"
    },
    {
      "p": "[ReMixMatch: Semi-Supervised Learning with Distribution Alignment and Augmentation Anchoring](https://arxiv.org/abs/1911.09785v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/mixmatch)",
      "n": "ReMixMatch",
      "d": "2019-11-21",
      "m1": "6.27"
    },
    {
      "p": "[RealMix: Towards Realistic Semi-Supervised Deep Learning Algorithms](https://arxiv.org/abs/1912.08766v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uizard-technologies/realmix)",
      "n": "EnAET",
      "d": "2019-12-18",
      "m1": "7.6"
    },
    {
      "p": "[RealMix: Towards Realistic Semi-Supervised Deep Learning Algorithms](https://arxiv.org/abs/1912.08766v1)",
      "c": "[&check;&nbsp;Link](https://github.com/uizard-technologies/realmix)",
      "n": "RealMix",
      "d": "2019-12-18",
      "m1": "9.79"
    },
    {
      "p": "[MixMatch: A Holistic Approach to Semi-Supervised Learning](https://arxiv.org/abs/1905.02249v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/mixmatch)",
      "n": "MixMatch",
      "d": "2019-05-06",
      "m1": "11.08"
    },
    {
      "p": "[LiDAM: Semi-Supervised Learning with Localized Domain Adaptation and Iterative Matching](https://arxiv.org/abs/2010.06668v2)",
      "c": "",
      "n": "LiDAM",
      "d": "2020-10-13",
      "m1": "19.17"
    },
    {
      "p": "[Virtual Adversarial Training: A Regularization Method for Supervised and Semi-Supervised Learning](http://arxiv.org/abs/1704.03976v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/neural-structured-learning)",
      "n": "VAT",
      "d": "2017-04-13",
      "m1": "36.03"
    },
    {
      "p": "[Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results](http://arxiv.org/abs/1703.01780v6)",
      "c": "[&check;&nbsp;Link](https://github.com/CuriousAI/mean-teacher)",
      "n": "MeanTeacher",
      "d": "2017-03-06",
      "m1": "47.32"
    },
    {
      "p": "[mixup: Beyond Empirical Risk Minimization](http://arxiv.org/abs/1710.09412v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "MixUp",
      "d": "2017-10-25",
      "m1": "47.43"
    },
    {
      "p": "[Temporal Ensembling for Semi-Supervised Learning](http://arxiv.org/abs/1610.02242v3)",
      "c": "[&check;&nbsp;Link](https://github.com/benathi/fastswa-semi-sup)",
      "n": "\u2161-Model",
      "d": "2016-10-07",
      "m1": "53.12"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
