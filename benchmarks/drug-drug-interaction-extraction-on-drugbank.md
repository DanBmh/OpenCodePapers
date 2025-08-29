# drug-drug-interaction-extraction-on-drugbank

[Dataset Link](https://go.drugbank.com/) \
Task Hierarchy: ['Information Extraction', 'Drug–drug Interaction Extraction']

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
      "label": "AUROC",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "F1 score",
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
      "p": "[CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions](https://arxiv.org/abs/2403.17210v2)",
      "c": "",
      "n": "Ours (CADGL)",
      "d": "2024-03-25",
      "m1": "99.49",
      "m2": "98.21",
      "m3": "97.79"
    },
    {
      "p": "[SSI\u2013DDI: Substructure\u2013Substructure Interactions for Drug\u2013Drug Interaction Prediction](https://academic.oup.com/bib/article-abstract/22/6/bbab133/6265181?redirectedFrom=fulltext)",
      "c": "[&check;&nbsp;Link](https://github.com/AstraZeneca/chemicalx)",
      "n": "SSI-DDI",
      "d": "2021-11-07",
      "m1": "98.95",
      "m2": "96.33",
      "m3": "96.38"
    },
    {
      "p": "[Drug-Drug Adverse Effect Prediction with Graph Co-Attention](http://arxiv.org/abs/1905.00534v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AstraZeneca/chemicalx)",
      "n": "MHCA-DDI",
      "d": "2019-05-02",
      "m1": "86.33",
      "m2": "78.51",
      "m3": "83.31"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
