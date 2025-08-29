# medical-code-prediction-on-mimic-iii

[Dataset Link](https://mimic.physionet.org/) \
Task Hierarchy: ['Multi-Label Classification', 'Medical Code Prediction']

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
      "label": "Micro-F1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Macro-F1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Micro-AUC",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Macro-AUC",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "Precision@5",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "Precision@8",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "Precision@15",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "mAP",
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
      "p": "[A General Knowledge Injection Framework for ICD Coding](https://arxiv.org/abs/2505.18708v1)",
      "c": "[&check;&nbsp;Link](https://github.com/xuzhang0112/GKI-ICD)",
      "n": "GKI-ICD",
      "d": "2025-05-24",
      "m1": "61.2",
      "m2": "12.3",
      "m3": "99.3",
      "m4": "96.2",
      "m6": "77.7",
      "m7": "62.4",
      "m8": "66.1"
    },
    {
      "p": "[An Unsupervised Approach to Achieve Supervised-Level Explainability in Healthcare Records](https://arxiv.org/abs/2406.08958v2)",
      "c": "[&check;&nbsp;Link](https://github.com/joakimedin/medical-coding-reproducibility)",
      "n": "PLM-CA",
      "d": "2024-06-13",
      "m1": "60.0",
      "m2": "24.7",
      "m8": "64.7"
    },
    {
      "p": "[Knowledge Injected Prompt Based Fine-tuning for Multi-label Few-shot ICD Coding](https://arxiv.org/abs/2210.03304v2)",
      "c": "[&check;&nbsp;Link](https://github.com/whaleloops/KEPT)",
      "n": "MSMN+KEPTLongformer",
      "d": "2022-10-07",
      "m1": "59.9",
      "m2": "11.8",
      "m6": "77.1",
      "m7": "61.5"
    },
    {
      "p": "[Effective Convolutional Attention Network for Multi-label Clinical Document Classification](https://aclanthology.org/2021.emnlp-main.481)",
      "c": "",
      "n": "EffectiveCAN",
      "d": null,
      "m1": "58.9",
      "m2": "10.6",
      "m3": "98.8",
      "m4": "91.5",
      "m6": "75.8",
      "m7": "60.6"
    },
    {
      "p": "[Automatic ICD Coding Exploiting Discourse Structure and Reconciled Code Embeddings](https://aclanthology.org/2022.coling-1.254)",
      "c": "[&check;&nbsp;Link](https://github.com/discnet2022/discnet)",
      "n": "Discnet+RE",
      "d": null,
      "m1": "58.8",
      "m2": "14.0",
      "m3": "99.3",
      "m4": "95.6",
      "m6": "76.5",
      "m7": "61.4"
    },
    {
      "p": "[Read, Attend, and Code: Pushing the Limits of Medical Codes Prediction from Clinical Notes by Machines](https://arxiv.org/abs/2107.10650v1)",
      "c": "",
      "n": "RAC",
      "d": "2021-07-10",
      "m1": "58.6",
      "m2": "12.7",
      "m3": "99.2",
      "m4": "94.8",
      "m5": "82.9",
      "m6": "75.4",
      "m7": "60.1"
    },
    {
      "p": "[Code Synonyms Do Matter: Multiple Synonyms Matching Network for Automatic ICD Coding](https://arxiv.org/abs/2203.01515v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ganjinzero/icd-msmn)",
      "n": "MSMN",
      "d": "2022-03-03",
      "m1": "58.4",
      "m2": "10.3",
      "m3": "99.2",
      "m4": "95.0",
      "m6": "75.2",
      "m7": "59.9"
    },
    {
      "p": "[A Label Attention Model for ICD Coding from Clinical Text](https://arxiv.org/abs/2007.06351v1)",
      "c": "[&check;&nbsp;Link](https://github.com/joakimedin/medical-coding-reproducibility)",
      "n": "JointLAAT",
      "d": "2020-07-13",
      "m1": "57.5",
      "m2": "10.7",
      "m3": "98.8",
      "m4": "92.1",
      "m5": "80.6",
      "m6": "73.5",
      "m7": "59.0"
    },
    {
      "p": "[A Label Attention Model for ICD Coding from Clinical Text](https://arxiv.org/abs/2007.06351v1)",
      "c": "[&check;&nbsp;Link](https://github.com/joakimedin/medical-coding-reproducibility)",
      "n": "LAAT",
      "d": "2020-07-13",
      "m1": "57.5",
      "m2": "9.9",
      "m3": "98.8",
      "m4": "91.9",
      "m5": "81.3",
      "m6": "73.8",
      "m7": "59.1"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "MSATT-KG",
      "d": null,
      "m1": "55.3",
      "m2": "9.0",
      "m3": "99.2",
      "m4": "91.0",
      "m6": "72.8",
      "m7": "58.1"
    },
    {
      "p": "[ICD Coding from Clinical Text Using Multi-Filter Residual Convolutional Neural Network](https://arxiv.org/abs/1912.00862v1)",
      "c": "[&check;&nbsp;Link](https://github.com/joakimedin/medical-coding-reproducibility)",
      "n": "MultiResCNN",
      "d": "2019-11-25",
      "m1": "55.2",
      "m2": "8.5",
      "m3": "98.6",
      "m4": "91.0",
      "m6": "73.4",
      "m7": "58.4"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "CAML",
      "d": "2018-02-15",
      "m1": "53.9",
      "m2": "8.8",
      "m3": "98.6",
      "m4": "89.5",
      "m6": "70.9",
      "m7": "56.1"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "DR-CAML",
      "d": "2018-02-15",
      "m1": "52.9",
      "m2": "8.6",
      "m3": "98.5",
      "m4": "89.7",
      "m6": "69.0",
      "m7": "54.8"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "SVM",
      "d": "2018-02-15",
      "m1": "44.1"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "CNN",
      "d": "2018-02-15",
      "m1": "41.9",
      "m2": "4.2",
      "m3": "96.9",
      "m4": "80.6",
      "m6": "58.1",
      "m7": "44.3"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "Bi-GRU",
      "d": "2018-02-15",
      "m1": "41.7",
      "m2": "3.8",
      "m3": "97.1",
      "m4": "82.2",
      "m6": "58.5",
      "m7": "44.5"
    },
    {
      "p": "[Explainable Automated Coding of Clinical Notes using Hierarchical Label-wise Attention Networks and Label Embedding Initialisation](https://arxiv.org/abs/2010.15728v4)",
      "c": "[&check;&nbsp;Link](https://github.com/acadTags/Explainable-Automated-Medical-Coding)",
      "n": "HAN",
      "d": "2020-10-29",
      "m1": "40.7",
      "m2": "3.6",
      "m3": "98.1",
      "m4": "88.5",
      "m6": "61.4"
    },
    {
      "p": "[Explainable Prediction of Medical Codes from Clinical Text](http://arxiv.org/abs/1802.05695v2)",
      "c": "[&check;&nbsp;Link](https://github.com/jamesmullenbach/caml-mimic)",
      "n": "Logistic Regression",
      "d": "2018-02-15",
      "m1": "27.2",
      "m2": "1.1",
      "m3": "93.7",
      "m4": "56.1",
      "m6": "54.2",
      "m7": "41.1"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
