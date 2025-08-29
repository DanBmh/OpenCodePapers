# graph-regression-on-zinc-full

[Dataset Link](http://zinc15.docking.org/) \
Task Hierarchy: ['Graph Regression']

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
      "label": "Test MAE",
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
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA + rings + NodeRWSE + EdgeRWSE",
      "d": "2024-02-16",
      "m1": "0.0109\u00b10.0002"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA + RWSE + CY2C (Edge set attention, Random Walk Structural Encoding, clique adjacency, tuned)",
      "d": "2024-02-16",
      "m1": "0.0122\u00b10.0004"
    },
    {
      "p": "[Topology-Informed Graph Transformer](https://arxiv.org/abs/2402.02005v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leemingo/tigt)",
      "n": "TIGT",
      "d": "2024-02-03",
      "m1": "0.014"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA + RWSE (Edge set attention, Random Walk Structural Encoding, tuned)",
      "d": "2024-02-16",
      "m1": "0.0154\u00b10.0001"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA + RWSE (Edge set attention, Random Walk Structural Encoding)",
      "d": "2024-02-16",
      "m1": "0.017\u00b10.001"
    },
    {
      "p": "[Graph Inductive Biases in Transformers without Message Passing](https://arxiv.org/abs/2305.17589v1)",
      "c": "[&check;&nbsp;Link](https://github.com/liamma/grit)",
      "n": "GRIT",
      "d": "2023-05-27",
      "m1": "0.023"
    },
    {
      "p": "[Recipe for a General, Powerful, Scalable Graph Transformer](https://arxiv.org/abs/2205.12454v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rampasek/GraphGPS)",
      "n": "GraphGPS",
      "d": "2022-05-25",
      "m1": "0.024\u00b10.007"
    },
    {
      "p": "[Sign and Basis Invariant Networks for Spectral Graph Representation Learning](https://arxiv.org/abs/2202.13013v4)",
      "c": "[&check;&nbsp;Link](https://github.com/cptq/SignNet-BasisNet)",
      "n": "SignNet",
      "d": "2022-02-25",
      "m1": "0.024\u00b10.003"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA (Edge set attention, no positional encodings)",
      "d": "2024-02-16",
      "m1": "0.027\u00b10.001"
    },
    {
      "p": "[Do Transformers Really Perform Bad for Graph Representation?](https://arxiv.org/abs/2106.05234v5)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/Graphormer)",
      "n": "Graphormer",
      "d": "2021-06-09",
      "m1": "0.036\u00b10.002"
    },
    {
      "p": "[Weisfeiler and Leman go sparse: Towards scalable higher-order graph embeddings](https://arxiv.org/abs/1904.01543v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chrsmrrs/sparsewl)",
      "n": "\u03b4-2-GNN",
      "d": "2019-04-02",
      "m1": "0.042\u00b10.003"
    },
    {
      "p": "[Weisfeiler and Leman go sparse: Towards scalable higher-order graph embeddings](https://arxiv.org/abs/1904.01543v3)",
      "c": "[&check;&nbsp;Link](https://github.com/chrsmrrs/sparsewl)",
      "n": "\u03b4-2-LGNN",
      "d": "2019-04-02",
      "m1": "0.045\u00b10.006"
    },
    {
      "p": "[Pure Transformers are Powerful Graph Learners](https://arxiv.org/abs/2207.02505v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jw9730/tokengt)",
      "n": "TokenGT",
      "d": "2022-07-06",
      "m1": "0.047\u00b10.010"
    },
    {
      "p": "[Principal Neighbourhood Aggregation for Graph Nets](https://arxiv.org/abs/2004.05718v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rusty1s/pytorch_geometric)",
      "n": "PNA",
      "d": "2020-04-12",
      "m1": "0.057\u00b10.007"
    },
    {
      "p": "[How Powerful are Graph Neural Networks?](http://arxiv.org/abs/1810.00826v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gin)",
      "n": "GIN",
      "d": "2018-10-01",
      "m1": "0.068\u00b10.004"
    },
    {
      "p": "[Graph Attention Networks](http://arxiv.org/abs/1710.10903v3)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "GAT",
      "d": "2017-10-30",
      "m1": "0.078\u00b10.006"
    },
    {
      "p": "[How Attentive are Graph Attention Networks?](https://arxiv.org/abs/2105.14491v3)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "GATv2",
      "d": "2021-05-30",
      "m1": "0.079\u00b10.004"
    },
    {
      "p": "[Inductive Representation Learning on Large Graphs](http://arxiv.org/abs/1706.02216v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pyg-team/pytorch_geometric/blob/master/torch_geometric/nn/models/basic_gnn.py)",
      "n": "GraphSAGE",
      "d": "2017-06-07",
      "m1": "0.126\u00b10.003"
    },
    {
      "p": "[Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907v4)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gcn)",
      "n": "GCN",
      "d": "2016-09-09",
      "m1": "0.152\u00b10.023"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
