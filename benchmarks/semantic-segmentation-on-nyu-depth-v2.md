# semantic-segmentation-on-nyu-depth-v2

[Dataset Link](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) \
Task Hierarchy: ['10-shot image generation', 'Semantic Segmentation']

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
      "label": "Mean IoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Mean Accuracy",
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
      "p": "[OmniVec2 - A Novel Transformer based Network for Large Scale Multimodal and Multitask Learning](http://openaccess.thecvf.com//content/CVPR2024/html/Srivastava_OmniVec2_-_A_Novel_Transformer_based_Network_for_Large_Scale_CVPR_2024_paper.html)",
      "c": "",
      "n": "OmniVec2",
      "d": "2024-01-01",
      "m1": "63.6"
    },
    {
      "p": "[Diffusion-based RGB-D Semantic Segmentation with Deformable Attention Transformer](https://arxiv.org/abs/2409.15117v2)",
      "c": "",
      "n": "DiffusionMMS (DAT++-S)",
      "d": "2024-09-23",
      "m1": "61.5"
    },
    {
      "p": "[DepthMatch: Semi-Supervised RGB-D Scene Parsing through Depth-Guided Regularization](https://arxiv.org/abs/2505.20041v1)",
      "c": "",
      "n": "DepthMatch (DINOv2-S)",
      "d": "2025-05-26",
      "m1": "61.4"
    },
    {
      "p": "[GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer](https://arxiv.org/abs/2406.01210v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiadingcn/geminifusion)",
      "n": "GeminiFusion (Swin-Large)",
      "d": "2024-06-03",
      "m1": "60.9"
    },
    {
      "p": "[OmniVec: Learning robust representations with cross modal sharing](https://arxiv.org/abs/2311.05709v1)",
      "c": "",
      "n": "OmniVec",
      "d": "2023-11-07",
      "m1": "60.8"
    },
    {
      "p": "[GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer](https://arxiv.org/abs/2406.01210v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiadingcn/geminifusion)",
      "n": "GeminiFusion (Swin-Large)",
      "d": "2024-06-03",
      "m1": "60.2"
    },
    {
      "p": "[Efficient Multimodal Semantic Segmentation via Dual-Prompt Learning](https://arxiv.org/abs/2312.00360v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shaohuadong2021/dplnet)",
      "n": "DPLNet",
      "d": "2023-12-01",
      "m1": "59.3"
    },
    {
      "p": "[HDBFormer: Efficient RGB-D Semantic Segmentation with A Heterogeneous Dual-Branch Framework](https://arxiv.org/abs/2504.13579v1)",
      "c": "[&check;&nbsp;Link](https://github.com/weishuobin/hdbformer)",
      "n": "HDBFormer",
      "d": "2025-04-18",
      "m1": "59.3%"
    },
    {
      "p": "[PanopticNDT: Efficient and Robust Panoptic Mapping](https://arxiv.org/abs/2309.13635v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tui-nicr/emsanet)",
      "n": "EMSANet (2x ResNet-34 NBt1D, PanopticNDT version, finetuned)",
      "d": "2023-09-24",
      "m1": "59.02"
    },
    {
      "p": "[DFormerv2: Geometry Self-Attention for RGBD Semantic Segmentation](https://arxiv.org/abs/2504.04701v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormerv2-L",
      "d": "2025-04-07",
      "m1": "58.4%"
    },
    {
      "p": "[SwinMTL: A Shared Architecture for Simultaneous Depth Estimation and Semantic Segmentation from Monocular Camera Images](https://arxiv.org/abs/2403.10662v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pardistaghavi/swinmtl)",
      "n": "SwinMTL",
      "d": "2024-03-15",
      "m1": "58.14%"
    },
    {
      "p": "[PolyMaX: General Dense Prediction with Mask Transformer](https://arxiv.org/abs/2311.05770v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "PolyMaX(ConvNeXt-L)",
      "d": "2023-11-09",
      "m1": "58.08%"
    },
    {
      "p": "[HSPFormer: Hierarchical Spatial Perception Transformer for Semantic Segmentation](https://doi.org/10.1109/TITS.2025.3525542)",
      "c": "[&check;&nbsp;Link](https://github.com/SY-Ch/HSPFormer)",
      "n": "HSPFormer(PVT v2-B4)",
      "d": "2025-01-16",
      "m1": "57.8%"
    },
    {
      "p": "[GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer](https://arxiv.org/abs/2406.01210v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiadingcn/geminifusion)",
      "n": "GeminiFusion (MiT-B5)",
      "d": "2024-06-03",
      "m1": "57.7"
    },
    {
      "p": "[DFormerv2: Geometry Self-Attention for RGBD Semantic Segmentation](https://arxiv.org/abs/2504.04701v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormerv2-B",
      "d": "2025-04-07",
      "m1": "57.7%"
    },
    {
      "p": "[DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation](https://arxiv.org/abs/2309.09668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormer-L",
      "d": "2023-09-18",
      "m1": "57.2%"
    },
    {
      "p": "[CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers](https://arxiv.org/abs/2203.04838v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huaaaliu/rgbx_semantic_segmentation)",
      "n": "CMX (B5)",
      "d": "2022-03-09",
      "m1": "56.9%"
    },
    {
      "p": "[Delivering Arbitrary-Modal Semantic Segmentation](https://arxiv.org/abs/2303.01480v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jamycheung/DELIVER)",
      "n": "CMNeXt (B4)",
      "d": "2023-03-02",
      "m1": "56.9%"
    },
    {
      "p": "[Omnivore: A Single Model for Many Visual Modalities](https://arxiv.org/abs/2201.08377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/towhee-io/towhee)",
      "n": "OMNIVORE (Swin-L, finetuned)",
      "d": "2022-01-20",
      "m1": "56.8%"
    },
    {
      "p": "[GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer](https://arxiv.org/abs/2406.01210v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiadingcn/geminifusion)",
      "n": "GeminiFusion (MiT-B3)",
      "d": "2024-06-03",
      "m1": "56.8"
    },
    {
      "p": "[CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers](https://arxiv.org/abs/2203.04838v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huaaaliu/rgbx_semantic_segmentation)",
      "n": "CMX (B4)",
      "d": "2022-03-09",
      "m1": "56.3%"
    },
    {
      "p": "[MultiMAE: Multi-modal Multi-task Masked Autoencoders](https://arxiv.org/abs/2204.01678v1)",
      "c": "[&check;&nbsp;Link](https://github.com/EPFL-VILAB/MultiMAE)",
      "n": "MultiMAE (ViT-B)",
      "d": "2022-04-04",
      "m1": "56.0%"
    },
    {
      "p": "[DFormerv2: Geometry Self-Attention for RGBD Semantic Segmentation](https://arxiv.org/abs/2504.04701v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormerv2-S",
      "d": "2025-04-07",
      "m1": "56.0%"
    },
    {
      "p": "[Understanding Dark Scenes by Contrasting Multi-Modal Observations](https://arxiv.org/abs/2308.12320v2)",
      "c": "[&check;&nbsp;Link](https://github.com/palmdong/smmcl)",
      "n": "SMMCL (SegNeXt-B)",
      "d": "2023-08-23",
      "m1": "55.8%"
    },
    {
      "p": "[DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation](https://arxiv.org/abs/2309.09668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormer-B",
      "d": "2023-09-18",
      "m1": "55.6%"
    },
    {
      "p": "[ComPtr: Towards Diverse Bi-source Dense Prediction Tasks via A Simple yet General Complementary Transformer](https://arxiv.org/abs/2307.12349v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lartpang/comptr)",
      "n": "ComPtr (Swin-B)",
      "d": "2023-07-23",
      "m1": "55.5%"
    },
    {
      "p": "[AsymFormer: Asymmetrical Cross-Modal Representation Learning for Mobile Platform Real-Time RGB-D Semantic Segmentation](https://arxiv.org/abs/2309.14065v7)",
      "c": "[&check;&nbsp;Link](https://github.com/Fourier7754/AsymFormer)",
      "n": "AsymFormer",
      "d": "2023-09-25",
      "m1": "55.3%"
    },
    {
      "p": "[Omnivore: A Single Model for Many Visual Modalities](https://arxiv.org/abs/2201.08377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/towhee-io/towhee)",
      "n": "OMNIVORE (Swin-B, finetuned)",
      "d": "2022-01-20",
      "m1": "55.1%"
    },
    {
      "p": "[HAPNet: Toward Superior RGB-Thermal Scene Parsing via Hybrid, Asymmetric, and Progressive Heterogeneous Feature Fusion](https://arxiv.org/abs/2404.03527v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LiJiahang617/HAPNet)",
      "n": "HAPNet",
      "d": "2024-04-04",
      "m1": "55.0",
      "m2": "68.8"
    },
    {
      "p": "[CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers](https://arxiv.org/abs/2203.04838v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huaaaliu/rgbx_semantic_segmentation)",
      "n": "CMX (B2)",
      "d": "2022-03-09",
      "m1": "54.4%"
    },
    {
      "p": "[Multimodal Token Fusion for Vision Transformers](https://arxiv.org/abs/2204.08721v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huawei-noah/noah-research/tree/master/TokenFusion)",
      "n": "TokenFusion (S)",
      "d": "2022-04-19",
      "m1": "54.2%"
    },
    {
      "p": "[Understanding Dark Scenes by Contrasting Multi-Modal Observations](https://arxiv.org/abs/2308.12320v2)",
      "c": "[&check;&nbsp;Link](https://github.com/palmdong/smmcl)",
      "n": "SMMCL (SegFormer-B2)",
      "d": "2023-08-23",
      "m1": "53.7%"
    },
    {
      "p": "[DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation](https://arxiv.org/abs/2309.09668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormer-S",
      "d": "2023-09-18",
      "m1": "53.6%"
    },
    {
      "p": "[InvPT: Inverted Pyramid Multi-task Transformer for Dense Scene Understanding](https://arxiv.org/abs/2203.07997v3)",
      "c": "[&check;&nbsp;Link](https://github.com/prismformore/InvPT)",
      "n": "InvPT",
      "d": "2022-03-15",
      "m1": "53.56%"
    },
    {
      "p": "[HS3: Learning with Proper Task Complexity in Hierarchically Supervised Semantic Segmentation](https://arxiv.org/abs/2111.02333v1)",
      "c": "",
      "n": "HS3-Fuse (ResNet-101)",
      "d": "2021-11-03",
      "m1": "53.5%"
    },
    {
      "p": "[Pixel Difference Convolutional Network for RGB-D Semantic Segmentation](https://arxiv.org/abs/2302.11951v1)",
      "c": "",
      "n": "PDCNet (ResNet-101)",
      "d": "2023-02-23",
      "m1": "53.5%"
    },
    {
      "p": "[Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments](https://arxiv.org/abs/2207.04526v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tui-nicr/emsanet)",
      "n": "EMSANet (2x ResNet-34 NBt1D, finetuned)",
      "d": "2022-07-10",
      "m1": "53.34%"
    },
    {
      "p": "[DCANet: Differential Convolution Attention Network for RGB-D Semantic Segmentation](https://arxiv.org/abs/2210.06747v1)",
      "c": "",
      "n": "DCANet (ResNet-101)",
      "d": "2022-10-13",
      "m1": "53.3%"
    },
    {
      "p": "[Multimodal Token Fusion for Vision Transformers](https://arxiv.org/abs/2204.08721v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huawei-noah/noah-research/tree/master/TokenFusion)",
      "n": "TokenFusion (Ti)",
      "d": "2022-04-19",
      "m1": "53.3%"
    },
    {
      "p": "[InverseForm: A Loss Function for Structured Boundary-Aware Segmentation](https://arxiv.org/abs/2104.02745v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Qualcomm-AI-research/InverseForm)",
      "n": "InverseForm (ResNet-101)",
      "d": "2021-04-06",
      "m1": "53.1%"
    },
    {
      "p": "[Context-Aware Interaction Network for RGB-T Semantic Segmentation](https://arxiv.org/abs/2401.01624v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yinglv1106/cainet)",
      "n": "CAINet (MobileNet-V2)",
      "d": "2024-01-03",
      "m1": "52.6%"
    },
    {
      "p": "[Channel Exchanging Networks for Multimodal and Multitask Dense Image Prediction](https://arxiv.org/abs/2112.02252v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yikaiw/CEN)",
      "n": "CEN-PSPNet (ResNet-152)",
      "d": "2021-12-04",
      "m1": "52.5%"
    },
    {
      "p": "[Attention-based Dual Supervised Decoder for RGBD Semantic Segmentation](https://arxiv.org/abs/2201.01427v2)",
      "c": "",
      "n": "AMF (ResNet-50)",
      "d": "2022-01-05",
      "m1": "52.5%"
    },
    {
      "p": "[Understanding Dark Scenes by Contrasting Multi-Modal Observations](https://arxiv.org/abs/2308.12320v2)",
      "c": "[&check;&nbsp;Link](https://github.com/palmdong/smmcl)",
      "n": "SMMCL (ResNet-101)",
      "d": "2023-08-23",
      "m1": "52.5%"
    },
    {
      "p": "[Bi-directional Cross-Modality Feature Propagation with Separation-and-Aggregation Gate for RGB-D Semantic Segmentation](https://arxiv.org/abs/2007.09183v1)",
      "c": "[&check;&nbsp;Link](https://github.com/charlesCXK/RGBD_Semantic_Segmentation_PyTorch)",
      "n": "SA-Gate",
      "d": "2020-07-17",
      "m1": "52.4%"
    },
    {
      "p": "[Warp-Refine Propagation: Semi-Supervised Auto-labeling via Cycle-consistency](https://arxiv.org/abs/2109.13432v1)",
      "c": "",
      "n": "Warp-Refine",
      "d": "2021-09-28",
      "m1": "52.2%"
    },
    {
      "p": "[Deep feature selection-and-fusion for RGB-D semantic segmentation](https://arxiv.org/abs/2105.04102v1)",
      "c": "",
      "n": "FSFNet",
      "d": "2021-05-10",
      "m1": "52.0%"
    },
    {
      "p": "[Variational Context-Deformable ConvNets for Indoor Scene Parsing](http://openaccess.thecvf.com/content_CVPR_2020/html/Xiong_Variational_Context-Deformable_ConvNets_for_Indoor_Scene_Parsing_CVPR_2020_paper.html)",
      "c": "",
      "n": "VCD+ACNet (ResNet-50)",
      "d": "2020-06-01",
      "m1": "51.9%"
    },
    {
      "p": "[Optimizing rgb-d semantic segmentation through multi-modal interaction and pooling attention](https://arxiv.org/abs/2311.11312v2)",
      "c": "",
      "n": "MIPANet (ResNet50)",
      "d": "2023-11-19",
      "m1": "51.9%"
    },
    {
      "p": "[DFormer: Rethinking RGBD Representation Learning for Semantic Segmentation](https://arxiv.org/abs/2309.09668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VCIP-RGBD/DFormer)",
      "n": "DFormer-T",
      "d": "2023-09-18",
      "m1": "51.8%"
    },
    {
      "p": "[ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation](https://arxiv.org/abs/2108.10528v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hanchaoleng/shapeconv)",
      "n": "ShapeConv (ResNext-101)",
      "d": "2021-08-24",
      "m1": "51.3%"
    },
    {
      "p": "[Efficient Multi-Task Scene Analysis with RGB-D Transformers](https://arxiv.org/abs/2306.05242v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tui-nicr/nicr-scene-analysis-datasets)",
      "n": "EMSAFormer (SwinV2-T-128-Multi-Aug)",
      "d": "2023-06-08",
      "m1": "51.26%"
    },
    {
      "p": "[Depth-Adapted CNNs for RGB-D Semantic Segmentation](https://arxiv.org/abs/2206.03939v1)",
      "c": "",
      "n": "Z-ACN (ResNet-101)",
      "d": "2022-06-08",
      "m1": "51.24%"
    },
    {
      "p": "[Learning Deep Multimodal Feature Representation with Asymmetric Multi-layer Fusion](https://arxiv.org/abs/2108.05009v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yikaiw/AsymFusion)",
      "n": "AsymFusion (ResNet-152)",
      "d": "2021-08-11",
      "m1": "51.2%"
    },
    {
      "p": "[Dynamic Multimodal Fusion](https://arxiv.org/abs/2204.00102v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zihuixue/dynmm)",
      "n": "DynMM (ResNet-50)",
      "d": "2022-03-31",
      "m1": "51.0%"
    },
    {
      "p": "[Spatial Information Guided Convolution for Real-Time RGBD Semantic Segmentation](https://arxiv.org/abs/2004.04534v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LinZhuoChen/SGNet)",
      "n": "SGNet (ResNet-101)",
      "d": "2020-04-09",
      "m1": "51.0%"
    },
    {
      "p": "[Pattern-Structure Diffusion for Multi-Task Learning](http://openaccess.thecvf.com/content_CVPR_2020/html/Zhou_Pattern-Structure_Diffusion_for_Multi-Task_Learning_CVPR_2020_paper.html)",
      "c": "",
      "n": "PSD-ResNet50",
      "d": "2020-06-01",
      "m1": "51.0%"
    },
    {
      "p": "[Malleable 2.5D Convolution: Learning Receptive Fields along the Depth-axis for RGB-D Scene Parsing](https://arxiv.org/abs/2007.09365v1)",
      "c": "[&check;&nbsp;Link](https://github.com/charlesCXK/RGBD_Semantic_Segmentation_PyTorch)",
      "n": "Malleable 2.5D (ResNet-101)",
      "d": "2020-07-18",
      "m1": "50.9%"
    },
    {
      "p": "[Scene Parsing via Integrated Classification Model and Variance-Based Regularization](http://openaccess.thecvf.com/content_CVPR_2019/html/Shi_Scene_Parsing_via_Integrated_Classification_Model_and_Variance-Based_Regularization_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/shihengcan/ICM-matcaffe)",
      "n": "ICM",
      "d": "2019-06-01",
      "m1": "50.70"
    },
    {
      "p": "[Multi-layer Feature Aggregation for Deep Scene Parsing Models](https://arxiv.org/abs/2011.02572v1)",
      "c": "",
      "n": "SANet",
      "d": "2020-11-04",
      "m1": "50.7%"
    },
    {
      "p": "[Variational Context-Deformable ConvNets for Indoor Scene Parsing](http://openaccess.thecvf.com/content_CVPR_2020/html/Xiong_Variational_Context-Deformable_ConvNets_for_Indoor_Scene_Parsing_CVPR_2020_paper.html)",
      "c": "",
      "n": "VCD+RedNet (ResNet-50)",
      "d": "2020-06-01",
      "m1": "50.7%"
    },
    {
      "p": "[HaarNet: Large-scale Linear-Morphological Hybrid Network for RGB-D Semantic Segmentation](https://arxiv.org/abs/2310.07669v1)",
      "c": "",
      "n": "HaarNet",
      "d": "2023-10-11",
      "m1": "50.7%"
    },
    {
      "p": "[Pattern-Affinitive Propagation across Depth, Surface Normal and Semantic Segmentation](https://arxiv.org/abs/1906.03525v1)",
      "c": "",
      "n": "PAP (ResNet-50)",
      "d": "2019-06-08",
      "m1": "50.4%"
    },
    {
      "p": "[Cerberus Transformer: Joint Semantic, Affordance and Attribute Parsing](https://arxiv.org/abs/2111.12608v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-air-sun/cerberus)",
      "n": "Cerberus",
      "d": "2021-11-24",
      "m1": "50.4%"
    },
    {
      "p": "[Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis](https://arxiv.org/abs/2011.06961v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUI-NICR/ESANet)",
      "n": "ESANet (R34-NBt1D)",
      "d": "2020-11-13",
      "m1": "50.30"
    },
    {
      "p": "[Depth-Adapted CNNs for RGB-D Semantic Segmentation](https://arxiv.org/abs/2206.03939v1)",
      "c": "",
      "n": "Z-ACN (ResNet-50)",
      "d": "2022-06-08",
      "m1": "50.05%"
    },
    {
      "p": "[Malleable 2.5D Convolution: Learning Receptive Fields along the Depth-axis for RGB-D Scene Parsing](https://arxiv.org/abs/2007.09365v1)",
      "c": "[&check;&nbsp;Link](https://github.com/charlesCXK/RGBD_Semantic_Segmentation_PyTorch)",
      "n": "Malleable 2.5D (ResNet-50)",
      "d": "2020-07-18",
      "m1": "49.7%"
    },
    {
      "p": "[MMANet: Margin-aware Distillation and Modality-aware Regularization for Incomplete Multimodal Learning](https://arxiv.org/abs/2304.08028v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shicaiwei123/mmanet)",
      "n": "MMANet",
      "d": "2023-04-17",
      "m1": "49.62%"
    },
    {
      "p": "[Spatial-information Guided Adaptive Context-aware Network for Efficient RGB-D Semantic Segmentation](https://arxiv.org/abs/2308.06024v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mvme-hbut/sgacnet)",
      "n": "SGACNet (R34-NBt1D)",
      "d": "2023-08-11",
      "m1": "49.4%"
    },
    {
      "p": "[ComPtr: Towards Diverse Bi-source Dense Prediction Tasks via A Simple yet General Complementary Transformer](https://arxiv.org/abs/2307.12349v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lartpang/comptr)",
      "n": "ComPtr (Swin-T)",
      "d": "2023-07-23",
      "m1": "49.2%"
    },
    {
      "p": "[Depth-Adapted CNNs for RGB-D Semantic Segmentation](https://arxiv.org/abs/2206.03939v1)",
      "c": "",
      "n": "Z-ACN (ResNet-34)",
      "d": "2022-06-08",
      "m1": "49.15%"
    },
    {
      "p": "[Improving Multi-Modal Learning with Uni-Modal Teachers](https://arxiv.org/abs/2106.11059v1)",
      "c": "",
      "n": "UMT",
      "d": "2021-06-21",
      "m1": "49.14%"
    },
    {
      "p": "[MTI-Net: Multi-Scale Task Interaction Networks for Multi-Task Learning](https://arxiv.org/abs/2001.06902v5)",
      "c": "[&check;&nbsp;Link](https://github.com/SimonVandenhende/Multi-Task-Learning-PyTorch)",
      "n": "MTI-Net (HRNet-48)",
      "d": "2020-01-19",
      "m1": "49.0"
    },
    {
      "p": "[ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation](https://arxiv.org/abs/2108.10528v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hanchaoleng/shapeconv)",
      "n": "ShapeConv (ResNet-101)",
      "d": "2021-08-24",
      "m1": "49.0%"
    },
    {
      "p": "[Multimodal Knowledge Expansion](https://arxiv.org/abs/2103.14431v3)",
      "c": "[&check;&nbsp;Link](https://github.com/zihuixue/mke)",
      "n": "MKE",
      "d": "2021-03-26",
      "m1": "48.88%"
    },
    {
      "p": "[ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation](https://arxiv.org/abs/2108.10528v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hanchaoleng/shapeconv)",
      "n": "ShapeConv (ResNet-50)",
      "d": "2021-08-24",
      "m1": "48.8%"
    },
    {
      "p": "[mmFormer: Multimodal Medical Transformer for Incomplete Multimodal Learning of Brain Tumor Segmentation](https://arxiv.org/abs/2206.02425v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yaozhang93/mmformer)",
      "n": "mmFormer",
      "d": "2022-06-06",
      "m1": "48.45%"
    },
    {
      "p": "[ACNet: Attention Based Network to Exploit Complementary Features for RGBD Semantic Segmentation](https://arxiv.org/abs/1905.10089v1)",
      "c": "[&check;&nbsp;Link](https://github.com/anheidelonghu/ACNet)",
      "n": "ACNet",
      "d": "2019-05-24",
      "m1": "48.3%"
    },
    {
      "p": "[Spatial-information Guided Adaptive Context-aware Network for Efficient RGB-D Semantic Segmentation](https://arxiv.org/abs/2308.06024v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mvme-hbut/sgacnet)",
      "n": "SGACNet (R18-NBt1D)",
      "d": "2023-08-11",
      "m1": "48.2%"
    },
    {
      "p": "[Efficient RGB-D Semantic Segmentation for Indoor Scene Analysis](https://arxiv.org/abs/2011.06961v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUI-NICR/ESANet)",
      "n": "ESANet (R18-NBt1D )",
      "d": "2020-11-13",
      "m1": "48.17"
    },
    {
      "p": "[RFNet: Region-Aware Fusion Network for Incomplete Multi-Modal Brain Tumor Segmentation](http://openaccess.thecvf.com//content/ICCV2021/html/Ding_RFNet_Region-Aware_Fusion_Network_for_Incomplete_Multi-Modal_Brain_Tumor_Segmentation_ICCV_2021_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/dyh127/RFNet)",
      "n": "RFNet",
      "d": "2021-01-01",
      "m1": "48.13%"
    },
    {
      "p": "[Contrastive Multimodal Fusion with TupleInfoNCE](https://arxiv.org/abs/2107.02575v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hoi4d/TupleInfoNCE)",
      "n": "TupleInfoNCE",
      "d": "2021-07-06",
      "m1": "48.1%"
    },
    {
      "p": "[Dense Decoder Shortcut Connections for Single-Pass Semantic Segmentation](http://openaccess.thecvf.com/content_cvpr_2018/html/Bilinski_Dense_Decoder_Shortcut_CVPR_2018_paper.html)",
      "c": "",
      "n": "DDSC (ResNet-101)",
      "d": "2018-06-01",
      "m1": "48.1%"
    },
    {
      "p": "[Cascaded Feature Network for Semantic Segmentation of RGB-D Images](http://openaccess.thecvf.com/content_iccv_2017/html/Lin_Cascaded_Feature_Network_ICCV_2017_paper.html)",
      "c": "",
      "n": "CFN",
      "d": "2017-10-01",
      "m1": "47.7%"
    },
    {
      "p": "[Learning Fully Dense Neural Networks for Image Semantic Segmentation](https://arxiv.org/abs/1905.08929v1)",
      "c": "",
      "n": "FDNet (DenseNet264)",
      "d": "2019-05-22",
      "m1": "47.4%"
    },
    {
      "p": "[RedNet: Residual Encoder-Decoder Network for indoor RGB-D Semantic Segmentation](http://arxiv.org/abs/1806.01054v2)",
      "c": "[&check;&nbsp;Link](https://github.com/JindongJiang/RedNet)",
      "n": "RedNet",
      "d": "2018-06-04",
      "m1": "47.2%"
    },
    {
      "p": "[Depth-Adapted CNNs for RGB-D Semantic Segmentation](https://arxiv.org/abs/2206.03939v1)",
      "c": "",
      "n": "Z-ACN (ResNet-18)",
      "d": "2022-06-08",
      "m1": "47.02%"
    },
    {
      "p": "[Joint Task-Recursive Learning for Semantic Segmentation and Depth Estimation](http://openaccess.thecvf.com/content_ECCV_2018/html/Zhenyu_Zhang_Joint_Task-Recursive_Learning_ECCV_2018_paper.html)",
      "c": "",
      "n": "TRL (ResNet-101)",
      "d": "2018-09-01",
      "m1": "46.8%"
    },
    {
      "p": "[RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation](http://arxiv.org/abs/1611.06612v3)",
      "c": "[&check;&nbsp;Link](https://github.com/guosheng/refinenet)",
      "n": "RefineNet (ResNet-101)",
      "d": "2016-11-20",
      "m1": "46.5%"
    },
    {
      "p": "[Prompt Guided Transformer for Multi-Task Dense Prediction](https://arxiv.org/abs/2307.15362v1)",
      "c": "[&check;&nbsp;Link](https://github.com/innovator-zero/MTDP_Lib)",
      "n": "PGT (Swin-S)",
      "d": "2023-07-28",
      "m1": "46.43"
    },
    {
      "p": "[Exploring Relational Context for Multi-Task Dense Prediction](https://arxiv.org/abs/2104.13874v2)",
      "c": "[&check;&nbsp;Link](https://github.com/brdav/atrc)",
      "n": "ATRC",
      "d": "2021-04-28",
      "m1": "46.33%"
    },
    {
      "p": "[Locality-Sensitive Deconvolution Networks With Gated Fusion for RGB-D Indoor Semantic Segmentation](http://openaccess.thecvf.com/content_cvpr_2017/html/Cheng_Locality-Sensitive_Deconvolution_Networks_CVPR_2017_paper.html)",
      "c": "",
      "n": "LS-DeconvNet",
      "d": "2017-07-01",
      "m1": "45.9%"
    },
    {
      "p": "[Variational Context-Deformable ConvNets for Indoor Scene Parsing](http://openaccess.thecvf.com/content_CVPR_2020/html/Xiong_Variational_Context-Deformable_ConvNets_for_Indoor_Scene_Parsing_CVPR_2020_paper.html)",
      "c": "",
      "n": "VCD+DeepLab (VGG16)",
      "d": "2020-06-01",
      "m1": "45.3"
    },
    {
      "p": "[SOSD-Net: Joint Semantic Object Segmentation and Depth Estimation from Monocular images](https://arxiv.org/abs/2101.07422v1)",
      "c": "",
      "n": "SOSD-Net",
      "d": "2021-01-19",
      "m1": "45.0%"
    },
    {
      "p": "[Multi-Modal Attention-based Fusion Model for Semantic Segmentation of RGB-Depth Images](https://arxiv.org/abs/1912.11691v1)",
      "c": "",
      "n": "MMAF-Net-152",
      "d": "2019-12-25",
      "m1": "44.8%"
    },
    {
      "p": "[Recurrent Scene Parsing with Perspective Understanding in the Loop](http://arxiv.org/abs/1705.07238v2)",
      "c": "[&check;&nbsp;Link](https://github.com/aimerykong/Recurrent-Scene-Parsing-with-Perspective-Understanding-in-the-loop)",
      "n": "RecurrentSceneParsing",
      "d": "2017-05-20",
      "m1": "44.5%"
    },
    {
      "p": "[Light-Weight RefineNet for Real-Time Semantic Segmentation](http://arxiv.org/abs/1810.03272v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DrSleep/light-weight-refinenet)",
      "n": "Light-Weight-RefineNet-152",
      "d": "2018-10-08",
      "m1": "44.4%"
    },
    {
      "p": "[Depth-aware CNN for RGB-D Segmentation](http://arxiv.org/abs/1803.06791v1)",
      "c": "[&check;&nbsp;Link](https://github.com/laughtervv/DepthAwareCNN)",
      "n": "Depth-aware CNN",
      "d": "2018-03-19",
      "m1": "43.9%"
    },
    {
      "p": "[Light-Weight RefineNet for Real-Time Semantic Segmentation](http://arxiv.org/abs/1810.03272v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DrSleep/light-weight-refinenet)",
      "n": "Light-Weight-RefineNet-101",
      "d": "2018-10-08",
      "m1": "43.6%"
    },
    {
      "p": "[Temporally Distributed Networks for Fast Video Semantic Segmentation](https://arxiv.org/abs/2004.01800v2)",
      "c": "[&check;&nbsp;Link](https://github.com/feinanshan/TDNet)",
      "n": "TD2-PSP50",
      "d": "2020-04-03",
      "m1": "43.5"
    },
    {
      "p": "[NDDR-CNN: Layerwise Feature Fusing in Multi-Task CNNs by Neural Discriminative Dimensionality Reduction](http://arxiv.org/abs/1801.08297v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ethanygao/NDDR-CNN)",
      "n": "NDDR-CNN",
      "d": "2018-01-25",
      "m1": "43.3%"
    },
    {
      "p": "[3D Graph Neural Networks for RGBD Semantic Segmentation](http://openaccess.thecvf.com/content_iccv_2017/html/Qi_3D_Graph_Neural_ICCV_2017_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/yanx27/3DGNN_pytorch)",
      "n": "3DGNN",
      "d": "2017-10-01",
      "m1": "43.1%"
    },
    {
      "p": "[CI-Net: Contextual Information for Joint Semantic Segmentation and Depth Estimation](https://arxiv.org/abs/2107.13800v2)",
      "c": "",
      "n": "CI-Net",
      "d": "2021-07-29",
      "m1": "42.6%"
    },
    {
      "p": "[Real-Time Joint Semantic Segmentation and Depth Estimation Using Asymmetric Annotations](http://arxiv.org/abs/1809.04766v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DrSleep/multi-task-refinenet)",
      "n": "Multi-Task Light-Weight-RefineNet",
      "d": "2018-09-13",
      "m1": "42.0%"
    },
    {
      "p": "[Light-Weight RefineNet for Real-Time Semantic Segmentation](http://arxiv.org/abs/1810.03272v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DrSleep/light-weight-refinenet)",
      "n": "Light-Weight-RefineNet-50",
      "d": "2018-10-08",
      "m1": "41.7%"
    },
    {
      "p": "[Prompt Guided Transformer for Multi-Task Dense Prediction](https://arxiv.org/abs/2307.15362v1)",
      "c": "[&check;&nbsp;Link](https://github.com/innovator-zero/MTDP_Lib)",
      "n": "PGT (Swin-T)",
      "d": "2023-07-28",
      "m1": "41.61"
    },
    {
      "p": "[Multi-Task Meta Learning: learn how to adapt to unseen tasks](https://arxiv.org/abs/2210.06989v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ricupa/mtml-learn-how-to-adapt-to-unseen-tasks)",
      "n": "MTML",
      "d": "2022-10-13",
      "m1": "41.51%"
    },
    {
      "p": "[Semantic Segmentation with Reverse Attention](http://arxiv.org/abs/1707.06426v1)",
      "c": "",
      "n": "RAN",
      "d": "2017-07-20",
      "m1": "41.2%"
    },
    {
      "p": "[DenseMTL: Cross-task Attention Mechanism for Dense Multi-task Learning](https://arxiv.org/abs/2206.08927v2)",
      "c": "[&check;&nbsp;Link](https://github.com/astra-vision/densemtl)",
      "n": "DenseMTL",
      "d": "2022-06-17",
      "m1": "40.84%"
    },
    {
      "p": "[STD2P: RGBD Semantic Segmentation Using Spatio-Temporal Data-Driven Pooling](http://arxiv.org/abs/1604.02388v3)",
      "c": "[&check;&nbsp;Link](https://github.com/SSAW14/STD2P)",
      "n": "STD2P",
      "d": "2016-04-08",
      "m1": "40.1%"
    },
    {
      "p": "[Masked Supervised Learning for Semantic Segmentation](https://arxiv.org/abs/2210.00923v2)",
      "c": "[&check;&nbsp;Link](https://github.com/hasibzunair/masksup-segmentation)",
      "n": "MaskSup",
      "d": "2022-10-03",
      "m1": "39.31%"
    },
    {
      "p": "[HeMIS: Hetero-Modal Image Segmentation](http://arxiv.org/abs/1607.05194v1)",
      "c": "[&check;&nbsp;Link](https://github.com/momih/pc-hemis)",
      "n": "HeMIS",
      "d": "2016-07-18",
      "m1": "37.77%"
    },
    {
      "p": "[Temporally Distributed Networks for Fast Video Semantic Segmentation](https://arxiv.org/abs/2004.01800v2)",
      "c": "[&check;&nbsp;Link](https://github.com/feinanshan/TDNet)",
      "n": "TD4-PSP18",
      "d": "2020-04-03",
      "m1": "37.4"
    },
    {
      "p": "[What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](http://arxiv.org/abs/1703.04977v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kyle-dorman/bayesian-neural-network-blogpost)",
      "n": "Bayesian DenseNet",
      "d": "2017-03-15",
      "m1": "37.3%"
    },
    {
      "p": "[RGB-based Semantic Segmentation Using Self-Supervised Depth Pre-Training](https://arxiv.org/abs/2002.02200v1)",
      "c": "",
      "n": "HN-network",
      "d": "2020-02-06",
      "m1": "33.49%"
    },
    {
      "p": "[Composite Learning for Robust and Effective Dense Predictions](https://arxiv.org/abs/2210.07239v1)",
      "c": "",
      "n": "CompL",
      "d": "2022-10-13",
      "m1": "33.48%"
    },
    {
      "p": "[Efficient Yet Deep Convolutional Neural Networks for Semantic Segmentation](http://arxiv.org/abs/1707.08254v3)",
      "c": "[&check;&nbsp;Link](https://github.com/SharifAmit/DilatedFCNSegmentation)",
      "n": "Dilated FCN-2s RGB",
      "d": "2017-07-26",
      "m1": "32.3%"
    },
    {
      "p": "[AdaShare: Learning What To Share For Efficient Deep Multi-Task Learning](https://arxiv.org/abs/1911.12423v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sunxm2357/AdaShare)",
      "n": "AdaShare",
      "d": "2019-11-27",
      "m1": "29.6%"
    },
    {
      "p": "[Toward Edge-Efficient Dense Predictions with Synergistic Multi-Task Neural Architecture Search](https://arxiv.org/abs/2210.01384v1)",
      "c": "",
      "n": "EDNAS+JAReD",
      "d": "2022-10-04",
      "m1": "22.1%"
    },
    {
      "p": "[Cross-stitch Networks for Multi-task Learning](http://arxiv.org/abs/1604.03539v1)",
      "c": "[&check;&nbsp;Link](https://github.com/helloyide/Cross-stitch-Networks-for-Multi-task-Learning)",
      "n": "Cross-stitch",
      "d": "2016-04-12",
      "m1": "19.3%"
    },
    {
      "p": "[Fully Convolutional Networks for Semantic Segmentation](http://arxiv.org/abs/1605.06211v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pytorch/vision)",
      "n": "FCN-32s RGB-HHA",
      "d": "2016-05-20",
      "m2": "44"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
