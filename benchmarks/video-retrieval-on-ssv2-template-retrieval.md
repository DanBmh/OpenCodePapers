# video-retrieval-on-ssv2-template-retrieval

[Dataset Link]() \
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
      "label": "text-to-video R@10",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "text-to-video R@5",
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
      "p": "[Unmasked Teacher: Towards Training-Efficient Video Foundation Models](https://arxiv.org/abs/2303.16058v2)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/unmasked_teacher)",
      "n": "UMT-L (ViT-L/16)",
      "d": "2023-03-28",
      "m1": "90.8",
      "m2": "100.0",
      "m3": "100.0"
    },
    {
      "p": "[vid-TLDR: Training Free Token merging for Light-weight Video Transformer](https://arxiv.org/abs/2403.13347v2)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/vid-tldr)",
      "n": "vid-TLDR (UMT-L)",
      "d": "2024-03-20",
      "m1": "90.2",
      "m2": "100.0",
      "m3": "100.0"
    },
    {
      "p": "[HiTeA: Hierarchical Temporal-Aware Video-Language Pre-training](https://arxiv.org/abs/2212.14546v1)",
      "c": "",
      "n": "HiTeA",
      "d": "2022-12-30",
      "m1": "85.6",
      "m2": "100",
      "m3": "100"
    },
    {
      "p": "[VindLU: A Recipe for Effective Video-and-Language Pretraining](https://arxiv.org/abs/2212.05051v2)",
      "c": "[&check;&nbsp;Link](https://github.com/klauscc/vindlu)",
      "n": "VindLU",
      "d": "2022-12-09",
      "m1": "83.3",
      "m2": "100",
      "m3": "100"
    },
    {
      "p": "[Revealing Single Frame Bias for Video-and-Language Learning](https://arxiv.org/abs/2206.03428v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jayleicn/ClipBERT)",
      "n": "Singularity-temporal",
      "d": "2022-06-07",
      "m1": "77.6",
      "m2": "98.9",
      "m3": "96"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
