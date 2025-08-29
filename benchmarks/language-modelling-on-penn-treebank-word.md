# language-modelling-on-penn-treebank-word

[Dataset Link](https://catalog.ldc.upenn.edu/docs/LDC95T7/cl93.html) \
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
      "label": "Test perplexity",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Validation perplexity",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Params",
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
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 (Zero-Shot)",
      "d": "2020-05-28",
      "m1": "20.5",
      "m3": "175000M"
    },
    {
      "p": "[Language Models with Transformers](https://arxiv.org/abs/1904.09408v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cgraywang/gluon-nlp-1)",
      "n": "BERT-Large-CAS",
      "d": "2019-04-20",
      "m1": "31.3",
      "m2": "36.1",
      "m3": "395M"
    },
    {
      "p": "[Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "GPT-2",
      "d": "2019-02-14",
      "m1": "35.76",
      "m3": "1542M"
    },
    {
      "p": "[Mogrifier LSTM](https://arxiv.org/abs/1909.01792v2)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/lamb)",
      "n": "Mogrifier LSTM + dynamic eval",
      "d": "2019-09-04",
      "m1": "44.9",
      "m2": "44.8",
      "m3": "24M"
    },
    {
      "p": "[Improving Neural Language Modeling via Adversarial Training](https://arxiv.org/abs/1906.03805v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ChengyueGongR/advsoft)",
      "n": "adversarial + AWD-LSTM-MoS + dynamic eval",
      "d": "2019-06-10",
      "m1": "46.01",
      "m2": "46.63",
      "m3": "22M"
    },
    {
      "p": "[Gradual Learning of Recurrent Neural Networks](http://arxiv.org/abs/1708.08863v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zivaharoni/gradual-learning-rnn)",
      "n": "GL-LWGC + AWD-MoS-LSTM + dynamic eval",
      "d": "2017-08-29",
      "m1": "46.34",
      "m2": "46.64",
      "m3": "26M"
    },
    {
      "p": "[FRAGE: Frequency-Agnostic Word Representation](https://arxiv.org/abs/1809.06858v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ChengyueGongR/FrequencyAgnostic)",
      "n": "FRAGE + AWD-LSTM-MoS + dynamic eval",
      "d": "2018-09-18",
      "m1": "46.54",
      "m2": "47.38",
      "m3": "22M"
    },
    {
      "p": "[Direct Output Connection for a High-Rank Language Model](http://arxiv.org/abs/1808.10143v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab-nlp/doc_lm)",
      "n": "AWD-LSTM-DOC x5",
      "d": "2018-08-30",
      "m1": "47.17",
      "m2": "48.63",
      "m3": "185M"
    },
    {
      "p": "[Improved Language Modeling by Decoding the Past](http://arxiv.org/abs/1808.05908v4)",
      "c": "",
      "n": "Past Decode Reg. + AWD-LSTM-MoS + dyn. eval.",
      "d": "2018-08-14",
      "m1": "47.3",
      "m2": "48.0",
      "m3": "22M"
    },
    {
      "p": "[Advancing State of the Art in Language Modeling](https://arxiv.org/abs/2312.03735v1)",
      "c": "[&check;&nbsp;Link](https://github.com/davidherel/sota_lm)",
      "n": "Ensemble of All",
      "d": "2023-11-28",
      "m1": "47.31",
      "m2": "48.92"
    },
    {
      "p": "[Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](http://arxiv.org/abs/1711.03953v4)",
      "c": "[&check;&nbsp;Link](https://github.com/zihangdai/mos)",
      "n": "AWD-LSTM-MoS + dynamic eval",
      "d": "2017-11-10",
      "m1": "47.69",
      "m2": "48.33",
      "m3": "22M"
    },
    {
      "p": "[Deep Residual Output Layers for Neural Language Generation](https://arxiv.org/abs/1905.05513v2)",
      "c": "[&check;&nbsp;Link](https://github.com/idiap/drill)",
      "n": "AWD-LSTM-DRILL + dynamic eval",
      "d": "2019-05-14",
      "m1": "49.4",
      "m2": "49.5",
      "m3": "24M"
    },
    {
      "p": "[Deep Independently Recurrent Neural Network (IndRNN)](https://arxiv.org/abs/1910.06251v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Sunnydreamrain/IndRNN_pytorch)",
      "n": "Dense IndRNN+dynamic eval",
      "d": "2019-10-11",
      "m1": "50.97"
    },
    {
      "p": "[Dynamic Evaluation of Neural Sequence Models](http://arxiv.org/abs/1709.07432v2)",
      "c": "[&check;&nbsp;Link](https://github.com/benkrause/dynamic-evaluation)",
      "n": "AWD-LSTM + dynamic eval",
      "d": "2017-09-21",
      "m1": "51.1",
      "m2": "51.6",
      "m3": "24M"
    },
    {
      "p": "[Partially Shuffling the Training Data to Improve Language Models](http://arxiv.org/abs/1903.04167v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ofirpress/PartialShuffle)",
      "n": "AWD-LSTM-DOC + Partial Shuffle",
      "d": "2019-03-11",
      "m1": "52.0",
      "m2": "53.79",
      "m3": "23M"
    },
    {
      "p": "[Direct Output Connection for a High-Rank Language Model](http://arxiv.org/abs/1808.10143v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab-nlp/doc_lm)",
      "n": "AWD-LSTM-DOC",
      "d": "2018-08-30",
      "m1": "52.38",
      "m2": "54.12",
      "m3": "23M"
    },
    {
      "p": "[Regularizing and Optimizing LSTM Language Models](http://arxiv.org/abs/1708.02182v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/enas_lm)",
      "n": "AWD-LSTM + continuous cache pointer",
      "d": "2017-08-07",
      "m1": "52.8",
      "m2": "53.9",
      "m3": "24M"
    },
    {
      "p": "[Partially Shuffling the Training Data to Improve Language Models](http://arxiv.org/abs/1903.04167v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ofirpress/PartialShuffle)",
      "n": "AWD-LSTM-MoS + Partial Shuffle",
      "d": "2019-03-11",
      "m1": "53.92",
      "m2": "55.89",
      "m3": "22M"
    },
    {
      "p": "[Trellis Networks for Sequence Modeling](http://arxiv.org/abs/1810.06682v2)",
      "c": "[&check;&nbsp;Link](https://github.com/locuslab/trellisnet)",
      "n": "Trellis Network",
      "d": "2018-10-15",
      "m1": "54.19"
    },
    {
      "p": "[Breaking the Softmax Bottleneck: A High-Rank RNN Language Model](http://arxiv.org/abs/1711.03953v4)",
      "c": "[&check;&nbsp;Link](https://github.com/zihangdai/mos)",
      "n": "AWD-LSTM-MoS",
      "d": "2017-11-10",
      "m1": "54.44",
      "m2": "56.54",
      "m3": "22M"
    },
    {
      "p": "[Learning Associative Inference Using Fast Weight Memory](https://arxiv.org/abs/2011.07831v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ischlag/Fast-Weight-Memory-public)",
      "n": "AWD-FWM Schlag et al. (2020)",
      "d": "2020-11-16",
      "m1": "54.48",
      "m2": "56.76",
      "m3": "24M"
    },
    {
      "p": "[Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context](https://arxiv.org/abs/1901.02860v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Transformer-XL",
      "d": "2019-01-09",
      "m1": "54.55",
      "m2": "56.72",
      "m3": "24M"
    },
    {
      "p": "[AutoDropout: Learning Dropout Patterns to Regularize Deep Networks](https://arxiv.org/abs/2101.01761v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "Transformer-XL + AutoDropout",
      "d": "2021-01-05",
      "m1": "54.9",
      "m2": "58.1"
    },
    {
      "p": "[Pushing the bounds of dropout](http://arxiv.org/abs/1805.09208v2)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/lamb)",
      "n": "2-layer skip-LSTM + dropout tuning ",
      "d": "2018-05-23",
      "m1": "55.3",
      "m2": "57.1",
      "m3": "24M"
    },
    {
      "p": "[Deep Residual Output Layers for Neural Language Generation](https://arxiv.org/abs/1905.05513v2)",
      "c": "[&check;&nbsp;Link](https://github.com/idiap/drill)",
      "n": "AWD-LSTM-DRILL",
      "d": "2019-05-14",
      "m1": "55.7",
      "m2": "58.2",
      "m3": "24M"
    },
    {
      "p": "[DARTS: Differentiable Architecture Search](http://arxiv.org/abs/1806.09055v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/enas_lm)",
      "n": "Differentiable NAS",
      "d": "2018-06-24",
      "m1": "56.1",
      "m2": "58.3",
      "m3": "23M"
    },
    {
      "p": "[Deep Independently Recurrent Neural Network (IndRNN)](https://arxiv.org/abs/1910.06251v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Sunnydreamrain/IndRNN_pytorch)",
      "n": "Dense IndRNN",
      "d": "2019-10-11",
      "m1": "56.37"
    },
    {
      "p": "[Fraternal Dropout](http://arxiv.org/abs/1711.00066v4)",
      "c": "[&check;&nbsp;Link](https://github.com/kondiz/fraternal-dropout)",
      "n": "AWD-LSTM 3-layer with Fraternal dropout",
      "d": "2017-10-31",
      "m1": "56.8",
      "m2": "58.9",
      "m3": "24M"
    },
    {
      "p": "[Deep Equilibrium Models](https://arxiv.org/abs/1909.01377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/locuslab/deq)",
      "n": "DEQ-TrellisNet",
      "d": "2019-09-03",
      "m1": "57.1",
      "m3": "24M"
    },
    {
      "p": "[Regularizing and Optimizing LSTM Language Models](http://arxiv.org/abs/1708.02182v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/enas_lm)",
      "n": "AWD-LSTM",
      "d": "2017-08-07",
      "m1": "57.3",
      "m2": "60.0",
      "m3": "24M"
    },
    {
      "p": "[Efficient Neural Architecture Search via Parameter Sharing](http://arxiv.org/abs/1802.03268v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/enas_lm)",
      "n": "Efficient NAS",
      "d": "2018-02-09",
      "m1": " 58.6",
      "m2": "60.8",
      "m3": "24M"
    },
    {
      "p": "[Neural Architecture Search with Reinforcement Learning](http://arxiv.org/abs/1611.01578v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "NAS-RL",
      "d": "2016-11-05",
      "m1": "64.0",
      "m3": "25M"
    },
    {
      "p": "[Recurrent Highway Networks](http://arxiv.org/abs/1607.03474v5)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "Recurrent highway networks",
      "d": "2016-07-12",
      "m1": "65.4",
      "m2": "67.9",
      "m3": "23M"
    },
    {
      "p": "[Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling](http://arxiv.org/abs/1611.01462v3)",
      "c": "[&check;&nbsp;Link](https://github.com/JianGoForIt/YellowFin_Pytorch)",
      "n": "Inan et al. (2016) - Variational RHN",
      "d": "2016-11-04",
      "m1": "66.0",
      "m2": "68.1"
    },
    {
      "p": "[A Theoretically Grounded Application of Dropout in Recurrent Neural Networks](http://arxiv.org/abs/1512.05287v5)",
      "c": "[&check;&nbsp;Link](https://github.com/HKUST-KnowComp/R-Net)",
      "n": "Gal & Ghahramani (2016) - Variational LSTM (large)",
      "d": "2015-12-16",
      "m1": "75.2",
      "m2": "77.9"
    },
    {
      "p": "[Recurrent Neural Network Regularization](http://arxiv.org/abs/1409.2329v5)",
      "c": "[&check;&nbsp;Link](https://github.com/wojzaremba/lstm)",
      "n": "Zaremba et al. (2014) - LSTM (large)",
      "d": "2014-09-08",
      "m1": "78.4",
      "m2": "82.2"
    },
    {
      "p": "[An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](http://arxiv.org/abs/1803.01271v2)",
      "c": "[&check;&nbsp;Link](https://github.com/timeseriesAI/tsai/tree/main/tsai/models)",
      "n": "LSTM (Bai et al., 2018)",
      "d": "2018-03-04",
      "m1": "78.93"
    },
    {
      "p": "[A Theoretically Grounded Application of Dropout in Recurrent Neural Networks](http://arxiv.org/abs/1512.05287v5)",
      "c": "[&check;&nbsp;Link](https://github.com/HKUST-KnowComp/R-Net)",
      "n": "Gal & Ghahramani (2016) - Variational LSTM (medium)",
      "d": "2015-12-16",
      "m1": "79.7",
      "m2": "81.9"
    },
    {
      "p": "[Recurrent Neural Network Regularization](http://arxiv.org/abs/1409.2329v5)",
      "c": "[&check;&nbsp;Link](https://github.com/wojzaremba/lstm)",
      "n": "Zaremba et al. (2014) - LSTM (medium)",
      "d": "2014-09-08",
      "m1": "82.7",
      "m2": "86.2"
    },
    {
      "p": "[R-Transformer: Recurrent Neural Network Enhanced Transformer](https://arxiv.org/abs/1907.05572v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DSE-MSU/R-transformer)",
      "n": "R-Transformer",
      "d": "2019-07-12",
      "m1": "84.38"
    },
    {
      "p": "[An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](http://arxiv.org/abs/1803.01271v2)",
      "c": "[&check;&nbsp;Link](https://github.com/timeseriesAI/tsai/tree/main/tsai/models)",
      "n": "GRU (Bai et al., 2018)",
      "d": "2018-03-04",
      "m1": "92.48"
    },
    {
      "p": "[Seq-U-Net: A One-Dimensional Causal U-Net for Efficient Sequence Modelling](https://arxiv.org/abs/1911.06393v1)",
      "c": "[&check;&nbsp;Link](https://github.com/f90/Seq-U-Net)",
      "n": "Seq-U-Net",
      "d": "2019-11-14",
      "m1": "107.95",
      "m3": "14.9M"
    },
    {
      "p": "[Seq-U-Net: A One-Dimensional Causal U-Net for Efficient Sequence Modelling](https://arxiv.org/abs/1911.06393v1)",
      "c": "[&check;&nbsp;Link](https://github.com/f90/Seq-U-Net)",
      "n": "TCN",
      "d": "2019-11-14",
      "m1": "108.47",
      "m3": "14.7M"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
