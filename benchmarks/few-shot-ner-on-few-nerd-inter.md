# few-shot-ner-on-few-nerd-inter

[Dataset Link](https://ningding97.github.io/fewnerd/) \
Task Hierarchy: ['Named Entity Recognition (NER)', 'Few-shot NER']

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
      "label": "5 way 1~2 shot",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "5 way 5~10 shot",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "10 way 1~2 shot",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "10 way 5~10 shot",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Average",
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
      "p": "[A Multi-Task Semantic Decomposition Framework with Task-specific Pre-training for Few-Shot NER](https://arxiv.org/abs/2308.14533v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dongguanting/msdp-fewshot-ner)",
      "n": "MSDP",
      "d": "2023-08-28",
      "m1": "76.86\u00b10.22",
      "m2": "84.78\u00b10.69",
      "m3": "69.78\u00b10.31",
      "m4": "81.50\u00b10.71"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "JCELRNER",
      "d": null,
      "m1": "71.62\u00b10.44",
      "m2": "76.14\u00b10.20"
    },
    {
      "p": "[NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data](https://arxiv.org/abs/2402.15343v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Serega6678/NuNER)",
      "n": "NuNER",
      "d": "2024-02-23",
      "m1": "67.37\u00b10.31",
      "m2": "73.50\u00b10.09",
      "m3": "66.54\u00b10.40",
      "m4": "71.04\u00b10.14"
    },
    {
      "p": "[HEProto: A Hierarchical Enhancing ProtoNet based on Multi-Task Learning for Few-shot Named Entity Recognition](https://dl.acm.org/doi/abs/10.1145/3583780.3614908)",
      "c": "[&check;&nbsp;Link](https://github.com/fanshu6hao/HEProto)",
      "n": "HEProto",
      "d": "2023-10-21",
      "m1": "66.40\u00b10.18",
      "m2": "72.53\u00b10.11",
      "m3": "60.91\u00b10.20",
      "m4": "68.92\u00b10.20"
    },
    {
      "p": "[Type-Aware Decomposed Framework for Few-Shot Named Entity Recognition](https://arxiv.org/abs/2302.06397v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liyongqi2002/TadNER)",
      "n": "TadNER",
      "d": "2023-02-13",
      "m1": "64.83\u00b10.14",
      "m2": "72.12\u00b10.12",
      "m3": "64.06\u00b10.19",
      "m4": "69.94\u00b10.15"
    },
    {
      "p": "[Decomposed Meta-Learning for Few-Shot Named Entity Recognition](https://arxiv.org/abs/2204.05751v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/vert-papers)",
      "n": "DecomposedMetaNER",
      "d": "2022-04-12",
      "m1": "64.75\u00b10.35",
      "m2": "71.49\u00b10.47",
      "m3": "58.65\u00b10.43",
      "m4": "68.11\u00b10.05"
    },
    {
      "p": "[Decomposed Meta-Learning for Few-Shot Sequence Labeling](https://tellarin.com/borje/papers/taslp24dml.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/vert-papers/tree/master/papers/DecomposedMetaSL)",
      "n": "DecomposedMetaSL",
      "d": "2024-03-04",
      "m1": "62.09\u00b10.93",
      "m2": "71.26\u00b10.15",
      "m3": "55.61\u00b10.32",
      "m4": "67.85\u00b10.18",
      "m5": "63.99"
    },
    {
      "p": "[An Enhanced Span-based Decomposition Method for Few-Shot Sequence Labeling](https://arxiv.org/abs/2109.13023v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wangpeiyi9979/esd)",
      "n": "ESD",
      "d": "2021-09-27",
      "m1": "59.29\u00b11.25",
      "m2": "69.06\u00b10.80",
      "m3": "52.16\u00b10.79",
      "m4": "64.00\u00b10.43"
    },
    {
      "p": "[Language Model Pre-Training with Sparse Latent Typing](https://arxiv.org/abs/2210.12582v2)",
      "c": "[&check;&nbsp;Link](https://github.com/renll/sparselt)",
      "n": "BERT-SparseLT + CONTaiNER",
      "d": "2022-10-23",
      "m1": "57.14",
      "m2": "66.17",
      "m3": "52.75",
      "m4": "62.43"
    },
    {
      "p": "[CONTaiNER: Few-Shot Named Entity Recognition via Contrastive Learning](https://arxiv.org/abs/2109.07589v2)",
      "c": "[&check;&nbsp;Link](https://github.com/psunlpgroup/container)",
      "n": "CONTaiNER",
      "d": "2021-09-15",
      "m1": "55.95",
      "m2": "61.83",
      "m3": "48.35",
      "m4": "57.12"
    },
    {
      "p": "[Few-NERD: A Few-Shot Named Entity Recognition Dataset](https://arxiv.org/abs/2105.07464v6)",
      "c": "[&check;&nbsp;Link](https://github.com/thunlp/Few-NERD)",
      "n": "StructShot",
      "d": "2021-05-16",
      "m1": "51.88\u00b10.69",
      "m2": "57.32\u00b10.63",
      "m3": "43.34\u00b10.10",
      "m4": "49.57\u00b13.08"
    },
    {
      "p": "[Few-NERD: A Few-Shot Named Entity Recognition Dataset](https://arxiv.org/abs/2105.07464v6)",
      "c": "[&check;&nbsp;Link](https://github.com/thunlp/Few-NERD)",
      "n": "NNShot",
      "d": "2021-05-16",
      "m1": "47.24\u00b11.00",
      "m2": "55.64\u00b10.63",
      "m3": "38.87\u00b10.21",
      "m4": "49.57\u00b12.73"
    },
    {
      "p": "[Few-NERD: A Few-Shot Named Entity Recognition Dataset](https://arxiv.org/abs/2105.07464v6)",
      "c": "[&check;&nbsp;Link](https://github.com/thunlp/Few-NERD)",
      "n": "ProtoBERT",
      "d": "2021-05-16",
      "m1": "38.83\u00b11.49",
      "m2": "58.79\u00b10.44",
      "m3": "32.45\u00b10.79",
      "m4": "52.92\u00b10.37"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
