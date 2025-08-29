# temporal-relation-extraction-on-vinoground

[Dataset Link](https://huggingface.co/datasets/HanSolo9682/Vinoground) \
Task Hierarchy: ['Temporal Relation Extraction']

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
      "label": "Text Score",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Video Score",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Group Score",
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
      "p": "[]()",
      "c": "",
      "n": "GPT-4o (CoT)",
      "d": null,
      "m1": "59.2",
      "m2": "51",
      "m3": "35"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GPT-4o",
      "d": null,
      "m1": "54",
      "m2": "38.2",
      "m3": "24.6"
    },
    {
      "p": "[Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191v2)",
      "c": "[&check;&nbsp;Link](https://github.com/qwenlm/qwen2-vl)",
      "n": "Qwen2-VL-72B",
      "d": "2024-09-18",
      "m1": "50.4",
      "m2": "32.6",
      "m3": "17.4"
    },
    {
      "p": "[LLaVA-OneVision: Easy Visual Task Transfer](https://arxiv.org/abs/2408.03326v3)",
      "c": "[&check;&nbsp;Link](https://github.com/evolvinglmms-lab/lmms-eval)",
      "n": "LLaVA-OneVision-Qwen2-72B",
      "d": "2024-08-06",
      "m1": "48.4",
      "m2": "35.2",
      "m3": "21.8"
    },
    {
      "p": "[LLaVA-OneVision: Easy Visual Task Transfer](https://arxiv.org/abs/2408.03326v3)",
      "c": "[&check;&nbsp;Link](https://github.com/evolvinglmms-lab/lmms-eval)",
      "n": "LLaVA-OneVision-Qwen2-7B",
      "d": "2024-08-06",
      "m1": "41.6",
      "m2": "29.4",
      "m3": "14.6"
    },
    {
      "p": "[Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191v2)",
      "c": "[&check;&nbsp;Link](https://github.com/qwenlm/qwen2-vl)",
      "n": "Qwen2-VL-7B",
      "d": "2024-09-18",
      "m1": "40.2",
      "m2": "32.4",
      "m3": "15.2"
    },
    {
      "p": "[Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/abs/2403.05530v5)",
      "c": "[&check;&nbsp;Link](https://github.com/dlvuldet/primevul)",
      "n": "Gemini-1.5-Pro (CoT)",
      "d": "2024-03-08",
      "m1": "37",
      "m2": "27.6",
      "m3": "12.4"
    },
    {
      "p": "[VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs](https://arxiv.org/abs/2406.07476v3)",
      "c": "[&check;&nbsp;Link](https://github.com/damo-nlp-sg/videollama2)",
      "n": "VideoLLaMA2-72B",
      "d": "2024-06-11",
      "m1": "36.2",
      "m2": "21.8",
      "m3": "8.4"
    },
    {
      "p": "[Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/abs/2403.05530v5)",
      "c": "[&check;&nbsp;Link](https://github.com/dlvuldet/primevul)",
      "n": "Gemini-1.5-Pro",
      "d": "2024-03-08",
      "m1": "35.8",
      "m2": "22.6",
      "m3": "10.2"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Claude 3.5 Sonnet",
      "d": null,
      "m1": "32.8",
      "m2": "28.8",
      "m3": "10.6"
    },
    {
      "p": "[MiniCPM-V: A GPT-4V Level MLLM on Your Phone](https://arxiv.org/abs/2408.01800v1)",
      "c": "[&check;&nbsp;Link](https://github.com/openbmb/minicpm-v)",
      "n": "MiniCPM-2.6",
      "d": "2024-08-03",
      "m1": "32.6",
      "m2": "29.2",
      "m3": "11.2"
    },
    {
      "p": "[InternLM-XComposer-2.5: A Versatile Large Vision Language Model Supporting Long-Contextual Input and Output](https://arxiv.org/abs/2407.03320v1)",
      "c": "[&check;&nbsp;Link](https://github.com/internlm/internlm-xcomposer)",
      "n": "InternLM-XC-2.5 (CoT)",
      "d": "2024-07-03",
      "m1": "30.8",
      "m2": "28.4",
      "m3": "9"
    },
    {
      "p": "[InternLM-XComposer-2.5: A Versatile Large Vision Language Model Supporting Long-Contextual Input and Output](https://arxiv.org/abs/2407.03320v1)",
      "c": "[&check;&nbsp;Link](https://github.com/internlm/internlm-xcomposer)",
      "n": "InternLM-XC-2.5",
      "d": "2024-07-03",
      "m1": "28.8",
      "m2": "27.8",
      "m3": "9.6"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LLaVA-NeXT-Video-34B (CoT)",
      "d": null,
      "m1": "25.8",
      "m2": "22.2",
      "m3": "5.2"
    },
    {
      "p": "[Video-LLaVA: Learning United Visual Representation by Alignment Before Projection](https://arxiv.org/abs/2311.10122v3)",
      "c": "[&check;&nbsp;Link](https://github.com/PKU-YuanGroup/Video-LLaVA)",
      "n": "Video-LLaVA-7B",
      "d": "2023-11-16",
      "m1": "24.8",
      "m2": "25.8",
      "m3": "6.6"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Phi-3.5-Vision",
      "d": null,
      "m1": "24",
      "m2": "22.4",
      "m3": "6.2"
    },
    {
      "p": "[MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726v2)",
      "c": "[&check;&nbsp;Link](https://github.com/boheumd/MA-LMM)",
      "n": "MA-LMM-Vicuna-7B",
      "d": "2024-04-08",
      "m1": "23.8",
      "m2": "25.6",
      "m3": "6.8"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LLaVA-NeXT-Video-34B",
      "d": null,
      "m1": "23",
      "m2": "21.2",
      "m3": "3.8"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LLaVA-NeXT-Video-7B (CoT)",
      "d": null,
      "m1": "21.8",
      "m2": "26.2",
      "m3": "6.8"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LLaVA-NeXT-Video-7B",
      "d": null,
      "m1": "21.8",
      "m2": "25.6",
      "m3": "6.2"
    },
    {
      "p": "[VTimeLLM: Empower LLM to Grasp Video Moments](https://arxiv.org/abs/2311.18445v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huangb23/vtimellm)",
      "n": "VTimeLLM",
      "d": "2023-11-30",
      "m1": "19.4",
      "m2": "27",
      "m3": "5.2"
    },
    {
      "p": "[VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding](https://arxiv.org/abs/2109.14084v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "VideoCLIP",
      "d": "2021-09-28",
      "m1": "17",
      "m2": "2.8",
      "m3": "1.2"
    },
    {
      "p": "[LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment](https://arxiv.org/abs/2310.01852v7)",
      "c": "[&check;&nbsp;Link](https://github.com/PKU-YuanGroup/Video-LLaVA)",
      "n": "LanguageBind",
      "d": "2023-10-03",
      "m1": "10.6",
      "m2": "5",
      "m3": "1.2"
    },
    {
      "p": "[ImageBind: One Embedding Space To Bind Them All](https://arxiv.org/abs/2305.05665v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/imagebind)",
      "n": "ImageBind",
      "d": "2023-05-09",
      "m1": "9.4",
      "m2": "3.4",
      "m3": "0.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
