# image-retrieval-on-cirr

[Dataset Link](https://cuberick-orion.github.io/CIRR/) \
Task Hierarchy: ['Image Retrieval']

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
      "label": "(Recall@5+Recall_subset@1)/2",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Recall@10",
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
      "p": "[TMCIR: Token Merge Benefits Composed Image Retrieval](https://arxiv.org/abs/2504.10995v1)",
      "c": "",
      "n": "TMCIR",
      "d": "2025-04-15",
      "m1": "83.46",
      "m2": "91.06"
    },
    {
      "p": "[Improving Composed Image Retrieval via Contrastive Learning with Scaling Positives and Negatives](https://arxiv.org/abs/2404.11317v2)",
      "c": "[&check;&nbsp;Link](https://github.com/BUAADreamer/SPN4CIR)",
      "n": "SPN4CIR (SPRC)",
      "d": "2024-04-17",
      "m1": "82.69",
      "m2": "90.87"
    },
    {
      "p": "[Sentence-level Prompts Benefit Composed Image Retrieval](https://arxiv.org/abs/2310.05473v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chunmeifeng/sprc)",
      "n": "SPRC2",
      "d": "2023-10-09",
      "m1": "82.66",
      "m2": "90.39"
    },
    {
      "p": "[Sentence-level Prompts Benefit Composed Image Retrieval](https://arxiv.org/abs/2310.05473v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chunmeifeng/sprc)",
      "n": "SPRC",
      "d": "2023-10-09",
      "m1": "81.39",
      "m2": "89.74"
    },
    {
      "p": "[Candidate Set Re-ranking for Composed Image Retrieval with Dual Multi-modal Encoder](https://arxiv.org/abs/2305.16304v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Cuberick-Orion/Bi-Blip4CIR)",
      "n": "Candidate Set Re-ranking",
      "d": "2023-05-25",
      "m1": "80.9",
      "m2": "89.78"
    },
    {
      "p": "[CaLa: Complementary Association Learning for Augmenting Composed Image Retrieval](https://arxiv.org/abs/2405.19149v2)",
      "c": "[&check;&nbsp;Link](https://github.com/chiangsonw/cala)",
      "n": "CaLa",
      "d": "2024-05-29",
      "m1": "78.74",
      "m2": "89.59"
    },
    {
      "p": "[Data Roaming and Quality Assessment for Composed Image Retrieval](https://arxiv.org/abs/2303.09429v2)",
      "c": "[&check;&nbsp;Link](https://github.com/levymsn/LaSCo)",
      "n": "CASE (Pre-trained on LaSCo.Ca)",
      "d": "2023-03-16",
      "m1": "78.25",
      "m2": "88.75"
    },
    {
      "p": "[Data Roaming and Quality Assessment for Composed Image Retrieval](https://arxiv.org/abs/2303.09429v2)",
      "c": "[&check;&nbsp;Link](https://github.com/levymsn/LaSCo)",
      "n": "CASE",
      "d": "2023-03-16",
      "m1": "77.5",
      "m2": "87.25"
    },
    {
      "p": "[VISTA: Visualized Text Embedding For Universal Multi-Modal Retrieval](https://arxiv.org/abs/2406.04292v1)",
      "c": "[&check;&nbsp;Link](https://github.com/flagopen/flagembedding)",
      "n": "VISTA (base)",
      "d": "2024-06-06",
      "m1": "75.9"
    },
    {
      "p": "[MegaPairs: Massive Data Synthesis For Universal Multimodal Retrieval](https://arxiv.org/abs/2412.14475v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VectorSpaceLab/MegaPairs)",
      "n": "MMRet-MLLM",
      "d": "2024-12-19",
      "m1": "75.7",
      "m2": "85.1"
    },
    {
      "p": "[Target-Guided Composed Image Retrieval](https://arxiv.org/abs/2309.01366v1)",
      "c": "",
      "n": "TG-CIR (Wen et al., 2023)",
      "d": "2023-09-04",
      "m1": "75.6",
      "m2": "87.16"
    },
    {
      "p": "[Composed Image Retrieval using Contrastive Learning and Task-oriented CLIP-based Features](https://arxiv.org/abs/2308.11485v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir (v3)",
      "d": "2023-08-22",
      "m1": "75.10"
    },
    {
      "p": "[Bi-directional Training for Composed Image Retrieval via Text Prompt Learning](https://arxiv.org/abs/2303.16604v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Cuberick-Orion/Bi-Blip4CIR)",
      "n": "BLIP4CIR+Bi",
      "d": "2023-03-29",
      "m1": "72.59",
      "m2": "83.88"
    },
    {
      "p": "[Conditioned and Composed Image Retrieval Combining and Partially Fine-Tuning CLIP-Based Features](https://openaccess.thecvf.com/content/CVPR2022W/ODRUM/html/Baldrati_Conditioned_and_Composed_Image_Retrieval_Combining_and_Partially_Fine-Tuning_CLIP-Based_CVPRW_2022_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir (v2)",
      "d": "2022-06-19",
      "m1": "69.09"
    },
    {
      "p": "[Effective Conditioned and Composed Image Retrieval Combining CLIP-Based Features](http://openaccess.thecvf.com//content/CVPR2022/html/Baldrati_Effective_Conditioned_and_Composed_Image_Retrieval_Combining_CLIP-Based_Features_CVPR_2022_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir",
      "d": "2022-01-01",
      "m1": "63.87"
    },
    {
      "p": "[Image Retrieval on Real-life Images with Pre-trained Vision-and-Language Models](https://arxiv.org/abs/2108.04024v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Cuberick-Orion/CIRR)",
      "n": "CIRPLANT",
      "d": "2021-08-09",
      "m1": "45.88"
    },
    {
      "p": "[ARTEMIS: Attention-based Retrieval with Text-Explicit Matching and Implicit Similarity](https://arxiv.org/abs/2203.08101v2)",
      "c": "[&check;&nbsp;Link](https://github.com/naver/artemis)",
      "n": "ARTEMIS",
      "d": "2022-03-15",
      "m1": "43.05",
      "m2": "61.31"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
