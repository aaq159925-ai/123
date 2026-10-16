# Dataset provenance and preprocessing

## Upstream 10-class export

The upstream dataset is `datasets/upstream/HanYang+wuhan_10_2755/`. Its original `README.roboflow.txt` records:

- exported from Roboflow on 2022-03-30 at 05:53 GMT;
- 2,755 images in YOLO v5 PyTorch format;
- EXIF auto-orientation with orientation metadata stripped;
- stretch resize to 640 by 640 pixels;
- no offline image augmentation.

Upstream classes:

```text
0 albi, 1 cedr, 2 cinn, 3 gink, 4 koel,
5 magn, 6 meta, 7 plat, 8 sali, 9 sapi
```

## Derived 9-class training dataset

The actual experiment dataset is `datasets/new-wuhan/`. Direct label comparison shows this transformation:

1. remove upstream class 6 (`meta`) annotations;
2. remap upstream IDs 7, 8, 9 to IDs 6, 7, 8;
3. retain the original train/validation/test image split;
4. remove eight JSON files mixed into the upstream test image folder.

Removed `meta` boxes:

| Split | Boxes removed |
| --- | ---: |
| train | 36 |
| valid | 14 |
| test | 5 |
| total | 55 |

Derived classes:

```text
0 albi, 1 cedr, 2 cinn, 3 gink, 4 koel,
5 magn, 6 plat, 7 sali, 8 sapi
```

Use `project/ultralytics/cfg/datasets/WuHanl.yaml` for the historical 9-class experiment. Dataset-root `data.yaml` files contain stale paths and are retained only as provenance.

## Online training augmentation

Saved effective settings:

```yaml
hsv_h: 0.015
hsv_s: 0.7
hsv_v: 0.4
translate: 0.1
scale: 0.5
fliplr: 0.5
mosaic: 1.0
close_mosaic: 10
mixup: 0.0
copy_paste: 0.0
degrees: 0.0
shear: 0.0
perspective: 0.0
flipud: 0.0
```

Roboflow applied no offline augmentation; YOLO applied online HSV, translation, scale, horizontal flip, and Mosaic during training. Saved `augment: false` is an inference/validation option and does not disable these training augmentations.
