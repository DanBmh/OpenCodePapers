# boundary-detection-on-coauthor

[Dataset Link](https://coauthor.stanford.edu/) \
Task Hierarchy: ['Boundary Detection']

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
      "label": "Cohen\u2019s Kappa score",
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
      "p": "[GigaCheck: Detecting LLM-generated Content](https://arxiv.org/abs/2410.23728v2)",
      "c": "",
      "n": "GigaCheck (Mistral-7B-v0.3)",
      "d": "2024-10-31",
      "m1": "0.4158"
    },
    {
      "p": "[Detecting AI-Generated Sentences in Human-AI Collaborative Hybrid Texts: Challenges, Strategies, and Insights](https://arxiv.org/abs/2403.03506v4)",
      "c": "[&check;&nbsp;Link](https://github.com/douglashiwo/aisentencedetection)",
      "n": "DeBERTa-v3 (Naive)",
      "d": "2024-03-06",
      "m1": "0.4002"
    },
    {
      "p": "[GigaCheck: Detecting LLM-generated Content](https://arxiv.org/abs/2410.23728v2)",
      "c": "",
      "n": "GigaCheck (DN-DAB-DETR)",
      "d": "2024-10-31",
      "m1": "0.1885"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
