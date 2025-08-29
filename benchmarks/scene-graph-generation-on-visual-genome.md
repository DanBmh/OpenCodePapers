# scene-graph-generation-on-visual-genome

[Dataset Link](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) \
Task Hierarchy: ['Scene Graph Generation']

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
      "label": "Recall@50",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "mean Recall @20",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Recall@100",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Recall@20",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "mean Recall @100",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "R@100",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "mR@100",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "mR@50",
      "sortable": "true"
    },
    {
      "key": "m9",
      "label": "zR@100",
      "sortable": "true"
    },
    {
      "key": "m10",
      "label": "zR@20",
      "sortable": "true"
    },
    {
      "key": "m11",
      "label": "zR@50",
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
      "p": "[Groupwise Query Specialization and Quality-Aware Multi-Assignment for Transformer-based Visual Relationship Detection](https://arxiv.org/abs/2403.17709v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/speaq)",
      "n": "SpeaQ (without reweighting)",
      "d": "2024-03-26",
      "m1": "32.9",
      "m3": "36.0",
      "m5": "14.1",
      "m6": "36.0",
      "m7": "14.1",
      "m8": "11.8"
    },
    {
      "p": "[Groupwise Query Specialization and Quality-Aware Multi-Assignment for Transformer-based Visual Relationship Detection](https://arxiv.org/abs/2403.17709v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/speaq)",
      "n": "SpeaQ (with reweighting)",
      "d": "2024-03-26",
      "m1": "32.1",
      "m3": "35.5",
      "m5": "17.6",
      "m6": "35.5",
      "m7": "17.6",
      "m8": "15.1"
    },
    {
      "p": "[Unbiased Scene Graph Generation from Biased Training](https://arxiv.org/abs/2002.11949v3)",
      "c": "[&check;&nbsp;Link](https://github.com/KaihuaTang/Scene-Graph-Benchmark.pytorch)",
      "n": "Causal-TDE",
      "d": "2020-02-27",
      "m1": "31.93",
      "m2": "6.9"
    },
    {
      "p": "[Energy-Based Learning for Scene Graph Generation](https://arxiv.org/abs/2103.02221v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mods333/energy-based-scene-graph)",
      "n": "SG-EBM",
      "d": "2021-03-03",
      "m1": "31.74",
      "m2": "7.1"
    },
    {
      "p": "[GPS-Net: Graph Property Sensing Network for Scene Graph Generation](https://arxiv.org/abs/2003.12962v1)",
      "c": "[&check;&nbsp;Link](https://github.com/taksau/GPS-Net)",
      "n": "GPS-Net",
      "d": "2020-03-29",
      "m1": "28.9"
    },
    {
      "p": "[Tackling the Challenges in Scene Graph Generation with Local-to-Global Interactions](https://arxiv.org/abs/2106.08543v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangminwoo/Local-to-Global-Interaction-Networks-SGG)",
      "n": "LOGIN",
      "d": "2021-06-16",
      "m1": "28.2",
      "m3": "31.4",
      "m4": "22.2"
    },
    {
      "p": "[Learning to Compose Dynamic Tree Structures for Visual Contexts](http://arxiv.org/abs/1812.01880v1)",
      "c": "[&check;&nbsp;Link](https://github.com/KaihuaTang/Scene-Graph-Benchmark.pytorch)",
      "n": "VCTree",
      "d": "2018-12-05",
      "m1": "27.9"
    },
    {
      "p": "[NODIS: Neural Ordinary Differential Scene Understanding](https://arxiv.org/abs/2001.04735v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yrcong/NODIS)",
      "n": "NODIS",
      "d": "2020-01-14",
      "m1": "27.7",
      "m4": "21.6"
    },
    {
      "p": "[Knowledge-Embedded Routing Network for Scene Graph Generation](http://arxiv.org/abs/1903.03326v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yuweihao/KERN)",
      "n": "KERN",
      "d": "2019-03-08",
      "m1": "27.1"
    },
    {
      "p": "[Recovering the Unbiased Scene Graphs from the Biased Ones](https://arxiv.org/abs/2107.02112v1)",
      "c": "[&check;&nbsp;Link](https://github.com/coldmanck/recovering-unbiased-scene-graphs)",
      "n": "DLFE",
      "d": "2021-07-05",
      "m1": "25.4"
    },
    {
      "p": "[Fine-Grained Scene Graph Generation with Data Transfer](https://arxiv.org/abs/2203.11654v2)",
      "c": "[&check;&nbsp;Link](https://github.com/waxnkw/ietrans-sgg.pytorch)",
      "n": "IETrans",
      "d": "2022-03-22",
      "m1": "23.5",
      "m3": "27.2",
      "m5": "18.0"
    },
    {
      "p": "[Panoptic Scene Graph Generation with Semantics-Prototype Learning](https://arxiv.org/abs/2307.15567v3)",
      "c": "[&check;&nbsp;Link](https://github.com/lili0415/psg-biased-annotation)",
      "n": "ADTrans",
      "d": "2023-07-28",
      "m1": "23.0",
      "m2": "12.3",
      "m5": "19.2",
      "m7": "19.2",
      "m8": "15.8"
    },
    {
      "p": "[Graph R-CNN for Scene Graph Generation](http://arxiv.org/abs/1808.00191v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jwyang/graph-rcnn.pytorch)",
      "n": "Graph-RCNN",
      "d": "2018-08-01",
      "m1": "11.4"
    },
    {
      "p": "[Scene Graph Generation from Objects, Phrases and Region Captions](http://arxiv.org/abs/1707.09700v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yikang-li/MSDN)",
      "n": "MSDN",
      "d": "2017-07-31",
      "m1": "10.72"
    },
    {
      "p": "[Biasing Like Human: A Cognitive Bias Framework for Scene Graph Generation](https://arxiv.org/abs/2203.09160v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rafa-cxg/PySGG-cxg)",
      "n": "C-bias",
      "d": "2022-03-17",
      "m2": "11.63",
      "m5": "17.24"
    },
    {
      "p": "[CogTree: Cognition Tree Loss for Unbiased Scene Graph Generation](https://arxiv.org/abs/2009.07526v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CYVincent/Scene-Graph-Transformer-CogTree)",
      "n": "CogTree",
      "d": "2020-09-16",
      "m2": "7.9"
    },
    {
      "p": "[Expressive Scene Graph Generation Using Commonsense Knowledge Infusion for Visual Understanding and Reasoning](https://link.springer.com/chapter/10.1007/978-3-031-06981-9_6)",
      "c": "[&check;&nbsp;Link](https://github.com/jaleedkhan/neusire)",
      "n": "ExpressiveSGG",
      "d": "2022-05-31",
      "m6": "39.12"
    },
    {
      "p": "[NeuSyRE: Neuro-Symbolic Visual Understanding and Reasoning Framework based on Scene Graph Enrichment](https://www.semantic-web-journal.net/content/neusyre-neuro-symbolic-visual-understanding-and-reasoning-framework-based-scene-graph-0)",
      "c": "[&check;&nbsp;Link](https://github.com/jaleedkhan/neusire)",
      "n": "NeuSyRE",
      "d": "2023-11-05",
      "m6": "39.1",
      "m7": "12.6",
      "m8": "10.9"
    },
    {
      "p": "[KnowZRel: Common Sense Knowledge-based Zero-Shot Relationship Retrieval for Generalised Scene Graph Generation](https://ieeexplore.ieee.org/document/10897903)",
      "c": "[&check;&nbsp;Link](https://github.com/jaleedkhan/zsrr-sgg)",
      "n": "KnowZRel",
      "d": "2025-02-21",
      "m9": "35.65",
      "m10": "14.22",
      "m11": "25.43"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
