# video-retrieval-on-youcook2

[Dataset Link](http://youcook2.eecs.umich.edu/) \
Task Hierarchy: ['Video Retrieval']

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
      "label": "text-to-video R@1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "text-to-video R@5",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "text-to-video R@10",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "text-to-video Median Rank",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "text-to-video Mean Rank",
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
      "p": "[VAST: A Vision-Audio-Subtitle-Text Omni-Modality Foundation Model and Dataset](https://arxiv.org/abs/2305.18500v2)",
      "c": "[&check;&nbsp;Link](https://github.com/TXH-mercury/VALOR)",
      "n": "VAST",
      "d": "2023-05-29",
      "m1": "50.4",
      "m2": "74.3",
      "m3": "80.8"
    },
    {
      "p": "[MELTR: Meta Loss Transformer for Learning to Fine-tune Video Foundation Models](https://arxiv.org/abs/2303.13009v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mlvlab/MELTR)",
      "n": "UniVL + MELTR",
      "d": "2023-03-23",
      "m1": "33.7",
      "m2": "63.1",
      "m3": "74.8",
      "m4": "3"
    },
    {
      "p": "[VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding](https://arxiv.org/abs/2109.14084v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "VideoCLIP",
      "d": "2021-09-28",
      "m1": "32.2",
      "m2": "62.6",
      "m3": "75.0"
    },
    {
      "p": "[MDMMT-2: Multidomain Multimodal Transformer for Video Retrieval, One More Step Towards Generalization](https://arxiv.org/abs/2203.07086v1)",
      "c": "",
      "n": "MDMMT-2",
      "d": "2022-03-14",
      "m1": "32.0",
      "m2": "64.0",
      "m3": "74.8",
      "m4": "3.0",
      "m5": "12.7"
    },
    {
      "p": "[TACo: Token-aware Cascade Contrastive Learning for Video-Text Alignment](https://arxiv.org/abs/2108.09980v1)",
      "c": "",
      "n": "TACo",
      "d": "2021-08-23",
      "m1": "29.6",
      "m2": "59.7",
      "m3": "72.7",
      "m4": "4"
    },
    {
      "p": "[UniVL: A Unified Video and Language Pre-Training Model for Multimodal Understanding and Generation](https://arxiv.org/abs/2002.06353v3)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/UniVL)",
      "n": "UniVL",
      "d": "2020-02-15",
      "m1": "28.9",
      "m2": "57.6",
      "m3": "70.0",
      "m4": "4"
    },
    {
      "p": "[VLM: Task-agnostic Video-Language Model Pre-training for Video Understanding](https://arxiv.org/abs/2105.09996v3)",
      "c": "[&check;&nbsp;Link](https://github.com/pytorch/fairseq)",
      "n": "VLM",
      "d": "2021-05-20",
      "m1": "27.05",
      "m2": "56.88",
      "m3": "69.38",
      "m4": "4"
    },
    {
      "p": "[VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding](https://arxiv.org/abs/2109.14084v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "VideoCLIP (zero-shot)",
      "d": "2021-09-28",
      "m1": "22.7",
      "m2": "50.4",
      "m3": "63.1"
    },
    {
      "p": "[VideoCoCa: Video-Text Modeling with Zero-Shot Transfer from Contrastive Captioners](https://arxiv.org/abs/2212.04979v3)",
      "c": "",
      "n": "VideoCoCa (zero-shot)",
      "d": "2022-12-09",
      "m1": "21.7",
      "m2": "43.9",
      "m3": "55.2"
    },
    {
      "p": "[COOT: Cooperative Hierarchical Transformer for Video-Text Representation Learning](https://arxiv.org/abs/2011.00597v1)",
      "c": "[&check;&nbsp;Link](https://github.com/gingsi/coot-videotext)",
      "n": "COOT",
      "d": "2020-11-01",
      "m1": "16.7",
      "m3": "52.3",
      "m4": "9"
    },
    {
      "p": "[HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips](https://arxiv.org/abs/1906.03327v2)",
      "c": "[&check;&nbsp;Link](https://github.com/antoine77340/MIL-NCE_HowTo100M)",
      "n": "Text-Video Embedding",
      "d": "2019-06-07",
      "m1": "8.2",
      "m2": "24.5",
      "m3": "35.3",
      "m4": "24"
    },
    {
      "p": "[RoME: Role-aware Mixture-of-Expert Transformer for Text-to-Video Retrieval](https://arxiv.org/abs/2206.12845v1)",
      "c": "[&check;&nbsp;Link](https://github.com/buraksatar/RoME_video_retrieval)",
      "n": "RoME",
      "d": "2022-06-26",
      "m1": "6.3",
      "m2": "16.9",
      "m3": "25.2",
      "m4": "53"
    },
    {
      "p": "[Semantic Role Aware Correlation Transformer for Text to Video Retrieval](https://arxiv.org/abs/2206.12849v1)",
      "c": "[&check;&nbsp;Link](https://github.com/buraksatar/RoME_video_retrieval)",
      "n": "Satar et al.",
      "d": "2022-06-26",
      "m1": "5.3",
      "m2": "14.5",
      "m3": "20.8",
      "m4": "77"
    },
    {
      "p": "[Associating Neural Word Embeddings With Deep Image Representations Using Fisher Vectors](http://openaccess.thecvf.com/content_cvpr_2015/html/Klein_Associating_Neural_Word_2015_CVPR_paper.html)",
      "c": "",
      "n": "HGLMM FV CCA",
      "d": "2015-06-01",
      "m1": "4.6",
      "m2": "14.3",
      "m3": "21.6",
      "m4": "75"
    },
    {
      "p": "[OmniVec: Learning robust representations with cross modal sharing](https://arxiv.org/abs/2311.05709v1)",
      "c": "",
      "n": "OmniVec",
      "d": "2023-11-07",
      "m3": "70.8"
    },
    {
      "p": "[OmniVec: Learning robust representations with cross modal sharing](https://arxiv.org/abs/2311.05709v1)",
      "c": "",
      "n": "OmniVec (pretrained)",
      "d": "2023-11-07",
      "m3": "64.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
