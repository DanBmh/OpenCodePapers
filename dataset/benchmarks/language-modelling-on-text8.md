# language-modelling-on-text8

[Dataset Link](http://mattmahoney.net/dc/textdata.html) \
Task Hierarchy: ['Language Modelling']

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
      "label": "Bit per Character (BPC)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Number of params",
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
      "p": "[Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "GPT-2",
      "d": "2019-02-14",
      "m1": "0.98",
      "m2": "1542M"
    },
    {
      "p": "[Focus Your Attention (with Adaptive IIR Filters)](https://arxiv.org/abs/2305.14952v2)",
      "c": "",
      "n": "Focus",
      "d": "2023-05-24",
      "m1": "0.98",
      "m2": "22M"
    },
    {
      "p": "[Dynamic Evaluation of Transformer Language Models](http://arxiv.org/abs/1904.08378v1)",
      "c": "[&check;&nbsp;Link](https://github.com/benkrause/dynamiceval-transformer)",
      "n": "Transformer-XL + RMS dynamic eval + decay",
      "d": "2019-04-17",
      "m1": "1.038",
      "m2": "277M"
    },
    {
      "p": "[Adaptive Attention Span in Transformers](https://arxiv.org/abs/1905.07799v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/adaptive-span)",
      "n": "24L Transformer + 8K adaptive span",
      "d": "2019-05-19",
      "m1": "1.07",
      "m2": "209M"
    },
    {
      "p": "[Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Transformer-XL - 24 layers",
      "d": "2019-01-09",
      "m1": "1.08",
      "m2": "277M"
    },
    {
      "p": "[Augmenting Self-attention with Persistent Memory](https://arxiv.org/abs/1907.01470v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/x-transformers)",
      "n": "All-attention network - 36 layers",
      "d": "2019-07-02",
      "m1": "1.08",
      "m2": "114M"
    },
    {
      "p": "[Long-Short Transformer: Efficient Transformers for Language and Vision](https://arxiv.org/abs/2107.02192v3)",
      "c": "[&check;&nbsp;Link](https://github.com/keonlee9420/Comprehensive-Transformer-TTS)",
      "n": "Transformer-LS (small)",
      "d": "2021-07-05",
      "m1": "1.09"
    },
    {
      "p": "[Adaptive Attention Span in Transformers](https://arxiv.org/abs/1905.07799v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/adaptive-span)",
      "n": "12L Transformer + 8K adaptive span",
      "d": "2019-05-19",
      "m1": "1.11",
      "m2": "38M"
    },
    {
      "p": "[Augmenting Self-attention with Persistent Memory](https://arxiv.org/abs/1907.01470v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/x-transformers)",
      "n": "All-attention network - 18 layers",
      "d": "2019-07-02",
      "m1": "1.11",
      "m2": "38M"
    },
    {
      "p": "[BP-Transformer: Modelling Long-Range Context via Binary Partitioning](https://arxiv.org/abs/1911.04070v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/transformer)",
      "n": "BP-Transformer - 12 Layers",
      "d": "2019-11-11",
      "m1": "1.11"
    },
    {
      "p": "[Character-Level Language Modeling with Deeper Self-Attention](http://arxiv.org/abs/1808.04444v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/code-prediction-transformer)",
      "n": "64-layer Character Transformer Model",
      "d": "2018-08-09",
      "m1": "1.13",
      "m2": "235M"
    },
    {
      "p": "[Recurrent Highway Networks with Grouped Auxiliary Memory](https://ieeexplore.ieee.org/document/8932404)",
      "c": "[&check;&nbsp;Link](https://github.com/WilliamRo/gam_rhn)",
      "n": "GAM-RHN-10",
      "d": "2019-12-13",
      "m1": "1.157",
      "m2": "44.7M"
    },
    {
      "p": "[Character-Level Language Modeling with Deeper Self-Attention](http://arxiv.org/abs/1808.04444v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/code-prediction-transformer)",
      "n": "12-layer Character Transformer Model",
      "d": "2018-08-09",
      "m1": "1.18",
      "m2": "44M"
    },
    {
      "p": "[Pay Attention when Required](https://arxiv.org/abs/2009.04534v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/LanguageModeling)",
      "n": "PAR Transformer 24B",
      "d": "2020-09-09",
      "m1": "1.18"
    },
    {
      "p": "[Dynamic Evaluation of Neural Sequence Models](http://arxiv.org/abs/1709.07432v2)",
      "c": "[&check;&nbsp;Link](https://github.com/benkrause/dynamic-evaluation)",
      "n": "mLSTM + dynamic eval",
      "d": "2017-09-21",
      "m1": "1.19",
      "m2": "45M"
    },
    {
      "p": "[Discrete Flows: Invertible Generative Models of Discrete Data](https://arxiv.org/abs/1905.10347v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google/edward2)",
      "n": "Bipartite flows (8 flows)",
      "d": "2019-05-24",
      "m1": "1.23"
    },
    {
      "p": "[Recurrent Highway Networks](http://arxiv.org/abs/1607.03474v5)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "Large RHN",
      "d": "2016-07-12",
      "m1": "1.27",
      "m2": "46M"
    },
    {
      "p": "[Multiplicative LSTM for sequence modelling](http://arxiv.org/abs/1609.07959v3)",
      "c": "[&check;&nbsp;Link](https://github.com/astakara48/python_project)",
      "n": "Large mLSTM +emb +WN +VD",
      "d": "2016-09-26",
      "m1": "1.27",
      "m2": "45M"
    },
    {
      "p": "[Hierarchical Multiscale Recurrent Neural Networks](http://arxiv.org/abs/1609.01704v7)",
      "c": "[&check;&nbsp;Link](https://github.com/bolducp/hierarchical-rnn)",
      "n": "LayerNorm HM-LSTM",
      "d": "2016-09-06",
      "m1": "1.29",
      "m2": "35M"
    },
    {
      "p": "[Recurrent Batch Normalization](http://arxiv.org/abs/1603.09025v5)",
      "c": "[&check;&nbsp;Link](https://github.com/cooijmanstim/recurrent-batch-normalization)",
      "n": "BN LSTM",
      "d": "2016-03-30",
      "m1": "1.36",
      "m2": "16M"
    },
    {
      "p": "[Multiplicative LSTM for sequence modelling](http://arxiv.org/abs/1609.07959v3)",
      "c": "[&check;&nbsp;Link](https://github.com/astakara48/python_project)",
      "n": "Unregularised mLSTM",
      "d": "2016-09-26",
      "m1": "1.40",
      "m2": "45M"
    },
    {
      "p": "[Bayesian Flow Networks](https://arxiv.org/abs/2308.07037v5)",
      "c": "[&check;&nbsp;Link](https://github.com/nnaisense/bayesian-flow-networks)",
      "n": "BFN",
      "d": "2023-08-14",
      "m1": "1.41"
    },
    {
      "p": "[Architectural Complexity Measures of Recurrent Neural Networks](http://arxiv.org/abs/1602.08210v3)",
      "c": "",
      "n": "td-LSTM-large",
      "d": "2016-02-26",
      "m1": "1.49"
    },
    {
      "p": "[Architectural Complexity Measures of Recurrent Neural Networks](http://arxiv.org/abs/1602.08210v3)",
      "c": "",
      "n": "td-LSTM (Zhang et al., 2016)",
      "d": "2016-02-26",
      "m1": "1.63"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
