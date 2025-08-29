# audio-classification-on-audioset

[Dataset Link](https://research.google.com/audioset/index.html) \
Task Hierarchy: ['Classification', 'Audio Classification']

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
      "label": "Test mAP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "AUC",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "d-prime",
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
      "m1": "0.558"
    },
    {
      "p": "[OmniVec: Learning robust representations with cross modal sharing](https://arxiv.org/abs/2311.05709v1)",
      "c": "",
      "n": "OmniVec",
      "d": "2023-11-07",
      "m1": "0.548"
    },
    {
      "p": "[EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning](https://arxiv.org/abs/2403.09502v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jongsuk1/equiav)",
      "n": "EquiAV",
      "d": "2024-03-14",
      "m1": "0.546"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MAViL (Audio-Visual, single)",
      "d": null,
      "m1": "0.533"
    },
    {
      "p": "[Audiovisual Masked Autoencoders](https://arxiv.org/abs/2212.05922v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/av_mae)",
      "n": "Audiovisual Masked Autoencoder (Audiovisual, Single)",
      "d": "2022-12-09",
      "m1": "0.518"
    },
    {
      "p": "[Contrastive Audio-Visual Masked Autoencoder](https://arxiv.org/abs/2210.07839v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yuangongnd/cav-mae)",
      "n": "CAV-MAE (Audio-Visual)",
      "d": "2022-10-02",
      "m1": "0.512"
    },
    {
      "p": "[BEATs: Audio Pre-Training with Acoustic Tokenizers](https://arxiv.org/abs/2212.09058v1)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/unilm/tree/master/beats)",
      "n": "BEATs (Audio-only, Ensemble)",
      "d": "2022-12-18",
      "m1": "0.506"
    },
    {
      "p": "[UAVM: Towards Unifying Audio and Visual Models](https://arxiv.org/abs/2208.00061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/uavm)",
      "n": "UAVM (Audio + Video)",
      "d": "2022-07-29",
      "m1": "0.504"
    },
    {
      "p": "[SSLAM: Enhancing Self-Supervised Models with Audio Mixtures for Polyphonic Soundscapes](https://arxiv.org/abs/2506.12222v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ta012/SSLAM)",
      "n": "SSLAM (Audio-Only, Single)",
      "d": "2025-06-13",
      "m1": "0.502"
    },
    {
      "p": "[Efficient Large-scale Audio Tagging via Transformer-to-CNN Knowledge Distillation](https://arxiv.org/abs/2211.04772v3)",
      "c": "[&check;&nbsp;Link](https://github.com/fschmid56/efficientat)",
      "n": "mn40_as (Ensemble)",
      "d": "2022-11-09",
      "m1": "0.498"
    },
    {
      "p": "[Self-supervised Audio Teacher-Student Transformer for Both Clip-level and Frame-level Tasks](https://arxiv.org/abs/2306.04186v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Audio-WestlakeU/ATST-SED)",
      "n": "ATST-C2F(Single)",
      "d": "2023-06-07",
      "m1": "0.497"
    },
    {
      "p": "[Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt)",
      "n": "MBT (AS-500K training + Video)",
      "d": "2021-06-30",
      "m1": "0.496"
    },
    {
      "p": "[Efficient Training of Audio Transformers with Patchout](https://arxiv.org/abs/2110.05069v3)",
      "c": "[&check;&nbsp;Link](https://github.com/kkoutini/passt)",
      "n": "PaSST (Ensemble)",
      "d": "2021-10-11",
      "m1": "0.496"
    },
    {
      "p": "[Dynamic Convolutional Neural Networks as Efficient Pre-trained Audio Models](https://arxiv.org/abs/2310.15648v1)",
      "c": "[&check;&nbsp;Link](https://github.com/fschmid56/efficientat)",
      "n": "DyMN-L (Audio-Only, Single)",
      "d": "2023-10-24",
      "m1": "0.490"
    },
    {
      "p": "[M2D2: Exploring General-purpose Audio-Language Representations Beyond CLAP](https://arxiv.org/abs/2503.22104v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab/m2d)",
      "n": "M2D2",
      "d": "2025-03-28",
      "m1": "0.490"
    },
    {
      "p": "[HTS-AT: A Hierarchical Token-Semantic Audio Transformer for Sound Classification and Detection](https://arxiv.org/abs/2202.00874v1)",
      "c": "[&check;&nbsp;Link](https://github.com/retrocirce/hts-audio-transformer)",
      "n": "HTS-AT (Ensemble)",
      "d": "2022-02-02",
      "m1": "0.487"
    },
    {
      "p": "[BEATs: Audio Pre-Training with Acoustic Tokenizers](https://arxiv.org/abs/2212.09058v1)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/unilm/tree/master/beats)",
      "n": "BEATs (Audio-only, Single)",
      "d": "2022-12-18",
      "m1": "0.486"
    },
    {
      "p": "[EAT: Self-Supervised Pre-Training with Efficient Audio Transformer](https://arxiv.org/abs/2401.03497v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cwx-worst-one/eat)",
      "n": "EAT",
      "d": "2024-01-07",
      "m1": "0.486"
    },
    {
      "p": "[DTF-AT: Decoupled Time-Frequency Audio Transformer for Event Classification](https://ojs.aaai.org/index.php/AAAI/article/view/29716)",
      "c": "[&check;&nbsp;Link](https://github.com/ta012/DTFAT)",
      "n": "DTF-AT (Single)",
      "d": "2024-03-24",
      "m1": "0.486"
    },
    {
      "p": "[AST: Audio Spectrogram Transformer](https://arxiv.org/abs/2104.01778v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/ast)",
      "n": "AST (Ensemble)",
      "d": "2021-04-05",
      "m1": "0.485"
    },
    {
      "p": "[M2D-CLAP: Masked Modeling Duo Meets CLAP for Learning General-purpose Audio-Language Representation](https://arxiv.org/abs/2406.02032v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab/m2d)",
      "n": "M2D-CLAP/0.7",
      "d": "2024-06-04",
      "m1": "0.485"
    },
    {
      "p": "[Masked Modeling Duo: Towards a Universal Audio Pre-training Framework](https://arxiv.org/abs/2404.06095v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab/m2d)",
      "n": "M2D-AS/0.7",
      "d": "2024-04-09",
      "m1": "0.485"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MAViL (Audio-only, single)",
      "d": null,
      "m1": "0.484"
    },
    {
      "p": "[Efficient Large-scale Audio Tagging via Transformer-to-CNN Knowledge Distillation](https://arxiv.org/abs/2211.04772v3)",
      "c": "[&check;&nbsp;Link](https://github.com/fschmid56/efficientat)",
      "n": "mn40_as (Single)",
      "d": "2022-11-09",
      "m1": "0.483"
    },
    {
      "p": "[MAX-AST: COMBINING CONVOLUTION, LOCAL AND GLOBAL SELF-ATTENTIONS FOR AUDIO EVENT CLASSIFICATION](https://cmsworkshops.com/ICASSP2024/view_paper.php?PaperNum=7388)",
      "c": "[&check;&nbsp;Link](https://github.com/ta012/MaxAST)",
      "n": "MAX-AST (Single)",
      "d": "2024-04-14",
      "m1": "0.481"
    },
    {
      "p": "[Self-supervised Audio Teacher-Student Transformer for Both Clip-level and Frame-level Tasks](https://arxiv.org/abs/2306.04186v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Audio-WestlakeU/ATST-SED)",
      "n": "ATST-Frame",
      "d": "2023-06-07",
      "m1": "0.480"
    },
    {
      "p": "[Masked Modeling Duo: Towards a Universal Audio Pre-training Framework](https://arxiv.org/abs/2404.06095v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nttcslab/m2d)",
      "n": "M2D/0.7",
      "d": "2024-04-09",
      "m1": "0.479"
    },
    {
      "p": "[Play It Back: Iterative Attention for Audio Recognition](https://arxiv.org/abs/2210.11328v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alexandrosstergiou/PlayItBack)",
      "n": "PlayItBackX3",
      "d": "2022-10-20",
      "m1": "0.477"
    },
    {
      "p": "[DASS: Distilled Audio State Space Models Are Stronger and More Duration-Scalable Learners](https://arxiv.org/abs/2407.04082v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Saurabhbhati/DASS)",
      "n": "DASS-Medium (Audio-only, single)",
      "d": "2024-07-04",
      "m1": "0.476"
    },
    {
      "p": "[PSLA: Improving Audio Tagging with Pretraining, Sampling, Labeling, and Aggregation](https://arxiv.org/abs/2102.01243v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/psla)",
      "n": "PSLA (Ensemble)",
      "d": "2021-02-02",
      "m1": "0.474",
      "m2": "0.981",
      "m3": "2.936"
    },
    {
      "p": "[DASS: Distilled Audio State Space Models Are Stronger and More Duration-Scalable Learners](https://arxiv.org/abs/2407.04082v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Saurabhbhati/DASS)",
      "n": "DASS-Small (Audio-only, single)",
      "d": "2024-07-04",
      "m1": "0.472"
    },
    {
      "p": "[Efficient Training of Audio Transformers with Patchout](https://arxiv.org/abs/2110.05069v3)",
      "c": "[&check;&nbsp;Link](https://github.com/kkoutini/passt)",
      "n": "PaSST-S (Single)",
      "d": "2021-10-11",
      "m1": "0.471"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MaskSpec (AS-2M)",
      "d": null,
      "m1": "0.471"
    },
    {
      "p": "[Contrastive Audio-Visual Masked Autoencoder](https://arxiv.org/abs/2210.07839v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yuangongnd/cav-mae)",
      "n": "CAV-MAE (Audio-Only)",
      "d": "2022-10-02",
      "m1": "0.466"
    },
    {
      "p": "[Audiovisual Masked Autoencoders](https://arxiv.org/abs/2212.05922v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/av_mae)",
      "n": "Audiovisual Masked Autoencoder (Audio-only, Single)",
      "d": "2022-12-09",
      "m1": "0.466"
    },
    {
      "p": "[Large Scale Audiovisual Learning of Sounds with Weakly Labeled Data](https://arxiv.org/abs/2006.01595v1)",
      "c": "",
      "n": "AudioVisual Fusion Net",
      "d": "2020-05-29",
      "m1": "0.462",
      "m2": "0.975"
    },
    {
      "p": "[AST: Audio Spectrogram Transformer](https://arxiv.org/abs/2104.01778v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/ast)",
      "n": "AST (Single)",
      "d": "2021-04-05",
      "m1": "0.459"
    },
    {
      "p": "[ERANNs: Efficient Residual Audio Neural Networks for Audio Pattern Recognition](https://arxiv.org/abs/2106.01621v7)",
      "c": "",
      "n": "ERANN-1-6",
      "d": "2021-06-03",
      "m1": "0.450",
      "m2": "0.976",
      "m3": "2.804"
    },
    {
      "p": "[Perceiver: General Perception with Iterative Attention](https://arxiv.org/abs/2103.03206v2)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/deepmind-research/tree/master/perceiver)",
      "n": "Perceiver",
      "d": "2021-03-04",
      "m1": "0.449"
    },
    {
      "p": "[PSLA: Improving Audio Tagging with Pretraining, Sampling, Labeling, and Aggregation](https://arxiv.org/abs/2102.01243v3)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/psla)",
      "n": "PSLA (Single)",
      "d": "2021-02-02",
      "m1": "0.443",
      "m2": "0.975",
      "m3": "2.778"
    },
    {
      "p": "[PANNs: Large-Scale Pretrained Audio Neural Networks for Audio Pattern Recognition](http://arxiv.org/abs/1912.10211v5)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "PANNs-CNN14 (Single)",
      "d": "2020-08-23",
      "m1": "0.431",
      "m2": "0.973",
      "m3": "2.732"
    },
    {
      "p": "[End-to-End Audio Strikes Back: Boosting Augmentations Towards An Efficient Audio Classification Network](https://arxiv.org/abs/2204.11479v5)",
      "c": "[&check;&nbsp;Link](https://github.com/Alibaba-MIIL/AudioClassfication)",
      "n": "EAT-M",
      "d": "2022-04-25",
      "m1": "0.426"
    },
    {
      "p": "[Conformer-Based Self-Supervised Learning for Non-Speech Audio Tasks](https://arxiv.org/abs/2110.07313v3)",
      "c": "",
      "n": "Conformer (AS-2M)",
      "d": "2021-10-14",
      "m1": "0.411"
    },
    {
      "p": "[End-to-End Audio Strikes Back: Boosting Augmentations Towards An Efficient Audio Classification Network](https://arxiv.org/abs/2204.11479v5)",
      "c": "[&check;&nbsp;Link](https://github.com/Alibaba-MIIL/AudioClassfication)",
      "n": "EAT-S",
      "d": "2022-04-25",
      "m1": "0.405"
    },
    {
      "p": "[A Sequential Self Teaching Approach for Improving Generalization in Sound Event Recognition](https://arxiv.org/abs/2007.00144v1)",
      "c": "",
      "n": "WEANet-SUSTAIN",
      "d": "2020-06-30",
      "m1": "0.398",
      "m2": "0.972"
    },
    {
      "p": "[VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text](https://arxiv.org/abs/2104.11178v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/vatt)",
      "n": "VATT-Base",
      "d": "2021-04-22",
      "m1": "0.394",
      "m2": "0.971",
      "m3": "2.895"
    },
    {
      "p": "[Multi-Format Contrastive Learning of Audio Representations](https://arxiv.org/abs/2103.06508v3)",
      "c": "",
      "n": "Multi-Format Contrastive",
      "d": "2021-03-11",
      "m1": "0.376"
    },
    {
      "p": "[Self-Supervised MultiModal Versatile Networks](https://arxiv.org/abs/2006.16228v2)",
      "c": "[&check;&nbsp;Link](https://github.com/deepmind/deepmind-research/tree/master/mmv)",
      "n": "MMV",
      "d": "2020-06-29",
      "m1": "0.309"
    },
    {
      "p": "[Contrastive Audio-Visual Masked Autoencoder](https://arxiv.org/abs/2210.07839v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yuangongnd/cav-mae)",
      "n": "CAV-MAE (Visual-Only)",
      "d": "2022-10-02",
      "m1": "0.262"
    },
    {
      "p": "[Look, Listen and Learn](http://arxiv.org/abs/1705.08168v2)",
      "c": "[&check;&nbsp;Link](https://github.com/marl/l3embedding)",
      "n": "L3",
      "d": "2017-05-23",
      "m1": "0.249"
    },
    {
      "p": "[Unsupervised Learning of Semantic Audio Representations](http://arxiv.org/abs/1711.02209v1)",
      "c": "",
      "n": "Triplet",
      "d": "2017-11-06",
      "m1": "0.244"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
