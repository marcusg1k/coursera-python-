def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size

    partial_block_remainder = filesize % block_size

    if partial_block_remainder > 0: 
        return block_size * (full_blocks + 1) 
    return block_size * full_blocks