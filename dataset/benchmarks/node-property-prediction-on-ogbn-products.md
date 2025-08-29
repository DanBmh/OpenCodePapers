# node-property-prediction-on-ogbn-products

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
      "p": "[Learning on Large-scale Text-attributed Graphs via Variational Inference](https://arxiv.org/abs/2210.14709v2)",
      "c": "[&check;&nbsp;Link](https://github.com/andyjzhao/glem)",
      "n": "GLEM+EnGCN",
      "d": "2022-10-26",
      "m1": "0.9014 \u00b1 0.0012",
      "m2": "Yes",
      "m3": "0.9370 \u00b1 0.0004",
      "m4": "139633805"
    },
    {
      "p": "[A Comprehensive Study on Large-Scale Graph Training: Benchmarking and Rethinking](https://arxiv.org/abs/2210.07494v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VITA-Group/Large_Scale_GCN_Benchmarking)",
      "n": "EnGCN",
      "d": "2022-10-14",
      "m1": "0.8798 \u00b1 0.0004",
      "m2": "No",
      "m3": "0.9241 \u00b1 0.0003",
      "m4": "653918"
    },
    {
      "p": "[Learning on Large-scale Text-attributed Graphs via Variational Inference](https://arxiv.org/abs/2210.14709v2)",
      "c": "[&check;&nbsp;Link](https://github.com/andyjzhao/glem)",
      "n": "GLEM+GIANT+SAGN+SCR",
      "d": "2022-10-26",
      "m1": "0.8737 \u00b1 0.0006",
      "m2": "Yes",
      "m3": "0.9400 \u00b1 0.0003",
      "m4": "139792525"
    },
    {
      "p": "[Label Deconvolution for Node Representation Learning on Large-scale Attributed Graphs against Learning Bias](https://arxiv.org/abs/2309.14907v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MIRALab-USTC/LD)",
      "n": "LD+GIANT+SAGN+SCR",
      "d": "2023-09-26",
      "m1": "0.8718 \u00b1 0.0004",
      "m2": "Yes",
      "m3": "0.9399 \u00b1 0.0002",
      "m4": "110636896"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "**GraDBERT+GIANT & SAGN+SLE+CnS **",
      "d": null,
      "m1": "0.8692 \u00b1 0.0007",
      "m2": "Yes",
      "m3": "0.9371 \u00b1 0.0003",
      "m4": "1154654"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GIANT-XRT+R-SAGN+SCR+C&S",
      "d": null,
      "m1": "0.8684 \u00b1 0.0005",
      "m2": "Yes",
      "m3": "0.9365 \u00b1 0.0003",
      "m4": "1154142"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GIANT-XRT+SAGN+SCR+C&S",
      "d": "2021-12-08",
      "m1": "0.8680 \u00b1 0.0007",
      "m2": "Yes",
      "m3": "0.9357 \u00b1 0.0004",
      "m4": "1154654"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GIANT-XRT+SAGN+MCR+C&S",
      "d": "2021-12-08",
      "m1": "0.8673 \u00b1 0.0008",
      "m2": "Yes",
      "m3": "0.9387 \u00b1 0.0002",
      "m4": "1154654"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GIANT-XRT+SAGN+SCR",
      "d": "2021-12-08",
      "m1": "0.8667 \u00b1 0.0009",
      "m2": "Yes",
      "m3": "0.9364 \u00b1 0.0005",
      "m4": "1154654"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GIANT-XRT+SAGN+MCR",
      "d": "2021-12-08",
      "m1": "0.8651 \u00b1 0.0009",
      "m2": "Yes",
      "m3": "0.9389 \u00b1 0.0002",
      "m4": "1154654"
    },
    {
      "p": "[Label Deconvolution for Node Representation Learning on Large-scale Attributed Graphs against Learning Bias](https://arxiv.org/abs/2309.14907v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MIRALab-USTC/LD)",
      "n": "LD+GAMLP",
      "d": "2023-09-26",
      "m1": "0.8645 \u00b1 0.0012",
      "m2": "Yes",
      "m3": "0.9415 \u00b1 0.0003",
      "m4": "144331677"
    },
    {
      "p": "[Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction](https://arxiv.org/abs/2111.00064v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/pecos)",
      "n": "GIANT-XRT+SAGN+SLE+C&S (use raw text)",
      "d": "2021-10-29",
      "m1": "0.8643 \u00b1 0.0020",
      "m2": "Yes",
      "m3": "0.9352 \u00b1 0.0005",
      "m4": "1548382"
    },
    {
      "p": "[Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction](https://arxiv.org/abs/2111.00064v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/pecos)",
      "n": "GIANT-XRT+SAGN+SLE (use raw text)",
      "d": "2021-10-29",
      "m1": "0.8622 \u00b1 0.0022",
      "m2": "Yes",
      "m3": "0.9363 \u00b1 0.0005",
      "m4": "1548382"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GIANT-XRT+GAMLP+MCR",
      "d": "2021-12-08",
      "m1": "0.8591 \u00b1 0.0008",
      "m2": "Yes",
      "m3": "0.9402 \u00b1 0.0004",
      "m4": "2144151"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GAMLP+RLU+SCR+C&S",
      "d": "2021-12-08",
      "m1": "0.8520 \u00b1 0.0008",
      "m2": "No",
      "m3": "0.9304 \u00b1 0.0005",
      "m4": "3335831"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GAMLP+RLU+SCR",
      "d": "2021-12-08",
      "m1": "0.8505 \u00b1 0.0009",
      "m2": "No",
      "m3": "0.9292 \u00b1 0.0005",
      "m4": "3335831"
    },
    {
      "p": "[Scalable and Adaptive Graph Neural Networks with Self-Label-Enhanced training](https://arxiv.org/abs/2104.09376v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "SAGN+SLE (4 stages)+C&S",
      "d": "2021-04-19",
      "m1": "0.8485 \u00b1 0.0010",
      "m2": "No",
      "m3": "0.9302 \u00b1 0.0003",
      "m4": "2179678"
    },
    {
      "p": "[Scalable and Adaptive Graph Neural Networks with Self-Label-Enhanced training](https://arxiv.org/abs/2104.09376v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "SAGN+SLE (4 stages)",
      "d": "2021-04-19",
      "m1": "0.8468 \u00b1 0.0012",
      "m2": "No",
      "m3": "0.9309 \u00b1 0.0007",
      "m4": "2179678"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "GAMLP+MCR",
      "d": "2021-12-08",
      "m1": "0.8462 \u00b1 0.0003",
      "m2": "No",
      "m3": "0.9319 \u00b1 0.0003",
      "m4": "3335831"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GAMLP+RLU",
      "d": null,
      "m1": "0.8459 \u00b1 0.0010",
      "m2": "No",
      "m3": "0.9324 \u00b1 0.0005",
      "m4": "3335831"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "Spec-MLP-Wide + C&S",
      "d": "2020-10-27",
      "m1": "0.8451 \u00b1 0.0006",
      "m2": "No",
      "m3": "0.9132 \u00b1 0.0010",
      "m4": "406063"
    },
    {
      "p": "[SCR: Training Graph Neural Networks with Consistency Regularization](https://arxiv.org/abs/2112.04319v2)",
      "c": "[&check;&nbsp;Link](https://github.com/THUDM/SCR)",
      "n": "SAGN+MCR",
      "d": "2021-12-08",
      "m1": "0.8441 \u00b1 0.0005",
      "m2": "No",
      "m3": "0.9325 \u00b1 0.0004",
      "m4": "2179678"
    },
    {
      "p": "[Scalable and Adaptive Graph Neural Networks with Self-Label-Enhanced training](https://arxiv.org/abs/2104.09376v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "SAGN+SLE",
      "d": "2021-04-19",
      "m1": "0.8428 \u00b1 0.0014",
      "m2": "No",
      "m3": "0.9287 \u00b1 0.0003",
      "m4": "2179678"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "MLP + C&S",
      "d": "2020-10-27",
      "m1": "0.8418 \u00b1 0.0007",
      "m2": "No",
      "m3": "0.9147 \u00b1 0.0009",
      "m4": "96247"
    },
    {
      "p": "[Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction](https://arxiv.org/abs/2111.00064v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/pecos)",
      "n": "GIANT-XRT+GraphSAINT(use raw text)",
      "d": "2021-10-29",
      "m1": "0.8415 \u00b1 0.0022",
      "m2": "Yes",
      "m3": "0.9318 \u00b1 0.0004",
      "m4": "417583"
    },
    {
      "p": "[Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification](https://arxiv.org/abs/2406.08993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LUOyk1999/tunedGNN)",
      "n": "GraphSAGE",
      "d": "2024-06-13",
      "m1": "0.8389 \u00b1 0.0036",
      "m2": "No",
      "m3": "0.9242 \u00b1 0.0029",
      "m4": "433047"
    },
    {
      "p": "[Polynormer: Polynomial-Expressive Graph Transformer in Linear Time](https://arxiv.org/abs/2403.01232v3)",
      "c": "[&check;&nbsp;Link](https://github.com/cornell-zhang/Polynormer/tree/master/large_graph_exp)",
      "n": "Polynormer",
      "d": "2024-03-02",
      "m1": "0.8382 \u00b1 0.0011",
      "m2": "No",
      "m3": "0.9239 \u00b1 0.0005",
      "m4": "2383654"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GAMLP",
      "d": null,
      "m1": "0.8354 \u00b1 0.0009",
      "m2": "No",
      "m3": "0.9312 \u00b1 0.0003",
      "m4": "3335831"
    },
    {
      "p": "[Adaptive Graph Diffusion Networks](https://arxiv.org/abs/2012.15024v2)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "AGDN",
      "d": "2020-12-30",
      "m1": "0.8334 \u00b1 0.0027",
      "m2": "No",
      "m3": "0.9229 \u00b1 0.0010",
      "m4": "1544047"
    },
    {
      "p": "[Training Graph Neural Networks with 1000 Layers](https://arxiv.org/abs/2106.07476v3)",
      "c": "[&check;&nbsp;Link](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb_eff/ogbn_arxiv_dgl)",
      "n": "RevGNN-112",
      "d": "2021-06-14",
      "m1": "0.8307 \u00b1 0.0030",
      "m2": "No",
      "m3": "0.9290 \u00b1 0.0007",
      "m4": "2945007"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "Linear + C&S",
      "d": "2020-10-27",
      "m1": "0.8301 \u00b1 0.0001",
      "m2": "No",
      "m3": "0.9134 \u00b1 0.0001",
      "m4": "10763"
    },
    {
      "p": "[Masked Label Prediction: Unified Message Passing Model for Semi-Supervised Classification](https://arxiv.org/abs/2009.03509v5)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp)",
      "n": "UniMP",
      "d": "2020-09-08",
      "m1": "0.8256 \u00b1 0.0031",
      "m2": "No",
      "m3": "0.9308 \u00b1 0.0017",
      "m4": "1475605"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "Plain Linear + C&S",
      "d": "2020-10-27",
      "m1": "0.8254 \u00b1 0.0003",
      "m2": "No",
      "m3": "0.9103 \u00b1 0.0001",
      "m4": "4747"
    },
    {
      "p": "[Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification](https://arxiv.org/abs/2406.08993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/LUOyk1999/tunedGNN)",
      "n": "GCN",
      "d": "2024-06-13",
      "m1": "0.8233 \u00b1 0.0019",
      "m2": "No",
      "m3": "0.9224 \u00b1 0.0036",
      "m4": "233047"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "DeeperGCN+FLAG",
      "d": "2020-10-19",
      "m1": "0.8193 \u00b1 0.0031",
      "m2": "No",
      "m3": "0.9221 \u00b1 0.0037",
      "m4": "253743"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GAT+FLAG",
      "d": "2020-10-19",
      "m1": "0.8176 \u00b1 0.0045",
      "m2": "No",
      "m3": "0.9251 \u00b1 0.0006",
      "m4": "751574"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE + C&S + node2vec",
      "d": "2017-06-07",
      "m1": "0.8154 \u00b1 0.0050",
      "m2": "No",
      "m3": "0.9238 \u00b1 0.0006",
      "m4": "103983"
    },
    {
      "p": "[Scalable and Adaptive Graph Neural Networks with Self-Label-Enhanced training](https://arxiv.org/abs/2104.09376v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "SAGN",
      "d": "2021-04-19",
      "m1": "0.8120 \u00b1 0.0007",
      "m2": "No",
      "m3": "0.9309 \u00b1 0.0004",
      "m4": "2233391"
    },
    {
      "p": "[Dimensionality Reduction Meets Message Passing for Graph Node Embeddings](https://arxiv.org/abs/2202.00408v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ksadowski13/PCAPass)",
      "n": "PCAPass + XGBoost",
      "d": "2022-02-01",
      "m1": "0.8115 \u00b1 0.0002",
      "m2": "No",
      "m3": "0.9200 \u00b1 0.0005",
      "m4": "0"
    },
    {
      "p": "[DeeperGCN: All You Need to Train Deeper GCNs](https://arxiv.org/abs/2006.07739v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/deepergcn)",
      "n": "DeeperGCN",
      "d": "2020-06-13",
      "m1": "0.8098 \u00b1 0.0020",
      "m2": "No",
      "m3": "0.9238 \u00b1 0.0009",
      "m4": "253743"
    },
    {
      "p": "[E2EG: End-to-End Node Classification Using Graph Topology and Text-based Node Attributes](https://arxiv.org/abs/2208.04609v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tuanh23/e2eg)",
      "n": "E2EG (use raw text)",
      "d": "2022-08-09",
      "m1": "0.8098 \u00b1 0.0040",
      "m2": "Yes",
      "m3": "0.9234 \u00b1 0.0009",
      "m4": "66793520"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "GAT w/NS + C&S",
      "d": "2020-10-27",
      "m1": "0.8092 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.9263 \u00b1 0.0008",
      "m4": "753622"
    },
    {
      "p": "[SIGN: Scalable Inception Graph Neural Networks](https://arxiv.org/abs/2004.11198v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/sign)",
      "n": "SIGN",
      "d": "2020-04-23",
      "m1": "0.8052 \u00b1 0.0016",
      "m2": "No",
      "m3": "0.9299 \u00b1 0.0004",
      "m4": "3483703"
    },
    {
      "p": "[Node Feature Extraction by Self-Supervised Multi-scale Neighborhood Prediction](https://arxiv.org/abs/2111.00064v3)",
      "c": "[&check;&nbsp;Link](https://github.com/amzn/pecos)",
      "n": "GIANT-XRT+MLP (use raw text)",
      "d": "2021-10-29",
      "m1": "0.8049 \u00b1 0.0028",
      "m2": "Yes",
      "m3": "0.9210 \u00b1 0.0009",
      "m4": "275759"
    },
    {
      "p": "[Combining Label Propagation and Simple Models Out-performs Graph Neural Networks](https://arxiv.org/abs/2010.13993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/correct_and_smooth)",
      "n": "GraphSAGE w/NS + C&S",
      "d": "2020-10-27",
      "m1": "0.8041 \u00b1 0.0022",
      "m2": "No",
      "m3": "0.9238 \u00b1 0.0007",
      "m4": "207919"
    },
    {
      "p": "[GraphSAINT: Graph Sampling Based Inductive Learning Method](https://arxiv.org/abs/1907.04931v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/graphsaint)",
      "n": "GraphSAINT-inductive",
      "d": "2019-07-10",
      "m1": "0.8027 \u00b1 0.0026",
      "m2": "No",
      "m3": "Please tell us",
      "m4": "331661"
    },
    {
      "p": "[Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks](https://arxiv.org/abs/1905.07953v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "ClusterGCN+residual+3 layers",
      "d": "2019-05-20",
      "m1": "0.7971 \u00b1 0.0042",
      "m2": "No",
      "m3": "0.9188 \u00b1 0.0008",
      "m4": "456034"
    },
    {
      "p": "[Graph Attention Networks](http://arxiv.org/abs/1710.10903v3)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "GAT with NeighborSampling",
      "d": "2017-10-30",
      "m1": "0.7945 \u00b1 0.0059",
      "m2": "No",
      "m3": "Please tell us",
      "m4": "751574"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GraphSAGE+FLAG",
      "d": "2020-10-19",
      "m1": "0.7936 \u00b1 0.0057",
      "m2": "No",
      "m3": "0.9205 \u00b1 0.0007",
      "m4": "206895"
    },
    {
      "p": "[Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks](https://arxiv.org/abs/1905.07953v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "Cluster-GAT",
      "d": "2019-05-20",
      "m1": "0.7923 \u00b1 0.0078",
      "m2": "No",
      "m3": "0.8985 \u00b1 0.0022",
      "m4": "1540848"
    },
    {
      "p": "[GraphSAINT: Graph Sampling Based Inductive Learning Method](https://arxiv.org/abs/1907.04931v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/graphsaint)",
      "n": "GraphSAINT (SAGE aggr)",
      "d": "2019-07-10",
      "m1": "0.7908 \u00b1 0.0024",
      "m2": "No",
      "m3": "0.9162 \u00b1 0.0008",
      "m4": "206895"
    },
    {
      "p": "[Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph Convolutional Networks](https://arxiv.org/abs/1905.07953v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research)",
      "n": "ClusterGCN (SAGE aggr)",
      "d": "2019-05-20",
      "m1": "0.7897 \u00b1 0.0033",
      "m2": "No",
      "m3": "0.9212 \u00b1 0.0009",
      "m4": "206895"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "NeighborSampling (SAGE aggr)",
      "d": "2017-06-07",
      "m1": "0.7870 \u00b1 0.0036",
      "m2": "No",
      "m3": "0.9170 \u00b1 0.0009",
      "m4": "206895"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "Full-batch GraphSAGE",
      "d": "2017-06-07",
      "m1": "0.7850 \u00b1 0.0014",
      "m2": "No",
      "m3": "0.9224 \u00b1 0.0007",
      "m4": "206895"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE",
      "d": "2017-06-07",
      "m1": "0.7829 \u00b1 0.0016",
      "m2": "No",
      "m3": "Please tell us",
      "m4": "Please tell us"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "TCNN",
      "d": null,
      "m1": "0.7606 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.8991 \u00b1 0.0011",
      "m4": "22624"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "Full-batch GCN",
      "d": "2016-09-09",
      "m1": "0.7564 \u00b1 0.0021",
      "m2": "No",
      "m3": "0.9200 \u00b1 0.0003",
      "m4": "103727"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Label Propagation",
      "d": null,
      "m1": "0.7434 \u00b1 0.0000",
      "m2": "No",
      "m3": "0.9091 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GraphZoom (Node2vec)",
      "d": null,
      "m1": "0.7406 \u00b1 0.0026",
      "m2": "No",
      "m3": "0.9066 \u00b1 0.0011",
      "m4": "120251183"
    },
    {
      "p": "[node2vec: Scalable Feature Learning for Networks](http://arxiv.org/abs/1607.00653v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/node2vec)",
      "n": "Node2vec",
      "d": "2016-07-03",
      "m1": "0.7249 \u00b1 0.0010",
      "m2": "No",
      "m3": "0.9032 \u00b1 0.0006",
      "m4": "313612207"
    },
    {
      "p": "[Graph-less Neural Networks: Teaching Old MLPs New Tricks via Distillation](https://arxiv.org/abs/2110.08727v2)",
      "c": "[&check;&nbsp;Link](https://github.com/snap-research/graphless-neural-networks)",
      "n": "GLNN",
      "d": "2021-10-17",
      "m1": "0.6886 \u00b1 0.0046"
    },
    {
      "p": "[Distilling Self-Knowledge From Contrastive Links to Classify Graph Nodes Without Passing Messages](https://arxiv.org/abs/2106.08541v1)",
      "c": "[&check;&nbsp;Link](https://github.com/cf020031308/LinkDist/blob/master/ogbn.py)",
      "n": "CoLinkDistMLP",
      "d": "2021-06-16",
      "m1": "0.6259 \u00b1 0.0010",
      "m2": "No",
      "m3": "0.7721 \u00b1 0.0015",
      "m4": "115806"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "MLP+FLAG",
      "d": "2020-10-19",
      "m1": "0.6241 \u00b1 0.0016",
      "m2": "No",
      "m3": "0.7688 \u00b1 0.0014",
      "m4": "103727"
    },
    {
      "p": "[Open Graph Benchmark: Datasets for Machine Learning on Graphs](https://arxiv.org/abs/2005.00687v7)",
      "c": "[&check;&nbsp;Link](https://github.com/snap-stanford/ogb)",
      "n": "MLP",
      "d": "2020-05-02",
      "m1": "0.6106 \u00b1 0.0008",
      "m2": "No",
      "m3": "0.7554 \u00b1 0.0014",
      "m4": "103727"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
