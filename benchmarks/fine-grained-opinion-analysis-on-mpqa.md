# fine-grained-opinion-analysis-on-mpqa

[Dataset Link](https://mpqa.cs.pitt.edu/) \
Task Hierarchy: ['Sentiment Analysis', 'Fine-Grained Opinion Analysis']

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
      "label": "Holder Binary F1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Target Binary F1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "F1 (Opinion)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "F1 (Opinion-Holder Pair)",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "F1 (Opinion-Role Pair)",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "F1 (Opinion-Target Pair)",
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
      "p": "[Enhancing Opinion Role Labeling with Semantic-Aware Word Representations from Semantic Role Labeling](https://aclanthology.org/N19-1066)",
      "c": "[&check;&nbsp;Link](https://github.com/zhangmeishan/SRL4ORL)",
      "n": "SRL-SAWR",
      "d": "2019-06-01",
      "m1": "84.91",
      "m2": "73.29"
    },
    {
      "p": "[SRL4ORL: Improving Opinion Role Labeling using Multi-task Learning with Semantic Role Labeling](http://arxiv.org/abs/1711.00768v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amarasovic/naacl-mpqa-srl4orl)",
      "n": "FS-MTL",
      "d": "2017-11-02",
      "m1": "83.80",
      "m2": "72.06"
    },
    {
      "p": "[Mastering the Explicit Opinion-role Interaction: Syntax-aided Neural Transition System for Unified Opinion Role Labeling](https://arxiv.org/abs/2110.02001v2)",
      "c": "[&check;&nbsp;Link](https://github.com/chocowu/syptrtrans-orl)",
      "n": "SyPtrTrans",
      "d": "2021-10-05",
      "m3": "65.28",
      "m4": "59.48",
      "m5": "51.62",
      "m6": "44.04"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
