# blockchain_ballot_dapp
# Ethereum Blockchain Ballot System dApp
Th objective is to build a blockchain ballot system to allow voters (Ethereum addresses) to vote for one out of 4 proposals. The chairperson of the ballot will register voters thus giving them the right to vote.

The number of voters is limited to the default number of public addresses provided by the Ganache-CLI. 

The 4 proposals registered voters will vote on are:
i.   Financial Programming
ii.  Machine Learning Applications in Finance
iii. Blockchain and Cryptocurrency
iv.  FinTech Bootcamp
## User story
- The chairperson registers a voter using their Ethereum smart contract
- Registration will give the user one and only one vote
- Only A register voter is allowed to vote
- The voter can vote for only one of the 4 proposals on the ballot
- The number of voters is only limited by the number of Ethereum addresses on Ganache-CLI blockchain
- The ballot chairperson can get the total number of vote per proposals
- The ballot chairperson can find out the winning proposal

## Functional components
### Smart contract
1. Smart Contract code
The smart contract is written using Solidity language. The contract has the following functions:
- register: register a voter so that they have a right to vote a voter
- vote: allows a voter to vote for a single proposal
- wininngProposal: get the winning proposal
- getCount: get the number of votes per proposals on a the ballot

2. Smart contract compilation and deployment

Python package solc is used  to compile and deploy the smart contract. The contract is deployed on Ganache-CLI blockchain. Users interact with the Smart contract using a web interface.

The module deploy_contract.py compiles and deploys the Smart contract on Ganache-CLI

### Web3
Users interact with Ganache-CLI using Python app with Web3.py

### User web interface development
Python Flask Framework is used to build a web interface that allows users to exercise the dApp functionality. The web interface has the following features:

dapp.py is the main app that allows users to interact with the deployed smart contract. It has the following functions:
- register function: GET data form register.html page.
- registered function: POST data to registered.html page
- vote function: GET data from vote.html page.
- registered function: POST data to registered.html page
- winningProposal
- winner
- count function
- getCountresult function

allow users to register 
### Web UI to interact with the smart contract
- Register a wallet address
  To register a voter (i) Click on 'Register' (ii) select the appropriate address from the dropdown menu and click on 'Register'
  button (iii) the registration confirmation is displayed on the browser
  (insert 3 images)
- Use a registered wallet address to vote on only one of the proposals
  To vote (i) Select vote (ii) Select a registered user (iii) select the proposal to vote for (iv) click on 'Vote' (v)    vote 
  confirmation is displayed on the browser
  (insert 3 images)
- Get the total number of vote per proposals
  To get the total number of vote per proposal (i) click on 'GET Number of vote per proposals' (ii) The number of vote per proposal is displayed in the browser
  (insert 2 images)
  
- Get the winning proposal
    To get the winning proposal (i) click on 'GET winning' (ii) The winning proposal is displayed in the browser
  (insert 2 images)
)
## Installation

Linux environment is required for installation. Ubuntu is used for this case. To install clone the repository to your local machine. Follow these steps o run:
i. Open a terminal and launch ganache-cli: ganache-cli
ii. Open a second terminal and launch the: pyhton3 dapp.py
iii. Open a browser and go to the loopback address 12.7.0.0.1:5000

## Packages used
- Python Flask Framework
- solc
- web3
- ganache-cli
- ??? more...
