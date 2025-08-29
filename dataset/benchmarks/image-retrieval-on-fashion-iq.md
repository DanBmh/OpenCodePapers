# image-retrieval-on-fashion-iq

[Dataset Link](https://github.com/XiaoxiaoGuo/fashion-iq) \
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
      "label": "(Recall@10+Recall@50)/2",
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
      "p": "[]()",
      "c": "",
      "n": "DQU-CIR",
      "d": null,
      "m1": "71.77",
      "m2": "61.97"
    },
    {
      "p": "[TMCIR: Token Merge Benefits Composed Image Retrieval](https://arxiv.org/abs/2504.10995v1)",
      "c": "",
      "n": "TMCIR",
      "d": "2025-04-15",
      "m1": "66.56",
      "m2": "56.57"
    },
    {
      "p": "[Improving Composed Image Retrieval via Contrastive Learning with Scaling Positives and Negatives](https://arxiv.org/abs/2404.11317v2)",
      "c": "[&check;&nbsp;Link](https://github.com/BUAADreamer/SPN4CIR)",
      "n": "SPN4CIR (SPRC)",
      "d": "2024-04-17",
      "m1": "66.41",
      "m2": "56.37"
    },
    {
      "p": "[Sentence-level Prompts Benefit Composed Image Retrieval](https://arxiv.org/abs/2310.05473v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chunmeifeng/sprc)",
      "n": "SPRC",
      "d": "2023-10-09",
      "m1": "64.85",
      "m2": "54.92"
    },
    {
      "p": "[Candidate Set Re-ranking for Composed Image Retrieval with Dual Multi-modal Encoder](https://arxiv.org/abs/2305.16304v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Cuberick-Orion/Bi-Blip4CIR)",
      "n": "Candidate Set Re-ranking",
      "d": "2023-05-25",
      "m1": "62.15",
      "m2": "51.17"
    },
    {
      "p": "[Ranking-aware Uncertainty for Text-guided Image Retrieval](https://arxiv.org/abs/2308.08131v1)",
      "c": "",
      "n": "RUTIR (BLIP B/16)",
      "d": "2023-08-16",
      "m1": "61.32"
    },
    {
      "p": "[Data Roaming and Quality Assessment for Composed Image Retrieval](https://arxiv.org/abs/2303.09429v2)",
      "c": "[&check;&nbsp;Link](https://github.com/levymsn/LaSCo)",
      "n": "CASE",
      "d": "2023-03-16",
      "m1": "59.73",
      "m2": "48.79"
    },
    {
      "p": "[CaLa: Complementary Association Learning for Augmenting Composed Image Retrieval](https://arxiv.org/abs/2405.19149v2)",
      "c": "[&check;&nbsp;Link](https://github.com/chiangsonw/cala)",
      "n": "CaLa",
      "d": "2024-05-29",
      "m1": "57.96",
      "m2": "46.69"
    },
    {
      "p": "[Bi-directional Training for Composed Image Retrieval via Text Prompt Learning](https://arxiv.org/abs/2303.16604v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Cuberick-Orion/Bi-Blip4CIR)",
      "n": "BLIP4CIR+Bi",
      "d": "2023-03-29",
      "m1": "55.4"
    },
    {
      "p": "[Composed Image Retrieval using Contrastive Learning and Task-oriented CLIP-based Features](https://arxiv.org/abs/2308.11485v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir (v3)",
      "d": "2023-08-22",
      "m1": "55.36"
    },
    {
      "p": "[Ranking-aware Uncertainty for Text-guided Image Retrieval](https://arxiv.org/abs/2308.08131v1)",
      "c": "",
      "n": "RUTIR (CLIP ResNet50)",
      "d": "2023-08-16",
      "m1": "55.27"
    },
    {
      "p": "[Collaborative Group: Composed Image Retrieval via Consensus Learning from Noisy Annotations](https://arxiv.org/abs/2306.02092v2)",
      "c": "",
      "n": "Css-Net",
      "d": "2023-06-03",
      "m1": "51.34"
    },
    {
      "p": "[Composed Image Retrieval with Text Feedback via Multi-grained Uncertainty Regularization](https://arxiv.org/abs/2211.07394v6)",
      "c": "[&check;&nbsp;Link](https://github.com/Monoxide-Chen/uncertainty_retrieval)",
      "n": "MUR (4*ResNet50)",
      "d": "2022-11-14",
      "m1": "50.61"
    },
    {
      "p": "[Conditioned and Composed Image Retrieval Combining and Partially Fine-Tuning CLIP-Based Features](https://openaccess.thecvf.com/content/CVPR2022W/ODRUM/html/Baldrati_Conditioned_and_Composed_Image_Retrieval_Combining_and_Partially_Fine-Tuning_CLIP-Based_CVPRW_2022_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir (v2)",
      "d": "2022-06-19",
      "m1": "50.03"
    },
    {
      "p": "[Composed Image Retrieval with Text Feedback via Multi-grained Uncertainty Regularization](https://arxiv.org/abs/2211.07394v6)",
      "c": "[&check;&nbsp;Link](https://github.com/Monoxide-Chen/uncertainty_retrieval)",
      "n": "MUR",
      "d": "2022-11-14",
      "m1": "47.28"
    },
    {
      "p": "[Effective Conditioned and Composed Image Retrieval Combining CLIP-Based Features](http://openaccess.thecvf.com//content/CVPR2022/html/Baldrati_Effective_Conditioned_and_Composed_Image_Retrieval_Combining_CLIP-Based_Features_CVPR_2022_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/ABaldrati/CLIP4Cir)",
      "n": "CLIP4Cir",
      "d": "2022-01-01",
      "m1": "47.21"
    },
    {
      "p": "[MegaPairs: Massive Data Synthesis For Universal Multimodal Retrieval](https://arxiv.org/abs/2412.14475v1)",
      "c": "[&check;&nbsp;Link](https://github.com/VectorSpaceLab/MegaPairs)",
      "n": "MMRet-MLLM",
      "d": "2024-12-19",
      "m1": "46.1",
      "m2": "35.6"
    },
    {
      "p": "[RTIC: Residual Learning for Text and Image Composition using Graph Convolutional Network](https://arxiv.org/abs/2104.03015v3)",
      "c": "[&check;&nbsp;Link](https://github.com/brandonhanx/compfashion)",
      "n": "RTIC-GCN",
      "d": "2021-04-07",
      "m1": "40.64"
    },
    {
      "p": "[CoSMo: Content-Style Modulation for Image Retrieval With Text Feedback](http://openaccess.thecvf.com//content/CVPR2021/html/Lee_CoSMo_Content-Style_Modulation_for_Image_Retrieval_With_Text_Feedback_CVPR_2021_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/postBG/CosMo.pytorch)",
      "n": "CoSMo",
      "d": "2021-06-19",
      "m1": "39.45"
    },
    {
      "p": "[CurlingNet: Compositional Learning between Images and Text for Fashion IQ Data](https://arxiv.org/abs/2003.12299v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nashory/rtic-gcn-pytorch)",
      "n": "CurlingNet",
      "d": "2020-03-27",
      "m1": "38.45"
    },
    {
      "p": "[Image Search With Text Feedback by Visiolinguistic Attention Learning](http://openaccess.thecvf.com/content_CVPR_2020/html/Chen_Image_Search_With_Text_Feedback_by_Visiolinguistic_Attention_Learning_CVPR_2020_paper.html)",
      "c": "[&check;&nbsp;Link](https://github.com/yanbeic/VAL)",
      "n": "VAL w/ GloVe",
      "d": "2020-06-01",
      "m1": "35.38"
    },
    {
      "p": "[Compositional Learning of Image-Text Query for Image Retrieval](https://arxiv.org/abs/2006.11149v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ecom-research/ComposeAE)",
      "n": "ComposeAE",
      "d": "2020-06-19",
      "m1": "20.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
