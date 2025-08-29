# link-property-prediction-on-ogbl-ppa

[Dataset Link](https://ogb.stanford.edu/) \
Task Hierarchy: ['Link Property Prediction']

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
      "label": "Ext. data",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Test Hits@100",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Validation Hits@100",
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
      "p": "[Edge2Node: Reducing Edge Prediction to Node Classification](https://arxiv.org/abs/2311.02921v3)",
      "c": "",
      "n": "** E2N**",
      "d": "2023-11-06",
      "m1": "No",
      "m2": "0.8911 \u00b1 0.1266",
      "m3": "0.8857 \u00b1 0.1331",
      "m4": "526851"
    },
    {
      "p": "[Reconsidering the Performance of GAE in Link Prediction](https://arxiv.org/abs/2411.03845v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GraphPKU/Refined-GAE)",
      "n": "Refined-GAE",
      "d": "2024-11-06",
      "m1": "No",
      "m2": "0.7334 \u00b1 0.0092",
      "m3": "0.7391 \u00b1 0.0178",
      "m4": "295848449"
    },
    {
      "p": "[GraphGPT: Graph Learning with Generative Pre-trained Transformers](https://arxiv.org/abs/2401.00529v1)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba/graph-gpt)",
      "n": "GraphGPT(SMTP)",
      "d": "2023-12-31",
      "m1": "No",
      "m2": "0.6876 \u00b1 0.0067",
      "m3": "0.7017 \u00b1 0.0044",
      "m4": "145263360"
    },
    {
      "p": "[Pure Message Passing Can Estimate Common Neighbor for Link Prediction](https://arxiv.org/abs/2309.00976v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Barcavin/efficient-node-labelling)",
      "n": "MPLP",
      "d": "2023-09-02",
      "m1": "No",
      "m2": "0.6524 \u00b1 0.0150",
      "m3": "0.6685 \u00b1 0.0073",
      "m4": "147794531"
    },
    {
      "p": "[Can GNNs Learn Link Heuristics? A Concise Review and Evaluation of Link Prediction Methods](https://arxiv.org/abs/2411.14711v1)",
      "c": "[&check;&nbsp;Link](https://github.com/astroming/GNNHE)",
      "n": "GCN (node embedding)",
      "d": "2024-11-22",
      "m1": "No",
      "m2": "0.6354 \u00b1 0.0121",
      "m3": "0.6524 \u00b1 0.0096",
      "m4": "148144898"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "SIEG",
      "d": null,
      "m1": "No",
      "m2": "0.6322 \u00b1 0.0174",
      "m3": "0.6533 \u00b1 0.0234",
      "m4": "1993965"
    },
    {
      "p": "[Neural Common Neighbor with Completion for Link Prediction](https://arxiv.org/abs/2302.00890v4)",
      "c": "[&check;&nbsp;Link](https://github.com/GraphPKU/NeuralCommonNeighbor)",
      "n": "**Neural Common Neighbor **",
      "d": "2023-02-02",
      "m1": "No",
      "m2": "0.6119 \u00b1 0.0085",
      "m3": "0.6021 \u00b1 0.0037",
      "m4": "33538"
    },
    {
      "p": "[Network In Graph Neural Network](https://arxiv.org/abs/2111.11638v1)",
      "c": "",
      "n": "NGNN + SEAL",
      "d": "2021-11-23",
      "m1": "No",
      "m2": "0.5971 \u00b1 0.0245",
      "m3": "0.5995 \u00b1 0.0205",
      "m4": "735426"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "SUREL+",
      "d": null,
      "m1": "No",
      "m2": "0.5432 \u00b1 0.0044",
      "m3": "0.5492 \u00b1 0.0112",
      "m4": "52802"
    },
    {
      "p": "[SUREL+: Moving from Walks to Sets for Scalable Subgraph-based Graph Representation Learning](https://arxiv.org/abs/2303.03379v3)",
      "c": "[&check;&nbsp;Link](https://github.com/Graph-COM/SUREL_Plus)",
      "n": "SUREL+",
      "d": "2023-03-06",
      "m1": "No",
      "m2": "0.5432 \u00b1 0.0044",
      "m3": "0.5492 \u00b1 0.0112",
      "m4": "52802"
    },
    {
      "p": "[Edge Proposal Sets for Link Prediction](https://arxiv.org/abs/2106.15810v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "RA+Edge Proposal Set",
      "d": "2021-06-30",
      "m1": "No",
      "m2": "0.5324 \u00b1 0.0000",
      "m3": "0.5142 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MLP+CN&RA&AA",
      "d": null,
      "m1": "No",
      "m2": "0.5062 \u00b1 0.0035",
      "m3": "0.4906 \u00b1 0.0029",
      "m4": "163330"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "BUDDY",
      "d": null,
      "m1": "No",
      "m2": "0.4934 \u00b1 0.0098",
      "m3": "0.4931 \u00b1 0.0025",
      "m4": "644"
    },
    {
      "p": "[Predicting Missing Links via Local Information](http://arxiv.org/abs/0901.0553v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fs302/EasyLink)",
      "n": "Resource Allocation",
      "d": "2009-01-05",
      "m1": "No",
      "m2": "0.4933 \u00b1 0.0000",
      "m3": "0.4722 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[Labeling Trick: A Theory of Using Graph Neural Networks for Multi-Node Representation Learning](https://arxiv.org/abs/2010.16103v5)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/seal)",
      "n": "SEAL",
      "d": "2020-10-30",
      "m1": "No",
      "m2": "0.4880 \u00b1 0.0316",
      "m3": "0.5125 \u00b1 0.0252",
      "m4": "709122"
    },
    {
      "p": "[Simplifying Subgraph Representation Learning for Scalable Link Prediction](https://arxiv.org/abs/2301.12562v4)",
      "c": "[&check;&nbsp;Link](https://github.com/venomouscyanide/s3grl)",
      "n": "S3GRL (PoS Plus)",
      "d": "2023-01-29",
      "m1": "No",
      "m2": "0.4242 \u00b1 0.0180",
      "m3": "0.6512 \u00b1 0.0109",
      "m4": "32270001"
    },
    {
      "p": "[Adaptive Graph Diffusion Networks](https://arxiv.org/abs/2012.15024v2)",
      "c": "[&check;&nbsp;Link](https://github.com/skepsun/SAGN_with_SLE)",
      "n": "AGDN",
      "d": "2020-12-30",
      "m1": "No",
      "m2": "0.4123 \u00b1 0.0159",
      "m3": "0.4332 \u00b1 0.0092",
      "m4": "36904259"
    },
    {
      "p": "[Network In Graph Neural Network](https://arxiv.org/abs/2111.11638v1)",
      "c": "",
      "n": "NGNN + GraphSAGE",
      "d": "2021-11-23",
      "m1": "No",
      "m2": "0.4005 \u00b1 0.0138",
      "m3": "0.4058 \u00b1 0.0123",
      "m4": "556033"
    },
    {
      "p": "[Network In Graph Neural Network](https://arxiv.org/abs/2111.11638v1)",
      "c": "",
      "n": "NGNN + GCN",
      "d": "2021-11-23",
      "m1": "No",
      "m2": "0.3683 \u00b1 0.0099",
      "m3": "0.3834 \u00b1 0.0082",
      "m4": "410113"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Adamic Adar",
      "d": null,
      "m1": "No",
      "m2": "0.3245 \u00b1 0.0000",
      "m3": "0.3268 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[Open Graph Benchmark: Datasets for Machine Learning on Graphs](https://arxiv.org/abs/2005.00687v7)",
      "c": "[&check;&nbsp;Link](https://github.com/snap-stanford/ogb)",
      "n": "Matrix Factorization",
      "d": "2020-05-02",
      "m1": "No",
      "m2": "0.3229 \u00b1 0.0094",
      "m3": "0.3228 \u00b1 0.0428",
      "m4": "147662849"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Common Neighbor",
      "d": null,
      "m1": "No",
      "m2": "0.2765 \u00b1 0.0000",
      "m3": "0.2823 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[DeepWalk: Online Learning of Social Representations](http://arxiv.org/abs/1403.6652v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleRec/tree/master/models/recall/deepwalk)",
      "n": "DeepWalk",
      "d": "2014-03-26",
      "m1": "No",
      "m2": "0.2302 \u00b1 0.0163",
      "m3": "Please tell us",
      "m4": "150138741"
    },
    {
      "p": "[node2vec: Scalable Feature Learning for Networks](http://arxiv.org/abs/1607.00653v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/node2vec)",
      "n": "Node2vec",
      "d": "2016-07-03",
      "m1": "No",
      "m2": "0.2226 \u00b1 0.0083",
      "m3": "0.2253 \u00b1 0.0088",
      "m4": "73878913"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN",
      "d": "2016-09-09",
      "m1": "No",
      "m2": "0.1867 \u00b1 0.0132",
      "m3": "0.1845 \u00b1 0.0140",
      "m4": "278529"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE",
      "d": "2017-06-07",
      "m1": "No",
      "m2": "0.1655 \u00b1 0.0240",
      "m3": "0.1724 \u00b1 0.0264",
      "m4": "424449"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
