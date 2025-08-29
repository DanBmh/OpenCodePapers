# question-answering-on-scde-1

[Dataset Link](https://vgtomahawk.github.io/sced.html) \
Task Hierarchy: ['Question Answering']

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
      "label": "BA",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "PA",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "DE",
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
      "p": "[]()",
      "c": "",
      "n": "albert-xxlarge + APN(baseline)",
      "d": null,
      "m1": "0.852",
      "m2": "0.555",
      "m3": "0.437"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "bert-large-uncased + APN(baseline)",
      "d": null,
      "m1": "0.721",
      "m2": "0.324",
      "m3": "0.699"
    },
    {
      "p": "[SCDE: Sentence Cloze Dataset with High Quality Distractors From Examinations](https://arxiv.org/abs/2004.12934v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shawnkx/SCDE)",
      "n": "bert-large-uncased + APN",
      "d": "2020-04-27",
      "m1": "0.717",
      "m2": "0.299",
      "m3": "0.661"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
