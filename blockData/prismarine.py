import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["prismarine_block_type:8"]
    #
    if type == 'default':
        return 0
    if type == 'dark':
        return 1
    if type == 'bricks':
        return 2
    #