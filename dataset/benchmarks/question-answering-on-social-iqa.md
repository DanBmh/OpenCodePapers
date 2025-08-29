# question-answering-on-social-iqa

[Dataset Link](https://leaderboard.allenai.org/socialiqa/submissions/public) \
Task Hierarchy: ['Question Answering']

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
      "p": "[UNICORN on RAINBOW: A Universal Commonsense Reasoning Model on a New Multitask Benchmark](https://arxiv.org/abs/2103.13009v1)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/rainbow)",
      "n": "Unicorn 11B (fine-tuned)",
      "d": "2021-03-24",
      "m1": "83.2"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 13B + MixLoRA",
      "d": "2024-04-22",
      "m1": "82.5"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "CompassMTL 567M with Tailor",
      "d": "2022-10-12",
      "m1": "82.2"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "CompassMTL 567M",
      "d": "2022-10-12",
      "m1": "81.7"
    },
    {
      "p": "[Mixture-of-Subspaces in Low-Rank Adaptation](https://arxiv.org/abs/2406.11909v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wutaiqiang/moslora)",
      "n": "LLaMA-3 8B+MoSLoRA (fine-tuned)",
      "d": "2024-06-16",
      "m1": "81.0"
    },
    {
      "p": "[Two is Better than Many? Binary Classification as an Effective Approach to Multi-Choice Question Answering](https://arxiv.org/abs/2210.16495v1)",
      "c": "[&check;&nbsp;Link](https://github.com/declare-lab/team)",
      "n": "DeBERTa-Large 304M",
      "d": "2022-10-29",
      "m1": "80.2"
    },
    {
      "p": "[Two is Better than Many? Binary Classification as an Effective Approach to Multi-Choice Question Answering](https://arxiv.org/abs/2210.16495v1)",
      "c": "[&check;&nbsp;Link](https://github.com/declare-lab/team)",
      "n": "DeBERTa-Large 304M (classification-based)",
      "d": "2022-10-29",
      "m1": "79.9"
    },
    {
      "p": "[UnifiedQA: Crossing Format Boundaries With a Single QA System](https://arxiv.org/abs/2005.00700v3)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/unifiedqa)",
      "n": "UnifiedQA 3B",
      "d": "2020-05-02",
      "m1": "79.8"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "ExDeBERTa 567M",
      "d": "2022-10-12",
      "m1": "79.6"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-3 8B + MixLoRA",
      "d": "2024-04-22",
      "m1": "78.8"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 7B + MixLoRA",
      "d": "2024-04-22",
      "m1": "78"
    },
    {
      "p": "[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "RoBERTa-Large 355M (fine-tuned)",
      "d": "2019-07-26",
      "m1": "76.7"
    },
    {
      "p": "[SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728v3)",
      "c": "[&check;&nbsp;Link](https://github.com/clear-nus/llm-human-model)",
      "n": "BERT-large 340M (fine-tuned)",
      "d": "2019-04-22",
      "m1": "64.5"
    },
    {
      "p": "[SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728v3)",
      "c": "[&check;&nbsp;Link](https://github.com/clear-nus/llm-human-model)",
      "n": "BERT-base 110M (fine-tuned)",
      "d": "2019-04-22",
      "m1": "63.1"
    },
    {
      "p": "[SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728v3)",
      "c": "[&check;&nbsp;Link](https://github.com/clear-nus/llm-human-model)",
      "n": "GPT-1 117M (fine-tuned)",
      "d": "2019-04-22",
      "m1": "63"
    },
    {
      "p": "[Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463v1)",
      "c": "[&check;&nbsp;Link](https://github.com/knowlab/bi-weekly-paper-presentation)",
      "n": "phi-1.5-web 1.3B (zero-shot)",
      "d": "2023-09-11",
      "m1": "53.0"
    },
    {
      "p": "[Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463v1)",
      "c": "[&check;&nbsp;Link](https://github.com/knowlab/bi-weekly-paper-presentation)",
      "n": "phi-1.5 1.3B (zero-shot)",
      "d": "2023-09-11",
      "m1": "52.6"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 65B (zero-shot)",
      "d": "2023-02-27",
      "m1": "52.3"
    },
    {
      "p": "[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556v1)",
      "c": "[&check;&nbsp;Link](https://github.com/karpathy/llama2.c)",
      "n": "Chinchilla (zero-shot)",
      "d": "2022-03-29",
      "m1": "51.3"
    },
    {
      "p": "[Scaling Language Models: Methods, Analysis & Insights from Training Gopher](https://arxiv.org/abs/2112.11446v2)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/dolma)",
      "n": "Gopher (zero-shot)",
      "d": "2021-12-08",
      "m1": "50.6"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 13B (zero-shot)",
      "d": "2023-02-27",
      "m1": "50.4"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 33B (zero-shot)",
      "d": "2023-02-27",
      "m1": "50.4"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 7B (zero-shot)",
      "d": "2023-02-27",
      "m1": "48.9"
    },
    {
      "p": "[SocialIQA: Commonsense Reasoning about Social Interactions](https://arxiv.org/abs/1904.09728v3)",
      "c": "[&check;&nbsp;Link](https://github.com/clear-nus/llm-human-model)",
      "n": "Random chance baseline",
      "d": "2019-04-22",
      "m1": "33.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
