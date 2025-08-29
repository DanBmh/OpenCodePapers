# depth-estimation-on-stanford2d3d-panoramic

[Dataset Link](https://github.com/alexsax/2D-3D-Semantics) \
Task Hierarchy: ['Depth Estimation']

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
      "label": "RMSE",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "absolute relative error",
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
      "p": "[HiMODE: A Hybrid Monocular Omnidirectional Depth Estimation Model](https://arxiv.org/abs/2204.05007v1)",
      "c": "",
      "n": "HiMODE",
      "d": "2022-04-11",
      "m1": "0.2619",
      "m2": "0.0532"
    },
    {
      "p": "[FreDSNet: Joint Monocular Depth and Semantic Segmentation with Fast Fourier Convolutions](https://arxiv.org/abs/2210.01595v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sbrunoberenguel/fredsnet)",
      "n": "FreDSNet",
      "d": "2022-10-04",
      "m1": "0.2727",
      "m2": "0.0952"
    },
    {
      "p": "[Improving 360 Monocular Depth Estimation via Non-local Dense Prediction Transformer and Joint Supervised and Self-supervised Learning](https://arxiv.org/abs/2109.10563v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yuniw18/Joint_360depth)",
      "n": "NLFB",
      "d": "2021-09-22",
      "m1": "0.2776",
      "m2": "0.0649"
    },
    {
      "p": "[PanoFormer: Panorama Transformer for Indoor 360 Depth Estimation](https://arxiv.org/abs/2203.09283v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zhijieshen-bjtu/panoformer)",
      "n": "PanoFormer",
      "d": "2022-03-17",
      "m1": "0.3083",
      "m2": "0.0405"
    },
    {
      "p": "[ACDNet: Adaptively Combined Dilated Convolution for Monocular Panorama Depth Estimation](https://arxiv.org/abs/2112.14440v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zcq15/acdnet)",
      "n": "ACDNet",
      "d": "2021-12-29",
      "m1": "0.341",
      "m2": "0.0984"
    },
    {
      "p": "[OmniFusion: 360 Monocular Depth Estimation via Geometry-Aware Fusion](https://arxiv.org/abs/2203.00838v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yuyanli0831/omnifusion)",
      "n": "OmniFusion (2-iter)",
      "d": "2022-03-02",
      "m1": "0.3474",
      "m2": "0.095"
    },
    {
      "p": "[GLPanoDepth: Global-to-Local Panoramic Depth Estimation](https://arxiv.org/abs/2202.02796v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LeoDarcy/GLPanoDepth)",
      "n": "GLPanoDepth",
      "d": "2022-02-06",
      "m1": "0.3493"
    },
    {
      "p": "[Neural Contourlet Network for Monocular 360 Depth Estimation](https://arxiv.org/abs/2208.01817v1)",
      "c": "[&check;&nbsp;Link](https://github.com/zhijieshen-bjtu/neural-contourlet-network-for-mode)",
      "n": "Neural Contourlet Network",
      "d": "2022-08-03",
      "m1": "0.3528",
      "m2": "0.0558"
    },
    {
      "p": "[SliceNet: Deep Dense Depth Estimation From a Single Indoor Panorama Using a Slice-Based Representation](http://openaccess.thecvf.com//content/CVPR2021/html/Pintore_SliceNet_Deep_Dense_Depth_Estimation_From_a_Single_Indoor_Panorama_CVPR_2021_paper.html)",
      "c": "",
      "n": "SliceNet",
      "d": "2021-06-19",
      "m1": "0.3684",
      "m2": "0.0744"
    },
    {
      "p": "[Distortion-Aware Convolutional Filters for Dense Prediction in Panoramic Images](http://openaccess.thecvf.com/content_ECCV_2018/html/Keisuke_Tateno_Distortion-Aware_Convolutional_Filters_ECCV_2018_paper.html)",
      "c": "",
      "n": "DisConv",
      "d": "2018-09-01",
      "m1": "0.369",
      "m2": "0.176"
    },
    {
      "p": "[UniFuse: Unidirectional Fusion for 360$^{\\circ}$ Panorama Depth Estimation](https://arxiv.org/abs/2102.03550v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/UniFuse-Unidirectional-Fusion)",
      "n": "UniFuse with fusion",
      "d": "2021-02-06",
      "m1": "0.3691",
      "m2": "0.1114"
    },
    {
      "p": "[BiFuse++: Self-supervised and Efficient Bi-projection Fusion for 360 Depth Estimation](https://arxiv.org/abs/2209.02952v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fuenwang/bifusev2)",
      "n": "BiFuse++",
      "d": "2022-09-07",
      "m1": "0.372",
      "m2": "0.1117"
    },
    {
      "p": "[PanoDepth: A Two-Stage Approach for Monocular Omnidirectional Depth Estimation](https://arxiv.org/abs/2202.01323v1)",
      "c": "",
      "n": "PanoDepth",
      "d": "2022-02-02",
      "m1": "0.3747",
      "m2": "0.0972"
    },
    {
      "p": "[HoHoNet: 360 Indoor Holistic Understanding with Latent Horizontal Features](https://arxiv.org/abs/2011.11498v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sunset1995/HoHoNet)",
      "n": "HoHoNet (ResNet-101)",
      "d": "2020-11-23",
      "m1": "0.3834",
      "m2": "0.1014"
    },
    {
      "p": "[BiFuse: Monocular 360 Depth Estimation via Bi-Projection Fusion](http://openaccess.thecvf.com/content_CVPR_2020/html/Wang_BiFuse_Monocular_360_Depth_Estimation_via_Bi-Projection_Fusion_CVPR_2020_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/Yeh-yu-hsuan/BiFuse)",
      "n": "BiFuse with fusion",
      "d": "2020-06-01",
      "m1": "0.4142",
      "m2": "0.1209"
    },
    {
      "p": "[Geometric Structure Based and Regularized Depth Estimation From 360 Indoor Imagery](http://openaccess.thecvf.com/content_CVPR_2020/html/Jin_Geometric_Structure_Based_and_Regularized_Depth_Estimation_From_360_Indoor_CVPR_2020_paper.html)",
      "c": "",
      "n": "Jin et al.",
      "d": "2020-06-01",
      "m1": "0.421"
    },
    {
      "p": "[SphereDepth: Panorama Depth Estimation from Spherical Domain](https://arxiv.org/abs/2208.13714v3)",
      "c": "",
      "n": "SphereDepth",
      "d": "2022-08-29",
      "m1": "0.4512",
      "m2": "0.1158"
    },
    {
      "p": "[OmniDepth: Dense Depth Estimation for Indoors Spherical Panoramas](http://arxiv.org/abs/1807.09620v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VCL3D/SphericalViewSynthesis)",
      "n": "OmniDepth",
      "d": "2018-07-25",
      "m1": "0.6152",
      "m2": "0.1996 "
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
