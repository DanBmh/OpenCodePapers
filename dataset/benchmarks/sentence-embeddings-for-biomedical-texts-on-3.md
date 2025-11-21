# sentence-embeddings-for-biomedical-texts-on-3

[Dataset Link]() \
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
      "label": "F1",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Precision",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "Recall",
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
      "p": "[Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations](https://www.sciencedirect.com/science/article/pii/S2590177X19300575)",
      "c": "",
      "n": "BioBERT\n(pre-trained on PubMed abstracts + PMC, fine-tuned on \"Annotated corpus for semantic similarity of clinical trial outcomes, original corpus\")",
      "d": "2019-10-17",
      "m1": "89.75",
      "m2": "88.93",
      "m3": "90.76"
    },
    {
      "p": "[Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations](https://www.sciencedirect.com/science/article/pii/S2590177X19300575)",
      "c": "",
      "n": "SciBERT uncased\n(SciVocab, fine-tuned on \"Annotated corpus for semantic similarity of clinical trial outcomes, original corpus\")",
      "d": "2019-10-17",
      "m1": "89.3",
      "m2": "87.99",
      "m3": "90.78"
    },
    {
      "p": "[Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations](https://www.sciencedirect.com/science/article/pii/S2590177X19300575)",
      "c": "",
      "n": "SciBERT cased\n(SciVocab, fine-tuned on \"Annotated corpus for semantic similarity of clinical trial outcomes, original corpus\")",
      "d": "2019-10-17",
      "m1": "89.3",
      "m2": "87.31",
      "m3": "91.53"
    },
    {
      "p": "[Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations](https://www.sciencedirect.com/science/article/pii/S2590177X19300575)",
      "c": "",
      "n": "BERT-Base uncased\n(fine-tuned on \"Annotated corpus for semantic similarity of clinical trial outcomes, original corpus\")",
      "d": "2019-10-17",
      "m1": "86.8",
      "m2": "85.76",
      "m3": "88.15"
    },
    {
      "p": "[Measuring semantic similarity of clinical trial outcomes using deep pre-trained language representations](https://www.sciencedirect.com/science/article/pii/S2590177X19300575)",
      "c": "",
      "n": "BERT-Base cased\n(fine-tuned on \"Annotated corpus for semantic similarity of clinical trial outcomes, original corpus\")",
      "d": "2019-10-17",
      "m1": "84.21",
      "m2": "83.36",
      "m3": "85.2"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
