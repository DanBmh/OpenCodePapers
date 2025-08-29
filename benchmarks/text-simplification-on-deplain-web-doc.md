# text-simplification-on-deplain-web-doc

[Dataset Link](https://github.com/rstodden/DEPlain/tree/main/B__Document-level_Corpus/DEplain-web-doc) \
Task Hierarchy: ['', 'Text Simplification']

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
      "n": "long-mBART (trained on DEplain-APA-doc & DEplain-web-doc)",
      "d": "2023-05-30",
      "m1": "49.745",
      "m2": "23.37",
      "m3": "0.445",
      "m4": "57.95"
    },
    {
      "p": "[DEPLAIN: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification](https://arxiv.org/abs/2305.18939v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rstodden/deplain)",
      "n": "long-mBART (trained on DEplain-web-doc)",
      "d": "2023-05-30",
      "m1": "49.584",
      "m2": "23.282",
      "m3": "0.462",
      "m4": "63.5"
    },
    {
      "p": "[DEPLAIN: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification](https://arxiv.org/abs/2305.18939v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rstodden/deplain)",
      "n": "long-mBART (trained on DEplain-APA-doc)",
      "d": "2023-05-30",
      "m1": "43.087",
      "m2": "21.9",
      "m3": "0.377",
      "m4": "64.7"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
