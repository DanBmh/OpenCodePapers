# text-summarization-on-reddit-tifu

[Dataset Link](http://snap.stanford.edu/graphsage/) \
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
      "p": "[Calibrating Sequence likelihood Improves Conditional Language Generation](https://arxiv.org/abs/2210.00045v1)",
      "c": "",
      "n": "PEGASUS 2B + SLiC",
      "d": "2022-09-30",
      "m1": "32.03",
      "m2": "11.13",
      "m3": "25.51"
    },
    {
      "p": "[Better Fine-Tuning by Reducing Representational Collapse](https://arxiv.org/abs/2008.03156v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pytorch/fairseq/tree/master/examples/rxf)",
      "n": "BART+R3F",
      "d": "2020-08-06",
      "m1": "30.31",
      "m2": "10.98",
      "m3": "24.74"
    },
    {
      "p": "[Muppet: Massive Multi-task Representations with Pre-Finetuning](https://arxiv.org/abs/2101.11038v1)",
      "c": "[&check;&nbsp;Link](https://huggingface.co/facebook/muppet-roberta-base)",
      "n": "MUPPET BART Large",
      "d": "2021-01-26",
      "m1": "30.3",
      "m2": "11.25",
      "m3": "24.92"
    },
    {
      "p": "[SummaReranker: A Multi-Task Mixture-of-Experts Re-ranking Framework for Abstractive Summarization](https://arxiv.org/abs/2203.06569v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ntunlp/summareranker)",
      "n": "PEGASUS + SummaReranker",
      "d": "2022-03-13",
      "m1": "29.83",
      "m2": "9.5",
      "m3": "23.47"
    },
    {
      "p": "[Extractive Summarization as Text Matching](https://arxiv.org/abs/2004.08795v1)",
      "c": "[&check;&nbsp;Link](https://github.com/maszhongming/MatchSum)",
      "n": "MatchSum",
      "d": "2020-04-19",
      "m1": "25.09",
      "m2": "6.17",
      "m3": "20.13"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
