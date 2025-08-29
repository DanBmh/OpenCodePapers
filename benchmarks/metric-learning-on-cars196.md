# metric-learning-on-cars196

[Dataset Link](https://ai.stanford.edu/~jkrause/cars/car_dataset.html) \
Task Hierarchy: ['Metric Learning']

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
      "label": "R@1",
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
      "p": "[Unicom: Universal and Compact Representation Learning for Image Retrieval](https://arxiv.org/abs/2304.05884v1)",
      "c": "[&check;&nbsp;Link](https://github.com/OML-Team/open-metric-learning)",
      "n": "Unicom+ViT-L@336px",
      "d": "2023-04-12",
      "m1": "98.2"
    },
    {
      "p": "[Hyperbolic Vision Transformers: Combining Improvements in Metric Learning](https://arxiv.org/abs/2203.10833v2)",
      "c": "[&check;&nbsp;Link](https://github.com/OML-Team/open-metric-learning)",
      "n": "Hyp-DINO 8x8",
      "d": "2022-03-21",
      "m1": "92.8"
    },
    {
      "p": "[Calibrated neighborhood aware confidence measure for deep metric learning](https://arxiv.org/abs/2006.04935v1)",
      "c": "",
      "n": "NED",
      "d": "2020-06-08",
      "m1": "91.5"
    },
    {
      "p": "[Learning Intra-Batch Connections for Deep Metric Learning](https://arxiv.org/abs/2102.07753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dvl-tum/intra_batch)",
      "n": "ResNet-50 + Intra-Batch (ensemble of 5)",
      "d": "2021-02-15",
      "m1": "91.5"
    },
    {
      "p": "[Attributable Visual Similarity Learning](https://arxiv.org/abs/2203.14932v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zbr17/avsl)",
      "n": "ResNet-50 + AVSL",
      "d": "2022-03-28",
      "m1": "91.5"
    },
    {
      "p": "[Learning Semantic Proxies from Visual Prompts for Parameter-Efficient Fine-Tuning in Deep Metric Learning](https://arxiv.org/abs/2402.02340v2)",
      "c": "[&check;&nbsp;Link](https://github.com/noahsark/parameterefficient-dml)",
      "n": "EfficientDML-VPTSP-G/512",
      "d": "2024-02-04",
      "m1": "91.2"
    },
    {
      "p": "[Center Contrastive Loss for Metric Learning](https://arxiv.org/abs/2308.00458v1)",
      "c": "",
      "n": "CCL (ResNet-50)",
      "d": "2023-08-01",
      "m1": "91.02"
    },
    {
      "p": "[Integrating Language Guidance into Vision-based Deep Metric Learning](https://arxiv.org/abs/2203.08543v1)",
      "c": "[&check;&nbsp;Link](https://github.com/explainableml/languageguidance_for_dml)",
      "n": "ResNet50 + Language",
      "d": "2022-03-16",
      "m1": "90.2"
    },
    {
      "p": "[It Takes Two to Tango: Mixup for Deep Metric Learning](https://arxiv.org/abs/2106.04990v2)",
      "c": "[&check;&nbsp;Link](https://github.com/billpsomas/Metrix_ICLR22)",
      "n": "ResNet-50 + Metrix",
      "d": "2021-06-09",
      "m1": "89.6"
    },
    {
      "p": "[S2SD: Simultaneous Similarity-based Self-Distillation for Deep Metric Learning](https://arxiv.org/abs/2009.08348v3)",
      "c": "[&check;&nbsp;Link](https://github.com/MLforHealth/S2SD)",
      "n": "ResNet50 + S2SD",
      "d": "2020-09-17",
      "m1": "89.5"
    },
    {
      "p": "[Recall@k Surrogate Loss with Large Batches and Similarity Mixup](https://arxiv.org/abs/2108.11179v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yash0307/RecallatK_surrogate)",
      "n": "Recall@k Surrogate loss (ViT-B/16)",
      "d": "2021-08-25",
      "m1": "89.5"
    },
    {
      "p": "[A unifying mutual information view of metric learning: cross-entropy vs. pairwise losses](https://arxiv.org/abs/2003.08983v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jeromerony/dml_cross_entropy)",
      "n": "ResNet-50 + Cross-Entropy",
      "d": "2020-03-19",
      "m1": "89.3"
    },
    {
      "p": "[Hyperbolic Vision Transformers: Combining Improvements in Metric Learning](https://arxiv.org/abs/2203.10833v2)",
      "c": "[&check;&nbsp;Link](https://github.com/OML-Team/open-metric-learning)",
      "n": "Hyp-DINO",
      "d": "2022-03-21",
      "m1": "89.2"
    },
    {
      "p": "[Non-isotropy Regularization for Proxy-based Deep Metric Learning](https://arxiv.org/abs/2203.08547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/explainableml/nonisotropicproxydml)",
      "n": "ResNet50 + NIR",
      "d": "2022-03-16",
      "m1": "89.1"
    },
    {
      "p": "[DAS: Densely-Anchored Sampling for Deep Metric Learning](https://arxiv.org/abs/2208.00119v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lizhaoliu-Lec/DAS)",
      "n": "Margin + DAS",
      "d": "2022-07-30",
      "m1": "88.34"
    },
    {
      "p": "[Proxy Anchor Loss for Deep Metric Learning](https://arxiv.org/abs/2003.13911v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tjddus9597/Proxy-Anchor-CVPR2020)",
      "n": "BN-Inception + Proxy-Anchor",
      "d": "2020-03-31",
      "m1": "88.3"
    },
    {
      "p": "[Recall@k Surrogate Loss with Large Batches and Similarity Mixup](https://arxiv.org/abs/2108.11179v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yash0307/RecallatK_surrogate)",
      "n": "Recall@k Surrogate loss (ResNet-50)",
      "d": "2021-08-25",
      "m1": "88.3"
    },
    {
      "p": "[Learning Intra-Batch Connections for Deep Metric Learning](https://arxiv.org/abs/2102.07753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dvl-tum/intra_batch)",
      "n": "ResNet-50 + Intra-Batch",
      "d": "2021-02-15",
      "m1": "88.1"
    },
    {
      "p": "[Metric Learning With HORDE: High-Order Regularizer for Deep Embeddings](https://arxiv.org/abs/1908.02735v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pierre-jacob/ICCV2019-Horde)",
      "n": "ABE + HORDE",
      "d": "2019-08-07",
      "m1": "88.0"
    },
    {
      "p": "[DAS: Densely-Anchored Sampling for Deep Metric Learning](https://arxiv.org/abs/2208.00119v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lizhaoliu-Lec/DAS)",
      "n": "MS + SEC + DAS",
      "d": "2022-07-30",
      "m1": "87.8"
    },
    {
      "p": "[DiVA: Diverse Visual Feature Aggregation for Deep Metric Learning](https://arxiv.org/abs/2004.13458v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Confusezius/ECCV2020_DiVA_MultiFeature_DML)",
      "n": "ResNet50 + DiVA",
      "d": "2020-04-28",
      "m1": "87.6"
    },
    {
      "p": "[Towards Interpretable Deep Metric Learning with Structural Matching](https://arxiv.org/abs/2108.05889v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wl-zhao/diml)",
      "n": "ProxyAnchor + DIML",
      "d": "2021-08-12",
      "m1": "87.01"
    },
    {
      "p": "[ProxyNCA++: Revisiting and Revitalizing Proxy Neighborhood Component Analysis](https://arxiv.org/abs/2004.01113v2)",
      "c": "[&check;&nbsp;Link](https://github.com/euwern/proxynca_pp)",
      "n": "ResNet-50 + ProxyNCA++",
      "d": "2020-04-02",
      "m1": "86.5"
    },
    {
      "p": "[Dissecting the impact of different loss functions with gradient surgery](https://arxiv.org/abs/2201.11307v1)",
      "c": "",
      "n": "Gradient Surgery",
      "d": "2022-01-27",
      "m1": "86.5"
    },
    {
      "p": "[Hyperbolic Vision Transformers: Combining Improvements in Metric Learning](https://arxiv.org/abs/2203.10833v2)",
      "c": "[&check;&nbsp;Link](https://github.com/OML-Team/open-metric-learning)",
      "n": "Hyp-ViT",
      "d": "2022-03-21",
      "m1": "86.5"
    },
    {
      "p": "[The Group Loss for Deep Metric Learning](https://arxiv.org/abs/1912.00385v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dvl-tum/group_loss)",
      "n": "Group Loss",
      "d": "2019-12-01",
      "m1": "85.6"
    },
    {
      "p": "[Attention-based Ensemble for Deep Metric Learning](http://arxiv.org/abs/1804.00382v2)",
      "c": "",
      "n": "ABE-8-512",
      "d": "2018-04-02",
      "m1": "85.2"
    },
    {
      "p": "[SoftTriple Loss: Deep Metric Learning Without Triplet Sampling](https://arxiv.org/abs/1909.05235v2)",
      "c": "[&check;&nbsp;Link](https://github.com/idstcv/SoftTriple)",
      "n": "BN-Inception + SoftTriple",
      "d": "2019-09-11",
      "m1": "84.5"
    },
    {
      "p": "[PADS: Policy-Adapted Sampling for Visual Similarity Learning](https://arxiv.org/abs/2003.11113v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Confusezius/CVPR2020_PADS)",
      "n": "ResNet50 (128) + PADS",
      "d": "2020-03-24",
      "m1": "83.5"
    },
    {
      "p": "[Circle Loss: A Unified Perspective of Pair Similarity Optimization](https://arxiv.org/abs/2002.10857v2)",
      "c": "[&check;&nbsp;Link](https://github.com/layumi/Person_reID_baseline_pytorch)",
      "n": "CircleLoss",
      "d": "2020-02-25",
      "m1": "83.4"
    },
    {
      "p": "[Improved Embeddings with Easy Positive Triplet Mining](https://arxiv.org/abs/1904.04370v2)",
      "c": "[&check;&nbsp;Link](https://github.com/littleredxh/DREML)",
      "n": "EPSHN(512)",
      "d": "2019-04-08",
      "m1": "82.7"
    },
    {
      "p": "[MIC: Mining Interclass Characteristics for Improved Metric Learning](https://arxiv.org/abs/1909.11574v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Confusezius/metric-learning-mining-interclass-characteristics)",
      "n": "ResNet50 (128) + MIC",
      "d": "2019-09-25",
      "m1": "82.6"
    },
    {
      "p": "[Sampling Matters in Deep Embedding Learning](http://arxiv.org/abs/1706.07567v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CompVis/metric-learning-divide-and-conquer)",
      "n": "ResNet-50 + Margin",
      "d": "2017-06-23",
      "m1": "79.6"
    },
    {
      "p": "[Hardness-Aware Deep Metric Learning](https://arxiv.org/abs/1903.05503v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wzzheng/HDML)",
      "n": "GoogLeNet + HDML",
      "d": "2019-03-13",
      "m1": "79.1"
    },
    {
      "p": "[Improved Embeddings with Easy Positive Triplet Mining](https://arxiv.org/abs/1904.04370v2)",
      "c": "[&check;&nbsp;Link](https://github.com/littleredxh/DREML)",
      "n": "EPSHN(64)",
      "d": "2019-04-08",
      "m1": "75.5"
    },
    {
      "p": "[Hard negative examples are hard, but useful](https://arxiv.org/abs/2007.12749v2)",
      "c": "[&check;&nbsp;Link](https://github.com/littleredxh/HardNegative)",
      "n": "SCT(64)",
      "d": "2020-07-24",
      "m1": "73.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
