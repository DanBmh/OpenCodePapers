# text-summarization-on-x-sum

[Dataset Link](https://github.com/EdinburghNLP/XSum/tree/master/XSum-Dataset) \
Task Hierarchy: ['Text Summarization']

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
      "label": "ROUGE-1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "ROUGE-2",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "ROUGE-3",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "ROUGE-L",
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
      "p": "[Lift Yourself Up: Retrieval-augmented Text Generation with Self Memory](https://arxiv.org/abs/2305.02437v3)",
      "c": "[&check;&nbsp;Link](https://github.com/hannibal046/selfmemory)",
      "n": "Selfmem",
      "d": "2023-05-03",
      "m1": "50.30",
      "m2": "26.70",
      "m3": "41.60"
    },
    {
      "p": "[BRIO: Bringing Order to Abstractive Summarization](https://arxiv.org/abs/2203.16804v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yixinl7/brio)",
      "n": "BRIO",
      "d": "2022-03-31",
      "m1": "49.07",
      "m2": "25.59",
      "m3": "40.40"
    },
    {
      "p": "[SummaReranker: A Multi-Task Mixture-of-Experts Re-ranking Framework for Abstractive Summarization](https://arxiv.org/abs/2203.06569v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ntunlp/summareranker)",
      "n": "PEGASUS + SummaReranker",
      "d": "2022-03-13",
      "m1": "48.12",
      "m2": "24.95",
      "m4": "40.00"
    },
    {
      "p": "[SimCLS: A Simple Framework for Contrastive Learning of Abstractive Summarization](https://arxiv.org/abs/2106.01890v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yixinL7/SimCLS)",
      "n": "PEGASUS + SimCLS",
      "d": "2021-06-03",
      "m1": "47.61",
      "m2": "24.57",
      "m4": "39.44"
    },
    {
      "p": "[PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/abs/1912.08777v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "PEGASUSLARGE",
      "d": "2019-12-18",
      "m1": "47.21",
      "m2": "24.56"
    },
    {
      "p": "[Hierarchical Learning for Generation with Long Source Sequences](https://arxiv.org/abs/2104.07545v2)",
      "c": "",
      "n": "HAT-BART",
      "d": "2021-04-15",
      "m1": "45.92",
      "m2": "22.79"
    },
    {
      "p": "[BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BART",
      "d": "2019-10-29",
      "m1": "45.14",
      "m2": "22.27",
      "m3": "37.25"
    },
    {
      "p": "[Text Summarization with Pretrained Encoders](https://arxiv.org/abs/1908.08345v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nlpyang/PreSumm)",
      "n": "BertSumExtAbs",
      "d": "2019-08-22",
      "m1": "38.81",
      "m2": "16.50",
      "m3": "31.27"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "T-ConvS2S",
      "d": "2018-08-27",
      "m1": "31.89",
      "m2": "11.54",
      "m3": "25.75"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "Baseline : Extractive Oracle",
      "d": "2018-08-27",
      "m1": "29.79",
      "m2": "8.81",
      "m3": "22.66"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "PtGen",
      "d": "2018-08-27",
      "m1": "29.70",
      "m2": "9.21",
      "m3": "23.24"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "Seq2Seq",
      "d": "2018-08-27",
      "m1": "28.42",
      "m2": "8.77",
      "m3": "22.48"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "PtGen-Covg",
      "d": "2018-08-27",
      "m1": "28.10",
      "m2": "8.02",
      "m3": "21.72"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "Baseline : Lead-3",
      "d": "2018-08-27",
      "m1": "16.30",
      "m2": "1.60",
      "m3": "11.95"
    },
    {
      "p": "[Don't Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization](http://arxiv.org/abs/1808.08745v1)",
      "c": "[&check;&nbsp;Link](https://github.com/shashiongithub/XSum)",
      "n": "Baseline : Random",
      "d": "2018-08-27",
      "m1": "15.16",
      "m2": "1.78",
      "m3": "11.27"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-L (one-shot)",
      "d": "2023-05-17",
      "m2": "23.2"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-M (one-shot)",
      "d": "2023-05-17",
      "m2": "17.2"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-S (one-shot)",
      "d": "2023-05-17",
      "m2": "16.9"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
