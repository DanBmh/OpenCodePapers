# supervised-video-summarization-on-summe

[Dataset Link](https://gyglim.github.io/me/vsum/index.html) \
Task Hierarchy: ['Video Summarization', 'Supervised Video Summarization']

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
      "label": "F1-score (Canonical)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "F1-score (Augmented)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Kendall's Tau",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Spearman's Rho",
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
      "p": "[Combining Global and Local Attention with Positional Encoding for Video Summarization](https://www.iti.gr/~bmezaris/publications/ism2021a_preprint.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/e-apostolidis/PGL-SUM)",
      "n": "PGL-SUM (maximum learning capacity)",
      "d": "2021-12-01",
      "m1": "57.1"
    },
    {
      "p": "[Combining Global and Local Attention with Positional Encoding for Video Summarization](https://www.iti.gr/~bmezaris/publications/ism2021a_preprint.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/e-apostolidis/PGL-SUM)",
      "n": "PGL-SUM",
      "d": "2021-12-01",
      "m1": "55.6"
    },
    {
      "p": "[Align and Attend: Multimodal Summarization with Dual Contrastive Losses](https://arxiv.org/abs/2303.07284v3)",
      "c": "[&check;&nbsp;Link](https://github.com/boheumd/A2Summ)",
      "n": "A2Summ",
      "d": "2023-03-13",
      "m1": "55.0",
      "m3": "0.108",
      "m4": "0.129"
    },
    {
      "p": "[Joint Video Summarization and Moment Localization by Cross-Task Sample Transfer](http://openaccess.thecvf.com//content/CVPR2022/html/Jiang_Joint_Video_Summarization_and_Moment_Localization_by_Cross-Task_Sample_Transfer_CVPR_2022_paper.html)",
      "c": "",
      "n": "iPTNet",
      "d": "2022-01-01",
      "m1": "54.5",
      "m2": "56.9",
      "m3": "0.101",
      "m4": "0.119"
    },
    {
      "p": "[Query Twice: Dual Mixture Attention Meta Learning for Video Summarization](https://arxiv.org/abs/2008.08360v1)",
      "c": "",
      "n": "DMASum",
      "d": "2020-08-19",
      "m1": "54.3",
      "m3": "0.063",
      "m4": "0.089"
    },
    {
      "p": "[CLIP-It! Language-Guided Video Summarization](https://arxiv.org/abs/2107.00650v2)",
      "c": "[&check;&nbsp;Link](https://github.com/srpkdyy/CLIP-It)",
      "n": "CLIP-It",
      "d": "2021-07-01",
      "m1": "54.2",
      "m2": "56.4"
    },
    {
      "p": "[Relational Reasoning Over Spatial-Temporal Graphs for Video Summarization](https://ieeexplore.ieee.org/abstract/document/9750933)",
      "c": "",
      "n": "RR-STG",
      "d": "2022-04-06",
      "m1": "53.4",
      "m2": "54.8",
      "m3": "0.211",
      "m4": "0.234"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "MSVA",
      "d": "2021-04-23",
      "m1": "53.4",
      "m3": "0.200",
      "m4": "0.230"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "MC-VSA [DBLP:journals/corr/abs-2006-01410]",
      "d": "2021-04-23",
      "m1": "51.6"
    },
    {
      "p": "[Progressive Video Summarization via Multimodal Self-supervised Learning](https://arxiv.org/abs/2201.02494v4)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "SSPVS(+Text)",
      "d": "2022-01-07",
      "m1": "50.7",
      "m3": "0.192",
      "m4": "0.257"
    },
    {
      "p": "[Video Joint Modelling Based on Hierarchical Transformer for Co-summarization](https://arxiv.org/abs/2112.13478v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "VJMHT",
      "d": "2021-12-27",
      "m1": "50.6",
      "m2": "51.7",
      "m3": "0.106",
      "m4": "0.108"
    },
    {
      "p": "[DSNet: A Flexible Detect-to-Summarize Network for Video Summarization](https://ieeexplore.ieee.org/document/9275314)",
      "c": "[&check;&nbsp;Link](https://github.com/li-plus/DSNet)",
      "n": "DSNet",
      "d": "2020-12-01",
      "m1": "50.2",
      "m2": "50.7"
    },
    {
      "p": "[Progressive Video Summarization via Multimodal Self-supervised Learning](https://arxiv.org/abs/2201.02494v4)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "SSPVS",
      "d": "2022-01-07",
      "m1": "48.7",
      "m2": "50.4",
      "m3": "0.178",
      "m4": "0.240"
    },
    {
      "p": "[Discriminative Feature Learning for Unsupervised Video Summarization](http://arxiv.org/abs/1811.09791v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wildoctopus/SADNet)",
      "n": "CSNet",
      "d": "2018-11-24",
      "m1": "48.6",
      "m2": "48.7"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "VASNet [DBLP:conf/accv/FajtlSAMR18]",
      "d": "2021-04-23",
      "m1": "48",
      "m3": "0.160",
      "m4": "0.170"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "re-SEQ2SEQ [DBLP:conf/eccv/ZhangGS18]",
      "d": "2021-04-23",
      "m1": "44.9"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "M-AVS [DBLP:journals/corr/abs-1708-09545]",
      "d": "2021-04-23",
      "m1": "44.4"
    },
    {
      "p": "[Hierarchical Multimodal Transformer to Summarize Videos](https://arxiv.org/abs/2109.10559v1)",
      "c": "",
      "n": "HMT",
      "d": "2021-09-22",
      "m1": "44.1",
      "m2": "44.8",
      "m3": "0.079",
      "m4": "0.080"
    },
    {
      "p": "[Supervised Video Summarization via Multiple Feature Sets with Parallel Attention](https://arxiv.org/abs/2104.11530v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "MAVS [DBLP:conf/mm/FengLKZ18]",
      "d": "2021-04-23",
      "m1": "43.1"
    },
    {
      "p": "[Deep Reinforcement Learning for Unsupervised Video Summarization with Diversity-Representativeness Reward](http://arxiv.org/abs/1801.00054v3)",
      "c": "[&check;&nbsp;Link](https://github.com/KaiyangZhou/pytorch-vsumm-reinforce)",
      "n": "DR-DSN",
      "d": "2017-12-29",
      "m1": "42.1",
      "m2": "43.9"
    },
    {
      "p": "[CSTA: CNN-based Spatiotemporal Attention for Video Summarization](https://arxiv.org/abs/2405.11905v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thswodnjs3/CSTA)",
      "n": "CSTA",
      "d": "2024-05-20",
      "m3": "0.246",
      "m4": "0.274"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
