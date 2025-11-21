# semantic-similarity-on-sick

[Dataset Link](http://marcobaroni.org/composes/sick.html) \
Task Hierarchy: ['Language Modelling', 'Sentence Pair Modeling', 'Semantic Similarity']

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
      "label": "MSE",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Pearson Correlation",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Spearman Correlation",
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
      "p": "[Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](http://arxiv.org/abs/1503.00075v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/tree_lstm)",
      "n": "Dependency Tree-LSTM (Tai et al., 2015)",
      "d": "2015-02-28",
      "m1": "0.2532",
      "m2": "0.8676",
      "m3": "0.8083"
    },
    {
      "p": "[Skip-Thought Vectors](http://arxiv.org/abs/1506.06726v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/InferSent)",
      "n": "combine-skip (Kiros et al., 2015)",
      "d": "2015-06-22",
      "m1": "0.2687",
      "m2": "0.8584",
      "m3": "0.7916"
    },
    {
      "p": "[Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](http://arxiv.org/abs/1503.00075v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/tree_lstm)",
      "n": "Bidirectional LSTM (Tai et al., 2015)",
      "d": "2015-02-28",
      "m1": "0.2736",
      "m2": "0.8567",
      "m3": "0.7966"
    },
    {
      "p": "[Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](http://arxiv.org/abs/1503.00075v3)",
      "c": "[&check;&nbsp;Link](https://github.com/dmlc/dgl/tree/master/examples/pytorch/tree_lstm)",
      "n": "LSTM (Tai et al., 2015)",
      "d": "2015-02-28",
      "m1": "0.2831",
      "m2": "0.8528",
      "m3": "0.7911"
    },
    {
      "p": "[Efficient Vector Representation for Documents through Corruption](http://arxiv.org/abs/1707.02377v1)",
      "c": "[&check;&nbsp;Link](https://github.com/mchen24/iclr2017)",
      "n": "Doc2VecC",
      "d": "2017-07-08",
      "m1": "0.3053",
      "m2": "0.8381",
      "m3": "0.7621"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
