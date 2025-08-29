# named-entity-recognition-on-slue

[Dataset Link](https://github.com/asappresearch/slue-toolkit) \
Task Hierarchy: ['Named Entity Recognition (NER)']

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
      "label": "F1 (%)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "label-F1 (%)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Text model",
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
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-L-LL60K (pipeline approach, uses LM)",
      "d": "2021-11-19",
      "m1": "69.6",
      "m2": "82.2",
      "m3": "DeBERTa-L"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-LS960 (pipeline approach, uses LM)",
      "d": "2021-11-19",
      "m1": "68.0",
      "m2": "79.8",
      "m3": "DeBERTa-L"
    },
    {
      "p": "[Wav2Seq: Pre-training Speech-to-Text Encoder-Decoder Models Using Pseudo Languages](https://arxiv.org/abs/2205.01086v1)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/wav2seq)",
      "n": "Wav2Seq (from HuBERT-large)",
      "d": "2022-05-02",
      "m1": "65.4"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-L-LL60K (e2e approach, uses LM)",
      "d": "2021-11-19",
      "m1": "64.8",
      "m2": "73.3",
      "m3": "N/A"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-LS960 (e2e approach, uses LM)",
      "d": "2021-11-19",
      "m1": "63.4",
      "m2": "71.7",
      "m3": "N/A"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "HuBERT-B-LS960 (e2e approach, uses LM)",
      "d": "2021-11-19",
      "m1": "61.9",
      "m2": "70.3",
      "m3": "N/A"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-VP100K (e2e approach, uses LM)",
      "d": "2021-11-19",
      "m1": "61.8",
      "m2": "69.8",
      "m3": "N/A"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-L-LL60K (pipeline approach)",
      "d": "2021-11-19",
      "m1": "57.8",
      "m2": "78.8",
      "m3": "DeBERTa-L"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-L-LL60K (e2e approach)",
      "d": "2021-11-19",
      "m1": "50.9",
      "m2": "64.7",
      "m3": "-"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-LS960 (e2e approach)",
      "d": "2021-11-19",
      "m1": "50.2",
      "m2": "64.0",
      "m3": "-"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "HuBERT-B-LS960 (e2e approach)",
      "d": "2021-11-19",
      "m1": "49.8",
      "m2": "62.9",
      "m3": "-"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-LS960 (pipeline approach)",
      "d": "2021-11-19",
      "m1": "49.5",
      "m2": "74.2",
      "m3": "DeBERTa-L"
    },
    {
      "p": "[SLUE: New Benchmark Tasks for Spoken Language Understanding Evaluation on Natural Speech](https://arxiv.org/abs/2111.10367v3)",
      "c": "[&check;&nbsp;Link](https://github.com/asappresearch/slue-toolkit)",
      "n": "W2V2-B-VP100K (e2e approach)",
      "d": "2021-11-19",
      "m1": "47.9",
      "m2": "60.8",
      "m3": "-"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
