# sleep-stage-detection-on-sleep-edf

[Dataset Link](https://www.physionet.org/content/sleep-edfx/1.0.0/) \
Task Hierarchy: ['Sleep Stage Detection']

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
      "label": "Accuracy",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Cohen's kappa",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Macro-F1",
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
      "p": "[SleePyCo: Automatic Sleep Scoring with Feature Pyramid and Contrastive Learning](https://arxiv.org/abs/2209.09452v1)",
      "c": "[&check;&nbsp;Link](https://github.com/gist-ailab/sleepyco)",
      "n": "SleePyCo (Fpz-Cz only)",
      "d": "2022-09-20",
      "m1": "86.8%",
      "m2": "0.820",
      "m3": "0.812"
    },
    {
      "p": "[Do Not Sleep on Traditional Machine Learning: Simple and Interpretable Techniques Are Competitive to Deep Learning for Sleep Scoring](https://arxiv.org/abs/2207.07753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/predict-idlab/sleep-linear)",
      "n": "CatBoost",
      "d": "2022-07-15",
      "m1": "86.6%",
      "m2": "0.816",
      "m3": "0.810"
    },
    {
      "p": "[XSleepNet: Multi-View Sequential Model for Automatic Sleep Staging](https://arxiv.org/abs/2007.05492v4)",
      "c": "[&check;&nbsp;Link](https://github.com/pquochuy/xsleepnet)",
      "n": "XSleepNet (EEG, EOG)",
      "d": "2020-07-08",
      "m1": "86.4%",
      "m2": "0.813",
      "m3": "0.809"
    },
    {
      "p": "[Do Not Sleep on Traditional Machine Learning: Simple and Interpretable Techniques Are Competitive to Deep Learning for Sleep Scoring](https://arxiv.org/abs/2207.07753v3)",
      "c": "[&check;&nbsp;Link](https://github.com/predict-idlab/sleep-linear)",
      "n": "Linear model",
      "d": "2022-07-15",
      "m1": "86.3%",
      "m2": "0.813",
      "m3": "0.805"
    },
    {
      "p": "[Intra- and Inter-epoch Temporal Context Network (IITNet) Using Sub-epoch Features for Automatic Sleep Scoring on Raw Single-channel EEG](https://arxiv.org/abs/1902.06562v2)",
      "c": "[&check;&nbsp;Link](https://github.com/gist-ailab/IITNet-official)",
      "n": "IITNet CRNN (Fpz-Cz only)",
      "d": "2019-02-18",
      "m1": "84.0%"
    },
    {
      "p": "[DeepSleepNet: a Model for Automatic Sleep Stage Scoring based on Raw Single-Channel EEG](http://arxiv.org/abs/1703.04046v2)",
      "c": "[&check;&nbsp;Link](https://github.com/akaraspt/deepsleepnet)",
      "n": "DeepSleepNet",
      "d": "2017-03-12",
      "m1": "82%",
      "m2": "0.76",
      "m3": "0.769"
    },
    {
      "p": "[Joint Classification and Prediction CNN Framework for Automatic Sleep Stage Classification](http://arxiv.org/abs/1805.06546v3)",
      "c": "[&check;&nbsp;Link](https://github.com/pquochuy/MultitaskSleepNet)",
      "n": "Multitask 1-max CNN",
      "d": "2018-05-16",
      "m1": "81.9%"
    },
    {
      "p": "[Deep Convolutional Neural Networks for Interpretable Analysis of EEG Sleep Stage Scoring](http://arxiv.org/abs/1710.00633v1)",
      "c": "",
      "n": "Deep CNN with\ntransfer-learning",
      "d": "2017-10-02",
      "m1": "81.3%"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
