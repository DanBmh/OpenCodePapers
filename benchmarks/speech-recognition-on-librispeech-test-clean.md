# speech-recognition-on-librispeech-test-clean

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
      "p": "[High-precision medical speech recognition through synthetic data and semantic correction: UNITED-MEDASR](https://arxiv.org/abs/2412.00055v1)",
      "c": "",
      "n": "United Med ASR",
      "d": "2024-11-24",
      "m1": "0.985"
    },
    {
      "p": "[Samba-ASR: State-Of-The-Art Speech Recognition Leveraging Structured State-Space Models](https://arxiv.org/abs/2501.02832v3)",
      "c": "",
      "n": "SAMBA ASR",
      "d": "2025-01-06",
      "m1": "1.17"
    },
    {
      "p": "[FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information](https://arxiv.org/abs/2405.12807v10)",
      "c": "[&check;&nbsp;Link](https://github.com/lessw2020/fadam_pytorch)",
      "n": "FAdam",
      "d": "2024-05-21",
      "m1": "1.34"
    },
    {
      "p": "[Pushing the Limits of Semi-Supervised Learning for Automatic Speech Recognition](https://arxiv.org/abs/2010.10504v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tuanio/noisy-student-training-asr)",
      "n": "Conformer + Wav2vec 2.0 + SpecAugment-based Noisy Student Training with Libri-Light",
      "d": "2020-10-20",
      "m1": "1.4"
    },
    {
      "p": "[W2v-BERT: Combining Contrastive Learning and Masked Language Modeling for Self-Supervised Speech Pre-Training](https://arxiv.org/abs/2108.06209v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq/tree/ust/examples/w2vbert)",
      "n": "w2v-BERT XXL",
      "d": "2021-08-07",
      "m1": "1.4"
    },
    {
      "p": "[Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084v6)",
      "c": "",
      "n": "parakeet-rnnt-1.1b",
      "d": "2023-05-08",
      "m1": "1.46"
    },
    {
      "p": "[Self-training and Pre-training are Complementary for Speech Recognition](https://arxiv.org/abs/2010.11430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "Conv + Transformer + wav2vec2.0 + pseudo labeling",
      "d": "2020-10-22",
      "m1": "1.5"
    },
    {
      "p": "[Improved Noisy Student Training for Automatic Speech Recognition](https://arxiv.org/abs/2005.09629v2)",
      "c": "[&check;&nbsp;Link](https://github.com/upskyy/ContextNet)",
      "n": "ContextNet + SpecAugment-based Noisy Student Training with Libri-Light",
      "d": "2020-05-19",
      "m1": "1.7"
    },
    {
      "p": "[SpeechStew: Simply Mix All Available Speech Recognition Data to Train One Large Neural Network](https://arxiv.org/abs/2104.02133v3)",
      "c": "",
      "n": "SpeechStew (1B)",
      "d": "2021-04-05",
      "m1": "1.7"
    },
    {
      "p": "[ASAPP-ASR: Multistream CNN and Self-Attentive SRU for SOTA Speech Recognition](https://arxiv.org/abs/2005.10469v1)",
      "c": "",
      "n": "Multistream CNN with Self-Attentive SRU (WER includes text normalization)",
      "d": "2020-05-21",
      "m1": "1.75"
    },
    {
      "p": "[Multi-Head State Space Model for Speech Recognition](https://arxiv.org/abs/2305.12498v2)",
      "c": "",
      "n": "Stateformer",
      "d": "2023-05-21",
      "m1": "1.76"
    },
    {
      "p": "[wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477v3)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "wav2vec 2.0 with Libri-Light",
      "d": "2020-06-20",
      "m1": "1.8"
    },
    {
      "p": "[HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447v1)",
      "c": "[&check;&nbsp;Link](https://github.com/huggingface/transformers)",
      "n": "HuBERT with Libri-Light",
      "d": "2021-06-14",
      "m1": "1.8"
    },
    {
      "p": "[WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/abs/2110.13900v5)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/unilm)",
      "n": "WavLM Large",
      "d": "2021-10-26",
      "m1": "1.8"
    },
    {
      "p": "[E-Branchformer: Branchformer with Enhanced merging for speech recognition](https://arxiv.org/abs/2210.00077v2)",
      "c": "[&check;&nbsp;Link](https://github.com/espnet/espnet)",
      "n": "E-Branchformer (L) + Internal Language Model Estimation",
      "d": "2022-09-30",
      "m1": "1.81"
    },
    {
      "p": "[CR-CTC: Consistency regularization on CTC for improved speech recognition](https://arxiv.org/abs/2410.05101v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+pruned transducer w/ CR-CTC (no  external language model)",
      "d": "2024-10-07",
      "m1": "1.88"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(L)",
      "d": "2020-05-07",
      "m1": "1.9"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(L)",
      "d": "2020-05-16",
      "m1": "1.9"
    },
    {
      "p": "[Transformer-based ASR Incorporating Time-reduction Layer and Fine-tuning with Self-Knowledge Distillation](https://arxiv.org/abs/2103.09903v1)",
      "c": "",
      "n": "Transformer+Time reduction+Self Knowledge distillation",
      "d": "2021-03-17",
      "m1": "1.9"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(M)",
      "d": "2020-05-07",
      "m1": "2"
    },
    {
      "p": "[Improving RNN Transducer Based ASR with Auxiliary Tasks](https://arxiv.org/abs/2011.03109v2)",
      "c": "[&check;&nbsp;Link](https://github.com/upskyy/Transformer-Transducer)",
      "n": "Transformer Transducer",
      "d": "2020-11-05",
      "m1": "2.0"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(M)",
      "d": "2020-05-16",
      "m1": "2"
    },
    {
      "p": "[SpeechStew: Simply Mix All Available Speech Recognition Data to Train One Large Neural Network](https://arxiv.org/abs/2104.02133v3)",
      "c": "",
      "n": "SpeechStew (100M)",
      "d": "2021-04-05",
      "m1": "2.0"
    },
    {
      "p": "[Qwen-Audio: Advancing Universal Audio Understanding via Unified Large-Scale Audio-Language Models](https://arxiv.org/abs/2311.07919v2)",
      "c": "[&check;&nbsp;Link](https://github.com/alibaba-damo-academy/FunASR)",
      "n": "Qwen-Audio",
      "d": "2023-11-14",
      "m1": "2.0"
    },
    {
      "p": "[Zipformer: A faster and better encoder for automatic speech recognition](https://arxiv.org/abs/2310.11230v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+pruned transducer (no  external language model)",
      "d": "2023-10-17",
      "m1": "2.00"
    },
    {
      "p": "[CR-CTC: Consistency regularization on CTC for improved speech recognition](https://arxiv.org/abs/2410.05101v4)",
      "c": "[&check;&nbsp;Link](https://github.com/k2-fsa/icefall)",
      "n": "Zipformer+CR-CTC (no external language model)",
      "d": "2024-10-07",
      "m1": "2.02"
    },
    {
      "p": "[End-to-end ASR: from Supervised to Semi-Supervised Learning with Modern Architectures](https://arxiv.org/abs/1911.08460v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/models/sota/2019)",
      "n": "Conv + Transformer AM + Pseudo-Labeling (ConvLM with Transformer Rescoring)",
      "d": "2019-11-19",
      "m1": "2.03"
    },
    {
      "p": "[Iterative Pseudo-Labeling for Speech Recognition](https://arxiv.org/abs/2005.09267v2)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/ipl)",
      "n": "Conv + Transformer AM + Iterative Pseudo-Labeling (n-gram LM + Transformer Rescoring)",
      "d": "2020-05-19",
      "m1": "2.10"
    },
    {
      "p": "[Faster, Simpler and More Accurate Hybrid ASR Systems Using Wordpieces](https://arxiv.org/abs/2005.09150v2)",
      "c": "",
      "n": "CTC + Transformer LM rescoring",
      "d": "2020-05-19",
      "m1": "2.10"
    },
    {
      "p": "[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100v1)",
      "c": "[&check;&nbsp;Link](https://github.com/PaddlePaddle/PaddleSpeech)",
      "n": "Conformer(S)",
      "d": "2020-05-16",
      "m1": "2.1"
    },
    {
      "p": "[Graph Convolutions Enrich the Self-Attention in Transformers!](https://arxiv.org/abs/2312.04234v5)",
      "c": "[&check;&nbsp;Link](https://github.com/jeongwhanchoi/gfsa)",
      "n": "Branchformer + GFSA",
      "d": "2023-12-07",
      "m1": "2.11"
    },
    {
      "p": "[State-of-the-Art Speech Recognition Using Multi-Stream Self-Attention With Dilated 1D Convolutions](https://arxiv.org/abs/1910.00716v1)",
      "c": "[&check;&nbsp;Link](https://github.com/s-omranpour/Pytorch-Speech-Recognition)",
      "n": "Multi-Stream Self-Attention With Dilated 1D Convolutions",
      "d": "2019-10-01",
      "m1": "2.20"
    },
    {
      "p": "[Librispeech Transducer Model with Internal Language Model Prior Correction](https://arxiv.org/abs/2104.03006v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rwth-i6/returnn)",
      "n": "LSTM Transducer",
      "d": "2021-04-07",
      "m1": "2.23"
    },
    {
      "p": "[Transformer-based Acoustic Modeling for Hybrid Speech Recognition](https://arxiv.org/abs/1910.09799v2)",
      "c": "",
      "n": "Hybrid + Transformer LM rescoring",
      "d": "2019-10-22",
      "m1": "2.26"
    },
    {
      "p": "[RWTH ASR Systems for LibriSpeech: Hybrid vs Attention -- w/o Data Augmentation](https://arxiv.org/abs/1905.03072v3)",
      "c": "[&check;&nbsp;Link](https://github.com/rwth-i6/returnn)",
      "n": "Hybrid model with Transformer rescoring",
      "d": "2019-05-08",
      "m1": "2.3"
    },
    {
      "p": "[ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](https://arxiv.org/abs/2005.03191v3)",
      "c": "[&check;&nbsp;Link](https://github.com/TensorSpeech/TensorFlowASR)",
      "n": "ContextNet(S)",
      "d": "2020-05-07",
      "m1": "2.3"
    },
    {
      "p": "[End-to-end ASR: from Supervised to Semi-Supervised Learning with Modern Architectures](https://arxiv.org/abs/1911.08460v3)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter/tree/master/recipes/models/sota/2019)",
      "n": "Conv + Transformer AM (ConvLM  with Transformer Rescoring) (LS only)",
      "d": "2019-11-19",
      "m1": "2.31"
    },
    {
      "p": "[Squeezeformer: An Efficient Transformer for Automatic Speech Recognition](https://arxiv.org/abs/2206.00888v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/NeMo/tree/main/examples/asr/conf/squeezeformer)",
      "n": "Squeezeformer (L)",
      "d": "2022-06-02",
      "m1": "2.47"
    },
    {
      "p": "[SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mozilla/DeepSpeech)",
      "n": "LAS + SpecAugment",
      "d": "2019-04-18",
      "m1": "2.5"
    },
    {
      "p": "[A Comparative Study on Transformer vs RNN in Speech Applications](https://arxiv.org/abs/1909.06317v2)",
      "c": "[&check;&nbsp;Link](https://github.com/espnet/espnet)",
      "n": "Transformer",
      "d": "2019-09-13",
      "m1": "2.6"
    },
    {
      "p": "[QuartzNet: Deep Automatic Speech Recognition with 1D Time-Channel Separable Convolutions](https://arxiv.org/abs/1910.10261v1)",
      "c": "[&check;&nbsp;Link](https://github.com/NVIDIA/NeMo)",
      "n": "QuartzNet15x5",
      "d": "2019-10-22",
      "m1": "2.69"
    },
    {
      "p": "[SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mozilla/DeepSpeech)",
      "n": "LAS (no LM)",
      "d": "2019-04-18",
      "m1": "2.7"
    },
    {
      "p": "[Self-training and Pre-training are Complementary for Speech Recognition](https://arxiv.org/abs/2010.11430v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/fairseq)",
      "n": "wav2vec_wav2letter",
      "d": "2020-10-22",
      "m1": "2.7"
    },
    {
      "p": "[Espresso: A Fast End-to-end Neural Speech Recognition Toolkit](https://arxiv.org/abs/1909.08723v3)",
      "c": "[&check;&nbsp;Link](https://github.com/freewym/espresso)",
      "n": "Espresso",
      "d": "2019-09-18",
      "m1": "2.8"
    },
    {
      "p": "[Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/abs/1904.03288v3)",
      "c": "[&check;&nbsp;Link](https://github.com/osmr/imgclsmob)",
      "n": "Jasper DR 10x5 (+ Time/Freq Masks)",
      "d": "2019-04-05",
      "m1": "2.84"
    },
    {
      "p": "[Jasper: An End-to-End Convolutional Neural Acoustic Model](https://arxiv.org/abs/1904.03288v3)",
      "c": "[&check;&nbsp;Link](https://github.com/osmr/imgclsmob)",
      "n": "Jasper DR 10x5",
      "d": "2019-04-05",
      "m1": "2.95"
    },
    {
      "p": "[Neural Network Language Modeling with Letter-based Features and Importance Sampling](https://www.cs.jhu.edu/~hxu/neural-network-language.pdf)",
      "c": "",
      "n": "tdnn + chain + rnnlm rescoring",
      "d": "2018-04-15",
      "m1": "3.06"
    },
    {
      "p": "[Fully Convolutional Speech Recognition](http://arxiv.org/abs/1812.06864v2)",
      "c": "",
      "n": "Convolutional Speech Recognition",
      "d": "2018-12-17",
      "m1": "3.26"
    },
    {
      "p": "[MT4SSL: Boosting Self-Supervised Speech Representation Learning by Integrating Multiple Targets](https://arxiv.org/abs/2211.07321v3)",
      "c": "[&check;&nbsp;Link](https://github.com/ddlbojack/mt4ssl)",
      "n": "MT4SSL",
      "d": "2022-11-14",
      "m1": "3.4"
    },
    {
      "p": "[On the Choice of Modeling Unit for Sequence-to-Sequence Speech Recognition](https://arxiv.org/abs/1902.01955v2)",
      "c": "[&check;&nbsp;Link](https://github.com/30stomercury/Automatic_Speech_Recognition)",
      "n": "Model Unit Exploration",
      "d": "2019-02-05",
      "m1": "3.60"
    },
    {
      "p": "[Improved training of end-to-end attention models for speech recognition](http://arxiv.org/abs/1805.03294v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rwth-i6/returnn)",
      "n": "Seq-to-seq attention",
      "d": "2018-05-08",
      "m1": "3.82"
    },
    {
      "p": "[CRF-based Single-stage Acoustic Modeling with CTC Topology](https://ieeexplore.ieee.org/document/8682256)",
      "c": "[&check;&nbsp;Link](https://github.com/thu-spmi/cat)",
      "n": "CTC-CRF 4gram-LM",
      "d": "2019-04-16",
      "m1": "4.09"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HMM-TDNN trained with MMI + data augmentation (speed) + iVectors + 3 regularizations",
      "d": null,
      "m1": "4.3"
    },
    {
      "p": "[Let SSMs be ConvNets: State-space Modeling with Optimal Tensor Contractions](https://arxiv.org/abs/2501.13230v1)",
      "c": "",
      "n": "Centaurus (30 M)",
      "d": "2025-01-22",
      "m1": "4.4"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HMM-TDNN + iVectors",
      "d": null,
      "m1": "4.8"
    },
    {
      "p": "[Letter-Based Speech Recognition with Gated ConvNets](http://arxiv.org/abs/1712.09444v2)",
      "c": "[&check;&nbsp;Link](https://github.com/eric-erki/wav2letter)",
      "n": "Gated ConvNets",
      "d": "2017-12-22",
      "m1": "4.8"
    },
    {
      "p": "[Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](http://arxiv.org/abs/1512.02595v1)",
      "c": "[&check;&nbsp;Link](https://github.com/tensorflow/models/tree/master/research/deep_speech)",
      "n": "Deep Speech 2",
      "d": "2015-12-08",
      "m1": "5.33"
    },
    {
      "p": "[Improving End-to-End Speech Recognition with Policy Learning](http://arxiv.org/abs/1712.07101v1)",
      "c": "",
      "n": "CTC + policy learning",
      "d": "2017-12-19",
      "m1": "5.42"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HMM-DNN + pNorm*",
      "d": null,
      "m1": "5.5"
    },
    {
      "p": "[The PyTorch-Kaldi Speech Recognition Toolkit](http://arxiv.org/abs/1811.07453v2)",
      "c": "[&check;&nbsp;Link](https://github.com/mravanelli/pytorch-kaldi)",
      "n": "Li-GRU",
      "d": "2018-11-19",
      "m1": "6.2"
    },
    {
      "p": "[Snips Voice Platform: an embedded Spoken Language Understanding system for private-by-design voice interfaces](http://arxiv.org/abs/1805.10190v3)",
      "c": "[&check;&nbsp;Link](https://github.com/snipsco/snips-nlu)",
      "n": "Snips",
      "d": "2018-05-25",
      "m1": "6.4"
    },
    {
      "p": "[Semi-Supervised Speech Recognition via Local Prior Matching](https://arxiv.org/abs/2002.10336v1)",
      "c": "[&check;&nbsp;Link](https://github.com/facebookresearch/wav2letter)",
      "n": "Local Prior Matching (Large Model)",
      "d": "2020-02-24",
      "m1": "7.19"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "HMM-(SAT)GMM",
      "d": null,
      "m1": "8.0"
    },
    {
      "p": "[Amortized Neural Networks for Low-Latency Speech Recognition](https://arxiv.org/abs/2108.01553v1)",
      "c": "",
      "n": "AmNet",
      "d": "2021-08-03",
      "m1": "8.6"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
