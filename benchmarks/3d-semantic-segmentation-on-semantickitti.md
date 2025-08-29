# 3d-semantic-segmentation-on-semantickitti

[Dataset Link](http://www.semantic-kitti.org/) \
Task Hierarchy: ['Semantic Segmentation', '3D Semantic Segmentation']

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
      "label": "test mIoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "val mIoU",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "mIoU-1%",
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
      "p": "[LSK3DNet: Towards Effective and Efficient 3D Perception with Large Sparse Kernels](https://arxiv.org/abs/2403.15173v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fengzicai/lsk3dnet)",
      "n": "LSK3DNet",
      "d": "2024-03-22",
      "m1": "75.6%",
      "m2": "70.2%"
    },
    {
      "p": "[Point Transformer V3: Simpler, Faster, Stronger](https://arxiv.org/abs/2312.10035v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Pointcept/Pointcept)",
      "n": "PPT+PTv3",
      "d": "2023-12-15",
      "m1": "75.5%",
      "m2": "72.3%"
    },
    {
      "p": "[UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase](https://arxiv.org/abs/2309.05573v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pjlab-adg/pcseg)",
      "n": "UniSeg",
      "d": "2023-09-11",
      "m1": "75.2%",
      "m2": "71.3%"
    },
    {
      "p": "[Spherical Transformer for LiDAR-based 3D Recognition](https://arxiv.org/abs/2303.12766v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dvlab-research/sphereformer)",
      "n": "SphereFormer",
      "d": "2023-03-22",
      "m1": "74.8%",
      "m2": "67.8%"
    },
    {
      "p": "[DINO in the Room: Leveraging 2D Foundation Models for 3D Segmentation](https://arxiv.org/abs/2503.18944v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VisualComputingInstitute/DITR)",
      "n": "DITR",
      "d": "2025-03-24",
      "m1": "74.4%",
      "m2": "69.0%"
    },
    {
      "p": "[FRNet: Frustum-Range Networks for Scalable LiDAR Segmentation](https://arxiv.org/abs/2312.04484v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ldkong1205/Robo3D)",
      "n": "FRNet",
      "d": "2023-12-07",
      "m1": "73.3%",
      "m2": "68.7%"
    },
    {
      "p": "[Rethinking Range View Representation for LiDAR Segmentation](https://arxiv.org/abs/2303.05367v3)",
      "c": "",
      "n": "RangeFormer",
      "d": "2023-03-09",
      "m1": "73.3%",
      "m2": "67.6%"
    },
    {
      "p": "[2DPASS: 2D Priors Assisted Semantic Segmentation on LiDAR Point Clouds](https://arxiv.org/abs/2207.04397v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yanx27/2dpass)",
      "n": "2DPASS",
      "d": "2022-07-10",
      "m1": "72.9%",
      "m2": "69.3%"
    },
    {
      "p": "[Point Transformer V2: Grouped Vector Attention and Partition-based Pooling](https://arxiv.org/abs/2210.05666v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Pointcept/Pointcept)",
      "n": "PTv2",
      "d": "2022-10-11",
      "m1": "72.6%",
      "m2": "70.3%"
    },
    {
      "p": "[Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation](https://arxiv.org/abs/2206.02099v1)",
      "c": "",
      "n": "PVKD",
      "d": "2022-06-05",
      "m1": "71.2%"
    },
    {
      "p": "[(AF)2-S3Net: Attentive Feature Fusion with Adaptive Feature Selection for Sparse Semantic Segmentation Network](https://arxiv.org/abs/2102.04530v1)",
      "c": "",
      "n": "AF2S3Net",
      "d": "2021-02-08",
      "m1": "70.8%",
      "m2": "74.2%"
    },
    {
      "p": "[Using a Waffle Iron for Automotive Point Cloud Semantic Segmentation](https://arxiv.org/abs/2301.10100v2)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/waffleiron)",
      "n": "WaffleIron",
      "d": "2023-01-24",
      "m1": "70.8%",
      "m2": "68.0%"
    },
    {
      "p": "[Cylindrical and Asymmetrical 3D Convolution Networks for LiDAR Segmentation](https://arxiv.org/abs/2011.10033v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xinge008/Cylinder3D)",
      "n": "Cylinder3D",
      "d": "2020-11-19",
      "m1": "68.9%",
      "m2": "64.3%"
    },
    {
      "p": "[Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution](https://arxiv.org/abs/2007.16100v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Pointcept/Pointcept)",
      "n": "SPVNAS",
      "d": "2020-07-31",
      "m1": "66.4%",
      "m2": "64.7%"
    },
    {
      "p": "[Sparse Single Sweep LiDAR Point Cloud Segmentation via Learning Contextual Shape Priors from Scene Completion](https://arxiv.org/abs/2012.03762v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yanx27/JS3C-Net)",
      "n": "JS3C-Net",
      "d": "2020-12-07",
      "m1": "66.0%"
    },
    {
      "p": "[GFNet: Geometric Flow Network for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2207.02605v2)",
      "c": "[&check;&nbsp;Link](https://github.com/haibo-qiu/gfnet)",
      "n": "GFNet",
      "d": "2022-07-06",
      "m1": "65.4%"
    },
    {
      "p": "[KPRNet: Improving projection-based LiDAR semantic segmentation](https://arxiv.org/abs/2007.12668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DeyvidKochanov-TomTom/kprnet)",
      "n": "KPRNet",
      "d": "2020-07-24",
      "m1": "63.1%"
    },
    {
      "p": "[TORNADO-Net: mulTiview tOtal vaRiatioN semAntic segmentation with Diamond inceptiOn module](https://arxiv.org/abs/2008.10544v1)",
      "c": "",
      "n": "TORNADONet-HiRes",
      "d": "2020-08-24",
      "m1": "63.1%"
    },
    {
      "p": "[Number-Adaptive Prototype Learning for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2210.09948v1)",
      "c": "",
      "n": "NAPL",
      "d": "2022-10-18",
      "m1": "61.6%"
    },
    {
      "p": "[Meta-RangeSeg: LiDAR Sequence Semantic Segmentation Using Multiple Feature Aggregation](https://arxiv.org/abs/2202.13377v3)",
      "c": "[&check;&nbsp;Link](https://github.com/songw-zju/Meta-RangeSeg)",
      "n": "Meta-RangeSeg",
      "d": "2022-02-27",
      "m1": "61.0%"
    },
    {
      "p": "[Semantic Segmentation for Real Point Cloud Scenes via Bilateral Augmentation and Adaptive Fusion](https://arxiv.org/abs/2103.07074v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ShiQiu0419/BAAF-Net)",
      "n": "BAAF-Net",
      "d": "2021-03-12",
      "m1": "59.9%"
    },
    {
      "p": "[SalsaNext: Fast, Uncertainty-aware Semantic Segmentation of LiDAR Point Clouds for Autonomous Driving](https://arxiv.org/abs/2003.03653v4)",
      "c": "[&check;&nbsp;Link](https://github.com/TiagoCortinhal/SalsaNext)",
      "n": "SalsaNext",
      "d": "2020-03-07",
      "m1": "59.5%"
    },
    {
      "p": "[KPConv: Flexible and Deformable Convolution for Point Clouds](https://arxiv.org/abs/1904.08889v2)",
      "c": "[&check;&nbsp;Link](https://github.com/isl-org/Open3D-ML)",
      "n": "KPConv",
      "d": "2019-04-18",
      "m1": "58.8%"
    },
    {
      "p": "[PolarNet: An Improved Grid Representation for Online LiDAR Point Clouds Semantic Segmentation](https://arxiv.org/abs/2003.14032v2)",
      "c": "[&check;&nbsp;Link](https://github.com/edwardzhou130/PolarSeg)",
      "n": "PolarNet",
      "d": "2020-03-31",
      "m1": "57.2%"
    },
    {
      "p": "[FPS-Net: A Convolutional Fusion Network for Large-Scale LiDAR Point Cloud Segmentation](https://arxiv.org/abs/2103.00738v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xiaoaoran/FPS-Net)",
      "n": "FPS-Net",
      "d": "2021-03-01",
      "m1": "57.1%"
    },
    {
      "p": "[SqueezeSegV3: Spatially-Adaptive Convolution for Efficient Point-Cloud Segmentation](https://arxiv.org/abs/2004.01803v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/Paddle3D)",
      "n": "SqueezeSegV3",
      "d": "2020-04-03",
      "m1": "55.9%"
    },
    {
      "p": "[3D-MiniNet: Learning a 2D Representation from Point Clouds for Fast and Efficient 3D LIDAR Semantic Segmentation](https://arxiv.org/abs/2002.10893v5)",
      "c": "[&check;&nbsp;Link](https://github.com/Shathe/3D-MiniNet)",
      "n": "3D-MiniNet",
      "d": "2020-02-25",
      "m1": "55.8%"
    },
    {
      "p": "[Multi Projection Fusion for Real-time Semantic Segmentation of 3D LiDAR Point Clouds](https://arxiv.org/abs/2011.01974v2)",
      "c": "",
      "n": "MPF",
      "d": "2020-11-03",
      "m1": "55.5%"
    },
    {
      "p": "[Multi-scale Interaction for Real-time LiDAR Data Segmentation on an Embedded Platform](https://arxiv.org/abs/2008.09162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PRBonn/LiDAR-MOS)",
      "n": "MINet",
      "d": "2020-08-20",
      "m1": "55.2%"
    },
    {
      "p": "[RandLA-Net: Efficient Semantic Segmentation of Large-Scale Point Clouds](https://arxiv.org/abs/1911.11236v3)",
      "c": "[&check;&nbsp;Link](https://github.com/intel-isl/Open3D-ML)",
      "n": "RandLA-Net",
      "d": "2019-11-25",
      "m1": "53.9%"
    },
    {
      "p": "[FG-Net: Fast Large-Scale LiDAR Point Clouds Understanding Network Leveraging Correlated Feature Mining and Geometric-Aware Modelling](https://arxiv.org/abs/2012.09439v2)",
      "c": "[&check;&nbsp;Link](https://github.com/KangchengLiu/Feature-Geometric-Net-FG-Net)",
      "n": "FG-Net",
      "d": "2020-12-17",
      "m1": "53.8%"
    },
    {
      "p": "[LatticeNet: Fast Point Cloud Segmentation Using Permutohedral Lattices](https://arxiv.org/abs/1912.05905v3)",
      "c": "[&check;&nbsp;Link](https://github.com/AIS-Bonn/lattice_net)",
      "n": "LatticeNet",
      "d": "2019-12-12",
      "m1": "52.9%"
    },
    {
      "p": "[RangeNet++: Fast and Accurate LiDAR Semantic Segmentation](http://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/milioto2019iros.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/PRBonn/lidar-bonnetal)",
      "n": "RangeNet++",
      "d": "2019-11-04",
      "m1": "52.2%"
    },
    {
      "p": "[SemanticKITTI: A Dataset for Semantic Scene Understanding of LiDAR Sequences](https://arxiv.org/abs/1904.01416v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PRBonn/semantic-kitti-api)",
      "n": "Darknet53",
      "d": "2019-04-02",
      "m1": "49.9%"
    },
    {
      "p": "[SqueezeSegV2: Improved Model Structure and Unsupervised Domain Adaptation for Road-Object Segmentation from a LiDAR Point Cloud](http://arxiv.org/abs/1809.08495v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xuanyuzhou98/SqueezeSegV2)",
      "n": "SqueezeSegV2",
      "d": "2018-09-22",
      "m1": "39.7%"
    },
    {
      "p": "[Tangent Convolutions for Dense Prediction in 3D](http://arxiv.org/abs/1807.02443v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tatarchm/tangent_conv)",
      "n": "TangentConv",
      "d": "2018-07-06",
      "m1": "35.9%"
    },
    {
      "p": "[SqueezeSeg: Convolutional Neural Nets with Recurrent CRF for Real-Time Road-Object Segmentation from 3D LiDAR Point Cloud](http://arxiv.org/abs/1710.07368v1)",
      "c": "[&check;&nbsp;Link](https://github.com/BichenWuUCB/SqueezeSeg)",
      "n": "SqueezeSeg",
      "d": "2017-10-19",
      "m1": "29.5%"
    },
    {
      "p": "[PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space](http://arxiv.org/abs/1706.02413v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yanx27/Pointnet_Pointnet2_pytorch)",
      "n": "PointNet++",
      "d": "2017-06-07",
      "m1": "20.1%"
    },
    {
      "p": "[SPLATNet: Sparse Lattice Networks for Point Cloud Processing](http://arxiv.org/abs/1802.08275v4)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/splatnet)",
      "n": "SPLATNet",
      "d": "2018-02-22",
      "m1": "18.4%"
    },
    {
      "p": "[Large-scale Point Cloud Semantic Segmentation with Superpoint Graphs](http://arxiv.org/abs/1711.09869v2)",
      "c": "[&check;&nbsp;Link](https://github.com/loicland/superpoint_graph)",
      "n": "SPGraph",
      "d": "2017-11-27",
      "m1": "17.4%"
    },
    {
      "p": "[PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation](http://arxiv.org/abs/1612.00593v2)",
      "c": "[&check;&nbsp;Link](https://github.com/charlesq34/pointnet)",
      "n": "PointNet",
      "d": "2016-12-02",
      "m1": "14.6%"
    },
    {
      "p": "[Towards Large-scale 3D Representation Learning with Multi-dataset Point Prompt Training](https://arxiv.org/abs/2308.09718v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Pointcept/Pointcept)",
      "n": "PPT+SparseUNet",
      "d": "2023-08-18",
      "m2": "71.4%"
    },
    {
      "p": "[OA-CNNs: Omni-Adaptive Sparse CNNs for 3D Semantic Segmentation](https://arxiv.org/abs/2403.14418v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Pointcept/Pointcept)",
      "n": "OA-CNNs",
      "d": "2024-03-21",
      "m2": "70.6%"
    },
    {
      "p": "[Less is More: Reducing Task and Model Complexity for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2303.11203v2)",
      "c": "[&check;&nbsp;Link](https://github.com/l1997i/lim3d)",
      "n": "LiM3D",
      "d": "2023-03-20",
      "m3": "58.4"
    },
    {
      "p": "[Less is More: Reducing Task and Model Complexity for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2303.11203v2)",
      "c": "[&check;&nbsp;Link](https://github.com/l1997i/lim3d)",
      "n": "LiM3D+SDSC",
      "d": "2023-03-20",
      "m3": "57.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
