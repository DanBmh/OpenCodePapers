# math-word-problem-solving-on-math23k

[Dataset Link](https://ai.tencent.com/ailab/nlp/dialogue/#datasets) \
Task Hierarchy: ['Mathematical Reasoning', 'Math Word Problem Solving']

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
      "label": "Accuracy (5-fold)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Accuracy (training-test)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "weakly-supervised",
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
      "p": "[Teaching-Inspired Integrated Prompting Framework: A Novel Approach for Enhancing Reasoning in Large Language Models](https://arxiv.org/abs/2410.08068v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sallytan13/teaching-inspired-prompting)",
      "n": "GPT-4 (Teaching-Inspired)",
      "d": "2024-10-10",
      "m1": "94.3"
    },
    {
      "p": "[Multi-View Reasoning: Consistent Contrastive Learning for Math Word Problem](https://arxiv.org/abs/2210.11694v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zwq2018/multi-view-consistency-for-mwp)",
      "n": "Multi-view* (ours)",
      "d": "2022-10-21",
      "m1": "85.2",
      "m2": "87.1"
    },
    {
      "p": "[Generate & Rank: A Multi-task Framework for Math Word Problems](https://arxiv.org/abs/2109.03034v1)",
      "c": "",
      "n": "Generate and Rank",
      "d": "2021-09-07",
      "m1": "84.3",
      "m2": "85.4"
    },
    {
      "p": "[An Expression Tree Decoding Strategy for Mathematical Equation Generation](https://arxiv.org/abs/2310.09619v3)",
      "c": "[&check;&nbsp;Link](https://github.com/zwq2018/multi-view-consistency-for-mwp)",
      "n": "Exp-Tree",
      "d": "2023-10-14",
      "m1": "84.1",
      "m2": "86.2"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "REAL2: Memory-augmented Solver",
      "d": null,
      "m1": "83.18",
      "m2": "85.2"
    },
    {
      "p": "[Learning to Reason Deductively: Math Word Problem Solving as Complex Relation Extraction](https://arxiv.org/abs/2203.10316v4)",
      "c": "[&check;&nbsp;Link](https://github.com/allanj/deductive-mwp)",
      "n": "Roberta-DeductReasoner",
      "d": "2022-03-19",
      "m1": "83"
    },
    {
      "p": "[MWP-BERT: Numeracy-Augmented Pre-training for Math Word Problem Solving](https://arxiv.org/abs/2107.13435v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lzhenwen/mwp-bert)",
      "n": "MWP-BERT",
      "d": "2021-07-28",
      "m1": "82.4",
      "m2": "84.7"
    },
    {
      "p": "[Recall and Learn: A Memory-augmented Solver for Math Word Problems](https://arxiv.org/abs/2109.13112v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sfeng-m/real4mwp)",
      "n": "Recall and Learn",
      "d": "2021-09-27",
      "m1": "80.8",
      "m2": "82.3"
    },
    {
      "p": "[MWPToolkit: An Open-Source Framework for Deep Learning-Based Math Word Problem Solvers](https://arxiv.org/abs/2109.00799v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lyh-yf/mwptoolkit)",
      "n": "RoBERTaGen",
      "d": "2021-09-02",
      "m1": "76.6"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GTS w/ Data Augmentation",
      "d": null,
      "m1": "75.9"
    },
    {
      "p": "[Graph-to-Tree Learning for Solving Math Word Problems](https://aclanthology.org/2020.acl-main.362)",
      "c": "[&check;&nbsp;Link](https://github.com/2003pro/Graph2Tree)",
      "n": "Graph2Tree",
      "d": "2020-07-01",
      "m1": "75.5",
      "m2": "77.4"
    },
    {
      "p": "[Semantically-Aligned Universal Tree-Structured Solver for Math Word Problems](https://arxiv.org/abs/2010.06823v1)",
      "c": "[&check;&nbsp;Link](https://github.com/QinJinghui/SAU-Solver)",
      "n": "SAU-Solver",
      "d": "2020-10-14",
      "m1": "74.84"
    },
    {
      "p": "[A Goal-Driven Tree-Structured Neural Model for Math Word Problems](https://www.ijcai.org/Proceedings/2019/736)",
      "c": "[&check;&nbsp;Link](https://github.com/ShichaoSun/math_seq2tree)",
      "n": "GTS",
      "d": "2019-08-10",
      "m1": "74.3"
    },
    {
      "p": "[Modeling Intra-Relation in Math Word Problems with Different Functional Multi-Head Attentions](https://aclanthology.org/P19-1619)",
      "c": "[&check;&nbsp;Link](https://github.com/lijierui/group-attention)",
      "n": "GROUP-ATT",
      "d": "2019-07-01",
      "m1": "66.9",
      "m2": "69.5"
    },
    {
      "p": "[Deep Neural Solver for Math Word Problems](https://aclanthology.org/D17-1088)",
      "c": "",
      "n": "Hybrid model w/ SNI",
      "d": "2017-09-01",
      "m1": "64.7"
    },
    {
      "p": "[ATHENA: Mathematical Reasoning with Thought Expansion](https://arxiv.org/abs/2311.01036v1)",
      "c": "[&check;&nbsp;Link](https://github.com/the-jb/athena-math)",
      "n": "ATHENA (roberta-large)",
      "d": "2023-11-02",
      "m2": "86.5"
    },
    {
      "p": "[ATHENA: Mathematical Reasoning with Thought Expansion](https://arxiv.org/abs/2311.01036v1)",
      "c": "[&check;&nbsp;Link](https://github.com/the-jb/athena-math)",
      "n": "ATHENA (roberta-base)",
      "d": "2023-11-02",
      "m2": "84.4"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "T-RNN",
      "d": null,
      "m2": "66.9"
    },
    {
      "p": "[Learning by Fixing: Solving Math Word Problems with Weak Supervision](https://arxiv.org/abs/2012.10582v2)",
      "c": "[&check;&nbsp;Link](https://github.com/evelinehong/LBF)",
      "n": "LBF",
      "d": "2020-12-19",
      "m3": "59.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
