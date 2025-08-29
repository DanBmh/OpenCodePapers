# text-simplification-on-deplain-apa-doc

[Dataset Link](https://github.com/rstodden/DEPlain/tree/main/B__Document-level_Corpus/DEplain-APA-doc) \
Task Hierarchy: ['Text Simplification']

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
      "label": "SARI (EASSE>=0.2.1)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "BLEU",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "BertScore (Precision)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "FRE (Flesch Reading Ease)",
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
      "p": "[DEPLAIN: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification](https://arxiv.org/abs/2305.18939v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rstodden/deplain)",
      "n": "long-mBART (trained on DEplain-APA-doc)",
      "d": "2023-05-30",
      "m1": "44.56",
      "m2": "38.136",
      "m3": "0.598",
      "m4": "65.4"
    },
    {
      "p": "[DEPLAIN: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification](https://arxiv.org/abs/2305.18939v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rstodden/deplain)",
      "n": "long-mBART (trained on DEplain-APA-doc & DEplain-web-doc)",
      "d": "2023-05-30",
      "m1": "42.862",
      "m2": "36.449",
      "m3": "0.589",
      "m4": "65.4"
    },
    {
      "p": "[DEPLAIN: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification](https://arxiv.org/abs/2305.18939v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rstodden/deplain)",
      "n": "long-mBART (trained on DEplain-web-doc)",
      "d": "2023-05-30",
      "m1": "35.02",
      "m2": "12.913",
      "m3": "0.475",
      "m4": "59.55"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
