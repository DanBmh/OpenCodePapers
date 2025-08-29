# graph-property-prediction-on-ogbg-molpcba

[Dataset Link](https://ogb.stanford.edu/) \
Task Hierarchy: ['Graph Property Prediction']

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
      "label": "Test AP",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Ext. data",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Validation AP",
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
      "n": "HyperFusino",
      "d": null,
      "m1": "0.3204 \u00b1 0.0001",
      "m2": "No",
      "m3": "0.3353 \u00b1 0.0002",
      "m4": "10887085"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HyperFusion",
      "d": null,
      "m1": "0.3204 \u00b1 0.0001",
      "m2": "No",
      "m3": "0.3353 \u00b1 0.0002",
      "m4": "10887085"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HIG(pre-trained on PCQM4M)",
      "d": null,
      "m1": "0.3167 \u00b1 0.0034",
      "m2": "Yes",
      "m3": "0.3252 \u00b1 0.0043",
      "m4": "119529665"
    },
    {
      "p": "[Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph Learning with Triplet Graph Transformers](https://arxiv.org/abs/2402.04538v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shamim-hussain/egt_pytorch)",
      "n": "TGT-Ag+TGT-At-DP",
      "d": "2024-02-07",
      "m1": "0.3167 \u00b1 0.0031",
      "m2": "Yes",
      "m4": "47000000"
    },
    {
      "p": "[Do Transformers Really Perform Bad for Graph Representation?](https://arxiv.org/abs/2106.05234v5)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/Graphormer)",
      "n": "Graphormer",
      "d": "2021-06-09",
      "m1": "0.3140 \u00b1 0.0032",
      "m3": "0.3227 \u00b1 0.0024",
      "m4": "119529664"
    },
    {
      "p": "[Do Transformers Really Perform Bad for Graph Representation?](https://arxiv.org/abs/2106.05234v5)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/Graphormer)",
      "n": "Graphormer (pre-trained on PCQM4M)",
      "d": "2021-06-09",
      "m1": "0.3140 \u00b1 0.0032",
      "m2": "Yes",
      "m3": "0.3227 \u00b1 0.0024",
      "m4": "119529664"
    },
    {
      "p": "[Next Level Message-Passing with Hierarchical Support Graphs](https://arxiv.org/abs/2406.15852v2)",
      "c": "[&check;&nbsp;Link](https://github.com/carlosinator/support-graphs)",
      "n": "GatedGCN-HSG",
      "d": "2024-06-22",
      "m1": "0.3129\u00b10.0020"
    },
    {
      "p": "[Towards Better Graph Representation Learning with Parameterized Decomposition & Filtering](https://arxiv.org/abs/2305.06102v1)",
      "c": "[&check;&nbsp;Link](https://github.com/qslim/PDF)",
      "n": "PDF",
      "d": "2023-05-10",
      "m1": "0.3031 \u00b1 0.0026",
      "m2": "No",
      "m3": "0.3115 \u00b1 0.0020",
      "m4": "3842048"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "PAS",
      "d": null,
      "m1": "0.3012 \u00b1 0.0039",
      "m2": "No",
      "m3": "0.3151 \u00b1 0.0047",
      "m4": "5560960"
    },
    {
      "p": "[Nested Graph Neural Networks](https://arxiv.org/abs/2110.13197v1)",
      "c": "[&check;&nbsp;Link](https://github.com/muhanzhang/NestedGNN)",
      "n": "Nested GIN+virtual node (ensemble)",
      "d": "2021-10-25",
      "m1": "0.3007 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.3059 \u00b1 0.0056",
      "m4": "44187480"
    },
    {
      "p": "[Nested Graph Neural Networks](https://arxiv.org/abs/2110.13197v1)",
      "c": "[&check;&nbsp;Link](https://github.com/muhanzhang/NestedGNN)",
      "n": "Nested GIN+virtual node (ens)",
      "d": "2021-10-25",
      "m1": "0.3007 \u00b1 0.0037",
      "m3": "0.3059 \u00b1 0.0056"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "GINE+bot",
      "d": null,
      "m1": "0.2994 \u00b1 0.0019",
      "m2": "No",
      "m3": "0.3094 \u00b1 0.0023",
      "m4": "5511680"
    },
    {
      "p": "[Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message Passing](https://arxiv.org/abs/2102.08786v3)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/CRaWl)",
      "n": "CRaWl",
      "d": "2021-02-17",
      "m1": "0.2986 \u00b1 0.0025",
      "m2": "No",
      "m3": "0.3075 \u00b1 0.0020",
      "m4": "6115728"
    },
    {
      "p": "[Unlocking the Potential of Classic GNNs for Graph-level Tasks: Simple Architectures Meet Excellence](https://arxiv.org/abs/2502.09263v1)",
      "c": "[&check;&nbsp;Link](https://github.com/LUOyk1999/GNNPlus)",
      "n": "GatedGCN+",
      "d": "2025-02-13",
      "m1": "0.2981 \u00b1 0.0024",
      "m2": "No",
      "m3": "0.3011 \u00b1 0.0037",
      "m4": "6016860"
    },
    {
      "p": "[Graph convolutions that can finally model local structure](https://arxiv.org/abs/2011.15069v2)",
      "c": "[&check;&nbsp;Link](https://github.com/RBrossard/GINEPLUS)",
      "n": "GINE+ w/ APPNP",
      "d": "2020-11-30",
      "m1": "0.2979 \u00b1 0.0030",
      "m2": "No",
      "m3": "0.3126 \u00b1 0.0023",
      "m4": "6147029"
    },
    {
      "p": "[Global Self-Attention as a Replacement for Graph Convolution](https://arxiv.org/abs/2108.03348v3)",
      "c": "[&check;&nbsp;Link](https://github.com/shamim-hussain/egt_pytorch)",
      "n": "EGT",
      "d": "2021-08-07",
      "m1": "0.2961 \u00b1 0.0024"
    },
    {
      "p": "[Parameterized Hypercomplex Graph Neural Networks for Graph Classification](https://arxiv.org/abs/2103.16584v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bayer-science-for-a-better-life/phc-gnn)",
      "n": "PHC-GNN",
      "d": "2021-03-30",
      "m1": "0.2947 \u00b1 0.0026",
      "m2": "No",
      "m3": "0.3068 \u00b1 0.0025",
      "m4": "1690328"
    },
    {
      "p": "[From Stars to Subgraphs: Uplifting Any GNN with Local Structure Awareness](https://arxiv.org/abs/2110.03753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/GNNAsKernel/GNNAsKernel)",
      "n": "GIN-AK",
      "d": "2021-10-07",
      "m1": "0.2930 \u00b1 0.0044",
      "m2": "No",
      "m3": "0.3047 \u00b1 0.0007",
      "m4": "3081029"
    },
    {
      "p": "[Graph convolutions that can finally model local structure](https://arxiv.org/abs/2011.15069v2)",
      "c": "[&check;&nbsp;Link](https://github.com/RBrossard/GINEPLUS)",
      "n": "GINE+ w/ virtual nodes",
      "d": "2020-11-30",
      "m1": "0.2917 \u00b1 0.0015",
      "m2": "No",
      "m3": "0.3065 \u00b1 0.0030",
      "m4": "6147029"
    },
    {
      "p": "[Recipe for a General, Powerful, Scalable Graph Transformer](https://arxiv.org/abs/2205.12454v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rampasek/GraphGPS)",
      "n": "GPS",
      "d": "2022-05-25",
      "m1": "0.2907",
      "m2": "No",
      "m3": "0.3015 \u00b1 0.0038",
      "m4": "9744496"
    },
    {
      "p": "[Directional Graph Networks](https://arxiv.org/abs/2010.02863v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Saro00/DGN)",
      "n": "DGN",
      "d": "2020-10-06",
      "m1": "0.2885 \u00b1 0.0030",
      "m2": "No",
      "m3": "0.2970 \u00b1 0.0021",
      "m4": "6732696"
    },
    {
      "p": "[RAN-GNNs: breaking the capacity limits of graph neural networks](https://arxiv.org/abs/2103.15565v1)",
      "c": "",
      "n": "RandomGIN-vn+FLAG",
      "d": "2021-03-29",
      "m1": "0.2881 \u00b1 0.0028",
      "m2": "No",
      "m3": "0.3035 \u00b1 0.0047",
      "m4": "5572026"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "DeeperGCN+virtual node+FLAG",
      "d": "2020-10-19",
      "m1": "0.2842 \u00b1 0.0043",
      "m2": "No",
      "m3": "0.2952 \u00b1 0.0029",
      "m4": "5550208"
    },
    {
      "p": "[Principal Neighbourhood Aggregation for Graph Nets](https://arxiv.org/abs/2004.05718v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rusty1s/pytorch_geometric)",
      "n": "PNA",
      "d": "2020-04-12",
      "m1": "0.2838 \u00b1 0.0035",
      "m2": "No",
      "m3": "0.2926 \u00b1 0.0026",
      "m4": "6550839"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GIN+virtual node+FLAG",
      "d": "2020-10-19",
      "m1": "0.2834 \u00b1 0.0038",
      "m2": "No",
      "m3": "0.2912 \u00b1 0.0026",
      "m4": "3374533"
    },
    {
      "p": "[Nested Graph Neural Networks](https://arxiv.org/abs/2110.13197v1)",
      "c": "[&check;&nbsp;Link](https://github.com/muhanzhang/NestedGNN)",
      "n": "Nested GIN+virtual node",
      "d": "2021-10-25",
      "m1": "0.2832 \u00b1 0.0041",
      "m3": "0.2915 \u00b1 0.0035"
    },
    {
      "p": "[DeeperGCN: All You Need to Train Deeper GCNs](https://arxiv.org/abs/2006.07739v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/deepergcn)",
      "n": "DeeperGCN+virtual node",
      "d": "2020-06-13",
      "m1": "0.2781 \u00b1 0.0038",
      "m2": "No",
      "m3": "0.2920 \u00b1 0.0025",
      "m4": "5550208"
    },
    {
      "p": "[How Powerful are Graph Neural Networks?](http://arxiv.org/abs/1810.00826v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gin)",
      "n": "GIN+virtual node",
      "d": "2018-10-01",
      "m1": "0.2703 \u00b1 0.0023",
      "m2": "No",
      "m3": "0.2798 \u00b1 0.0025",
      "m4": "3374533"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GCN+virtual node+FLAG",
      "d": "2020-10-19",
      "m1": "0.2483 \u00b1 0.0037",
      "m2": "No",
      "m3": "0.2556 \u00b1 0.0040",
      "m4": "2017028"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN+virtual node",
      "d": "2016-09-09",
      "m1": "0.2424 \u00b1 0.0034",
      "m2": "No",
      "m3": "0.2495 \u00b1 0.0042",
      "m4": "2017028"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GIN+FLAG",
      "d": "2020-10-19",
      "m1": "0.2395 \u00b1 0.0040",
      "m2": "No",
      "m3": "0.2451 \u00b1 0.0042",
      "m4": "1923433"
    },
    {
      "p": "[Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering](http://arxiv.org/abs/1606.09375v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mdeff/cnn_graph)",
      "n": "ChebNet",
      "d": "2016-06-30",
      "m1": "0.2306 \u00b1 0.0016",
      "m2": "No",
      "m3": "0.2372 \u00b1 0.0018",
      "m4": "1475003"
    },
    {
      "p": "[How Powerful are Graph Neural Networks?](http://arxiv.org/abs/1810.00826v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gin)",
      "n": "GIN",
      "d": "2018-10-01",
      "m1": "0.2266 \u00b1 0.0028",
      "m2": "No",
      "m3": "0.2305 \u00b1 0.0027",
      "m4": "1923433"
    },
    {
      "p": "[Robust Optimization as Data Augmentation for Large-scale Graphs](https://arxiv.org/abs/2010.09891v3)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "GCN+FLAG",
      "d": "2020-10-19",
      "m1": "0.2116 \u00b1 0.0017",
      "m2": "No",
      "m3": "0.2150 \u00b1 0.0022",
      "m4": "565928"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MorganFP+Rand. Forest",
      "d": null,
      "m1": "0.2054 \u00b1 0.0004",
      "m2": "No",
      "m3": "0.2226 \u00b1 0.0002",
      "m4": "29440000"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN",
      "d": "2016-09-09",
      "m1": "0.2020 \u00b1 0.0024",
      "m2": "No",
      "m3": "0.2059 \u00b1 0.0033",
      "m4": "565928"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
