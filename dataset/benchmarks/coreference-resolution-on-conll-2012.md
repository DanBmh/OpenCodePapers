# coreference-resolution-on-conll-2012

[Dataset Link](https://www.aclweb.org/anthology/W12-4501.pdf) \
Task Hierarchy: ['Coreference Resolution']

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
      "label": "Avg F1",
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
      "p": "[Maverick: Efficient and Accurate Coreference Resolution Defying Recent Trends](https://arxiv.org/abs/2407.21489v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sapienzanlp/maverick-coref)",
      "n": "Maverick_mes",
      "d": "2024-07-31",
      "m1": "83.6"
    },
    {
      "p": "[Coreference Resolution through a seq2seq Transition-Based System](https://arxiv.org/abs/2211.12142v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "seq2seq",
      "d": "2022-11-22",
      "m1": "83.3"
    },
    {
      "p": "[CorefQA: Coreference Resolution as Query-based Span Prediction](https://aclanthology.org/2020.acl-main.622)",
      "c": "[&check;&nbsp;Link](https://github.com/ShannonAI/CorefQA)",
      "n": "CorefQA + SpanBERT-large",
      "d": "2020-07-01",
      "m1": "83.1"
    },
    {
      "p": "[Autoregressive Structured Prediction with Language Models](https://arxiv.org/abs/2210.14698v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lyutyuh/asp)",
      "n": "ASP+T0-3B",
      "d": "2022-10-26",
      "m1": "82.3"
    },
    {
      "p": "[Word-Level Coreference Resolution](https://arxiv.org/abs/2109.04127v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vdobrovolskii/wl-coref)",
      "n": "wl-coref + RoBERTa",
      "d": "2021-09-09",
      "m1": "81.0"
    },
    {
      "p": "[Coreference Resolution without Span Representations](https://arxiv.org/abs/2101.00434v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yuvalkirstain/s2e-coref)",
      "n": "s2e + Longformer-Large",
      "d": "2021-01-02",
      "m1": "80.3"
    },
    {
      "p": "[Revealing the Myth of Higher-Order Inference in Coreference Resolution](https://arxiv.org/abs/2009.12013v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lxucs/coref-hoi)",
      "n": "SpanBERT + Cluster Merging",
      "d": "2020-09-25",
      "m1": "80.2"
    },
    {
      "p": "[Coreference Resolution without Span Representations](https://arxiv.org/abs/2101.00434v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yuvalkirstain/s2e-coref)",
      "n": "c2f + SpanBERT-Large",
      "d": "2021-01-02",
      "m1": "80.2"
    },
    {
      "p": "[CorefQA: Coreference Resolution as Query-based Span Prediction](https://aclanthology.org/2020.acl-main.622)",
      "c": "[&check;&nbsp;Link](https://github.com/ShannonAI/CorefQA)",
      "n": "CorefQA + SpanBERT-base",
      "d": "2020-07-01",
      "m1": "79.9"
    },
    {
      "p": "[Learning to Ignore: Long Document Coreference with Bounded Memory Neural Networks](https://arxiv.org/abs/2010.02807v3)",
      "c": "[&check;&nbsp;Link](https://github.com/shtoshni/fast-coref)",
      "n": "U-MEM* + SpanBERT-large",
      "d": "2020-10-06",
      "m1": "79.6"
    },
    {
      "p": "[BERT for Coreference Resolution: Baselines and Analysis](https://arxiv.org/abs/1908.09091v4)",
      "c": "[&check;&nbsp;Link](https://github.com/mandarjoshi90/coref)",
      "n": "c2f-coref + BERT-large",
      "d": "2019-08-24",
      "m1": "76.9"
    },
    {
      "p": "[Coreference Resolution with Entity Equalization](https://aclanthology.org/P19-1066)",
      "c": "[&check;&nbsp;Link](https://github.com/kkjawz/coref-ee)",
      "n": "EE + BERT-large",
      "d": "2019-07-01",
      "m1": "76.61"
    },
    {
      "p": "[A Cluster Ranking Model for Full Anaphora Resolution](https://arxiv.org/abs/1911.09532v2)",
      "c": "[&check;&nbsp;Link](https://github.com/juntaoy/dali-full-anaphora)",
      "n": "dali-full-anaphora",
      "d": "2019-11-21",
      "m1": "76.4"
    },
    {
      "p": "[End-to-end Deep Reinforcement Learning Based Coreference Resolution](https://aclanthology.org/P19-1064)",
      "c": "",
      "n": "reinforced model + ELMO",
      "d": "2019-07-01",
      "m1": "73.8"
    },
    {
      "p": "[Higher-order Coreference Resolution with Coarse-to-fine Inference](http://arxiv.org/abs/1804.05392v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kentonl/e2e-coref)",
      "n": "c2f-coref + ELMo",
      "d": "2018-04-15",
      "m1": "73.0"
    },
    {
      "p": "[End-to-end Neural Coreference Resolution](http://arxiv.org/abs/1707.07045v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kentonl/e2e-coref)",
      "n": "e2e-coref + ELMo",
      "d": "2017-07-21",
      "m1": "70.4"
    },
    {
      "p": "[End-to-end Neural Coreference Resolution](http://arxiv.org/abs/1707.07045v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kentonl/e2e-coref)",
      "n": "e2e-coref (ensemble)",
      "d": "2017-07-21",
      "m1": "68.8"
    },
    {
      "p": "[End-to-end Neural Coreference Resolution](http://arxiv.org/abs/1707.07045v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kentonl/e2e-coref)",
      "n": "e2e-coref (single)",
      "d": "2017-07-21",
      "m1": "67.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
