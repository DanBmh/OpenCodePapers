# semantic-segmentation-on-camvid

[Dataset Link](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/) \
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
      "label": "Global Accuracy",
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
      "p": "[SERNet-Former: Semantic Segmentation by Efficient Residual Network with Attention-Boosting Gates and Attention-Fusion Networks](https://arxiv.org/abs/2401.15741v7)",
      "c": "[&check;&nbsp;Link](https://github.com/serdarch/sernet-former)",
      "n": "SERNet-Former",
      "d": "2024-01-28",
      "m1": "84.62"
    },
    {
      "p": "[Scaling up Multi-domain Semantic Segmentation with Sentence Embeddings](https://arxiv.org/abs/2202.02002v2)",
      "c": "",
      "n": "SIW",
      "d": "2022-02-04",
      "m1": "83.7"
    },
    {
      "p": "[DSNet: A Novel Way to Use Atrous Convolutions in Semantic Segmentation](https://arxiv.org/abs/2406.03702v1)",
      "c": "[&check;&nbsp;Link](https://github.com/takaniwa/dsnet)",
      "n": "DSNet-Base",
      "d": "2024-06-06",
      "m1": "83.32"
    },
    {
      "p": "[RTFormer: Efficient Design for Real-Time Semantic Segmentation with Transformer](https://arxiv.org/abs/2210.07124v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "RTFormer-Base",
      "d": "2022-10-13",
      "m1": "82.5"
    },
    {
      "p": "[PIDNet: A Real-time Semantic Segmentation Network Inspired by PID Controllers](https://arxiv.org/abs/2206.02066v3)",
      "c": "[&check;&nbsp;Link](https://github.com/XuJiacong/PIDNet)",
      "n": "PIDNet-Wider",
      "d": "2022-06-04",
      "m1": "82.0%"
    },
    {
      "p": "[Improving Semantic Segmentation via Video Propagation and Label Relaxation](https://arxiv.org/abs/1812.01593v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/semantic-segmentation)",
      "n": "DeepLabV3Plus + SDCNetAug",
      "d": "2018-12-04",
      "m1": "81.7"
    },
    {
      "p": "[Deep Dual-resolution Networks for Real-time and Accurate Semantic Segmentation of Road Scenes](https://arxiv.org/abs/2101.06085v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Deci-AI/super-gradients)",
      "n": "DDRNet23",
      "d": "2021-01-15",
      "m1": "80.6%"
    },
    {
      "p": "[Efficient Semantic Video Segmentation with Per-frame Inference](https://arxiv.org/abs/2002.11433v2)",
      "c": "[&check;&nbsp;Link](https://github.com/irfanICMLL/ETC-Real-time-Per-frame-Semantic-video-segmentation)",
      "n": "ETC-Mobile",
      "d": "2020-02-26",
      "m1": "76.3"
    },
    {
      "p": "[Deep Spatio-Temporal Random Fields for Efficient Video Segmentation](http://arxiv.org/abs/1807.03148v1)",
      "c": "",
      "n": "VideoGCRF",
      "d": "2018-07-03",
      "m1": "75.2"
    },
    {
      "p": "[Dense Decoder Shortcut Connections for Single-Pass Semantic Segmentation](http://openaccess.thecvf.com/content_cvpr_2018/html/Bilinski_Dense_Decoder_Shortcut_CVPR_2018_paper.html)",
      "c": "",
      "n": "DenseDecoder",
      "d": "2018-06-01",
      "m1": "70.9"
    },
    {
      "p": "[BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation](http://arxiv.org/abs/1808.00897v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "BiSeNet",
      "d": "2018-08-02",
      "m1": "68.7%"
    },
    {
      "p": "[The One Hundred Layers Tiramisu: Fully Convolutional DenseNets for Semantic Segmentation](http://arxiv.org/abs/1611.09326v3)",
      "c": "[&check;&nbsp;Link](https://github.com/SimJeg/FC-DenseNet)",
      "n": "FC-DenseNet103",
      "d": "2016-11-28",
      "m1": "66.9%",
      "m2": "91.5%"
    },
    {
      "p": "[Efficient Dense Modules of Asymmetric Convolution for Real-Time Semantic Segmentation](https://arxiv.org/abs/1809.06323v3)",
      "c": "[&check;&nbsp;Link](https://github.com/osmr/imgclsmob)",
      "n": "EDANet",
      "d": "2018-09-17",
      "m1": "66.4",
      "m2": "90.8"
    },
    {
      "p": "[Multi-Scale Context Aggregation by Dilated Convolutions](http://arxiv.org/abs/1511.07122v3)",
      "c": "[&check;&nbsp;Link](https://github.com/fyu/dilation)",
      "n": "Dilated Convolutions",
      "d": "2015-11-23",
      "m1": "65.3%"
    },
    {
      "p": "[DFANet: Deep Feature Aggregation for Real-Time Semantic Segmentation](http://arxiv.org/abs/1904.02216v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huaifeng1993/DFANet)",
      "n": "DFANet A",
      "d": "2019-04-03",
      "m1": "64.7%"
    },
    {
      "p": "[Template-Based Automatic Search of Compact Semantic Segmentation Architectures](https://arxiv.org/abs/1904.02365v2)",
      "c": "[&check;&nbsp;Link](https://github.com/drsleep/nas-segm-pytorch)",
      "n": "Template-Based NAS-arch0 (480x360 inputs)",
      "d": "2019-04-04",
      "m1": "63.9%"
    },
    {
      "p": "[Efficient Road Lane Marking Detection with Deep Learning](http://arxiv.org/abs/1809.03994v1)",
      "c": "",
      "n": "LMDNet",
      "d": "2018-09-11",
      "m1": "63.5"
    },
    {
      "p": "[Template-Based Automatic Search of Compact Semantic Segmentation Architectures](https://arxiv.org/abs/1904.02365v2)",
      "c": "[&check;&nbsp;Link](https://github.com/drsleep/nas-segm-pytorch)",
      "n": "Template-Based NAS-arch1 (480x360 inputs)",
      "d": "2019-04-04",
      "m1": "63.2%"
    },
    {
      "p": "[Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs](http://arxiv.org/abs/1412.7062v4)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models)",
      "n": "DeepLab-MSc-CRF-LargeFOV",
      "d": "2014-12-22",
      "m1": "61.6%"
    },
    {
      "p": "[ReSeg: A Recurrent Neural Network-based Model for Semantic Segmentation](http://arxiv.org/abs/1511.07053v3)",
      "c": "[&check;&nbsp;Link](https://github.com/fvisin/reseg)",
      "n": "ReSeg",
      "d": "2015-11-22",
      "m1": "58.8%",
      "m2": "88.7%"
    },
    {
      "p": "[SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation](http://arxiv.org/abs/1511.00561v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSeg)",
      "n": "SegNet",
      "d": "2015-11-02",
      "m1": "46.4%"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
