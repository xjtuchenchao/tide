from tidecv import TIDE
import tidecv.datasets as datasets

bbox_file = '/shared/xjd/chenchao/mmdetection/work_dirs2/retinanet_transmission_test/custom_lr0.05_data2_newanchor7_5fm.bbox.json'

# Loads ground truth from a COCO-style annotation file.
# (path:str=None, name:str=None, year:int=2017, ann_set:str='val', force_download:bool=False)
gt = datasets.COCO(path='/shared/xjd/DataSets/transmission_line_detection/instances_test.json')    # 给定参数指明我们的annotation的路径

# Loads predictions from a COCO-style results file.
bbox_results = datasets.COCOResult(bbox_file)

tide = TIDE()
tide.evaluate_range(gt, bbox_results, mode=TIDE.BOX)
tide.summarize()

tide.plot(out_dir='demo1')