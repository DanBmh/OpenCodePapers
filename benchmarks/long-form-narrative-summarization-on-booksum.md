# long-form-narrative-summarization-on-booksum

[Dataset Link](https://github.com/salesforce/booksum) \
Task Hierarchy: ['Text Summarization', 'Long-Form Narrative Summarization']

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
      "label": "BERTScore (F1)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "ROUGE-1",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "ROUGE-2",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "ROUGE-L",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "ROUGE (geometric mean of 1/2/L)",
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
      "p": "[NexusSum: Hierarchical LLM Agents for Long-Form Narrative Summarization](https://arxiv.org/abs/2505.24575v1)",
      "c": "",
      "n": "NexusSum (Mistral Large)",
      "d": "2025-05-30",
      "m1": "70.70",
      "m2": "42.51",
      "m3": "10.27",
      "m4": "23.91",
      "m5": "18.27"
    },
    {
      "p": "[End-to-End Long Document Summarization using Gradient Caching](https://arxiv.org/abs/2501.01805v1)",
      "c": "",
      "n": "CachED (BART Large)",
      "d": "2025-01-03",
      "m1": "54.4"
    },
    {
      "p": "[End-to-End Long Document Summarization using Gradient Caching](https://arxiv.org/abs/2501.01805v1)",
      "c": "",
      "n": "SLED (BART Large)",
      "d": "2025-01-03",
      "m1": "52.4"
    },
    {
      "p": "[End-to-End Long Document Summarization using Gradient Caching](https://arxiv.org/abs/2501.01805v1)",
      "c": "",
      "n": "Unlimiformer (BART Base)",
      "d": "2025-01-03",
      "m1": "51.5"
    },
    {
      "p": "[End-to-End Long Document Summarization using Gradient Caching](https://arxiv.org/abs/2501.01805v1)",
      "c": "",
      "n": "Zero-Shot (GPT-4o)",
      "d": "2025-01-03",
      "m1": "47.24",
      "m2": "20.3",
      "m3": "3.5",
      "m4": "17.68"
    },
    {
      "p": "[NexusSum: Hierarchical LLM Agents for Long-Form Narrative Summarization](https://arxiv.org/abs/2505.24575v1)",
      "c": "",
      "n": "Zero-Shot (Mistral Large)",
      "d": "2025-05-30",
      "m1": "46.42",
      "m2": "19.63",
      "m3": "2.99",
      "m4": "12.0"
    },
    {
      "p": "[Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://arxiv.org/abs/2406.02818v1)",
      "c": "",
      "n": "Chain of Agents (Claude 3 Opus)",
      "d": "2024-06-04",
      "m5": "17.47"
    },
    {
      "p": "[NexusSum: Hierarchical LLM Agents for Long-Form Narrative Summarization](https://arxiv.org/abs/2505.24575v1)",
      "c": "",
      "n": "NexusSum (Claude 3 Haiku)",
      "d": "2025-05-30",
      "m5": "16.46"
    },
    {
      "p": "[Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://arxiv.org/abs/2406.02818v1)",
      "c": "",
      "n": "Chain of Agents (Claude 3 Sonet)",
      "d": "2024-06-04",
      "m5": "14.96"
    },
    {
      "p": "[Chain of Agents: Large Language Models Collaborating on Long-Context Tasks](https://arxiv.org/abs/2406.02818v1)",
      "c": "",
      "n": "Chain of Agents (Claude 3 Haiku)",
      "d": "2024-06-04",
      "m5": "13.70"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
