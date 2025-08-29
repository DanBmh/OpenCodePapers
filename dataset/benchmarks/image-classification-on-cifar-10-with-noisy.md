# image-classification-on-cifar-10-with-noisy

[Dataset Link](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf) \
Task Hierarchy: ['Image Classification']

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
      "label": "Accuracy (under 20% Sym. label noise)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy (under 50% Sym. label noise)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Accuracy (under 80% Sym. label noise)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Accuracy (under 90% Sym. label noise)",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Accuracy (under 95% Sym. label noise)",
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
      "p": "[SSR: An Efficient and Robust Framework for Learning with Unknown Label Noise](https://arxiv.org/abs/2111.11288v2)",
      "c": "[&check;&nbsp;Link](https://github.com/MrChenFeng/SSR_BMVC2022)",
      "n": "SSR",
      "d": "2021-11-22",
      "m1": "96.74%",
      "m2": "96.13%",
      "m3": "95.56%",
      "m4": "95.17%"
    },
    {
      "p": "[Contrast to Divide: Self-Supervised Pre-Training for Learning with Noisy Labels](https://arxiv.org/abs/2103.13646v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ContrastToDivide/C2D)",
      "n": "C2D (ELR+ with SimCLR, ResNet-34)",
      "d": "2021-03-25",
      "m1": "96.74 \u00b1 0.12",
      "m2": "95.55 \u00b1 0.32",
      "m3": "93.11 \u00b1 0.70",
      "m4": "89.30 \u00b1 0.21",
      "m5": "80.21 \u00b1 1.91"
    },
    {
      "p": "[Sample Prior Guided Robust Model Learning to Suppress Noisy Labels](https://arxiv.org/abs/2112.01197v3)",
      "c": "[&check;&nbsp;Link](https://github.com/bupt-ai-cz/PGDF)",
      "n": "PGDF (ResNet-18)",
      "d": "2021-12-02",
      "m1": "96.7%",
      "m2": "96.3%",
      "m3": "94.7%",
      "m4": "84.0%"
    },
    {
      "p": "[Contrast to Divide: Self-Supervised Pre-Training for Learning with Noisy Labels](https://arxiv.org/abs/2103.13646v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ContrastToDivide/C2D)",
      "n": "C2D (DivideMix with SimCLR, ResNet-18)",
      "d": "2021-03-25",
      "m1": "96.23 \u00b1 0.09",
      "m2": "95.15 \u00b1 0.16",
      "m3": "94.30 \u00b1 0.12",
      "m4": "93.42 \u00b1 0.09",
      "m5": "87.72 \u00b1 2.21"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
