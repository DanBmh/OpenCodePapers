# semantic-role-labeling-on-ontonotes

[Dataset Link](https://catalog.ldc.upenn.edu/LDC2013T19) \
Task Hierarchy: ['Semantic Role Labeling']

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
      "label": "F1",
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
      "p": "[Better Combine Them Together! Integrating Syntactic Constituency and Dependency Representations for Semantic Role Labeling](https://aclanthology.org/2021.findings-acl.49)",
      "c": "[&check;&nbsp;Link](https://github.com/scofield7419/hesyfu)",
      "n": "HeSyFu",
      "d": null,
      "m1": "88.59"
    },
    {
      "p": "[Semantic Role Labeling as Dependency Parsing: Exploring Latent Tree Structures Inside Arguments](https://arxiv.org/abs/2110.06865v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/crfsrl)",
      "n": "CRF2o + RoBERTa",
      "d": "2021-10-13",
      "m1": "88.32"
    },
    {
      "p": "[An MRC Framework for Semantic Role Labeling](https://arxiv.org/abs/2109.06660v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shannonai/mrc-srl)",
      "n": "MRC-SRL",
      "d": "2021-09-14",
      "m1": "88.3"
    },
    {
      "p": "[Augmenting Transformers with Recursively Composed Multi-grained Representations](https://arxiv.org/abs/2309.16319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ant-research/structuredlm_rtdt)",
      "n": "ReCAT(pretrained on wikitext103)",
      "d": "2023-09-28",
      "m1": "88.0"
    },
    {
      "p": "[Syntax-driven Approach for Semantic Role Labeling](https://aclanthology.org/2022.lrec-1.772)",
      "c": "[&check;&nbsp;Link](https://github.com/synlp/srl-mm)",
      "n": "SRL-MM + XLNet",
      "d": null,
      "m1": "87.67"
    },
    {
      "p": "[Semantic Role Labeling as Dependency Parsing: Exploring Latent Tree Structures Inside Arguments](https://arxiv.org/abs/2110.06865v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/crfsrl)",
      "n": "CRF2o + BERT",
      "d": "2021-10-13",
      "m1": "87.66"
    },
    {
      "p": "[Constraining Linear-chain CRFs to Regular Languages](https://arxiv.org/abs/2106.07306v6)",
      "c": "[&check;&nbsp;Link](https://github.com/person594/regccrf-experiments)",
      "n": "RoBERTa+RegCCRF",
      "d": "2021-06-14",
      "m1": "87.51"
    },
    {
      "p": "[Constraining Linear-chain CRFs to Regular Languages](https://arxiv.org/abs/2106.07306v6)",
      "c": "[&check;&nbsp;Link](https://github.com/person594/regccrf-experiments)",
      "n": "RoBERTa+CRF",
      "d": "2021-06-14",
      "m1": " 87.27"
    },
    {
      "p": "[A Span Selection Model for Semantic Role Labeling](http://arxiv.org/abs/1810.02245v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hiroki13/span-based-srl)",
      "n": "BiLSTM-Span (Ensemble)",
      "d": "2018-10-04",
      "m1": "87.0"
    },
    {
      "p": "[A Span Selection Model for Semantic Role Labeling](http://arxiv.org/abs/1810.02245v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hiroki13/span-based-srl)",
      "n": "BiLSTM-Span",
      "d": "2018-10-04",
      "m1": "86.2"
    },
    {
      "p": "[Dependency or Span, End-to-End Uniform Semantic Role Labeling](http://arxiv.org/abs/1901.05280v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bcmi220/unisrl)",
      "n": "Li et al.",
      "d": "2019-01-16",
      "m1": "86.0"
    },
    {
      "p": "[Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://arxiv.org/abs/1805.04787v2)",
      "c": "[&check;&nbsp;Link](https://github.com/luheng/lsgn)",
      "n": "He et al.,",
      "d": "2018-05-12",
      "m1": "85.5"
    },
    {
      "p": "[Deep contextualized word representations](http://arxiv.org/abs/1802.05365v2)",
      "c": "[&check;&nbsp;Link](https://github.com/flairNLP/flair)",
      "n": "He et al., 2017 + ELMo",
      "d": "2018-02-15",
      "m1": "84.6"
    },
    {
      "p": "[Semantic Role Labeling as Dependency Parsing: Exploring Latent Tree Structures Inside Arguments](https://arxiv.org/abs/2110.06865v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/crfsrl)",
      "n": "CRF2o",
      "d": "2021-10-13",
      "m1": "83.66"
    },
    {
      "p": "[Deep Semantic Role Labeling with Self-Attention](http://arxiv.org/abs/1712.01586v1)",
      "c": "[&check;&nbsp;Link](https://github.com/XMUNLP/Tagger)",
      "n": "Tan et al.",
      "d": "2017-12-05",
      "m1": "82.7"
    },
    {
      "p": "[Jointly Predicting Predicates and Arguments in Neural Semantic Role Labeling](http://arxiv.org/abs/1805.04787v2)",
      "c": "[&check;&nbsp;Link](https://github.com/luheng/lsgn)",
      "n": "He et al.",
      "d": "2018-05-12",
      "m1": "82.1"
    },
    {
      "p": "[Deep Semantic Role Labeling: What Works and What's Next](https://aclanthology.org/P17-1044)",
      "c": "[&check;&nbsp;Link](https://github.com/luheng/deep_srl)",
      "n": "He et al.",
      "d": "2017-07-01",
      "m1": "81.7"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
