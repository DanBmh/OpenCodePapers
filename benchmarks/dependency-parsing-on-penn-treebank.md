# dependency-parsing-on-penn-treebank

[Dataset Link](https://catalog.ldc.upenn.edu/docs/LDC95T7/cl93.html) \
Task Hierarchy: ['Dependency Parsing']

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
      "label": "LAS",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "UAS",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "POS",
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
      "p": "[Rethinking Self-Attention: Towards Interpretability in Neural Parsing](https://arxiv.org/abs/1911.03875v3)",
      "c": "[&check;&nbsp;Link](https://github.com/KhalilMrini/LAL-Parser)",
      "n": "Label Attention Layer + HPSG + XLNet",
      "d": "2019-11-10",
      "m1": "96.26",
      "m2": "97.42",
      "m3": "97.3"
    },
    {
      "p": "[Enhancing Structure-aware Encoder with Extremely Limited Data for Graph-based Dependency Parsing](https://aclanthology.org/2022.coling-1.483)",
      "c": "[&check;&nbsp;Link](https://github.com/synlp/dmpar)",
      "n": "DMPar + XLNet",
      "d": null,
      "m1": "95.92",
      "m2": "97.30"
    },
    {
      "p": "[Automated Concatenation of Embeddings for Structured Prediction](https://arxiv.org/abs/2010.05006v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Alibaba-NLP/ACE)",
      "n": "ACE",
      "d": "2020-10-10",
      "m1": "95.8",
      "m2": "97.2"
    },
    {
      "p": "[Deep Biaffine Attention for Neural Dependency Parsing](http://arxiv.org/abs/1611.01734v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/dependency_parsing/ddparser)",
      "n": "Deep Biaffine + RoBERTa",
      "d": "2016-11-06",
      "m1": "95.75",
      "m2": "97.29"
    },
    {
      "p": "[Head-Driven Phrase Structure Grammar Parsing on Penn Treebank](https://arxiv.org/abs/1907.02684v4)",
      "c": "[&check;&nbsp;Link](https://github.com/DoodleJZ/HPSG-Neural-Parser)",
      "n": "HPSG Parser (Joint) + XLNet ",
      "d": "2019-07-05",
      "m1": "95.72",
      "m2": "97.20",
      "m3": "97.3"
    },
    {
      "p": "[Second-Order Neural Dependency Parsing with Message Passing and End-to-End Training](https://arxiv.org/abs/2010.05003v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangxinyu0922/Second_Order_Parsing)",
      "n": "MFVI",
      "d": "2020-10-10",
      "m1": "95.34",
      "m2": "96.91"
    },
    {
      "p": "[Semi-Supervised Sequence Modeling with Cross-View Training](http://arxiv.org/abs/1809.08370v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "CVT + Multi-Task",
      "d": "2018-09-22",
      "m1": "95.02",
      "m2": "96.61"
    },
    {
      "p": "[Recursive Non-Autoregressive Graph-to-Graph Transformer for Dependency Parsing with Iterative Refinement](https://arxiv.org/abs/2003.13118v2)",
      "c": "[&check;&nbsp;Link](https://github.com/idiap/g2g-transformer)",
      "n": "RNG Transformer",
      "d": "2020-03-29",
      "m1": "95.01",
      "m2": "96.66"
    },
    {
      "p": "[Generalizing Natural Language Analysis through Span-relation Representations](https://arxiv.org/abs/1911.03822v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jzbjyb/SpanRel)",
      "n": "SpanRel",
      "d": "2019-11-10",
      "m1": "94.70",
      "m2": "96.44"
    },
    {
      "p": "[Efficient Second-Order TreeCRF for Neural Dependency Parsing](https://arxiv.org/abs/2005.00975v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "CRFPar",
      "d": "2020-05-03",
      "m1": "94.49",
      "m2": "96.14"
    },
    {
      "p": "[Left-to-Right Dependency Parsing with Pointer Networks](http://arxiv.org/abs/1903.08445v1)",
      "c": "[&check;&nbsp;Link](https://github.com/danifg/Left2Right-Pointer-Parser)",
      "n": "Left-to-Right Pointer Network",
      "d": "2019-03-20",
      "m1": "94.43",
      "m2": "96.04"
    },
    {
      "p": "[Graph-based Dependency Parsing with Graph Neural Networks](https://aclanthology.org/P19-1237)",
      "c": "[&check;&nbsp;Link](https://github.com/AntNLP/gnn-dep-parsing)",
      "n": "Graph-based parser with GNNs",
      "d": "2019-07-01",
      "m1": "94.31",
      "m2": "95.97",
      "m3": "97.3"
    },
    {
      "p": "[Deep Biaffine Attention for Neural Dependency Parsing](http://arxiv.org/abs/1611.01734v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/dependency_parsing/ddparser)",
      "n": "Deep Biaffine",
      "d": "2016-11-06",
      "m1": "94.22",
      "m2": "95.87"
    },
    {
      "p": "[Stack-Pointer Networks for Dependency Parsing](http://arxiv.org/abs/1805.01087v1)",
      "c": "[&check;&nbsp;Link](https://github.com/XuezheMax/NeuroNLP2)",
      "n": "Stack-Pointer Network",
      "d": "2018-05-03",
      "m1": "94.19",
      "m2": "95.87",
      "m3": "97.3"
    },
    {
      "p": "[An improved neural network model for joint POS tagging and dependency parsing](http://arxiv.org/abs/1807.03955v2)",
      "c": "[&check;&nbsp;Link](https://github.com/datquocnguyen/jPTDP)",
      "n": "jPTDP",
      "d": "2018-07-11",
      "m1": "93.87",
      "m2": "95.51",
      "m3": "97.97"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Experiment-bert",
      "d": null,
      "m1": "93.2",
      "m2": "95.42"
    },
    {
      "p": "[Globally Normalized Transition-Based Neural Networks](http://arxiv.org/abs/1603.06042v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/syntaxnet)",
      "n": "Andor et al.",
      "d": "2016-03-19",
      "m1": "92.79",
      "m2": "94.61",
      "m3": "97.44"
    },
    {
      "p": "[Distilling an Ensemble of Greedy Dependency Parsers into One MST Parser](http://arxiv.org/abs/1609.07561v1)",
      "c": "[&check;&nbsp;Link](https://github.com/adhigunasurya/distillation_parser)",
      "n": "Distilled neural FOG",
      "d": "2016-09-24",
      "m1": "92.06",
      "m2": "94.26",
      "m3": "97.44"
    },
    {
      "p": "[Structured Training for Neural Network Transition-Based Parsing](http://arxiv.org/abs/1506.06158v1)",
      "c": "",
      "n": "Weiss et al.",
      "d": "2015-06-19",
      "m1": "92.06",
      "m2": "94.01",
      "m3": "97.3"
    },
    {
      "p": "[Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](http://arxiv.org/abs/1603.04351v3)",
      "c": "[&check;&nbsp;Link](https://github.com/elikip/bist-parser)",
      "n": "BIST transition-based parser",
      "d": "2016-03-14",
      "m1": "91.9",
      "m2": "93.99",
      "m3": "97.44"
    },
    {
      "p": "[Training with Exploration Improves a Greedy Stack-LSTM Parser](http://arxiv.org/abs/1603.03793v2)",
      "c": "",
      "n": "Arc-hybrid",
      "d": "2016-03-11",
      "m1": "91.42",
      "m2": "93.56",
      "m3": "97.3"
    },
    {
      "p": "[Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations](http://arxiv.org/abs/1603.04351v3)",
      "c": "[&check;&nbsp;Link](https://github.com/elikip/bist-parser)",
      "n": "BIST graph-based parser",
      "d": "2016-03-14",
      "m1": "91.0",
      "m2": "93.1",
      "m3": "97.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
