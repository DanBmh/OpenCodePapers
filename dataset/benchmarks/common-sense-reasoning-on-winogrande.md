# common-sense-reasoning-on-winogrande

[Dataset Link](http://winogrande.allenai.org/) \
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
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-32B 269B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "96.1"
    },
    {
      "p": "[UNICORN on RAINBOW: A Universal Commonsense Reasoning Model on a New Multitask Benchmark](https://arxiv.org/abs/2103.13009v1)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/rainbow)",
      "n": "Unicorn 11B (fine-tuned)",
      "d": "2021-03-24",
      "m1": "91.3"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "CompassMTL 567M with Tailor",
      "d": "2022-10-12",
      "m1": "90.5"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "CompassMTL 567M",
      "d": "2022-10-12",
      "m1": "89.6"
    },
    {
      "p": "[UnifiedQA: Crossing Format Boundaries With a Single QA System](https://arxiv.org/abs/2005.00700v3)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/unifiedqa)",
      "n": "UnifiedQA 11B (fine-tuned)",
      "d": "2020-05-02",
      "m1": "89.4"
    },
    {
      "p": "[The Claude 3 Model Family: Opus, Sonnet, Haiku](https://www.anthropic.com/news/claude-3-family)",
      "c": "",
      "n": "Claude 3 Opus (5-shot)",
      "d": "2024-03-04",
      "m1": "88.5"
    },
    {
      "p": "[GPT-4 Technical Report](https://arxiv.org/abs/2303.08774v5)",
      "c": "[&check;&nbsp;Link](https://github.com/openai/evals)",
      "n": "GPT-4 (5-shot)",
      "d": "2023-03-15",
      "m1": "87.5"
    },
    {
      "p": "[Task Compass: Scaling Multi-task Pre-training with Task Prefix](https://arxiv.org/abs/2210.06277v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cooelf/compassmtl)",
      "n": "ExDeBERTa 567M",
      "d": "2022-10-12",
      "m1": "87"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 13B + MixLoRA",
      "d": "2024-04-22",
      "m1": "86.3"
    },
    {
      "p": "[Mixture-of-Subspaces in Low-Rank Adaptation](https://arxiv.org/abs/2406.11909v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wutaiqiang/moslora)",
      "n": "LLaMA3 8B+MoSLoRA",
      "d": "2024-06-16",
      "m1": "85.8"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-L (1-shot)",
      "d": "2023-05-17",
      "m1": "83.0"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-3 8B + MixLoRA",
      "d": "2024-04-22",
      "m1": "82.1"
    },
    {
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-L 4.1B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "81.7"
    },
    {
      "p": "[GPT-4 Technical Report](https://arxiv.org/abs/2303.08774v5)",
      "c": "[&check;&nbsp;Link](https://github.com/openai/evals)",
      "n": "GPT-3.5 (5-shot)",
      "d": "2023-03-15",
      "m1": "81.6"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 540B (0-shot)",
      "d": "2022-04-05",
      "m1": "81.1"
    },
    {
      "p": "[Parameter-Efficient Sparsity Crafting from Dense to Mixture-of-Experts for Instruction Tuning on General Tasks](https://arxiv.org/abs/2401.02731v4)",
      "c": "[&check;&nbsp;Link](https://github.com/wuhy68/parameter-efficient-moe)",
      "n": "Camelidae-8\u00d734B",
      "d": "2024-01-05",
      "m1": "80.9"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-M (1-shot)",
      "d": "2023-05-17",
      "m1": "79.2"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "RoBERTa-Winogrande 355M (fine-tuned)",
      "d": "2019-07-24",
      "m1": "79.1"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-S (1-shot)",
      "d": "2023-05-17",
      "m1": "77.9"
    },
    {
      "p": "[Mixtral of Experts](https://arxiv.org/abs/2401.04088v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jingyaogong/minimind)",
      "n": "Mixtral 8x7B (0-shot)",
      "d": "2024-01-08",
      "m1": "77.2"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 62B (0-shot)",
      "d": "2022-04-05",
      "m1": "77.0"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM-cont 62B (0-shot)",
      "d": "2022-04-05",
      "m1": "77.0"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 65B (0-shot)",
      "d": "2023-02-27",
      "m1": "77.0"
    },
    {
      "p": "[MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TUDB-Labs/MixLoRA)",
      "n": "LLaMA-2 7B + MixLoRA",
      "d": "2024-04-22",
      "m1": "76.8"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 33B (0-shot)",
      "d": "2023-02-27",
      "m1": "76.0"
    },
    {
      "p": "[Mistral 7B](https://arxiv.org/abs/2310.06825v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mistralai/mistral-src)",
      "n": "Mistral 7B (0-shot)",
      "d": "2023-10-10",
      "m1": "75.3"
    },
    {
      "p": "[The Claude 3 Model Family: Opus, Sonnet, Haiku](https://www.anthropic.com/news/claude-3-family)",
      "c": "",
      "n": "Claude 3 Sonnet (5-shot)",
      "d": "2024-03-04",
      "m1": "75.1"
    },
    {
      "p": "[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556v1)",
      "c": "[&check;&nbsp;Link](https://github.com/karpathy/llama2.c)",
      "n": "Chinchilla 70B (0-shot)",
      "d": "2022-03-29",
      "m1": "74.9"
    },
    {
      "p": "[The Claude 3 Model Family: Opus, Sonnet, Haiku](https://www.anthropic.com/news/claude-3-family)",
      "c": "",
      "n": "Claude 3 Haiku (5-shot)",
      "d": "2024-03-04",
      "m1": "74.2"
    },
    {
      "p": "[Mixtral of Experts](https://arxiv.org/abs/2401.04088v1)",
      "c": "[&check;&nbsp;Link](https://github.com/jingyaogong/minimind)",
      "n": "Mistral 7B (0-shot)",
      "d": "2024-01-08",
      "m1": "74.2"
    },
    {
      "p": "[Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463v1)",
      "c": "[&check;&nbsp;Link](https://github.com/knowlab/bi-weekly-paper-presentation)",
      "n": "phi-1.5-web 1.3B (zero-shot)",
      "d": "2023-09-11",
      "m1": "74.0"
    },
    {
      "p": "[UnifiedQA: Crossing Format Boundaries With a Single QA System](https://arxiv.org/abs/2005.00700v3)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/unifiedqa)",
      "n": "Unified QA 406M (fine-tuned)",
      "d": "2020-05-02",
      "m1": "73.3"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 13B (0-shot)",
      "d": "2023-02-27",
      "m1": "73.0"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (few-shot, k=16)",
      "d": "2021-09-03",
      "m1": "72.8"
    },
    {
      "p": "[Generative Data Augmentation for Commonsense Reasoning](https://arxiv.org/abs/2004.11546v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangyiben/G-DAUG-c-Generative-Data-Augmentation-for-Commonsense-Reasoning)",
      "n": "G-DAUG-Combo + RoBERTa-Large",
      "d": "2020-04-24",
      "m1": "71.4"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (0-shot)",
      "d": "2021-09-03",
      "m1": "71.2"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "RWKV v5 Eagle 7B",
      "d": null,
      "m1": "70.8"
    },
    {
      "p": "[Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM](https://arxiv.org/abs/2403.07816v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Leeroo-AI/mergoo)",
      "n": "Branch-Train-MiX 4x7B (sampling top-1 expert)",
      "d": "2024-03-12",
      "m1": "70.6"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 175B (0-shot)",
      "d": "2020-05-28",
      "m1": "70.2"
    },
    {
      "p": "[Scaling Language Models: Methods, Analysis & Insights from Training Gopher](https://arxiv.org/abs/2112.11446v2)",
      "c": "[&check;&nbsp;Link](https://github.com/allenai/dolma)",
      "n": "Gopher 280B (0-shot)",
      "d": "2021-12-08",
      "m1": "70.1"
    },
    {
      "p": "[LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LLaMA 7B (0-shot)",
      "d": "2023-02-27",
      "m1": "70.1"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "BLOOM 176B (1-shot)",
      "d": "2023-03-30",
      "m1": "67"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 12B (5-shot)",
      "d": "2023-04-03",
      "m1": "66.6"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "OPT 66B (1-shot)",
      "d": "2023-03-30",
      "m1": "66.1"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "BERT-Winogrande 345M (fine-tuned)",
      "d": "2019-07-24",
      "m1": "64.9"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "Bloomberg GPT (one-shot)",
      "d": "2023-03-30",
      "m1": "64.1"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 12B (0-shot)",
      "d": "2023-04-03",
      "m1": "63.9"
    },
    {
      "p": "[Exploring the Benefits of Training Expert Language Models over Instruction Tuning](https://arxiv.org/abs/2302.03202v2)",
      "c": "[&check;&nbsp;Link](https://github.com/joeljang/rlphf)",
      "n": "RoE-3B",
      "d": "2023-02-07",
      "m1": "61.60"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 6.9B (0-shot)",
      "d": "2023-04-03",
      "m1": "60.9"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "GPT-NeoX (one-shot)",
      "d": "2023-03-30",
      "m1": "60.6"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "FLAN-T5-Large 783M",
      "d": "2023-04-27",
      "m1": "59.9"
    },
    {
      "p": "[Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling](https://arxiv.org/abs/2304.01373v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Lightning-AI/lit-gpt)",
      "n": "Pythia 2.8B (0-shot)",
      "d": "2023-04-03",
      "m1": "59.4"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "RoBERTa-DPR 355M (0-shot)",
      "d": "2019-07-24",
      "m1": "58.9"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "ALBERT-xxlarge 235M",
      "d": "2021-04-16",
      "m1": "58.7"
    },
    {
      "p": "[Guess the Instruction! Flipped Learning Makes Language Models Stronger Zero-Shot Learners](https://arxiv.org/abs/2210.02969v4)",
      "c": "[&check;&nbsp;Link](https://github.com/seonghyeonye/flipped-learning)",
      "n": "Flipped-3B",
      "d": "2022-10-06",
      "m1": "58.56"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "GPT-2-XL 1.5B",
      "d": "2023-04-27",
      "m1": "58.3"
    },
    {
      "p": "[The CoT Collection: Improving Zero-shot and Few-shot Learning of Language Models via Chain-of-Thought Fine-Tuning](https://arxiv.org/abs/2305.14045v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kaistai/cot-collection)",
      "n": "T0-3B (CoT fine-tuned)",
      "d": "2023-05-23",
      "m1": "57.5"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 Large 760M (0-shot)",
      "d": "2020-05-28",
      "m1": "57.4"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "RoBERTa-base 125M",
      "d": "2021-04-16",
      "m1": "56.3"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "LaMini-F-T5 783M",
      "d": "2023-04-27",
      "m1": "56"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "LaMini-GPT 1.5B",
      "d": "2023-04-27",
      "m1": "56"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "BERT-large 345M",
      "d": "2021-04-16",
      "m1": "55.6"
    },
    {
      "p": "[Knowledge-in-Context: Towards Knowledgeable Semi-Parametric Language Models](https://arxiv.org/abs/2210.16433v3)",
      "c": "",
      "n": "KiC-770M",
      "d": "2022-10-28",
      "m1": "55.30"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "T5-Large 738M",
      "d": "2023-04-27",
      "m1": "55.2"
    },
    {
      "p": "[LaMini-LM: A Diverse Herd of Distilled Models from Large-Scale Instructions](https://arxiv.org/abs/2304.14402v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mbzuai-nlp/lamini-lm)",
      "n": "LaMini-T5 738M",
      "d": "2023-04-27",
      "m1": "54.9"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "RoBERTa-large 355M",
      "d": "2021-04-16",
      "m1": "54.9"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "sMLP \u2013 deterministic 9.4B (0-shot)",
      "d": "2022-03-14",
      "m1": "54.3"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Switch Transformer 9B (0-shot)",
      "d": "2022-03-14",
      "m1": "53.4"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "BERT-base 110M",
      "d": "2021-04-16",
      "m1": "53.1"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "ALBERT-base 11M",
      "d": "2021-04-16",
      "m1": "52.8"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "BERT-large 345M (0-shot)",
      "d": "2019-07-24",
      "m1": "51.9"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "HASH Layers 10B (0-shot)",
      "d": "2022-03-14",
      "m1": "51.7"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Gshard 9B (0-shot)",
      "d": "2022-03-14",
      "m1": "51.1"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Base Layers 10B (0-shot)",
      "d": "2022-03-14",
      "m1": "51"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "BERT-DPR 345M (0-shot)",
      "d": "2019-07-24",
      "m1": "51"
    },
    {
      "p": "[Back to Square One: Artifact Detection, Training and Commonsense Disentanglement in the Winograd Schema](https://arxiv.org/abs/2104.08161v2)",
      "c": "",
      "n": "Random baseline",
      "d": "2021-04-16",
      "m1": "50"
    },
    {
      "p": "[WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vered1986/self_talk)",
      "n": "RoBERTa-large 355M (0-shot)",
      "d": "2019-07-24",
      "m1": "50"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
