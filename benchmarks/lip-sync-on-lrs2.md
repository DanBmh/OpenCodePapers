# lip-sync-on-lrs2

[Dataset Link](https://www.robots.ox.ac.uk/~vgg/data/lip_reading/lrs2.html) \
Task Hierarchy: ['10-shot image generation', 'Talking Head Generation', 'Unconstrained Lip-synchronization']

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
      "label": "FID",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "LSE-D",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "LSE-C",
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
      "p": "[MARLIN: Masked Autoencoder for facial video Representation LearnINg](https://arxiv.org/abs/2211.06627v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ControlNet/MARLIN)",
      "n": "Wav2Lip + ViT + MARLIN",
      "d": "2022-11-12",
      "m1": "3.452",
      "m2": "7.127",
      "m3": "5.528"
    },
    {
      "p": "[A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild](https://arxiv.org/abs/2008.10010v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Rudrabha/Wav2Lip)",
      "n": "Wav2Lip + GAN",
      "d": "2020-08-23",
      "m1": "4.446",
      "m2": "6.469"
    },
    {
      "p": "[A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild](https://arxiv.org/abs/2008.10010v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Rudrabha/Wav2Lip)",
      "n": "Wav2Lip",
      "d": "2020-08-23",
      "m1": "4.887",
      "m2": "6.386",
      "m3": "7.781"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
