# speech-recognition-on-librispeech-test-other

[Dataset Link](http://www.openslr.org/12) \
Task Hierarchy: ['Speech Recognition']

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
      "label": "Word Error Rate (WER)",
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
      "p": "[Samba-ASR: State-Of-The-Art Speech Recognition Leveraging Structured State-Space Models](https://arxiv.org/abs/2501.02832v3)",
      "c": "",
      "n": "SAMBA ASR",
      "d": "2025-01-06",
      "m1": "2.48"
    },
    {
      "p": "[FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information](https://arxiv.org/abs/2405.12807v10)",
      "c": "[&check;&nbsp;Link](https://github.com/lessw2020/fadam_pytorch)",
      "n": "FAdam",
      "d": "2024-05-21",
      "m1": "2.49"
    },
    {
      "p": "[W2v-BERT: Combining Contrastive Learning and Masked Language Modeling for Self-Supervised Speech Pre-Training](https://arxiv.org/abs/2108.06209v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq/tree/ust/examples/w2vbert)",
      "n": "w2v-BERT XXL",
      "d": "2021-08-07",
      "m1": "2.5"
    },
    {
      "p": "[Pushing the Limits of Semi-Supervised Learning for Automatic Speech Recognition](https://arxiv.org/abs/2010.10504v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tuanio/noisy-student-training-asr)",
      "n": "Conformer + Wav2vec 2.0 + SpecAugment-based Noisy Student Training with Libri-Light",
      "d": "2020-10-20",
      "m1": "2.6"
    },
    {
      "p": "[HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "HuBERT with Libri-Light",
      "d": "2021-06-14",
      "m1": "2.9"
    },
    {
      "p": "[wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "wav2vec 2.0 with Libri-Light",
      "d": "2020-06-20",
      "m1": "3.0"
    },
    {
      "p": "[Self-training and Pre-training are Complementary for Speech Recognition](https://arxiv.org/abs/2010.11430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "Conv + Transformer + wav2vec2.0 + pseudo labeling",
      "d": "2020-10-22",
      "m1": "3.1"
    },
    {
      "p": "[WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/abs/2110.13900v5)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/unilm)",
      "n": "WavLM Large",
      "d": "2021-10-26",
      "m1": "3.2"
    },
    {
      "p": "[SpeechStew: Simply Mix All Available Speech Recognition Data to Train One Large Neural Network](https://arxiv.org/abs/2104.02133v3)",
      "c": "",
      "n": "SpeechStew (1B)",
      "d": "2021-04-05",
      "m1": "3.3"
    },
    {
      "p": "[Improved Noisy Student Training for Automatic Speech Recognition](https://arxiv.org/abs/2005.09629v2)",
      "c": "[&check;&nbsp;Link](https://github.com/upskyy/ContextNet)",
      "n": "ContextNet + SpecAugment-based Noisy Student Training with Libri-Light",
      "d": "2020-05-19",
      "m1": "3.4"
    },
    {
      "p": "[E-Branchformer: Branchformer with Enhanced merging for speech recognition](https://arxiv.org/abs/2210.00077v2)",
      "c": "[&check;&nbsp;Link](https://github.com/espnet/espnet)",
      "n": "E-Branchformer (L) + Internal Language Model Estimation",
      "d": "2022-09-30",
      "m1": "3.65"
    },
    {
      "p": "[data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language](https://arxiv.org/abs/2202.03555v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers/tree/main/src/transformers/models/data2vec)",
      "n": "data2vec",
      "d": "2022-02-07",
      "m1": "3.7"
    },
    {
      "p": "[Iterative Pseudo-Labeling for Speech Recognition](https://arxiv.org/abs/2005.09267v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/ipl)",
      "n": "Conv + Transformer AM + Iterative Pseudo-Labeling (n-gram LM + Transformer Rescoring)",
      "d": "2020-05-19",
      "m1": "3.83"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(L)",
      "d": "2020-05-16",
      "m1": "3.9"
    },
    {
      "p": "[CR-CTC: Consistency regularization on CTC for improved speech recognition](https://arxiv.org/abs/2410.05101v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+pruned transducer w/ CR-CTC\n(no external language model)",
      "d": "2024-10-07",
      "m1": "3.95"
    },
    {
      "p": "[SpeechStew: Simply Mix All Available Speech Recognition Data to Train One Large Neural Network](https://arxiv.org/abs/2104.02133v3)",
      "c": "",
      "n": "SpeechStew (100M)",
      "d": "2021-04-05",
      "m1": "4.0"
    },
    {
      "p": "[wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "wav2vec 2.0",
      "d": "2020-06-20",
      "m1": "4.1"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(L)",
      "d": "2020-05-07",
      "m1": "4.1"
    },
    {
      "p": "[End-to-end ASR: from Supervised to Semi-Supervised Learning with Modern Architectures](https://arxiv.org/abs/1911.08460v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/models/sota/2019)",
      "n": "Conv + Transformer AM (ConvLM with Transformer Rescoring)",
      "d": "2019-11-19",
      "m1": "4.11"
    },
    {
      "p": "[Faster, Simpler and More Accurate Hybrid ASR Systems Using Wordpieces](https://arxiv.org/abs/2005.09150v2)",
      "c": "",
      "n": "CTC + Transformer LM rescoring",
      "d": "2020-05-19",
      "m1": "4.20"
    },
    {
      "p": "[Improving RNN Transducer Based ASR with Auxiliary Tasks](https://arxiv.org/abs/2011.03109v2)",
      "c": "[&check;&nbsp;Link](https://github.com/upskyy/Transformer-Transducer)",
      "n": "Transformer Transducer",
      "d": "2020-11-05",
      "m1": "4.20"
    },
    {
      "p": "[Qwen-Audio: Advancing Universal Audio Understanding via Unified Large-Scale Audio-Language Models](https://arxiv.org/abs/2311.07919v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba-damo-academy/FunASR)",
      "n": "Qwen-Audio",
      "d": "2023-11-14",
      "m1": "4.2"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(M)",
      "d": "2020-05-16",
      "m1": "4.3"
    },
    {
      "p": "[CR-CTC: Consistency regularization on CTC for improved speech recognition](https://arxiv.org/abs/2410.05101v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+CR-CTC\n(no external language model)",
      "d": "2024-10-07",
      "m1": "4.35"
    },
    {
      "p": "[Zipformer: A faster and better encoder for automatic speech recognition](https://arxiv.org/abs/2310.11230v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+pruned transducer\n(no external language model)",
      "d": "2023-10-17",
      "m1": "4.38"
    },
    {
      "p": "[ASAPP-ASR: Multistream CNN and Self-Attentive SRU for SOTA Speech Recognition](https://arxiv.org/abs/2005.10469v1)",
      "c": "",
      "n": "Multistream CNN with Self-Attentive SRU",
      "d": "2020-05-21",
      "m1": "4.46"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(M)",
      "d": "2020-05-07",
      "m1": "4.5"
    },
    {
      "p": "[Transformer-based Acoustic Modeling for Hybrid Speech Recognition](https://arxiv.org/abs/1910.09799v2)",
      "c": "",
      "n": "hybrid + Transformer LM rescoring",
      "d": "2019-10-22",
      "m1": "4.85"
    },
    {
      "p": "[Graph Convolutions Enrich the Self-Attention in Transformers!](https://arxiv.org/abs/2312.04234v5)",
      "c": "[&check;&nbsp;Link](https://github.com/jeongwhanchoi/gfsa)",
      "n": "Branchformer + GFSA",
      "d": "2023-12-07",
      "m1": "4.94"
    },
    {
      "p": "[RWTH ASR Systems for LibriSpeech: Hybrid vs Attention -- w/o Data Augmentation](https://arxiv.org/abs/1905.03072v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rwth-i6/returnn)",
      "n": "Hybrid model with Transformer rescoring",
      "d": "2019-05-08",
      "m1": "5.0"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(S)",
      "d": "2020-05-16",
      "m1": "5.0"
    },
    {
      "p": "[End-to-end ASR: from Supervised to Semi-Supervised Learning with Modern Architectures](https://arxiv.org/abs/1911.08460v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/models/sota/2019)",
      "n": "Conv + Transformer AM (ConvLM  with Transformer Rescoring) (LS only)",
      "d": "2019-11-19",
      "m1": "5.18"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(S)",
      "d": "2020-05-07",
      "m1": "5.5"
    },
    {
      "p": "[Librispeech Transducer Model with Internal Language Model Prior Correction](https://arxiv.org/abs/2104.03006v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwth-i6/returnn)",
      "n": "LSTM Transducer",
      "d": "2021-04-07",
      "m1": "5.6"
    },
    {
      "p": "[A Comparative Study on Transformer vs RNN in Speech Applications](https://arxiv.org/abs/1909.06317v2)",
      "c": "[&check;&nbsp;Link](https://github.com/espnet/espnet)",
      "n": "Transformer",
      "d": "2019-09-13",
      "m1": "5.7"
    },
    {
      "p": "[SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mozilla/DeepSpeech)",
      "n": "LAS + SpecAugment",
      "d": "2019-04-18",
      "m1": "5.8"
    },
    {
      "p": "[State-of-the-Art Speech Recognition Using Multi-Stream Self-Attention With Dilated 1D Convolutions](https://arxiv.org/abs/1910.00716v1)",
      "c": "[&check;&nbsp;Link](https://github.com/s-omranpour/Pytorch-Speech-Recognition)",
      "n": "Multi-Stream Self-Attention With Dilated 1D Convolutions",
      "d": "2019-10-01",
      "m1": "5.80"
    },
    {
      "p": "[Squeezeformer: An Efficient Transformer for Automatic Speech Recognition](https://arxiv.org/abs/2206.00888v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/NeMo/tree/main/examples/asr/conf/squeezeformer)",
      "n": "Squeezeformer (L)",
      "d": "2022-06-02",
      "m1": "5.97"
    },
    {
      "p": "[SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mozilla/DeepSpeech)",
      "n": "LAS (no LM)",
      "d": "2019-04-18",
      "m1": "6.5"
    },
    {
      "p": "[Relaxed Attention: A Simple Method to Boost Performance of End-to-End Automatic Speech Recognition](https://arxiv.org/abs/2107.01275v2)",
      "c": "[&check;&nbsp;Link](https://github.com/freewym/espresso)",
      "n": "Conformer with Relaxed Attention",
      "d": "2021-07-02",
      "m1": "6.85"
    },
    {
      "p": "[QuartzNet: Deep Automatic Speech Recognition with 1D Time-Channel Separable Convolutions](https://arxiv.org/abs/1910.10261v1)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/NeMo)",
      "n": "QuartzNet15x5",
      "d": "2019-10-22",
      "m1": "7.25"
    },
    {
      "p": "[Neural Network Language Modeling with Letter-based Features and Importance Sampling](https://www.cs.jhu.edu/~hxu/neural-network-language.pdf)",
      "c": "",
      "n": "tdnn + chain + rnnlm rescoring",
      "d": "2018-04-15",
      "m1": "7.63"
    },
    {
      "p": "[Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/abs/1904.03288v3)",
      "c": "[&check;&nbsp;Link](https://github.com/osmr/imgclsmob)",
      "n": "Jasper DR 10x5 (+ Time/Freq Masks)",
      "d": "2019-04-05",
      "m1": "7.84"
    },
    {
      "p": "[Espresso: A Fast End-to-end Neural Speech Recognition Toolkit](https://arxiv.org/abs/1909.08723v3)",
      "c": "[&check;&nbsp;Link](https://github.com/freewym/espresso)",
      "n": "Espresso",
      "d": "2019-09-18",
      "m1": "8.7"
    },
    {
      "p": "[Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/abs/1904.03288v3)",
      "c": "[&check;&nbsp;Link](https://github.com/osmr/imgclsmob)",
      "n": "Jasper DR 10x5",
      "d": "2019-04-05",
      "m1": "8.79"
    },
    {
      "p": "[MT4SSL: Boosting Self-Supervised Speech Representation Learning by Integrating Multiple Targets](https://arxiv.org/abs/2211.07321v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ddlbojack/mt4ssl)",
      "n": "MT4SSL",
      "d": "2022-11-14",
      "m1": "9.6"
    },
    {
      "p": "[Fully Convolutional Speech Recognition](http://arxiv.org/abs/1812.06864v2)",
      "c": "",
      "n": "Convolutional Speech Recognition",
      "d": "2018-12-17",
      "m1": "10.47"
    },
    {
      "p": "[CRF-based Single-stage Acoustic Modeling with CTC Topology](https://ieeexplore.ieee.org/document/8682256)",
      "c": "[&check;&nbsp;Link](https://github.com/thu-spmi/cat)",
      "n": "CTC-CRF 4gram-LM",
      "d": "2019-04-16",
      "m1": "10.65"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "TDNN + pNorm + speed up/down speech",
      "d": null,
      "m1": "12.5"
    },
    {
      "p": "[Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](http://arxiv.org/abs/1512.02595v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/deep_speech)",
      "n": "Deep Speech 2",
      "d": "2015-12-08",
      "m1": "13.25"
    },
    {
      "p": "[Semi-Supervised Speech Recognition via Local Prior Matching](https://arxiv.org/abs/2002.10336v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter)",
      "n": "Local Prior Matching (Large Model, ConvLM LM)",
      "d": "2020-02-24",
      "m1": "15.28"
    },
    {
      "p": "[Snips Voice Platform: an embedded Spoken Language Understanding system for private-by-design voice interfaces](http://arxiv.org/abs/1805.10190v3)",
      "c": "[&check;&nbsp;Link](https://github.com/snipsco/snips-nlu)",
      "n": "Snips",
      "d": "2018-05-25",
      "m1": "16.5"
    },
    {
      "p": "[Semi-Supervised Speech Recognition via Local Prior Matching](https://arxiv.org/abs/2002.10336v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter)",
      "n": "Local Prior Matching (Large Model)",
      "d": "2020-02-24",
      "m1": "20.84"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
