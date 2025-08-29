# image-generation-on-cifar-10

[Dataset Link](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf) \
Task Hierarchy: ['Image Generation']

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
      "label": "FID",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "IS",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "NFE",
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
      "p": "[Generative Modeling with Explicit Memory](https://arxiv.org/abs/2412.08781v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lins-lab/gmem)",
      "n": "GMem",
      "d": "2024-12-11",
      "m1": "1.22"
    },
    {
      "p": "[Direct Discriminative Optimization: Your Likelihood-Based Visual Generative Model is Secretly a GAN Discriminator](https://arxiv.org/abs/2503.01103v2)",
      "c": "[&check;&nbsp;Link](https://github.com/nvlabs/ddo)",
      "n": "EDM+DDO",
      "d": "2025-03-03",
      "m1": "1.30"
    },
    {
      "p": "[SAN: Inducing Metrizability of GAN with Discriminative Normalized Linear Layer](https://arxiv.org/abs/2301.12811v4)",
      "c": "[&check;&nbsp;Link](https://github.com/sony/san)",
      "n": "StyleSAN-XL",
      "d": "2023-01-30",
      "m1": "1.36"
    },
    {
      "p": "[Uni-Instruct: One-step Diffusion Model through Unified Diffusion Divergence Instruction](https://arxiv.org/abs/2505.20755)",
      "c": "",
      "n": "Uni-Instruct",
      "d": "2025-05-27",
      "m1": "1.38",
      "m3": "1"
    },
    {
      "p": "[Adversarial Score identity Distillation: Rapidly Surpassing the Teacher in One Step](https://arxiv.org/abs/2410.14919v4)",
      "c": "[&check;&nbsp;Link](https://github.com/mingyuanzhou/sid)",
      "n": "SiDA-EDM",
      "d": "2024-10-19",
      "m1": "1.396",
      "m3": "1"
    },
    {
      "p": "[Compensation Sampling for Improved Convergence in Diffusion Models](https://arxiv.org/abs/2312.06285v1)",
      "c": "[&check;&nbsp;Link](https://github.com/hotfinda/Compensation-sampling)",
      "n": "PFGM++ +CS",
      "d": "2023-12-11",
      "m1": "1.50"
    },
    {
      "p": "[Diffusion Models Are Innate One-Step Generators](https://arxiv.org/abs/2405.20750v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Zyriix/GDD)",
      "n": "GDD-I",
      "d": "2024-05-31",
      "m1": "1.54",
      "m3": "1"
    },
    {
      "p": "[Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation](https://arxiv.org/abs/2404.04057v3)",
      "c": "[&check;&nbsp;Link](https://github.com/mingyuanzhou/sid)",
      "n": "SiD",
      "d": "2024-04-05",
      "m1": "1.71",
      "m3": "1"
    },
    {
      "p": "[PFGM++: Unlocking the Potential of Physics-Inspired Generative Models](https://arxiv.org/abs/2302.04265v2)",
      "c": "[&check;&nbsp;Link](https://github.com/newbeeer/pfgmpp)",
      "n": "PFGM++",
      "d": "2023-02-08",
      "m1": "1.74"
    },
    {
      "p": "[SciRE-Solver: Accelerating Diffusion Models Sampling by Score-integrand Solver with Recursive Difference](https://arxiv.org/abs/2308.07896v3)",
      "c": "",
      "n": "SciRE-Solver (with EDM)",
      "d": "2023-08-15",
      "m1": "1.76"
    },
    {
      "p": "[Refining Generative Process with Discriminator Guidance in Score-based Diffusion Models](https://arxiv.org/abs/2211.17091v4)",
      "c": "[&check;&nbsp;Link](https://github.com/alsdudrla10/DG)",
      "n": "Discriminator Guidance (unconditional)",
      "d": "2022-11-28",
      "m1": "1.77"
    },
    {
      "p": "[Elucidating the Exposure Bias in Diffusion Models](https://arxiv.org/abs/2308.15321v6)",
      "c": "[&check;&nbsp;Link](https://github.com/forever208/ddpm-ip)",
      "n": "EDM-ES",
      "d": "2023-08-29",
      "m1": "1.8"
    },
    {
      "p": "[The GAN is dead; long live the GAN! A Modern GAN Baseline](https://arxiv.org/abs/2501.05441v1)",
      "c": "[&check;&nbsp;Link](https://github.com/brownvc/r3gan)",
      "n": "R3GAN",
      "d": "2025-01-09",
      "m1": "1.96"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Inductive Moment Matching",
      "d": null,
      "m1": "1.98"
    },
    {
      "p": "[Truncated Consistency Models](https://arxiv.org/abs/2410.14895v2)",
      "c": "",
      "n": "TCM",
      "d": "2024-10-18",
      "m1": "2.05",
      "m3": "2"
    },
    {
      "p": "[Consistency Models Made Easy](https://arxiv.org/abs/2406.14548v2)",
      "c": "[&check;&nbsp;Link](https://github.com/locuslab/ect)",
      "n": "ECT",
      "d": "2024-06-20",
      "m1": "2.11",
      "m3": "2"
    },
    {
      "p": "[Subspace Diffusion Generative Models](https://arxiv.org/abs/2205.01490v2)",
      "c": "[&check;&nbsp;Link](https://github.com/bjing2016/subspace-diffusion)",
      "n": "Subspace Diffusion (NSCN++)",
      "d": "2022-05-03",
      "m1": "2.17"
    },
    {
      "p": "[Posterior Mean Matching: Generative Modeling through Online Bayesian Inference](https://arxiv.org/abs/2412.13286v2)",
      "c": "",
      "n": "Posterior Mean Matching",
      "d": "2024-12-17",
      "m1": "2.18"
    },
    {
      "p": "[Variational Schr\u00f6dinger Diffusion Models](https://arxiv.org/abs/2405.04795v4)",
      "c": "",
      "n": "VSDM",
      "d": "2024-05-08",
      "m1": "2.28"
    },
    {
      "p": "[Block Flow: Learning Straight Flow on Data Blocks](https://arxiv.org/abs/2501.11361v1)",
      "c": "[&check;&nbsp;Link](https://github.com/wpp13749/block_flow)",
      "n": "block flow",
      "d": "2025-01-20",
      "m1": "2.29"
    },
    {
      "p": "[SciRE-Solver: Accelerating Diffusion Models Sampling by Score-integrand Solver with Recursive Difference](https://arxiv.org/abs/2308.07896v3)",
      "c": "",
      "n": "with Score-SDE",
      "d": "2023-08-15",
      "m1": "2.42 FID (20 NFE)"
    },
    {
      "p": "[Poisson Flow Generative Models](https://arxiv.org/abs/2209.11178v4)",
      "c": "[&check;&nbsp;Link](https://github.com/newbeeer/poisson_flow)",
      "n": "PFGM",
      "d": "2022-09-22",
      "m1": "2.48"
    },
    {
      "p": "[Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/diffusion_distillation)",
      "n": "PD (NFE=8)",
      "d": "2022-02-01",
      "m1": "2.57"
    },
    {
      "p": "[A High-Quality Robust Diffusion Framework for Corrupted Dataset](https://arxiv.org/abs/2311.17101v2)",
      "c": "[&check;&nbsp;Link](https://github.com/VinAIResearch/RDUOT)",
      "n": "RDUOT",
      "d": "2023-11-28",
      "m1": "2.95"
    },
    {
      "p": "[Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512v2)",
      "c": "[&check;&nbsp;Link](https://github.com/google-research/google-research/tree/master/diffusion_distillation)",
      "n": "PD (NFE=4)",
      "d": "2022-02-01",
      "m1": "3.00"
    },
    {
      "p": "[Likelihood Training of Schr\u00f6dinger Bridge using Forward-Backward SDEs Theory](https://arxiv.org/abs/2110.11291v5)",
      "c": "[&check;&nbsp;Link](https://github.com/ghliu/sb-fbsde)",
      "n": "SB-FBSDE",
      "d": "2021-10-21",
      "m1": "3.01"
    },
    {
      "p": "[The Disappearance of Timestep Embedding in Modern Time-Dependent Neural Networks](https://arxiv.org/abs/2405.14126v1)",
      "c": "[&check;&nbsp;Link](https://github.com/kmbmjn/disappearance_of_timestep_embedding)",
      "n": "DDPM",
      "d": "2024-05-23",
      "m1": "3.074"
    },
    {
      "p": "[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239v2)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "Denoising Diffusion",
      "d": "2020-06-19",
      "m1": "3.17"
    },
    {
      "p": "[Beyond Masked and Unmasked: Discrete Diffusion Models via Partial Masking](https://arxiv.org/abs/2505.18495v1)",
      "c": "",
      "n": "MDM-Prime",
      "d": "2025-05-24",
      "m1": "3.26",
      "m2": "9.67"
    },
    {
      "p": "[Efficient generative adversarial networks using linear additive-attention Transformers](https://arxiv.org/abs/2401.09596v4)",
      "c": "[&check;&nbsp;Link](https://github.com/milmor/ladagan)",
      "n": "LadaGAN",
      "d": "2024-01-17",
      "m1": "3.29"
    },
    {
      "p": "[Blackout Diffusion: Generative Diffusion Models in Discrete-State Spaces](https://arxiv.org/abs/2305.11089v1)",
      "c": "[&check;&nbsp;Link](https://github.com/lanl/blackout-diffusion)",
      "n": "Blackout Diffusion",
      "d": "2023-05-18",
      "m1": "4.58"
    },
    {
      "p": "[Differentiable Augmentation for Data-Efficient GAN Training](https://arxiv.org/abs/2006.10738v4)",
      "c": "[&check;&nbsp;Link](https://github.com/POSTECH-CVLab/PyTorch-StudioGAN)",
      "n": "DiffAugment-BigGAN",
      "d": "2020-06-18",
      "m1": "4.61"
    },
    {
      "p": "[Beyond Masked and Unmasked: Discrete Diffusion Models via Partial Masking](https://arxiv.org/abs/2505.18495v1)",
      "c": "",
      "n": "MDM",
      "d": "2025-05-24",
      "m1": "4.66",
      "m2": "9.09"
    },
    {
      "p": "[Forward-only Diffusion Probabilistic Models](https://arxiv.org/abs/2505.16733v1)",
      "c": "[&check;&nbsp;Link](https://github.com/Algolzw/FoD)",
      "n": "FoD-ODE",
      "d": "2025-05-22",
      "m1": "5.01"
    },
    {
      "p": "[Consistency Models](https://arxiv.org/abs/2303.01469v2)",
      "c": "[&check;&nbsp;Link](https://github.com/openai/consistency_models)",
      "n": "CT (Direct Generation, NFE=2)",
      "d": "2023-03-02",
      "m1": "5.83"
    },
    {
      "p": "[GENIE: Higher-Order Denoising Diffusion Solvers](https://arxiv.org/abs/2210.05475v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nv-tlabs/GENIE)",
      "n": "GENIE (NFEs=10)",
      "d": "2022-10-11",
      "m1": "5.97"
    },
    {
      "p": "[Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747v2)",
      "c": "[&check;&nbsp;Link](https://github.com/shivammehta25/Matcha-TTS)",
      "n": "FM",
      "d": "2022-10-06",
      "m1": "6.35"
    },
    {
      "p": "[ViTGAN: Training GANs with Vision Transformers](https://arxiv.org/abs/2107.04589v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/parti-pytorch)",
      "n": "ViTGAN",
      "d": "2021-07-09",
      "m1": "6.66"
    },
    {
      "p": "[Score-based Generative Modeling in Latent Space](https://arxiv.org/abs/2106.05931v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/LSGM)",
      "n": "LSGM (NLL)",
      "d": "2021-06-10",
      "m1": "6.89"
    },
    {
      "p": "[Lessons Learned from the Training of GANs on Artificial Datasets](https://arxiv.org/abs/2007.06418v2)",
      "c": "[&check;&nbsp;Link](https://github.com/tsc2017/MIX-GAN)",
      "n": "MIX-BigGAN",
      "d": "2020-07-13",
      "m1": "8.17"
    },
    {
      "p": "[Regularizing Generative Adversarial Networks under Limited Data](https://arxiv.org/abs/2104.03310v1)",
      "c": "[&check;&nbsp;Link](https://github.com/google/lecam-gan)",
      "n": "LeCAM (BigGAN + DA)",
      "d": "2021-04-07",
      "m1": "8.46"
    },
    {
      "p": "[LT-GAN: Self-Supervised GAN with Latent Transformation Detection](https://arxiv.org/abs/2010.09893v1)",
      "c": "",
      "n": "CR +LT-BigGAN",
      "d": "2020-10-19",
      "m1": "9.80"
    },
    {
      "p": "[EAGAN: Efficient Two-stage Evolutionary Architecture Search for GANs](https://arxiv.org/abs/2111.15097v2)",
      "c": "[&check;&nbsp;Link](https://github.com/marsggbo/EAGAN)",
      "n": "EAGAN (G+D)",
      "d": "2021-11-30",
      "m1": "9.91"
    },
    {
      "p": "[EAGAN: Efficient Two-stage Evolutionary Architecture Search for GANs](https://arxiv.org/abs/2111.15097v2)",
      "c": "[&check;&nbsp;Link](https://github.com/marsggbo/EAGAN)",
      "n": "EAGAN (G)",
      "d": "2021-11-30",
      "m1": "10.14"
    },
    {
      "p": "[Improving GAN Training with Probability Ratio Clipping and Sample Reweighting](https://arxiv.org/abs/2006.06900v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Holmeswww/PPOGAN)",
      "n": "PPOGAN",
      "d": "2020-06-12",
      "m1": "10.7"
    },
    {
      "p": "[Improved Techniques for Training Score-Based Generative Models](https://arxiv.org/abs/2006.09011v2)",
      "c": "[&check;&nbsp;Link](https://github.com/yang-song/score_sde_pytorch)",
      "n": "NCSNv2",
      "d": "2020-06-16",
      "m1": "10.87"
    },
    {
      "p": "[Discriminator Contrastive Divergence: Semi-Amortized Generative Modeling by Exploring Energy of the Discriminator](https://arxiv.org/abs/2004.01704v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MinkaiXu/Discriminator-Contrastive-Divergence)",
      "n": "SNGAN-DCD (Latent)",
      "d": "2020-04-05",
      "m1": "16.24"
    },
    {
      "p": "[$\u03a0-$nets: Deep Polynomial Neural Networks](https://arxiv.org/abs/2003.03828v2)",
      "c": "[&check;&nbsp;Link](https://github.com/grigorisg9gr/polynomial_nets)",
      "n": "Pi-net",
      "d": "2020-03-08",
      "m1": "16.79"
    },
    {
      "p": "[Deep Polynomial Neural Networks](https://arxiv.org/abs/2006.13026v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Faceplugin-ltd/FaceRecognition-Android)",
      "n": "ProdPoly",
      "d": "2020-06-20",
      "m1": "16.79"
    },
    {
      "p": "[Dist-GAN: An Improved GAN using Distance Constraints](http://arxiv.org/abs/1803.08887v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tntrung/gan)",
      "n": "Dist-GAN",
      "d": "2018-03-23",
      "m1": "17.61"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "LOGAN",
      "d": null,
      "m1": "17.87"
    },
    {
      "p": "[Dual Contradistinctive Generative Autoencoder](https://arxiv.org/abs/2011.10063v1)",
      "c": "",
      "n": "DC-VAE",
      "d": "2020-11-19",
      "m1": "17.9"
    },
    {
      "p": "[Learning Stationary Markov Processes with Contrastive Adjustment](https://arxiv.org/abs/2303.05497v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ludvb/nkca)",
      "n": "NK-CA",
      "d": "2023-03-09",
      "m1": "18.27"
    },
    {
      "p": "[Contextual Convolutional Neural Networks](https://arxiv.org/abs/2108.07387v1)",
      "c": "[&check;&nbsp;Link](https://github.com/iduta/coconv)",
      "n": "CoProGAN",
      "d": "2021-08-17",
      "m1": "19.66"
    },
    {
      "p": "[Stable Rank Normalization for Improved Generalization in Neural Networks and GANs](https://arxiv.org/abs/1906.04659v3)",
      "c": "",
      "n": "SRN-GANs",
      "d": "2019-06-11",
      "m1": "19.83"
    },
    {
      "p": "[DuelGAN: A Duel Between Two Discriminators Stabilizes the GAN Training](https://arxiv.org/abs/2101.07524v3)",
      "c": "",
      "n": "PeerGAN",
      "d": "2021-01-19",
      "m1": "21.55"
    },
    {
      "p": "[Discriminator Contrastive Divergence: Semi-Amortized Generative Modeling by Exploring Energy of the Discriminator](https://arxiv.org/abs/2004.01704v1)",
      "c": "[&check;&nbsp;Link](https://github.com/MinkaiXu/Discriminator-Contrastive-Divergence)",
      "n": "SNGAN-DCD (Pixel)",
      "d": "2020-04-05",
      "m1": "21.67"
    },
    {
      "p": "[Spectral Normalization for Generative Adversarial Networks](http://arxiv.org/abs/1802.05957v1)",
      "c": "[&check;&nbsp;Link](https://github.com/pytorch/pytorch/blob/a77b391de723a69fb59ff6ae9d1236ca93f03a97/torch/nn/utils/spectral_norm.py)",
      "n": "SN-GANs",
      "d": "2018-02-16",
      "m1": "21.7"
    },
    {
      "p": "[CLR-GAN: Improving GANs Stability and Quality via Consistent Latent Representation and Reconstruction](https://link.springer.com/chapter/10.1007/978-3-031-73232-4_12)",
      "c": "[&check;&nbsp;Link](https://github.com/Petecheco/CLR-GAN)",
      "n": "CLR-GAN",
      "d": "2024-09-30",
      "m1": "23.3"
    },
    {
      "p": "[A Contrastive Learning Approach for Training Variational Autoencoder Priors](https://arxiv.org/abs/2010.02917v3)",
      "c": "",
      "n": "NCP-VAE",
      "d": "2020-10-06",
      "m1": "24.08"
    },
    {
      "p": "[GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium](http://arxiv.org/abs/1706.08500v6)",
      "c": "[&check;&nbsp;Link](https://github.com/jantic/DeOldify)",
      "n": "WGAN-GP + TT Update Rule",
      "d": "2017-06-26",
      "m1": "24.8"
    },
    {
      "p": "[On gradient regularizers for MMD GANs](https://arxiv.org/abs/1805.11565v5)",
      "c": "[&check;&nbsp;Link](https://github.com/MichaelArbel/Scaled-MMD-GAN)",
      "n": "SN-SMMDGAN",
      "d": "2018-05-29",
      "m1": "25.0"
    },
    {
      "p": "[Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600v3)",
      "c": "[&check;&nbsp;Link](https://github.com/yang-song/score_sde_pytorch)",
      "n": "NCSN",
      "d": "2019-07-12",
      "m1": "25.32"
    },
    {
      "p": "[The relativistic discriminator: a key element missing from standard GAN](http://arxiv.org/abs/1807.00734v3)",
      "c": "[&check;&nbsp;Link](https://github.com/eriklindernoren/PyTorch-GAN)",
      "n": "RSGAN-GP",
      "d": "2018-07-02",
      "m1": "25.60"
    },
    {
      "p": "[Gradient penalty from a maximum margin perspective](https://arxiv.org/abs/1910.06922v2)",
      "c": "[&check;&nbsp;Link](https://github.com/lucidrains/stylegan2-pytorch)",
      "n": "HingeGAN",
      "d": "2019-10-15",
      "m1": "27.12"
    },
    {
      "p": "[First Order Generative Adversarial Networks](http://arxiv.org/abs/1802.04591v2)",
      "c": "[&check;&nbsp;Link](https://github.com/zalandoresearch/first_order_gan)",
      "n": "FOGAN",
      "d": "2018-02-13",
      "m1": "27.4"
    },
    {
      "p": "[Mode Seeking Generative Adversarial Networks for Diverse Image Synthesis](https://arxiv.org/abs/1903.05628v6)",
      "c": "[&check;&nbsp;Link](https://github.com/HelenMao/MSGAN)",
      "n": "MSGAN",
      "d": "2019-03-13",
      "m1": "28.73"
    },
    {
      "p": "[Improved Training of Wasserstein GANs](http://arxiv.org/abs/1704.00028v3)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "WGAN-GP",
      "d": "2017-03-31",
      "m1": "29.3"
    },
    {
      "p": "[Quaternion Generative Adversarial Networks](https://arxiv.org/abs/2104.09630v2)",
      "c": "[&check;&nbsp;Link](https://github.com/eleGAN23/QVAE)",
      "n": "QSNGAN",
      "d": "2021-04-19",
      "m1": "31.966"
    },
    {
      "p": "[NVAE: A Deep Hierarchical Variational Autoencoder](https://arxiv.org/abs/2007.03898v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/NVAE)",
      "n": "NVAE w/ flow",
      "d": "2020-07-08",
      "m1": "32.53"
    },
    {
      "p": "[Densely connected normalizing flows](https://arxiv.org/abs/2106.04627v3)",
      "c": "[&check;&nbsp;Link](https://github.com/matejgrcic/DenseFlow)",
      "n": "DenseFlow-74-10",
      "d": "2021-06-08",
      "m1": "34.90"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "ACGAN",
      "d": null,
      "m1": "35.47"
    },
    {
      "p": "[Deep Polynomial Neural Networks](https://arxiv.org/abs/2006.13026v2)",
      "c": "[&check;&nbsp;Link](https://github.com/Faceplugin-ltd/FaceRecognition-Android)",
      "n": "ProdPoly no activation functions",
      "d": "2020-06-20",
      "m1": "40.45"
    },
    {
      "p": "[Generative Latent Flow](https://arxiv.org/abs/1905.10485v2)",
      "c": "[&check;&nbsp;Link](https://github.com/rakhimovv/GenerativeLatentFlow)",
      "n": "GLF+perceptual loss (ours)",
      "d": "2019-05-24",
      "m1": "44.6"
    },
    {
      "p": "[Residual Flows for Invertible Generative Modeling](https://arxiv.org/abs/1906.02735v6)",
      "c": "[&check;&nbsp;Link](https://github.com/rtqichen/residual-flows)",
      "n": "Residual Flow",
      "d": "2019-06-06",
      "m1": "46.37"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "RESFLOW",
      "d": null,
      "m1": "48.29"
    },
    {
      "p": "[Prescribed Generative Adversarial Networks](https://arxiv.org/abs/1910.04302v1)",
      "c": "[&check;&nbsp;Link](https://github.com/adjidieng/PresGANs)",
      "n": "PresGAN",
      "d": "2019-10-09",
      "m1": "52.202"
    },
    {
      "p": "[Large Scale GAN Training for High Fidelity Natural Image Synthesis](http://arxiv.org/abs/1809.11096v2)",
      "c": "[&check;&nbsp;Link](https://github.com/ajbrock/BigGAN-PyTorch)",
      "n": "BigGAN",
      "d": "2018-09-28",
      "m2": "9.22"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
