# monocular-depth-estimation-on-kitti-eigen

[Dataset Link](http://www.cvlibs.net/datasets/kitti/) \
Task Hierarchy: ['3D', 'Depth Estimation', 'Monocular Depth Estimation']

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
      "label": "absolute relative error",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "RMSE",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Sq Rel",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "RMSE log",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Delta < 1.25",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Delta < 1.25^2",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "Delta < 1.25^3",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "Square relative error (SqRel)",
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
      "p": "[SPIdepth: Strengthened Pose Information for Self-supervised Monocular Depth Estimation](https://arxiv.org/abs/2404.12501v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Lavreniuk/SPIdepth)",
      "n": "SPIDepth",
      "d": "2024-04-18",
      "m1": "0.029",
      "m2": "1.394",
      "m3": "0.069",
      "m4": "0.048",
      "m5": "0.99",
      "m6": "0.999",
      "m7": "1.000"
    },
    {
      "p": "[UniK3D: Universal Camera Monocular 3D Estimation](https://arxiv.org/abs/2503.16591v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lpiccinelli-eth/UniK3D)",
      "n": "UniK3D (FT, metric)",
      "d": "2025-03-20",
      "m1": "0.037",
      "m2": "1.68",
      "m4": "0.060",
      "m5": "0.990",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[UniDepthV2: Universal Monocular Metric Depth Estimation Made Simpler](https://arxiv.org/abs/2502.20110v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lpiccinelli-eth/unidepth)",
      "n": "UniDepthV2 (FT, metric)",
      "d": "2025-02-27",
      "m1": "0.037",
      "m2": "1.71",
      "m4": "0.061",
      "m5": "0.989",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[Metric3Dv2: A Versatile Monocular Geometric Foundation Model for Zero-shot Metric Depth and Surface Normal Estimation](https://arxiv.org/abs/2404.15506v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yvanyin/metric3d)",
      "n": "Metric3Dv2 (g2, FT, 80m, flip_aug_test)",
      "d": "2024-03-22",
      "m1": "0.039",
      "m2": "1.766",
      "m4": "0.060",
      "m5": "0.989",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[LightedDepth: Video Depth Estimation in Light of Limited Inference View Angles](http://openaccess.thecvf.com//content/CVPR2023/html/Zhu_LightedDepth_Video_Depth_Estimation_in_Light_of_Limited_Inference_View_CVPR_2023_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/shngjz/lighteddepth)",
      "n": "LightedDepth (Video Method)",
      "d": "2023-01-01",
      "m1": "0.041",
      "m2": "1.748",
      "m3": "0.107",
      "m4": "0.059",
      "m5": "0.989",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[FutureDepth: Learning to Predict the Future Improves Video Depth Estimation](https://arxiv.org/abs/2403.12953v2)",
      "c": "",
      "n": "FutureDepth",
      "d": "2024-03-19",
      "m1": "0.041",
      "m2": "1.856",
      "m3": "0.117",
      "m4": "0.066",
      "m5": "0.984",
      "m6": "0.998",
      "m7": "1.000",
      "m8": "0.117"
    },
    {
      "p": "[UniDepth: Universal Monocular Metric Depth Estimation](https://arxiv.org/abs/2403.18913v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lpiccinelli-eth/unidepth)",
      "n": "UniDepth (Zero-shot)",
      "d": "2024-03-27",
      "m1": "0.042",
      "m2": "1.75",
      "m4": "0.064",
      "m5": "0.986",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[SQLdepth: Generalizable Self-Supervised Fine-Structured Monocular Depth Estimation](https://arxiv.org/abs/2309.00526v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hisfog/SfMNeXt-Impl)",
      "n": "SQLdepth (ConvNeXt-L)",
      "d": "2023-09-01",
      "m1": "0.043",
      "m2": "1.698",
      "m3": "0.105",
      "m4": "0.064",
      "m5": "0.983",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving](https://arxiv.org/abs/2403.07535v1)",
      "c": "[&check;&nbsp;Link](https://github.com/junda24/afnet)",
      "n": "AFNet",
      "d": "2024-03-12",
      "m1": "0.044",
      "m2": "1.712",
      "m3": "0.132",
      "m4": "0.069",
      "m5": "0.980",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LiheYoung/Depth-Anything)",
      "n": "Depth Anything",
      "d": "2024-01-19",
      "m1": "0.046",
      "m2": "1.896",
      "m3": "0.121",
      "m4": "0.069",
      "m5": "0.982",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[Harnessing Diffusion Models for Visual Perception with Meta Prompts](https://arxiv.org/abs/2312.14733v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fudan-zvg/meta-prompts)",
      "n": "MetaPrompt-SD",
      "d": "2023-12-22",
      "m1": "0.047",
      "m2": "1.928",
      "m3": "0.125",
      "m4": "0.071",
      "m5": "0.981",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation](https://arxiv.org/abs/2403.18807v4)",
      "c": "[&check;&nbsp;Link](https://github.com/aradhye2002/ecodepth)",
      "n": "ECoDepth",
      "d": "2024-03-27",
      "m1": "0.048",
      "m2": "1.966",
      "m3": "0.139",
      "m4": "0.074",
      "m5": "0.979",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[ScaleDepth: Decomposing Metric Depth Estimation into Scale Prediction and Relative Depth Estimation](https://arxiv.org/abs/2407.08187v1)",
      "c": "[&check;&nbsp;Link](https://github.com/RuijieZhu94/mmdepth/blob/main/projects/ScaleDepth/README.md)",
      "n": "ScaleDepth-K",
      "d": "2024-07-11",
      "m1": "0.048",
      "m2": "1.987",
      "m3": "0.136",
      "m4": "0.073",
      "m5": "0.98",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[EVP: Enhanced Visual Perception using Inverse Multi-Attentive Feature Refinement and Regularized Image-Text Alignment](https://arxiv.org/abs/2312.08548v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lavreniuk/evp)",
      "n": "EVP",
      "d": "2023-12-13",
      "m1": "0.048",
      "m2": "2.015",
      "m3": "0.136",
      "m4": "0.073",
      "m5": "0.980",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[GEDepth: Ground Embedding for Monocular Depth Estimation](https://arxiv.org/abs/2309.09975v1)",
      "c": "[&check;&nbsp;Link](https://github.com/qcraftai/gedepth)",
      "n": "GEDepth",
      "d": "2023-09-18",
      "m1": "0.048",
      "m2": "2.044",
      "m3": "0.142",
      "m4": "0.076",
      "m5": "0.9763",
      "m6": "0.9972",
      "m7": "0.9993"
    },
    {
      "p": "[MAMo: Leveraging Memory and Attention for Monocular Video Depth Estimation](https://arxiv.org/abs/2307.14336v3)",
      "c": "",
      "n": "MAMo",
      "d": "2023-07-26",
      "m1": "0.049",
      "m2": "1.984",
      "m3": "0.13",
      "m4": "0.072",
      "m5": "0.977",
      "m6": "0.998",
      "m7": "0.9995"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-L 1K-MIM",
      "d": "2022-05-26",
      "m1": "0.050",
      "m2": "1.966",
      "m3": "0.139",
      "m4": "0.075",
      "m5": "0.977",
      "m6": "0.998",
      "m7": "1.000"
    },
    {
      "p": "[IEBins: Iterative Elastic Bins for Monocular Depth Estimation](https://arxiv.org/abs/2309.14137v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shuweishao/iebins)",
      "n": "IEBins",
      "d": "2023-09-25",
      "m1": "0.050",
      "m2": "2.011",
      "m3": "0.142",
      "m4": "0.075",
      "m5": "0.978",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[NDDepth: Normal-Distance Assisted Monocular Depth Estimation](https://arxiv.org/abs/2309.10592v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ShuweiShao/NDDepth)",
      "n": "NDDepth",
      "d": "2023-09-19",
      "m1": "0.050",
      "m2": "2.025",
      "m3": "0.141",
      "m4": "0.075",
      "m5": "0.978",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[URCDC-Depth: Uncertainty Rectified Cross-Distillation with CutFlip for Monocular Depth Estimation](https://arxiv.org/abs/2302.08149v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shuweishao/urcdc-depth)",
      "n": "URCDC-Depth",
      "d": "2023-02-16",
      "m1": "0.050",
      "m2": "2.032",
      "m3": "0.142",
      "m4": "0.076",
      "m5": "0.977",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[iDisc: Internal Discretization for Monocular Depth Estimation](https://arxiv.org/abs/2304.06334v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lpiccinelli-eth/unidepth)",
      "n": "iDisc",
      "d": "2023-04-13",
      "m1": "0.050",
      "m2": "2.067",
      "m3": "0.145",
      "m4": "0.077",
      "m5": "0.977",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[DDP: Diffusion Model for Dense Visual Prediction](https://arxiv.org/abs/2303.17559v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiyuanfeng/ddp)",
      "n": "DDP (Swin-L, step-3)",
      "d": "2023-03-30",
      "m1": "0.050",
      "m2": "2.072",
      "m3": "0.148",
      "m4": "0.076",
      "m5": "0.975",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[Analysis of NaN Divergence in Training Monocular Depth Estimation Model](https://arxiv.org/abs/2311.03938v1)",
      "c": "",
      "n": "MIM-Swin-V2",
      "d": "2023-11-07",
      "m1": "0.0508",
      "m2": "2.0373",
      "m3": "0.1458",
      "m4": "0.077",
      "m5": "0.9757",
      "m6": "0.9974",
      "m7": "0.9994"
    },
    {
      "p": "[Attention Attention Everywhere: Monocular Depth Prediction with Skip Attention](https://arxiv.org/abs/2210.09071v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ashutosh1807/pixelformer)",
      "n": "PixelFormer",
      "d": "2022-10-17",
      "m1": "0.051",
      "m2": "2.081",
      "m3": "0.149",
      "m4": "0.077",
      "m5": "0.976",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[Revealing the Dark Secrets of Masked Image Modeling](https://arxiv.org/abs/2205.13543v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/MIM-Depth-Estimation)",
      "n": "SwinV2-B 1K-MIM",
      "d": "2022-05-26",
      "m1": "0.052",
      "m2": "2.050",
      "m3": "0.148",
      "m4": "0.078",
      "m5": "0.976",
      "m6": "0.998",
      "m7": "0.999"
    },
    {
      "p": "[BinsFormer: Revisiting Adaptive Bins for Monocular Depth Estimation](https://arxiv.org/abs/2204.00987v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zhyever/monocular-depth-estimation-toolbox)",
      "n": "BinsFormer",
      "d": "2022-04-03",
      "m1": "0.052",
      "m2": "2.098",
      "m3": "0.151",
      "m4": "0.079",
      "m5": "0.974",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[NeW CRFs: Neural Window Fully-connected CRFs for Monocular Depth Estimation](https://arxiv.org/abs/2203.01502v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aliyun/NeWCRFs)",
      "n": "NeWCRFs",
      "d": "2022-03-03",
      "m1": "0.052",
      "m2": "2.129",
      "m3": "0.155",
      "m4": "0.079",
      "m5": "0.974",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[DepthFormer: Exploiting Long-Range Correlation and Local Information for Accurate Monocular Depth Estimation](https://arxiv.org/abs/2203.14211v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zhyever/Monocular-Depth-Estimation-Toolbox/tree/main/configs/depthformer)",
      "n": "DepthFormer",
      "d": "2022-03-27",
      "m1": "0.052",
      "m2": "2.143",
      "m3": "0.158",
      "m4": "0.079",
      "m5": "0.975",
      "m6": "0.997",
      "m7": "0.999"
    },
    {
      "p": "[Monocular Depth Estimation through Virtual-world Supervision and Real-world SfM Self-Supervision](https://arxiv.org/abs/2103.12209v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HMRC-AEL/MonoDEVSNet)",
      "n": "MonoDELSNet",
      "d": "2021-03-22",
      "m1": "0.053",
      "m2": "2.101",
      "m3": "0.161",
      "m4": "0.082",
      "m5": "0.969",
      "m6": "0.996",
      "m7": "0.999"
    },
    {
      "p": "[Deep Two-View Structure-from-Motion Revisited](https://arxiv.org/abs/2104.00556v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jytime/Deep-SfM-Revisited)",
      "n": "SfM-Revisited",
      "d": "2021-04-01",
      "m1": "0.055",
      "m2": "2.273",
      "m3": "0.224"
    },
    {
      "p": "[D-Net: A Generalised and Optimised Deep Network for Monocular Depth Estimation](https://ieeexplore.ieee.org/document/9551940)",
      "c": "[&check;&nbsp;Link](https://github.com/Joshuat38/D-Net)",
      "n": "D-Net",
      "d": "2021-09-29",
      "m1": "0.056",
      "m2": "2.362",
      "m3": "0.189",
      "m4": "0.087",
      "m5": "0.963",
      "m6": "0.995",
      "m7": "0.999"
    },
    {
      "p": "[Global-Local Path Networks for Monocular Depth Estimation with Vertical CutDepth](https://arxiv.org/abs/2201.07436v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "GLPDepth",
      "d": "2022-01-19",
      "m1": "0.057",
      "m2": "2.297",
      "m4": "0.086",
      "m5": "0.967",
      "m6": "0.996",
      "m7": "0.999"
    },
    {
      "p": "[NVS-MonoDepth: Improving Monocular Depth Prediction with Novel View Synthesis](https://arxiv.org/abs/2112.12577v1)",
      "c": "",
      "n": "NVS-MonoDepth",
      "d": "2021-12-22",
      "m1": "0.057",
      "m2": "2.702"
    },
    {
      "p": "[Depthformer : Multiscale Vision Transformer For Monocular Depth Estimation With Local Global Information Fusion](https://arxiv.org/abs/2207.04535v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ashutosh1807/depthformer)",
      "n": "Depthformer",
      "d": "2022-07-10",
      "m1": "0.058",
      "m2": "2.285",
      "m3": "0.187",
      "m4": " 0.087",
      "m5": "0.967",
      "m6": "0.996",
      "m7": "0.999"
    },
    {
      "p": "[AdaBins: Depth Estimation using Adaptive Bins](https://arxiv.org/abs/2011.14141v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shariqfarooq123/AdaBins)",
      "n": "AdaBins",
      "d": "2020-11-28",
      "m1": "0.058",
      "m2": "2.360",
      "m4": "0.088",
      "m5": "0.964",
      "m6": "0.995",
      "m7": "0.999"
    },
    {
      "p": "[Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image](https://arxiv.org/abs/2307.10984v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yvanyin/metric3d)",
      "n": "Metric3D (zero-shot)",
      "d": "2023-07-20",
      "m1": "0.058",
      "m2": "2.77",
      "m5": "0.967",
      "m6": "0.995",
      "m7": "0.999"
    },
    {
      "p": "[Monocular Depth Estimation Using Laplacian Pyramid-Based Depth Residuals](https://ieeexplore.ieee.org/document/9316778)",
      "c": "[&check;&nbsp;Link](https://github.com/tjqansthd/LapDepth-release)",
      "n": "LapDepth",
      "d": "2021-01-08",
      "m1": "0.059",
      "m2": "2.446",
      "m4": "0.091",
      "m5": "0.962",
      "m6": "0.994",
      "m7": "0.999"
    },
    {
      "p": "[Vision Transformers for Dense Prediction](https://arxiv.org/abs/2103.13413v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DPT-Hybrid",
      "d": "2021-03-24",
      "m1": "0.062",
      "m2": "2.573",
      "m4": "0.092",
      "m5": "0.959",
      "m6": "0.995",
      "m7": "0.999"
    },
    {
      "p": "[From Big to Small: Multi-Scale Local Planar Guidance for Monocular Depth Estimation](https://arxiv.org/abs/1907.10326v6)",
      "c": "[&check;&nbsp;Link](https://github.com/cleinc/bts)",
      "n": "BTS",
      "d": "2019-07-24",
      "m1": "0.064"
    },
    {
      "p": "[DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DINOv2 (ViT-g/14 frozen, w/ DPT decoder)",
      "d": "2023-04-14",
      "m1": "0.0652",
      "m2": "2.1128",
      "m3": "0.1797",
      "m4": "0.0882",
      "m5": "0.968",
      "m6": "0.997",
      "m7": "0.9993"
    },
    {
      "p": "[LightDepth: A Resource Efficient Depth Estimation Approach for Dealing with Ground Truth Sparsity via Curriculum Learning](https://arxiv.org/abs/2211.08608v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fatemehkarimii/lightdepth)",
      "n": "LightDepth",
      "d": "2022-11-16",
      "m1": "0.070",
      "m2": "2.923"
    },
    {
      "p": "[Deep Ordinal Regression Network for Monocular Depth Estimation](http://arxiv.org/abs/1806.02446v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hufu6371/DORN)",
      "n": "DORN",
      "d": "2018-06-06",
      "m1": "0.072",
      "m2": "2.727",
      "m4": "0.120",
      "m5": "0.932",
      "m6": "0.984",
      "m7": "0.994"
    },
    {
      "p": "[Enforcing geometric constraints of virtual normal for depth prediction](https://arxiv.org/abs/1907.12209v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aim-uofa/AdelaiDepth)",
      "n": "VNL",
      "d": "2019-07-29",
      "m1": "0.072"
    },
    {
      "p": "[PrimeDepth: Efficient Monocular Depth Estimation with a Stable Diffusion Preimage](https://arxiv.org/abs/2409.09144v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vislearn/PrimeDepth)",
      "n": "PrimeDepth + Depth Anything",
      "d": "2024-09-13",
      "m1": "0.073",
      "m5": "0.953"
    },
    {
      "p": "[On Deep Learning Techniques to Boost Monocular Depth Estimation for Autonomous Navigation](https://arxiv.org/abs/2010.06626v2)",
      "c": "",
      "n": "DSN",
      "d": "2020-10-13",
      "m1": "0.075"
    },
    {
      "p": "[PrimeDepth: Efficient Monocular Depth Estimation with a Stable Diffusion Preimage](https://arxiv.org/abs/2409.09144v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vislearn/PrimeDepth)",
      "n": "PrimeDepth",
      "d": "2024-09-13",
      "m1": "0.079",
      "m5": "0.937"
    },
    {
      "p": "[Focal-WNet: An Architecture Unifying Convolution and Attention for Depth Estimation](https://ieeexplore.ieee.org/abstract/document/9824488)",
      "c": "[&check;&nbsp;Link](https://github.com/Goubeast/Focal-WNet)",
      "n": "Focal-WNet",
      "d": "2022-07-18",
      "m1": "0.082",
      "m2": "3.076",
      "m4": "0.120",
      "m5": "0.926",
      "m6": "0.986",
      "m7": "0.997"
    },
    {
      "p": "[DepthMaster: Taming Diffusion Models for Monocular Depth Estimation](https://arxiv.org/abs/2501.02576v1)",
      "c": "[&check;&nbsp;Link](https://github.com/indu1ge/DepthMaster)",
      "n": "DepthMaster",
      "d": "2025-01-05",
      "m1": "0.082",
      "m5": "0.937"
    },
    {
      "p": "[Manydepth2: Motion-Aware Self-Supervised Multi-Frame Monocular Depth Estimation in Dynamic Scenes](https://arxiv.org/abs/2312.15268v8)",
      "c": "[&check;&nbsp;Link](https://github.com/kaichen-z/rad)",
      "n": "Manydepth2",
      "d": "2023-12-23",
      "m1": "0.091",
      "m2": "4.232",
      "m3": "0.170",
      "m4": "0.649",
      "m5": "0.909",
      "m6": "0.968",
      "m7": "0.984"
    },
    {
      "p": "[Enhancing self-supervised monocular depth estimation with traditional visual odometry](https://arxiv.org/abs/1908.03127v2)",
      "c": "",
      "n": "VOMonodepth",
      "d": "2019-08-08",
      "m1": "0.091"
    },
    {
      "p": "[High Quality Monocular Depth Estimation via Transfer Learning](http://arxiv.org/abs/1812.11941v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ialhashim/DenseDepth)",
      "n": "DenseDepth",
      "d": "2018-12-31",
      "m1": "0.093"
    },
    {
      "p": "[Single View Stereo Matching](http://arxiv.org/abs/1803.02612v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lawy623/SVS)",
      "n": "SVS",
      "d": "2018-03-07",
      "m1": "0.094"
    },
    {
      "p": "[Learning monocular depth estimation infusing traditional stereo knowledge](http://arxiv.org/abs/1904.04144v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fabiotosi92/monoResMatch-Tensorflow)",
      "n": "monoResMatch",
      "d": "2019-04-08",
      "m1": "0.096"
    },
    {
      "p": "[Semi-Supervised Monocular Depth Estimation with Left-Right Consistency Using Deep Neural Network](https://arxiv.org/abs/1905.07542v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jahaniam/semidepth)",
      "n": "SemiDepth",
      "d": "2019-05-18",
      "m1": "0.096"
    },
    {
      "p": "[Monocular Depth Estimation by Learning from Heterogeneous Datasets](http://arxiv.org/abs/1803.08018v2)",
      "c": "",
      "n": "CFA",
      "d": "2018-03-21",
      "m1": "0.096"
    },
    {
      "p": "[Self-Supervised Monocular Depth Hints](https://arxiv.org/abs/1909.09051v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nianticlabs/depth-hints)",
      "n": "Depth Hints",
      "d": "2019-09-19",
      "m1": "0.096"
    },
    {
      "p": "[Structure-Attentioned Memory Network for Monocular Depth Estimation](https://arxiv.org/abs/1909.04594v1)",
      "c": "",
      "n": "SOM",
      "d": "2019-09-10",
      "m1": "0.097"
    },
    {
      "p": "[Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://arxiv.org/abs/2312.02145v2)",
      "c": "[&check;&nbsp;Link](https://github.com/prs-eth/marigold)",
      "n": "Marigold",
      "d": "2023-12-04",
      "m1": "0.099",
      "m2": "3.304",
      "m4": "0.138",
      "m5": "0.916",
      "m6": "0.987",
      "m7": "0.996"
    },
    {
      "p": "[GCNDepth: Self-supervised Monocular Depth Estimation based on Graph Convolutional Network](https://arxiv.org/abs/2112.06782v1)",
      "c": "[&check;&nbsp;Link](https://github.com/arminmasoumian/gcndepth)",
      "n": "GCNDepth",
      "d": "2021-12-13",
      "m1": "0.104",
      "m2": "4.494",
      "m4": "0.181",
      "m5": "0.888",
      "m6": "0.965",
      "m7": "0.984"
    },
    {
      "p": "[Digging Into Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/1806.01260v4)",
      "c": "[&check;&nbsp;Link](https://github.com/nianticlabs/monodepth2)",
      "n": "monodepth2 M",
      "d": "2018-06-04",
      "m1": "0.106"
    },
    {
      "p": "[Single Image Depth Estimation Trained via Depth from Defocus Cues](https://arxiv.org/abs/2001.05036v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shirgur/UnsupervisedDepthFromFocus)",
      "n": "DeepLabV3+ (F10)",
      "d": "2020-01-14",
      "m1": "0.110"
    },
    {
      "p": "[DiPE: Deeper into Photometric Errors for Unsupervised Learning of Depth and Ego-motion from Monocular Videos](https://arxiv.org/abs/2003.01360v3)",
      "c": "[&check;&nbsp;Link](https://github.com/HalleyJiang/DiPE)",
      "n": "DiPE",
      "d": "2020-03-03",
      "m1": "0.112"
    },
    {
      "p": "[Toward Hierarchical Self-Supervised Monocular Absolute Depth Estimation for Autonomous Driving Applications](https://arxiv.org/abs/2004.05560v2)",
      "c": "[&check;&nbsp;Link](https://github.com/TJ-IPLab/DNet)",
      "n": "DNet",
      "d": "2020-04-12",
      "m1": "0.113",
      "m2": "4.812",
      "m4": "0.191",
      "m5": "0.877",
      "m6": "0.960",
      "m7": "0.981"
    },
    {
      "p": "[Learn Stereo, Infer Mono: Siamese Networks for Self-Supervised, Monocular, Depth Estimation](http://arxiv.org/abs/1905.00401v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mtngld/lsim)",
      "n": "LSIM",
      "d": "2019-05-01",
      "m1": "0.113"
    },
    {
      "p": "[Unsupervised Scale-consistent Depth Learning from Video](https://arxiv.org/abs/2105.11610v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JiawangBian/SC-SfMLearner-Release)",
      "n": "SC-Depth (ResNet 50)",
      "d": "2021-05-25",
      "m1": "0.114",
      "m2": "4.706",
      "m4": "0.191",
      "m5": "0.873",
      "m6": "0.960",
      "m7": "0.982"
    },
    {
      "p": "[Towards Scene Understanding: Unsupervised Monocular Depth Estimation With Semantic-Aware Representation](http://openaccess.thecvf.com/content_CVPR_2019/html/Chen_Towards_Scene_Understanding_Unsupervised_Monocular_Depth_Estimation_With_Semantic-Aware_Representation_CVPR_2019_paper.html)",
      "c": "",
      "n": "SemanticAware",
      "d": "2019-06-01",
      "m1": "0.118"
    },
    {
      "p": "[Unsupervised Scale-consistent Depth Learning from Video](https://arxiv.org/abs/2105.11610v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JiawangBian/SC-SfMLearner-Release)",
      "n": "SC-Depth (ResNet18)",
      "d": "2021-05-25",
      "m1": "0.119",
      "m2": "4.950",
      "m4": "0.197",
      "m5": "0.863",
      "m6": "0.957",
      "m7": "0.981"
    },
    {
      "p": "[3D Packing for Self-Supervised Monocular Depth Estimation](https://arxiv.org/abs/1905.02693v4)",
      "c": "[&check;&nbsp;Link](https://github.com/TRI-ML/packnet-sfm)",
      "n": "PackNet-SfM",
      "d": "2019-05-06",
      "m1": "0.12"
    },
    {
      "p": "[Learning monocular depth estimation with unsupervised trinocular assumptions](http://arxiv.org/abs/1808.01606v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mattpoggi/3net)",
      "n": "3Net",
      "d": "2018-08-05",
      "m1": "0.126"
    },
    {
      "p": "[Unsupervised Scale-consistent Depth and Ego-motion Learning from Monocular Video](https://arxiv.org/abs/1908.10553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/JiawangBian/SC-SfMLearner-Release)",
      "n": "SC-SfMLearner_CS+K",
      "d": "2019-08-28",
      "m1": "0.128"
    },
    {
      "p": "[Self-supervised Learning for Single View Depth and Surface Normal Estimation](http://arxiv.org/abs/1903.00112v1)",
      "c": "",
      "n": "SelfDepthNorm",
      "d": "2019-03-01",
      "m1": "0.133"
    },
    {
      "p": "[SIGNet: Semantic Instance Aided Unsupervised 3D Geometry Perception](http://arxiv.org/abs/1812.05642v2)",
      "c": "[&check;&nbsp;Link](https://github.com/mengyuest/SIGNet)",
      "n": "SIGNet",
      "d": "2018-12-13",
      "m1": "0.133"
    },
    {
      "p": "[Depth Prediction Without the Sensors: Leveraging Structure for Unsupervised Learning from Monocular Videos](http://arxiv.org/abs/1811.06152v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/struct2depth)",
      "n": "struct2depth",
      "d": "2018-11-15",
      "m1": "0.135"
    },
    {
      "p": "[Unsupervised Scale-consistent Depth and Ego-motion Learning from Monocular Video](https://arxiv.org/abs/1908.10553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/JiawangBian/SC-SfMLearner-Release)",
      "n": "SC-SfMLearner",
      "d": "2019-08-28",
      "m1": "0.137"
    },
    {
      "p": "[Competitive Collaboration: Joint Unsupervised Learning of Depth, Camera Motion, Optical Flow and Motion Segmentation](http://arxiv.org/abs/1805.09806v3)",
      "c": "[&check;&nbsp;Link](https://github.com/anuragranj/cc)",
      "n": "CC",
      "d": "2018-05-24",
      "m1": "0.140"
    },
    {
      "p": "[Scaling up Multi-domain Semantic Segmentation with Sentence Embeddings](https://arxiv.org/abs/2202.02002v2)",
      "c": "",
      "n": "SIW",
      "d": "2022-02-04",
      "m1": "0.14"
    },
    {
      "p": "[Learning to Recover 3D Scene Shape from a Single Image](https://arxiv.org/abs/2012.09365v1)",
      "c": "[&check;&nbsp;Link](https://github.com/aim-uofa/AdelaiDepth)",
      "n": "LeReS",
      "d": "2020-12-17",
      "m1": "0.149",
      "m5": "0.784"
    },
    {
      "p": "[Geometry-Aware Symmetric Domain Adaptation for Monocular Depth Estimation](http://arxiv.org/abs/1904.01870v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sshan-zhao/GASDA)",
      "n": "GASDA",
      "d": "2019-04-03",
      "m1": "0.149"
    },
    {
      "p": "[Veritatem Dies Aperit- Temporally Consistent Depth Prediction Enabled by a Multi-Task Geometric and Semantic Scene Understanding Approach](https://arxiv.org/abs/1903.10764v2)",
      "c": "[&check;&nbsp;Link](https://github.com/atapour/temporal-depth-segmentation)",
      "n": "VDA",
      "d": "2019-03-26",
      "m1": "0.193"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
