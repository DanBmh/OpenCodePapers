# reading-comprehension-on-race

[Dataset Link](https://www.cs.cmu.edu/~glai1/data/race/) \
Task Hierarchy: ['Reading Comprehension']

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
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy (Middle)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Accuracy (High)",
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
      "p": "[Improving Machine Reading Comprehension with Single-choice Decision and Transfer Learning](https://arxiv.org/abs/2011.03292v2)",
      "c": "",
      "n": "ALBERT (Ensemble)",
      "d": "2020-11-06",
      "m1": "91.4"
    },
    {
      "p": "[Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053v4)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/Megatron-LM)",
      "n": "Megatron-BERT (ensemble)",
      "d": "2019-09-17",
      "m1": "90.9",
      "m2": "93.1",
      "m3": "90.0"
    },
    {
      "p": "[DUMA: Reading Comprehension with Transposition Thinking](https://arxiv.org/abs/2001.09415v5)",
      "c": "[&check;&nbsp;Link](https://github.com/pfZhu/duma_code)",
      "n": "ALBERTxxlarge+DUMA(ensemble)",
      "d": "2020-01-26",
      "m1": "89.8",
      "m2": "88.7",
      "m3": "92.6"
    },
    {
      "p": "[Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053v4)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/Megatron-LM)",
      "n": "Megatron-BERT",
      "d": "2019-09-17",
      "m1": "89.5",
      "m2": "91.8",
      "m3": "88.6"
    },
    {
      "p": "[DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654v6)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DeBERTalarge",
      "d": "2020-06-05",
      "m1": "86.8"
    },
    {
      "p": "[Funnel-Transformer: Filtering out Sequential Redundancy for Efficient Language Processing](https://arxiv.org/abs/2006.03236v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "B10-10-10",
      "d": "2020-06-05",
      "m1": "85.7",
      "m2": "88.8",
      "m3": "84.4"
    },
    {
      "p": "[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "RoBERTa",
      "d": "2019-07-26",
      "m1": "83.2",
      "m2": "86.5",
      "m3": "81.3"
    },
    {
      "p": "[Orca 2: Teaching Small Language Models How to Reason](https://arxiv.org/abs/2311.11045v2)",
      "c": "",
      "n": "Orca 2-13B",
      "d": "2023-11-18",
      "m1": "82.87"
    },
    {
      "p": "[Orca 2: Teaching Small Language Models How to Reason](https://arxiv.org/abs/2311.11045v2)",
      "c": "",
      "n": "Orca 2-7B",
      "d": "2023-11-18",
      "m1": "80.79"
    },
    {
      "p": "[Hierarchical Learning for Generation with Long Source Sequences](https://arxiv.org/abs/2104.07545v2)",
      "c": "",
      "n": "HAT (Encoder)",
      "d": "2021-04-15",
      "m1": "67.3"
    },
    {
      "p": "[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "XLNet",
      "d": "2019-06-19",
      "m2": "88.6",
      "m3": "84.0"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 540B (zero-shot)",
      "d": "2022-04-05",
      "m2": "68.1",
      "m3": "49.1"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 65B (zero-shot)",
      "d": "2023-02-27",
      "m2": "67.9",
      "m3": "51.6"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 62B (zero-shot)",
      "d": "2022-04-05",
      "m2": "64.3",
      "m3": "47.5"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 33B (zero-shot)",
      "d": "2023-02-27",
      "m2": "64.1",
      "m3": "48.3"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 13B (zero-shot)",
      "d": "2023-02-27",
      "m2": "61.6",
      "m3": "47.2"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 7B (zero-shot)",
      "d": "2023-02-27",
      "m2": "61.1",
      "m3": "46.9"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 175B (0-shot)",
      "d": "2020-05-28",
      "m2": "58.4"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 8B (zero-shot)",
      "d": "2022-04-05",
      "m2": "57.9",
      "m3": "42.3"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "Bloomberg GPT (one-shot)",
      "d": "2023-03-30",
      "m2": "54.32",
      "m3": "41.74"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "BLOOM 176B (one-shot)",
      "d": "2023-03-30",
      "m2": "52.3",
      "m3": "39.14"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "OPT 66B (one-shot)",
      "d": "2023-03-30",
      "m2": "47.42",
      "m3": "37.02"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "GPT-NeoX (one-shot)",
      "d": "2023-03-30",
      "m2": "41.23",
      "m3": "34.33"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 175B (zero-shot)",
      "d": "2020-05-28",
      "m3": "45.5"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
