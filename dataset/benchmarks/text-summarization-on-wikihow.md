# text-summarization-on-wikihow

[Dataset Link](https://github.com/mahnazkoupaee/WikiHow-Dataset) \
Task Hierarchy: ['Text Summarization']

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
      "label": "ROUGE-1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "ROUGE-2",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "ROUGE-L",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Content F1",
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
      "p": "[Abstractive Summarization of Spoken andWritten Instructions with BERT](https://arxiv.org/abs/2008.09676)",
      "c": "[&check;&nbsp;Link](https://github.com/nlpyang/PreSumm)",
      "n": "BertSum",
      "d": "2020-08-21",
      "m1": "35.91",
      "m2": "13.9",
      "m3": "34.82",
      "m4": "29.8"
    },
    {
      "p": "[Extractive Summarization as Text Matching](https://arxiv.org/abs/2004.08795v1)",
      "c": "[&check;&nbsp;Link](https://github.com/maszhongming/MatchSum)",
      "n": "MatchSum (BERT-base)",
      "d": "2020-04-19",
      "m1": "31.85",
      "m2": "8.98",
      "m3": "29.58"
    },
    {
      "p": "[WikiHow: A Large Scale Text Summarization Dataset](http://arxiv.org/abs/1810.09305v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wikidepia/indonesian_datasets)",
      "n": "Pointer-generator + coverage",
      "d": "2018-10-18",
      "m1": "28.53",
      "m2": "9.23",
      "m3": "26.54"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
