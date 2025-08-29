# semantic-textual-similarity-on-mrpc

[Dataset Link](https://www.microsoft.com/en-us/download/details.aspx?id=52398) \
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
      "label": "Accuracy",
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
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "MT-DNN-SMART",
      "d": "2019-11-08",
      "m1": "93.7%",
      "m2": "91.7"
    },
    {
      "p": "[ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942v6)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "ALBERT",
      "d": "2019-09-26",
      "m1": "93.4%"
    },
    {
      "p": "[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "RoBERTa (ensemble)",
      "d": "2019-07-26",
      "m1": "92.3%"
    },
    {
      "p": "[StructBERT: Incorporating Language Structures into Pre-training for Deep Language Understanding](https://arxiv.org/abs/1908.04577v3)",
      "c": "",
      "n": "StructBERTRoBERTa ensemble",
      "d": "2019-08-13",
      "m1": "91.5%",
      "m2": "93.6%"
    },
    {
      "p": "[Learning to Encode Position for Transformer with Continuous Dynamical Model](https://arxiv.org/abs/2003.09229v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xuanqing94/FLOATER)",
      "n": "FLOATER-large",
      "d": "2020-03-13",
      "m1": "91.4%"
    },
    {
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "SMART",
      "d": "2019-11-08",
      "m1": "91.3%"
    },
    {
      "p": "[LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339v2)",
      "c": "[&check;&nbsp;Link](https://github.com/timdettmers/bitsandbytes)",
      "n": "RoBERTa-large 355M (MLP quantized vector-wise, fine-tuned)",
      "d": "2022-08-15",
      "m1": "91.0%"
    },
    {
      "p": "[SpanBERT: Improving Pre-training by Representing and Predicting Spans](https://arxiv.org/abs/1907.10529v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/SpanBERT)",
      "n": "SpanBERT",
      "d": "2019-07-24",
      "m1": "90.9%"
    },
    {
      "p": "[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "XLNet (single model)",
      "d": "2019-06-19",
      "m1": "90.8%"
    },
    {
      "p": "[AutoBERT-Zero: Evolving BERT Backbone from Scratch](https://arxiv.org/abs/2107.07445v2)",
      "c": "",
      "n": "AutoBERT-Zero (Large)",
      "d": "2021-07-15",
      "m1": "90.7%"
    },
    {
      "p": "[CLEAR: Contrastive Learning for Sentence Representation](https://arxiv.org/abs/2012.15466v1)",
      "c": "",
      "n": "MLM+ del-word+ reorder",
      "d": "2020-12-31",
      "m1": "90.6%"
    },
    {
      "p": "[AutoBERT-Zero: Evolving BERT Backbone from Scratch](https://arxiv.org/abs/2107.07445v2)",
      "c": "",
      "n": "AutoBERT-Zero (Base)",
      "d": "2021-07-15",
      "m1": "90.5%"
    },
    {
      "p": "[A Statistical Framework for Low-bitwidth Training of Deep Neural Networks](https://arxiv.org/abs/2010.14298v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cjf00000/StatQuant)",
      "n": "PSQ (Chen et al., 2020)",
      "d": "2020-10-27",
      "m1": "90.4"
    },
    {
      "p": "[DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DistilBERT 66M",
      "d": "2019-10-02",
      "m1": "90.2%"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-11B",
      "d": "2019-10-23",
      "m1": "90.0%",
      "m2": "91.9"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Large",
      "d": "2019-10-23",
      "m1": "89.9%",
      "m2": "92.4"
    },
    {
      "p": "[Q8BERT: Quantized 8Bit BERT](https://arxiv.org/abs/1910.06188v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NervanaSystems/nlp-architect/blob/master/nlp_architect/models/transformers/quantized_bert.py)",
      "n": "Q8BERT (Zafrir et al., 2019)",
      "d": "2019-10-14",
      "m1": "89.7"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ELECTRA",
      "d": null,
      "m1": "89.6%"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-3B",
      "d": "2019-10-23",
      "m1": "89.2%",
      "m2": "92.5"
    },
    {
      "p": "[MobileBERT: a Compact Task-Agnostic BERT for Resource-Limited Devices](https://arxiv.org/abs/2004.02984v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/official/nlp/projects/mobilebert)",
      "n": "MobileBERT",
      "d": "2020-04-06",
      "m1": "88.8%"
    },
    {
      "p": "[ERNIE: Enhanced Language Representation with Informative Entities](https://arxiv.org/abs/1905.07129v3)",
      "c": "[&check;&nbsp;Link](https://github.com/thunlp/ERNIE)",
      "n": "ERNIE",
      "d": "2019-05-17",
      "m1": "88.2%"
    },
    {
      "p": "[Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT](https://arxiv.org/abs/1909.05840v2)",
      "c": "",
      "n": "Q-BERT (Shen et al., 2020)",
      "d": "2019-09-12",
      "m1": "88.2"
    },
    {
      "p": "[FNet: Mixing Tokens with Fourier Transforms](https://arxiv.org/abs/2105.03824v4)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "FNet-Large",
      "d": "2021-05-09",
      "m1": "88%"
    },
    {
      "p": "[SqueezeBERT: What can computer vision teach NLP about efficient neural networks?](https://arxiv.org/abs/2006.11316v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers/blob/main/src/transformers/models/squeezebert/modeling_squeezebert.py)",
      "n": "SqueezeBERT",
      "d": "2020-06-19",
      "m1": "87.8%"
    },
    {
      "p": "[Charformer: Fast Character Transformers via Gradient-based Subword Tokenization](https://arxiv.org/abs/2106.12672v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "Charformer-Tall",
      "d": "2021-06-23",
      "m1": "87.5%",
      "m2": "91.4"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Base",
      "d": "2019-10-23",
      "m1": "87.5%",
      "m2": "90.7"
    },
    {
      "p": "[How to Train BERT with an Academic Budget](https://arxiv.org/abs/2104.07705v2)",
      "c": "[&check;&nbsp;Link](https://github.com/peteriz/academic-budget-bert)",
      "n": "24hBERT",
      "d": "2021-04-15",
      "m1": "87.5%"
    },
    {
      "p": "[ERNIE 2.0: A Continual Pre-training Framework for Language Understanding](https://arxiv.org/abs/1907.12412v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-1.0)",
      "n": "ERNIE 2.0 Large",
      "d": "2019-07-29",
      "m1": "87.4%"
    },
    {
      "p": "[TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351v5)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/paddlenlp/transformers/tinybert)",
      "n": "TinyBERT-6 67M",
      "d": "2019-09-23",
      "m1": "87.3%"
    },
    {
      "p": "[RealFormer: Transformer Likes Residual Attention](https://arxiv.org/abs/2012.11747v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "RealFormer",
      "d": "2020-12-21",
      "m1": "87.01%",
      "m2": "90.91%"
    },
    {
      "p": "[SubRegWeigh: Effective and Efficient Annotation Weighing with Subword Regularization](https://arxiv.org/abs/2409.06216v2)",
      "c": "[&check;&nbsp;Link](https://github.com/4ldk/SubRegWeigh)",
      "n": "RoBERTa + SubRegWeigh (K-means)",
      "d": "2024-09-10",
      "m1": "86.82%"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5-Small",
      "d": "2019-10-23",
      "m1": "86.6%",
      "m2": "89.7"
    },
    {
      "p": "[TinyBERT: Distilling BERT for Natural Language Understanding](https://arxiv.org/abs/1909.10351v5)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/paddlenlp/transformers/tinybert)",
      "n": "TinyBERT-4 14.5M",
      "d": "2019-09-23",
      "m1": "86.4%"
    },
    {
      "p": "[ERNIE 2.0: A Continual Pre-training Framework for Language Understanding](https://arxiv.org/abs/1907.12412v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-1.0)",
      "n": "ERNIE 2.0 Base",
      "d": "2019-07-29",
      "m1": "86.1%"
    },
    {
      "p": "[Discriminative Improvements to Distributional Sentence Similarity](https://aclanthology.org/D13-1090)",
      "c": "",
      "n": "TF-KLD",
      "d": "2013-10-01",
      "m1": "80.4%",
      "m2": "85.9%"
    },
    {
      "p": "[Learning General Purpose Distributed Sentence Representations via Large Scale Multi-task Learning](http://arxiv.org/abs/1804.00079v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "GenSen",
      "d": "2018-03-30",
      "m1": "78.6%",
      "m2": "84.4%"
    },
    {
      "p": "[Supervised Learning of Universal Sentence Representations from Natural Language Inference Data](http://arxiv.org/abs/1705.02364v5)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "InferSent",
      "d": "2017-05-05",
      "m1": "76.2%",
      "m2": "83.1%"
    },
    {
      "p": "[Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BigBird",
      "d": "2020-07-28",
      "m2": "91.5"
    },
    {
      "p": "[Entailment as Few-Shot Learner](https://arxiv.org/abs/2104.14690v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/few_shot/efl)",
      "n": "RoBERTa-large 355M + Entailment as Few-shot Learner",
      "d": "2021-04-29",
      "m2": "91.0"
    },
    {
      "p": "[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805v2)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "BERT-LARGE",
      "d": "2018-10-11",
      "m2": "89.3"
    },
    {
      "p": "[Nystr\u00f6mformer: A Nystr\u00f6m-Based Algorithm for Approximating Self-Attention](https://arxiv.org/abs/2102.03902v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/xformers)",
      "n": "Nystr\u00f6mformer",
      "d": "2021-02-07",
      "m2": "88.1%"
    },
    {
      "p": "[Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning](https://arxiv.org/abs/2012.13255v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rabeehk/compacter)",
      "n": "BERT-Base",
      "d": "2020-12-22"
    },
    {
      "p": "[Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning](https://arxiv.org/abs/2012.13255v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rabeehk/compacter)",
      "n": "BERT-Large",
      "d": "2020-12-22"
    },
    {
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "SMART-BERT",
      "d": "2019-11-08"
    },
    {
      "p": "[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://arxiv.org/abs/1911.03437v5)",
      "c": "[&check;&nbsp;Link](https://github.com/namisan/mt-dnn)",
      "n": "SMARTRoBERTa",
      "d": "2019-11-08"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
