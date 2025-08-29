# domain-generalization-on-imagenet-sketch

[Dataset Link](https://github.com/HaohanWang/ImageNet-Sketch) \
Task Hierarchy: ['Domain Generalization']

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
      "label": "Top-1 accuracy",
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
      "p": "[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlfoundations/model-soups)",
      "n": "Model soups (BASIC-L)",
      "d": "2022-03-10",
      "m1": "77.18"
    },
    {
      "p": "[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mlfoundations/model-soups)",
      "n": "Model soups (ViT-G/14)",
      "d": "2022-03-10",
      "m1": "74.24"
    },
    {
      "p": "[Context-Aware Robust Fine-Tuning](https://arxiv.org/abs/2211.16175v1)",
      "c": "",
      "n": "CAR-FT (CLIP, ViT-L/14@336px)",
      "d": "2022-11-29",
      "m1": "65.5"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-XL (Im21k, 384)",
      "d": "2022-01-10",
      "m1": "55.0"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "CAFormer-B36 (IN21K, 384)",
      "d": "2022-10-24",
      "m1": "54.5"
    },
    {
      "p": "[A Whac-A-Mole Dilemma: Shortcuts Come in Multiples Where Mitigating One Amplifies Others](https://arxiv.org/abs/2212.04825v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/Whac-A-Mole)",
      "n": "LLE (ViT-H/14, MAE, Edge Aug)",
      "d": "2022-12-09",
      "m1": "53.39"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvFormer-B36 (IN21K, 384)",
      "d": "2022-10-24",
      "m1": "52.9"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "CAFormer-B36 (IN21K)",
      "d": "2022-10-24",
      "m1": "52.8"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvFormer-B36 (IN21K)",
      "d": "2022-10-24",
      "m1": "52.7"
    },
    {
      "p": "[Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/mae)",
      "n": "MAE (ViT-H, 448)",
      "d": "2021-11-11",
      "m1": "50.9"
    },
    {
      "p": "[Enhance the Visual Representation via Discrete Adversarial Training](https://arxiv.org/abs/2209.07735v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/easyrobust/tree/main/examples/imageclassification/imagenet/dat)",
      "n": "MAE+DAT (ViT-H)",
      "d": "2022-09-16",
      "m1": "50.03"
    },
    {
      "p": "[Generalized Parametric Contrastive Learning](https://arxiv.org/abs/2209.12400v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dvlab-research/parametric-contrastive-learning)",
      "n": "GPaCo (ViT-L)",
      "d": "2022-09-26",
      "m1": "48.3"
    },
    {
      "p": "[Distilling Out-of-Distribution Robustness from Vision-Language Foundation Models](https://arxiv.org/abs/2311.01441v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lapisrocks/DiscreteAdversarialDistillation)",
      "n": "Discrete Adversarial Distillation (ViT-B, 224)",
      "d": "2023-11-02",
      "m1": "46.1"
    },
    {
      "p": "[Pyramid Adversarial Training Improves ViT Performance](https://arxiv.org/abs/2111.15121v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/adversarialtraining)",
      "n": "Pyramid Adversarial Training Improves ViT (Im21k)",
      "d": "2021-11-30",
      "m1": "46.03"
    },
    {
      "p": "[Vision Models Are More Robust And Fair When Pretrained On Uncurated Images Without Supervision](https://arxiv.org/abs/2202.08360v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/vissl)",
      "n": "SEER (RegNet10B)",
      "d": "2022-02-16",
      "m1": "45.6"
    },
    {
      "p": "[Discrete Representations Strengthen Vision Transformer Robustness](https://arxiv.org/abs/2111.10493v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/easyrobust/tree/main/examples/imageclassification/imagenet/drvit)",
      "n": "DrViT",
      "d": "2021-11-20",
      "m1": "44.72"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "CAFormer-B36",
      "d": "2022-10-24",
      "m1": "42.5"
    },
    {
      "p": "[Pyramid Adversarial Training Improves ViT Performance](https://arxiv.org/abs/2111.15121v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/adversarialtraining)",
      "n": "Pyramid Adversarial Training Improves ViT",
      "d": "2021-11-30",
      "m1": "41.04"
    },
    {
      "p": "[MetaFormer Baselines for Vision](https://arxiv.org/abs/2210.13452v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ConvFormer-B36",
      "d": "2022-10-24",
      "m1": "39.5"
    },
    {
      "p": "[Sequencer: Deep LSTM for Image Classification](https://arxiv.org/abs/2205.01972v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "Sequencer2D-L",
      "d": "2022-05-04",
      "m1": "35.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
