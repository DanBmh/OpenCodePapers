# link-property-prediction-on-ogbl-collab

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
      "label": "Test Hits@50",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Ext. data",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Validation Hits@50",
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
      "n": "E2N",
      "d": "2023-11-06",
      "m1": "0.9515 \u00b1 0.1410",
      "m2": "No",
      "m3": "0.9546 \u00b1 0.1270",
      "m4": "526851"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HyperFusion",
      "d": null,
      "m1": "0.7129 \u00b1 0.0018",
      "m2": "No",
      "m3": "0.7385 \u00b1 0.0099",
      "m4": "1064446212"
    },
    {
      "p": "[GIDN: A Lightweight Graph Inception Diffusion Network for High-efficient Link Prediction](https://arxiv.org/abs/2210.01301v3)",
      "c": "",
      "n": "GIDN@YITU",
      "d": "2022-10-04",
      "m1": "0.7096 \u00b1 0.0055",
      "m2": "No",
      "m3": "0.9620 \u00b1 0.0040",
      "m4": "60449025"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "PLNLP + SIGN",
      "d": null,
      "m1": "0.7087 \u00b1 0.0033",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "34980864"
    },
    {
      "p": "[Pairwise Learning for Neural Link Prediction](https://arxiv.org/abs/2112.02936v6)",
      "c": "[&check;&nbsp;Link](https://github.com/zhitao-wang/PLNLP)",
      "n": "PLNLP (random walk aug.)",
      "d": "2021-12-06",
      "m1": "0.7059 \u00b1 0.0029",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "34980864"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HOP-REC",
      "d": null,
      "m1": "0.7012 \u00b1 0.0016",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "30191104"
    },
    {
      "p": "[Global Attention Improves Graph Networks Generalization](https://arxiv.org/abs/2006.07846v2)",
      "c": "[&check;&nbsp;Link](https://github.com/omri1348/LRGA)",
      "n": "PLNLP+ LRGA",
      "d": "2020-06-14",
      "m1": "0.6909 \u00b1 0.0055",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "35200656"
    },
    {
      "p": "[Pairwise Learning for Neural Link Prediction](https://arxiv.org/abs/2112.02936v6)",
      "c": "[&check;&nbsp;Link](https://github.com/zhitao-wang/PLNLP)",
      "n": "PLNLP (val as input)",
      "d": "2021-12-06",
      "m1": "0.6872 \u00b1 0.0052",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "35112192"
    },
    {
      "p": "[Reconsidering the Performance of GAE in Link Prediction](https://arxiv.org/abs/2411.03845v1)",
      "c": "[&check;&nbsp;Link](https://github.com/GraphPKU/Refined-GAE)",
      "n": "Refined-GAE",
      "d": "2024-11-06",
      "m1": "0.6816 \u00b1 0.0041",
      "m2": "No",
      "m3": "1.0000 \u00b1 0.0000",
      "m4": "126669825"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "TopoLink",
      "d": null,
      "m1": "0.6792 \u00b1 0.0074",
      "m2": "No",
      "m3": "0.6771 \u00b1 0.0083",
      "m4": "483363845"
    },
    {
      "p": "[Simplifying Subgraph Representation Learning for Scalable Link Prediction](https://arxiv.org/abs/2301.12562v4)",
      "c": "[&check;&nbsp;Link](https://github.com/venomouscyanide/s3grl)",
      "n": "S3GRL (PoS Plus)",
      "d": "2023-01-29",
      "m1": "0.6683 \u00b1 0.0030",
      "m2": "No",
      "m3": "0.9861 \u00b1 0.0006",
      "m4": "5913025"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ELPH",
      "d": null,
      "m1": "0.6636 \u00b1 0.5876",
      "m2": "No",
      "m3": "0.6631 \u00b1 0.0021",
      "m4": "3284065"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "BUDDY",
      "d": null,
      "m1": "0.6572 \u00b1 0.0053",
      "m2": "No",
      "m3": "0.6621 \u00b1 0.0016",
      "m4": "1184867"
    },
    {
      "p": "[Edge Proposal Sets for Link Prediction](https://arxiv.org/abs/2106.15810v1)",
      "c": "[&check;&nbsp;Link](https://github.com/sangyx/gtrick/tree/main/benchmark/pyg)",
      "n": "Adamic Adar+Edge Proposal Set",
      "d": "2021-06-30",
      "m1": "0.6548 \u00b1 0.0000",
      "m2": "No",
      "m3": "0.9735 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[Labeling Trick: A Theory of Using Graph Neural Networks for Multi-Node Representation Learning](https://arxiv.org/abs/2010.16103v5)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/seal)",
      "n": "SEAL-nofeat (val as input)",
      "d": "2020-10-30",
      "m1": "0.6474 \u00b1 0.0043",
      "m2": "No",
      "m3": "0.6495 \u00b1 0.0043",
      "m4": "501570"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Adamic Adar",
      "d": null,
      "m1": "0.6417 \u00b1 0.0000",
      "m2": "No",
      "m3": "0.6349 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Common Neighbor",
      "d": null,
      "m1": "0.6137 \u00b1 0.0000",
      "m2": "No",
      "m3": "0.6036 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[Labeling Trick: A Theory of Using Graph Neural Networks for Multi-Node Representation Learning](https://arxiv.org/abs/2010.16103v5)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/seal)",
      "n": "SEAL-nofeat",
      "d": "2020-10-30",
      "m1": "0.5471 \u00b1 0.0049",
      "m2": "No",
      "m3": "0.6495 \u00b1 0.0043",
      "m4": "501570"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE  (val as input)",
      "d": "2017-06-07",
      "m1": "0.5463 \u00b1 0.0112",
      "m2": "No",
      "m3": "0.5688 \u00b1 0.0077",
      "m4": "460289"
    },
    {
      "p": "[Network In Graph Neural Network](https://arxiv.org/abs/2111.11638v1)",
      "c": "",
      "n": "NGNN + GraphSAGE",
      "d": "2021-11-23",
      "m1": "0.5359 \u00b1 0.0056",
      "m2": "No",
      "m3": "0.6281 \u00b1 0.0046",
      "m4": "591873"
    },
    {
      "p": "[Network In Graph Neural Network](https://arxiv.org/abs/2111.11638v1)",
      "c": "",
      "n": "NGNN + GCN",
      "d": "2021-11-23",
      "m1": "0.5348 \u00b1 0.0040",
      "m2": "No",
      "m3": "0.6273 \u00b1 0.0040",
      "m4": "428033"
    },
    {
      "p": "[DeeperGCN: All You Need to Train Deeper GCNs](https://arxiv.org/abs/2006.07739v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/deepergcn)",
      "n": "DeeperGCN",
      "d": "2020-06-13",
      "m1": "0.5273 \u00b1 0.0047",
      "m2": "No",
      "m3": "0.6187 \u00b1 0.0045",
      "m4": "117383"
    },
    {
      "p": "[Global Attention Improves Graph Networks Generalization](https://arxiv.org/abs/2006.07846v2)",
      "c": "[&check;&nbsp;Link](https://github.com/omri1348/LRGA)",
      "n": "LRGA + GCN",
      "d": "2020-06-14",
      "m1": "0.5221 \u00b1 0.0072",
      "m2": "No",
      "m3": "0.6088 \u00b1 0.0059",
      "m4": "1069489"
    },
    {
      "p": "[On the effect of the average clustering coefficient on topology-based link prediction in featureless graphs](https://arxiv.org/abs/2501.06721v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rafiepour/ClusteringEffect)",
      "n": "Jaccard Index",
      "d": "2025-01-12",
      "m1": "0.5050 \u00b1 0.0000",
      "m2": "No",
      "m3": "0.6098 \u00b1 0.0000",
      "m4": "0"
    },
    {
      "p": "[DeepWalk: Online Learning of Social Representations](http://arxiv.org/abs/1403.6652v2)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleRec/tree/master/models/recall/deepwalk)",
      "n": "DeepWalk",
      "d": "2014-03-26",
      "m1": "0.5037 \u00b1 0.0034",
      "m2": "No",
      "m3": "Please tell us",
      "m4": "61390187"
    },
    {
      "p": "[node2vec: Scalable Feature Learning for Networks](http://arxiv.org/abs/1607.00653v1)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/node2vec)",
      "n": "Node2vec",
      "d": "2016-07-03",
      "m1": "0.4888 \u00b1 0.0054",
      "m2": "No",
      "m3": "0.5703 \u00b1 0.0052",
      "m4": "30322945"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE",
      "d": "2017-06-07",
      "m1": "0.4810 \u00b1 0.0081",
      "m2": "No",
      "m3": "0.5688 \u00b1 0.0077",
      "m4": "460289"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN (val as input)",
      "d": "2016-09-09",
      "m1": "0.4714 \u00b1 0.0145",
      "m2": "No",
      "m3": "0.5263 \u00b1 0.0115",
      "m4": "296449"
    },
    {
      "p": "[VQ-GNN: A Universal Framework to Scale up Graph Neural Networks using Vector Quantization](https://arxiv.org/abs/2110.14363v1)",
      "c": "[&check;&nbsp;Link](https://github.com/devnkong/VQ-GNN)",
      "n": "VQ-GNN (SAGE-Mean)",
      "d": "2021-10-27",
      "m1": "0.4673 \u00b1 0.0164 ."
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN",
      "d": "2016-09-09",
      "m1": "0.4475 \u00b1 0.0107",
      "m2": "No",
      "m3": "0.5263 \u00b1 0.0115",
      "m4": "296449"
    },
    {
      "p": "[VQ-GNN: A Universal Framework to Scale up Graph Neural Networks using Vector Quantization](https://arxiv.org/abs/2110.14363v1)",
      "c": "[&check;&nbsp;Link](https://github.com/devnkong/VQ-GNN)",
      "n": "VQ-GNN (GCN)",
      "d": "2021-10-27",
      "m1": "0.4316 \u00b1 0.0134"
    },
    {
      "p": "[VQ-GNN: A Universal Framework to Scale up Graph Neural Networks using Vector Quantization](https://arxiv.org/abs/2110.14363v1)",
      "c": "[&check;&nbsp;Link](https://github.com/devnkong/VQ-GNN)",
      "n": "VQ-GNN (GAT)",
      "d": "2021-10-27",
      "m1": "0.4102 \u00b1 0.0099"
    },
    {
      "p": "[Open Graph Benchmark: Datasets for Machine Learning on Graphs](https://arxiv.org/abs/2005.00687v7)",
      "c": "[&check;&nbsp;Link](https://github.com/snap-stanford/ogb)",
      "n": "Matrix Factorization",
      "d": "2020-05-02",
      "m1": "0.3886 \u00b1 0.0029",
      "m2": "No",
      "m3": "0.4896 \u00b1 0.0029",
      "m4": "60514049"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE (val as input)",
      "d": "2017-06-07",
      "m4": "460289"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
