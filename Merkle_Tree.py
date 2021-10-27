# This is a code example for the Merkle tree hash algorithm which has been used mostly in p2p 
# networking apps as well as in detecting changes in files or data blocks. 

# This is an implementation of the Merkle Tree hash aglorithm.

import hashlib
import uuid

class MerkleTreeHash(object):
    def __init__(self):
        pass

    def find_merkle_hash(self,file_hashes):
        # We want to find the Merkle tree hash of all of the file hashes passed to this function. 
        # Using recursion to solve this problem. 
        blocks = []
        if not file_hashes:
            raise ValueError('Missing the required file hashes for computing the Merkle Tree.')

        # Sorting the hashes.
        for m in sorted(file_hashes):
            blocks.append(m)
        
        # adjusting the block of hashes until we have an even number of items in the blocks, meaning, append to the end of the block.
        length_list = len(blocks)
        
        # Use modulus math to determine when we have an even number of items in the block. 
        while length_list % 2 !=0: 
            blocks.extend(blocks[-1:])
            length_list = len(blocks)

        # After knowing we have an even number of items, we need to group the items into two's.
        secondary = []
        for k in [blocks[x:x+2] for x in range(0,len(blocks), 2)]:
            # k is a list with only two items to concatenate them and create a new hash. 
            hasher = hashlib.sha256()
            print(hasher)
            # hasher2 = hasher.encode('utf-8')
            # hasher.update(k[0]+k[1])      // TypeError: Unicode-objects must be encoded before hashing
            secondary.append(hasher.hexdigest())

        # since this is a recursive method, determine when there is only a single item in the list. this marks the end of the
        # iteration and we can then return the last hash as the Merkle root.

        if len(secondary)== 1:
            # return the first 64 characters, but you can return the entire hash by removing "[0:64]"
            return secondary[0][0:64]
        else:
            # If the length is greater than 1, then pass the secondary list back into the iteration. 
            return self.find_merkle_hash(secondary)

if __name__ == '__main__':
    file_hashes = []
    for i in range(0,13):
        file_hashes.append(str(uuid.uuid4().hex))
    print('Find the Merkle Tree hash of {0} random hashes' .format(len(file_hashes)))

    cls = MerkleTreeHash()
    mk = cls.find_merkle_hash(file_hashes)
    print('The Merkle tree hash of the hashes below is: {0}'.format(mk))
    print('...')
    print(file_hashes)


    
