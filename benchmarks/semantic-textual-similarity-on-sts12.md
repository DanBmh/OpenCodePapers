# semantic-textual-similarity-on-sts12

[Dataset Link](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark) \
Task Hierarchy: ['Semantic Textual Similarity']

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
      "label": "Spearman Correlation",
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
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+OPT-13B",
      "d": "2023-07-31",
      "m1": "0.8020"
    },
    {
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+LLaMA-30B",
      "d": "2023-07-31",
      "m1": "0.7972"
    },
    {
      "p": "[Improved Universal Sentence Embeddings with Prompt-based Contrastive Learning and Energy-based Learning](https://arxiv.org/abs/2203.06875v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yjiangcm/promcse)",
      "n": "PromCSE-RoBERTa-large (0.355B)",
      "d": "2022-03-14",
      "m1": "0.7956"
    },
    {
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+OPT-2.7B",
      "d": "2023-07-31",
      "m1": "0.7949"
    },
    {
      "p": "[AnglE-optimized Text Embeddings](https://arxiv.org/abs/2309.12871v9)",
      "c": "[&check;&nbsp;Link](https://github.com/SeanLee97/AnglE)",
      "n": "AnglE-LLaMA-7B",
      "d": "2023-09-22",
      "m1": "0.7868"
    },
    {
      "p": "[AnglE-optimized Text Embeddings](https://arxiv.org/abs/2309.12871v9)",
      "c": "[&check;&nbsp;Link](https://github.com/SeanLee97/AnglE)",
      "n": "AnglE-LLaMA-13B",
      "d": "2023-09-22",
      "m1": "0.7868"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-RoBERTa-large-cross (unsup.)",
      "d": "2021-09-27",
      "m1": "0.7828"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-BERT-large-bi (unsup.)",
      "d": "2021-09-27",
      "m1": "0.7819"
    },
    {
      "p": "[SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://arxiv.org/abs/2104.08821v4)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/text_matching/simcse)",
      "n": "SimCSE-RoBERTa-large",
      "d": "2021-04-18",
      "m1": "0.7746"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-RoBERTa-base-cross (unsup.)",
      "d": "2021-09-27",
      "m1": "0.7637"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-BERT-base-bi (unsup.)",
      "d": "2021-09-27",
      "m1": "0.7509"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SRoBERTa-NLI-large",
      "d": "2019-08-27",
      "m1": "0.7453"
    },
    {
      "p": "[DiffCSE: Difference-based Contrastive Learning for Sentence Embeddings](https://arxiv.org/abs/2204.10298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/voidism/diffcse)",
      "n": "DiffCSE-BERT-base",
      "d": "2022-04-21",
      "m1": "0.7228"
    },
    {
      "p": "[Generating Datasets with Pretrained Language Models](https://arxiv.org/abs/2104.07540v3)",
      "c": "[&check;&nbsp;Link](https://github.com/timoschick/dino)",
      "n": "Dino (STSb/\u0304\ud83e\udd95)",
      "d": "2021-04-15",
      "m1": "0.7027"
    },
    {
      "p": "[SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://arxiv.org/abs/2104.08821v4)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/text_matching/simcse)",
      "n": "SimCSE-RoBERTa-base",
      "d": "2021-04-18",
      "m1": "0.7016"
    },
    {
      "p": "[DiffCSE: Difference-based Contrastive Learning for Sentence Embeddings](https://arxiv.org/abs/2204.10298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/voidism/diffcse)",
      "n": "DiffCSE-RoBERTa-base",
      "d": "2022-04-21",
      "m1": "0.7005"
    },
    {
      "p": "[Fast, Effective, and Self-Supervised: Transforming Masked Language Models into Universal Lexical and Sentence Encoders](https://arxiv.org/abs/2104.08027v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cambridgeltl/mirror-bert)",
      "n": "Mirror-BERT-base (unsup.)",
      "d": "2021-04-16",
      "m1": "0.674"
    },
    {
      "p": "[On the Sentence Embeddings from Pre-trained Language Models](https://arxiv.org/abs/2011.05864v1)",
      "c": "[&check;&nbsp;Link](https://github.com/InsaneLife/dssm)",
      "n": "BERTlarge-flow (target)",
      "d": "2020-11-02",
      "m1": "0.6520"
    },
    {
      "p": "[Fast, Effective, and Self-Supervised: Transforming Masked Language Models into Universal Lexical and Sentence Encoders](https://arxiv.org/abs/2104.08027v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cambridgeltl/mirror-bert)",
      "n": "Mirror-RoBERTa-base (unsup.)",
      "d": "2021-04-16",
      "m1": "0.648"
    },
    {
      "p": "[An Unsupervised Sentence Embedding Method by Mutual Information Maximization](https://arxiv.org/abs/2009.12061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yanzhangnlp/IS-BERT)",
      "n": "IS-BERT-NLI",
      "d": "2020-09-25",
      "m1": "0.5677"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
