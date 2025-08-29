# constituency-parsing-on-penn-treebank

[Dataset Link](https://catalog.ldc.upenn.edu/docs/LDC95T7/cl93.html) \
Task Hierarchy: ['Constituency Parsing']

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
      "label": "F1 score",
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
      "p": "[To be Continuous, or to be Discrete, Those are Bits of Questions](https://arxiv.org/abs/2406.07812v1)",
      "c": "[&check;&nbsp;Link](https://github.com/speedcell4/parserker)",
      "n": "Hashing + XLNet",
      "d": "2024-06-12",
      "m1": "96.43"
    },
    {
      "p": "[Improving Constituency Parsing with Span Attention](https://arxiv.org/abs/2010.07543v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cuhksz-nlp/SAPar)",
      "n": "SAPar + XLNet",
      "d": "2020-10-15",
      "m1": "96.40"
    },
    {
      "p": "[Rethinking Self-Attention: Towards Interpretability in Neural Parsing](https://arxiv.org/abs/1911.03875v3)",
      "c": "[&check;&nbsp;Link](https://github.com/KhalilMrini/LAL-Parser)",
      "n": "Label Attention Layer + HPSG + XLNet",
      "d": "2019-11-10",
      "m1": "96.38"
    },
    {
      "p": "[Strongly Incremental Constituency Parsing with Graph Neural Networks](https://arxiv.org/abs/2010.14568v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "Attach-Juxtapose Parser + XLNet",
      "d": "2020-10-27",
      "m1": "96.34"
    },
    {
      "p": "[Head-Driven Phrase Structure Grammar Parsing on Penn Treebank](https://arxiv.org/abs/1907.02684v4)",
      "c": "[&check;&nbsp;Link](https://github.com/DoodleJZ/HPSG-Neural-Parser)",
      "n": "Head-Driven Phrase Structure Grammar Parsing (Joint) + XLNet",
      "d": "2019-07-05",
      "m1": "96.33"
    },
    {
      "p": "[Fast and Accurate Neural CRF Constituency Parsing](https://arxiv.org/abs/2008.03736v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "CRF Parser + RoBERTa",
      "d": "2020-08-09",
      "m1": "96.32"
    },
    {
      "p": "[To be Continuous, or to be Discrete, Those are Bits of Questions](https://arxiv.org/abs/2406.07812v1)",
      "c": "[&check;&nbsp;Link](https://github.com/speedcell4/parserker)",
      "n": "Hashing + Bert",
      "d": "2024-06-12",
      "m1": "96.03"
    },
    {
      "p": "[N-ary Constituent Tree Parsing with Recursive Semi-Markov Model](https://aclanthology.org/2021.acl-long.205/)",
      "c": "[&check;&nbsp;Link](https://github.com/NP-NET-research/Recursive-Semi-Markov-Model)",
      "n": "N-ary semi-markov + BERT-large",
      "d": "2021-07-26",
      "m1": "95.92"
    },
    {
      "p": "[Investigating Non-local Features for Neural Constituency Parsing](https://arxiv.org/abs/2109.12814v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ringos/nfc-parser)",
      "n": "NFC + BERT-large",
      "d": "2021-09-27",
      "m1": "95.92"
    },
    {
      "p": "[Head-Driven Phrase Structure Grammar Parsing on Penn Treebank](https://arxiv.org/abs/1907.02684v4)",
      "c": "[&check;&nbsp;Link](https://github.com/DoodleJZ/HPSG-Neural-Parser)",
      "n": "Head-Driven Phrase Structure Grammar Parsing (Joint) + BERT",
      "d": "2019-07-05",
      "m1": "95.84"
    },
    {
      "p": "[Fast and Accurate Neural CRF Constituency Parsing](https://arxiv.org/abs/2008.03736v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "CRF Parser + BERT",
      "d": "2020-08-09",
      "m1": "95.69"
    },
    {
      "p": "[Cloze-driven Pretraining of Self-attention Networks](http://arxiv.org/abs/1903.07785v1)",
      "c": "",
      "n": "CNN Large + fine-tune",
      "d": "2019-03-19",
      "m1": "95.6"
    },
    {
      "p": "[Generalizing Natural Language Analysis through Span-relation Representations](https://arxiv.org/abs/1911.03822v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jzbjyb/SpanRel)",
      "n": "SpanRel",
      "d": "2019-11-10",
      "m1": "95.5"
    },
    {
      "p": "[Tetra-Tagging: Word-Synchronous Parsing with Linear-Time Inference](https://arxiv.org/abs/1904.09745v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "Tetra Tagging",
      "d": "2019-04-22",
      "m1": "95.44"
    },
    {
      "p": "[Constituency Parsing with a Self-Attentive Encoder](http://arxiv.org/abs/1805.01052v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nikitakit/self-attentive-parser)",
      "n": "Self-attentive encoder + ELMo",
      "d": "2018-05-02",
      "m1": "95.13"
    },
    {
      "p": "[Improving Neural Parsing by Disentangling Model Combination and Reranking Effects](http://arxiv.org/abs/1707.03058v1)",
      "c": "",
      "n": "Model combination",
      "d": "2017-07-10",
      "m1": "94.66"
    },
    {
      "p": "[Direct Output Connection for a High-Rank Language Model](http://arxiv.org/abs/1808.10143v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab-nlp/doc_lm)",
      "n": "LSTM Encoder-Decoder + LSTM-LM",
      "d": "2018-08-30",
      "m1": "94.47"
    },
    {
      "p": "[An Empirical Study of Building a Strong Baseline for Constituency Parsing](https://aclanthology.org/P18-2097)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab-nlp/strong_s2s_baseline_parser)",
      "n": "LSTM Encoder-Decoder + LSTM-LM",
      "d": "2018-07-01",
      "m1": "94.32"
    },
    {
      "p": "[In-Order Transition-based Constituent Parsing](http://arxiv.org/abs/1707.05000v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hantek/distance-parser)",
      "n": "In-order",
      "d": "2017-07-17",
      "m1": "94.2"
    },
    {
      "p": "[Fast and Accurate Neural CRF Constituency Parsing](https://arxiv.org/abs/2008.03736v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yzhangcs/parser)",
      "n": "CRF Parser",
      "d": "2020-08-09",
      "m1": "94.12"
    },
    {
      "p": "[Parsing as Language Modeling](https://aclanthology.org/D16-1257)",
      "c": "[&check;&nbsp;Link](https://github.com/cdg720/emnlp2016)",
      "n": "Semi-supervised LSTM-LM",
      "d": "2016-11-01",
      "m1": "93.8"
    },
    {
      "p": "[What Do Recurrent Neural Network Grammars Learn About Syntax?](http://arxiv.org/abs/1611.05774v2)",
      "c": "[&check;&nbsp;Link](https://github.com/clab/rnng)",
      "n": "Stack-only RNNG",
      "d": "2016-11-17",
      "m1": "93.6"
    },
    {
      "p": "[Attention Is All You Need](https://arxiv.org/abs/1706.03762v7)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Transformer",
      "d": "2017-06-12",
      "m1": "92.7"
    },
    {
      "p": "[Syntactic Parse Fusion](https://aclanthology.org/D15-1160)",
      "c": "[&check;&nbsp;Link](https://github.com/BLLIP/bllip-parser)",
      "n": "Parse fusion",
      "d": "2015-09-01",
      "m1": "92.6"
    },
    {
      "p": "[Grammar as a Foreign Language](http://arxiv.org/abs/1412.7449v3)",
      "c": "[&check;&nbsp;Link](https://github.com/atpaino/deep-text-corrector)",
      "n": "Semi-supervised LSTM",
      "d": "2014-12-23",
      "m1": "92.1"
    },
    {
      "p": "[Effective Self-Training for Parsing](https://www.researchgate.net/publication/262408350_Effective_self-training_for_parsing)",
      "c": "[&check;&nbsp;Link](https://github.com/BLLIP/bllip-parser)",
      "n": "Self-training",
      "d": "2006-06-01",
      "m1": "92.1"
    },
    {
      "p": "[Recurrent Neural Network Grammars](http://arxiv.org/abs/1602.07776v4)",
      "c": "[&check;&nbsp;Link](https://github.com/clab/rnng)",
      "n": "RNN Grammar",
      "d": "2016-02-25",
      "m1": "\ufeff93.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
