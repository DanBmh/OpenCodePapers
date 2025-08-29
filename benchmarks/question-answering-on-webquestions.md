# question-answering-on-webquestions

[Dataset Link](https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a) \
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
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "CoA",
      "d": "2024-03-26",
      "m1": "70.7"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "CoA w/o actions",
      "d": "2024-03-26",
      "m1": "64.7"
    },
    {
      "p": "[DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714v1)",
      "c": "[&check;&nbsp;Link](https://github.com/stanfordnlp/dsp)",
      "n": "DSP",
      "d": "2023-10-05",
      "m1": "59.4"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "DSP",
      "d": "2024-03-26",
      "m1": "59.4"
    },
    {
      "p": "[FiE: Building a Global Probability Space by Leveraging Early Fusion in Encoder for Open-Domain Question Answering](https://arxiv.org/abs/2211.10147v1)",
      "c": "",
      "n": "FiE+PAQ",
      "d": "2022-11-18",
      "m1": "56.3"
    },
    {
      "p": "[FiE: Building a Global Probability Space by Leveraging Early Fusion in Encoder for Open-Domain Question Answering](https://arxiv.org/abs/2211.10147v1)",
      "c": "",
      "n": "FiE",
      "d": "2022-11-18",
      "m1": "52.4"
    },
    {
      "p": "[FiDO: Fusion-in-Decoder optimized for stronger performance and faster inference](https://arxiv.org/abs/2212.08153v2)",
      "c": "",
      "n": "FiDO",
      "d": "2022-12-15",
      "m1": "51.1"
    },
    {
      "p": "[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "RAG",
      "d": "2020-05-22",
      "m1": "45.2"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "Few-shot",
      "d": "2020-05-28",
      "m1": "44.7"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "Few-shot",
      "d": "2024-03-26",
      "m1": "44.7"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM-540B (Few-Shot)",
      "d": "2022-04-05",
      "m1": "43.5"
    },
    {
      "p": "[Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "Zero-shot",
      "d": "2019-02-14",
      "m1": "43"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "Zero-shot",
      "d": "2024-03-26",
      "m1": "43"
    },
    {
      "p": "[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683v4)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "T5.1.1-XXL+SSM",
      "d": "2019-10-23",
      "m1": "42.8"
    },
    {
      "p": "[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903v6)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/guidance)",
      "n": "CoT",
      "d": "2022-01-28",
      "m1": "42.5"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "CoT",
      "d": "2024-03-26",
      "m1": "42.5"
    },
    {
      "p": "[Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "DPR",
      "d": "2020-04-10",
      "m1": "42.4"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3-175B (Few-Shot)",
      "d": "2020-05-28",
      "m1": "41.5"
    },
    {
      "p": "[REALM: Retrieval-Augmented Language Model Pre-Training](https://arxiv.org/abs/2002.08909v1)",
      "c": "[&check;&nbsp;Link](https://github.com/deepset-ai/haystack)",
      "n": "REALM",
      "d": "2020-02-10",
      "m1": "40.7"
    },
    {
      "p": "[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ysymyth/ReAct)",
      "n": "React",
      "d": "2022-10-06",
      "m1": "38.3"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "React",
      "d": "2024-03-26",
      "m1": "38.3"
    },
    {
      "p": "[Latent Retrieval for Weakly Supervised Open Domain Question Answering](https://arxiv.org/abs/1906.00300v3)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/language/tree/master/language/orqa)",
      "n": "ORQA",
      "d": "2019-06-01",
      "m1": "36.4"
    },
    {
      "p": "[Measuring and Narrowing the Compositionality Gap in Language Models](https://arxiv.org/abs/2210.03350v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ofirpress/self-ask)",
      "n": "Self-Ask",
      "d": "2022-10-07",
      "m1": "31.1"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "Self-Ask",
      "d": "2024-03-26",
      "m1": "31.1"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-L (one-shot)",
      "d": "2023-05-17",
      "m1": "28.2"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-M (one-shot)",
      "d": "2023-05-17",
      "m1": "26.9"
    },
    {
      "p": "[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ysymyth/tree-of-thought-llm)",
      "n": "ToT",
      "d": "2023-05-17",
      "m1": "26.3"
    },
    {
      "p": "[Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models](https://arxiv.org/abs/2403.17359v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MAGICS-LAB/Chain-of-Actions)",
      "n": "ToT",
      "d": "2024-03-26",
      "m1": "26.3"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3-175B (One-Shot)",
      "d": "2020-05-28",
      "m1": "25.3"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM-540B (One-Shot)",
      "d": "2022-04-05",
      "m1": "22.6"
    },
    {
      "p": "[PaLM 2 Technical Report](https://arxiv.org/abs/2305.10403v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eternityyw/tram-benchmark)",
      "n": "PaLM 2-S (one-shot)",
      "d": "2023-05-17",
      "m1": "21.8"
    },
    {
      "p": "[GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06905v2)",
      "c": "",
      "n": "GLaM 62B/64E (Zero-Shot)",
      "d": "2021-12-13",
      "m1": "15.5"
    },
    {
      "p": "[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165v4)",
      "c": "[&check;&nbsp;Link](https://github.com/ggml-org/llama.cpp)",
      "n": "GPT-3-175B (Zero-Shot)",
      "d": "2020-05-28",
      "m1": "14.4"
    },
    {
      "p": "[PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311v5)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/CoCa-pytorch)",
      "n": "PaLM-540B (Zero-Shot)",
      "d": "2022-04-05",
      "m1": "10.6"
    },
    {
      "p": "[Large-scale Simple Question Answering with Memory Networks](http://arxiv.org/abs/1506.02075v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/ParlAI)",
      "n": "Memory Networks (ensemble)",
      "d": "2015-06-05",
      "m2": "42.2%"
    },
    {
      "p": "[Question Answering with Subgraph Embeddings](http://arxiv.org/abs/1406.3676v3)",
      "c": "[&check;&nbsp;Link](https://github.com/gmtt/CSCI590)",
      "n": "Subgraph embeddings",
      "d": "2014-06-14",
      "m2": "39.2%"
    },
    {
      "p": "[Open Question Answering with Weakly Supervised Embedding Models](http://arxiv.org/abs/1404.4326v1)",
      "c": "",
      "n": "Weakly Supervised Embeddings",
      "d": "2014-04-16",
      "m2": "29.7%"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
