# common-sense-reasoning-on-arc-challenge

[Dataset Link](https://allenai.org/data/arc) \
Task Hierarchy: ['Common Sense Reasoning']

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
      "p": "[GPT-4 Technical Report](https://arxiv.org/abs/2303.08774v5)",
      "c": "[&check;&nbsp;Link](https://github.com/openai/evals)",
      "n": "GPT-4 (few-shot, k=25)",
      "d": "2023-03-15",
      "m1": "96.4"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2 (few-shot, CoT, SC)",
      "d": "2023-05-17",
      "m1": "95.1"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Shivaay (4B, few-shot, k=8)",
      "d": null,
      "m1": "91.04"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "StupidLLM",
      "d": null,
      "m1": "91.03"
    },
    {
      "p": "[Model Card and Evaluations for Claude Models](https://www-files.anthropic.com/production/images/Model-Card-Claude-2.pdf)",
      "c": "",
      "n": "Claude 2 (few-shot, k=5)",
      "d": "2023-07-11",
      "m1": "91"
    },
    {
      "p": "[Model Card and Evaluations for Claude Models](https://www-files.anthropic.com/production/images/Model-Card-Claude-2.pdf)",
      "c": "",
      "n": "Claude 1.3 (few-shot, k=5)",
      "d": "2023-07-11",
      "m1": "90"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (Self Improvement, Self Consistency)",
      "d": "2022-10-20",
      "m1": "89.8"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (Self Consistency)",
      "d": "2022-10-20",
      "m1": "88.7"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (Self Improvement, CoT Prompting)",
      "d": "2022-10-20",
      "m1": "88.3"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (Self Improvement, Standard-Prompting)",
      "d": "2022-10-20",
      "m1": "87.2"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (Standard-Prompting)",
      "d": "2022-10-20",
      "m1": "87.1"
    },
    {
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-32B 269B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "86.5"
    },
    {
      "p": "[Model Card and Evaluations for Claude Models](https://www-files.anthropic.com/production/images/Model-Card-Claude-2.pdf)",
      "c": "",
      "n": "Claude Instant 1.1 (few-shot, k=5)",
      "d": "2023-07-11",
      "m1": "85.7"
    },
    {
      "p": "[GPT-4 Technical Report](https://arxiv.org/abs/2303.08774v5)",
      "c": "[&check;&nbsp;Link](https://github.com/openai/evals)",
      "n": "GPT-3.5 (few-shot, k=25)",
      "d": "2023-03-15",
      "m1": "85.2"
    },
    {
      "p": "[Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610v2)",
      "c": "",
      "n": "PaLM 540B (CoT Prompting)",
      "d": "2022-10-20",
      "m1": "85.2"
    },
    {
      "p": "[Mixture-of-Subspaces in Low-Rank Adaptation](https://arxiv.org/abs/2406.11909v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wutaiqiang/moslora)",
      "n": "LLaMA 3 8B + MoSLoRA (fine-tuned)",
      "d": "2024-06-16",
      "m1": "81.5"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-3 8B + MixLoRA",
      "d": "2024-04-22",
      "m1": "79.9"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 13B + MixLoRA",
      "d": "2024-04-22",
      "m1": "69.9"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-L (1-shot)",
      "d": "2023-05-17",
      "m1": "69.2"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "GAL 120B (zero-shot)",
      "d": "2022-11-16",
      "m1": "67.9"
    },
    {
      "p": "[Parameter-Efficient Sparsity Crafting from Dense to Mixture-of-Experts for Instruction Tuning on General Tasks](https://arxiv.org/abs/2401.02731v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wuhy68/parameter-efficient-moe)",
      "n": "Camelidae-8\u00d734B",
      "d": "2024-01-05",
      "m1": "65.2"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-M (1-shot)",
      "d": "2023-05-17",
      "m1": "64.9"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (few-shot, k=13)",
      "d": "2021-09-03",
      "m1": "63.8"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (zero-shot)",
      "d": "2021-09-03",
      "m1": "63.1"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-S (1-shot)",
      "d": "2023-05-17",
      "m1": "59.6"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 7B + MixLoRA",
      "d": "2024-04-22",
      "m1": "58.1"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 33B (zero-shot)",
      "d": "2023-02-27",
      "m1": "57.8"
    },
    {
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-L 4.1B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "56.9"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 65B (zero-shot)",
      "d": "2023-02-27",
      "m1": "56.0"
    },
    {
      "p": "[Mistral 7B](https://arxiv.org/abs/2310.06825v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mistralai/mistral-src)",
      "n": "Mistral 7B (0-shot)",
      "d": "2023-10-10",
      "m1": "55.5"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 175B (1 shot)",
      "d": "2020-05-28",
      "m1": "53.2"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 13B (zero-shot)",
      "d": "2023-02-27",
      "m1": "52.7"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "GPT-3 (zero-shot)",
      "d": "2022-11-16",
      "m1": "51.4"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 175B (0-shot)",
      "d": "2020-05-28",
      "m1": "51.4"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "BLOOM 176B (1-shot)",
      "d": "2023-03-30",
      "m1": "50.85"
    },
    {
      "p": "[GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06905v2)",
      "c": "",
      "n": "GLaM 64B/64E (0 shot)",
      "d": "2021-12-13",
      "m1": "50.3"
    },
    {
      "p": "[UL2: Unifying Language Learning Paradigms](https://arxiv.org/abs/2205.05131v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "UL2 20B (chain-of-thought + self-consistency)",
      "d": "2022-05-10",
      "m1": "49.5"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "Bloomberg GPT 50B (1-shot)",
      "d": "2023-03-30",
      "m1": "48.63"
    },
    {
      "p": "[GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06905v2)",
      "c": "",
      "n": "GLaM 64B/64E (1 shot)",
      "d": "2021-12-13",
      "m1": "48.2"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 7B (zero-shot)",
      "d": "2023-02-27",
      "m1": "47.6"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "GPT-NeoX 20B (1-shot)",
      "d": "2023-03-30",
      "m1": "45.39"
    },
    {
      "p": "[Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463v1)",
      "c": "[&check;&nbsp;Link](https://github.com/knowlab/bi-weekly-paper-presentation)",
      "n": "phi-1.5-web 1.3B (zero-shot)",
      "d": "2023-09-11",
      "m1": "44.9"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "OPT 66B (one-shot)",
      "d": "2023-03-30",
      "m1": "44.54"
    },
    {
      "p": "[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nvidia/tensorrt-model-optimizer)",
      "n": "OPT-175B",
      "d": "2023-01-02",
      "m1": "43.94"
    },
    {
      "p": "[UL2: Unifying Language Learning Paradigms](https://arxiv.org/abs/2205.05131v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "UL2 20B (chain-of-thought)",
      "d": "2022-05-10",
      "m1": "42.9"
    },
    {
      "p": "[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nvidia/tensorrt-model-optimizer)",
      "n": "SparseGPT (175B, 50% Sparsity)",
      "d": "2023-01-02",
      "m1": "41.3"
    },
    {
      "p": "[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nvidia/tensorrt-model-optimizer)",
      "n": "SparseGPT (175B, 4:8 Sparsity)",
      "d": "2023-01-02",
      "m1": "39.85"
    },
    {
      "p": "[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nvidia/tensorrt-model-optimizer)",
      "n": "SparseGPT (175B, 2:4 Sparsity)",
      "d": "2023-01-02",
      "m1": "38.99"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 12B (5-shot)",
      "d": "2023-04-03",
      "m1": "36.8"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "BLOOM (few-shot, k=5)",
      "d": "2022-11-16",
      "m1": "32.9"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 12B (0-shot)",
      "d": "2023-04-03",
      "m1": "31.8"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "OPT (few-shot, k=5)",
      "d": "2022-11-16",
      "m1": "31.1"
    },
    {
      "p": "[UL2: Unifying Language Learning Paradigms](https://arxiv.org/abs/2205.05131v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "UL2 20B (zero-shot)",
      "d": "2022-05-10",
      "m1": "29.8"
    },
    {
      "p": "[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nvidia/tensorrt-model-optimizer)",
      "n": "OPT-175B (50% Sparsity)",
      "d": "2023-01-02",
      "m1": "25.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
