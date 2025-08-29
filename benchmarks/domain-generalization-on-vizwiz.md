# domain-generalization-on-vizwiz

[Dataset Link](https://vizwiz.org/tasks-and-datasets/image-classification/) \
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
      "label": "Accuracy - All Images",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy - Corrupted Images",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Accuracy - Clean Images",
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
      "p": "[VOLO: Vision Outlooker for Visual Recognition](https://arxiv.org/abs/2106.13112v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VOLO-D5",
      "d": "2021-06-24",
      "m1": "57.2",
      "m2": "51.8",
      "m3": "59.7"
    },
    {
      "p": "[A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545v2)",
      "c": "[&check;&nbsp;Link](https://github.com/keras-team/keras/blob/master/keras/applications/convnext.py)",
      "n": "ConvNeXt-B",
      "d": "2022-01-10",
      "m1": "53.5",
      "m2": "46.9",
      "m3": "56"
    },
    {
      "p": "[Aggregated Residual Transformations for Deep Neural Networks](http://arxiv.org/abs/1611.05431v2)",
      "c": "[&check;&nbsp;Link](https://github.com/pytorch/vision)",
      "n": "ResNeXt-101 32x16d",
      "d": "2016-11-16",
      "m1": "51.7",
      "m2": "48.1",
      "m3": "54.8"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B8 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "50.5",
      "m2": "45.8",
      "m3": "53.2"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B7 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "49.7",
      "m2": "45",
      "m3": "52"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B6 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "49.6",
      "m2": "44.7",
      "m3": "53.2"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B5 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "49.1",
      "m2": "44",
      "m3": "51.7"
    },
    {
      "p": "[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ViT-16/L-224",
      "d": "2020-10-22",
      "m1": "49"
    },
    {
      "p": "[ResNet strikes back: An improved training procedure in timm](https://arxiv.org/abs/2110.00476v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-50 (gn)",
      "d": "2021-10-01",
      "m1": "48.9",
      "m2": "39.1",
      "m3": "44.4"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B4 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "48.1",
      "m2": "42.5",
      "m3": "51.4"
    },
    {
      "p": "[Deep Residual Learning for Image Recognition](http://arxiv.org/abs/1512.03385v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/deeplab)",
      "n": "ResNet-152",
      "d": "2015-12-10",
      "m1": "47.5",
      "m2": "43.3",
      "m3": "51.3"
    },
    {
      "p": "[Deep Residual Learning for Image Recognition](http://arxiv.org/abs/1512.03385v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/deeplab)",
      "n": "ResNet-101",
      "d": "2015-12-10",
      "m1": "46.3",
      "m2": "40.5",
      "m3": "50.1"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Strategies From Data](http://openaccess.thecvf.com/content_CVPR_2019/html/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/mindspore-ai/models/blob/master/research/cv/autoaugment)",
      "n": "EfficientNet-B6 (autoaug)",
      "d": "2019-06-01",
      "m1": "45.8",
      "m2": "39.3",
      "m3": "50.7"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Strategies From Data](http://openaccess.thecvf.com/content_CVPR_2019/html/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/mindspore-ai/models/blob/master/research/cv/autoaugment)",
      "n": "EfficientNet-B5 (autoaug)",
      "d": "2019-06-01",
      "m1": "45.7",
      "m2": "39.8",
      "m3": "50.2"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B3 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "45.5",
      "m2": "39.8",
      "m3": "49.5"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Strategies From Data](http://openaccess.thecvf.com/content_CVPR_2019/html/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/mindspore-ai/models/blob/master/research/cv/autoaugment)",
      "n": "EfficientNet-B7 (autoaug)",
      "d": "2019-06-01",
      "m1": "45",
      "m2": "39.1",
      "m3": "49.9"
    },
    {
      "p": "[RandAugment: Practical automated data augmentation with a reduced search space](https://arxiv.org/abs/1909.13719v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B7 (randaug)",
      "d": "2019-09-30",
      "m1": "45",
      "m2": "38.9",
      "m3": "48.7"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Strategies From Data](http://openaccess.thecvf.com/content_CVPR_2019/html/Cubuk_AutoAugment_Learning_Augmentation_Strategies_From_Data_CVPR_2019_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/mindspore-ai/models/blob/master/research/cv/autoaugment)",
      "n": "EfficientNet-B4 (autoaug)",
      "d": "2019-06-01",
      "m1": "44.3",
      "m2": "38.2",
      "m3": "48.6"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B2 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "44.3",
      "m2": "38.2",
      "m3": "48"
    },
    {
      "p": "[Deep Residual Learning for Image Recognition](http://arxiv.org/abs/1512.03385v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/deeplab)",
      "n": "ResNet-50",
      "d": "2015-12-10",
      "m1": "42.9",
      "m2": "37.1",
      "m3": "47.7"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B5",
      "d": "2019-05-28",
      "m1": "42.8",
      "m2": "37",
      "m3": "47.3"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Policies from Data](http://arxiv.org/abs/1805.09501v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/autoaugment)",
      "n": "EfficientNet-B3 (autoaug)",
      "d": "2018-05-24",
      "m1": "42.6",
      "m2": "34.9",
      "m3": "47.5"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B1 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "42.4",
      "m2": "36.2",
      "m3": "46.7"
    },
    {
      "p": "[AugMix: A Simple Data Processing Method to Improve Robustness and Uncertainty](https://arxiv.org/abs/1912.02781v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-50 (augmix)",
      "d": "2019-12-05",
      "m1": "42.2",
      "m2": "35.9",
      "m3": "46.4"
    },
    {
      "p": "[RandAugment: Practical automated data augmentation with a reduced search space](https://arxiv.org/abs/1909.13719v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B5 (randaug)",
      "d": "2019-09-30",
      "m1": "42.1",
      "m2": "35.5",
      "m3": "47.3"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-101 (lpf3)",
      "d": "2019-04-25",
      "m1": "41.7",
      "m2": "35.7",
      "m3": "46.1"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B4",
      "d": "2019-05-28",
      "m1": "41.7",
      "m2": "35.6",
      "m3": "46.4"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Policies from Data](http://arxiv.org/abs/1805.09501v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/autoaugment)",
      "n": "EfficientNet-B2 (autoaug)",
      "d": "2018-05-24",
      "m1": "41.6",
      "m2": "34.3",
      "m3": "45.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-50 (lpf5)",
      "d": "2019-04-25",
      "m1": "41.5",
      "m2": "35.2",
      "m3": "45.3"
    },
    {
      "p": "[The Many Faces of Robustness: A Critical Analysis of Out-of-Distribution Generalization](https://arxiv.org/abs/2006.16241v3)",
      "c": "[&check;&nbsp;Link](https://github.com/hendrycks/imagenet-r)",
      "n": "ResNet-50 (deepaugment)",
      "d": "2020-06-29",
      "m1": "41.3",
      "m2": "34.9",
      "m3": "46"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-101 (lpf2)",
      "d": "2019-04-25",
      "m1": "41.1",
      "m2": "35.1",
      "m3": "45.2"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-101 (lpf5)",
      "d": "2019-04-25",
      "m1": "41",
      "m2": "34.8",
      "m3": "45.8"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B3",
      "d": "2019-05-28",
      "m1": "40.7",
      "m2": "34.2",
      "m3": "45.3"
    },
    {
      "p": "[Adversarial Examples Improve Image Recognition](https://arxiv.org/abs/1911.09665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "EfficientNet-B0 (advprop+autoaug)",
      "d": "2019-11-21",
      "m1": "40.5",
      "m2": "34.2",
      "m3": "44.9"
    },
    {
      "p": "[The Many Faces of Robustness: A Critical Analysis of Out-of-Distribution Generalization](https://arxiv.org/abs/2006.16241v3)",
      "c": "[&check;&nbsp;Link](https://github.com/hendrycks/imagenet-r)",
      "n": "ResNet-50 (deepaugment+augmix)",
      "d": "2020-06-29",
      "m1": "40.3",
      "m2": "34.1",
      "m3": "44.5"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-50 (lpf2)",
      "d": "2019-04-25",
      "m1": "40.3",
      "m2": "33.4",
      "m3": "45.1"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-50 (lpf3)",
      "d": "2019-04-25",
      "m1": "40",
      "m2": "34.3",
      "m3": "44.7"
    },
    {
      "p": "[Bag of Tricks for Image Classification with Convolutional Neural Networks](http://arxiv.org/abs/1812.01187v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleOCR)",
      "n": "ResNet-26-D",
      "d": "2018-12-04",
      "m1": "39.7",
      "m2": "35.8",
      "m3": "43.5"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Policies from Data](http://arxiv.org/abs/1805.09501v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/autoaugment)",
      "n": "EfficientNet-B1 (autoaug)",
      "d": "2018-05-24",
      "m1": "39.7",
      "m2": "32.8",
      "m3": "44.4"
    },
    {
      "p": "[ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness](https://arxiv.org/abs/1811.12231v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rgeirhos/texture-vs-shape)",
      "n": "ResNet-50 (SIN_IN_IN)",
      "d": "2018-11-29",
      "m1": "39.2",
      "m2": "32.4",
      "m3": "44.6"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C)",
      "d": "2020-07-01",
      "m1": "38.8",
      "m2": "33.6",
      "m3": "42.9"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_brightness)",
      "d": "2020-07-01",
      "m1": "38.8",
      "m2": "32.5",
      "m3": "43.5"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "DenseNet121 (lpf5)",
      "d": "2019-04-25",
      "m1": "38.7",
      "m2": "32",
      "m3": "42.7"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-34 (lpf2)",
      "d": "2019-04-25",
      "m1": "38.3",
      "m2": "32.4",
      "m3": "42.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "DenseNet-121 (lpf3)",
      "d": "2019-04-25",
      "m1": "38.3",
      "m2": "32.3",
      "m3": "42.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-34 (lpf3)",
      "d": "2019-04-25",
      "m1": "38.3",
      "m2": "31.9",
      "m3": "42.9"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "DenseNet-121 (lpf2)",
      "d": "2019-04-25",
      "m1": "38.3",
      "m2": "31.7",
      "m3": "43.1"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_spatter)",
      "d": "2020-07-01",
      "m1": "38.3",
      "m2": "31.4",
      "m3": "42.7"
    },
    {
      "p": "[ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness](https://arxiv.org/abs/1811.12231v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rgeirhos/texture-vs-shape)",
      "n": "ResNet-50 (SIN_IN)",
      "d": "2018-11-29",
      "m1": "38.2",
      "m2": "32.5",
      "m3": "42.7"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_saturate)",
      "d": "2020-07-01",
      "m1": "38.2",
      "m2": "32.4",
      "m3": "42.4"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B2",
      "d": "2019-05-28",
      "m1": "38.1",
      "m2": "31.4",
      "m3": "42.8"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_pixelate)",
      "d": "2020-07-01",
      "m1": "37.4",
      "m2": "30.9",
      "m3": "41.4"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 BN (lpf2)",
      "d": "2019-04-25",
      "m1": "37.2",
      "m2": "31.3",
      "m3": "41.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-34 (lpf5)",
      "d": "2019-04-25",
      "m1": "37.2",
      "m2": "29.9",
      "m3": "42.5"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 BN (lpf5)",
      "d": "2019-04-25",
      "m1": "37",
      "m2": "30.8",
      "m3": "41.7"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 BN (lpf3)",
      "d": "2019-04-25",
      "m1": "36.9",
      "m2": "30.6",
      "m3": "42.1"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-16 BN",
      "d": "2014-09-04",
      "m1": "36.7",
      "m2": "31.1",
      "m3": "41.1"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B1",
      "d": "2019-05-28",
      "m1": "36.7",
      "m2": "30.9",
      "m3": "41.5"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_contrast)",
      "d": "2020-07-01",
      "m1": "36.5",
      "m2": "30.7",
      "m3": "40.9"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_jpeg_compression)",
      "d": "2020-07-01",
      "m1": "36.5",
      "m2": "30.3",
      "m3": "41.3"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_gaussian_noise)",
      "d": "2020-07-01",
      "m1": "36.4",
      "m2": "30.2",
      "m3": "40.6"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-19 BN",
      "d": "2014-09-04",
      "m1": "36.2",
      "m2": "29.4",
      "m3": "40.8"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_frost)",
      "d": "2020-07-01",
      "m1": "36.1",
      "m2": "29.7",
      "m3": "40"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "MobileNetV2 (lpf3)",
      "d": "2019-04-25",
      "m1": "36",
      "m2": "30.4",
      "m3": "40.3"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_fog_aws)",
      "d": "2020-07-01",
      "m1": "35.9",
      "m2": "30.3",
      "m3": "39.9"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "MobileNetV2 (lpf5)",
      "d": "2019-04-25",
      "m1": "35.8",
      "m2": "29.1",
      "m3": "40.1"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_motion_blur)",
      "d": "2020-07-01",
      "m1": "35.7",
      "m2": "30.2",
      "m3": "39.6"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-18 (lpf3)",
      "d": "2019-04-25",
      "m1": "35.6",
      "m2": "28.5",
      "m3": "39.5"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "MobileNetV2 (lpf2)",
      "d": "2019-04-25",
      "m1": "35.5",
      "m2": "30.3",
      "m3": "39.2"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-18 (lpf2)",
      "d": "2019-04-25",
      "m1": "35.5",
      "m2": "28.7",
      "m3": "40.1"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 (lpf3)",
      "d": "2019-04-25",
      "m1": "35.1",
      "m2": "28.2",
      "m3": "40"
    },
    {
      "p": "[AutoAugment: Learning Augmentation Policies from Data](http://arxiv.org/abs/1805.09501v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/autoaugment)",
      "n": "EfficientNet-B0 (autoaug)",
      "d": "2018-05-24",
      "m1": "34.9",
      "m2": "27.3",
      "m3": "40.1"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-19",
      "d": "2014-09-04",
      "m1": "34.7",
      "m2": "29",
      "m3": "39.3"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-16",
      "d": "2014-09-04",
      "m1": "34.7",
      "m2": "28.5",
      "m3": "39.5"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "ResNet-18 (lpf5)",
      "d": "2019-04-25",
      "m1": "34.7",
      "m2": "27.7",
      "m3": "38.9"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 (lpf5)",
      "d": "2019-04-25",
      "m1": "34.5",
      "m2": "27.8",
      "m3": "39.4"
    },
    {
      "p": "[EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ultralytics/yolov5)",
      "n": "EfficientNet-B0",
      "d": "2019-05-28",
      "m1": "34.2",
      "m2": "27.4",
      "m3": "38.4"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-13 BN",
      "d": "2014-09-04",
      "m1": "33.7",
      "m2": "28.3",
      "m3": "38.4"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "VGG-16 (lpf2)",
      "d": "2019-04-25",
      "m1": "33.5",
      "m2": "26.7",
      "m3": "38.5"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-11 BN",
      "d": "2014-09-04",
      "m1": "32.9",
      "m2": "25.8",
      "m3": "37.1"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_zoom_blur)",
      "d": "2020-07-01",
      "m1": "32.7",
      "m2": "28.3",
      "m3": "36.6"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-13",
      "d": "2014-09-04",
      "m1": "32.4",
      "m2": "26.4",
      "m3": "36.5"
    },
    {
      "p": "[Very Deep Convolutional Networks for Large-Scale Image Recognition](http://arxiv.org/abs/1409.1556v6)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/slim)",
      "n": "VGG-11",
      "d": "2014-09-04",
      "m1": "31.5",
      "m2": "25.2",
      "m3": "36.1"
    },
    {
      "p": "[Measuring Robustness to Natural Distribution Shifts in Image Classification](https://arxiv.org/abs/2007.00644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modestyachts/imagenet-testbed)",
      "n": "ResNet-50 (IN-C_greyscale)",
      "d": "2020-07-01",
      "m1": "30.2",
      "m2": "24.3",
      "m3": "34.3"
    },
    {
      "p": "[Adversarial Training for Free!](https://arxiv.org/abs/1904.12843v2)",
      "c": "[&check;&nbsp;Link](https://github.com/locuslab/fast_adversarial)",
      "n": "ResNet-50 (adv-train-free)",
      "d": "2019-04-29",
      "m1": "26.7",
      "m2": "20.5",
      "m3": "30.9"
    },
    {
      "p": "[ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness](https://arxiv.org/abs/1811.12231v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rgeirhos/texture-vs-shape)",
      "n": "ResNet-50 (SIN)",
      "d": "2018-11-29",
      "m1": "25.3",
      "m2": "20.4",
      "m3": "30"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "AlexNet (lpf3)",
      "d": "2019-04-25",
      "m1": "23.1",
      "m2": "17.5",
      "m3": "26.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "AlexNet (lpf2)",
      "d": "2019-04-25",
      "m1": "22.8",
      "m2": "18.2",
      "m3": "26.8"
    },
    {
      "p": "[Making Convolutional Networks Shift-Invariant Again](https://arxiv.org/abs/1904.11486v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwightman/pytorch-image-models)",
      "n": "AlexNet (lpf5)",
      "d": "2019-04-25",
      "m1": "22.7",
      "m2": "18.4",
      "m3": "26.8"
    },
    {
      "p": "[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ViT-8/B-224",
      "d": "2020-10-22",
      "m3": "450"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
