"""
Deploy Solidity Contract to Ganache-CLI
"""
# Import required libraries for compiling and deploying a smart contract
from solcx import compile_source
from web3 import Web3, HTTPProvider

# set the provider (interface) to be used for web3 (ganache-cli)
WEB3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
#w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# provide the smart contract
CONTRACT_SOURCE_CODE = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract Ballot {

    struct Voter {
        uint weight;
        bool voted;
        uint8 vote;
        // address delegate;
    }

    //modifer
    modifier onlyOwner () {
      require(msg.sender == chairperson);
      _;
    }

    address public chairperson;
    mapping(address => Voter) public voters;
    uint[4] public proposals;

    // Create a new ballot with 4 different proposals.
    function Balloting() public {
        chairperson = msg.sender;
        voters[chairperson].weight = 1;
    }

    // Give a toVoter the right to vote on this ballot.
    // May only be called by chairperson
    function register(address toVoter) public {
        if(voters[toVoter].weight != 0) revert();
        voters[toVoter].weight = 1;
        voters[toVoter].voted = false;
    }

    // Give a single vote to a proposal.
    function vote(uint8 toProposal) public {
        Voter storage sender = voters[msg.sender];
        if(sender.voted || sender.weight == 0) revert();
        sender.voted = true;
        sender.vote = toProposal;
        proposals[toProposal] += sender.weight;
    }
    // Get the winning proposal
    function winningProposal() public view returns (uint8 _winningProposal) {
        uint256 winningVoteCount = 0;
        for (uint8 prop = 0; prop < 4; prop++)
            if (proposals[prop] > winningVoteCount) {
                winningVoteCount = proposals[prop];
                _winningProposal = prop;
            }
    }
    // Get the vote count for each proposal
    function getCount() public view returns (uint[4] memory) {
        return proposals;
    }

}
'''
# compile the solidity source code
COMPILED_SOL = compile_source(CONTRACT_SOURCE_CODE)
# create an interface for the compiled contracct
SMARTCONTRACT_INTERFACE = COMPILED_SOL['<stdin>:Ballot']
#
Ballot = WEB3.eth.contract(
    abi=SMARTCONTRACT_INTERFACE['abi'],
    bytecode=SMARTCONTRACT_INTERFACE['bin'])
# send eth from which account?
WEB3.eth.defaultAccount = WEB3.eth.accounts[0]
address = WEB3.eth.accounts[0]
private_key = "0x52ceaf34e1f36e7f739419ff67d1e0c77f550e455508279442582640015e8140"


nonce = WEB3.eth.get_transaction_count(address)

# build transaction
transaction = Ballot.constructor().build_transaction(
    {
        "chainId": 1337,
        "gasPrice": WEB3.eth.gas_price,
        "from": address,
        "nonce": nonce,
    }
)
# Sign the transaction
sign_transaction = WEB3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
# Send the transaction
TX_HASH = WEB3.eth.send_raw_transaction(sign_transaction.rawTransaction)
# Wait for the transaction to be mined, and get the transaction receipt
print("Waiting for transaction to finish...")
TX_RECEIPT = WEB3.eth.wait_for_transaction_receipt(TX_HASH)
print(f"Done! Contract deployed to {TX_RECEIPT.contractAddress}")

ASSETREGISTER = WEB3.eth.contract(
    # get the contract address from the transaction address
    address=TX_RECEIPT.contractAddress,
    abi=SMARTCONTRACT_INTERFACE['abi'],
)
