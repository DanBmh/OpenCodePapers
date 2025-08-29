# text-simplification-on-asset

[Dataset Link](https://github.com/facebookresearch/asset) \
Task Hierarchy: ['', 'Text Simplification']

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
      "label": "BLEU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "SARI (EASSE>=0.2.1)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "METEOR",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "FKGL",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "QuestEval (Reference-less, BERTScore)",
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
      "p": "[Metric-Based In-context Learning: A Case Study in Text Simplification](https://arxiv.org/abs/2307.14632v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nlp-ku/metric-based-in-context-learning)",
      "n": "GPT-175B (15 SARI-selected examples, random ordering)",
      "d": "2023-07-27",
      "m1": "73.92",
      "m2": "47.94",
      "m4": "7.73"
    },
    {
      "p": "[MUSS: Multilingual Unsupervised Sentence Simplification by Mining Paraphrases](https://arxiv.org/abs/2005.00352v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/muss)",
      "n": "MUSS (BART+ACCESS Supervised)",
      "d": "2020-05-01",
      "m1": "72.98",
      "m2": "44.15",
      "m4": "6.05"
    },
    {
      "p": "[Control Prefixes for Parameter-Efficient Text Generation](https://arxiv.org/abs/2110.08329v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Yale-LILY/dart)",
      "n": "Control Prefixes (BART)",
      "d": "2021-10-15",
      "m2": "43.58",
      "m4": "5.97",
      "m5": "0.64"
    },
    {
      "p": "[Text Simplification by Tagging](https://arxiv.org/abs/2103.05070v1)",
      "c": "[&check;&nbsp;Link](https://github.com/grammarly/gector)",
      "n": "TST",
      "d": "2021-03-08",
      "m2": "43.21"
    },
    {
      "p": "[MUSS: Multilingual Unsupervised Sentence Simplification by Mining Paraphrases](https://arxiv.org/abs/2005.00352v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/muss)",
      "n": "MUSS (BART+ACCESS Unsupervised)",
      "d": "2020-05-01",
      "m2": "42.65",
      "m4": "8.23"
    },
    {
      "p": "[Controllable Sentence Simplification](https://arxiv.org/abs/1910.02677v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/access)",
      "n": "ACCESS",
      "d": "2019-10-07",
      "m1": "75.99*",
      "m2": "40.13"
    },
    {
      "p": "[Integrating Transformer and Paraphrase Rules for Sentence Simplification](http://arxiv.org/abs/1810.11193v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Sanqiang/text_simplification)",
      "n": "DMASS-DCSS",
      "d": "2018-10-26",
      "m1": "71.44*",
      "m2": "38.67"
    },
    {
      "p": "[Sentence Simplification with Deep Reinforcement Learning](http://arxiv.org/abs/1703.10931v2)",
      "c": "[&check;&nbsp;Link](https://github.com/XingxingZhang/dress)",
      "n": "Dress-LS",
      "d": "2017-03-31",
      "m1": "86.39*",
      "m2": "36.59"
    },
    {
      "p": "[Unsupervised Neural Text Simplification](https://arxiv.org/abs/1810.07931v6)",
      "c": "[&check;&nbsp;Link](https://github.com/subramanyamdvss/UnsupNTS)",
      "n": "UNTS (Unsupervised)",
      "d": "2018-10-18",
      "m1": "76.14*",
      "m2": "35.19"
    },
    {
      "p": "[Sentence Simplification by Monolingual Machine Translation](https://aclanthology.org/P12-1107)",
      "c": "",
      "n": "PBMT-R",
      "d": "2012-07-01",
      "m1": "79.39*",
      "m2": "34.63"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "T5",
      "d": "2021-02-02",
      "m3": "0.581"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "BART",
      "d": "2021-02-02",
      "m3": "0.560"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
