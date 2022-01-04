import pickle,json

# data = dict(name='Bob', age=25, score=88)
# pickle_dumps = pickle.dumps(data)
# with open('demo.pkl', 'wb') as f:
#     f.write(pickle_dumps)
# with open('demo.pkl', 'rb') as f:
#     data = pickle.load(f)
# print(f'pickle file:{data}')

# json_dumps = json.dumps(data)
# print(f'json_dumps:{json_dumps}')
# with open('demo.json', 'w') as f:
#     f.write(json_dumps)
# with open('demo.json', 'r') as f:
#     data = json.load(f)
# print(f'json file:{data}')

# 读取检测结果
with open('lr_0.01_result.pkl', 'rb') as f:
    result = pickle.load(f)
print(result)
# json_result = json.dumps(result)
# with open('lr_0.01_result.json', 'w') as f:
#     f.write(json_result)
# print('Finished!')
    



