
def pad(orig, multiple):
    if orig%multiple == 0:
        return orig
    else:
        return multiple * (orig//multiple + 1)


def np_float_to_bytes(numpy_float):
    # How is this so hard?
    return int((numpy_float).astype(int)).to_bytes(4, byteorder='little')


def bytes_to_int(bytes):
    return int.from_bytes(bytes, byteorder='little')

def is_2d(blockshape):
    if blockshape[0] == 1 or blockshape[1] == 1 or blockshape[2] == 1: # 2d
        return True
    return False


def define_blockshape(bits_per_voxel, blockshape):
    if is_2d(blockshape):
        factor = 2 
    else: # 2D
        factor = 8
        
    if bits_per_voxel == -1:
        bits_per_voxel = 4096 * factor // (blockshape[0] * blockshape[1] * blockshape[2])
    else:
        if blockshape[0] == -1:
            blockshape = (4096 * factor // (blockshape[1] * blockshape[2] * bits_per_voxel), blockshape[1], blockshape[2])
        elif blockshape[1] == -1:
            blockshape = (blockshape[0], 4096 * factor // (blockshape[2] * blockshape[0] * bits_per_voxel), blockshape[2])
        elif blockshape[2] == -1:
            blockshape = (blockshape[0], blockshape[1], 4096 * factor // (blockshape[0] * blockshape[1] * bits_per_voxel))
        else:
            assert(bits_per_voxel * blockshape[0] * blockshape[1] * blockshape[2] == 4096 * factor)
    return bits_per_voxel, blockshape
