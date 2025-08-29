# graph-regression-on-zinc

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
      "label": "MAE",
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
      "m1": "0.051"
    },
    {
      "p": "[Self-Attention in Colors: Another Take on Encoding Graph Structure in Transformers](https://arxiv.org/abs/2304.10933v1)",
      "c": "[&check;&nbsp;Link](https://github.com/inria-thoth/csa)",
      "n": "CSA",
      "d": "2023-04-21",
      "m1": "0.056"
    },
    {
      "p": "[Topology-Informed Graph Transformer](https://arxiv.org/abs/2402.02005v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leemingo/tigt)",
      "n": "TIGT",
      "d": "2024-02-03",
      "m1": "0.057"
    },
    {
      "p": "[Graph Inductive Biases in Transformers without Message Passing](https://arxiv.org/abs/2305.17589v1)",
      "c": "[&check;&nbsp;Link](https://github.com/liamma/grit)",
      "n": "GRIT",
      "d": "2023-05-27",
      "m1": "0.059"
    },
    {
      "p": "[Extending the Design Space of Graph Neural Networks by Rethinking Folklore Weisfeiler-Lehman](https://arxiv.org/abs/2306.03266v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jiaruifeng/n2gnn)",
      "n": "N2-GNN",
      "d": "2023-06-05",
      "m1": "0.059"
    },
    {
      "p": "[CKGConv: General Graph Convolution with Continuous Kernels](https://arxiv.org/abs/2404.13604v2)",
      "c": "[&check;&nbsp;Link](https://github.com/networkslab/ckgconv)",
      "n": "CKGCN",
      "d": "2024-04-21",
      "m1": "0.059"
    },
    {
      "p": "[Learning Long Range Dependencies on Graphs via Random Walks](https://arxiv.org/abs/2406.03386v2)",
      "c": "[&check;&nbsp;Link](https://github.com/borgwardtlab/neuralwalker)",
      "n": "NeuralWalker",
      "d": "2024-06-05",
      "m1": "0.065 \u00b1 0.001"
    },
    {
      "p": "[Towards Better Graph Representation Learning with Parameterized Decomposition & Filtering](https://arxiv.org/abs/2305.06102v1)",
      "c": "[&check;&nbsp;Link](https://github.com/qslim/PDF)",
      "n": "PDF",
      "d": "2023-05-10",
      "m1": "0.066 \u00b1 0.002"
    },
    {
      "p": "[Recipe for a General, Powerful, Scalable Graph Transformer](https://arxiv.org/abs/2205.12454v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rampasek/GraphGPS)",
      "n": "GPS",
      "d": "2022-05-25",
      "m1": "0.070 \u00b1 0.002"
    },
    {
      "p": "[Recipe for a General, Powerful, Scalable Graph Transformer](https://arxiv.org/abs/2205.12454v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rampasek/GraphGPS)",
      "n": "GINE",
      "d": "2022-05-25",
      "m1": "0.070 \u00b1 0.004"
    },
    {
      "p": "[Substructure Aware Graph Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/26318)",
      "c": "[&check;&nbsp;Link](https://github.com/BlackHalo-Drake/SAGNN-Substructure-Aware-Graph-Neural-Networks)",
      "n": "SAGNN",
      "d": "2023-06-26",
      "m1": "0.072\u00b10.002"
    },
    {
      "p": "[CIN++: Enhancing Topological Message Passing](https://arxiv.org/abs/2306.03561v1)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN++",
      "d": "2023-06-06",
      "m1": "0.074"
    },
    {
      "p": "[A Generalization of ViT/MLP-Mixer to Graphs](https://arxiv.org/abs/2212.13350v2)",
      "c": "[&check;&nbsp;Link](https://github.com/XiaoxinHe/Graph-ViT-MLPMixer)",
      "n": "GraphMLPMixer",
      "d": "2022-12-27",
      "m1": "0.075 \u00b1 0.001"
    },
    {
      "p": "[CIN++: Enhancing Topological Message Passing](https://arxiv.org/abs/2306.03561v1)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN++-500k",
      "d": "2023-06-06",
      "m1": "0.077"
    },
    {
      "p": "[Graph Transformers without Positional Encodings](https://arxiv.org/abs/2401.17791v3)",
      "c": "",
      "n": "EIGENFORMER",
      "d": "2024-01-31",
      "m1": "0.077"
    },
    {
      "p": "[Weisfeiler and Lehman Go Cellular: CW Networks](https://arxiv.org/abs/2106.12575v3)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN",
      "d": "2021-06-23",
      "m1": "0.079"
    },
    {
      "p": "[Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message Passing](https://arxiv.org/abs/2102.08786v3)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/CRaWl)",
      "n": "CRaWl+VN",
      "d": "2021-02-17",
      "m1": "0.088"
    },
    {
      "p": "[CIN++: Enhancing Topological Message Passing](https://arxiv.org/abs/2306.03561v1)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN++-small",
      "d": "2023-06-06",
      "m1": "0.091"
    },
    {
      "p": "[Weisfeiler and Lehman Go Cellular: CW Networks](https://arxiv.org/abs/2106.12575v3)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN-small",
      "d": "2021-06-23",
      "m1": "0.094"
    },
    {
      "p": "[Weisfeiler and Lehman Go Paths: Learning Topological Features via Path Complexes](https://arxiv.org/abs/2308.06838v6)",
      "c": "",
      "n": "PIN",
      "d": "2023-08-13",
      "m1": "0.096"
    },
    {
      "p": "[Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message Passing](https://arxiv.org/abs/2102.08786v3)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/CRaWl)",
      "n": "CRaWl",
      "d": "2021-02-17",
      "m1": "0.101"
    },
    {
      "p": "[Principal Neighbourhood Aggregation for Graph Nets](https://arxiv.org/abs/2004.05718v5)",
      "c": "[&check;&nbsp;Link](https://github.com/rusty1s/pytorch_geometric)",
      "n": "PNA",
      "d": "2020-04-12",
      "m1": "0.142"
    },
    {
      "p": "[Multi-Mask Aggregators for Graph Neural Networks](https://openreview.net/forum?id=hZ3b8CskgC)",
      "c": "[&check;&nbsp;Link](https://github.com/asarigun/mma)",
      "n": "MMA",
      "d": "2022-11-24",
      "m1": "0.156"
    },
    {
      "p": "[From Primes to Paths: Enabling Fast Multi-Relational Graph Analysis](https://arxiv.org/abs/2411.11149v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kbogas/PAM_BoP)",
      "n": "BoP",
      "d": "2024-11-17",
      "m1": "0.297"
    },
    {
      "p": "[An Experimental Study of the Transferability of Spectral Graph Networks](https://arxiv.org/abs/2012.10258v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Axeln78/Transferability-of-spectral-gnns)",
      "n": "ChebNet",
      "d": "2020-12-18",
      "m1": "0.360"
    },
    {
      "p": "[Factorizable Graph Convolutional Networks](https://arxiv.org/abs/2010.05421v1)",
      "c": "[&check;&nbsp;Link](https://github.com/ihollywhy/FactorGCN.PyTorch)",
      "n": "FactorGCN",
      "d": "2020-10-12",
      "m1": "0.366"
    },
    {
      "p": "[Graph-level Representation Learning with Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2309.16014v3)",
      "c": "[&check;&nbsp;Link](https://github.com/geriskenderi/graph-jepa)",
      "n": "Graph-JEPA",
      "d": "2023-09-27",
      "m1": "0.434"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
