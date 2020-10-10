from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - datasets of transactions.
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming chain if the following rules apply:
        - the incoming chain must be longer than the local one
        - the incoming chain if formatted properly
        """
        if len(chain) <= len(self.chain):
            raise Exception(
                'Cannot replace. The incoming chain must be longer.')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(
                f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = chain

    def to_json(self):
        """
        Serialize the blockchain into a list of blocks.
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the bockchain:
        - the chain must start with the genesis block
        - blocks must be formatted correctly
        """

        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        # Skip the genesis block
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


def main():
    bc = Blockchain()
    bc.add_block('one')
    bc.add_block('two')
    print(bc)


if (__name__ == '__main__'):
    main()
