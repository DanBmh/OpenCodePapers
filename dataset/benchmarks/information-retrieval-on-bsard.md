# information-retrieval-on-bsard

[Dataset Link](https://github.com/maastrichtlawtech/bsard) \
Task Hierarchy: ['Information Retrieval']

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
      "label": "Recall@100",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Recall@200",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Recall@500",
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
      "p": "[A Statutory Article Retrieval Dataset in French](https://arxiv.org/abs/2108.11792v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maastrichtlawtech/bsard)",
      "n": "Two-tower Bi-Encoder (RoBERTa)",
      "d": "2021-08-26",
      "m1": "74.78",
      "m2": "78.04",
      "m3": "83.39"
    },
    {
      "p": "[A Statutory Article Retrieval Dataset in French](https://arxiv.org/abs/2108.11792v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maastrichtlawtech/bsard)",
      "n": "Siamese Bi-Encoder (RoBERTa)",
      "d": "2021-08-26",
      "m1": "71.63",
      "m2": "78.38",
      "m3": "83.77"
    },
    {
      "p": "[A Statutory Article Retrieval Dataset in French](https://arxiv.org/abs/2108.11792v2)",
      "c": "[&check;&nbsp;Link](https://github.com/maastrichtlawtech/bsard)",
      "n": "BM25",
      "d": "2021-08-26",
      "m1": "51.33",
      "m2": "56.78",
      "m3": "64.71"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
