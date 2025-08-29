# medical-image-segmentation-on-kvasir-seg

[Dataset Link](https://datasets.simula.no/kvasir/) \
Task Hierarchy: ['Medical Image Segmentation']

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
      "label": "mean Dice",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Average MAE",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "S-Measure",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "max E-Measure",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "mIoU",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "FPS",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "F-measure",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "Precision",
      "sortable": "true"
    },
    {
      "key": "m9",
      "label": "Recall",
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
      "p": "[Using DUCK-Net for Polyp Image Segmentation](https://arxiv.org/abs/2311.02239v1)",
      "c": "[&check;&nbsp;Link](https://github.com/RazvanDu/DUCK-Net)",
      "n": "DUCK-Net",
      "d": "2023-11-03",
      "m1": "0.9502",
      "m5": "0.9051",
      "m8": "0.9628",
      "m9": "0.9379"
    },
    {
      "p": "[EffiSegNet: Gastrointestinal Polyp Segmentation through a Pre-Trained EfficientNet-based Network with a Simplified Decoder](https://arxiv.org/abs/2407.16298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ivezakis/effisegnet)",
      "n": "EffiSegNet-B5",
      "d": "2024-07-23",
      "m1": "0.9488",
      "m5": "0.9065",
      "m7": "0.9513",
      "m8": "0.9713",
      "m9": "0.9321"
    },
    {
      "p": "[EffiSegNet: Gastrointestinal Polyp Segmentation through a Pre-Trained EfficientNet-based Network with a Simplified Decoder](https://arxiv.org/abs/2407.16298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ivezakis/effisegnet)",
      "n": "EffiSegNet-B4",
      "d": "2024-07-23",
      "m1": "0.9483",
      "m5": "0.9056",
      "m7": "0.9552",
      "m8": "0.9679",
      "m9": "0.9429"
    },
    {
      "p": "[From Semantic Segmentation of Natural Images to Medical Image Segmentation Using ViT-Based Architectures](https://link.springer.com/chapter/10.1007/978-3-031-80507-3_12)",
      "c": "",
      "n": "SegMed",
      "d": "2025-01-31",
      "m1": "0.947",
      "m5": "0.899"
    },
    {
      "p": "[Adaptive t-vMF Dice Loss for Multi-class Medical Image Segmentation](https://arxiv.org/abs/2207.07842v1)",
      "c": "[&check;&nbsp;Link](https://github.com/usagisukisuki/adaptive_t-vmf_dice_loss)",
      "n": "FCB Former",
      "d": "2022-07-16",
      "m1": "0.9445",
      "m5": "0.8974"
    },
    {
      "p": "[FCB-SwinV2 Transformer for Polyp Segmentation](https://arxiv.org/abs/2302.01027v1)",
      "c": "",
      "n": "FCB-SwinV2 Transformer",
      "d": "2023-02-02",
      "m1": "0.9420",
      "m5": "0.8973"
    },
    {
      "p": "[Spatially Exclusive Pasting: A General Data Augmentation for the Polyp Segmentation](https://arxiv.org/abs/2211.08284v3)",
      "c": "",
      "n": "SEP",
      "d": "2022-11-15",
      "m1": "0.9411",
      "m5": "0.9002"
    },
    {
      "p": "[LM-Net: A Light-weight and Multi-scale Network for Medical Image Segmentation](https://arxiv.org/abs/2501.03838v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Asunatan/LM-Net)",
      "n": "LM-Net",
      "d": "2025-01-07",
      "m1": "0.9409",
      "m5": "0.8912",
      "m8": "0.8964",
      "m9": "0.9038"
    },
    {
      "p": "[MetaFormer and CNN Hybrid Model for Polyp Image Segmentation](https://ieeexplore.ieee.org/document/10681057)",
      "c": "[&check;&nbsp;Link](https://github.com/hyunnamlee/RAPUNet)",
      "n": "RAPUNet",
      "d": "2024-09-16",
      "m1": "0.939",
      "m5": "0.885"
    },
    {
      "p": "[FCN-Transformer Feature Fusion for Polyp Segmentation](https://arxiv.org/abs/2208.08352v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ESandML/FCBFormer)",
      "n": "FCBFormer",
      "d": "2022-08-17",
      "m1": "0.9385",
      "m5": "0.8903"
    },
    {
      "p": "[HarDNet-DFUS: An Enhanced Harmonically-Connected Network for Diabetic Foot Ulcer Image Segmentation and Colonoscopy Polyp Segmentation](https://arxiv.org/abs/2209.07313v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yuwenlo/hardnet-dfus)",
      "n": "HarDNet-DFUS",
      "d": "2022-09-15",
      "m1": "0.9363",
      "m5": "0.8894"
    },
    {
      "p": "[Stepwise Feature Fusion: Local Guides Global](https://arxiv.org/abs/2203.03635v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Qiming-Huang/ssformer)",
      "n": "SSFormer-L",
      "d": "2022-03-07",
      "m1": "0.9357",
      "m5": "0.8905"
    },
    {
      "p": "[S2S2: Semantic Stacking for Robust Semantic Segmentation in Medical Imaging](https://arxiv.org/abs/2412.13156v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ymp5078/semantic-stacking)",
      "n": "FCBFormer",
      "d": "2024-12-17",
      "m1": "0.932"
    },
    {
      "p": "[ESFPNet: efficient deep learning architecture for real-time lesion segmentation in autofluorescence bronchoscopic video](https://arxiv.org/abs/2207.07759v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dumyCq/CFPNet)",
      "n": "ESFPNet-L",
      "d": "2022-07-15",
      "m1": "0.931",
      "m5": "0.887"
    },
    {
      "p": "[UGCANet: A Unified Global Context-Aware Transformer-based Network with Feature Alignment for Endoscopic Image Analysis](https://arxiv.org/abs/2307.06260v1)",
      "c": "",
      "n": "UGCANet",
      "d": "2023-07-12",
      "m1": "0.928",
      "m5": "0.881"
    },
    {
      "p": "[EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation](https://arxiv.org/abs/2405.06880v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sldgroup/emcad)",
      "n": "EMCAD",
      "d": "2024-05-11",
      "m1": "0.928"
    },
    {
      "p": "[G-CASCADE: Efficient Cascaded Graph Convolutional Decoding for 2D Medical Image Segmentation](https://arxiv.org/abs/2310.16175v1)",
      "c": "[&check;&nbsp;Link](https://github.com/SLDGroup/G-CASCADE)",
      "n": "PVT-GCASCADE",
      "d": "2023-10-24",
      "m1": "0.9274",
      "m5": "0.8790"
    },
    {
      "p": "[ColonFormer: An Efficient Transformer based Method for Colon Polyp Segmentation](https://arxiv.org/abs/2205.08473v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ducnt9907/ColonFormer)",
      "n": "ColonFormer",
      "d": "2022-05-17",
      "m1": "0.927",
      "m5": "0.877"
    },
    {
      "p": "[RaBiT: An Efficient Transformer using Bidirectional Feature Pyramid Network with Reverse Attention for Colon Polyp Segmentation](https://arxiv.org/abs/2307.06420v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nguyenhoangthuan99/RaBiT)",
      "n": "RaBiT",
      "d": "2023-07-12",
      "m1": "0.927",
      "m5": "0.873"
    },
    {
      "p": "[GMSRF-Net: An improved generalizability with global multi-scale residual fusion network for polyp segmentation](https://arxiv.org/abs/2111.10614v1)",
      "c": "[&check;&nbsp;Link](https://github.com/NoviceMAn-prog/GMSRFNet)",
      "n": "GMSRF-Net",
      "d": "2021-11-20",
      "m1": "0.9263",
      "m5": "0.8843"
    },
    {
      "p": "[Medical Image Segmentation via Cascaded Attention Decoding](https://openaccess.thecvf.com/content/WACV2023/html/Rahman_Medical_Image_Segmentation_via_Cascaded_Attention_Decoding_WACV_2023_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/SLDGroup/CASCADE)",
      "n": "PVT-CASCADE",
      "d": "2023-01-03",
      "m1": "0.9258",
      "m5": "0.8776"
    },
    {
      "p": "[DuAT: Dual-Aggregation Transformer Network for Medical Image Segmentation](https://arxiv.org/abs/2212.11677v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Barrett-python/DuAT)",
      "n": "DuAT",
      "d": "2022-12-21",
      "m1": "0.924",
      "m2": "0.023",
      "m5": "0.876"
    },
    {
      "p": "[MSRF-Net: A Multi-Scale Residual Fusion Network for Biomedical Image Segmentation](https://arxiv.org/abs/2105.07451v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NoviceMAn-prog/MSRF-Net)",
      "n": "MSRF-Net",
      "d": "2021-05-16",
      "m1": "0.9217",
      "m5": "0.8914"
    },
    {
      "p": "[Adaptation of Distinct Semantics for Uncertain Areas in Polyp Segmentation](https://arxiv.org/abs/2405.07523v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vinhhust2806/ADSNet)",
      "n": "ADSNet",
      "d": "2024-05-13",
      "m1": "0.92",
      "m5": "0.871"
    },
    {
      "p": "[CaraNet: Context Axial Reverse Attention Network for Segmentation of Small Medical Objects](https://arxiv.org/abs/2108.07368v3)",
      "c": "[&check;&nbsp;Link](https://github.com/AngeLouCN/CaraNet)",
      "n": "CaraNet",
      "d": "2021-08-16",
      "m1": "0.918",
      "m2": "0.023",
      "m3": "0.929",
      "m4": "0.968",
      "m5": "0.865"
    },
    {
      "p": "[TransFuse: Fusing Transformers and CNNs for Medical Image Segmentation](https://arxiv.org/abs/2102.08005v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Rayicer/TransFuse)",
      "n": "TransFuse-L",
      "d": "2021-02-16",
      "m1": "0.918",
      "m5": "0.868"
    },
    {
      "p": "[TransFuse: Fusing Transformers and CNNs for Medical Image Segmentation](https://arxiv.org/abs/2102.08005v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Rayicer/TransFuse)",
      "n": "TransFuse-S",
      "d": "2021-02-16",
      "m1": "0.918",
      "m5": "0.868"
    },
    {
      "p": "[BDG-Net: Boundary Distribution Guided Network for Accurate Polyp Segmentation](https://arxiv.org/abs/2201.00767v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zihuanqiu/BDG-Net)",
      "n": "BDG-Net",
      "d": "2022-01-03",
      "m1": "0.915",
      "m2": "0.021",
      "m3": "0.923",
      "m4": "0.972",
      "m5": "0.865"
    },
    {
      "p": "[SAM-EG: Segment Anything Model with Egde Guidance framework for efficient Polyp Segmentation](https://arxiv.org/abs/2406.14819v1)",
      "c": "",
      "n": "SAM-EG",
      "d": "2024-06-21",
      "m1": "0.915",
      "m5": "0.862"
    },
    {
      "p": "[UniNet: A Contrastive Learning-guided Unified Framework with Feature Selection for Anomaly Detection](https://pangdatangtt.github.io/#:~:text=guided%20anomaly%20discrimination.-,Abstract,-Anomaly%20detection%20(AD)",
      "c": "[&check;&nbsp;Link](https://github.com/pangdatangtt/UniNet)",
      "n": "UniNet",
      "d": "2025-02-28",
      "m1": "0.915",
      "m5": "0.857"
    },
    {
      "p": "[MEGANet: Multi-Scale Edge-Guided Attention Network for Weak Boundary Polyp Segmentation](https://arxiv.org/abs/2309.03329v3)",
      "c": "[&check;&nbsp;Link](https://github.com/uark-aicv/meganet)",
      "n": "MEGANet(Res2Net-50)",
      "d": "2023-09-06",
      "m1": "0.913",
      "m2": "0.025",
      "m5": "0.863"
    },
    {
      "p": "[KDAS: Knowledge Distillation via Attention Supervision Framework for Polyp Segmentation](https://arxiv.org/abs/2312.08555v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huyquoctrinh/kdas)",
      "n": "KDAS",
      "d": "2023-12-13",
      "m1": "0.913",
      "m2": "0.027",
      "m5": "0.848"
    },
    {
      "p": "[HarDNet-MSEG: A Simple Encoder-Decoder Polyp Segmentation Neural Network that Achieves over 0.9 Mean Dice and 86 FPS](https://arxiv.org/abs/2101.07172v2)",
      "c": "[&check;&nbsp;Link](https://github.com/james128333/HarDNet-MSEG)",
      "n": "HarDNet-MSEG",
      "d": "2021-01-18",
      "m1": "0.912",
      "m2": "0.025",
      "m3": "0.923",
      "m4": "0.958",
      "m5": "0.857",
      "m6": "116"
    },
    {
      "p": "[UACANet: Uncertainty Augmented Context Attention for Polyp Segmentation](https://arxiv.org/abs/2107.02368v3)",
      "c": "[&check;&nbsp;Link](https://github.com/plemeri/UACANet)",
      "n": "UACANet-L",
      "d": "2021-07-06",
      "m1": "0.912",
      "m2": "0.025",
      "m3": "0.917",
      "m4": "0.958",
      "m5": "0.862"
    },
    {
      "p": "[MEGANet: Multi-Scale Edge-Guided Attention Network for Weak Boundary Polyp Segmentation](https://arxiv.org/abs/2309.03329v3)",
      "c": "[&check;&nbsp;Link](https://github.com/uark-aicv/meganet)",
      "n": "MEGANet(ResNet-34)",
      "d": "2023-09-06",
      "m1": "0.911",
      "m2": "0.026",
      "m5": "0.859"
    },
    {
      "p": "[ProMISe: Promptable Medical Image Segmentation using SAM](https://arxiv.org/abs/2403.04164v3)",
      "c": "[&check;&nbsp;Link](https://github.com/xinkunwang111/promise)",
      "n": "ProMISe",
      "d": "2024-03-07",
      "m1": "0.911",
      "m5": "0.851"
    },
    {
      "p": "[A-DenseUNet: Adaptive Densely Connected UNet for Polyp Segmentation in Colonoscopy Images with Atrous Convolution](https://www.mdpi.com/1424-8220/21/4/1441)",
      "c": "",
      "n": "A-DenseUNet",
      "d": "2021-02-19",
      "m1": "0.9085",
      "m5": "0.8615"
    },
    {
      "p": "[UACANet: Uncertainty Augmented Context Attention for Polyp Segmentation](https://arxiv.org/abs/2107.02368v3)",
      "c": "[&check;&nbsp;Link](https://github.com/plemeri/UACANet)",
      "n": "UACANet-S",
      "d": "2021-07-06",
      "m1": "0.905",
      "m2": "0.026",
      "m3": "0.914",
      "m4": "0.951",
      "m5": "0.852"
    },
    {
      "p": "[COMMA: Propagating Complementary Multi-Level Aggregation Network for Polyp Segmentation](https://www.mdpi.com/2076-3417/12/4/2114)",
      "c": "",
      "n": "COMMA (ResNet-50)",
      "d": "2022-02-17",
      "m1": "0.904",
      "m2": "0.024",
      "m3": "0.925",
      "m4": "0.963",
      "m5": "0.860"
    },
    {
      "p": "[Polyp-SAM++: Can A Text Guided SAM Perform Better for Polyp Segmentation?](https://arxiv.org/abs/2308.06623v1)",
      "c": "[&check;&nbsp;Link](https://github.com/RisabBiswas/Polyp-SAM-PlusPlus)",
      "n": "Polyp-SAM++",
      "d": "2023-08-12",
      "m1": "0.902",
      "m5": "0.862",
      "m7": "0.92"
    },
    {
      "p": "[AG-CUResNeSt: A Novel Method for Colon Polyp Segmentation](https://arxiv.org/abs/2105.00402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/code-implementation1/Code9/tree/main/resnest)",
      "n": "AG-CUResNeSt",
      "d": "2021-05-02",
      "m1": "0.902",
      "m5": "0.845"
    },
    {
      "p": "[COMMA: Propagating Complementary Multi-Level Aggregation Network for Polyp Segmentation](https://www.mdpi.com/2076-3417/12/4/2114)",
      "c": "",
      "n": "COMMA (Res2Net-50)",
      "d": "2022-02-17",
      "m1": "0.901",
      "m2": "0.027",
      "m3": "0.919",
      "m4": "0.951",
      "m5": "0.852"
    },
    {
      "p": "[TGANet: Text-guided attention for improved polyp segmentation](https://arxiv.org/abs/2205.04280v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nikhilroxtomar/tganet)",
      "n": "TGA-Net",
      "d": "2022-05-09",
      "m1": "0.8982",
      "m5": "0.8330"
    },
    {
      "p": "[PraNet: Parallel Reverse Attention Network for Polyp Segmentation](https://arxiv.org/abs/2006.11392v4)",
      "c": "[&check;&nbsp;Link](https://github.com/DengPingFan/PraNet)",
      "n": "PraNet",
      "d": "2020-06-13",
      "m1": "0.898",
      "m2": "0.030",
      "m3": "0.915",
      "m4": "0.948",
      "m5": "0.849"
    },
    {
      "p": "[TransResU-Net: Transformer based ResU-Net for Real-Time Colonoscopy Polyp Segmentation](https://arxiv.org/abs/2206.08985v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nikhilroxtomar/transresunet)",
      "n": "TransResU-Net",
      "d": "2022-06-17",
      "m1": "0.8884",
      "m5": "0.8214",
      "m6": "48.61"
    },
    {
      "p": "[Multi Kernel Positional Embedding ConvNeXt for Polyp Segmentation](https://arxiv.org/abs/2301.06673v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huyquoctrinh/PEFNet)",
      "n": "PEFNet",
      "d": "2023-01-17",
      "m1": "0.8818",
      "m5": "0.8163"
    },
    {
      "p": "[FANet: A Feedback Attention Network for Improved Biomedical Image Segmentation](https://arxiv.org/abs/2103.17235v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nikhilroxtomar/fanet)",
      "n": "FANet",
      "d": "2021-03-31",
      "m1": "0.8803",
      "m2": "0.8153"
    },
    {
      "p": "[TransNetR: Transformer-based Residual Network for Polyp Segmentation with Multi-Center Out-of-Distribution Testing](https://arxiv.org/abs/2303.07428v1)",
      "c": "[&check;&nbsp;Link](https://github.com/debeshjha/transnetr)",
      "n": "TransNetR",
      "d": "2023-03-13",
      "m1": "0.8706",
      "m5": "0.8016",
      "m6": "54.60"
    },
    {
      "p": "[Self-Prompting Polyp Segmentation in Colonoscopy using Hybrid Yolo-SAM 2 Model](https://arxiv.org/abs/2409.09484v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sajjad-sh33/yolo_sam2)",
      "n": "Yolo-SAM 2",
      "d": "2024-09-14",
      "m1": "0.866",
      "m5": "0.764"
    },
    {
      "p": "[DDANet: Dual Decoder Attention Network for Automatic Polyp Segmentation](https://arxiv.org/abs/2012.15245v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nikhilroxtomar/DDANet)",
      "n": "DDANet",
      "d": "2020-12-30",
      "m1": "0.8576",
      "m5": "0.7800",
      "m6": "69.59"
    },
    {
      "p": "[Dual Cross-Attention for Medical Image Segmentation](https://arxiv.org/abs/2303.17696v1)",
      "c": "[&check;&nbsp;Link](https://github.com/gorkemcanates/dual-cross-attention)",
      "n": "DoubleUnet-DCA",
      "d": "2023-03-30",
      "m1": "0.8516",
      "m5": "0.7434"
    },
    {
      "p": "[A Comprehensive Study on Colorectal Polyp Segmentation with ResUNet++, Conditional Random Field and Test-Time Augmentation](https://arxiv.org/abs/2107.12435v1)",
      "c": "[&check;&nbsp;Link](https://github.com/DebeshJha/ResUNet-with-CRF-and-TTA)",
      "n": "ResUNet++ + TTA + CRF",
      "d": "2021-07-26",
      "m1": "0.8508",
      "m5": "0.7800",
      "m6": "69.59"
    },
    {
      "p": "[UNet++: A Nested U-Net Architecture for Medical Image Segmentation](http://arxiv.org/abs/1807.10165v1)",
      "c": "[&check;&nbsp;Link](https://github.com/qubvel/segmentation_models.pytorch)",
      "n": "U-Net++",
      "d": "2018-07-18",
      "m1": "0.8210",
      "m2": "0.048",
      "m3": "0.862",
      "m4": "0.910"
    },
    {
      "p": "[Real-Time Polyp Detection, Localization and Segmentation in Colonoscopy Using Deep Learning](https://arxiv.org/abs/2011.07631v2)",
      "c": "[&check;&nbsp;Link](https://github.com/DebeshJha/ColonSegNet)",
      "n": "ColonSegNet",
      "d": "2020-11-15",
      "m1": "0.8206",
      "m5": "0.7239",
      "m6": "182.38"
    },
    {
      "p": "[U-Net: Convolutional Networks for Biomedical Image Segmentation](http://arxiv.org/abs/1505.04597v1)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "U-Net",
      "d": "2015-05-18",
      "m1": "0.8180",
      "m2": "0.055",
      "m3": "0.858",
      "m4": "0.893"
    },
    {
      "p": "[ResUNet++: An Advanced Architecture for Medical Image Segmentation](https://arxiv.org/abs/1911.07067v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rishikksh20/ResUnet)",
      "n": "ResUNet++",
      "d": "2019-11-16",
      "m1": "0.8133"
    },
    {
      "p": "[Kvasir-SEG: A Segmented Polyp Dataset](https://arxiv.org/abs/1911.07069v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tfboys-lzz/fobs)",
      "n": "ResUNet",
      "d": "2019-11-16",
      "m1": "0.7877"
    },
    {
      "p": "[RUPNet: Residual upsampling network for real-time polyp segmentation](https://arxiv.org/abs/2301.02703v2)",
      "c": "",
      "n": "RUPNet",
      "d": "2023-01-06",
      "m1": "0.7658",
      "m5": "0.6553",
      "m6": "152.60"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
