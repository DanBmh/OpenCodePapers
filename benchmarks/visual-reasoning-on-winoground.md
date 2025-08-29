# visual-reasoning-on-winoground

[Dataset Link](https://huggingface.co/datasets/facebook/winoground) \
Task Hierarchy: ['Visual Reasoning']

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
      "label": "Image Score",
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
      "p": "[A Cognitive Paradigm Approach to Probe the Perception-Reasoning Interface in VLMs](https://arxiv.org/abs/2501.13620v5)",
      "c": "",
      "n": "GPT-4o + CA",
      "d": "2025-01-23",
      "m1": "75.5",
      "m2": "58.5",
      "m3": "52"
    },
    {
      "p": "[The Role of Chain-of-Thought in Complex Vision-Language Reasoning Task](https://arxiv.org/abs/2311.09193v1)",
      "c": "",
      "n": "GPT-4V (CoT, pick b/w two options)",
      "d": "2023-11-15",
      "m1": "75.25",
      "m2": "68.75",
      "m3": "58.75"
    },
    {
      "p": "[The Role of Chain-of-Thought in Complex Vision-Language Reasoning Task](https://arxiv.org/abs/2311.09193v1)",
      "c": "",
      "n": "GPT-4V (pick b/w two options)",
      "d": "2023-11-15",
      "m1": "69.25",
      "m2": "46.25",
      "m3": "39.25"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "MMICL + CoCoT",
      "d": "2024-01-05",
      "m1": "64.25",
      "m2": "52.5",
      "m3": "50.75"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "GPT-4V + CoCoT",
      "d": "2024-01-05",
      "m1": "58.5",
      "m2": "49.5",
      "m3": "44.5"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "OpenFlamingo + CoCoT",
      "d": "2024-01-05",
      "m1": "58.25",
      "m2": "55.25",
      "m3": "41.5"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "GPT-4V",
      "d": "2024-01-05",
      "m1": "54.5",
      "m2": "42.5",
      "m3": "37.75"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "FIBER (EqSim)",
      "d": "2023-03-25",
      "m1": "51.5",
      "m2": "32.00",
      "m3": "27.5"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "FIBER (finetuned, Flickr30k)",
      "d": "2023-03-25",
      "m1": "51.25",
      "m2": "26.50",
      "m3": "23.00"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "MMICL + CCoT",
      "d": "2024-01-05",
      "m1": "51",
      "m2": "48",
      "m3": "47.5"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "OpenFlamingo + DDCoT",
      "d": "2024-01-05",
      "m1": "47.5",
      "m2": "47.25",
      "m3": "39"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "VQ2",
      "d": "2023-05-17",
      "m1": "47",
      "m2": "42.2",
      "m3": "30.5"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "MMICL + DDCoT",
      "d": "2024-01-05",
      "m1": "46.75",
      "m2": "45",
      "m3": "36.75"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "X-VLM 16M",
      "d": "2023-05-12",
      "m1": "46.7",
      "m2": "24.5",
      "m3": "21.2"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "PaLI (ft SNLI-VE + Synthetic Data)",
      "d": "2023-05-17",
      "m1": "46.5",
      "m2": "38",
      "m3": "28.75"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "FIBER",
      "d": "2023-03-25",
      "m1": "46.25",
      "m2": "25.75",
      "m3": "22.25"
    },
    {
      "p": "[MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://arxiv.org/abs/2309.07915v3)",
      "c": "[&check;&nbsp;Link](https://github.com/haozhezhao/mic)",
      "n": "MMICL (FLAN-T5-XXL)",
      "d": "2023-09-14",
      "m1": "45.50",
      "m2": "44.99",
      "m3": "43.00"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "PaLI (ft SNLI-VE)",
      "d": "2023-05-17",
      "m1": "45.00",
      "m2": "41.50",
      "m3": "28.70"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "Gemini + DDCoT",
      "d": "2024-01-05",
      "m1": "45",
      "m2": "25",
      "m3": "23.75"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "METER (EqSim)",
      "d": "2023-03-25",
      "m1": "45.0",
      "m2": "22.75",
      "m3": "18.75"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "X-VLM 4M",
      "d": "2023-05-12",
      "m1": "44.0",
      "m2": "26.7",
      "m3": "21.5"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "BLIP2 (ft COCO)",
      "d": "2023-05-17",
      "m1": "44.00",
      "m2": "26.00",
      "m3": "23.50"
    },
    {
      "p": "[Prompting Large Vision-Language Models for Compositional Reasoning](https://arxiv.org/abs/2401.11337v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tossowski/keycomp)",
      "n": "KeyComp* (GPT-4)",
      "d": "2024-01-20",
      "m1": "43.5",
      "m2": "28.7",
      "m3": "18.2"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "METER (finetuned, Flickr30k)",
      "d": "2023-03-25",
      "m1": "43.5",
      "m2": "20.75",
      "m3": "14.75"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP2 (SGVL)",
      "d": "2023-05-10",
      "m1": "42.8",
      "m2": "28.5",
      "m3": "23.3"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP (SGVL)",
      "d": "2023-05-10",
      "m1": "42.8",
      "m2": "27.3",
      "m3": "21.5"
    },
    {
      "p": "[Prompting Large Vision-Language Models for Compositional Reasoning](https://arxiv.org/abs/2401.11337v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tossowski/keycomp)",
      "n": "KeyComp* (GPT-3.5)",
      "d": "2024-01-20",
      "m1": "42.7",
      "m2": "27.8",
      "m3": "17.4"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "OpenFlamingo + CCoT",
      "d": "2024-01-05",
      "m1": "42.5",
      "m2": "27.5",
      "m3": "20"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "NegBLIP",
      "d": "2023-05-10",
      "m1": "42.5",
      "m2": "24.0",
      "m3": "18.5"
    },
    {
      "p": "[Does Structural Attention Improve Compositional Representations in Vision-Language Models?](https://sslneurips22.github.io/paper_pdfs/paper_65.pdf)",
      "c": "",
      "n": "IAIS large (Flickr30k)",
      "d": "2022-12-03",
      "m1": "42.50",
      "m2": "19.75",
      "m3": "16.00"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "LLaVA-1.5-CCoT",
      "d": "2023-11-27",
      "m1": "42.0",
      "m2": "35.5",
      "m3": "22.3"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP2",
      "d": "2023-05-10",
      "m1": "42.0",
      "m2": "23.8",
      "m3": "19.0"
    },
    {
      "p": "[Does Structural Attention Improve Compositional Representations in Vision-Language Models?](https://sslneurips22.github.io/paper_pdfs/paper_65.pdf)",
      "c": "",
      "n": "IAIS large (COCO)",
      "d": "2022-12-03",
      "m1": "41.75",
      "m2": "19.75",
      "m3": "15.50"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "NegBLIP2",
      "d": "2023-05-10",
      "m1": "41.5",
      "m2": "26.0",
      "m3": "20.5"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP (+Graph Text, +Graph Neg)",
      "d": "2023-05-10",
      "m1": "40.5",
      "m2": "25.5",
      "m3": "19.0"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP (+Graph Text)",
      "d": "2023-05-10",
      "m1": "40.3",
      "m2": "20.5",
      "m3": "16.5"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "Gemini + CoCoT",
      "d": "2024-01-05",
      "m1": "40",
      "m2": "32.5",
      "m3": "27.75"
    },
    {
      "p": "[Does Structural Attention Improve Compositional Representations in Vision-Language Models?](https://sslneurips22.github.io/paper_pdfs/paper_65.pdf)",
      "c": "",
      "n": "CACR base",
      "d": "2022-12-03",
      "m1": "39.25",
      "m2": "17.75",
      "m3": "14.25"
    },
    {
      "p": "[Equivariant Similarity for Vision-Language Foundation Models](https://arxiv.org/abs/2303.14465v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "METER",
      "d": "2023-03-25",
      "m1": "39.25",
      "m2": "15.75",
      "m3": "12.00"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "OpenFlamingo",
      "d": "2024-01-05",
      "m1": "39",
      "m2": "41.25",
      "m3": "33.25"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "BLIP",
      "d": "2023-05-10",
      "m1": "39.0",
      "m2": "19.2",
      "m3": "15.0"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GPT-4V (image-caption match answer yes/no, zero-shot)",
      "d": null,
      "m1": "38.00",
      "m2": "38.00",
      "m3": "38.00"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "UNITER large",
      "d": "2022-04-07",
      "m1": "38.00",
      "m2": "14.00",
      "m3": "10.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VinVL",
      "d": "2022-04-07",
      "m1": "37.75",
      "m2": "17.75",
      "m3": "14.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "ViLLA large",
      "d": "2022-04-07",
      "m1": "37.00",
      "m2": "13.25",
      "m3": "11.00"
    },
    {
      "p": "[Revisiting the Role of Language Priors in Vision-Language Models](https://arxiv.org/abs/2306.01879v4)",
      "c": "[&check;&nbsp;Link](https://github.com/linzhiqiu/visual_gpt_score)",
      "n": "BLIP (VisualGPTScore, \u03b1-tuned)",
      "d": "2023-06-02",
      "m1": "36.5",
      "m2": "21.5",
      "m3": "16.8"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "BLIP 14M",
      "d": "2023-05-12",
      "m1": "36.5",
      "m2": "18.5",
      "m3": "14.5"
    },
    {
      "p": "[ViLEM: Visual-Language Error Modeling for Image-Text Retrieval](http://openaccess.thecvf.com//content/CVPR2023/html/Chen_ViLEM_Visual-Language_Error_Modeling_for_Image-Text_Retrieval_CVPR_2023_paper.html)",
      "c": "",
      "n": "ViT-B/16 + BERT base + ViLEM",
      "d": "2023-01-01",
      "m1": "36.5"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "LLaVA-1.5",
      "d": "2023-11-27",
      "m1": "36.0",
      "m2": "33.3",
      "m3": "20.1"
    },
    {
      "p": "[Revisiting the Role of Language Priors in Vision-Language Models](https://arxiv.org/abs/2306.01879v4)",
      "c": "[&check;&nbsp;Link](https://github.com/linzhiqiu/visual_gpt_score)",
      "n": "BLIP (ITM)",
      "d": "2023-06-02",
      "m1": "35.8",
      "m2": "15.8",
      "m3": "13.3"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "BLIP 129M",
      "d": "2023-05-12",
      "m1": "35.5",
      "m2": "15.0",
      "m3": "11.7"
    },
    {
      "p": "[Does Structural Attention Improve Compositional Representations in Vision-Language Models?](https://sslneurips22.github.io/paper_pdfs/paper_65.pdf)",
      "c": "",
      "n": "ROSITA (Flickr30k)",
      "d": "2022-12-03",
      "m1": "35.25",
      "m2": "15.25",
      "m3": "12.25"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "ViLT (ViT-B/32)",
      "d": "2022-04-07",
      "m1": "34.75",
      "m2": "14.00",
      "m3": "9.25"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "BLIP 129M (CapFilt/L)",
      "d": "2023-05-12",
      "m1": "34.7",
      "m2": "15.2",
      "m3": "12.2"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "BLIP-ViT/L 129M",
      "d": "2023-05-12",
      "m1": "34.7",
      "m2": "14.5",
      "m3": "12.2"
    },
    {
      "p": "[Your Diffusion Model is Secretly a Zero-Shot Classifier](https://arxiv.org/abs/2303.16203v3)",
      "c": "[&check;&nbsp;Link](https://github.com/diffusion-classifier/diffusion-classifier)",
      "n": "Diffusion Classifier (zero-shot)",
      "d": "2023-03-28",
      "m1": "34.00"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "PEVL 14M",
      "d": "2023-05-12",
      "m1": "33.2",
      "m2": "15.7",
      "m3": "12.2"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "ALBEF 14M",
      "d": "2023-05-12",
      "m1": "32.5",
      "m2": "16.2",
      "m3": "12.7"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "FLAVA (ITM)",
      "d": "2022-04-07",
      "m1": "32.25",
      "m2": "20.50",
      "m3": "14.25"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "UNITER base",
      "d": "2022-04-07",
      "m1": "32.25",
      "m2": "13.25",
      "m3": "10.00"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "CLIP (SGVL)",
      "d": "2023-05-10",
      "m1": "32.0",
      "m2": "14.0",
      "m3": "9.8"
    },
    {
      "p": "[ViLEM: Visual-Language Error Modeling for Image-Text Retrieval](http://openaccess.thecvf.com//content/CVPR2023/html/Chen_ViLEM_Visual-Language_Error_Modeling_for_Image-Text_Retrieval_CVPR_2023_paper.html)",
      "c": "",
      "n": "ViT-B/16 + BERT base",
      "d": "2023-01-01",
      "m1": "31.2"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "Gemini",
      "d": "2024-01-05",
      "m1": "30.75",
      "m2": "26",
      "m3": "25"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "OCLIP (ViT-H/14) ",
      "d": "2023-11-17",
      "m1": "30.75",
      "m2": "12.75"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "CLIP (ViT-B/32)",
      "d": "2022-04-07",
      "m1": "30.75",
      "m2": "10.50",
      "m3": "8.00"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA large (ITM)",
      "d": "2023-05-11",
      "m1": "30.75",
      "m2": "10.25",
      "m3": "7.25"
    },
    {
      "p": "[Prompting Large Vision-Language Models for Compositional Reasoning](https://arxiv.org/abs/2401.11337v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tossowski/keycomp)",
      "n": "KeyComp (GPT-3.5)",
      "d": "2024-01-20",
      "m1": "30.3",
      "m2": "24.6",
      "m3": "12.4"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "CLIP (ViT-L/14)",
      "d": "2023-11-17",
      "m1": "30.25",
      "m2": "8.0"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "ViLLA base",
      "d": "2022-04-07",
      "m1": "30.00",
      "m2": "12.00",
      "m3": "8.00"
    },
    {
      "p": "[Going Beyond Nouns With Vision & Language Models Using Synthetic Data](https://arxiv.org/abs/2303.17590v2)",
      "c": "[&check;&nbsp;Link](https://github.com/uvavision/syvic)",
      "n": "syn-CLIP",
      "d": "2023-03-30",
      "m1": "30.00",
      "m2": "11.50",
      "m3": "9.50"
    },
    {
      "p": "[Going Beyond Nouns With Vision & Language Models Using Synthetic Data](https://arxiv.org/abs/2303.17590v2)",
      "c": "[&check;&nbsp;Link](https://github.com/uvavision/syvic)",
      "n": "syn-CyCLIP",
      "d": "2023-03-30",
      "m1": "30.00",
      "m2": "10.75",
      "m3": "8.25"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "NegCLIP",
      "d": "2023-05-10",
      "m1": "29.5",
      "m2": "10.5",
      "m3": "8.0"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA large (TLC-A)",
      "d": "2023-05-11",
      "m1": "29.25",
      "m2": "27.00",
      "m3": "17.50"
    },
    {
      "p": "[Measuring Progress in Fine-grained Vision-and-Language Understanding](https://arxiv.org/abs/2305.07558v1)",
      "c": "[&check;&nbsp;Link](https://github.com/e-bug/fine-grained-evals)",
      "n": "ALBEF 4M",
      "d": "2023-05-12",
      "m1": "29.2",
      "m2": "15.5",
      "m3": "11.0"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "LDM-T5 (SelfEval)",
      "d": "2023-11-17",
      "m1": "29.00",
      "m2": "13.50"
    },
    {
      "p": "[Going Beyond Nouns With Vision & Language Models Using Synthetic Data](https://arxiv.org/abs/2303.17590v2)",
      "c": "[&check;&nbsp;Link](https://github.com/uvavision/syvic)",
      "n": "CyCLIP",
      "d": "2023-03-30",
      "m1": "28.50",
      "m2": "9.50",
      "m3": "7.25"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "PDM-T5 (SelfEval)",
      "d": "2023-11-17",
      "m1": "28.25",
      "m2": "12.00"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "COCA ViT-L14 (f.t on COCO)",
      "d": "2023-05-17",
      "m1": "28.25",
      "m2": "11.50",
      "m3": "8.25"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "LLaVA-1.5-ZS-CoT",
      "d": "2023-11-27",
      "m1": "28.0",
      "m2": "22.5",
      "m3": "12.3"
    },
    {
      "p": "[Revisiting the Role of Language Priors in Vision-Language Models](https://arxiv.org/abs/2306.01879v4)",
      "c": "[&check;&nbsp;Link](https://github.com/linzhiqiu/visual_gpt_score)",
      "n": "BLIP (ITC)",
      "d": "2023-06-02",
      "m1": "28.0",
      "m2": "9.0",
      "m3": "6.5"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "OFA large (ft SNLI-VE)",
      "d": "2023-05-17",
      "m1": "27.70",
      "m2": "14.30",
      "m3": "9.00"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA base (ITM)",
      "d": "2023-05-11",
      "m1": "26.75",
      "m2": "10.75",
      "m3": "6.50"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "CLIP RN50x64",
      "d": "2023-05-17",
      "m1": "26.50",
      "m2": "13.75",
      "m3": "10.25"
    },
    {
      "p": "[An Examination of the Compositionality of Large Generative Vision-Language Models](https://arxiv.org/abs/2308.10509v2)",
      "c": "[&check;&nbsp;Link](https://github.com/teleema/sade)",
      "n": "LLaVA-7B (GPTScore)",
      "d": "2023-08-21",
      "m1": "25.50",
      "m2": "17.00",
      "m3": "10.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "FLAVA (contrastive)",
      "d": "2022-04-07",
      "m1": "25.25",
      "m2": "13.50",
      "m3": "9.00"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "Random chance",
      "d": "2022-04-07",
      "m1": "25.00",
      "m2": "25.00",
      "m3": "16.67"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "LLaVA",
      "d": "2023-05-10",
      "m1": "24.8",
      "m2": "25.0",
      "m3": "13.0"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA base (TLC-A)",
      "d": "2023-05-11",
      "m1": "24.50",
      "m2": "23.50",
      "m3": "13.75"
    },
    {
      "p": "[An Examination of the Compositionality of Large Generative Vision-Language Models](https://arxiv.org/abs/2308.10509v2)",
      "c": "[&check;&nbsp;Link](https://github.com/teleema/sade)",
      "n": "MiniGPT-4-7B (GPTScore)",
      "d": "2023-08-21",
      "m1": "24.50",
      "m2": "21.75",
      "m3": "11.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "ViLBERT base",
      "d": "2022-04-07",
      "m1": "23.75",
      "m2": "7.25",
      "m3": "4.75"
    },
    {
      "p": "[Incorporating Structured Representations into Pretrained Vision & Language Models Using Scene Graphs](https://arxiv.org/abs/2305.06343v2)",
      "c": "",
      "n": "MiniGPT-4",
      "d": "2023-05-10",
      "m1": "23.3",
      "m2": "18.0",
      "m3": "9.5"
    },
    {
      "p": "[An Examination of the Compositionality of Large Generative Vision-Language Models](https://arxiv.org/abs/2308.10509v2)",
      "c": "[&check;&nbsp;Link](https://github.com/teleema/sade)",
      "n": "MiniGPT-4-7B (VisualGPTScore)",
      "d": "2023-08-21",
      "m1": "23.25",
      "m2": "18.00",
      "m3": "9.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSE++ (COCO, ResNet)",
      "d": "2022-04-07",
      "m1": "22.75",
      "m2": "8.00",
      "m3": "4.00"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA tiny (ITM)",
      "d": "2023-05-11",
      "m1": "22.75",
      "m2": "7.75",
      "m3": "4.50"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "LDM-CLIP (SelfEval)",
      "d": "2023-11-17",
      "m1": "22.75",
      "m2": "7.25"
    },
    {
      "p": "[CoCoT: Contrastive Chain-of-Thought Prompting for Large Multimodal Models with Multiple Image Inputs](https://arxiv.org/abs/2401.02582v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vista-h/gpt-4v_social_media)",
      "n": "Gemini + CCoT",
      "d": "2024-01-05",
      "m1": "22.5",
      "m2": "33",
      "m3": "20.75"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "InstructBLIP-CCoT ",
      "d": "2023-11-27",
      "m1": "21.0",
      "m2": "21.3",
      "m3": "8.3"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSRN (Flickr30k)",
      "d": "2022-04-07",
      "m1": "20.00",
      "m2": "5.00",
      "m3": "3.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSE++ (Flickr30k, ResNet)",
      "d": "2022-04-07",
      "m1": "20.00",
      "m2": "5.00",
      "m3": "2.75"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSE++ (Flickr30k, VGG)",
      "d": "2022-04-07",
      "m1": "19.75",
      "m2": "6.25",
      "m3": "4.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "UniT (ITM finetuned)",
      "d": "2022-04-07",
      "m1": "19.50",
      "m2": "6.25",
      "m3": "4.00"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "LXMERT",
      "d": "2022-04-07",
      "m1": "19.25",
      "m2": "7.00",
      "m3": "4.00"
    },
    {
      "p": "[What You See is What You Read? Improving Text-Image Alignment Evaluation](https://arxiv.org/abs/2305.10400v4)",
      "c": "[&check;&nbsp;Link](https://github.com/yonatanbitton/wysiwyr)",
      "n": "TIFA",
      "d": "2023-05-17",
      "m1": "19.00",
      "m2": "12.50",
      "m3": "11.30"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "IDEFICS 80B",
      "d": null,
      "m1": "18.75",
      "m2": "22.5",
      "m3": "8.0"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSE++ (COCO, VGG)",
      "d": "2022-04-07",
      "m1": "18.75",
      "m2": "5.50",
      "m3": "3.50"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VSRN (COCO)",
      "d": "2022-04-07",
      "m1": "17.50",
      "m2": "7.00",
      "m3": "3.75"
    },
    {
      "p": "[SelfEval: Leveraging the discriminative nature of generative models for evaluation](https://arxiv.org/abs/2311.10708v2)",
      "c": "",
      "n": "PDM-CLIP (SelfEval)",
      "d": "2023-11-17",
      "m1": "17.00",
      "m2": "14.00"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "IDEFICS 9B",
      "d": null,
      "m1": "16.8",
      "m2": "20.8",
      "m3": "5.0"
    },
    {
      "p": "[Simple Token-Level Confidence Improves Caption Correctness](https://arxiv.org/abs/2305.07021v1)",
      "c": "",
      "n": "OFA tiny (TLC-A)",
      "d": "2023-05-11",
      "m1": "16.50",
      "m2": "15.75",
      "m3": "6.75"
    },
    {
      "p": "[Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality](https://arxiv.org/abs/2204.03162v2)",
      "c": "[&check;&nbsp;Link](https://github.com/wangt-cn/eqben)",
      "n": "VisualBERT base",
      "d": "2022-04-07",
      "m1": "15.50",
      "m2": "2.50",
      "m3": "1.50"
    },
    {
      "p": "[An Examination of the Compositionality of Large Generative Vision-Language Models](https://arxiv.org/abs/2308.10509v2)",
      "c": "[&check;&nbsp;Link](https://github.com/teleema/sade)",
      "n": "MiniGPT-4-7B (BERTScore)",
      "d": "2023-08-21",
      "m1": "14.00",
      "m2": "8.00",
      "m3": "2.75"
    },
    {
      "p": "[An Examination of the Compositionality of Large Generative Vision-Language Models](https://arxiv.org/abs/2308.10509v2)",
      "c": "[&check;&nbsp;Link](https://github.com/teleema/sade)",
      "n": "LLaVA-7B (BERTScore)",
      "d": "2023-08-21",
      "m1": "13.50",
      "m2": "5.25",
      "m3": "2.25"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "InstructBLIP-ZS-CoT",
      "d": "2023-11-27",
      "m1": "9.3",
      "m2": "16.3",
      "m3": "4.0"
    },
    {
      "p": "[Compositional Chain-of-Thought Prompting for Large Multimodal Models](https://arxiv.org/abs/2311.17076v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chancharikmitra/ccot)",
      "n": "InstructBLIP",
      "d": "2023-11-27",
      "m1": "7.0",
      "m2": "11.5",
      "m3": "3.3"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
