# text-classification-on-dbpedia

[Dataset Link](https://wiki.dbpedia.org/datasets) \
Task Hierarchy: ['Classification', 'Text Classification']

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
      "label": "Error",
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
      "p": "[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "XLNet",
      "d": "2019-06-19",
      "m1": "0.62"
    },
    {
      "p": "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Bidirectional Encoder Representations from Transformers",
      "d": "2018-10-11",
      "m1": "0.64"
    },
    {
      "p": "[Unsupervised Data Augmentation for Consistency Training](https://arxiv.org/abs/1904.12848v6)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/uda)",
      "n": "BERT large",
      "d": "2019-04-29",
      "m1": "0.68"
    },
    {
      "p": "[How to Fine-Tune BERT for Text Classification?](https://arxiv.org/abs/1905.05583v3)",
      "c": "[&check;&nbsp;Link](https://github.com/xuyige/BERT4doc-Classification)",
      "n": "BERT-ITPT-FiT",
      "d": "2019-05-14",
      "m1": "0.68"
    },
    {
      "p": "[Revisiting LSTM Networks for Semi-Supervised Text Classification via Mixed Objective Function](https://arxiv.org/abs/2009.04007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DevSinghSachan/ssl_text_classification)",
      "n": "L MIXED",
      "d": "2020-09-08",
      "m1": "0.7"
    },
    {
      "p": "[Universal Language Model Fine-tuning for Text Classification](http://arxiv.org/abs/1801.06146v5)",
      "c": "[&check;&nbsp;Link](https://github.com/fastai/fastai)",
      "n": "ULMFiT",
      "d": "2018-01-18",
      "m1": "0.80"
    },
    {
      "p": "[Sampling Bias in Deep Active Classification: An Empirical Study](https://arxiv.org/abs/1909.09389v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Xtra-Computing/thundersvm)",
      "n": "ULMFiT (Small data)",
      "d": "2019-09-20",
      "m1": "0.8"
    },
    {
      "p": "[Disconnected Recurrent Neural Networks for Text Categorization](https://aclanthology.org/P18-1215)",
      "c": "",
      "n": "DRNN",
      "d": "2018-07-01",
      "m1": "0.81"
    },
    {
      "p": "[Supervised and Semi-Supervised Text Categorization using LSTM for Region Embeddings](http://arxiv.org/abs/1602.02373v2)",
      "c": "",
      "n": "CNN",
      "d": "2016-02-07",
      "m1": "0.84"
    },
    {
      "p": "[Deep Pyramid Convolutional Neural Networks for Text Categorization](https://aclanthology.org/P17-1052)",
      "c": "[&check;&nbsp;Link](https://github.com/Cheneng/DPCNN)",
      "n": "DPCNN",
      "d": "2017-07-01",
      "m1": "0.88"
    },
    {
      "p": "[Joint Embedding of Words and Labels for Text Classification](http://arxiv.org/abs/1805.04174v1)",
      "c": "[&check;&nbsp;Link](https://github.com/guoyinwang/LEAM)",
      "n": "LEAM",
      "d": "2018-05-10",
      "m1": "0.98"
    },
    {
      "p": "[Explicit Interaction Model towards Text Classification](http://arxiv.org/abs/1811.09386v1)",
      "c": "[&check;&nbsp;Link](https://github.com/NonvolatileMemory/AAAI_2019_EXAM)",
      "n": "EXAM",
      "d": "2018-11-23",
      "m1": "1"
    },
    {
      "p": "[Learning Context-Sensitive Convolutional Filters for Text Processing](http://arxiv.org/abs/1709.08294v3)",
      "c": "",
      "n": "M-ACNN",
      "d": "2017-09-25",
      "m1": "1.07"
    },
    {
      "p": "[Unsupervised Data Augmentation for Consistency Training](https://arxiv.org/abs/1904.12848v6)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/uda)",
      "n": "BERT large UDA",
      "d": "2019-04-29",
      "m1": "1.09"
    },
    {
      "p": "[On Tree-Based Neural Sentence Modeling](http://arxiv.org/abs/1808.09644v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ExplorerFreda/TreeEnc)",
      "n": "Balanced+bi-leaf-RNN",
      "d": "2018-08-29",
      "m1": "1.2"
    },
    {
      "p": "[Compositional Coding Capsule Network with K-Means Routing for Text Classification](https://arxiv.org/abs/1810.09177v5)",
      "c": "[&check;&nbsp;Link](https://github.com/leftthomas/CCCapsNet)",
      "n": "CCCapsNet",
      "d": "2018-10-22",
      "m1": "1.28"
    },
    {
      "p": "[Very Deep Convolutional Networks for Text Classification](http://arxiv.org/abs/1606.01781v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dongjun-Lee/text-classification-models-tf)",
      "n": "VDCN",
      "d": "2016-06-06",
      "m1": "1.29"
    },
    {
      "p": "[Bag of Tricks for Efficient Text Classification](http://arxiv.org/abs/1607.01759v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fastText)",
      "n": "FastText",
      "d": "2016-07-06",
      "m1": "1.4"
    },
    {
      "p": "[Baseline Needs More Love: On Simple Word-Embedding-Based Models and Associated Pooling Mechanisms](http://arxiv.org/abs/1805.09843v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dinghanshen/SWEM)",
      "n": "SWEM-concat",
      "d": "2018-05-24",
      "m1": "1.43"
    },
    {
      "p": "[Character-level Convolutional Networks for Text Classification](http://arxiv.org/abs/1509.01626v3)",
      "c": "[&check;&nbsp;Link](https://github.com/makcedward/nlpaug)",
      "n": "Char-level CNN",
      "d": "2015-09-04",
      "m1": "1.55"
    },
    {
      "p": "[Abstractive Text Classification Using Sequence-to-convolution Neural Networks](https://arxiv.org/abs/1805.07745v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tgisaturday/Seq2CNN)",
      "n": "Seq2CNN(50)",
      "d": "2018-05-20",
      "m1": "2.77"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
