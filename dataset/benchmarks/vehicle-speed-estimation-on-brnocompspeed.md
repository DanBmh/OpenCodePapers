# vehicle-speed-estimation-on-brnocompspeed

[Dataset Link](https://github.com/JakubSochor/BrnoCompSpeed) \
Task Hierarchy: ['Video', 'Vehicle Speed Estimation']

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
      "label": "Mean Speed Measurement Error (km/h)",
      "sortable": "true"
    },
    {
      "key": "m2",
      "label": "Median Speed Measurement Error (km/h)",
      "sortable": "true"
    },
    {
      "key": "m3",
      "label": "95-th Percentile Speed Measurement Error (km/h)",
      "sortable": "true"
    },
    {
      "key": "m4",
      "label": "99-th Percentile Speed Measurement Error (km/h)",
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
      "p": "[Detection of 3D Bounding Boxes of Vehicles Using Perspective Transformation for Accurate Speed Measurement](https://arxiv.org/abs/2003.13137v2)",
      "c": "[&check;&nbsp;Link](https://github.com/kocurvik/retinanet_traffic_3D)",
      "n": "Transform3D",
      "d": "2020-03-29",
      "m1": "0.75",
      "m2": "0.58",
      "m3": "1.84"
    },
    {
      "p": "[Perspective transformation for accurate detection of 3D bounding boxes of vehicles in traffic surveillance](https://www.researchgate.net/publication/330913274_Perspective_transformation_for_accurate_detection_of_3D_bounding_boxes_of_vehicles_in_traffic_surveillance)",
      "c": "[&check;&nbsp;Link](https://github.com/kocurvik/CVWW2019_results)",
      "n": "Transform2D",
      "d": "2019-02-08",
      "m1": "0.83",
      "m2": "0.60",
      "m3": "2.04"
    },
    {
      "p": "[Perspective transformation for accurate detection of 3D bounding boxes of vehicles in traffic surveillance](https://www.researchgate.net/publication/330913274_Perspective_transformation_for_accurate_detection_of_3D_bounding_boxes_of_vehicles_in_traffic_surveillance)",
      "c": "[&check;&nbsp;Link](https://github.com/kocurvik/CVWW2019_results)",
      "n": "Transform3D",
      "d": "2019-02-08",
      "m1": "0.86",
      "m2": "0.65",
      "m3": "2.17"
    },
    {
      "p": "[Traffic Surveillance Camera Calibration by 3D Model Bounding Box Alignment for Accurate Vehicle Speed Measurement](http://arxiv.org/abs/1702.06451v2)",
      "c": "",
      "n": "Edgelets + BBScale + reg",
      "d": "2017-02-21",
      "m1": "1.10",
      "m2": "0.97",
      "m4": "3.05"
    }
  ],
  "markdown": "true",
  "caption": "Check out how to [contribute](https://gitlab.com/OpenCodePapers/OpenCodePapers/-/blob/main/CONTRIBUTING.md) new results."
}
```
