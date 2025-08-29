# point-cloud-registration-on-nuscenes-distant

[Dataset Link]() \
Task Hierarchy: ['3D Point Cloud Interpolation', 'Point Cloud Registration']

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
      "label": "mRR @ Normal Criterion (1.5\u00b0&0.3m)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "RR @ Loose Criterion (5\u00b0&2m), on LoNuScenes",
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
      "p": "[Density-invariant Features for Distant Point Cloud Registration](https://arxiv.org/abs/2307.09788v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liuquan98/gcl)",
      "n": "GCL+KPConv",
      "d": "2023-07-19",
      "m1": "71.5",
      "m2": "86.5"
    },
    {
      "p": "[Density-invariant Features for Distant Point Cloud Registration](https://arxiv.org/abs/2307.09788v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liuquan98/gcl)",
      "n": "GCL+Conv",
      "d": "2023-07-19",
      "m1": "70.2",
      "m2": "82.4"
    },
    {
      "p": "[APR: Online Distant Point Cloud Registration Through Aggregated Point Cloud Reconstruction](https://arxiv.org/abs/2305.02893v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liuquan98/apr)",
      "n": "FCGF+APR(s)",
      "d": "2023-05-04",
      "m1": "62.9",
      "m2": "51.8"
    },
    {
      "p": "[APR: Online Distant Point Cloud Registration Through Aggregated Point Cloud Reconstruction](https://arxiv.org/abs/2305.02893v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liuquan98/apr)",
      "n": "Predator+APR(a)",
      "d": "2023-05-04",
      "m1": "52.2",
      "m2": "62.7"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
