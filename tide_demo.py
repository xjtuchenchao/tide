import urllib.request # For downloading the sample Mask R-CNN annotations

# bbox_file = 'mask_rcnn_bbox.json'
# mask_file = 'mask_rcnn_mask.json'

# urllib.request.urlretrieve('https://dl.fbaipublicfiles.com/detectron/35861795/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_1x.yaml.02_31_37.KqyEK4tT/output/test/coco_2014_minival/generalized_rcnn/bbox_coco_2014_minival_results.json', bbox_file)
# urllib.request.urlretrieve('https://dl.fbaipublicfiles.com/detectron/35861795/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_1x.yaml.02_31_37.KqyEK4tT/output/test/coco_2014_minival/generalized_rcnn/segmentations_coco_2014_minival_results.json', mask_file)

# print('Results Downloaded!')

from tidecv import TIDE
import tidecv.datasets as datasets


bbox_file = 'mask_rcnn_bbox.json'

# Loads ground truth from a COCO-style annotation file.
# (path:str=None, name:str=None, year:int=2017, ann_set:str='val', force_download:bool=False)
gt = datasets.COCO()    # 给定参数指明我们的annotation的路径

# Loads predictions from a COCO-style results file.
bbox_results = datasets.COCOResult(bbox_file)

tide = TIDE()
tide.evaluate_range(gt, bbox_results, mode=TIDE.BOX)
tide.summarize()

tide.plot(out_dir='demo')