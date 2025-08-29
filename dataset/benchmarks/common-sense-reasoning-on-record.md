# common-sense-reasoning-on-record

[Dataset Link](https://sheng-z.github.io/ReCoRD-explorer/) \
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
      "label": "EM",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "F1",
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
      "p": "[Toward Efficient Language Model Pretraining and Downstream Adaptation via Self-Evolution: A Case Study on SuperGLUE](https://arxiv.org/abs/2212.01853v1)",
      "c": "",
      "n": "Turing NLR v5 XXL 5.4B (fine-tuned)",
      "d": "2022-12-04",
      "m1": "95.9",
      "m2": "96.4"
    },
    {
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-32B 269B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "95.1"
    },
    {
      "p": "[DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654v6)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DeBERTa-1.5B",
      "d": "2020-06-05",
      "m1": "94.1",
      "m2": "94.5"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM 540B (finetuned) ",
      "d": "2022-04-05",
      "m1": "94.0",
      "m2": "94.6"
    },
    {
      "p": "[Toward Efficient Language Model Pretraining and Downstream Adaptation via Self-Evolution: A Case Study on SuperGLUE](https://arxiv.org/abs/2212.01853v1)",
      "c": "",
      "n": "Vega v2 6B (fine-tuned)",
      "d": "2022-12-04",
      "m1": "93.9",
      "m2": "94.4"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-XXL 11B (fine-tuned)",
      "d": "2019-10-23",
      "m1": "93.4"
    },
    {
      "p": "[Integrating a Heterogeneous Graph with Entity-aware Self-attention using Relative Position Labels for Reading Comprehension Model](https://arxiv.org/abs/2307.10443v3)",
      "c": "",
      "n": "GESA 500M",
      "d": "2023-07-19",
      "m1": "91.7",
      "m2": "92.2"
    },
    {
      "p": "[LUKE-Graph: A Transformer-based Approach with Gated Relational Graph Attention for Cloze-style Reading Comprehension](https://arxiv.org/abs/2303.06675v1)",
      "c": "",
      "n": "LUKE-Graph",
      "d": "2023-03-12",
      "m1": "91.2",
      "m2": "91.5"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LUKE (single model)",
      "d": null,
      "m1": "90.640",
      "m2": "91.209"
    },
    {
      "p": "[LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://arxiv.org/abs/2010.01057v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "LUKE 483M",
      "d": "2020-10-02",
      "m1": "90.6",
      "m2": "91.2"
    },
    {
      "p": "[KELM: Knowledge Enhanced Pre-Trained Language Representations with Message Passing on Hierarchical Relational Graphs](https://arxiv.org/abs/2109.04223v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nlp-anonymous-happy/anonymous-kg-guided-nlp)",
      "n": "KELM (finetuning RoBERTa-large based single model)",
      "d": "2021-09-09",
      "m1": "89.1",
      "m2": "89.6"
    },
    {
      "p": "[ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/mesh)",
      "n": "ST-MoE-L 4.1B (fine-tuned)",
      "d": "2022-02-17",
      "m1": "88.9"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (prompt-tuned)",
      "d": "2021-09-03",
      "m1": "85.1"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "XLNet + MTL + Verifier (ensemble)",
      "d": null,
      "m1": "83.090",
      "m2": "83.737"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3 Large 760M (0-shot)",
      "d": "2020-05-28",
      "m1": "82.1"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "CSRLM (single model)",
      "d": null,
      "m1": "81.780",
      "m2": "82.584"
    },
    {
      "p": "[Pingan Smart Health and SJTU at COIN - Shared Task: utilizing Pre-trained Language Models and Common-sense Knowledge in Machine Reading Tasks](https://aclanthology.org/D19-6011)",
      "c": "",
      "n": "XLNet + Verifier",
      "d": "2019-11-01",
      "m1": "81.5",
      "m2": "82.7"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "XLNet + MTL + Verifier (single model)",
      "d": null,
      "m1": "81.460",
      "m2": "82.664"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Switch Transformer 9B",
      "d": "2022-03-14",
      "m1": "79.9"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "{SKG-NET} (single model)",
      "d": null,
      "m1": "79.480",
      "m2": "80.038"
    },
    {
      "p": "[KELM: Knowledge Enhanced Pre-Trained Language Representations with Message Passing on Hierarchical Relational Graphs](https://arxiv.org/abs/2109.04223v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nlp-anonymous-happy/anonymous-kg-guided-nlp)",
      "n": "KELM (finetuning BERT-large based single model)",
      "d": "2021-09-09",
      "m1": "76.2",
      "m2": "76.7"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "sMLP \u2013 deterministic 9.4B (0-shot)",
      "d": "2022-03-14",
      "m1": "73.4"
    },
    {
      "p": "[Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652v5)",
      "c": "[&check;&nbsp;Link](https://github.com/hiyouga/llama-efficient-tuning)",
      "n": "FLAN 137B (zero-shot)",
      "d": "2021-09-03",
      "m1": "72.5"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Gshard 9B",
      "d": "2022-03-14",
      "m1": "72.4"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "SKG-BERT (single model)",
      "d": null,
      "m1": "72.240",
      "m2": "72.778"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "KT-NET (single model)",
      "d": null,
      "m1": "71.600",
      "m2": "73.620"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "DCReader+BERT (single model)",
      "d": null,
      "m1": "69.490",
      "m2": "71.138"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "HASH Layers 10B (0-shot)",
      "d": "2022-03-14",
      "m1": "67.2"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GraphBert (single)",
      "d": null,
      "m1": "60.800",
      "m2": "62.986"
    },
    {
      "p": "[Efficient Language Modeling with Sparse all-MLP](https://arxiv.org/abs/2203.06850v3)",
      "c": "",
      "n": "Base Layers 10B (0-shot)",
      "d": "2022-03-14",
      "m1": "60.7"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GraphBert-WordNet (single)",
      "d": null,
      "m1": "59.860",
      "m2": "61.885"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GraphBert-NELL (single)",
      "d": null,
      "m1": "59.410",
      "m2": "61.515"
    },
    {
      "p": "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BERT-Base (single model)",
      "d": "2018-10-11",
      "m1": "54.040",
      "m2": "56.065"
    },
    {
      "p": "[ReCoRD: Bridging the Gap between Human and Machine Commonsense Reading Comprehension](http://arxiv.org/abs/1810.12885v1)",
      "c": "",
      "n": "DocQA + ELMo",
      "d": "2018-10-30",
      "m1": "45.4",
      "m2": "46.7"
    },
    {
      "p": "[N-Grammer: Augmenting Transformers with latent n-grams](https://arxiv.org/abs/2207.06366v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/lingvo)",
      "n": "N-Grammer 343M",
      "d": "2022-07-13",
      "m1": "28.9",
      "m2": "29.9"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-11B",
      "d": "2019-10-23",
      "m2": "94.1"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-L (one-shot)",
      "d": "2023-05-17",
      "m2": "93.8"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-M (one-shot)",
      "d": "2023-05-17",
      "m2": "92.4"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-S (one-shot)",
      "d": "2023-05-17",
      "m2": "92.1"
    },
    {
      "p": "[Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916v4)",
      "c": "[&check;&nbsp;Link](https://github.com/kojima-takeshi188/zero_shot_cot)",
      "n": "GPT-3 175B (one-shot)",
      "d": "2022-05-24",
      "m2": "90.2"
    },
    {
      "p": "[AlexaTM 20B: Few-Shot Learning Using a Large-Scale Multilingual Seq2Seq Model](https://arxiv.org/abs/2208.01448v2)",
      "c": "[&check;&nbsp;Link](https://github.com/amazon-science/alexa-teacher-models)",
      "n": "AlexaTM 20B",
      "d": "2022-08-02",
      "m2": "88.4"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "Bloomberg GPT 50B (1-shot)",
      "d": "2023-03-30",
      "m2": "82.8"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "OPT 66B (1-shot)",
      "d": "2023-03-30",
      "m2": "82.5"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "BLOOM 176B (1-shot)",
      "d": "2023-03-30",
      "m2": "78"
    },
    {
      "p": "[BloombergGPT: A Large Language Model for Finance](https://arxiv.org/abs/2303.17564v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yangletliu/finlora)",
      "n": "GPT-NeoX 20B (1-shot)",
      "d": "2023-03-30",
      "m2": "67.9"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
