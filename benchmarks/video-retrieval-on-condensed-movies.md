# video-retrieval-on-condensed-movies

[Dataset Link](https://www.robots.ox.ac.uk/~vgg/data/condensed-movies/) \
Task Hierarchy: ['Video Retrieval']

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
      "label": "text-to-video R@1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "text-to-video R@5",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "text-to-video R@10",
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
      "p": "[TESTA: Temporal-Spatial Token Aggregation for Long-form Video-Language Understanding](https://arxiv.org/abs/2310.19060v1)",
      "c": "[&check;&nbsp;Link](https://github.com/renshuhuai-andy/testa)",
      "n": "TESTA (ViT-B/16)",
      "d": "2023-10-29",
      "m1": "24.9",
      "m2": "46.5",
      "m3": "55.1"
    },
    {
      "p": "[VindLU: A Recipe for Effective Video-and-Language Pretraining](https://arxiv.org/abs/2212.05051v2)",
      "c": "[&check;&nbsp;Link](https://github.com/klauscc/vindlu)",
      "n": "VINDLU",
      "d": "2022-12-09",
      "m1": "18.4",
      "m2": "36.4 ",
      "m3": "44.3"
    },
    {
      "p": "[Long-Form Video-Language Pre-Training with Multimodal Temporal Contrastive Learning](https://arxiv.org/abs/2210.06031v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/xpretrain)",
      "n": "LF-VILA ",
      "d": "2022-10-12",
      "m1": "13.6",
      "m2": "32.5",
      "m3": "41.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
