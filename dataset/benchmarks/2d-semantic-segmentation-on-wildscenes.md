# 2d-semantic-segmentation-on-wildscenes

[Dataset Link](https://csiro-robotics.github.io/WildScenes/) \
Task Hierarchy: ['2D Semantic Segmentation']

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
      "label": "mIoU",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "mIoU (Temporal DA) ",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "mIoU (Env DA)",
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
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former (Swin-L)",
      "d": "2021-12-02",
      "m1": "47.85"
    },
    {
      "p": "[Unified Perceptual Parsing for Scene Understanding](http://arxiv.org/abs/1807.10221v1)",
      "c": "[&check;&nbsp;Link](https://github.com/open-mmlab/mmsegmentation)",
      "n": "UPerNet (ConvNeXt-L)",
      "d": "2018-07-26",
      "m1": "47.30"
    },
    {
      "p": "[Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Mask2Former (ResNet-50)",
      "d": "2021-12-02",
      "m1": "43.71"
    },
    {
      "p": "[Rethinking Atrous Convolution for Semantic Image Segmentation](http://arxiv.org/abs/1706.05587v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "DeepLabv3 (ResNet-50)",
      "d": "2017-06-17",
      "m1": "43.37",
      "m2": "43.95",
      "m3": "36.12"
    },
    {
      "p": "[SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers](https://arxiv.org/abs/2105.15203v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Segformer (MiT-B5)",
      "d": "2021-05-31",
      "m1": "40.83"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
