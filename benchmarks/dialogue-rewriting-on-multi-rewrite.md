# dialogue-rewriting-on-multi-rewrite

[Dataset Link]() \
Task Hierarchy: ['Dialogue Rewriting']

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
      "label": "Rewriting F3",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "BLEU-1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "BLEU-2",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "ROUGE-1",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "ROUGE-2",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Rewriting F1",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "Rewriting F2",
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
      "p": "[Incomplete Utterance Rewriting as Semantic Segmentation](https://arxiv.org/abs/2009.13166v1)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/ContextualSP)",
      "n": "RUN+BERT",
      "d": "2020-09-28",
      "m1": "47.7"
    },
    {
      "p": "[SARG: A Novel Semi Autoregressive Generator for Multi-turn Incomplete Utterance Restoration](https://arxiv.org/abs/2008.01474v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NetEase-GameAI/SARG)",
      "n": "SARG (n_beam=5)",
      "d": "2020-08-04",
      "m1": "46.4",
      "m7": "52.5"
    },
    {
      "p": "[SARG: A Novel Semi Autoregressive Generator for Multi-turn Incomplete Utterance Restoration](https://arxiv.org/abs/2008.01474v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NetEase-GameAI/SARG)",
      "n": "SARG (greedy)",
      "d": "2020-08-04",
      "m2": "92.2",
      "m3": "89.6",
      "m4": "92.1",
      "m5": "86.0",
      "m6": "62.4"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
