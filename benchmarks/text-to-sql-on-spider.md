# text-to-sql-on-spider

[Dataset Link](https://zenodo.org/record/5205322#.YTts_o5Kgab) \
Task Hierarchy: ['Text-To-SQL']

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
      "label": "Execution Accuracy (Test)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Exact Match Accuracy (Test)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Execution Accuracy (Dev)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Exact Match Accuracy (Dev)",
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
      "p": "[A Preview of XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL](https://arxiv.org/abs/2411.08599v3)",
      "c": "[&check;&nbsp;Link](https://github.com/XGenerationLab/XiYan-SQL)",
      "n": "XiYan-SQL",
      "d": "2024-11-13",
      "m1": "89.65"
    },
    {
      "p": "[PET-SQL: A Prompt-Enhanced Two-Round Refinement of Text-to-SQL with Cross-consistency](https://arxiv.org/abs/2403.09732v4)",
      "c": "[&check;&nbsp;Link](https://github.com/zhshlii/petsql)",
      "n": "PET-SQL",
      "d": "2024-03-13",
      "m1": "87.6",
      "m2": "66.6"
    },
    {
      "p": "[Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation](https://arxiv.org/abs/2308.15363v4)",
      "c": "[&check;&nbsp;Link](https://github.com/beachwang/dail-sql)",
      "n": "DAIL-SQL + GPT-4 + Self-Consistency",
      "d": "2023-08-29",
      "m1": "86.6",
      "m3": "84.4",
      "m4": "74.4"
    },
    {
      "p": "[DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction](https://arxiv.org/abs/2304.11015v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mohammadrezapourreza/few-shot-nl2sql-with-prompting)",
      "n": "DIN-SQL + GPT-4",
      "d": "2023-04-21",
      "m1": "85.3",
      "m2": "60"
    },
    {
      "p": "[MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation](https://arxiv.org/abs/2410.12916v1)",
      "c": "[&check;&nbsp;Link](https://github.com/layer6ai-labs/msc-sql)",
      "n": "MSc-SQL",
      "d": "2024-10-16",
      "m1": "84.7"
    },
    {
      "p": "[Learning Metadata-Agnostic Representations for Text-to-SQL In-Context Example Selection](https://arxiv.org/abs/2410.14049v1)",
      "c": "",
      "n": "MARLO + Claude 2.1",
      "d": "2024-10-17",
      "m1": "84.0",
      "m3": "83.6"
    },
    {
      "p": "[C3: Zero-shot Text-to-SQL with ChatGPT](https://arxiv.org/abs/2307.07306v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bigbigwatermalon/c3sql)",
      "n": "C3 + ChatGPT + Zero-Shot",
      "d": "2023-07-14",
      "m1": "82.3",
      "m3": "81.8"
    },
    {
      "p": "[RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL](https://arxiv.org/abs/2302.05965v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ruckbreasoning/resdsql)",
      "n": "RESDSQL-3B + NatSQL",
      "d": "2023-02-12",
      "m1": "79.9",
      "m2": "72.0",
      "m3": "84.1",
      "m4": "80.5"
    },
    {
      "p": "[Improving Generalization in Language Model-Based Text-to-SQL Semantic Parsing: Two Simple Semantic Boundary-Based Techniques](https://arxiv.org/abs/2305.17378v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dakingrai/ood-generalization-semantic-boundary-techniques)",
      "n": "T5-3B+NatSQL+Token Preprocessing",
      "d": "2023-05-27",
      "m1": "78",
      "m3": "73.7",
      "m4": "69.4"
    },
    {
      "p": "[Graphix-T5: Mixing Pre-Trained Transformers with Graph-Aware Layers for Text-to-SQL Parsing](https://arxiv.org/abs/2301.07507v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/graphix)",
      "n": "Graphix-3B+PICARD",
      "d": "2023-01-18",
      "m1": "77.6",
      "m3": "81.0",
      "m4": "77.1"
    },
    {
      "p": "[T5-SR: A Unified Seq-to-Seq Decoding Strategy for Semantic Parsing](https://arxiv.org/abs/2306.08368v1)",
      "c": "[&check;&nbsp;Link](https://github.com/JuruoMP/T5-SR)",
      "n": "T5-SR",
      "d": "2023-06-14",
      "m1": "75.2",
      "m2": "72.4",
      "m4": "77.2"
    },
    {
      "p": "[PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models](https://arxiv.org/abs/2109.05093v1)",
      "c": "[&check;&nbsp;Link](https://github.com/servicenow/picard)",
      "n": "T5-3B + PICARD",
      "d": "2021-09-10",
      "m1": "75.1",
      "m2": "71.9 ",
      "m4": "75.5"
    },
    {
      "p": "[SADGA: Structure-Aware Dual Graph Aggregation Network for Text-to-SQL](https://arxiv.org/abs/2111.00653v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmirlab-group/sadga)",
      "n": "SADGA + GAP",
      "d": "2021-11-01",
      "m2": "70.1",
      "m4": "73.1"
    },
    {
      "p": "[RYANSQL: Recursively Applying Sketch-based Slot Fillings for Complex Text-to-SQL in Cross-Domain Databases](https://arxiv.org/abs/2004.03125v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kakaoenterprise/RYANSQL)",
      "n": "RYANSQL (BERT)",
      "d": "2020-04-07",
      "m2": "58.2",
      "m4": "66.6"
    },
    {
      "p": "[DataGpt-SQL-7B: An Open-Source Language Model for Text-to-SQL](https://arxiv.org/abs/2409.15985v1)",
      "c": "",
      "n": "datagpt-sql-7B + InvalidSQL-Feedback",
      "d": "2024-09-24",
      "m3": "87.2",
      "m4": "81.6"
    },
    {
      "p": "[DataGpt-SQL-7B: An Open-Source Language Model for Text-to-SQL](https://arxiv.org/abs/2409.15985v1)",
      "c": "",
      "n": "datagpt-sql-7B",
      "d": "2024-09-24",
      "m3": "84.8",
      "m4": "80.3"
    },
    {
      "p": "[LEVER: Learning to Verify Language-to-Code Generation with Execution](https://arxiv.org/abs/2302.08468v3)",
      "c": "[&check;&nbsp;Link](https://github.com/niansong1996/lever)",
      "n": "code-davinci-002 175B (LEVER)",
      "d": "2023-02-16",
      "m3": "81.9"
    },
    {
      "p": "[Knowledge-to-SQL: Enhancing SQL Generation with Data Expert LLM](https://arxiv.org/abs/2402.11517v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Rcrossmeister/Knowledge-to-SQL)",
      "n": "DELLM + GPT-4",
      "d": "2024-02-18",
      "m3": "71.68"
    },
    {
      "p": "[Learning Contextual Representations for Semantic Parsing with Generation-Augmented Pre-Training](https://arxiv.org/abs/2012.10309v1)",
      "c": "[&check;&nbsp;Link](https://github.com/awslabs/gap-text2sql)",
      "n": "RATSQL + GAP",
      "d": "2020-12-18",
      "m4": "71.8"
    },
    {
      "p": "[TaBERT: Pretraining for Joint Understanding of Textual and Tabular Data](https://arxiv.org/abs/2005.08314v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/tabert)",
      "n": "MAPO + TABERTLarge (K = 3)",
      "d": "2020-05-17",
      "m4": "64.5"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
