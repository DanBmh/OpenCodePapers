# question-answering-on-medqa-usmle

[Dataset Link](https://drive.google.com/file/d/1ImYUSLk9JbgHXOemfvyiDiirluZHPeQw/view) \
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
      "p": "[Capabilities of Gemini Models in Medicine](https://arxiv.org/abs/2404.18416v2)",
      "c": "",
      "n": "Med-Gemini",
      "d": "2024-04-29",
      "m1": "91.1"
    },
    {
      "p": "[Can Generalist Foundation Models Outcompete Special-Purpose Tuning? Case Study in Medicine](https://arxiv.org/abs/2311.16452v1)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/promptbase)",
      "n": "GPT-4",
      "d": "2023-11-28",
      "m1": "90.2"
    },
    {
      "p": "[Towards Expert-Level Medical Question Answering with Large Language Models](https://arxiv.org/abs/2305.09617v1)",
      "c": "[&check;&nbsp;Link](https://github.com/m42-health/med42)",
      "n": "Med-PaLM 2",
      "d": "2023-05-16",
      "m1": "85.4"
    },
    {
      "p": "[Towards Expert-Level Medical Question Answering with Large Language Models](https://arxiv.org/abs/2305.09617v1)",
      "c": "[&check;&nbsp;Link](https://github.com/m42-health/med42)",
      "n": "Med-PaLM 2 (CoT + SC)",
      "d": "2023-05-16",
      "m1": "83.7"
    },
    {
      "p": "[Towards Expert-Level Medical Question Answering with Large Language Models](https://arxiv.org/abs/2305.09617v1)",
      "c": "[&check;&nbsp;Link](https://github.com/m42-health/med42)",
      "n": "Med-PaLM 2 (5-shot)",
      "d": "2023-05-16",
      "m1": "79.7"
    },
    {
      "p": "[MedMobile: A mobile-sized language model with expert-level clinical capabilities](https://arxiv.org/abs/2410.09019v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nyuolab/MedMobile)",
      "n": "MedMobile (3.8B)",
      "d": "2024-10-11",
      "m1": "75.7"
    },
    {
      "p": "[Small Language Models Learn Enhanced Reasoning Skills from Medical Textbooks](https://arxiv.org/abs/2404.00376v2)",
      "c": "",
      "n": "Meerkat-7B",
      "d": "2024-03-30",
      "m1": "74.3"
    },
    {
      "p": "[Small Language Models Learn Enhanced Reasoning Skills from Medical Textbooks](https://arxiv.org/abs/2404.00376v2)",
      "c": "",
      "n": "Meerkat-7B (Single)",
      "d": "2024-03-30",
      "m1": "70.6"
    },
    {
      "p": "[MEDITRON-70B: Scaling Medical Pretraining for Large Language Models](https://arxiv.org/abs/2311.16079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/epfllm/meditron)",
      "n": "Meditron-70B (CoT + SC)",
      "d": "2023-11-27",
      "m1": "70.2"
    },
    {
      "p": "[Large Language Models Encode Clinical Knowledge](https://arxiv.org/abs/2212.13138v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/olaph)",
      "n": "Flan-PaLM (540 B)",
      "d": "2022-12-26",
      "m1": "67.6"
    },
    {
      "p": "[MEDITRON-70B: Scaling Medical Pretraining for Large Language Models](https://arxiv.org/abs/2311.16079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/epfllm/meditron)",
      "n": "LLAMA-2 (70B SC CoT)",
      "d": "2023-11-27",
      "m1": "61.5"
    },
    {
      "p": "[SHAKTI: A 2.5 Billion Parameter Small Language Model Optimized for Edge AI and Low-Resource Environments](https://arxiv.org/abs/2410.11331v1)",
      "c": "",
      "n": "Shakti-LLM (2.5B)",
      "d": "2024-10-15",
      "m1": "60.3"
    },
    {
      "p": "[Can large language models reason about medical questions?](https://arxiv.org/abs/2207.08143v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vlievin/medical-reasoning)",
      "n": "Codex 5-shot CoT",
      "d": "2022-07-17",
      "m1": "60.2"
    },
    {
      "p": "[MEDITRON-70B: Scaling Medical Pretraining for Large Language Models](https://arxiv.org/abs/2311.16079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/epfllm/meditron)",
      "n": "LLAMA-2 (70B)",
      "d": "2023-11-27",
      "m1": "59.2"
    },
    {
      "p": "[Variational Open-Domain Question Answering](https://arxiv.org/abs/2210.06345v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VodLM/vod)",
      "n": "VOD (BioLinkBERT)",
      "d": "2022-09-23",
      "m1": "55.0"
    },
    {
      "p": "[BioMedGPT: Open Multimodal Generative Pre-trained Transformer for BioMedicine](https://arxiv.org/abs/2308.09442v2)",
      "c": "[&check;&nbsp;Link](https://github.com/pharmolix/openbiomed)",
      "n": "BioMedGPT-10B",
      "d": "2023-08-18",
      "m1": "50.4"
    },
    {
      "p": "[Large Language Models Encode Clinical Knowledge](https://arxiv.org/abs/2212.13138v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/olaph)",
      "n": "PubMedGPT (2.7 B)",
      "d": "2022-12-26",
      "m1": "50.3"
    },
    {
      "p": "[Deep Bidirectional Language-Knowledge Graph Pretraining](https://arxiv.org/abs/2210.09338v2)",
      "c": "[&check;&nbsp;Link](https://github.com/michiyasunaga/dragon)",
      "n": "DRAGON + BioLinkBERT",
      "d": "2022-10-17",
      "m1": "47.5"
    },
    {
      "p": "[Large Language Models Encode Clinical Knowledge](https://arxiv.org/abs/2212.13138v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/olaph)",
      "n": "BioLinkBERT (340 M)",
      "d": "2022-12-26",
      "m1": "45.1"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "GAL 120B (zero-shot)",
      "d": "2022-11-16",
      "m1": "44.4"
    },
    {
      "p": "[LinkBERT: Pretraining Language Models with Document Links](https://arxiv.org/abs/2203.15827v1)",
      "c": "[&check;&nbsp;Link](https://github.com/michiyasunaga/LinkBERT)",
      "n": "BioLinkBERT (base)",
      "d": "2022-03-29",
      "m1": "40.0"
    },
    {
      "p": "[GrapeQA: GRaph Augmentation and Pruning to Enhance Question-Answering](https://arxiv.org/abs/2303.12320v2)",
      "c": "",
      "n": "GrapeQA: PEGA",
      "d": "2023-03-22",
      "m1": "39.51"
    },
    {
      "p": "[BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://arxiv.org/abs/1901.08746v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/biobert)",
      "n": "BioBERT (large)",
      "d": "2019-01-25",
      "m1": "36.7"
    },
    {
      "p": "[BioBERT: a pre-trained biomedical language representation model for biomedical text mining](https://arxiv.org/abs/1901.08746v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/biobert)",
      "n": "BioBERT (base)",
      "d": "2019-01-25",
      "m1": "34.1"
    },
    {
      "p": "[Large Language Models Encode Clinical Knowledge](https://arxiv.org/abs/2212.13138v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmis-lab/olaph)",
      "n": "GPT-Neo (2.7 B)",
      "d": "2022-12-26",
      "m1": "33.3"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "BLOOM (few-shot, k=5)",
      "d": "2022-11-16",
      "m1": "23.3"
    },
    {
      "p": "[Galactica: A Large Language Model for Science](https://arxiv.org/abs/2211.09085v1)",
      "c": "[&check;&nbsp;Link](https://github.com/paperswithcode/galai)",
      "n": "OPT (few-shot, k=5)",
      "d": "2022-11-16",
      "m1": "22.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
