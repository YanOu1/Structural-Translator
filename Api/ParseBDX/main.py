import sys
sys.path.append(".")
import Api.ParseBDX.function
import Api.ParseBDX.share
import Api.ParseBDX.indexList
import Api.ParseBDX.unpackData
import Api.ParseBDX.RuntimeIdPalette
import Api.ParseBDX.ContainerIndex
# 载入依赖项





Api.ParseBDX.share.BDXContext = Api.ParseBDX.unpackData.getBDXdata('Api/ParseBDX/input.bdx')
# 取得解压后的 BDX 数据
# 舍弃内部文件头 BDX



authorName = Api.ParseBDX.unpackData.getBDXauthor(Api.ParseBDX.share.BDXContext,0)
Api.ParseBDX.share.BDXContext = Api.ParseBDX.share.BDXContext[authorName[-1]:]
authorName = authorName[0]
# 取得作者之名



Api.ParseBDX.share.pointer = 0
Api.ParseBDX.share.penPos = [0,0,0]
Api.ParseBDX.share.blockPalette = []
Api.ParseBDX.share.resultList = []
Api.ParseBDX.share.runtimeIdsBlockPalette = []
Api.ParseBDX.share.successStates = False
# 初始化


while True:
    if Api.ParseBDX.share.BDXContext[Api.ParseBDX.share.pointer:Api.ParseBDX.share.pointer+1] == b'\x58':
        Api.ParseBDX.share.successStates = True
        break
    # 判断是否需要结束

    Api.ParseBDX.share.functionName = Api.ParseBDX.unpackData.getType(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)
    if Api.ParseBDX.share.functionName == False:
        break
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.functionName[-1]
    Api.ParseBDX.share.operation = Api.ParseBDX.share.functionName[1]
    operationNum = Api.ParseBDX.share.functionName[2]
    Api.ParseBDX.share.functionName = Api.ParseBDX.share.functionName[0]
    # 取得函数名、操作编号的 Bytes 及 Int 形式
    # 若 Api.ParseBDX.unpackData.getType 返回 False ，则表明文件可能已损坏

    exec(f'Api.ParseBDX.function.{Api.ParseBDX.indexList.indexListforMain[operationNum]}()')
    # 解析 Operation



if authorName == '':
    print('作者未定义.')
else:
    print('作者之名: ' + authorName)
if Api.ParseBDX.share.successStates == False:
    print('文件不完整或已损坏.')
if Api.ParseBDX.share.successStates == True:
    print('文件完整.')
# 打印作者名称及文件完整结论
with open("Api/ParseBDX/ans.json","w+",encoding='utf-8') as file:
    import json
    file.write(json.dumps(Api.ParseBDX.share.resultList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
# 输出结果
print('SUCCESS - 已成功解析目标文件，已保存在 Api/ParseBDX/ans.json 下.')
# 打印解析结果