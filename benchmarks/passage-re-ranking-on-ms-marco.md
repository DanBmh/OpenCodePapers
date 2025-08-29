# passage-re-ranking-on-ms-marco

[Dataset Link](https://microsoft.github.io/msmarco/) \
Task Hierarchy: ['Passage Re-Ranking']

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
      "p": "[HLATR: Enhance Multi-stage Text Retrieval with Hybrid List Aware Transformer Reranking](https://arxiv.org/abs/2205.10569v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Alibaba-NLP/HLATR)",
      "n": "HLATR",
      "d": "2022-05-21",
      "m1": "0.42"
    },
    {
      "p": "[Document Expansion by Query Prediction](https://arxiv.org/abs/1904.08375v2)",
      "c": "[&check;&nbsp;Link](https://github.com/castorini/Anserini)",
      "n": "BERT + Doc2query",
      "d": "2019-04-17",
      "m1": "0.368"
    },
    {
      "p": "[Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085v5)",
      "c": "[&check;&nbsp;Link](https://github.com/nyu-dl/dl4marco-bert)",
      "n": "BERT + Small Training",
      "d": "2019-01-13",
      "m1": "0.359"
    },
    {
      "p": "[An Updated Duet Model for Passage Re-ranking](http://arxiv.org/abs/1903.07666v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dfcf93/MSMARCO)",
      "n": "Duet v2",
      "d": "2019-03-18",
      "m1": "0.253"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
