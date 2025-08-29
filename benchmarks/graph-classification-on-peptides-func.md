# graph-classification-on-peptides-func

[Dataset Link](http://github.com/vijaydwivedi75/lrgb) \
Task Hierarchy: ['Classification', 'Graph Classification']

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
      "label": "AP",
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
      "n": "ESA + RWSE (Edge set attention, Random Walk Structural Encoding, + validation set)",
      "d": "2024-02-16",
      "m1": "0.7479"
    },
    {
      "p": "[Molecular Fingerprints Are Strong Models for Peptide Function Prediction](https://arxiv.org/abs/2501.17901v1)",
      "c": "[&check;&nbsp;Link](https://github.com/arch4ngel21/scikit-fingerprints)",
      "n": "ECFP + LightGBM",
      "d": "2025-01-29",
      "m1": "0.7460"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA + RWSE (Edge set attention, Random Walk Structural Encoding, tuned)",
      "d": "2024-02-16",
      "m1": "0.7357\u00b10.0036"
    },
    {
      "p": "[Molecular Fingerprints Are Strong Models for Peptide Function Prediction](https://arxiv.org/abs/2501.17901v1)",
      "c": "[&check;&nbsp;Link](https://github.com/arch4ngel21/scikit-fingerprints)",
      "n": "TT + LightGBM",
      "d": "2025-01-29",
      "m1": "0.7318"
    },
    {
      "p": "[Spatio-Spectral Graph Neural Networks](https://arxiv.org/abs/2405.19121v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sigeisler/s2gnn)",
      "n": "S\u00b2GCN",
      "d": "2024-05-29",
      "m1": "0.7311\u00b10.0066"
    },
    {
      "p": "[Molecular Fingerprints Are Strong Models for Peptide Function Prediction](https://arxiv.org/abs/2501.17901v1)",
      "c": "[&check;&nbsp;Link](https://github.com/arch4ngel21/scikit-fingerprints)",
      "n": "RDKit + LightGBM",
      "d": "2025-01-29",
      "m1": "0.7311"
    },
    {
      "p": "[Unlocking the Potential of Classic GNNs for Graph-level Tasks: Simple Architectures Meet Excellence](https://arxiv.org/abs/2502.09263v1)",
      "c": "[&check;&nbsp;Link](https://github.com/LUOyk1999/GNNPlus)",
      "n": "GCN+",
      "d": "2025-02-13",
      "m1": "0.7261 \u00b1 0.0067"
    },
    {
      "p": "[Enhancing Graph Transformers with Hierarchical Distance Structural Encoding](https://arxiv.org/abs/2308.11129v4)",
      "c": "[&check;&nbsp;Link](https://github.com/luoyk1999/hdse)",
      "n": "GraphGPS + HDSE",
      "d": "2023-08-22",
      "m1": "0.7156\u00b10.0058"
    },
    {
      "p": "[DRew: Dynamically Rewired Message Passing with Delay](https://arxiv.org/abs/2305.08018v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bengutteridge/drew)",
      "n": "DRew-GCN+LapPE",
      "d": "2023-05-13",
      "m1": "0.7150\u00b10.0044"
    },
    {
      "p": "[Recurrent Distance Filtering for Graph Representation Learning](https://arxiv.org/abs/2312.01538v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skeletondyh/gred)",
      "n": "GRED+LapPE",
      "d": "2023-12-03",
      "m1": "0.7133\u00b10.0011"
    },
    {
      "p": "[Learning Long Range Dependencies on Graphs via Random Walks](https://arxiv.org/abs/2406.03386v2)",
      "c": "[&check;&nbsp;Link](https://github.com/borgwardtlab/neuralwalker)",
      "n": "NeuralWalker",
      "d": "2024-06-05",
      "m1": "0.7096 \u00b1 0.0078"
    },
    {
      "p": "[Recurrent Distance Filtering for Graph Representation Learning](https://arxiv.org/abs/2312.01538v3)",
      "c": "[&check;&nbsp;Link](https://github.com/skeletondyh/gred)",
      "n": "GRED",
      "d": "2023-12-03",
      "m1": "0.7085\u00b10.0027"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA (Edge set attention, no positional encodings, tuned)",
      "d": "2024-02-16",
      "m1": "0.7071\u00b10.0015"
    },
    {
      "p": "[Graph Inductive Biases in Transformers without Message Passing](https://arxiv.org/abs/2305.17589v1)",
      "c": "[&check;&nbsp;Link](https://github.com/liamma/grit)",
      "n": "GRIT",
      "d": "2023-05-27",
      "m1": "0.6988\u00b10.0082"
    },
    {
      "p": "[CKGConv: General Graph Convolution with Continuous Kernels](https://arxiv.org/abs/2404.13604v2)",
      "c": "[&check;&nbsp;Link](https://github.com/networkslab/ckgconv)",
      "n": "CKGCN",
      "d": "2024-04-21",
      "m1": "0.6952"
    },
    {
      "p": "[A Generalization of ViT/MLP-Mixer to Graphs](https://arxiv.org/abs/2212.13350v2)",
      "c": "[&check;&nbsp;Link](https://github.com/XiaoxinHe/Graph-ViT-MLPMixer)",
      "n": "Graph ViT",
      "d": "2022-12-27",
      "m1": "0.6942\u00b10.0075"
    },
    {
      "p": "[A Generalization of ViT/MLP-Mixer to Graphs](https://arxiv.org/abs/2212.13350v2)",
      "c": "[&check;&nbsp;Link](https://github.com/XiaoxinHe/Graph-ViT-MLPMixer)",
      "n": "GraphMLPMixer",
      "d": "2022-12-27",
      "m1": "0.6921\u00b10.0054"
    },
    {
      "p": "[Next Level Message-Passing with Hierarchical Support Graphs](https://arxiv.org/abs/2406.15852v2)",
      "c": "[&check;&nbsp;Link](https://github.com/carlosinator/support-graphs)",
      "n": "GatedGCN-HSG",
      "d": "2024-06-22",
      "m1": "0.6866\u00b10.0038"
    },
    {
      "p": "[An end-to-end attention-based approach for learning on graphs](https://arxiv.org/abs/2402.10793v2)",
      "c": "[&check;&nbsp;Link](https://github.com/davidbuterez/edge-set-attention)",
      "n": "ESA (Edge set attention, no positional encodings, not tuned)",
      "d": "2024-02-16",
      "m1": "0.6863\u00b10.0044"
    },
    {
      "p": "[Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](https://arxiv.org/abs/2309.00367v2)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/lrgb)",
      "n": "GCN-tuned",
      "d": "2023-09-01",
      "m1": "0.6860\u00b10.0050"
    },
    {
      "p": "[Multiresolution Graph Transformers and Wavelet Positional Encoding for Learning Hierarchical Structures](https://arxiv.org/abs/2302.08647v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "MGT+WavePE",
      "d": "2023-02-17",
      "m1": "0.6817\u00b10.0064"
    },
    {
      "p": "[Path Neural Networks: Expressive and Accurate Graph Neural Networks](https://arxiv.org/abs/2306.05955v1)",
      "c": "[&check;&nbsp;Link](https://github.com/gasmichel/pathnns_expressive)",
      "n": "PathNN",
      "d": "2023-06-09",
      "m1": "0.6816\u00b10.0026"
    },
    {
      "p": "[Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](https://arxiv.org/abs/2309.00367v2)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/lrgb)",
      "n": "GatedGCN-tuned",
      "d": "2023-09-01",
      "m1": "0.6765\u00b10.0047"
    },
    {
      "p": "[On the Connection Between MPNN and Graph Transformer](https://arxiv.org/abs/2301.11956v4)",
      "c": "[&check;&nbsp;Link](https://github.com/chen-cai-osu/mpnn-gt-connection)",
      "n": "GatedGCN+RWSE+virtual node",
      "d": "2023-01-27",
      "m1": "0.6685\u00b10.0062"
    },
    {
      "p": "[Topology-Informed Graph Transformer](https://arxiv.org/abs/2402.02005v1)",
      "c": "[&check;&nbsp;Link](https://github.com/leemingo/tigt)",
      "n": "TIGT",
      "d": "2024-02-03",
      "m1": "0.6679"
    },
    {
      "p": "[Diffusing Graph Attention](https://arxiv.org/abs/2303.00613v1)",
      "c": "",
      "n": "Graph Diffuser",
      "d": "2023-03-01",
      "m1": "0.6651\u00b10.0010"
    },
    {
      "p": "[Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](https://arxiv.org/abs/2309.00367v2)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/lrgb)",
      "n": "GINE-tuned",
      "d": "2023-09-01",
      "m1": "0.6621\u00b10.0067"
    },
    {
      "p": "[Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance](https://arxiv.org/abs/2306.02866v3)",
      "c": "[&check;&nbsp;Link](https://github.com/jw9730/lps)",
      "n": "ViT-PS",
      "d": "2023-06-05",
      "m1": "0.6575"
    },
    {
      "p": "[CIN++: Enhancing Topological Message Passing](https://arxiv.org/abs/2306.03561v1)",
      "c": "[&check;&nbsp;Link](https://github.com/twitter-research/cwn)",
      "n": "CIN++-500k",
      "d": "2023-06-06",
      "m1": "0.6569\u00b10.0117"
    },
    {
      "p": "[Recipe for a General, Powerful, Scalable Graph Transformer](https://arxiv.org/abs/2205.12454v4)",
      "c": "[&check;&nbsp;Link](https://github.com/rampasek/GraphGPS)",
      "n": "GPS",
      "d": "2022-05-25",
      "m1": "0.6535\u00b10.0041"
    },
    {
      "p": "[Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark](https://arxiv.org/abs/2309.00367v2)",
      "c": "[&check;&nbsp;Link](https://github.com/toenshoff/lrgb)",
      "n": "GPS-tuned",
      "d": "2023-09-01",
      "m1": "0.6534\u00b10.0091"
    },
    {
      "p": "[Exphormer: Sparse Transformers for Graphs](https://arxiv.org/abs/2303.06147v2)",
      "c": "[&check;&nbsp;Link](https://github.com/hamed1375/exphormer)",
      "n": "Exphormer",
      "d": "2023-03-10",
      "m1": "0.6527\u00b10.0043"
    },
    {
      "p": "[Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for Molecular Graph Classification](https://ebooks.iospress.nl/doi/10.3233/FAIA240663)",
      "c": "[&check;&nbsp;Link](https://github.com/j-adamczyk/MOLTOP)",
      "n": "MOLTOP",
      "d": "2024-10-17",
      "m1": "0.6459 \u00b1 0.0005"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "SAN+RWSE",
      "d": "2022-06-16",
      "m1": "0.6439\u00b10.0075"
    },
    {
      "p": "[Graph Transformers without Positional Encodings](https://arxiv.org/abs/2401.17791v3)",
      "c": "",
      "n": "EIGENFORMER",
      "d": "2024-01-31",
      "m1": "0.6414"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "SAN+LapPE",
      "d": "2022-06-16",
      "m1": "0.6384\u00b10.0121"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "Transformer+LapPE",
      "d": "2022-06-16",
      "m1": "0.6326\u00b10.0126"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "GatedGCN+RWSE",
      "d": "2022-06-16",
      "m1": "0.6069\u00b10.0035"
    },
    {
      "p": "[How Powerful are Graph Neural Networks?](http://arxiv.org/abs/1810.00826v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/mxnet/gin)",
      "n": "GIN",
      "d": "2018-10-01",
      "m1": "0.6043\u00b10.0216"
    },
    {
      "p": "[PANDA: Expanded Width-Aware Message Passing Beyond Rewiring](https://arxiv.org/abs/2406.03671v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jeongwhanchoi/panda)",
      "n": "GCN + PANDA",
      "d": "2024-06-06",
      "m1": "0.6028\u00b10.0031"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "GCN",
      "d": "2022-06-16",
      "m1": "0.5930\u00b10.0023"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "GatedGCN",
      "d": "2022-06-16",
      "m1": "0.5864\u00b10.0077"
    },
    {
      "p": "[Simple and Deep Graph Convolutional Networks](https://arxiv.org/abs/2007.02133v1)",
      "c": "[&check;&nbsp;Link](https://github.com/chennnM/GCNII/tree/master/PyG/ogbn-arxiv)",
      "n": "GCNII",
      "d": "2020-07-04",
      "m1": "0.5543\u00b10.0078"
    },
    {
      "p": "[Long Range Graph Benchmark](https://arxiv.org/abs/2206.08164v4)",
      "c": "[&check;&nbsp;Link](https://github.com/vijaydwivedi75/lrgb)",
      "n": "GINE",
      "d": "2022-06-16",
      "m1": "0.5498\u00b10.0079"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
