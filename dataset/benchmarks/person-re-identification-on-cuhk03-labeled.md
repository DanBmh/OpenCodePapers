# person-re-identification-on-cuhk03-labeled

[Dataset Link](http://www.ee.cuhk.edu.hk/~xgwang/CUHK_identification.html) \
Task Hierarchy: ['Person Re-Identification']

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
      "label": "MAP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Rank-1",
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
      "p": "[]()",
      "c": "",
      "n": "Weakly Pre-training (ResNet101+RK)",
      "d": null,
      "m1": "89.29",
      "m2": "87.86"
    },
    {
      "p": "[Top-DB-Net: Top DropBlock for Activation Enhancement in Person Re-Identification](https://arxiv.org/abs/2010.05435v1)",
      "c": "[&check;&nbsp;Link](https://github.com/RQuispeC/top-dropblock)",
      "n": "Top-DB-Net + RK",
      "d": "2020-10-12",
      "m1": "88.5",
      "m2": "86.7"
    },
    {
      "p": "[DiP: Learning Discriminative Implicit Parts for Person Re-Identification](https://arxiv.org/abs/2212.13906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/siyuch-fdu/DiP)",
      "n": "DiP (without RK)",
      "d": "2022-12-24",
      "m1": "85.7",
      "m2": "87"
    },
    {
      "p": "[Lightweight Multi-Branch Network for Person Re-Identification](https://arxiv.org/abs/2101.10774v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mikel-brostrom/boxmot)",
      "n": "LightMBN (w/o ReRank)",
      "d": "2021-01-26",
      "m1": "85.1",
      "m2": "87.2"
    },
    {
      "p": "[Deep Miner: A Deep and Multi-branch Network which Mines Rich and Diverse Features for Person Re-identification](https://arxiv.org/abs/2102.09321v1)",
      "c": "[&check;&nbsp;Link](https://github.com/robin-schneider/cicy-fourfolds)",
      "n": "Deep Miner (w/o ReRank)",
      "d": "2021-02-18",
      "m1": "84.7",
      "m2": "86.6"
    },
    {
      "p": "[FPB: Feature Pyramid Branch for Person Re-Identification](https://arxiv.org/abs/2108.01901v1)",
      "c": "[&check;&nbsp;Link](https://github.com/anocodetest1/FPB)",
      "n": "FPB",
      "d": "2021-08-04",
      "m1": "83.8",
      "m2": "85.9"
    },
    {
      "p": "[Multi-task Learning with Coarse Priors for Robust Part-aware Person Re-identification](https://arxiv.org/abs/2003.08069v3)",
      "c": "[&check;&nbsp;Link](https://github.com/WangKan0128/MPN)",
      "n": "MPN (without re-ranking)",
      "d": "2020-03-18",
      "m1": "81.1",
      "m2": "85"
    },
    {
      "p": "[Learning Diverse Features with Part-Level Resolution for Person Re-Identification](https://arxiv.org/abs/2001.07442v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AI-NERC-NUPT/PLR-OSNet)",
      "n": "PLR-OSNet",
      "d": "2020-01-21",
      "m1": "80.5",
      "m2": "84.6"
    },
    {
      "p": "[Pyramidal Person Re-IDentification via Multi-Loss Dynamic Training](https://arxiv.org/abs/1810.12193v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TencentYoutuResearch/PersonReID-Pyramid)",
      "n": "Pyramid (CVPR' 19)",
      "d": "2018-10-29",
      "m1": "76.9",
      "m2": "78.9"
    },
    {
      "p": "[Batch DropBlock Network for Person Re-identification and Beyond](https://arxiv.org/abs/1811.07130v3)",
      "c": "[&check;&nbsp;Link](https://github.com/daizuozhuo/batch-feature-erasing-network)",
      "n": "BDB  (ICCV'19)",
      "d": "2018-11-17",
      "m1": "76.7",
      "m2": "79.4"
    },
    {
      "p": "[Top-DB-Net: Top DropBlock for Activation Enhancement in Person Re-Identification](https://arxiv.org/abs/2010.05435v1)",
      "c": "[&check;&nbsp;Link](https://github.com/RQuispeC/top-dropblock)",
      "n": "Top-DB-Net",
      "d": "2020-10-12",
      "m1": "75.4",
      "m2": "79.4"
    },
    {
      "p": "[Auto-ReID: Searching for a Part-aware ConvNet for Person Re-Identification](https://arxiv.org/abs/1903.09776v4)",
      "c": "[&check;&nbsp;Link](https://github.com/D-X-Y/GDAS)",
      "n": "Auto-ReID  (ICCV'19)",
      "d": "2019-03-23",
      "m1": "73.0",
      "m2": "77.9"
    },
    {
      "p": "[Learning Discriminative Features with Multiple Granularities for Person Re-Identification](http://arxiv.org/abs/1804.01438v3)",
      "c": "[&check;&nbsp;Link](https://github.com/seathiefwang/MGN-pytorch)",
      "n": "MGN (ACM MM'18)",
      "d": "2018-04-04",
      "m1": "67.4",
      "m2": "68.0"
    },
    {
      "p": "[Resource Aware Person Re-identification across Multiple Resolutions](http://arxiv.org/abs/1805.08805v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mileyan/DARENet)",
      "n": "DaRe+RE (CVPR'18)",
      "d": "2018-05-22",
      "m1": "61.6",
      "m2": "66.1"
    },
    {
      "p": "[Pedestrian Alignment Network for Large-scale Person Re-identification](http://arxiv.org/abs/1707.00408v1)",
      "c": "[&check;&nbsp;Link](https://github.com/layumi/Pedestrian_Alignment)",
      "n": "PAN+re-rank",
      "d": "2017-07-03",
      "m1": "45.8",
      "m2": "43.9"
    },
    {
      "p": "[Harmonious Attention Network for Person Re-Identification](http://arxiv.org/abs/1802.08122v1)",
      "c": "[&check;&nbsp;Link](https://github.com/milkplz/keras-frcnn)",
      "n": "HA-CNN (CVPR'18)",
      "d": "2018-02-22",
      "m1": "41.0",
      "m2": "44.4"
    },
    {
      "p": "[Pedestrian Alignment Network for Large-scale Person Re-identification](http://arxiv.org/abs/1707.00408v1)",
      "c": "[&check;&nbsp;Link](https://github.com/layumi/Pedestrian_Alignment)",
      "n": "PAN(Zheng et al., [2017a])",
      "d": "2017-07-03",
      "m1": "35.0",
      "m2": "36.9"
    },
    {
      "p": "[Re-ranking Person Re-identification with k-reciprocal Encoding](http://arxiv.org/abs/1701.08398v4)",
      "c": "",
      "n": "IDE-R+XQDA",
      "d": "2017-01-29",
      "m1": "29.6",
      "m2": "32.0"
    },
    {
      "p": "[Re-ranking Person Re-identification with k-reciprocal Encoding](http://arxiv.org/abs/1701.08398v4)",
      "c": "",
      "n": "IDE-R",
      "d": "2017-01-29",
      "m1": "21.0",
      "m2": "22.2"
    },
    {
      "p": "[Re-ranking Person Re-identification with k-reciprocal Encoding](http://arxiv.org/abs/1701.08398v4)",
      "c": "",
      "n": "IDE-C+XQDA",
      "d": "2017-01-29",
      "m1": "20.0",
      "m2": "21.9"
    },
    {
      "p": "[Re-ranking Person Re-identification with k-reciprocal Encoding](http://arxiv.org/abs/1701.08398v4)",
      "c": "",
      "n": "IDE-C",
      "d": "2017-01-29",
      "m1": "14.9",
      "m2": "15.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
