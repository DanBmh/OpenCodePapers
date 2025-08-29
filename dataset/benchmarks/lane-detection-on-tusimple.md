# lane-detection-on-tusimple

[Dataset Link](https://github.com/TuSimple/tusimple-benchmark) \
Task Hierarchy: ['Lane Detection']

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
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "F1 score",
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
      "p": "[Robust Lane Detection through Self Pre-training with Masked Sequential Autoencoders and Fine-tuning with Customized PolyLoss](https://arxiv.org/abs/2305.17271v2)",
      "c": "",
      "n": "SCNN_UNet_Attention_PL*",
      "d": "2023-05-26",
      "m1": "98.38"
    },
    {
      "p": "[CLRNetV2: A Faster and Stronger Lane Detector](https://ieeexplore.ieee.org/abstract/document/10930685)",
      "c": "",
      "n": "CLRNetV2 (ResNet18)",
      "d": "2025-03-18",
      "m1": "96.99",
      "m2": "97.90"
    },
    {
      "p": "[Lane detection with Position Embedding](https://arxiv.org/abs/2203.12301v1)",
      "c": "",
      "n": "PE-RESA",
      "d": "2022-03-23",
      "m1": "96.93"
    },
    {
      "p": "[Focus on Local: Detecting Lane Marker from Bottom Up via Key Point](https://arxiv.org/abs/2105.13680v1)",
      "c": "",
      "n": "FOLOLane(ERFNet)",
      "d": "2021-05-28",
      "m1": "96.92"
    },
    {
      "p": "[CLRNet: Cross Layer Refinement Network for Lane Detection](https://arxiv.org/abs/2203.10350v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CLRNet(ResNet-34)",
      "d": "2022-03-19",
      "m1": "96.9%",
      "m2": "97.82"
    },
    {
      "p": "[CLRNetV2: A Faster and Stronger Lane Detector](https://ieeexplore.ieee.org/abstract/document/10930685)",
      "c": "",
      "n": "CLRNetV2 (ResNet34)",
      "d": "2025-03-18",
      "m1": "96.88",
      "m2": "97.95"
    },
    {
      "p": "[CLRNet: Cross Layer Refinement Network for Lane Detection](https://arxiv.org/abs/2203.10350v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CLRNet(ResNet-18)",
      "d": "2022-03-19",
      "m1": "96.82%",
      "m2": "97.89"
    },
    {
      "p": "[RESA: Recurrent Feature-Shift Aggregator for Lane Detection](https://arxiv.org/abs/2008.13719v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "RESA",
      "d": "2020-08-31",
      "m1": "96.82",
      "m2": "96.93"
    },
    {
      "p": "[Contrastive Learning for Lane Detection via cross-similarity](https://arxiv.org/abs/2308.08242v4)",
      "c": "[&check;&nbsp;Link](https://github.com/zkyntu/UnLanedet)",
      "n": "CLLD",
      "d": "2023-08-16",
      "m1": "96.82"
    },
    {
      "p": "[CANet: Curved Guide Line Network with Adaptive Decoder for Lane Detection](https://arxiv.org/abs/2304.11546v1)",
      "c": "",
      "n": "CANet-L(ResNet101)",
      "d": "2023-04-23",
      "m1": "96.76%",
      "m2": "97.77"
    },
    {
      "p": "[CANet: Curved Guide Line Network with Adaptive Decoder for Lane Detection](https://arxiv.org/abs/2304.11546v1)",
      "c": "",
      "n": "CANet-M",
      "d": "2023-04-23",
      "m1": "96.66%",
      "m2": "97.44"
    },
    {
      "p": "[Learning Lightweight Lane Detection CNNs by Self Attention Distillation](https://arxiv.org/abs/1908.00821v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cardwing/Codes-for-Lane-Detection)",
      "n": "ENet-SAD",
      "d": "2019-08-02",
      "m1": "96.64%",
      "m2": "95.92"
    },
    {
      "p": "[Towards Lightweight Lane Detection by Optimizing Spatial Embedding](https://arxiv.org/abs/2008.08311v2)",
      "c": "[&check;&nbsp;Link](https://github.com/JungSeokWoo/Lightweight-LaneDetection)",
      "n": "HarD-SP",
      "d": "2020-08-19",
      "m1": "96.58%",
      "m2": "96.38"
    },
    {
      "p": "[CANet: Curved Guide Line Network with Adaptive Decoder for Lane Detection](https://arxiv.org/abs/2304.11546v1)",
      "c": "",
      "n": "CANet-S",
      "d": "2023-04-23",
      "m1": "96.56%",
      "m2": "97.51"
    },
    {
      "p": "[CondLaneNet: a Top-to-down Lane Detection Framework Based on Conditional Convolution](https://arxiv.org/abs/2105.05003v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CondLaneNet-L(ResNet-101)",
      "d": "2021-05-11",
      "m1": "96.54%",
      "m2": "97.24"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Oblique Convolution",
      "d": null,
      "m1": "96.50%",
      "m2": "97.42"
    },
    {
      "p": "[Learning to Cluster for Proposal-Free Instance Segmentation](http://arxiv.org/abs/1803.06459v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GT-RIPL/L2C)",
      "n": "Pairwise pixel supervision + FCN",
      "d": "2018-03-17",
      "m1": "96.50%",
      "m2": "94.31"
    },
    {
      "p": "[EL-GAN: Embedding Loss Driven Generative Adversarial Networks for Lane Detection](http://arxiv.org/abs/1806.05525v2)",
      "c": "",
      "n": "EL-GAN",
      "d": "2018-06-14",
      "m1": "96.40%",
      "m2": "96.26"
    },
    {
      "p": "[Towards End-to-End Lane Detection: an Instance Segmentation Approach](http://arxiv.org/abs/1802.05591v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MaybeShewill-CV/lanenet-lane-detection)",
      "n": "LaneNet",
      "d": "2018-02-15",
      "m1": "96.4%",
      "m2": "94.80"
    },
    {
      "p": "[Semantic Instance Segmentation with a Discriminative Loss Function](http://arxiv.org/abs/1708.02551v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Wizaron/instance-segmentation-pytorch)",
      "n": "Discriminative loss function",
      "d": "2017-08-08",
      "m1": "96.40%"
    },
    {
      "p": "[Agnostic Lane Detection](http://arxiv.org/abs/1905.03704v1)",
      "c": "",
      "n": "ENet-Label",
      "d": "2019-05-02",
      "m1": "96.29%",
      "m2": "95.23"
    },
    {
      "p": "[End-to-End Lane Marker Detection via Row-wise Classification](https://arxiv.org/abs/2005.08630v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Vipermdl/E2E-ERFNet)",
      "n": "R-34-E2E",
      "d": "2020-05-06",
      "m1": "96.22%",
      "m2": "96.58"
    },
    {
      "p": "[End-to-end Lane Shape Prediction with Transformers](https://arxiv.org/abs/2011.04233v2)",
      "c": "[&check;&nbsp;Link](https://github.com/liuruijin17/LSTR)",
      "n": "LSTR",
      "d": "2020-11-09",
      "m1": "96.18",
      "m2": "96.68"
    },
    {
      "p": "[End-to-End Lane Marker Detection via Row-wise Classification](https://arxiv.org/abs/2005.08630v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Vipermdl/E2E-ERFNet)",
      "n": "R-50-E2E",
      "d": "2020-05-06",
      "m1": "96.11%",
      "m2": "96.37"
    },
    {
      "p": "[Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection](https://arxiv.org/abs/2010.12035v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucastabelini/LaneATT)",
      "n": "LaneATT (ResNet-122)",
      "d": "2020-10-22",
      "m1": "96.10%",
      "m2": "96.06"
    },
    {
      "p": "[End-to-End Lane Marker Detection via Row-wise Classification](https://arxiv.org/abs/2005.08630v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Vipermdl/E2E-ERFNet)",
      "n": "ERF-E2E",
      "d": "2020-05-06",
      "m1": "96.02%",
      "m2": "96.25"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Lane-LSQ",
      "d": null,
      "m1": "95.84%"
    },
    {
      "p": "[Rethinking Efficient Lane Detection via Curve Modeling](https://arxiv.org/abs/2203.02431v2)",
      "c": "[&check;&nbsp;Link](https://github.com/voldemortX/pytorch-auto-drive)",
      "n": "B\u00e9zierLaneNet (ResNet-34)",
      "d": "2022-03-04",
      "m1": "95.65%"
    },
    {
      "p": "[LaneAF: Robust Multi-Lane Detection with Affinity Fields](https://arxiv.org/abs/2103.12040v4)",
      "c": "[&check;&nbsp;Link](https://github.com/sel118/LaneAF)",
      "n": "LaneAF",
      "d": "2021-03-22",
      "m1": "95.64%",
      "m2": "96.49"
    },
    {
      "p": "[Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection](https://arxiv.org/abs/2010.12035v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucastabelini/LaneATT)",
      "n": "LaneATT (ResNet-34)",
      "d": "2020-10-22",
      "m1": "95.63%",
      "m2": "96.77"
    },
    {
      "p": "[Eigenlanes: Data-Driven Lane Descriptors for Structurally Diverse Lanes](https://arxiv.org/abs/2203.15302v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dongkwonjin/eigenlanes)",
      "n": "Eigenlanes (ResNet-18)",
      "d": "2022-03-29",
      "m1": "95.62%"
    },
    {
      "p": "[Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection](https://arxiv.org/abs/2010.12035v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucastabelini/LaneATT)",
      "n": "LaneATT (ResNet-18)",
      "d": "2020-10-22",
      "m1": "95.57%",
      "m2": "96.71"
    },
    {
      "p": "[CondLaneNet: a Top-to-down Lane Detection Framework Based on Conditional Convolution](https://arxiv.org/abs/2105.05003v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CondLaneNet(ResNet-18)",
      "d": "2021-05-11",
      "m1": "95.48%"
    },
    {
      "p": "[Rethinking Efficient Lane Detection via Curve Modeling](https://arxiv.org/abs/2203.02431v2)",
      "c": "[&check;&nbsp;Link](https://github.com/voldemortX/pytorch-auto-drive)",
      "n": "B\u00e9zierLaneNet (ResNet-18)",
      "d": "2022-03-04",
      "m1": "95.41%"
    },
    {
      "p": "[CondLaneNet: a Top-to-down Lane Detection Framework Based on Conditional Convolution](https://arxiv.org/abs/2105.05003v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CondLaneNet-M(ResNet-34)",
      "d": "2021-05-11",
      "m1": "95.37%",
      "m2": "96.98"
    },
    {
      "p": "[Lane Detection and Classification using Cascaded CNNs](https://arxiv.org/abs/1907.01294v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fabvio/Cascade-LD)",
      "n": "End-to-end ERFNet",
      "d": "2019-07-02",
      "m1": "95.24%",
      "m2": "90.82"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ERFNet",
      "d": null,
      "m1": "94.5%"
    },
    {
      "p": "[PolyLaneNet: Lane Estimation via Deep Polynomial Regression](https://arxiv.org/abs/2004.10924v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucastabelini/PolyLaneNet)",
      "n": "PolyLaneNet",
      "d": "2020-04-23",
      "m1": "93.36%",
      "m2": "90.62"
    },
    {
      "p": "[A Keypoint-based Global Association Network for Lane Detection](https://arxiv.org/abs/2204.07335v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wolfwjs/ganet)",
      "n": "GANet(ResNet-34)",
      "d": "2022-04-15",
      "m2": "97.71"
    },
    {
      "p": "[A Keypoint-based Global Association Network for Lane Detection](https://arxiv.org/abs/2204.07335v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wolfwjs/ganet)",
      "n": "GANet(ResNet-18)",
      "d": "2022-04-15",
      "m2": "97.68"
    },
    {
      "p": "[CLRNet: Cross Layer Refinement Network for Lane Detection](https://arxiv.org/abs/2203.10350v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CLRNet(ResNet-101)",
      "d": "2022-03-19",
      "m2": "97.62"
    },
    {
      "p": "[A Keypoint-based Global Association Network for Lane Detection](https://arxiv.org/abs/2204.07335v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wolfwjs/ganet)",
      "n": "GANet(ResNet-101)",
      "d": "2022-04-15",
      "m2": "97.45"
    },
    {
      "p": "[CondLaneNet: a Top-to-down Lane Detection Framework Based on Conditional Convolution](https://arxiv.org/abs/2105.05003v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Turoad/lanedet)",
      "n": "CondLaneNet(ResNet-34)",
      "d": "2021-05-11",
      "m2": "97.01"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
