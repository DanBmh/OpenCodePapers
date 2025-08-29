# bird-s-eye-view-semantic-segmentation-on

[Dataset Link](https://www.nuscenes.org/) \
Task Hierarchy: ["Bird's-Eye View Semantic Segmentation"]

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
      "label": "IoU veh - 224x480 - Vis filter. - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "IoU veh - 448x800 - Vis filter. - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "IoU veh - 224x480 - No vis filter - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "IoU veh - 448x800 - No vis filter - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m5",
      "label": "IoU ped - 224x480 - Vis filter. - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m6",
      "label": "IoU lane - 224x480 - 100x100 at 0.5",
      "sortable": "true"
    },
    {
      "key": "m7",
      "label": "IoU veh - 224x480 - No vis filter - 100x50 at 0.25",
      "sortable": "true"
    },
    {
      "key": "m8",
      "label": "IoU vehicle - Setting 3",
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
      "p": "[PointBeV: A Sparse Approach to BeV Predictions](https://arxiv.org/abs/2312.00703v2)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/pointbev)",
      "n": "PointBeV",
      "d": "2023-12-01",
      "m1": "44.7",
      "m2": "48.7",
      "m3": "39.9",
      "m4": "43.2",
      "m5": "19.9"
    },
    {
      "p": "[PointBeV: A Sparse Approach to BeV Predictions](https://arxiv.org/abs/2312.00703v2)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/pointbev)",
      "n": "PointBeV (static)",
      "d": "2023-12-01",
      "m1": "44.0",
      "m2": "47.6",
      "m3": "38.7",
      "m4": "42.1",
      "m5": "18.5",
      "m6": "49.6"
    },
    {
      "p": "[Simple-BEV: What Really Matters for Multi-Sensor BEV Perception?](https://arxiv.org/abs/2206.07959v2)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/pointbev)",
      "n": "Simple-BEV",
      "d": "2022-06-16",
      "m1": "43.0",
      "m2": "46.6",
      "m3": "36.9",
      "m4": "40.9"
    },
    {
      "p": "[BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers](https://arxiv.org/abs/2203.17270v2)",
      "c": "[&check;&nbsp;Link](https://github.com/fundamentalvision/BEVFormer)",
      "n": "BEVFormer",
      "d": "2022-03-31",
      "m1": "42.0",
      "m2": "45.5",
      "m3": "35.8",
      "m4": "39.0",
      "m6": "25.7"
    },
    {
      "p": "[FIERY: Future Instance Prediction in Bird's-Eye View from Surround Monocular Cameras](https://arxiv.org/abs/2104.10490v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wayveai/fiery)",
      "n": "FIERY (static)",
      "d": "2021-04-21",
      "m1": "39.8",
      "m3": "35.8",
      "m5": "17.2"
    },
    {
      "p": "[BAEFormer: Bi-Directional and Early Interaction Transformers for Bird's Eye View Semantic Segmentation](http://openaccess.thecvf.com//content/CVPR2023/html/Pan_BAEFormer_Bi-Directional_and_Early_Interaction_Transformers_for_Birds_Eye_View_CVPR_2023_paper.html)",
      "c": "",
      "n": "BAEFormer",
      "d": "2023-01-01",
      "m1": "38.9",
      "m2": "41.0",
      "m3": "36",
      "m4": "37.8"
    },
    {
      "p": "[LaRa: Latents and Rays for Multi-Camera Bird's-Eye-View Semantic Segmentation](https://arxiv.org/abs/2206.13294v2)",
      "c": "[&check;&nbsp;Link](https://github.com/valeoai/LaRa)",
      "n": "LaRa",
      "d": "2022-06-27",
      "m1": "38.9",
      "m3": "35.4"
    },
    {
      "p": "[Cross-view Transformers for real-time Map-view Semantic Segmentation](https://arxiv.org/abs/2205.02833v1)",
      "c": "[&check;&nbsp;Link](https://github.com/bradyz/cross_view_transformers)",
      "n": "CVT",
      "d": "2022-05-05",
      "m1": "36.0",
      "m2": "37.7",
      "m3": "31.4",
      "m4": "32.5"
    },
    {
      "p": "[FIERY: Future Instance Prediction in Bird's-Eye View from Surround Monocular Cameras](https://arxiv.org/abs/2104.10490v3)",
      "c": "[&check;&nbsp;Link](https://github.com/wayveai/fiery)",
      "n": "FIERY",
      "d": "2021-04-21",
      "m3": "38.2",
      "m7": "41.1",
      "m8": "58.5"
    },
    {
      "p": "[TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving](https://arxiv.org/abs/2303.09998v2)",
      "c": "",
      "n": "TBP-Former",
      "d": "2023-03-17",
      "m5": "18.6"
    },
    {
      "p": "[TBP-Former: Learning Temporal Bird's-Eye-View Pyramid for Joint Perception and Prediction in Vision-Centric Autonomous Driving](https://arxiv.org/abs/2303.09998v2)",
      "c": "",
      "n": "TBP-Former (static)",
      "d": "2023-03-17",
      "m5": "17.2"
    },
    {
      "p": "[Lift, Splat, Shoot: Encoding Images From Arbitrary Camera Rigs by Implicitly Unprojecting to 3D](https://arxiv.org/abs/2008.05711v1)",
      "c": "[&check;&nbsp;Link](https://github.com/nv-tlabs/lift-splat-shoot)",
      "n": "Lift-Splat-Shoot",
      "d": "2020-08-13",
      "m5": "15.0"
    },
    {
      "p": "[ST-P3: End-to-end Vision-based Autonomous Driving via Spatial-Temporal Feature Learning](https://arxiv.org/abs/2207.07601v2)",
      "c": "[&check;&nbsp;Link](https://github.com/opendrivelab/st-p3)",
      "n": "ST-P3",
      "d": "2022-07-15",
      "m5": "14.5"
    },
    {
      "p": "[PETRv2: A Unified Framework for 3D Perception from Multi-Camera Images](https://arxiv.org/abs/2206.01256v3)",
      "c": "[&check;&nbsp;Link](https://github.com/megvii-research/petr)",
      "n": "PETRv2",
      "d": "2022-06-02",
      "m6": "44.8"
    },
    {
      "p": "[MatrixVT: Efficient Multi-Camera to BEV Transformation for 3D Perception](https://arxiv.org/abs/2211.10593v1)",
      "c": "[&check;&nbsp;Link](https://github.com/megvii-basedetection/bevdepth)",
      "n": "MatrixVT",
      "d": "2022-11-19",
      "m6": "44.8"
    },
    {
      "p": "[]()",
      "c": "",
      "n": "M^2BEV",
      "d": null,
      "m6": "38.0"
    },
    {
      "p": "[Monocular Semantic Occupancy Grid Mapping with Convolutional Variational Encoder-Decoder Networks](http://arxiv.org/abs/1804.02176v3)",
      "c": "",
      "n": "VED",
      "d": "2018-04-06",
      "m7": "8.8"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
