# efficient-vits-on-imagenet-1k-with-lv-vit-s

[Dataset Link]() \
Task Hierarchy: ['Image Classification', 'Efficient ViTs']

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
      "label": "Top 1 Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "GFLOPs",
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
      "p": "[Multi-criteria Token Fusion with One-step-ahead Attention for Efficient Vision Transformers](https://arxiv.org/abs/2403.10030v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/mctf)",
      "n": "MCTF ($r=8$)",
      "d": "2024-03-15",
      "m1": "83.5",
      "m2": "4.9"
    },
    {
      "p": "[Multi-criteria Token Fusion with One-step-ahead Attention for Efficient Vision Transformers](https://arxiv.org/abs/2403.10030v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/mctf)",
      "n": "MCTF ($r=12$)",
      "d": "2024-03-15",
      "m1": "83.4",
      "m2": "4.2"
    },
    {
      "p": "[All Tokens Matter: Token Labeling for Training Better Vision Transformers](https://arxiv.org/abs/2104.10858v3)",
      "c": "[&check;&nbsp;Link](https://github.com/zihangJiang/TokenLabeling)",
      "n": "Base (LV-ViT-S)",
      "d": "2021-04-22",
      "m1": "83.3",
      "m2": "6.6"
    },
    {
      "p": "[DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification](https://arxiv.org/abs/2106.02034v2)",
      "c": "[&check;&nbsp;Link](https://github.com/raoyongming/DynamicViT)",
      "n": "DynamicViT (90%)",
      "d": "2021-06-03",
      "m1": "83.3",
      "m2": "5.8"
    },
    {
      "p": "[DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification](https://arxiv.org/abs/2106.02034v2)",
      "c": "[&check;&nbsp;Link](https://github.com/raoyongming/DynamicViT)",
      "n": "DynamicViT (80%)",
      "d": "2021-06-03",
      "m1": "83.2",
      "m2": "5.1"
    },
    {
      "p": "[Beyond Attentive Tokens: Incorporating Token Importance and Diversity for Efficient Vision Transformers](https://arxiv.org/abs/2211.11315v1)",
      "c": "[&check;&nbsp;Link](https://github.com/BWLONG/BeyondAttentiveTokens)",
      "n": "BAT",
      "d": "2022-11-21",
      "m1": "83.1",
      "m2": "4.7"
    },
    {
      "p": "[Adaptive Sparse ViT: Towards Learnable Adaptive Token Pruning by Fully Exploiting Self-Attention](https://arxiv.org/abs/2209.13802v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cydia2018/as-vit)",
      "n": "AS-LV-S (70%)",
      "d": "2022-09-28",
      "m1": "83.1",
      "m2": "4.6"
    },
    {
      "p": "[PPT: Token Pruning and Pooling for Efficient Vision Transformers](https://arxiv.org/abs/2310.01812v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mindspore-lab/models)",
      "n": "PPT",
      "d": "2023-10-03",
      "m1": "83.1",
      "m2": "4.6"
    },
    {
      "p": "[SPViT: Enabling Faster Vision Transformers via Soft Token Pruning](https://arxiv.org/abs/2112.13890v2)",
      "c": "[&check;&nbsp;Link](https://github.com/peiyanflying/spvit)",
      "n": "SPViT",
      "d": "2021-12-27",
      "m1": "83.1",
      "m2": "4.3"
    },
    {
      "p": "[Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations](https://arxiv.org/abs/2202.07800v2)",
      "c": "[&check;&nbsp;Link](https://github.com/youweiliang/evit)",
      "n": "EViT (70%)",
      "d": "2022-02-16",
      "m1": "83.0",
      "m2": "4.7"
    },
    {
      "p": "[DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification](https://arxiv.org/abs/2106.02034v2)",
      "c": "[&check;&nbsp;Link](https://github.com/raoyongming/DynamicViT)",
      "n": "DynamicViT (70%)",
      "d": "2021-06-03",
      "m1": "83.0",
      "m2": "4.6"
    },
    {
      "p": "[Patch Slimming for Efficient Vision Transformers](https://arxiv.org/abs/2106.02852v2)",
      "c": "",
      "n": "DPS-LV-ViT-S",
      "d": "2021-06-05",
      "m1": "82.9",
      "m2": "4.5"
    },
    {
      "p": "[DiffRate : Differentiable Compression Rate for Efficient Vision Transformers](https://arxiv.org/abs/2305.17997v1)",
      "c": "[&check;&nbsp;Link](https://github.com/opengvlab/diffrate)",
      "n": "DiffRate",
      "d": "2023-05-29",
      "m1": "82.6",
      "m2": "3.9"
    },
    {
      "p": "[Adaptive Sparse ViT: Towards Learnable Adaptive Token Pruning by Fully Exploiting Self-Attention](https://arxiv.org/abs/2209.13802v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cydia2018/as-vit)",
      "n": "AS-LV-S (60%)",
      "d": "2022-09-28",
      "m1": "82.6",
      "m2": "3.9"
    },
    {
      "p": "[Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers](https://arxiv.org/abs/2304.10716v1)",
      "c": "[&check;&nbsp;Link](https://github.com/megvii-research/tps-cvpr2023)",
      "n": "dTPS",
      "d": "2023-04-21",
      "m1": "82.6",
      "m2": "3.8"
    },
    {
      "p": "[Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations](https://arxiv.org/abs/2202.07800v2)",
      "c": "[&check;&nbsp;Link](https://github.com/youweiliang/evit)",
      "n": "EViT (50%)",
      "d": "2022-02-16",
      "m1": "82.5",
      "m2": "3.9"
    },
    {
      "p": "[Joint Token Pruning and Squeezing Towards More Aggressive Compression of Vision Transformers](https://arxiv.org/abs/2304.10716v1)",
      "c": "[&check;&nbsp;Link](https://github.com/megvii-research/tps-cvpr2023)",
      "n": "eTPS",
      "d": "2023-04-21",
      "m1": "82.5",
      "m2": "3.8"
    },
    {
      "p": "[Patch Slimming for Efficient Vision Transformers](https://arxiv.org/abs/2106.02852v2)",
      "c": "",
      "n": "PS-LV-ViT-S",
      "d": "2021-06-05",
      "m1": "82.4",
      "m2": "4.7"
    },
    {
      "p": "[Multi-criteria Token Fusion with One-step-ahead Attention for Efficient Vision Transformers](https://arxiv.org/abs/2403.10030v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/mctf)",
      "n": "MCTF ($r=16$)",
      "d": "2024-03-15",
      "m1": "82.3",
      "m2": "3.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
