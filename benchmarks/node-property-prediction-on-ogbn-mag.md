# node-property-prediction-on-ogbn-mag

[Dataset Link](https://ogb.stanford.edu/) \
Task Hierarchy: ['Node Property Prediction']

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
      "label": "Test Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Ext. data",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Validation Accuracy",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Number of params",
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
      "n": "LDHGNN",
      "d": null,
      "m1": "0.8789 \u00b1 0.0024",
      "m2": "No",
      "m3": "0.8836 \u00b1 0.0028",
      "m4": "7720368"
    },
    {
      "p": "[Loss-aware Curriculum Learning for Heterogeneous Graph Neural Networks](https://arxiv.org/abs/2402.18875v1)",
      "c": "[&check;&nbsp;Link](https://github.com/calderkatyal/CPSC483FinalProject)",
      "n": "CLGNN",
      "d": "2024-02-29",
      "m1": "0.7956 \u00b1 0.0047",
      "m2": "No",
      "m3": "0.8021 \u00b1 0.0020",
      "m4": "7720368"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HGAMLP+LP+MS(LINE embs)",
      "d": null,
      "m1": "0.5794 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.5997 \u00b1 0.0012",
      "m4": "8469021"
    },
    {
      "p": "[Long-range Meta-path Search on Large-scale Heterogeneous Graphs](https://arxiv.org/abs/2307.08430v6)",
      "c": "[&check;&nbsp;Link](https://github.com/jhl-hust/lmsps)",
      "n": "LMSPS (w/o embs)",
      "d": "2023-07-17",
      "m1": "0.5784 \u00b1 0.0022",
      "m2": "No",
      "m3": "0.5951 \u00b1 0.0007",
      "m4": "16470044"
    },
    {
      "p": "[Efficient Heterogeneous Graph Learning via Random Projection](https://arxiv.org/abs/2310.14481v2)",
      "c": "[&check;&nbsp;Link](https://github.com/CrawlScript/RpHGNN)",
      "n": "RpHGNN+LP+CR (LINE embs)",
      "d": "2023-10-23",
      "m1": "0.5773 \u00b1 0.0012",
      "m2": "No",
      "m3": "0.5973 \u00b1 0.0008",
      "m4": "7720368"
    },
    {
      "p": "[Long-range Meta-path Search on Large-scale Heterogeneous Graphs](https://arxiv.org/abs/2307.08430v6)",
      "c": "[&check;&nbsp;Link](https://github.com/jhl-hust/lmsps)",
      "n": "LMSPS(w/o ComplEx embs)",
      "d": "2023-07-17",
      "m1": "0.5767 \u00b1 0.0015",
      "m2": "No",
      "m3": "0.5902 \u00b1 0.0016",
      "m4": "16470044"
    },
    {
      "p": "[Spectral Heterogeneous Graph Convolutions via Positive Noncommutative Polynomials](https://arxiv.org/abs/2305.19872v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ivam-he/PSHGCN/tree/main/ogbn-mag)",
      "n": "PSHGCN (ComplEx embs)",
      "d": "2023-05-31",
      "m1": "0.5752 \u00b1 0.0011",
      "m2": "No",
      "m3": "0.5943 \u00b1 0.0015",
      "m4": "4852434"
    },
    {
      "p": "[Spectral Heterogeneous Graph Convolutions via Positive Noncommutative Polynomials](https://arxiv.org/abs/2305.19872v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ivam-he/PSHGCN/tree/main/ogbn-mag)",
      "n": "PSHGCN",
      "d": "2023-05-31",
      "m1": "0.5752 \u00b1 0.0011",
      "m2": "No",
      "m3": "0.5943 \u00b1 0.0015",
      "m4": "4852434"
    },
    {
      "p": "[Long-range Meta-path Search on Large-scale Heterogeneous Graphs](https://arxiv.org/abs/2307.08430v6)",
      "c": "[&check;&nbsp;Link](https://github.com/jhl-hust/lmsps)",
      "n": "LDMLP(w/o ComplEx embs)",
      "d": "2023-07-17",
      "m1": "0.5739 \u00b1 0.0012",
      "m2": "No",
      "m3": "0.5888 \u00b1 0.0015",
      "m4": "13177884"
    },
    {
      "p": "[Simple and Efficient Heterogeneous Graph Neural Network](https://arxiv.org/abs/2207.02547v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ict-gimlab/sehgnn)",
      "n": "SeHGNN (ComplEx embs)",
      "d": "2022-07-06",
      "m1": "0.5719 \u00b1 0.0012",
      "m2": "No",
      "m3": "0.5917 \u00b1 0.0009",
      "m4": "8371231"
    },
    {
      "p": "[Simple and Efficient Heterogeneous Graph Neural Network](https://arxiv.org/abs/2207.02547v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ict-gimlab/sehgnn)",
      "n": "SeHGNN",
      "d": "2022-07-06",
      "m1": "0.5671 \u00b1 0.0014",
      "m2": "No",
      "m3": "0.5870 \u00b1 0.0008",
      "m4": "8371231"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "NARS-GAMLP+RLU+SCR",
      "d": "2021-12-08",
      "m1": "0.5631 \u00b1 0.0021",
      "m2": "No",
      "m3": "0.5734 \u00b1 0.0035",
      "m4": "6734882"
    },
    {
      "p": "[Graph Attention Multi-Layer Perceptron](https://arxiv.org/abs/2206.04355v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pku-dair/gamlp)",
      "n": "NARS-GAMLP+RLU",
      "d": "2022-06-09",
      "m1": "0.5590 \u00b1 0.0027",
      "m2": "No",
      "m3": "0.5702 \u00b1 0.0041",
      "m4": "6734882"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "NARS-GAMLP+RLU",
      "d": null,
      "m1": "0.5590 \u00b1 0.0027",
      "m2": "No",
      "m3": "0.5702 \u00b1 0.0041",
      "m4": "6734882"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "NARS-GAMLP+SCR-m",
      "d": "2021-12-08",
      "m1": "0.5451 \u00b1 0.0019",
      "m2": "No",
      "m3": "0.5590 \u00b1 0.0028",
      "m4": "6734882"
    },
    {
      "p": "[Scalable and Adaptive Graph Neural Networks with Self-Label-Enhanced training](https://arxiv.org/abs/2104.09376v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "NARS_SAGN+SLE",
      "d": "2021-04-19",
      "m1": "0.5440 \u00b1 0.0015",
      "m2": "No",
      "m3": "0.5591 \u00b1 0.0017",
      "m4": "3846330"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "NARS-GAMLP+SCR",
      "d": "2021-12-08",
      "m1": "0.5432 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.5654 \u00b1 0.0021",
      "m4": "6734882"
    },
    {
      "p": "[Graph Attention Multi-Layer Perceptron](https://arxiv.org/abs/2206.04355v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pku-dair/gamlp)",
      "n": "NARS-GAMLP",
      "d": "2022-06-09",
      "m1": "0.5396 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.5548 \u00b1 0.0008",
      "m4": "6734882"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "NARS-GAMLP",
      "d": null,
      "m1": "0.5396 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.5548 \u00b1 0.0008",
      "m4": "6734882"
    },
    {
      "p": "[Label-Enhanced Graph Neural Network for Semi-supervised Node Classification](https://arxiv.org/abs/2205.15653v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yule-BUAA/LEGNN)",
      "n": "LEGNN + AS-Train",
      "d": "2022-05-31",
      "m1": "0.5378 \u00b1 0.0016",
      "m2": "No",
      "m3": "0.5528 \u00b1 0.0013",
      "m4": "5147997"
    },
    {
      "p": "[Label-Enhanced Graph Neural Network for Semi-supervised Node Classification](https://arxiv.org/abs/2205.15653v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yule-BUAA/LEGNN)",
      "n": "LEGNN",
      "d": "2022-05-31",
      "m1": "0.5276 \u00b1 0.0014",
      "m2": "No",
      "m3": "0.5443 \u00b1 0.0009",
      "m4": "5147997"
    },
    {
      "p": "[Scalable Graph Neural Networks for Heterogeneous Graphs](https://arxiv.org/abs/2011.09679v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/NARS)",
      "n": "NARS",
      "d": "2020-11-19",
      "m1": "0.5240 \u00b1 0.0016",
      "m2": "No",
      "m3": "0.5372 \u00b1 0.0009",
      "m4": "4130149"
    },
    {
      "p": "[Heterogeneous Graph Representation Learning with Relation Awareness](https://arxiv.org/abs/2105.11122v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yule-BUAA/R-HGNN)",
      "n": "R-HGNN",
      "d": "2021-05-24",
      "m1": "0.5204 \u00b1 0.0026",
      "m2": "No",
      "m3": "0.5361 \u00b1 0.0022",
      "m4": "5638053"
    },
    {
      "p": "[Residual Network and Embedding Usage: New Tricks of Node Classification with Graph Convolutional Networks](https://arxiv.org/abs/2105.08330v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ytchx1999/PyG-OGB-Tricks/tree/main/DGL-ogbn-arxiv)",
      "n": "R-GSN + metapath2vec",
      "d": "2021-05-18",
      "m1": "0.5109 \u00b1 0.0038",
      "m2": "No",
      "m3": "0.5295 \u00b1 0.0042",
      "m4": "309777252"
    },
    {
      "p": "[Hybrid Micro/Macro Level Convolution for Heterogeneous Graph Learning](https://arxiv.org/abs/2012.14722v1)",
      "c": "[&check;&nbsp;Link](https://github.com/yule-BUAA/HGConv)",
      "n": "HGConv",
      "d": "2020-12-29",
      "m1": "0.5045 \u00b1 0.0017",
      "m2": "No",
      "m3": "0.5300 \u00b1 0.0018",
      "m4": "2850405"
    },
    {
      "p": "[Modeling Relational Data with Graph Convolutional Networks](http://arxiv.org/abs/1703.06103v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/tensorflow/rgcn)",
      "n": "R-GSN",
      "d": "2017-03-17",
      "m1": "0.5032 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.5182 \u00b1 0.0041",
      "m4": "154373028"
    },
    {
      "p": "[Heterogeneous Graph Transformer](https://arxiv.org/abs/2003.01332v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/hgt)",
      "n": "HGT (TransE embs)",
      "d": "2020-03-03",
      "m1": "0.4982 \u00b1 0.0013",
      "m2": "No",
      "m3": "0.5124 \u00b1 0.0046",
      "m4": "26877657"
    },
    {
      "p": "[GraphSAINT: Graph Sampling Based Inductive Learning Method](https://arxiv.org/abs/1907.04931v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/graphsaint)",
      "n": "GraphSAINT + metapath2vec",
      "d": "2019-07-10",
      "m1": "0.4966 \u00b1 0.0022",
      "m2": "No",
      "m3": "0.5066 \u00b1 0.0017",
      "m4": "309764724"
    },
    {
      "p": "[Heterogeneous Graph Transformer](https://arxiv.org/abs/2003.01332v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/hgt)",
      "n": "HGT (LADIES Sample)",
      "d": "2020-03-03",
      "m1": "0.4927 \u00b1 0.0061",
      "m2": "No",
      "m3": "0.4989 \u00b1 0.0047",
      "m4": "21173389"
    },
    {
      "p": "[GraphSAINT: Graph Sampling Based Inductive Learning Method](https://arxiv.org/abs/1907.04931v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/graphsaint)",
      "n": "GraphSAINT (R-GCN aggr)",
      "d": "2019-07-10",
      "m1": "0.4751 \u00b1 0.0022",
      "m2": "No",
      "m3": "0.4837 \u00b1 0.0026",
      "m4": "154366772"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "R-GCN+FLAG",
      "d": "2020-10-19",
      "m1": "0.4737 \u00b1 0.0048",
      "m2": "No",
      "m3": "0.4835 \u00b1 0.0036",
      "m4": "154366772"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "NeighborSampling (R-GCN aggr)",
      "d": "2017-06-07",
      "m1": "0.4678 \u00b1 0.0067",
      "m2": "No",
      "m3": "0.4761 \u00b1 0.0068",
      "m4": "154366772"
    },
    {
      "p": "[SIGN: Scalable Inception Graph Neural Networks](https://arxiv.org/abs/2004.11198v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/sign)",
      "n": "SIGN",
      "d": "2020-04-23",
      "m1": "0.4046 \u00b1 0.0012",
      "m2": "No",
      "m3": "0.4068 \u00b1 0.0010",
      "m4": "3724645"
    },
    {
      "p": "[Modeling Relational Data with Graph Convolutional Networks](http://arxiv.org/abs/1703.06103v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/tensorflow/rgcn)",
      "n": "Full-batch R-GCN",
      "d": "2017-03-17",
      "m1": "0.3977 \u00b1 0.0046",
      "m2": "No",
      "m3": "0.4084 \u00b1 0.0041",
      "m4": "154366772"
    },
    {
      "p": "[Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks](https://arxiv.org/abs/1905.07953v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "ClusterGCN (R-GCN aggr)",
      "d": "2019-05-20",
      "m1": "0.3732 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.3840 \u00b1 0.0031",
      "m4": "154366772"
    },
    {
      "p": "[metapath2vec: Scalable Representation Learning for Heterogeneous Networks](https://dl.acm.org/doi/10.1145/3097983.3098036)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/metapath2vec)",
      "n": "MetaPath2vec",
      "d": "2017-08-01",
      "m1": "0.3544 \u00b1 0.0036",
      "m2": "No",
      "m3": "0.3506 \u00b1 0.0017",
      "m4": "94479069"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MetaPath2vec",
      "d": null,
      "m1": "0.3544 \u00b1 0.0036",
      "m2": "No",
      "m3": "0.3506 \u00b1 0.0017",
      "m4": "94479069"
    },
    {
      "p": "[Distilling Self-Knowledge From Contrastive Links to Classify Graph Nodes Without Passing Messages](https://arxiv.org/abs/2106.08541v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cf020031308/LinkDist/blob/master/ogbn.py)",
      "n": "CoLinkDistMLP",
      "d": "2021-06-16",
      "m1": "0.2761 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.2646 \u00b1 0.0013",
      "m4": "278202"
    },
    {
      "p": "[Open Graph Benchmark: Datasets for Machine Learning on Graphs](https://arxiv.org/abs/2005.00687v7)",
      "c": "[&check;&nbsp;Link](https://github.com/snap-stanford/ogb)",
      "n": "MLP",
      "d": "2020-05-02",
      "m1": "0.2692 \u00b1 0.0026",
      "m2": "No",
      "m3": "0.2626 \u00b1 0.0016",
      "m4": "188509"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
