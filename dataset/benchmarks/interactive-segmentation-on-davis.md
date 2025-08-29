# interactive-segmentation-on-davis

[Dataset Link](https://davischallenge.org/) \
Task Hierarchy: ['Interactive Segmentation']

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
      "label": "NoC@90",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "NoC@85",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "NoC@95",
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
      "p": "[CFR-ICL: Cascade-Forward Refinement with Iterative Click Loss for Interactive Image Segmentation](https://arxiv.org/abs/2303.05620v2)",
      "c": "[&check;&nbsp;Link](https://github.com/TitorX/CFR-ICL-Interactive-Segmentation)",
      "n": "ICL CFR-1 (ViT-H, C+L)",
      "d": "2023-03-09",
      "m1": "4.24",
      "m2": "3",
      "m3": "7.50"
    },
    {
      "p": "[FocalClick: Towards Practical Interactive Image Segmentation](https://arxiv.org/abs/2204.02574v2)",
      "c": "[&check;&nbsp;Link](https://github.com/XavierCHEN34/ClickSEG)",
      "n": "FocalClick-B3-S2",
      "d": "2022-04-06",
      "m1": "4.52",
      "m2": "2.92"
    },
    {
      "p": "[MST: Adaptive Multi-Scale Tokens Guided Interactive Segmentation](https://arxiv.org/abs/2401.04403v2)",
      "c": "[&check;&nbsp;Link](https://github.com/hahamyt/mst)",
      "n": "ViT-B+MST+CL",
      "d": "2024-01-09",
      "m1": "4.55"
    },
    {
      "p": "[SimpleClick: Interactive Image Segmentation with Simple Vision Transformers](https://arxiv.org/abs/2210.11006v3)",
      "c": "[&check;&nbsp;Link](https://github.com/uncbiag/simpleclick)",
      "n": "SimpleClick (ViT-H, C+L)",
      "d": "2022-10-20",
      "m1": "4.70",
      "m2": "3.41"
    },
    {
      "p": "[Cascaded Sparse Feature Propagation Network for Interactive Segmentation](https://arxiv.org/abs/2203.05145v3)",
      "c": "[&check;&nbsp;Link](https://github.com/kleinzcy/csfpn)",
      "n": "IA-FP-Net",
      "d": "2022-03-10",
      "m1": "5.22",
      "m2": "4.03"
    },
    {
      "p": "[Reviving Iterative Training with Mask Guidance for Interactive Segmentation](https://arxiv.org/abs/2102.06583v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "RITM (HRNet-32, C+L)",
      "d": "2021-02-12",
      "m1": "5.34",
      "m2": "4.11"
    },
    {
      "p": "[SimpleClick: Interactive Image Segmentation with Simple Vision Transformers](https://arxiv.org/abs/2210.11006v3)",
      "c": "[&check;&nbsp;Link](https://github.com/uncbiag/simpleclick)",
      "n": "SimpleClick (ViT-H, SBD)",
      "d": "2022-10-20",
      "m1": "5.34",
      "m2": "4.20"
    },
    {
      "p": "[Reviving Iterative Training with Mask Guidance for Interactive Segmentation](https://arxiv.org/abs/2102.06583v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "RITM (HRNet18, SBD)",
      "d": "2021-02-12",
      "m1": "5.74",
      "m2": "4.36"
    },
    {
      "p": "[EdgeFlow: Achieving Practical Interactive Segmentation with Edge-Guided Flow](https://arxiv.org/abs/2109.09406v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "EdgeFlow",
      "d": "2021-09-20",
      "m1": "5.77",
      "m2": "4.54"
    },
    {
      "p": "[f-BRS: Rethinking Backpropagating Refinement for Interactive Segmentation](https://arxiv.org/abs/2001.10331v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "f-BRS-B (ResNet-101)",
      "d": "2020-01-28",
      "m1": "7.41",
      "m2": "5.04"
    },
    {
      "p": "[Interactive Image Segmentation via Backpropagating Refinement Scheme](http://openaccess.thecvf.com/content_CVPR_2019/html/Jang_Interactive_Image_Segmentation_via_Backpropagating_Refinement_Scheme_CVPR_2019_paper.html)",
      "c": "",
      "n": "BRS",
      "d": "2019-06-01",
      "m1": "8.24",
      "m2": "5.58"
    },
    {
      "p": "[Interactive Image Segmentation With Latent Diversity](http://openaccess.thecvf.com/content_cvpr_2018/html/Li_Interactive_Image_Segmentation_CVPR_2018_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/intel-isl/Intseg)",
      "n": "Latent diversity",
      "d": "2018-06-01",
      "m1": "9.57",
      "m2": "5.05"
    },
    {
      "p": "[Deep Interactive Object Selection](http://arxiv.org/abs/1603.04042v1)",
      "c": "[&check;&nbsp;Link](https://github.com/intel-isl/Intseg)",
      "n": "DOS with GC",
      "d": "2016-03-13",
      "m1": "12.58",
      "m2": "9.03"
    },
    {
      "p": "[Deep Interactive Object Selection](http://arxiv.org/abs/1603.04042v1)",
      "c": "[&check;&nbsp;Link](https://github.com/intel-isl/Intseg)",
      "n": "DOS w/o GC",
      "d": "2016-03-13",
      "m1": "17.11",
      "m2": "12.52"
    },
    {
      "p": "[Continuous Adaptation for Interactive Object Segmentation by Learning from Corrections](https://arxiv.org/abs/1911.12709v4)",
      "c": "",
      "n": "IA+SA",
      "d": "2019-11-28",
      "m2": "5.16"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
