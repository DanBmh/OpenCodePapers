# semantic-textual-similarity-on-senteval

[Dataset Link](https://arxiv.org/abs/1803.05449) \
Task Hierarchy: ['Semantic Textual Similarity']

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
      "label": "MRPC",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "SICK-R",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "SICK-E",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "STS",
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
      "p": "[Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](http://arxiv.org/abs/1804.00079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "GenSen",
      "d": "2018-03-30",
      "m1": "78.6/84.4",
      "m2": "0.888",
      "m3": "87.8",
      "m4": "78.9/78.6"
    },
    {
      "p": "[Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](http://arxiv.org/abs/1705.02364v5)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "InferSent",
      "d": "2017-05-05",
      "m1": "76.2/83.1",
      "m2": "0.884",
      "m3": "86.3",
      "m4": "75.8/75.5"
    },
    {
      "p": "[Discriminative Improvements to Distributional Sentence Similarity](https://aclanthology.org/D13-1090)",
      "c": "",
      "n": "TF-KLD",
      "d": "2013-10-01",
      "m1": "80.4/85.9",
      "m2": "-",
      "m3": "-",
      "m4": "-"
    },
    {
      "p": "[Training Complex Models with Multi-Task Weak Supervision](http://arxiv.org/abs/1810.02840v2)",
      "c": "[&check;&nbsp;Link](https://github.com/HazyResearch/metal)",
      "n": "Snorkel MeTaL(ensemble)",
      "d": "2018-10-05",
      "m1": "91.5/88.5",
      "m2": "-",
      "m3": "-",
      "m4": "90.1/89.7*"
    },
    {
      "p": "[Improving Multi-Task Deep Neural Networks via Knowledge Distillation for Natural Language Understanding](http://arxiv.org/abs/1904.09482v1)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "MT-DNN-ensemble",
      "d": "2019-04-20",
      "m1": "92.7/90.3",
      "m2": "-",
      "m3": "-",
      "m4": "91.1/90.7*"
    },
    {
      "p": "[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "XLNet-Large",
      "d": "2019-06-19",
      "m1": "93.0/90.7",
      "m2": "-",
      "m3": "-",
      "m4": "91.6/91.1*"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
