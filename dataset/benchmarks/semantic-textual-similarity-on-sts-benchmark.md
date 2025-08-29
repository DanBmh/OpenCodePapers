# semantic-textual-similarity-on-sts-benchmark

[Dataset Link](https://github.com/openai/human-eval) \
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
      "label": "Pearson Correlation",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Spearman Correlation",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Dev Pearson Correlation",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Dev Spearman Correlation",
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
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "MT-DNN-SMART",
      "d": "2019-11-08",
      "m1": "0.929",
      "m2": "0.925"
    },
    {
      "p": "[StructBERT: Incorporating Language Structures into Pre-training for Deep Language Understanding](https://arxiv.org/abs/1908.04577v3)",
      "c": "",
      "n": "StructBERTRoBERTa ensemble",
      "d": "2019-08-13",
      "m1": "0.928",
      "m2": "0.924"
    },
    {
      "p": "[MNet-Sim: A Multi-layered Semantic Similarity Network to Evaluate Sentence Similarity](https://arxiv.org/abs/2111.05412v1)",
      "c": "",
      "n": "Mnet-Sim",
      "d": "2021-11-09",
      "m1": "0.927",
      "m2": "0.931"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-11B",
      "d": "2019-10-23",
      "m1": "0.925",
      "m2": "0.921"
    },
    {
      "p": "[ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942v6)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ALBERT",
      "d": "2019-09-26",
      "m1": "0.925"
    },
    {
      "p": "[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "XLNet (single model)",
      "d": "2019-06-19",
      "m1": "0.925"
    },
    {
      "p": "[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "RoBERTa",
      "d": "2019-07-26",
      "m1": "0.922"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ELECTRA",
      "d": null,
      "m1": "0.921"
    },
    {
      "p": "[LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339v2)",
      "c": "[&check;&nbsp;Link](https://github.com/timdettmers/bitsandbytes)",
      "n": "RoBERTa-large 355M (MLP quantized vector-wise, fine-tuned)",
      "d": "2022-08-15",
      "m1": "0.919"
    },
    {
      "p": "[A Statistical Framework for Low-bitwidth Training of Deep Neural Networks](https://arxiv.org/abs/2010.14298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cjf00000/StatQuant)",
      "n": "PSQ (Chen et al., 2020)",
      "d": "2020-10-27",
      "m1": "0.919"
    },
    {
      "p": "[Entailment as Few-Shot Learner](https://arxiv.org/abs/2104.14690v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/few_shot/efl)",
      "n": "RoBERTa-large 355M + Entailment as Few-shot Learner",
      "d": "2021-04-29",
      "m1": "0.918"
    },
    {
      "p": "[ERNIE 2.0: A Continual Pre-training Framework for Language Understanding](https://arxiv.org/abs/1907.12412v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-1.0)",
      "n": "ERNIE 2.0 Large",
      "d": "2019-07-29",
      "m1": "0.912"
    },
    {
      "p": "[Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT](https://arxiv.org/abs/1909.05840v2)",
      "c": "",
      "n": "Q-BERT (Shen et al., 2020)",
      "d": "2019-09-12",
      "m1": "0.911"
    },
    {
      "p": "[Q8BERT: Quantized 8Bit BERT](https://arxiv.org/abs/1910.06188v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NervanaSystems/nlp-architect/blob/master/nlp_architect/models/transformers/quantized_bert.py)",
      "n": "Q8BERT (Zafrir et al., 2019)",
      "d": "2019-10-14",
      "m1": "0.911"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ELECTRA (no tricks)",
      "d": null,
      "m1": "0.910"
    },
    {
      "p": "[DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DistilBERT 66M",
      "d": "2019-10-02",
      "m1": "0.907"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-3B",
      "d": "2019-10-23",
      "m1": "0.906",
      "m2": "0.898"
    },
    {
      "p": "[CLEAR: Contrastive Learning for Sentence Representation](https://arxiv.org/abs/2012.15466v1)",
      "c": "",
      "n": "MLM+ del-word",
      "d": "2020-12-31",
      "m1": "0.905"
    },
    {
      "p": "[RealFormer: Transformer Likes Residual Attention](https://arxiv.org/abs/2012.11747v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "RealFormer",
      "d": "2020-12-21",
      "m1": "0.9011",
      "m2": "0.8988"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Large",
      "d": "2019-10-23",
      "m1": "0.899"
    },
    {
      "p": "[SpanBERT: Improving Pre-training by Representing and Predicting Spans](https://arxiv.org/abs/1907.10529v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/SpanBERT)",
      "n": "SpanBERT",
      "d": "2019-07-24",
      "m1": "0.899"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Base",
      "d": "2019-10-23",
      "m1": "0.894"
    },
    {
      "p": "[ERNIE 2.0: A Continual Pre-training Framework for Language Understanding](https://arxiv.org/abs/1907.12412v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-1.0)",
      "n": "ERNIE 2.0 Base",
      "d": "2019-07-29",
      "m1": "0.876"
    },
    {
      "p": "[Charformer: Fast Character Transformers via Gradient-based Subword Tokenization](https://arxiv.org/abs/2106.12672v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "Charformer-Tall",
      "d": "2021-06-23",
      "m1": "0.873"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Small",
      "d": "2019-10-23",
      "m1": "0.856",
      "m2": "0.85"
    },
    {
      "p": "[ERNIE: Enhanced Language Representation with Informative Entities](https://arxiv.org/abs/1905.07129v3)",
      "c": "[&check;&nbsp;Link](https://github.com/thunlp/ERNIE)",
      "n": "ERNIE",
      "d": "2019-05-17",
      "m1": "0.832"
    },
    {
      "p": "[How to Train BERT with an Academic Budget](https://arxiv.org/abs/2104.07705v2)",
      "c": "[&check;&nbsp;Link](https://github.com/peteriz/academic-budget-bert)",
      "n": "24hBERT",
      "d": "2021-04-15",
      "m1": "0.820"
    },
    {
      "p": "[TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351v5)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/paddlenlp/transformers/tinybert)",
      "n": "TinyBERT-4 14.5M",
      "d": "2019-09-23",
      "m1": "0.799"
    },
    {
      "p": "[Universal Sentence Encoder](http://arxiv.org/abs/1803.11175v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "USE_T",
      "d": "2018-03-29",
      "m1": "0.782"
    },
    {
      "p": "[AnglE-optimized Text Embeddings](https://arxiv.org/abs/2309.12871v9)",
      "c": "[&check;&nbsp;Link](https://github.com/SeanLee97/AnglE)",
      "n": "AnglE-LLaMA-13B",
      "d": "2023-09-22",
      "m2": "0.8969"
    },
    {
      "p": "[Adversarial Self-Attention for Language Understanding](https://arxiv.org/abs/2206.12608v3)",
      "c": "[&check;&nbsp;Link](https://github.com/gingasan/adversarialsa)",
      "n": "ASA + RoBERTa",
      "d": "2022-06-25",
      "m2": "0.892"
    },
    {
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+LLaMA-30B",
      "d": "2023-07-31",
      "m2": "0.8914"
    },
    {
      "p": "[AnglE-optimized Text Embeddings](https://arxiv.org/abs/2309.12871v9)",
      "c": "[&check;&nbsp;Link](https://github.com/SeanLee97/AnglE)",
      "n": "AnglE-LLaMA-7B",
      "d": "2023-09-22",
      "m2": "0.8897"
    },
    {
      "p": "[AnglE-optimized Text Embeddings](https://arxiv.org/abs/2309.12871v9)",
      "c": "[&check;&nbsp;Link](https://github.com/SeanLee97/AnglE)",
      "n": "AnglE-LLaMA-7B-v2",
      "d": "2023-09-22",
      "m2": "0.8897"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Large 770M",
      "d": "2019-10-23",
      "m2": "0.886"
    },
    {
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+OPT-13B",
      "d": "2023-07-31",
      "m2": "0.8856"
    },
    {
      "p": "[Scaling Sentence Embeddings with Large Language Models](https://arxiv.org/abs/2307.16645v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kongds/scaling_sentemb)",
      "n": "PromptEOL+CSE+OPT-2.7B",
      "d": "2023-07-31",
      "m2": "0.8833"
    },
    {
      "p": "[Improved Universal Sentence Embeddings with Prompt-based Contrastive Learning and Energy-based Learning](https://arxiv.org/abs/2203.06875v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yjiangcm/promcse)",
      "n": "PromCSE-RoBERTa-large (0.355B)",
      "d": "2022-03-14",
      "m2": "0.8787"
    },
    {
      "p": "[Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BigBird",
      "d": "2020-07-28",
      "m2": ".878"
    },
    {
      "p": "[SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://arxiv.org/abs/2104.08821v4)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/text_matching/simcse)",
      "n": "SimCSE-RoBERTalarge",
      "d": "2021-04-18",
      "m2": "0.867"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-RoBERTa-large-cross (unsup.)",
      "d": "2021-09-27",
      "m2": "0.867"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-RoBERTa-large-bi (unsup.)",
      "d": "2021-09-27",
      "m2": "0.8655"
    },
    {
      "p": "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BERT-LARGE",
      "d": "2018-10-11",
      "m2": "0.865"
    },
    {
      "p": "[Adversarial Self-Attention for Language Understanding](https://arxiv.org/abs/2206.12608v3)",
      "c": "[&check;&nbsp;Link](https://github.com/gingasan/adversarialsa)",
      "n": "ASA + BERT-base",
      "d": "2022-06-25",
      "m2": "0.865"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-BERT-large-bi (unsup.)",
      "d": "2021-09-27",
      "m2": "0.8616"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SRoBERTa-NLI-STSb-large",
      "d": "2019-08-27",
      "m2": "0.8615"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SBERT-STSb-base",
      "d": "2019-08-27",
      "m2": "0.8479"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-RoBERTa-base-cross (unsup.)",
      "d": "2021-09-27",
      "m2": "0.8465"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SBERT-STSb-large",
      "d": "2019-08-27",
      "m2": "0.8445"
    },
    {
      "p": "[FNet: Mixing Tokens with Fourier Transforms](https://arxiv.org/abs/2105.03824v4)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "FNet-Large",
      "d": "2021-05-09",
      "m2": "0.84"
    },
    {
      "p": "[Trans-Encoder: Unsupervised sentence-pair modelling through self- and mutual-distillations](https://arxiv.org/abs/2109.13059v4)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/trans-encoder)",
      "n": "Trans-Encoder-BERT-base-bi (unsup.)",
      "d": "2021-09-27",
      "m2": "0.839"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Pearl",
      "d": null,
      "m2": "0.7981"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SBERT-NLI-large",
      "d": "2019-08-27",
      "m2": "0.79"
    },
    {
      "p": "[Fast, Effective, and Self-Supervised: Transforming Masked Language Models into Universal Lexical and Sentence Encoders](https://arxiv.org/abs/2104.08027v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cambridgeltl/mirror-bert)",
      "n": "Mirror-RoBERTa-base (unsup.)",
      "d": "2021-04-16",
      "m2": "0.787"
    },
    {
      "p": "[Generating Datasets with Pretrained Language Models](https://arxiv.org/abs/2104.07540v3)",
      "c": "[&check;&nbsp;Link](https://github.com/timoschick/dino)",
      "n": "Dino (STSb/\u0304\ud83e\udd95)",
      "d": "2021-04-15",
      "m2": "0.7782"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SRoBERTa-NLI-base",
      "d": "2019-08-27",
      "m2": "0.7777"
    },
    {
      "p": "[Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084v1)",
      "c": "[&check;&nbsp;Link](https://github.com/UKPLab/sentence-transformers)",
      "n": "SBERT-NLI-base",
      "d": "2019-08-27",
      "m2": "0.7703"
    },
    {
      "p": "[Generating Datasets with Pretrained Language Models](https://arxiv.org/abs/2104.07540v3)",
      "c": "[&check;&nbsp;Link](https://github.com/timoschick/dino)",
      "n": "Dino (STS/\u0304\ud83e\udd95)",
      "d": "2021-04-15",
      "m2": "0.7651"
    },
    {
      "p": "[Fast, Effective, and Self-Supervised: Transforming Masked Language Models into Universal Lexical and Sentence Encoders](https://arxiv.org/abs/2104.08027v2)",
      "c": "[&check;&nbsp;Link](https://github.com/cambridgeltl/mirror-bert)",
      "n": "Mirror-BERT-base (unsup.)",
      "d": "2021-04-16",
      "m2": "0.764"
    },
    {
      "p": "[On the Sentence Embeddings from Pre-trained Language Models](https://arxiv.org/abs/2011.05864v1)",
      "c": "[&check;&nbsp;Link](https://github.com/InsaneLife/dssm)",
      "n": "BERTlarge-flow (target)",
      "d": "2020-11-02",
      "m2": "0.7226"
    },
    {
      "p": "[An Unsupervised Sentence Embedding Method by Mutual Information Maximization](https://arxiv.org/abs/2009.12061v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yanzhangnlp/IS-BERT)",
      "n": "IS-BERT-NLI",
      "d": "2020-09-25",
      "m2": "0.6921"
    },
    {
      "p": "[Rematch: Robust and Efficient Matching of Local Knowledge Graphs to Improve Structural and Semantic Similarity](https://arxiv.org/abs/2404.02126v1)",
      "c": "[&check;&nbsp;Link](https://github.com/osome-iu/Rematch-RARE)",
      "n": "Rematch",
      "d": "2024-04-02",
      "m2": "0.6652"
    },
    {
      "p": "[Def2Vec: Extensible Word Embeddings from Dictionary Definitions](https://aclanthology.org/2023.icnlsp-1.21)",
      "c": "[&check;&nbsp;Link](https://github.com/IreneMorazzoni/def_2_vec_irene)",
      "n": "Def2Vec",
      "d": "2023-12-16",
      "m2": "0.6372"
    },
    {
      "p": "[DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654v6)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DeBERTa (large)",
      "d": "2020-06-05",
      "m3": "92.5"
    },
    {
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "SMARTRoBERTa",
      "d": "2019-11-08",
      "m4": "92.8",
      "m5": "92.6"
    },
    {
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "SMART-BERT",
      "d": "2019-11-08",
      "m4": "90.0",
      "m5": "89.4"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
