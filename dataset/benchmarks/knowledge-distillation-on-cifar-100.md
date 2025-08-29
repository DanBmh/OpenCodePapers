# knowledge-distillation-on-cifar-100

[Dataset Link](https://www.cs.toronto.edu/~kriz/cifar.html) \
Task Hierarchy: ['Knowledge Distillation']

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
      "label": "Top-1 Accuracy (%)",
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
      "p": "[Understanding the Role of the Projector in Knowledge Distillation](https://arxiv.org/abs/2303.11098v5)",
      "c": "[&check;&nbsp;Link](https://github.com/yoshitomo-matsubara/torchdistill)",
      "n": "SRD (T:resnet-32x4, S:shufflenet-v2)",
      "d": "2023-03-20",
      "m1": "79.86"
    },
    {
      "p": "[Logit Standardization in Knowledge Distillation](https://arxiv.org/abs/2403.01427v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sunshangquan/logit-standardardization-kd)",
      "n": "shufflenet-v2(T:resnet-32x4, S:shufflenet-v2)",
      "d": "2024-03-03",
      "m1": "78.76"
    },
    {
      "p": "[MV-MR: multi-views and multi-representations for self-supervised learning and knowledge distillation](https://arxiv.org/abs/2303.12130v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vkinakh/mv-mr)",
      "n": "MV-MR (T: CLIP/ViT-B-16 S: resnet50)",
      "d": "2023-03-21",
      "m1": "78.6"
    },
    {
      "p": "[Logit Standardization in Knowledge Distillation](https://arxiv.org/abs/2403.01427v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sunshangquan/logit-standardardization-kd)",
      "n": "resnet8x4\n(T: resnet32x4 S: resnet8x4)",
      "d": "2024-03-03",
      "m1": "78.28"
    },
    {
      "p": "[Knowledge Distillation with the Reused Teacher Classifier](https://arxiv.org/abs/2203.14001v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DefangChen/SimKD)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4 [modified])",
      "d": "2022-03-26",
      "m1": "78.08"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "ReviewKD++(T:resnet-32x4, S:shufflenet-v2)",
      "d": "2023-05-26",
      "m1": "77.93"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "ReviewKD++(T:resnet-32x4, S:shufflenet-v1)",
      "d": "2023-05-26",
      "m1": "77.68"
    },
    {
      "p": "[LumiNet: The Bright Side of Perceptual Knowledge Distillation](https://arxiv.org/abs/2310.03669v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ismail31416/luminet)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2023-10-05",
      "m1": "77.50"
    },
    {
      "p": "[Information Theoretic Representation Distillation](https://arxiv.org/abs/2112.00459v3)",
      "c": "[&check;&nbsp;Link](https://github.com/roymiles/ITRD)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2021-12-01",
      "m1": "76.68"
    },
    {
      "p": "[Knowledge Distillation from A Stronger Teacher](https://arxiv.org/abs/2205.10536v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yoshitomo-matsubara/torchdistill)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2022-05-21",
      "m1": "76.31"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "DKD++(T:resnet-32x4, S:resnet-8x4)",
      "d": "2023-05-26",
      "m1": "76.28"
    },
    {
      "p": "[Wasserstein Contrastive Representation Distillation](https://arxiv.org/abs/2012.08674v2)",
      "c": "",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2020-12-15",
      "m1": "76.15"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "ReviewKD++(T:WRN-40-2, S:WRN-40-1)",
      "d": "2023-05-26",
      "m1": "75.66"
    },
    {
      "p": "[Distilling Knowledge via Knowledge Review](https://arxiv.org/abs/2104.09044v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yoshitomo-matsubara/torchdistill)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2021-04-19",
      "m1": "75.63"
    },
    {
      "p": "[Contrastive Representation Distillation](https://arxiv.org/abs/1910.10699v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HobbitLong/RepDistiller)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2019-10-23",
      "m1": "75.51"
    },
    {
      "p": "[Information Theoretic Representation Distillation](https://arxiv.org/abs/2112.00459v3)",
      "c": "[&check;&nbsp;Link](https://github.com/roymiles/ITRD)",
      "n": "vgg8 (T:vgg13 S:vgg8)",
      "d": "2021-12-01",
      "m1": "74.93"
    },
    {
      "p": "[Distilling Knowledge via Knowledge Review](https://arxiv.org/abs/2104.09044v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yoshitomo-matsubara/torchdistill)",
      "n": "vgg8 (T:vgg13 S:vgg8)",
      "d": "2021-04-19",
      "m1": "74.84"
    },
    {
      "p": "[Wasserstein Contrastive Representation Distillation](https://arxiv.org/abs/2012.08674v2)",
      "c": "",
      "n": "vgg8 (T:vgg13 S:vgg8)",
      "d": "2020-12-15",
      "m1": "74.72"
    },
    {
      "p": "[Contrastive Representation Distillation](https://arxiv.org/abs/1910.10699v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HobbitLong/RepDistiller)",
      "n": "vgg8 (T:vgg13 S:vgg8)",
      "d": "2019-10-23",
      "m1": "74.29"
    },
    {
      "p": "[Distilling the Knowledge in a Neural Network](http://arxiv.org/abs/1503.02531v1)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "resnet8x4 (T: resnet32x4 S: resnet8x4)",
      "d": "2015-03-09",
      "m1": "73.33"
    },
    {
      "p": "[Distilling the Knowledge in a Neural Network](http://arxiv.org/abs/1503.02531v1)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "vgg8 (T:vgg13 S:vgg8)",
      "d": "2015-03-09",
      "m1": "72.98"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "KD++(T:resnet56, S:resnet20)",
      "d": "2023-05-26",
      "m1": "72.53"
    },
    {
      "p": "[Information Theoretic Representation Distillation](https://arxiv.org/abs/2112.00459v3)",
      "c": "[&check;&nbsp;Link](https://github.com/roymiles/ITRD)",
      "n": "resnet110 (T:resnet110 S:resnet20)",
      "d": "2021-12-01",
      "m1": "71.99"
    },
    {
      "p": "[Wasserstein Contrastive Representation Distillation](https://arxiv.org/abs/2012.08674v2)",
      "c": "",
      "n": "resnet110 (T:resnet110 S:resnet20)",
      "d": "2020-12-15",
      "m1": "71.88"
    },
    {
      "p": "[Contrastive Representation Distillation](https://arxiv.org/abs/1910.10699v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HobbitLong/RepDistiller)",
      "n": "resnet110 (T:resnet110 S:resnet20)",
      "d": "2019-10-23",
      "m1": "71.56"
    },
    {
      "p": "[Improving Knowledge Distillation via Regularizing Feature Norm and Direction](https://arxiv.org/abs/2305.17007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wangyz1608/knowledge-distillation-via-nd)",
      "n": "DKD++(T:resnet50, S:mobilenetv2)",
      "d": "2023-05-26",
      "m1": "70.82"
    },
    {
      "p": "[Distilling the Knowledge in a Neural Network](http://arxiv.org/abs/1503.02531v1)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "resnet110 (T:resnet110 S:resnet20)",
      "d": "2015-03-09",
      "m1": "70.67"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
