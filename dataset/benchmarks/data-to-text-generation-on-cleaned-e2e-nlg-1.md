# data-to-text-generation-on-cleaned-e2e-nlg-1

[Dataset Link](http://www.macs.hw.ac.uk/InteractionLab/E2E/) \
Task Hierarchy: ['Data-to-Text Generation']

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
      "label": "BLEU (Test set)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "METEOR (Validation set)",
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
      "p": "[Control Prefixes for Parameter-Efficient Text Generation](https://arxiv.org/abs/2110.08329v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Yale-LILY/dart)",
      "n": "Control Prefixes (T5-large)",
      "d": "2021-10-15",
      "m1": "44.15"
    },
    {
      "p": "[Have Your Text and Use It Too! End-to-End Neural Data-to-Text Generation with Semantic Fidelity](https://arxiv.org/abs/2004.06577v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amazon-research/datatuner)",
      "n": "DataTuner_FC",
      "d": "2020-04-08",
      "m1": "43.6"
    },
    {
      "p": "[Semantic Noise Matters for Neural Natural Language Generation](https://arxiv.org/abs/1911.03905v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tuetschek/e2e-cleaning)",
      "n": "TGen",
      "d": "2019-11-10",
      "m1": "40.73"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "LSTM",
      "d": "2021-02-02",
      "m2": "0.394"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "TGen",
      "d": "2021-02-02",
      "m2": "0.391"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "BART",
      "d": "2021-02-02",
      "m2": "0.373"
    },
    {
      "p": "[The GEM Benchmark: Natural Language Generation, its Evaluation and Metrics](https://arxiv.org/abs/2102.01672v3)",
      "c": "",
      "n": "T5",
      "d": "2021-02-02",
      "m2": "0.369"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
