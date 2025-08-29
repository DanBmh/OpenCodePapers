# speech-separation-on-whamr

[Dataset Link](http://wham.whisper.ai/) \
Task Hierarchy: ['Speech Separation']

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
      "label": "SI-SDRi",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "MACs (G)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Number of parameters (M)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "SDRi",
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
      "p": "[TF-Locoformer: Transformer with Local Modeling by Convolution for Speech Separation and Enhancement](https://arxiv.org/abs/2408.03440v1)",
      "c": "[&check;&nbsp;Link](https://github.com/merlresearch/tf-locoformer)",
      "n": "TF-Locoformer (M)",
      "d": "2024-08-06",
      "m1": "18.5",
      "m3": "15",
      "m4": "16.9"
    },
    {
      "p": "[TF-Locoformer: Transformer with Local Modeling by Convolution for Speech Separation and Enhancement](https://arxiv.org/abs/2408.03440v1)",
      "c": "[&check;&nbsp;Link](https://github.com/merlresearch/tf-locoformer)",
      "n": "TF-Locoformer (S)",
      "d": "2024-08-06",
      "m1": "17.4",
      "m3": "5",
      "m4": "15.9"
    },
    {
      "p": "[Separate and Reconstruct: Asymmetric Encoder-Decoder for Speech Separation](https://arxiv.org/abs/2406.05983v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlguq456/SepReformer)",
      "n": "SepReformer-L + DM",
      "d": "2024-06-10",
      "m1": "17.1"
    },
    {
      "p": "[MossFormer2: Combining Transformer and RNN-Free Recurrent Network for Enhanced Time-Domain Monaural Speech Separation](https://arxiv.org/abs/2312.11825v2)",
      "c": "[&check;&nbsp;Link](https://github.com/modelscope/ClearerVoice-Studio)",
      "n": "MossFormer2",
      "d": "2023-12-19",
      "m1": "17.0"
    },
    {
      "p": "[MossFormer: Pushing the Performance Limit of Monaural Speech Separation using Gated Single-Head Transformer with Convolution-Augmented Joint Self-Attentions](https://arxiv.org/abs/2302.11824v1)",
      "c": "[&check;&nbsp;Link](https://github.com/modelscope/ClearerVoice-Studio)",
      "n": "MossFormer (L) + DM",
      "d": "2023-02-23",
      "m1": "16.3"
    },
    {
      "p": "[On Time Domain Conformer Models for Monaural Speech Separation in Noisy Reverberant Acoustic Environments](https://arxiv.org/abs/2310.06125v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/pubsep)",
      "n": "TD-Conformer (XL) + DM",
      "d": "2023-10-09",
      "m1": "14.6"
    },
    {
      "p": "[Compute and memory efficient universal sound source separation](https://arxiv.org/abs/2103.02644v2)",
      "c": "[&check;&nbsp;Link](https://github.com/etzinis/sudo_rm_rf)",
      "n": "Improved Sudo rm -rf (U=36)",
      "d": "2021-03-03",
      "m1": "13.5"
    },
    {
      "p": "[On Time Domain Conformer Models for Monaural Speech Separation in Noisy Reverberant Acoustic Environments](https://arxiv.org/abs/2310.06125v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/pubsep)",
      "n": "TD-Conformer (L) + DM",
      "d": "2023-10-09",
      "m1": "13.4"
    },
    {
      "p": "[Wavesplit: End-to-End Speech Separation by Speaker Clustering](https://arxiv.org/abs/2002.08933v2)",
      "c": "",
      "n": "Wavesplit",
      "d": "2020-02-20",
      "m1": "13.2"
    },
    {
      "p": "[Stepwise-Refining Speech Separation Network via Fine-Grained Encoding in High-order Latent Domain](https://arxiv.org/abs/2110.04791v2)",
      "c": "",
      "n": "DPTNET - SRSSN",
      "d": "2021-10-10",
      "m1": "12.3"
    },
    {
      "p": "[Stepwise-Refining Speech Separation Network via Fine-Grained Encoding in High-order Latent Domain](https://arxiv.org/abs/2110.04791v2)",
      "c": "",
      "n": "DPRNN - SRSSN",
      "d": "2021-10-10",
      "m1": "12.3"
    },
    {
      "p": "[Voice Separation with an Unknown Number of Multiple Speakers](https://arxiv.org/abs/2003.01531v4)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/svoice)",
      "n": "VSUNOS",
      "d": "2020-02-29",
      "m1": "12.2"
    },
    {
      "p": "[Sudo rm -rf: Efficient Networks for Universal Audio Source Separation](https://arxiv.org/abs/2007.06833v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mpariente/asteroid)",
      "n": "Sudo rm -rf (U=16)",
      "d": "2020-07-14",
      "m1": "12.1"
    },
    {
      "p": "[On Time Domain Conformer Models for Monaural Speech Separation in Noisy Reverberant Acoustic Environments](https://arxiv.org/abs/2310.06125v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/pubsep)",
      "n": "TD-Confomer (M) + DM",
      "d": "2023-10-09",
      "m1": "12"
    },
    {
      "p": "[Deformable Temporal Convolutional Networks for Monaural Noisy Reverberant Speech Separation](https://arxiv.org/abs/2210.15305v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/dtcn)",
      "n": "Deformable TCN + Dynamic Mixing",
      "d": "2022-10-27",
      "m1": "11.1",
      "m2": "3.7",
      "m3": "3.6",
      "m4": "10.3"
    },
    {
      "p": "[On Time Domain Conformer Models for Monaural Speech Separation in Noisy Reverberant Acoustic Environments](https://arxiv.org/abs/2310.06125v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/pubsep)",
      "n": "TD-Confomer (S)",
      "d": "2023-10-09",
      "m1": "10.5"
    },
    {
      "p": "[Deformable Temporal Convolutional Networks for Monaural Noisy Reverberant Speech Separation](https://arxiv.org/abs/2210.15305v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jwr1995/dtcn)",
      "n": "Deformable TCN + Shared Weights + Dynamic Mixing",
      "d": "2022-10-27",
      "m1": "10.1",
      "m2": "3.7",
      "m3": "1.3",
      "m4": "9.5"
    },
    {
      "p": "[WHAM!: Extending Speech Separation to Noisy Environments](https://arxiv.org/abs/1907.01160v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AkojimaSLP/Neural-mask-estimation)",
      "n": "Bi-LSTM-TASNET",
      "d": "2019-07-02",
      "m1": "9.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
