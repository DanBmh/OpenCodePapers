# video-generation-on-bair-robot-pushing

[Dataset Link](https://sites.google.com/berkeley.edu/robotic-interaction-datasets) \
Task Hierarchy: ['Video Generation']

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
      "label": "FVD score",
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
      "label": "Notes",
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
      "p": "[MAGVIT: Masked Generative Video Transformer](https://arxiv.org/abs/2212.05199v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/magvit)",
      "n": "MAGVIT",
      "d": "2022-12-10",
      "m1": "62",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[Diffusion Models for Video Prediction and Infilling](https://arxiv.org/abs/2206.07696v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Tobi-r9/RaMViD)",
      "n": "RaMViD",
      "d": "2022-06-15",
      "m1": "84.20",
      "m5": "1",
      "m6": "20",
      "m7": "15"
    },
    {
      "p": "[N\u00dcWA: Visual Synthesis Pre-training for Neural visUal World creAtion](https://arxiv.org/abs/2111.12417v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/nuwa-pytorch)",
      "n": "NUWA",
      "d": "2021-11-24",
      "m1": "86.9",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation](https://arxiv.org/abs/2205.09853v4)",
      "c": "[&check;&nbsp;Link](https://github.com/voletiv/mcvd-pytorch)",
      "n": "MCVD : c2t5p14",
      "d": "2022-05-19",
      "m1": "87.9",
      "m2": "0.838",
      "m3": "19.1",
      "m5": "2",
      "m6": "5",
      "m7": "14"
    },
    {
      "p": "[MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation](https://arxiv.org/abs/2205.09853v4)",
      "c": "[&check;&nbsp;Link](https://github.com/voletiv/mcvd-pytorch)",
      "n": "MCVD : c1t5p15",
      "d": "2022-05-19",
      "m1": "89.5",
      "m2": "0.78",
      "m3": "16.9",
      "m5": "1",
      "m6": "5",
      "m7": "15"
    },
    {
      "p": "[FitVid: Overfitting in Pixel-Level Video Prediction](https://arxiv.org/abs/2106.13195v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/fitvid)",
      "n": "FitVid",
      "d": "2021-06-24",
      "m1": "93.6",
      "m5": "1",
      "m6": "15",
      "m7": "15",
      "m8": "Uses 100 times more fake than real samples (atypical)"
    },
    {
      "p": "[Scaling Autoregressive Video Models](https://arxiv.org/abs/1906.02634v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rakhimovv/lvt)",
      "n": "Video Transformer",
      "d": "2019-06-06",
      "m1": "94\u00b1 2",
      "m5": "1",
      "m6": "15",
      "m7": "15",
      "m8": "FVD on only leftmost samples is 94, FVD on unrolled (all subsequences) is 96"
    },
    {
      "p": "[CCVS: Context-aware Controllable Video Synthesis](https://arxiv.org/abs/2107.08037v2)",
      "c": "[&check;&nbsp;Link](https://github.com/16lemoing/ccvs)",
      "n": "CCVS",
      "d": "2021-07-16",
      "m1": "99 \u00b1 2",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[VideoGPT: Video Generation using VQ-VAE and Transformers](https://arxiv.org/abs/2104.10157v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wilson1yan/VideoGPT)",
      "n": "VideoGPT",
      "d": "2021-04-20",
      "m1": "103.3",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[Transformation-based Adversarial Video Prediction on Large-Scale Data](https://arxiv.org/abs/2003.04035v3)",
      "c": "",
      "n": "TrIVD-GAN-FP",
      "d": "2020-03-09",
      "m1": "103.3",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[Adversarial Video Generation on Complex Datasets](https://arxiv.org/abs/1907.06571v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Harrypotterrrr/DVD-GAN)",
      "n": "DVD-GAN-FP",
      "d": "2019-07-15",
      "m1": "109.8",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP (from FVD)",
      "d": "2018-04-04",
      "m1": "116.4",
      "m5": "2",
      "m6": "14",
      "m7": "14"
    },
    {
      "p": "[MCVD: Masked Conditional Video Diffusion for Prediction, Generation, and Interpolation](https://arxiv.org/abs/2205.09853v4)",
      "c": "[&check;&nbsp;Link](https://github.com/voletiv/mcvd-pytorch)",
      "n": "MCVD : c2t5p28",
      "d": "2022-05-19",
      "m1": "118.4",
      "m2": "0.745",
      "m3": "16.2",
      "m5": "2",
      "m6": "5",
      "m7": "28"
    },
    {
      "p": "[Latent Video Transformer](https://arxiv.org/abs/2006.10704v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rakhimovv/lvt)",
      "n": "LVT",
      "d": "2020-06-18",
      "m1": "125.76\u00b12.90",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[VideoFlow: A Conditional Flow-Based Model for Stochastic Video Generation](https://arxiv.org/abs/1903.01434v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/tensor2tensor)",
      "n": "VideoFlow",
      "d": "2019-03-04",
      "m1": "131\u00b15",
      "m5": "3",
      "m6": "10",
      "m7": "14 (total 16)"
    },
    {
      "p": "[Improved Conditional VRNNs for Video Prediction](http://arxiv.org/abs/1904.12165v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/improved_vrnn)",
      "n": "Hier-VRNN",
      "d": "2019-04-27",
      "m1": "143.4",
      "m2": "0.822\u00b10.06",
      "m4": "0.055\u00b10.03",
      "m5": "2",
      "m6": "10",
      "m7": "28"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP (from vRNN)",
      "d": "2018-04-04",
      "m1": "143.43",
      "m2": "0.795\u00b10.07",
      "m4": "0.062\u00b10.03",
      "m5": "2",
      "m6": "10",
      "m7": "28"
    },
    {
      "p": "[Improved Conditional VRNNs for Video Prediction](http://arxiv.org/abs/1904.12165v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/improved_vrnn)",
      "n": "VRNN 1L",
      "d": "2019-04-27",
      "m1": "149.22",
      "m2": "0.829\u00b10.06",
      "m4": "0.058\u00b10.03",
      "m5": "2",
      "m6": "10",
      "m7": "28"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP (from SRVP)",
      "d": "2018-04-04",
      "m1": "152\u00b19",
      "m2": "0.7887\u00b10.0092",
      "m3": "18.44\u00b10.25",
      "m4": "0.0634\u00b10.0026",
      "m5": "2",
      "m6": "12",
      "m7": "28"
    },
    {
      "p": "[Exploring Spatial-Temporal Multi-Frequency Analysis for High-Fidelity and Temporal-Consistency Video Prediction](https://arxiv.org/abs/2002.09905v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Bei-Jin/STMFANet)",
      "n": "WAM",
      "d": "2020-02-23",
      "m1": "159.6",
      "m2": "0.844",
      "m3": "21.02",
      "m4": "0.0936",
      "m5": "2",
      "m6": "14",
      "m7": "28"
    },
    {
      "p": "[Stochastic Latent Residual Video Prediction](https://arxiv.org/abs/2002.09219v4)",
      "c": "[&check;&nbsp;Link](https://github.com/edouardelasalles/srvp)",
      "n": "SRVP",
      "d": "2020-02-21",
      "m1": "162 \u00b1 4",
      "m2": "0.8196\u00b10.0084",
      "m3": "19.59\u00b10.27",
      "m4": "0.0574\u00b10.0032",
      "m5": "2",
      "m6": "12",
      "m7": "28"
    },
    {
      "p": "[SLAMP: Stochastic Latent Appearance and Motion Prediction](https://arxiv.org/abs/2108.02760v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kaanakan/slamp)",
      "n": "SLAMP",
      "d": "2021-08-05",
      "m1": "245 \u00b1 5",
      "m2": "0.8175\u00b10.084",
      "m3": "19.67\u00b10.26",
      "m4": "0.0596\u00b10.0032",
      "m5": "2",
      "m6": "10",
      "m7": "28"
    },
    {
      "p": "[Stochastic Video Generation with a Learned Prior](http://arxiv.org/abs/1802.07687v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edenton/svg)",
      "n": "SVG (from SRVP)",
      "d": "2018-02-21",
      "m1": "255\u00b14",
      "m2": "0.8058\u00b10.0088",
      "m3": "18.95\u00b10.26",
      "m4": "0.0609\u00b10.0034",
      "m5": "2",
      "m6": "12",
      "m7": "28"
    },
    {
      "p": "[Stochastic Video Generation with a Learned Prior](http://arxiv.org/abs/1802.07687v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edenton/svg)",
      "n": "SVG-LP (from vRNN)",
      "d": "2018-02-21",
      "m1": "256.62",
      "m2": "0.816\u00b10.07",
      "m4": "0.061\u00b10.03",
      "m5": "2",
      "m6": "10",
      "m7": "28"
    },
    {
      "p": "[Stochastic Variational Video Prediction](http://arxiv.org/abs/1710.11252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/StanfordVL/roboturk_real_dataset)",
      "n": "SV2P (from FVD)",
      "d": "2017-10-30",
      "m1": "262.5",
      "m5": "2",
      "m6": "14",
      "m7": "14"
    },
    {
      "p": "[Unsupervised Learning for Physical Interaction through Video Prediction](http://arxiv.org/abs/1605.07157v4)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/video_prediction)",
      "n": "CDNA (from FVD)",
      "d": "2016-05-23",
      "m1": "296.5",
      "m5": "2",
      "m6": "14",
      "m7": "14"
    },
    {
      "p": "[Stochastic Video Generation with a Learned Prior](http://arxiv.org/abs/1802.07687v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edenton/svg)",
      "n": "SVG-FP (from FVD)",
      "d": "2018-02-21",
      "m1": "315.5",
      "m5": "2",
      "m6": "14",
      "m7": "14"
    },
    {
      "p": "[Latent Video Transformer](https://arxiv.org/abs/2006.10704v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rakhimovv/lvt)",
      "n": "Baseline (from LVT)",
      "d": "2020-06-18",
      "m1": "320.9",
      "m5": "1",
      "m6": "15",
      "m7": "15"
    },
    {
      "p": "[MoCoGAN: Decomposing Motion and Content for Video Generation](http://arxiv.org/abs/1707.04993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sergeytulyakov/mocogan)",
      "n": "MoCoGAN",
      "d": "2017-07-17",
      "m1": "503",
      "m5": "4",
      "m6": "12",
      "m7": "12"
    },
    {
      "p": "[Stochastic Variational Video Prediction](http://arxiv.org/abs/1710.11252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/StanfordVL/roboturk_real_dataset)",
      "n": "SV2P (from SRVP)",
      "d": "2017-10-30",
      "m1": "965\u00b117",
      "m2": "0.8169\u00b10.0086",
      "m3": "20.39\u00b10.27",
      "m4": "0.0912\u00b10.0053",
      "m5": "2",
      "m6": "12",
      "m7": "28"
    },
    {
      "p": "[Stochastic Adversarial Video Prediction](http://arxiv.org/abs/1804.01523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alexlee-gk/video_prediction)",
      "n": "SAVP-VAE (from WAM)",
      "d": "2018-04-04",
      "m2": "0.815",
      "m3": "19.09",
      "m5": "2",
      "m6": "14",
      "m7": "28"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
