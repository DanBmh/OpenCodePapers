# semantic-segmentation-on-ade20k

[Dataset Link](https://groups.csail.mit.edu/vision/datasets/ADE20K/) \
Task Hierarchy: ['Semantic Segmentation']

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
      "label": "Validation mIoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Test Score",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Params (M)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "GFLOPs (512 x 512)",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "GFLOPs",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Mean IoU (class)",
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
      "p": "[The Missing Point in Vision Transformers for Universal Image Segmentation](https://arxiv.org/abs/2505.19795v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sajjad-sh33/vit-p)",
      "n": "ViT-P (InternImage-H)",
      "d": "2025-05-26",
      "m1": "63.6",
      "m3": "1610"
    },
    {
      "p": "[ONE-PEACE: Exploring One General Representation Model Toward Unlimited Modalities](https://arxiv.org/abs/2305.11172v1)",
      "c": "[&check;&nbsp;Link](https://github.com/modelscope/modelscope)",
      "n": "ONE-PEACE",
      "d": "2023-05-18",
      "m1": "63.0",
      "m3": "1500"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-H",
      "d": "2022-11-10",
      "m1": "62.9",
      "m3": "1310",
      "m5": "4635"
    },
    {
      "p": "[Towards All-in-one Pre-training via Maximizing Multi-modal Mutual Information](https://arxiv.org/abs/2211.09807v2)",
      "c": "[&check;&nbsp;Link](https://github.com/OpenGVLab/M3I-Pretraining)",
      "n": "M3I Pre-training (InternImage-H)",
      "d": "2022-11-17",
      "m1": "62.9",
      "m3": "1310"
    },
    {
      "p": "[Image as a Foreign Language: BEiT Pretraining for All Vision and Vision-Language Tasks](https://arxiv.org/abs/2208.10442v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/unilm/tree/master/beit)",
      "n": "BEiT-3",
      "d": "2022-08-22",
      "m1": "62.8",
      "m3": "1900"
    },
    {
      "p": "[EVA: Exploring the Limits of Masked Visual Representation Learning at Scale](https://arxiv.org/abs/2211.07636v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EVA",
      "d": "2022-11-14",
      "m1": "62.3",
      "m3": "1074"
    },
    {
      "p": "[The Missing Point in Vision Transformers for Universal Image Segmentation](https://arxiv.org/abs/2505.19795v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sajjad-sh33/vit-p)",
      "n": "ViT-P (OneFormer, InternImage-H)",
      "d": "2025-05-26",
      "m1": "61.6",
      "m3": "1400"
    },
    {
      "p": "[Vision Transformer Adapter for Dense Predictions](https://arxiv.org/abs/2205.08534v4)",
      "c": "[&check;&nbsp;Link](https://github.com/czczup/vit-adapter)",
      "n": "ViT-Adapter-L (Mask2Former, BEiTv2 pretrain)",
      "d": "2022-05-17",
      "m1": "61.5",
      "m3": "571"
    },
    {
      "p": "[Contrastive Learning Rivals Masked Image Modeling in Fine-tuning via Feature Distillation](https://arxiv.org/abs/2205.14141v3)",
      "c": "[&check;&nbsp;Link](https://github.com/SwinTransformer/Feature-Distillation)",
      "n": "FD-SwinV2-G",
      "d": "2022-05-27",
      "m1": "61.4",
      "m3": "3000"
    },
    {
      "p": "[Reversible Column Networks](https://arxiv.org/abs/2212.11696v3)",
      "c": "[&check;&nbsp;Link](https://github.com/megvii-research/revcol)",
      "n": "RevCol-H (Mask2Former)",
      "d": "2022-12-22",
      "m1": "61.0",
      "m3": "2439"
    },
    {
      "p": "[Mask DINO: Towards A Unified Transformer-based Framework for Object Detection and Segmentation](https://arxiv.org/abs/2206.02777v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "MasK DINO (SwinL, multi-scale)",
      "d": "2022-06-06",
      "m1": "60.8",
      "m3": "223"
    },
    {
      "p": "[Vision Transformer Adapter for Dense Predictions](https://arxiv.org/abs/2205.08534v4)",
      "c": "[&check;&nbsp;Link](https://github.com/czczup/vit-adapter)",
      "n": "ViT-Adapter-L (Mask2Former, BEiT pretrain)",
      "d": "2022-05-17",
      "m1": "60.5",
      "m3": "571"
    },
    {
      "p": "[DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DINOv2 (ViT-g/14 frozen model, w/ ViT-Adapter + Mask2former)",
      "d": "2023-04-14",
      "m1": "60.2",
      "m3": "1080"
    },
    {
      "p": "[The Missing Point in Vision Transformers for Universal Image Segmentation](https://arxiv.org/abs/2505.19795v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sajjad-sh33/vit-p)",
      "n": "ViT-P (OneFormer, DiNAT-L)",
      "d": "2025-05-26",
      "m1": "59.9",
      "m3": "309"
    },
    {
      "p": "[Swin Transformer V2: Scaling Up Capacity and Resolution](https://arxiv.org/abs/2111.09883v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "SwinV2-G(UperNet)",
      "d": "2021-11-18",
      "m1": "59.9"
    },
    {
      "p": "[Parameter-Inverted Image Pyramid Networks](https://arxiv.org/abs/2406.04330v2)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/piip)",
      "n": "PIIP-LH6B(UperNet)",
      "d": "2024-06-06",
      "m1": "59.9"
    },
    {
      "p": "[SERNet-Former: Semantic Segmentation by Efficient Residual Network with Attention-Boosting Gates and Attention-Fusion Networks](https://arxiv.org/abs/2401.15741v7)",
      "c": "[&check;&nbsp;Link](https://github.com/serdarch/sernet-former)",
      "n": "SERNet-Former",
      "d": "2024-01-28",
      "m1": "59.35"
    },
    {
      "p": "[Focal Modulation Networks](https://arxiv.org/abs/2203.11926v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "FocalNet-L (Mask2Former)",
      "d": "2022-03-22",
      "m1": "58.5"
    },
    {
      "p": "[Vision Transformer Adapter for Dense Predictions](https://arxiv.org/abs/2205.08534v4)",
      "c": "[&check;&nbsp;Link](https://github.com/czczup/vit-adapter)",
      "n": "ViT-Adapter-L (UperNet, BEiT pretrain)",
      "d": "2022-05-17",
      "m1": "58.4",
      "m3": "451"
    },
    {
      "p": "[Representation Separation for Semantic Segmentation with Vision Transformers](https://arxiv.org/abs/2212.13764v1)",
      "c": "",
      "n": "RSSeg-ViT-L (BEiT pretrain)",
      "d": "2022-12-28",
      "m1": "58.4",
      "m3": "330"
    },
    {
      "p": "[Your ViT is Secretly an Image Segmentation Model](https://arxiv.org/abs/2503.19108v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tue-mps/eomt)",
      "n": "EoMT (DINOv2-L, single-scale, 512x512)",
      "d": "2025-03-24",
      "m1": "58.4",
      "m3": "316",
      "m4": "721",
      "m5": "721",
      "m6": "58.4"
    },
    {
      "p": "[SegViTv2: Exploring Efficient and Continual Semantic Segmentation with Plain Vision Transformers](https://arxiv.org/abs/2306.06289v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zbwxp/SegVit)",
      "n": "SegViT-v2 (BEiT-v2-Large)",
      "d": "2023-06-09",
      "m1": "58.2",
      "m4": "637.9"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-L FaPN-Mask2Former)",
      "d": "2021-12-23",
      "m1": "58.2"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-L MSFaPN-Mask2Former)",
      "d": "2021-12-23",
      "m1": "58.2"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-L (Mask2Former)",
      "d": "2022-09-29",
      "m1": "58.1"
    },
    {
      "p": "[HorNet: Efficient High-Order Spatial Interactions with Recursive Gated Convolutions](https://arxiv.org/abs/2207.14284v3)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmclassification)",
      "n": "HorNet-L (Mask2Former)",
      "d": "2022-07-28",
      "m1": "57.9"
    },
    {
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former (SwinL-FaPN)",
      "d": "2021-12-02",
      "m1": "57.7"
    },
    {
      "p": "[Dynamic Focus-aware Positional Queries for Semantic Segmentation](https://arxiv.org/abs/2204.01244v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ziplab/faseg)",
      "n": "FASeg (SwinL)",
      "d": "2022-04-04",
      "m1": "57.7"
    },
    {
      "p": "[Region Rebalance for Long-Tailed Semantic Segmentation](https://arxiv.org/abs/2204.01969v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dvlab-research/parametric-contrastive-learning)",
      "n": "RR (BEiT-L)",
      "d": "2022-04-05",
      "m1": "57.7"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "MOAT-4 (IN-22K pretraining, single-scale)",
      "d": "2022-10-04",
      "m1": "57.6",
      "m3": "496"
    },
    {
      "p": "[Could Giant Pretrained Image Models Extract Universal Representations?](https://arxiv.org/abs/2211.02043v1)",
      "c": "",
      "n": "Frozen Backbone, SwinV2-G-ext22K (Mask2Former)",
      "d": "2022-11-03",
      "m1": "57.6"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-L Mask2Former)",
      "d": "2021-12-23",
      "m1": "57.5"
    },
    {
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former (SwinL)",
      "d": "2021-12-02",
      "m1": "57.3"
    },
    {
      "p": "[Efficient Self-Ensemble for Semantic Segmentation](https://arxiv.org/abs/2111.13280v2)",
      "c": "[&check;&nbsp;Link](https://github.com/WalBouss/SenFormer)",
      "n": "SenFormer (BEiT-L)",
      "d": "2021-11-26",
      "m1": "57.1"
    },
    {
      "p": "[BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BEiT-L (ViT+UperNet)",
      "d": "2021-06-15",
      "m1": "57.0"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask(SeMask Swin-L MSFaPN-Mask2Former, single-scale)",
      "d": "2021-12-23",
      "m1": "57.0"
    },
    {
      "p": "[Harnessing Diffusion Models for Visual Perception with Meta Prompts](https://arxiv.org/abs/2312.14733v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fudan-zvg/meta-prompts)",
      "n": "MetaPrompt-SD",
      "d": "2023-12-22",
      "m1": "56.8"
    },
    {
      "p": "[FaPN: Feature-aligned Pyramid Network for Dense Image Prediction](https://arxiv.org/abs/2108.07058v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sithu31296/semantic-segmentation)",
      "n": "FaPN (MaskFormer, Swin-L, ImageNet-22k pretrain)",
      "d": "2021-08-16",
      "m1": "56.7"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "MOAT-3 (IN-22K pretraining, single-scale)",
      "d": "2022-10-04",
      "m1": "56.5",
      "m3": "198"
    },
    {
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former (Swin-L-FaPN)",
      "d": "2021-12-02",
      "m1": "56.4"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-L MaskFormer)",
      "d": "2021-12-23",
      "m1": "56.2"
    },
    {
      "p": "[Exploring Target Representations for Masked Autoencoders](https://arxiv.org/abs/2209.03917v3)",
      "c": "[&check;&nbsp;Link](https://github.com/liuxingbin/dbot)",
      "n": "dBOT ViT-L (CLIP)",
      "d": "2022-09-08",
      "m1": "56.2"
    },
    {
      "p": "[Conditional Boundary Loss for Semantic Segmentation](https://ieeexplore.ieee.org/document/10173725)",
      "c": "[&check;&nbsp;Link](https://github.com/dywu98/CBL-Conditional-Boundary-Loss)",
      "n": "Mask2Former+CBL(Swin-B)",
      "d": "2023-07-05",
      "m1": "56.1"
    },
    {
      "p": "[Text-image Alignment for Diffusion-based Perception](https://arxiv.org/abs/2310.00031v3)",
      "c": "[&check;&nbsp;Link](https://github.com/damaggu/tadp)",
      "n": "TADP",
      "d": "2023-09-29",
      "m1": "55.9"
    },
    {
      "p": "[CSWin Transformer: A General Vision Transformer Backbone with Cross-Shaped Windows](https://arxiv.org/abs/2107.00652v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleClas)",
      "n": "CSWin-L (UperNet, ImageNet-22k pretrain)",
      "d": "2021-07-01",
      "m1": "55.70"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-XL",
      "d": "2023-11-27",
      "m1": "55.6"
    },
    {
      "p": "[Focal Self-attention for Local-Global Interactions in Vision Transformers](https://arxiv.org/abs/2107.00641v1)",
      "c": "[&check;&nbsp;Link](https://github.com/BR-IDL/PaddleViT/tree/develop/image_classification/Focal_Transformer)",
      "n": "Focal-L (UperNet, ImageNet-22k pretrain)",
      "d": "2021-07-01",
      "m1": "55.40"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-XL",
      "d": "2022-11-10",
      "m1": "55.3",
      "m3": "368",
      "m5": "3142"
    },
    {
      "p": "[Exploring Target Representations for Masked Autoencoders](https://arxiv.org/abs/2209.03917v3)",
      "c": "[&check;&nbsp;Link](https://github.com/liuxingbin/dbot)",
      "n": "dBOT ViT-L",
      "d": "2022-09-08",
      "m1": "55.2"
    },
    {
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former(Swin-B)",
      "d": "2021-12-02",
      "m1": "55.1"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V2-H (FCMAE)",
      "d": "2023-01-02",
      "m1": "55"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-L++",
      "d": "2023-11-27",
      "m1": "55"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-Large (UperNet)",
      "d": "2022-09-29",
      "m1": "54.9"
    },
    {
      "p": "[Conditional Boundary Loss for Semantic Segmentation](https://ieeexplore.ieee.org/document/10173725)",
      "c": "[&check;&nbsp;Link](https://github.com/dywu98/CBL-Conditional-Boundary-Loss)",
      "n": "MaskFormer+CBL(Swin-B)",
      "d": "2023-07-05",
      "m1": "54.9"
    },
    {
      "p": "[TransNeXt: Robust Foveal Visual Perception for Vision Transformers](https://arxiv.org/abs/2311.17132v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Westlake-AI/openmixup)",
      "n": "TransNeXt-Base (IN-1K pretrain, Mask2Former, 512)",
      "d": "2023-11-28",
      "m1": "54.7",
      "m3": "109"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "MOAT-2 (IN-22K pretraining, single-scale)",
      "d": "2022-10-04",
      "m1": "54.7",
      "m3": "81"
    },
    {
      "p": "[Context Autoencoder for Self-Supervised Representation Learning](https://arxiv.org/abs/2202.03026v3)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmselfsup)",
      "n": "CAE (ViT-L, UperNet)",
      "d": "2022-02-07",
      "m1": "54.7"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-B6",
      "d": "2022-02-20",
      "m1": "54.7"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT_s-Large (UperNet)",
      "d": "2022-09-29",
      "m1": "54.6"
    },
    {
      "p": "[DDP: Diffusion Model for Dense Visual Prediction](https://arxiv.org/abs/2303.17559v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jiyuanfeng/ddp)",
      "n": "DDP (Swin-L, step-3)",
      "d": "2023-03-30",
      "m1": "54.4",
      "m3": "207"
    },
    {
      "p": "[Vision Transformers with Patch Diversification](https://arxiv.org/abs/2104.12753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ChengyueGongR/PatchVisionTransformer)",
      "n": "PatchDiverse + Swin-L (multi-scale test, upernet, ImageNet22k pretrain)",
      "d": "2021-04-26",
      "m1": "54.4"
    },
    {
      "p": "[VOLO: Vision Outlooker for Visual Recognition](https://arxiv.org/abs/2106.13112v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VOLO-D5",
      "d": "2021-06-24",
      "m1": "54.3"
    },
    {
      "p": "[K-Net: Towards Unified Image Segmentation](https://arxiv.org/abs/2106.14855v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zwwwayne/k-net)",
      "n": "K-Net",
      "d": "2021-06-28",
      "m1": "54.3"
    },
    {
      "p": "[Generalized Parametric Contrastive Learning](https://arxiv.org/abs/2209.12400v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dvlab-research/parametric-contrastive-learning)",
      "n": "GPaCo (Swin-L)",
      "d": "2022-09-26",
      "m1": "54.3"
    },
    {
      "p": "[Efficient Self-Ensemble for Semantic Segmentation](https://arxiv.org/abs/2111.13280v2)",
      "c": "[&check;&nbsp;Link](https://github.com/WalBouss/SenFormer)",
      "n": "SenFormer (Swin-L)",
      "d": "2021-11-26",
      "m1": "54.2"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "Swin V2-H",
      "d": "2023-01-02",
      "m1": "54.2"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-L",
      "d": "2022-11-10",
      "m1": "54.1",
      "m3": "256",
      "m5": "2526"
    },
    {
      "p": "[TransNeXt: Robust Foveal Visual Perception for Vision Transformers](https://arxiv.org/abs/2311.17132v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Westlake-AI/openmixup)",
      "n": "TransNeXt-Small (IN-1K pretrain, Mask2Former, 512)",
      "d": "2023-11-28",
      "m1": "54.1",
      "m3": "69"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-XL++",
      "d": "2022-01-10",
      "m1": "54",
      "m3": "391",
      "m4": "3335"
    },
    {
      "p": "[Sequential Ensembling for Semantic Segmentation](https://arxiv.org/abs/2210.05387v1)",
      "c": "",
      "n": "Sequential Ensemble (SegFormer)",
      "d": "2022-10-08",
      "m1": "54",
      "m3": "216.3"
    },
    {
      "p": "[MogaNet: Multi-order Gated Aggregation Network](https://arxiv.org/abs/2211.03295v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/OpenSTL)",
      "n": "MogaNet-XL (UperNet)",
      "d": "2022-11-07",
      "m1": "54"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-B++",
      "d": "2023-11-27",
      "m1": "53.9"
    },
    {
      "p": "[Per-Pixel Classification is Not All You Need for Semantic Segmentation](https://arxiv.org/abs/2107.06278v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "MaskFormer(Swin-B)",
      "d": "2021-07-13",
      "m1": "53.8"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-L++",
      "d": "2022-01-10",
      "m1": "53.7",
      "m3": "235",
      "m4": "2458"
    },
    {
      "p": "[Swin Transformer V2: Scaling Up Capacity and Resolution](https://arxiv.org/abs/2111.09883v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "SwinV2-G-HTC++ Liu et al. ([2021a])",
      "d": "2021-11-18",
      "m1": "53.7"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V2-L",
      "d": "2023-01-02",
      "m1": "53.7"
    },
    {
      "p": "[Segmenter: Transformer for Semantic Segmentation](https://arxiv.org/abs/2105.05633v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "Seg-L-Mask/16 (MS)",
      "d": "2021-05-12",
      "m1": "53.63"
    },
    {
      "p": "[Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/mae)",
      "n": "MAE (ViT-L, UperNet)",
      "d": "2021-11-11",
      "m1": "53.6"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-L FPN)",
      "d": "2021-12-23",
      "m1": "53.52"
    },
    {
      "p": "[Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/abs/2103.14030v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Swin-L (UperNet, ImageNet-22k pretrain)",
      "d": "2021-03-25",
      "m1": "53.50",
      "m2": "62.8"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "Swin-L",
      "d": "2023-01-02",
      "m1": "53.5"
    },
    {
      "p": "[TransNeXt: Robust Foveal Visual Perception for Vision Transformers](https://arxiv.org/abs/2311.17132v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Westlake-AI/openmixup)",
      "n": "TransNeXt-Tiny (IN-1K pretrain, Mask2Former, 512)",
      "d": "2023-11-28",
      "m1": "53.4",
      "m3": "47.5"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-B++",
      "d": "2022-01-10",
      "m1": "53.1",
      "m3": "122",
      "m4": "1828"
    },
    {
      "p": "[Augmenting Convolutional networks with attention-based aggregation](https://arxiv.org/abs/2112.13692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/deit)",
      "n": "PatchConvNet-L120 (UperNet)",
      "d": "2021-12-27",
      "m1": "52.9"
    },
    {
      "p": "[Exploring Target Representations for Masked Autoencoders](https://arxiv.org/abs/2209.03917v3)",
      "c": "[&check;&nbsp;Link](https://github.com/liuxingbin/dbot)",
      "n": "dBOT ViT-B (CLIP)",
      "d": "2022-09-08",
      "m1": "52.9"
    },
    {
      "p": "[Augmenting Convolutional networks with attention-based aggregation](https://arxiv.org/abs/2112.13692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/deit)",
      "n": "PatchConvNet-B120\n(UperNet)",
      "d": "2021-12-27",
      "m1": "52.8"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "Swin-B",
      "d": "2023-01-02",
      "m1": "52.8"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-S++",
      "d": "2023-11-27",
      "m1": "52.7"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V2-B",
      "d": "2023-01-02",
      "m1": "52.1"
    },
    {
      "p": "[DeBiFormer: Vision Transformer with Deformable Agent Bi-level Routing Attention](https://arxiv.org/abs/2410.08582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/maclong01/DeBiFormer)",
      "n": "DeBiFormer-B (IN1k pretrain, Upernet 160k)",
      "d": "2024-10-11",
      "m1": "52.0"
    },
    {
      "p": "[All Tokens Matter: Token Labeling for Training Better Vision Transformers](https://arxiv.org/abs/2104.10858v3)",
      "c": "[&check;&nbsp;Link](https://github.com/zihangJiang/TokenLabeling)",
      "n": "LV-ViT-L (UperNet, MS)",
      "d": "2021-04-22",
      "m1": "51.8",
      "m3": "209"
    },
    {
      "p": "[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "SegFormer-B5",
      "d": "2021-05-31",
      "m1": "51.8",
      "m3": "84.7"
    },
    {
      "p": "[BiFormer: Vision Transformer with Bi-Level Routing Attention](https://arxiv.org/abs/2303.08810v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rayleizhu/biformer)",
      "n": "BiFormer-B (IN1k pretrain, Upernet 160k)",
      "d": "2023-03-15",
      "m1": "51.7"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V2-L (Supervised)",
      "d": "2023-01-02",
      "m1": "51.6"
    },
    {
      "p": "[Is Attention Better Than Matrix Decomposition?](https://arxiv.org/abs/2109.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Gsunshine/Enjoy-Hamburger)",
      "n": "Light-Ham (VAN-Huge)",
      "d": "2021-09-09",
      "m1": "51.5",
      "m3": "61.1",
      "m4": "71.8"
    },
    {
      "p": "[DAT++: Spatially Dynamic Vision Transformer with Deformable Attention](https://arxiv.org/abs/2309.01430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-B++",
      "d": "2023-09-04",
      "m1": "51.5"
    },
    {
      "p": "[CrossFormer: A Versatile Vision Transformer Hinging on Cross-scale Attention](https://arxiv.org/abs/2108.00154v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cheerss/CrossFormer)",
      "n": "CrossFormer (ImageNet1k-pretrain, UPerNet, multi-scale test)",
      "d": "2021-07-31",
      "m1": "51.4"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-B",
      "d": "2022-11-10",
      "m1": "51.3",
      "m3": "128",
      "m5": "1185"
    },
    {
      "p": "[DAT++: Spatially Dynamic Vision Transformer with Deformable Attention](https://arxiv.org/abs/2309.01430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-S++",
      "d": "2023-09-04",
      "m1": "51.2"
    },
    {
      "p": "[Active Token Mixer](https://arxiv.org/abs/2203.06108v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/TokenMixers)",
      "n": "ActiveMLP-L(UperNet)",
      "d": "2022-03-11",
      "m1": "51.1",
      "m3": "108"
    },
    {
      "p": "[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "SegFormer-B4",
      "d": "2021-05-31",
      "m1": "51.1",
      "m3": "64.1"
    },
    {
      "p": "[Augmenting Convolutional networks with attention-based aggregation](https://arxiv.org/abs/2112.13692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/deit)",
      "n": "PatchConvNet-B60 (UperNet)",
      "d": "2021-12-27",
      "m1": "51.1"
    },
    {
      "p": "[Is Attention Better Than Matrix Decomposition?](https://arxiv.org/abs/2109.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Gsunshine/Enjoy-Hamburger)",
      "n": "Light-Ham (VAN-Large)",
      "d": "2021-09-09",
      "m1": "51.0",
      "m3": "45.6",
      "m4": "55.0"
    },
    {
      "p": "[Towards Sustainable Self-supervised Learning](https://arxiv.org/abs/2210.11016v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sail-sg/tec)",
      "n": "TEC (Vit-B, Upernet)",
      "d": "2022-10-20",
      "m1": "51.0"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-S",
      "d": "2023-11-27",
      "m1": "51"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-B FPN)",
      "d": "2021-12-23",
      "m1": "50.98",
      "m3": "96"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-S",
      "d": "2022-11-10",
      "m1": "50.9",
      "m3": "80",
      "m5": "1017"
    },
    {
      "p": "[MogaNet: Multi-order Gated Aggregation Network](https://arxiv.org/abs/2211.03295v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/OpenSTL)",
      "n": "MogaNet-L (UperNet)",
      "d": "2022-11-07",
      "m1": "50.9",
      "m4": "1176"
    },
    {
      "p": "[Exploring Target Representations for Masked Autoencoders](https://arxiv.org/abs/2209.03917v3)",
      "c": "[&check;&nbsp;Link](https://github.com/liuxingbin/dbot)",
      "n": "dBOT ViT-B",
      "d": "2022-09-08",
      "m1": "50.8"
    },
    {
      "p": "[BiFormer: Vision Transformer with Bi-Level Routing Attention](https://arxiv.org/abs/2303.08810v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rayleizhu/biformer)",
      "n": "Upernet-BiFormer-S (IN1k pretrain, Upernet 160k)",
      "d": "2023-03-15",
      "m1": "50.8"
    },
    {
      "p": "[Shuffle Transformer: Rethinking Spatial Shuffle for Vision Transformer](https://arxiv.org/abs/2106.03650v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/EasyCV)",
      "n": "UperNet Shuffle-B",
      "d": "2021-06-07",
      "m1": "50.5"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V1-L",
      "d": "2023-01-02",
      "m1": "50.5"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-Base (UperNet)",
      "d": "2022-09-29",
      "m1": "50.4"
    },
    {
      "p": "[ELSA: Enhanced Local Self-Attention for Vision Transformer](https://arxiv.org/abs/2112.12786v1)",
      "c": "[&check;&nbsp;Link](https://github.com/damo-cv/elsa)",
      "n": "ELSA-Swin-S",
      "d": "2021-12-23",
      "m1": "50.3"
    },
    {
      "p": "[DAT++: Spatially Dynamic Vision Transformer with Deformable Attention](https://arxiv.org/abs/2309.01430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-T++",
      "d": "2023-09-04",
      "m1": "50.3"
    },
    {
      "p": "[Rethinking Semantic Segmentation from a Sequence-to-Sequence Perspective with Transformers](https://arxiv.org/abs/2012.15840v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "SETR-MLA (160k, MS)",
      "d": "2020-12-31",
      "m1": "50.28"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-Large (HamNet)",
      "d": "2022-02-20",
      "m1": "50.2",
      "m3": "55"
    },
    {
      "p": "[Multi-Scale High-Resolution Vision Transformer for Semantic Segmentation](https://arxiv.org/abs/2111.01236v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/HRViT)",
      "n": "HRViT-b3 (SegFormer, SS)",
      "d": "2021-11-01",
      "m1": "50.2",
      "m3": "28.7",
      "m4": "67.9"
    },
    {
      "p": "[Twins: Revisiting the Design of Spatial Attention in Vision Transformers](https://arxiv.org/abs/2104.13840v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "Twins-SVT-L (UperNet, ImageNet-1k pretrain)",
      "d": "2021-04-28",
      "m1": "50.2"
    },
    {
      "p": "[MogaNet: Multi-order Gated Aggregation Network](https://arxiv.org/abs/2211.03295v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/OpenSTL)",
      "n": "MogaNet-B (UperNet)",
      "d": "2022-11-07",
      "m1": "50.1",
      "m4": "1050"
    },
    {
      "p": "[Segmenter: Transformer for Semantic Segmentation](https://arxiv.org/abs/2105.05633v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "Seg-B-Mask/16(MS, ViT-B)",
      "d": "2021-05-12",
      "m1": "50.0"
    },
    {
      "p": "[iBOT: Image BERT Pre-Training with Online Tokenizer](https://arxiv.org/abs/2111.07832v3)",
      "c": "[&check;&nbsp;Link](https://github.com/bytedance/ibot)",
      "n": "iBOT (ViT-B/16)",
      "d": "2021-11-15",
      "m1": "50.0"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-B",
      "d": "2022-01-10",
      "m1": "49.9",
      "m3": "122",
      "m4": "1170"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-Small (UperNet)",
      "d": "2022-09-29",
      "m1": "49.9"
    },
    {
      "p": "[ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](https://arxiv.org/abs/2301.00808v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvNeXt V1-B",
      "d": "2023-01-02",
      "m1": "49.9"
    },
    {
      "p": "[Neighborhood Attention Transformer](https://arxiv.org/abs/2204.07143v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "NAT-Base",
      "d": "2022-04-14",
      "m1": "49.7",
      "m3": "123",
      "m4": "1137"
    },
    {
      "p": "[Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/abs/2103.14030v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Swin-B (UperNet, ImageNet-1k pretrain)",
      "d": "2021-03-25",
      "m1": "49.7"
    },
    {
      "p": "[Segmenter: Transformer for Semantic Segmentation](https://arxiv.org/abs/2105.05633v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "Seg-B/8 (MS, ViT-B)",
      "d": "2021-05-12",
      "m1": "49.61"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-S",
      "d": "2022-01-10",
      "m1": "49.6",
      "m3": "82",
      "m4": "1027"
    },
    {
      "p": "[Is Attention Better Than Matrix Decomposition?](https://arxiv.org/abs/2109.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Gsunshine/Enjoy-Hamburger)",
      "n": "Light-Ham (VAN-Base)",
      "d": "2021-09-09",
      "m1": "49.6",
      "m3": "27.4",
      "m4": "34.4"
    },
    {
      "p": "[Neighborhood Attention Transformer](https://arxiv.org/abs/2204.07143v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "NAT-Small",
      "d": "2022-04-14",
      "m1": "49.5",
      "m3": "82",
      "m4": "1010"
    },
    {
      "p": "[DaViT: Dual Attention Vision Transformers](https://arxiv.org/abs/2204.03645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "DaViT-B",
      "d": "2022-04-07",
      "m1": "49.4"
    },
    {
      "p": "[Vision Transformer with Deformable Attention](https://arxiv.org/abs/2201.00520v3)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-B (UperNet)",
      "d": "2022-01-03",
      "m1": "49.38",
      "m3": "121"
    },
    {
      "p": "[Augmenting Convolutional networks with attention-based aggregation](https://arxiv.org/abs/2112.13692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/deit)",
      "n": "PatchConvNet-S60 (UperNet)",
      "d": "2021-12-27",
      "m1": "49.3"
    },
    {
      "p": "[ColorMAE: Exploring data-independent masking strategies in Masked AutoEncoders](https://arxiv.org/abs/2407.13036v1)",
      "c": "[&check;&nbsp;Link](https://github.com/carlosh93/ColorMAE)",
      "n": "ColorMAE-Green-ViTB-1600",
      "d": "2024-07-17",
      "m1": "49.3"
    },
    {
      "p": "[MogaNet: Multi-order Gated Aggregation Network](https://arxiv.org/abs/2211.03295v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/OpenSTL)",
      "n": "MogaNet-S (UperNet)",
      "d": "2022-11-07",
      "m1": "49.2",
      "m4": "946"
    },
    {
      "p": "[When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism](https://arxiv.org/abs/2201.10801v1)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras-io/blob/master/examples/vision/shiftvit.py)",
      "n": "Shift-B (UperNet)",
      "d": "2022-01-26",
      "m1": "49.2"
    },
    {
      "p": "[UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ailab-cvc/unireplknet)",
      "n": "UniRepLKNet-T",
      "d": "2023-11-27",
      "m1": "49.1"
    },
    {
      "p": "[Vision Transformers for Dense Prediction](https://arxiv.org/abs/2103.13413v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DPT-Hybrid",
      "d": "2021-03-24",
      "m1": "49.02"
    },
    {
      "p": "[Global Context Vision Transformers](https://arxiv.org/abs/2206.09959v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "GC ViT-B",
      "d": "2022-06-20",
      "m1": "49",
      "m3": "125",
      "m4": "1348"
    },
    {
      "p": "[Architecture-Agnostic Masked Image Modeling -- From ViT back to CNN](https://arxiv.org/abs/2205.13943v4)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpretrain)",
      "n": "A2MIM (ViT-B)",
      "d": "2022-05-27",
      "m1": "49"
    },
    {
      "p": "[EfficientViT: Multi-Scale Linear Attention for High-Resolution Dense Prediction](https://arxiv.org/abs/2205.14756v6)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientViT-B3 (r512)",
      "d": "2022-05-29",
      "m1": "49"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-Tiny (UperNet)",
      "d": "2022-09-29",
      "m1": "48.8"
    },
    {
      "p": "[Multi-Scale High-Resolution Vision Transformer for Semantic Segmentation](https://arxiv.org/abs/2111.01236v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/HRViT)",
      "n": "HRViT-b2 (SegFormer, SS)",
      "d": "2021-11-01",
      "m1": "48.76",
      "m3": "20.8",
      "m4": "28.0"
    },
    {
      "p": "[Neighborhood Attention Transformer](https://arxiv.org/abs/2204.07143v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "NAT-Tiny",
      "d": "2022-04-14",
      "m1": "48.4",
      "m3": "58",
      "m4": "934"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-M24/8 (UperNet)",
      "d": "2021-06-17",
      "m1": "48.4"
    },
    {
      "p": "[ResNeSt: Split-Attention Networks](https://arxiv.org/abs/2004.08955v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNeSt-200",
      "d": "2020-04-19",
      "m1": "48.36"
    },
    {
      "p": "[Vision Transformer with Deformable Attention](https://arxiv.org/abs/2201.00520v3)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-S (UperNet)",
      "d": "2022-01-03",
      "m1": "48.31",
      "m3": "81"
    },
    {
      "p": "[Global Context Vision Transformers](https://arxiv.org/abs/2206.09959v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "GC ViT-S",
      "d": "2022-06-20",
      "m1": "48.3",
      "m3": "84",
      "m4": "1163"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-T",
      "d": "2022-11-10",
      "m1": "48.1",
      "m3": "59",
      "m5": "944"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-Large",
      "d": "2022-02-20",
      "m1": "48.1",
      "m3": "49"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-S24/8 (UperNet)",
      "d": "2021-06-17",
      "m1": "48.1"
    },
    {
      "p": "[Per-Pixel Classification is Not All You Need for Semantic Segmentation](https://arxiv.org/abs/2107.06278v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "MaskFormer(ResNet-101)",
      "d": "2021-07-13",
      "m1": "48.1"
    },
    {
      "p": "[Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/mae)",
      "n": "MAE (ViT-B, UperNet)",
      "d": "2021-11-11",
      "m1": "48.1"
    },
    {
      "p": "[Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation](https://arxiv.org/abs/1909.11065v6)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "HRNetV2 + OCR + RMI (PaddleClas pretrained)",
      "d": "2019-09-24",
      "m1": "47.98"
    },
    {
      "p": "[When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism](https://arxiv.org/abs/2201.10801v1)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras-io/blob/master/examples/vision/shiftvit.py)",
      "n": "Shift-B",
      "d": "2022-01-26",
      "m1": "47.9"
    },
    {
      "p": "[When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism](https://arxiv.org/abs/2201.10801v1)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras-io/blob/master/examples/vision/shiftvit.py)",
      "n": "Shift-S",
      "d": "2022-01-26",
      "m1": "47.8"
    },
    {
      "p": "[MogaNet: Multi-order Gated Aggregation Network](https://arxiv.org/abs/2211.03295v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chengtan9907/OpenSTL)",
      "n": "MogaNet-S (Semantic FPN)",
      "d": "2022-11-07",
      "m1": "47.7",
      "m4": "189"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-S FPN)",
      "d": "2021-12-23",
      "m1": "47.63",
      "m3": "56"
    },
    {
      "p": "[ResNeSt: Split-Attention Networks](https://arxiv.org/abs/2004.08955v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNeSt-269",
      "d": "2020-04-19",
      "m1": "47.60"
    },
    {
      "p": "[Shuffle Transformer: Rethinking Spatial Shuffle for Vision Transformer](https://arxiv.org/abs/2106.03650v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/EasyCV)",
      "n": "UperNet Shuffle-T",
      "d": "2021-06-07",
      "m1": "47.6"
    },
    {
      "p": "[CondNet: Conditional Classifier for Scene Segmentation](https://arxiv.org/abs/2109.10322v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sithu31296/semantic-segmentation)",
      "n": "CondNet(ResNest-101)",
      "d": "2021-09-21",
      "m1": "47.54"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "tiny-MOAT-3 (IN-1K pretraining, single scale)",
      "d": "2022-10-04",
      "m1": "47.5",
      "m3": "24"
    },
    {
      "p": "[CondNet: Conditional Classifier for Scene Segmentation](https://arxiv.org/abs/2109.10322v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sithu31296/semantic-segmentation)",
      "n": "CondNet(ResNet-101)",
      "d": "2021-09-21",
      "m1": "47.38"
    },
    {
      "p": "[Dilated Neighborhood Attention Transformer](https://arxiv.org/abs/2209.15001v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DiNAT-Mini (UperNet)",
      "d": "2022-09-29",
      "m1": "47.2"
    },
    {
      "p": "[DCNAS: Densely Connected Neural Architecture Search for Semantic Image Segmentation](https://arxiv.org/abs/2003.11883v2)",
      "c": "",
      "n": "DCNAS",
      "d": "2020-03-26",
      "m1": "47.12"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-S24/8 (Semantic-FPN)",
      "d": "2021-06-17",
      "m1": "47.1"
    },
    {
      "p": "[ResNeSt: Split-Attention Networks](https://arxiv.org/abs/2004.08955v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNeSt-101",
      "d": "2020-04-19",
      "m1": "46.91"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-M24/8 (Semantic-FPN)",
      "d": "2021-06-17",
      "m1": "46.9"
    },
    {
      "p": "[Is Attention Better Than Matrix Decomposition?](https://arxiv.org/abs/2109.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Gsunshine/Enjoy-Hamburger)",
      "n": "HamNet (ResNet-101)",
      "d": "2021-09-09",
      "m1": "46.8"
    },
    {
      "p": "[Sequential Ensembling for Semantic Segmentation](https://arxiv.org/abs/2210.05387v1)",
      "c": "",
      "n": "Sequential Ensemble (DeepLabv3+)",
      "d": "2022-10-08",
      "m1": "46.8"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-T",
      "d": "2022-01-10",
      "m1": "46.7",
      "m3": "60",
      "m4": "939"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-Base (Semantic-FPN)",
      "d": "2022-02-20",
      "m1": "46.7"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-S12/8 (UperNet)",
      "d": "2021-06-17",
      "m1": "46.6"
    },
    {
      "p": "[Global Context Vision Transformers](https://arxiv.org/abs/2206.09959v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "GC ViT-T",
      "d": "2022-06-20",
      "m1": "46.5",
      "m3": "58",
      "m4": "947"
    },
    {
      "p": "[Neighborhood Attention Transformer](https://arxiv.org/abs/2204.07143v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "NAT-Mini",
      "d": "2022-04-14",
      "m1": "46.4",
      "m3": "50",
      "m4": "900"
    },
    {
      "p": "[When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism](https://arxiv.org/abs/2201.10801v1)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras-io/blob/master/examples/vision/shiftvit.py)",
      "n": "Shift-T",
      "d": "2022-01-26",
      "m1": "46.3"
    },
    {
      "p": "[DaViT: Dual Attention Vision Transformers](https://arxiv.org/abs/2204.03645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "DaViT-T",
      "d": "2022-04-07",
      "m1": "46.3"
    },
    {
      "p": "[Context Prior for Scene Segmentation](https://arxiv.org/abs/2004.01547v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ycszen/ContextPrior)",
      "n": "CPN(ResNet-101)",
      "d": "2020-04-03",
      "m1": "46.27"
    },
    {
      "p": "[MultiMAE: Multi-modal Multi-task Masked Autoencoders](https://arxiv.org/abs/2204.01678v1)",
      "c": "[&check;&nbsp;Link](https://github.com/EPFL-VILAB/MultiMAE)",
      "n": "MultiMAE (ViT-B)",
      "d": "2022-04-04",
      "m1": "46.2"
    },
    {
      "p": "[Scene Segmentation with Dual Relation-aware Attention Network](https://ieeexplore.ieee.org/document/9154612)",
      "c": "[&check;&nbsp;Link](https://github.com/junfu1115/DRAN)",
      "n": "DRAN(ResNet-101)",
      "d": "2020-08-05",
      "m1": "46.18"
    },
    {
      "p": "[Pyramidal Convolution: Rethinking Convolutional Neural Networks for Visual Recognition](https://arxiv.org/abs/2006.11538v1)",
      "c": "[&check;&nbsp;Link](https://github.com/iduta/pyconv)",
      "n": "PyConvSegNet-152",
      "d": "2020-06-20",
      "m1": "45.99",
      "m2": "56.52"
    },
    {
      "p": "[Disentangled Non-Local Neural Networks](https://arxiv.org/abs/2006.06668v2)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "DNL",
      "d": "2020-06-11",
      "m1": "45.97"
    },
    {
      "p": "[Adaptive Context Network for Scene Parsing](https://arxiv.org/abs/1911.01664v1)",
      "c": "",
      "n": "ACNet (ResNet-101)",
      "d": "2019-11-05",
      "m1": "45.90"
    },
    {
      "p": "[Adaptive Context Network for Scene Parsing](https://arxiv.org/abs/1911.01664v1)",
      "c": "",
      "n": "ACNet\n(ResNet-101)",
      "d": "2019-11-05",
      "m1": "45.90"
    },
    {
      "p": "[Multi-Scale High-Resolution Vision Transformer for Semantic Segmentation](https://arxiv.org/abs/2111.01236v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/HRViT)",
      "n": "HRViT-b1 (SegFormer, SS)",
      "d": "2021-11-01",
      "m1": "45.88",
      "m3": "8.2",
      "m4": "14.6"
    },
    {
      "p": "[Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation](https://arxiv.org/abs/1909.11065v6)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "OCR(HRNetV2-W48)",
      "d": "2019-09-24",
      "m1": "45.66"
    },
    {
      "p": "[Strip Pooling: Rethinking Spatial Pooling for Scene Parsing](https://arxiv.org/abs/2003.13328v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Andrew-Qibin/SPNet)",
      "n": "SPNet (ResNet-101)",
      "d": "2020-03-30",
      "m1": "45.6"
    },
    {
      "p": "[Self-Supervised Learning with Swin Transformers](https://arxiv.org/abs/2105.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/Swin-Transformer)",
      "n": "Swin-T (UPerNet) MoBY",
      "d": "2021-05-10",
      "m1": "45.58"
    },
    {
      "p": "[Vision Transformer with Deformable Attention](https://arxiv.org/abs/2201.00520v3)",
      "c": "[&check;&nbsp;Link](https://github.com/leaplabthu/dat)",
      "n": "DAT-T (UperNet)",
      "d": "2022-01-03",
      "m1": "45.54",
      "m3": "60"
    },
    {
      "p": "[iBOT: Image BERT Pre-Training with Online Tokenizer](https://arxiv.org/abs/2111.07832v3)",
      "c": "[&check;&nbsp;Link](https://github.com/bytedance/ibot)",
      "n": "iBOT (ViT-S/16)",
      "d": "2021-11-15",
      "m1": "45.4"
    },
    {
      "p": "[Beyond Self-attention: External Attention using Two Linear Layers for Visual Tasks](https://arxiv.org/abs/2105.02358v2)",
      "c": "[&check;&nbsp;Link](https://github.com/xmu-xiaoma666/External-Attention-pytorch)",
      "n": "EANet\n(ResNet-101)",
      "d": "2021-05-05",
      "m1": "45.33"
    },
    {
      "p": "[Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation](https://arxiv.org/abs/1909.11065v6)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "OCR (ResNet-101)",
      "d": "2019-09-24",
      "m1": "45.28"
    },
    {
      "p": "[Asymmetric Non-local Neural Networks for Semantic Segmentation](https://arxiv.org/abs/1908.07678v5)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "Asymmetric ALNN",
      "d": "2019-08-21",
      "m1": "45.24"
    },
    {
      "p": "[Is Attention Better Than Matrix Decomposition?](https://arxiv.org/abs/2109.04553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Gsunshine/Enjoy-Hamburger)",
      "n": "Light-Ham (VAN-Small, D=256)",
      "d": "2021-09-09",
      "m1": "45.2",
      "m3": "13.8",
      "m4": "15.8"
    },
    {
      "p": "[Location-aware Upsampling for Semantic Segmentation](https://arxiv.org/abs/1911.05250v2)",
      "c": "[&check;&nbsp;Link](https://github.com/HolmesShuan/Location-aware-Upsampling-for-Semantic-Segmentation)",
      "n": "LaU-regression-loss",
      "d": "2019-11-13",
      "m1": "45.02",
      "m2": "56.32"
    },
    {
      "p": "[Pyramid Scene Parsing Network](http://arxiv.org/abs/1612.01105v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "PSPNet",
      "d": "2016-12-04",
      "m1": "44.94",
      "m2": "55.38"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "tiny-MOAT-2 (IN-1K pretraining, single scale)",
      "d": "2022-10-04",
      "m1": "44.9",
      "m3": "13"
    },
    {
      "p": "[Co-Occurrent Features in Semantic Segmentation](http://openaccess.thecvf.com/content_CVPR_2019/html/Zhang_Co-Occurrent_Features_in_Semantic_Segmentation_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/zhanghang1989/PyTorch-Encoding)",
      "n": "CFNet(ResNet-101)",
      "d": "2019-06-01",
      "m1": "44.89"
    },
    {
      "p": "[Context Encoding for Semantic Segmentation](http://arxiv.org/abs/1803.08904v1)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "EncNet",
      "d": "2018-03-23",
      "m1": "44.65",
      "m2": "55.67"
    },
    {
      "p": "[Location-aware Upsampling for Semantic Segmentation](https://arxiv.org/abs/1911.05250v2)",
      "c": "[&check;&nbsp;Link](https://github.com/HolmesShuan/Location-aware-Upsampling-for-Semantic-Segmentation)",
      "n": "LaU-offset-loss",
      "d": "2019-11-13",
      "m1": "44.55",
      "m2": "56.41"
    },
    {
      "p": "[FastFCN: Rethinking Dilated Convolution in the Backbone for Semantic Segmentation](http://arxiv.org/abs/1903.11816v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "EncNet + JPU",
      "d": "2019-03-28",
      "m1": "44.34",
      "m2": "55.84"
    },
    {
      "p": "[Symbolic Graph Reasoning Meets Convolutions](http://papers.nips.cc/paper/7456-symbolic-graph-reasoning-meets-convolutions)",
      "c": "[&check;&nbsp;Link](https://github.com/julianschoep/SGRLayer)",
      "n": "SGR (ResNet-101)",
      "d": "2018-12-01",
      "m1": "44.32"
    },
    {
      "p": "[XCiT: Cross-Covariance Image Transformers](https://arxiv.org/abs/2106.09681v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "XCiT-S12/8 (Semantic-FPN)",
      "d": "2021-06-17",
      "m1": "44.2"
    },
    {
      "p": "[Auto-DeepLab: Hierarchical Neural Architecture Search for Semantic Image Segmentation](http://arxiv.org/abs/1901.02985v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "Auto-DeepLab-L",
      "d": "2019-01-10",
      "m1": "43.98"
    },
    {
      "p": "[PSANet: Point-wise Spatial Attention Network for Scene Parsing](http://openaccess.thecvf.com/content_ECCV_2018/html/Hengshuang_Zhao_PSANet_Point-wise_Spatial_ECCV_2018_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "PSANet (ResNet-101)",
      "d": "2018-09-01",
      "m1": "43.77"
    },
    {
      "p": "[Dynamic-structured Semantic Propagation Network](http://arxiv.org/abs/1803.06067v1)",
      "c": "",
      "n": "DSSPN (ResNet-101)",
      "d": "2018-03-16",
      "m1": "43.68"
    },
    {
      "p": "[Pyramid Scene Parsing Network](http://arxiv.org/abs/1612.01105v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "PSPNet (ResNet-152)",
      "d": "2016-12-04",
      "m1": "43.51"
    },
    {
      "p": "[Pyramid Scene Parsing Network](http://arxiv.org/abs/1612.01105v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "PSPNet\n(ResNet-101)",
      "d": "2016-12-04",
      "m1": "43.29"
    },
    {
      "p": "[High-Resolution Representations for Labeling Pixels and Regions](http://arxiv.org/abs/1904.04514v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleDetection)",
      "n": "HRNetV2",
      "d": "2019-04-09",
      "m1": "43.2"
    },
    {
      "p": "[SeMask: Semantically Masked Transformers for Semantic Segmentation](https://arxiv.org/abs/2112.12782v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Picsart-AI-Research/SeMask-Segmentation)",
      "n": "SeMask (SeMask Swin-T FPN)",
      "d": "2021-12-23",
      "m1": "43.16",
      "m3": "35"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "tiny-MOAT-1 (IN-1K pretraining, single scale)",
      "d": "2022-10-04",
      "m1": "43.1",
      "m3": "8"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-Small",
      "d": "2022-02-20",
      "m1": "42.9",
      "m3": "18"
    },
    {
      "p": "[MetaFormer Is Actually What You Need for Vision](https://arxiv.org/abs/2111.11418v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "PoolFormer-M48",
      "d": "2021-11-22",
      "m1": "42.7"
    },
    {
      "p": "[Unified Perceptual Parsing for Scene Understanding](http://arxiv.org/abs/1807.10221v1)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "UperNet (ResNet-101)",
      "d": "2018-07-26",
      "m1": "42.66"
    },
    {
      "p": "[MOAT: Alternating Mobile Convolution and Attention Brings Strong Vision Models](https://arxiv.org/abs/2210.01820v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/deeplab2)",
      "n": "tiny-MOAT-0 (IN-1K pretraining, single scale)",
      "d": "2022-10-04",
      "m1": "41.2",
      "m3": "6"
    },
    {
      "p": "[RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation](http://arxiv.org/abs/1611.06612v3)",
      "c": "[&check;&nbsp;Link](https://github.com/guosheng/refinenet)",
      "n": "RefineNet",
      "d": "2016-11-20",
      "m1": "40.7"
    },
    {
      "p": "[FBNetV5: Neural Architecture Search for Multiple Tasks in One Run](https://arxiv.org/abs/2111.10007v3)",
      "c": "",
      "n": "FBNetV5",
      "d": "2021-11-19",
      "m1": "40.4"
    },
    {
      "p": "[ConvMLP: Hierarchical Convolutional MLPs for Vision](https://arxiv.org/abs/2109.04454v2)",
      "c": "[&check;&nbsp;Link](https://github.com/BR-IDL/PaddleViT/tree/develop/image_classification)",
      "n": "ConvMLP-L",
      "d": "2021-09-09",
      "m1": "40"
    },
    {
      "p": "[ConvMLP: Hierarchical Convolutional MLPs for Vision](https://arxiv.org/abs/2109.04454v2)",
      "c": "[&check;&nbsp;Link](https://github.com/BR-IDL/PaddleViT/tree/develop/image_classification)",
      "n": "ConvMLP-M",
      "d": "2021-09-09",
      "m1": "38.6"
    },
    {
      "p": "[Visual Attention Network](https://arxiv.org/abs/2202.09741v5)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "VAN-Tiny",
      "d": "2022-02-20",
      "m1": "38.5",
      "m3": "8"
    },
    {
      "p": "[Architecture-Agnostic Masked Image Modeling -- From ViT back to CNN](https://arxiv.org/abs/2205.13943v4)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmpretrain)",
      "n": "A2MIM (ResNet-50)",
      "d": "2022-05-27",
      "m1": "38.3"
    },
    {
      "p": "[iBOT: Image BERT Pre-Training with Online Tokenizer](https://arxiv.org/abs/2111.07832v3)",
      "c": "[&check;&nbsp;Link](https://github.com/bytedance/ibot)",
      "n": "iBOT (ViT-B/16) (linear head)",
      "d": "2021-11-15",
      "m1": "38.3"
    },
    {
      "p": "[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "SegFormer-B0",
      "d": "2021-05-31",
      "m1": "37.4",
      "m3": "3.8"
    },
    {
      "p": "[MUXConv: Information Multiplexing in Convolutional Neural Networks](https://arxiv.org/abs/2003.13880v2)",
      "c": "[&check;&nbsp;Link](https://github.com/human-analysis/MUXConv)",
      "n": "MUXNet-m + PPM",
      "d": "2020-03-31",
      "m1": "35.8"
    },
    {
      "p": "[ConvMLP: Hierarchical Convolutional MLPs for Vision](https://arxiv.org/abs/2109.04454v2)",
      "c": "[&check;&nbsp;Link](https://github.com/BR-IDL/PaddleViT/tree/develop/image_classification)",
      "n": "ConvMLP-S",
      "d": "2021-09-09",
      "m1": "35.8"
    },
    {
      "p": "[MUXConv: Information Multiplexing in Convolutional Neural Networks](https://arxiv.org/abs/2003.13880v2)",
      "c": "[&check;&nbsp;Link](https://github.com/human-analysis/MUXConv)",
      "n": "MUXNet-m + C1",
      "d": "2020-03-31",
      "m1": "32.42"
    },
    {
      "p": "[Multi-Scale Context Aggregation by Dilated Convolutions](http://arxiv.org/abs/1511.07122v3)",
      "c": "[&check;&nbsp;Link](https://github.com/fyu/dilation)",
      "n": "DilatedNet",
      "d": "2015-11-23",
      "m1": "32.31"
    },
    {
      "p": "[Fully Convolutional Networks for Semantic Segmentation](http://arxiv.org/abs/1411.4038v2)",
      "c": "[&check;&nbsp;Link](https://github.com/pochih/fcn-pytorch)",
      "n": "FCN",
      "d": "2014-11-14",
      "m1": "29.39"
    },
    {
      "p": "[SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](http://arxiv.org/abs/1511.00561v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "SegNet",
      "d": "2015-11-02",
      "m1": "21.64"
    },
    {
      "p": "[InternImage: Exploring Large-Scale Vision Foundation Models with Deformable Convolutions](https://arxiv.org/abs/2211.05778v4)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/internimage)",
      "n": "InternImage-H (M3I Pre-training)",
      "d": "2022-11-10",
      "m3": "1310"
    },
    {
      "p": "[FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization](https://arxiv.org/abs/2303.14189v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "FastViT-MA36",
      "d": "2023-03-24",
      "m6": "44.6"
    },
    {
      "p": "[FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization](https://arxiv.org/abs/2303.14189v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "FastViT-SA36",
      "d": "2023-03-24",
      "m6": "42.9"
    },
    {
      "p": "[FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization](https://arxiv.org/abs/2303.14189v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "FastViT-SA24",
      "d": "2023-03-24",
      "m6": "41"
    },
    {
      "p": "[FastViT: A Fast Hybrid Vision Transformer using Structural Reparameterization](https://arxiv.org/abs/2303.14189v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "FastViT-SA12",
      "d": "2023-03-24",
      "m6": "38"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
