# video-prediction-on-kth

[Dataset Link](https://www.csc.kth.se/cvap/actions/) \
Task Hierarchy: ['Video Prediction']

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
      "label": "FVD",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "SSIM",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "PSNR",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "LPIPS",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Cond",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Train",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "Pred",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "Params (M)",
      "sortable": "true"
    },
    {
      "key": "m9",
      "label": "MSE",
      "sortable": "true"
    },
    {
      "key": "m10",
      "label": "Diversity",
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
      "p": "[Accurate Grid Keypoint Learning for Efficient Video Prediction](https://arxiv.org/abs/2107.13170v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xjgaocs/Grid-Keypoint-Learning)",
      "n": "Grid-keypoints",
      "d": "2021-07-28",
      "m1": "144.2",
      "m2": "0.837",
      "m3": "27.11",
      "m4": "0.092",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "2.0"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP-VAE (from Grid-keypoints)",
      "d": "2018-04-04",
      "m1": "145.7",
      "m2": "0.806",
      "m3": "26.00",
      "m4": "0.116",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "7.3"
    },
    {
      "p": "[Stochastic Video Generation with a Learned Prior](http://arxiv.org/abs/1802.07687v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edenton/svg)",
      "n": "SVG-LP (from Grid-keypoints)",
      "d": "2018-02-21",
      "m1": "157.9",
      "m2": "0.800",
      "m3": "23.91",
      "m4": "0.129",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "22.8"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP (from Grid-keypoints)",
      "d": "2018-04-04",
      "m1": "183.7",
      "m2": "0.699",
      "m3": "23.79",
      "m4": "0.126",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "17.6"
    },
    {
      "p": "[Stochastic Variational Video Prediction](http://arxiv.org/abs/1710.11252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/StanfordVL/roboturk_real_dataset)",
      "n": "SV2P time-invariant (from Grid-keypoints)",
      "d": "2017-10-30",
      "m1": "209.5",
      "m2": "0.782",
      "m3": "25.87",
      "m4": "0.232",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "8.3"
    },
    {
      "p": "[Stochastic Latent Residual Video Prediction](https://arxiv.org/abs/2002.09219v4)",
      "c": "[&check;&nbsp;Link](https://github.com/edouardelasalles/srvp)",
      "n": "SRVP",
      "d": "2020-02-21",
      "m1": "222 \u00b1 3",
      "m2": "0.8697\u00b10.0046",
      "m3": "29.69\u00b1032",
      "m4": "0.0736\u00b10.0029",
      "m5": "10",
      "m6": "10",
      "m7": "30"
    },
    {
      "p": "[SLAMP: Stochastic Latent Appearance and Motion Prediction](https://arxiv.org/abs/2108.02760v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kaanakan/slamp)",
      "n": "SLAMP",
      "d": "2021-08-05",
      "m1": "228 \u00b1 5",
      "m2": "0.8646\u00b10.0050",
      "m3": "29.39\u00b10.30",
      "m4": "0.0795\u00b10.0034",
      "m5": "10",
      "m6": "10",
      "m7": "30"
    },
    {
      "p": "[Stochastic Variational Video Prediction](http://arxiv.org/abs/1710.11252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/StanfordVL/roboturk_real_dataset)",
      "n": "SV2P time-invariant (from Grid-keypoints)",
      "d": "2017-10-30",
      "m1": "253.5",
      "m2": "0.772",
      "m3": "25.70",
      "m4": "0.260",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "8.3"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP (from SRVP)",
      "d": "2018-04-04",
      "m1": "374 \u00b1 3",
      "m2": "0.7564\u00b10.0062",
      "m3": "26.51\u00b10.29",
      "m4": "0.1120\u00b10.0039",
      "m5": "10",
      "m6": "10",
      "m7": "30"
    },
    {
      "p": "[Stochastic Video Generation with a Learned Prior](http://arxiv.org/abs/1802.07687v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edenton/svg)",
      "n": "SVG-LP (from SRVP)",
      "d": "2018-02-21",
      "m1": "377 \u00b1 6",
      "m2": "0.8438\u00b10.0054",
      "m3": "28.06\u00b10.29",
      "m4": "0.0923\u00b10.0038",
      "m5": "10",
      "m6": "10",
      "m7": "30"
    },
    {
      "p": "[Unsupervised Learning of Object Structure and Dynamics from Videos](https://arxiv.org/abs/1906.07889v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "Struct-VRNN (from Grid-keypoints)",
      "d": "2019-06-19",
      "m1": "395.0",
      "m2": "0.766",
      "m3": "24.29",
      "m4": "0.124",
      "m5": "10",
      "m6": "10",
      "m7": "40",
      "m8": "2.3"
    },
    {
      "p": "[Stochastic Variational Video Prediction](http://arxiv.org/abs/1710.11252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/StanfordVL/roboturk_real_dataset)",
      "n": "SV2P (from SRVP)",
      "d": "2017-10-30",
      "m1": "636 \u00b1 1",
      "m2": "0.838",
      "m3": "28.19\u00b10.31",
      "m4": "0.2049\u00b10.0053",
      "m5": "10",
      "m6": "10",
      "m7": "30"
    },
    {
      "p": "[MSPred: Video Prediction at Multiple Spatio-Temporal Scales with Hierarchical Recurrent Networks](https://arxiv.org/abs/2203.09303v4)",
      "c": "[&check;&nbsp;Link](https://github.com/AIS-Bonn/MSPred)",
      "n": "MSPred",
      "d": "2022-03-17",
      "m2": "0.951",
      "m3": "27.81",
      "m4": "0.029",
      "m9": "23.18"
    },
    {
      "p": "[Exploring Spatial-Temporal Multi-Frequency Analysis for High-Fidelity and Temporal-Consistency Video Prediction](https://arxiv.org/abs/2002.09905v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Bei-Jin/STMFANet)",
      "n": "WAM",
      "d": "2020-02-23",
      "m2": "0.893",
      "m3": "29.85",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Eidetic 3D LSTM: A Model for Video Prediction and Beyond](https://openreview.net/forum?id=B1lKS2AqtX)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/simvpv2)",
      "n": "E3d-LSTM",
      "d": "2019-05-01",
      "m2": "0.879",
      "m3": "29.31",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Video Prediction Recalling Long-term Motion Context via Memory Alignment Learning](https://arxiv.org/abs/2104.00924v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sangmin-git/LMC-Memory)",
      "n": "LMC",
      "d": "2021-04-02",
      "m2": "0.879",
      "m3": "27.5",
      "m4": "159.8",
      "m5": "10",
      "m7": "40"
    },
    {
      "p": "[Mutual Suppression Network for Video Prediction using Disentangled Features](https://arxiv.org/abs/1804.04810v2)",
      "c": "",
      "n": "MSNET",
      "d": "2018-04-13",
      "m2": "0.876",
      "m3": "27.08",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[PredRNN++: Towards A Resolution of the Deep-in-Time Dilemma in Spatiotemporal Predictive Learning](http://arxiv.org/abs/1804.06300v2)",
      "c": "[&check;&nbsp;Link](https://github.com/thuml/predrnn-pytorch)",
      "n": "PredRNN++",
      "d": "2018-04-17",
      "m2": "0.865",
      "m3": "28.47",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP-VAE",
      "d": "2018-04-04",
      "m2": "0.852",
      "m3": "27.77",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[VarNet: Exploring Variations for Unsupervised Video Prediction](https://ieeexplore.ieee.org/document/8594264)",
      "c": "[&check;&nbsp;Link](https://github.com/jinbeibei/VarNet)",
      "n": "VarNet",
      "d": "2018-10-01",
      "m2": "0.843",
      "m3": "28.48",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[PredRNN: A Recurrent Neural Network for Spatiotemporal Predictive Learning](https://arxiv.org/abs/2103.09504v4)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/simvpv2)",
      "n": "PredRNN-V2",
      "d": "2021-03-17",
      "m2": "0.839",
      "m3": "28.37",
      "m4": "0.139",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Z-Order Recurrent Neural Networks for Video Prediction](https://ieeexplore.ieee.org/document/8784821)",
      "c": "",
      "n": "Znet",
      "d": "2019-07-08",
      "m2": "0.817",
      "m3": "27.58",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Convolutional Tensor-Train LSTM for Spatio-temporal Learning](https://arxiv.org/abs/2002.09131v5)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/conv-tt-lstm)",
      "n": "Conv-TT-LSTM",
      "d": "2020-02-21",
      "m2": "0.815",
      "m3": "27.62",
      "m4": "0.196",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Decomposing Motion and Content for Natural Video Sequence Prediction](http://arxiv.org/abs/1706.08033v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rubenvillegas/iclr2017mcnet)",
      "n": "MCnet + Residual",
      "d": "2017-06-25",
      "m2": "0.806",
      "m3": "26.29",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Decomposing Motion and Content for Natural Video Sequence Prediction](http://arxiv.org/abs/1706.08033v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rubenvillegas/iclr2017mcnet)",
      "n": "MCnet",
      "d": "2017-06-25",
      "m2": "0.804",
      "m3": "25.95",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Dynamic Filter Networks](http://arxiv.org/abs/1605.09673v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dbbert/dfn)",
      "n": "DFN",
      "d": "2016-05-31",
      "m2": "0.794",
      "m3": "27.26",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Deep Learning for Precipitation Nowcasting: A Benchmark and A New Model](http://arxiv.org/abs/1706.03458v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Hzzone/Precipitation-Nowcasting)",
      "n": "TrajGRU",
      "d": "2017-06-12",
      "m2": "0.790",
      "m3": "26.97",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Folded Recurrent Neural Networks for Future Video Prediction](http://arxiv.org/abs/1712.00311v2)",
      "c": "[&check;&nbsp;Link](https://github.com/moliusimon/frnn)",
      "n": "fRNN",
      "d": "2017-12-01",
      "m2": "0.771",
      "m3": "26.12",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Video Pixel Networks](http://arxiv.org/abs/1610.00527v1)",
      "c": "[&check;&nbsp;Link](https://github.com/3ammor/Video-Pixel-Networks)",
      "n": "VPN",
      "d": "2016-10-03",
      "m2": "0.746",
      "m3": "23.76",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting](http://arxiv.org/abs/1506.04214v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ndrplz/ConvLSTM_pytorch)",
      "n": "ConvLSTM",
      "d": "2015-06-13",
      "m2": "0.712",
      "m3": "23.58",
      "m4": "0.231",
      "m5": "10",
      "m7": "20"
    },
    {
      "p": "[Diverse Video Generation using a Gaussian Process Trigger](https://arxiv.org/abs/2107.04619v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shgaurav1/DVG)",
      "n": "DVG",
      "d": "2021-07-09",
      "m10": "0.483"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
