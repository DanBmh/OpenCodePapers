# audio-classification-on-vggsound

[Dataset Link](http://www.robots.ox.ac.uk/~vgg/data/vggsound/) \
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
      "label": "Top 1 Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Top 5 Accuracy",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Mean AP",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "AUC",
      "sortable": "true"
    },
    {
      "key": "m5",
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
      "p": "[Mirasol3B: A Multimodal Autoregressive model for time-aligned and contextual modalities](https://arxiv.org/abs/2311.05698v3)",
      "c": "",
      "n": "Mirasol3B",
      "d": "2023-11-09",
      "m1": "69.8"
    },
    {
      "p": "[CA^2ST: Cross-Attention in Audio, Space, and Time for Holistic Video Recognition](https://arxiv.org/abs/2503.23447v1)",
      "c": "",
      "n": "CA2ST(B/16)",
      "d": "2025-03-30",
      "m1": "68.3"
    },
    {
      "p": "[ONE-PEACE: Exploring One General Representation Model Toward Unlimited Modalities](https://arxiv.org/abs/2305.11172v1)",
      "c": "[&check;&nbsp;Link](https://github.com/modelscope/modelscope)",
      "n": "ONE-PEACE (Audio-Visual)",
      "d": "2023-05-18",
      "m1": "68.2"
    },
    {
      "p": "[CA^2ST: Cross-Attention in Audio, Space, and Time for Holistic Video Recognition](https://arxiv.org/abs/2503.23447v1)",
      "c": "",
      "n": "CAVA(B/16)",
      "d": "2025-03-30",
      "m1": "68.2"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MAViL",
      "d": null,
      "m1": "67.1"
    },
    {
      "p": "[EquiAV: Leveraging Equivariance for Audio-Visual Contrastive Learning](https://arxiv.org/abs/2403.09502v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jongsuk1/equiav)",
      "n": "EquiAV",
      "d": "2024-03-14",
      "m1": "67.1"
    },
    {
      "p": "[Multiscale Multimodal Transformer for Multimodal Action Recognition](https://openreview.net/pdf?id=aqP3WFwMPbe)",
      "c": "",
      "n": "MMT (Audio-Visual)",
      "d": "2022-09-22",
      "m1": "66.2",
      "m2": "85.7"
    },
    {
      "p": "[Contrastive Audio-Visual Masked Autoencoder](https://arxiv.org/abs/2210.07839v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yuangongnd/cav-mae)",
      "n": "CAV-MAE (Audio-Visual)",
      "d": "2022-10-02",
      "m1": "65.9"
    },
    {
      "p": "[UAVM: Towards Unifying Audio and Visual Models](https://arxiv.org/abs/2208.00061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/uavm)",
      "n": "UAVM (Audio + Video)",
      "d": "2022-07-29",
      "m1": "65.8"
    },
    {
      "p": "[Audiovisual Masked Autoencoders](https://arxiv.org/abs/2212.05922v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/av_mae)",
      "n": "Audiovisual Masked Autoencoder  (Audiovisual, Single)",
      "d": "2022-12-09",
      "m1": "65.0"
    },
    {
      "p": "[AVT: Audio-Video Transformer for Multimodal Action Recognition](https://openreview.net/pdf?id=yFuHxmSwGus)",
      "c": "",
      "n": "AVT (Audio-Visual)",
      "d": "2022-09-22",
      "m1": "63.9",
      "m2": "85.0"
    },
    {
      "p": "[ONE-PEACE: Exploring One General Representation Model Toward Unlimited Modalities](https://arxiv.org/abs/2305.11172v1)",
      "c": "[&check;&nbsp;Link](https://github.com/modelscope/modelscope)",
      "n": "ONE-PEACE (Audio-Only)",
      "d": "2023-05-18",
      "m1": "59.6"
    },
    {
      "p": "[Contrastive Audio-Visual Masked Autoencoder](https://arxiv.org/abs/2210.07839v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yuangongnd/cav-mae)",
      "n": "CAV-MAE (Audio-Only)",
      "d": "2022-10-02",
      "m1": "59.5"
    },
    {
      "p": "[Audiovisual Masked Autoencoders](https://arxiv.org/abs/2212.05922v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/av_mae)",
      "n": "Audiovisual Masked Autoencoder\n(Audio-only, Single)",
      "d": "2022-12-09",
      "m1": "57.2"
    },
    {
      "p": "[Multiscale Audio Spectrogram Transformer for Efficient Audio Classification](https://arxiv.org/abs/2303.10757v1)",
      "c": "",
      "n": "MAST (Audio Only)",
      "d": "2023-03-19",
      "m1": "57.0",
      "m2": "81.3"
    },
    {
      "p": "[UAVM: Towards Unifying Audio and Visual Models](https://arxiv.org/abs/2208.00061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/uavm)",
      "n": "UAVM (Audio Only)",
      "d": "2022-07-29",
      "m1": "56.5"
    },
    {
      "p": "[Multiscale Multimodal Transformer for Multimodal Action Recognition](https://openreview.net/pdf?id=aqP3WFwMPbe)",
      "c": "",
      "n": "MMT (Video)",
      "d": "2022-09-22",
      "m1": "56.1",
      "m2": "77.9"
    },
    {
      "p": "[Play It Back: Iterative Attention for Audio Recognition](https://arxiv.org/abs/2210.11328v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alexandrosstergiou/PlayItBack)",
      "n": "PlayItBackX3",
      "d": "2022-10-20",
      "m1": "53.7",
      "m2": "79.2",
      "m3": "56.1",
      "m4": "97.8",
      "m5": "2.846"
    },
    {
      "p": "[AVT: Audio-Video Transformer for Multimodal Action Recognition](https://openreview.net/pdf?id=yFuHxmSwGus)",
      "c": "",
      "n": "AVT (V)",
      "d": "2022-09-22",
      "m1": "53.2",
      "m2": "74.8"
    },
    {
      "p": "[Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt)",
      "n": "MBT (A)",
      "d": "2021-06-30",
      "m1": "52.3",
      "m2": "78.1"
    },
    {
      "p": "[Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt)",
      "n": "MBT (V)",
      "d": "2021-06-30",
      "m1": "51.2",
      "m2": "72.6"
    },
    {
      "p": "[UAVM: Towards Unifying Audio and Visual Models](https://arxiv.org/abs/2208.00061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/YuanGongND/uavm)",
      "n": "UAVM (Video Only)",
      "d": "2022-07-29",
      "m1": "49.9"
    },
    {
      "p": "[Attention Bottlenecks for Multimodal Fusion](https://arxiv.org/abs/2107.00135v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/scenic/tree/main/scenic/projects/mbt)",
      "n": "MBT (AV)",
      "d": "2021-06-30",
      "m2": "85.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
