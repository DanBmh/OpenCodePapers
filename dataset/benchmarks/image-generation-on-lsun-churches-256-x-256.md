# image-generation-on-lsun-churches-256-x-256

[Dataset Link](https://www.yf.io/p/lsun) \
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
      "label": "Clean-FID (trainfull)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "NFE",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "Recall",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "clean-FID",
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
      "p": "[Projected GANs Converge Faster](https://arxiv.org/abs/2111.01007v1)",
      "c": "[&check;&nbsp;Link](https://github.com/autonomousvision/projected_gan)",
      "n": "Projected GAN",
      "d": "2021-11-01",
      "m1": "1.59"
    },
    {
      "p": "[Ensembling Off-the-shelf Models for GAN Training](https://arxiv.org/abs/2112.09130v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nupurkmr9/vision-aided-gan)",
      "n": "Vision-aided GAN",
      "d": "2021-12-16",
      "m1": "1.72",
      "m2": "1.72 \u00b1 0.01"
    },
    {
      "p": "[Diffusion-GAN: Training GANs with Diffusion](https://arxiv.org/abs/2206.02262v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Zhendong-Wang/Diffusion-GAN)",
      "n": "Diffusion ProjectedGAN",
      "d": "2022-06-05",
      "m1": "1.85"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "Patch Diffusion",
      "d": null,
      "m1": "2.66"
    },
    {
      "p": "[Image Generators with Conditionally-Independent Pixel Synthesis](https://arxiv.org/abs/2011.13775v1)",
      "c": "[&check;&nbsp;Link](https://github.com/saic-mdal/CIPS)",
      "n": "CIPS",
      "d": "2020-11-27",
      "m1": "2.92"
    },
    {
      "p": "[StyleSwin: Transformer-based GAN for High-resolution Image Generation](https://arxiv.org/abs/2112.10762v2)",
      "c": "[&check;&nbsp;Link](https://github.com/microsoft/StyleSwin)",
      "n": "StyleSwin",
      "d": "2021-12-20",
      "m1": "2.95"
    },
    {
      "p": "[Diffusion-GAN: Training GANs with Diffusion](https://arxiv.org/abs/2206.02262v4)",
      "c": "[&check;&nbsp;Link](https://github.com/Zhendong-Wang/Diffusion-GAN)",
      "n": "Diffusion StyleGAN2",
      "d": "2022-06-05",
      "m1": "3.17"
    },
    {
      "p": "[StyleNAT: Giving Each Head a New Perspective](https://arxiv.org/abs/2211.05770v2)",
      "c": "[&check;&nbsp;Link](https://github.com/SHI-Labs/Neighborhood-Attention-Transformer)",
      "n": "StyleNAT",
      "d": "2022-11-10",
      "m1": "3.4"
    },
    {
      "p": "[CLR-GAN: Improving GANs Stability and Quality via Consistent Latent Representation and Reconstruction](https://link.springer.com/chapter/10.1007/978-3-031-73232-4_12)",
      "c": "[&check;&nbsp;Link](https://github.com/Petecheco/CLR-GAN)",
      "n": "CLR-GAN",
      "d": "2024-09-30",
      "m1": "3.43",
      "m4": "0.48"
    },
    {
      "p": "[Analyzing and Improving the Image Quality of StyleGAN](https://arxiv.org/abs/1912.04958v2)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "StyleGAN2",
      "d": "2019-12-03",
      "m1": "3.86",
      "m2": "4.28 \u00b1 0.03"
    },
    {
      "p": "[Polarity Sampling: Quality and Diversity Control of Pre-Trained Generative Networks via Singular Values](https://arxiv.org/abs/2203.01993v2)",
      "c": "[&check;&nbsp;Link](https://github.com/AhmedImtiazPrio/magnet-polarity)",
      "n": "Polarity-StyleGAN2",
      "d": "2022-03-03",
      "m1": "3.92"
    },
    {
      "p": "[Truncated Diffusion Probabilistic Models and Diffusion-based Adversarial Auto-Encoders](https://arxiv.org/abs/2202.09671v4)",
      "c": "[&check;&nbsp;Link](https://github.com/jegzheng/truncated-diffusion-probabilistic-models)",
      "n": "TDPM+ (TTrunc=99)",
      "d": "2022-02-19",
      "m1": "3.98",
      "m3": "100"
    },
    {
      "p": "[Adversarial Generation of Continuous Images](https://arxiv.org/abs/2011.12026v2)",
      "c": "[&check;&nbsp;Link](https://github.com/universome/inr-gan)",
      "n": "INR-GAN-bil",
      "d": "2020-11-24",
      "m1": "4.04"
    },
    {
      "p": "[Unleashing Transformers: Parallel Token Prediction with Discrete Absorbing Diffusion for Fast High-Resolution Image Generation from Vector-Quantized Codes](https://arxiv.org/abs/2111.12701v1)",
      "c": "[&check;&nbsp;Link](https://github.com/samb-t/unleashing-transformers)",
      "n": "Unleashing Transformers",
      "d": "2021-11-24",
      "m1": "4.07"
    },
    {
      "p": "[A Style-Based Generator Architecture for Generative Adversarial Networks](http://arxiv.org/abs/1812.04948v3)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/stylegan)",
      "n": "StyleGAN",
      "d": "2018-12-12",
      "m1": "4.21",
      "m2": "4.75 \u00b1 0.01"
    },
    {
      "p": "[SWAGAN: A Style-based Wavelet-driven Generative Model](https://arxiv.org/abs/2102.06108v1)",
      "c": "[&check;&nbsp;Link](https://github.com/rinongal/swagan)",
      "n": "SWAGAN-Bi",
      "d": "2021-02-11",
      "m1": "4.97"
    },
    {
      "p": "[Wavelet Diffusion Models are fast and scalable Image Generators](https://arxiv.org/abs/2211.16152v2)",
      "c": "[&check;&nbsp;Link](https://github.com/vinairesearch/wavediff)",
      "n": "WaveDiff",
      "d": "2022-11-29",
      "m1": "5.06",
      "m3": "4",
      "m4": "0.40"
    },
    {
      "p": "[MSG-GAN: Multi-Scale Gradients for Generative Adversarial Networks](https://arxiv.org/abs/1903.06048v4)",
      "c": "[&check;&nbsp;Link](https://github.com/akanimax/BMSG-GAN)",
      "n": "MSG-StyleGAN",
      "d": "2019-03-14",
      "m1": "5.2",
      "m2": "5.38 \u00b1 0.03"
    },
    {
      "p": "[Tackling the Generative Learning Trilemma with Denoising Diffusion GANs](https://arxiv.org/abs/2112.07804v2)",
      "c": "[&check;&nbsp;Link](https://github.com/NVlabs/denoising-diffusion-gan)",
      "n": "DDGAN",
      "d": "2021-12-15",
      "m1": "5.25"
    },
    {
      "p": "[Flow Matching in Latent Space](https://arxiv.org/abs/2307.08698v1)",
      "c": "[&check;&nbsp;Link](https://github.com/vinairesearch/lfm)",
      "n": "LFM",
      "d": "2023-07-17",
      "m1": "5.54"
    },
    {
      "p": "[Progressive Growing of GANs for Improved Quality, Stability, and Variation](http://arxiv.org/abs/1710.10196v3)",
      "c": "[&check;&nbsp;Link](https://github.com/tkarras/progressive_growing_of_gans)",
      "n": "PGGAN",
      "d": "2017-10-27",
      "m1": "6.42",
      "m2": "6.43 \u00b1 0.05"
    },
    {
      "p": "[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239v2)",
      "c": "[&check;&nbsp;Link](https://github.com/labmlai/annotated_deep_learning_paper_implementations)",
      "n": "Denoising Diffusion Probabilistic Model",
      "d": "2020-06-19",
      "m1": "7.89"
    },
    {
      "p": "[Pseudo Numerical Methods for Diffusion Models on Manifolds](https://arxiv.org/abs/2202.09778v2)",
      "c": "[&check;&nbsp;Link](https://github.com/sanster/lama-cleaner)",
      "n": "PNDM",
      "d": "2022-02-20",
      "m1": "8.69"
    },
    {
      "p": "[TransGAN: Two Pure Transformers Can Make One Strong GAN, and That Can Scale Up](https://arxiv.org/abs/2102.07074v4)",
      "c": "[&check;&nbsp;Link](https://github.com/VITA-Group/TransGAN)",
      "n": "TransGAN",
      "d": "2021-02-14",
      "m1": "8.94"
    },
    {
      "p": "[Gotta Go Fast When Generating Data with Score-Based Models](https://arxiv.org/abs/2105.14080v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AlexiaJM/score_sde_fast_sampling)",
      "n": "VE (erel=0.01)",
      "d": "2021-05-28",
      "m1": "26.46"
    },
    {
      "p": "[Gotta Go Fast When Generating Data with Score-Based Models](https://arxiv.org/abs/2105.14080v1)",
      "c": "[&check;&nbsp;Link](https://github.com/AlexiaJM/score_sde_fast_sampling)",
      "n": "VE (erel=0.02)",
      "d": "2021-05-28",
      "m1": "26.46"
    },
    {
      "p": "[Bellman Optimal Stepsize Straightening of Flow-Matching Models](https://arxiv.org/abs/2312.16414v3)",
      "c": "[&check;&nbsp;Link](https://github.com/nguyenngocbaocmt02/boss)",
      "n": "BOSS",
      "d": "2023-12-27",
      "m5": "13.21"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
