# grammatical-error-correction-on-restricted

[Dataset Link](https://github.com/keisks/jfleg) \
Task Hierarchy: ['Grammatical Error Correction']

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
      "label": "F0.5",
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
      "p": "[A Multilayer Convolutional Encoder-Decoder Neural Network for Grammatical Error Correction](http://arxiv.org/abs/1801.08831v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nusnlp/mlconvgec2018)",
      "n": "CNN Seq2Seq",
      "d": "2018-01-26",
      "m1": "70.14 (measured by Ge et al., 2018)"
    },
    {
      "p": "[Neural Quality Estimation of Grammatical Error Correction](https://aclanthology.org/D18-1274)",
      "c": "[&check;&nbsp;Link](https://github.com/nusnlp/neuqe)",
      "n": "CNN Seq2Seq + Quality Estimation",
      "d": "2018-10-01",
      "m1": "56.52"
    },
    {
      "p": "[Approaching Neural Grammatical Error Correction as a Low-Resource Machine Translation Task](http://arxiv.org/abs/1804.05940v1)",
      "c": "[&check;&nbsp;Link](https://github.com/grammatical/neural-naacl2018)",
      "n": "Transformer",
      "d": "2018-04-16",
      "m1": "55.8"
    },
    {
      "p": "[LM-Critic: Language Models for Unsupervised Grammatical Error Correction](https://arxiv.org/abs/2109.06822v2)",
      "c": "[&check;&nbsp;Link](https://github.com/grammarly/gector)",
      "n": "+ BIFI with no critic",
      "d": "2021-09-14",
      "m1": "18.7"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
