# visual-dialog-on-visdial-v09-val

[Dataset Link](https://visualdialog.org/) \
Task Hierarchy: ['Visual Dialog']

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
      "label": "MRR",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "R@1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "R@10",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "R@5",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Mean Rank",
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
      "p": "[Factor Graph Attention](https://arxiv.org/abs/1904.05880v3)",
      "c": "[&check;&nbsp;Link](https://github.com/idansc/fga)",
      "n": "9xFGA (VGG)",
      "d": "2019-04-11",
      "m1": "68.92",
      "m2": "55.16",
      "m3": "92.95",
      "m4": "86.26",
      "m5": "3.39"
    },
    {
      "p": "[Dual Attention Networks for Visual Reference Resolution in Visual Dialog](https://arxiv.org/abs/1902.09368v3)",
      "c": "[&check;&nbsp;Link](https://github.com/gicheonkang/DAN-VisDial)",
      "n": "DAN",
      "d": "2019-02-25",
      "m1": "66.38",
      "m2": "53.33",
      "m3": "90.38",
      "m4": "82.42",
      "m5": "4.04"
    },
    {
      "p": "[Visual Coreference Resolution in Visual Dialog using Neural Module Networks](http://arxiv.org/abs/1809.01816v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/corefnmn)",
      "n": "CorefNMN (ResNet-152)",
      "d": "2018-09-06",
      "m1": "64.1",
      "m2": "50.92",
      "m3": "88.81",
      "m4": "80.18",
      "m5": "4.45"
    },
    {
      "p": "[Are You Talking to Me? Reasoned Visual Dialog Generation through Adversarial Learning](http://arxiv.org/abs/1711.07613v1)",
      "c": "",
      "n": "CoAtt",
      "d": "2017-11-21",
      "m1": "63.98",
      "m2": "50.29",
      "m3": "88.81",
      "m4": "80.71",
      "m5": "4.47"
    },
    {
      "p": "[Visual Coreference Resolution in Visual Dialog using Neural Module Networks](http://arxiv.org/abs/1809.01816v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/corefnmn)",
      "n": "CorefNMN",
      "d": "2018-09-06",
      "m1": "63.6",
      "m2": "50.24",
      "m3": "88.51",
      "m4": "79.81",
      "m5": "4.53"
    },
    {
      "p": "[DualVD: An Adaptive Dual Encoding Model for Deep Visual Understanding in Visual Dialogue](https://arxiv.org/abs/1911.07251v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JXZe/DualVD)",
      "n": "DualVD",
      "d": "2019-11-17",
      "m1": "62.94",
      "m2": "48.64",
      "m3": "89.94",
      "m4": "80.89",
      "m5": "4.17"
    },
    {
      "p": "[Two can play this Game: Visual Dialog with Discriminative Question Generation and Answering](http://arxiv.org/abs/1803.11186v1)",
      "c": "",
      "n": "SF-QIH-se-2",
      "d": "2018-03-29",
      "m1": "62.42",
      "m2": "48.55",
      "m3": "87.75",
      "m4": "78.96",
      "m5": "4.70"
    },
    {
      "p": "[Best of Both Worlds: Transferring Knowledge from Discriminative Learning to a Generative Visual Dialog Model](http://arxiv.org/abs/1706.01554v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiasenlu/visDial.pytorch)",
      "n": "HCIAE-NP-ATT",
      "d": "2017-06-05",
      "m1": "62.22",
      "m2": "48.48",
      "m3": "87.59",
      "m4": "78.75",
      "m5": "4.81"
    },
    {
      "p": "[Hierarchical Question-Image Co-Attention for Visual Question Answering](http://arxiv.org/abs/1606.00061v5)",
      "c": "[&check;&nbsp;Link](https://github.com/jiasenlu/HieCoAttenVQA)",
      "n": "HieCoAtt-QI",
      "d": "2016-05-31",
      "m1": "57.88",
      "m2": "43.51",
      "m3": "83.96",
      "m4": "74.49",
      "m5": "5.84"
    },
    {
      "p": "[Making History Matter: History-Advantage Sequence Training for Visual Dialog](http://arxiv.org/abs/1902.09326v3)",
      "c": "",
      "n": "HACAN",
      "d": "2019-02-25",
      "m1": "0.6792",
      "m2": "54.76",
      "m3": "90.68",
      "m4": "83.03",
      "m5": "3.97"
    },
    {
      "p": "[Multi-View Attention Network for Visual Dialog](https://arxiv.org/abs/2004.14025v3)",
      "c": "[&check;&nbsp;Link](https://github.com/taesunwhang/MVAN-VisDial)",
      "n": "MVAN",
      "d": "2020-04-29",
      "m1": "0.6765",
      "m2": "54.65",
      "m3": "91.47",
      "m4": "83.85",
      "m5": "3.73"
    },
    {
      "p": "[Iterative Context-Aware Graph Inference for Visual Dialog](https://arxiv.org/abs/2004.02194v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wh0330/CAG_VisDial)",
      "n": "CAG",
      "d": "2020-04-05",
      "m1": "0.6756",
      "m2": "54.64",
      "m3": "91.48",
      "m4": "83.72",
      "m5": "3.75"
    },
    {
      "p": "[Recursive Visual Attention in Visual Dialog](http://arxiv.org/abs/1812.02664v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yuleiniu/rva)",
      "n": "RVA",
      "d": "2018-12-06",
      "m1": "0.6634",
      "m2": "52.71",
      "m3": "90.73",
      "m4": "82.97",
      "m5": "3.93"
    },
    {
      "p": "[Reasoning Visual Dialogs with Structural and Partial Observations](https://arxiv.org/abs/1904.05548v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zilongzheng/visdial-gnn)",
      "n": "GNN",
      "d": "2019-04-11",
      "m1": "0.6285",
      "m2": "48.95",
      "m3": "88.36",
      "m4": "79.65",
      "m5": "4.57"
    },
    {
      "p": "[Visual Dialog](http://arxiv.org/abs/1611.08669v5)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/ParlAI)",
      "n": "MN-QIH-D",
      "d": "2016-11-26",
      "m1": "0.5965",
      "m2": "45.55",
      "m3": "85.37",
      "m4": "76.22",
      "m5": "5.46"
    },
    {
      "p": "[Visual Dialog](http://arxiv.org/abs/1611.08669v5)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/ParlAI)",
      "n": "HRE-QIH-D",
      "d": "2016-11-26",
      "m1": "0.5846",
      "m2": "44.67",
      "m3": "84.22",
      "m4": "74.50",
      "m5": "5.72"
    },
    {
      "p": "[Visual Dialog](http://arxiv.org/abs/1611.08669v5)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/ParlAI)",
      "n": "HRE-QIH-D",
      "d": "2016-11-26",
      "m1": "0.5807",
      "m2": "43.82",
      "m3": "84.07",
      "m4": "74.68",
      "m5": "5.78"
    },
    {
      "p": "[Visual Reference Resolution using Attention Memory for Visual Dialog](http://arxiv.org/abs/1709.07992v3)",
      "c": "",
      "n": "AMEM",
      "d": "2017-09-23",
      "m2": "48.53",
      "m3": "87.43",
      "m4": "78.66",
      "m5": "4.86"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
