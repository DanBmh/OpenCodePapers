# answer-selection-on-asnq

[Dataset Link](https://github.com/alexa/wqa_tanda) \
Task Hierarchy: ['Question Answering', 'Answer Selection']

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
      "label": "MAP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "MRR",
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
      "p": "[Pre-training Transformer Models with Sentence-Level Objectives for Answer Sentence Selection](https://arxiv.org/abs/2205.10455v2)",
      "c": "",
      "n": "DeBERTa-V3-Large + SSP",
      "d": "2022-05-20",
      "m1": "0.743",
      "m2": "0.800"
    },
    {
      "p": "[Pre-training Transformer Models with Sentence-Level Objectives for Answer Sentence Selection](https://arxiv.org/abs/2205.10455v2)",
      "c": "",
      "n": "ELECTRA-Base + SSP",
      "d": "2022-05-20",
      "m1": "0.697",
      "m2": "0.757"
    },
    {
      "p": "[Paragraph-based Transformer Pre-training for Multi-Sentence Inference](https://arxiv.org/abs/2205.01228v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amazon-research/wqa-multi-sentence-inference)",
      "n": "RoBERTa-Base Joint MSPP",
      "d": "2022-05-02",
      "m1": "0.673",
      "m2": "0.737"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
