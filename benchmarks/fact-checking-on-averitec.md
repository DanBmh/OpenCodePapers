# fact-checking-on-averitec

[Dataset Link](https://fever.ai/dataset/averitec.html) \
Task Hierarchy: ['Fact Checking']

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
      "label": "Question Only score",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Question + Answer score",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "AveriTeC",
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
      "p": "[HerO at AVeriTeC: The Herd of Open Large Language Models for Verifying Real-World Claims](https://arxiv.org/abs/2410.12377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ssu-humane/hero)",
      "n": "HerO",
      "d": "2024-10-16",
      "m1": "0.48",
      "m2": "0.35",
      "m3": "0.57"
    },
    {
      "p": "[AIC CTU system at AVeriTeC: Re-framing automated fact-checking as a simple RAG task](https://arxiv.org/abs/2410.11446v1)",
      "c": "[&check;&nbsp;Link](https://github.com/aic-factcheck/aic_averitec)",
      "n": "CTU AIC",
      "d": "2024-10-15",
      "m1": "0.46",
      "m2": "0.32",
      "m3": "0.5"
    },
    {
      "p": "[InFact: A Strong Baseline for Automated Fact-Checking](https://aclanthology.org/2024.fever-1.12/)",
      "c": "",
      "n": "InFact",
      "d": "2024-11-01",
      "m1": "0.45",
      "m2": "0.34",
      "m3": "0.63"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
