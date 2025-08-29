# robot-manipulation-on-mimicgen

[Dataset Link]() \
Task Hierarchy: ['Robot Manipulation']

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
      "label": "Succ. Rate (12 tasks, 100 demo/task)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Succ. Rate (12 tasks, 1000 demo/task)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Succ. Rate (12 tasks, 200 demo/task)",
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
      "p": "[SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space](https://arxiv.org/abs/2507.01723v1)",
      "c": "[&check;&nbsp;Link](https://github.com/amazon-science/Spherical_Diffusion_Policy)",
      "n": "SDP",
      "d": "2025-07-02",
      "m1": "76"
    },
    {
      "p": "[Equivariant Diffusion Policy](https://arxiv.org/abs/2407.01812v3)",
      "c": "[&check;&nbsp;Link](https://github.com/pointW/equidiff)",
      "n": "EquiDiff (Voxel)",
      "d": "2024-07-01",
      "m1": "63.9",
      "m2": "77.9",
      "m3": "72.6"
    },
    {
      "p": "[Equivariant Diffusion Policy](https://arxiv.org/abs/2407.01812v3)",
      "c": "[&check;&nbsp;Link](https://github.com/pointW/equidiff)",
      "n": "EquiDiff (Image)",
      "d": "2024-07-01",
      "m1": "53.7",
      "m2": "79.7",
      "m3": "68.5"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "DP (Evaluated in EquiDiff)",
      "d": null,
      "m1": "42.0",
      "m2": "71.4",
      "m3": "57.8"
    },
    {
      "p": "[3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](https://arxiv.org/abs/2403.03954v7)",
      "c": "[&check;&nbsp;Link](https://github.com/YanjieZe/3D-Diffusion-Policy)",
      "n": "DP3 (Evaluated in EquiDiff)",
      "d": "2024-03-06",
      "m1": "23.9",
      "m2": "56.8",
      "m3": "35.1"
    },
    {
      "p": "[What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](https://arxiv.org/abs/2108.03298v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ARISE-Initiative/robomimic)",
      "n": "BC RNN (Evaluated in EquiDiff)",
      "d": "2021-08-06",
      "m1": "22.9",
      "m2": "70.3",
      "m3": "41.2"
    },
    {
      "p": "[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705v1)",
      "c": "",
      "n": "ACT (Evaluated in EquiDiff)",
      "d": "2023-04-23",
      "m1": "21.3",
      "m2": "63.3",
      "m3": "38.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
