# Ethereum Blockchain Ballot System dApp
Th objective is to build a blockchain ballot system to allow voters (Ethereum addresses) to vote for one out of 4 proposals. The chairperson of the ballot will register voters thus giving them the right to vote.

The number of voters is limited to the default number of public addresses provided by the Ganache-CLI. 

The 4 proposals registered voters will vote on are:
- Financial Programming
- Machine Learning Applications in Finance
- Blockchain and Cryptocurrency
- FinTech Bootcamp
## User story
- The chairperson registers a voter using their Ethereum smart contract
- Registration will give the user one and only one vote
- Only a register voter is allowed to vote
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
- winningProposal: get the winning proposal
- getCount: get the number of votes per proposals on a the ballot

2. Smart contract compilation and deployment

Python package solc is used  to compile and deploy the smart contract. The contract is deployed on Ganache-CLI blockchain. Users interact with the Smart contract using a web interface.

The module deploy_contract.py compiles and deploys the Smart contract on Ganache-CLI

Users interact with Ganache-CLI using Python app with Web3.py
(insert image of gaanche-cli)

### Front-end development
Based on Python Flask Framework
Allows users to interact with the dApp  Implemented modules:
- index.html module: Web interface landing page displaying the actions available to the user
- home.html module: Allows user to go back to the landing page after performing an action
- register.html module: Pass voter address to dApp for registration
- registered.html module: Displays registration confirmation page
- vote.html module: Pass voter selected proposal to dApp for validating the choice
- voted.html module: Display the confirmation page of the vote
- winningProposal.html module: Pass the request to dApp to fetch the winning proposal
- winner.html module: Display the winning proposal
- count.html function: Pass the request to dApp to the number of voters per proposal
- getCountresult.html module: Display the number of voters per proposal
![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/b98691fe-a78b-4f05-ae3c-06f74a93ef92)


### Backend interface
This is the dApp engine, it  allows interaction between the deployed contract and the front-end interface. 
1. deployconract.py module: 
- Compile and deploy the contract on Ganache local blockchain
- Make the ABI and BYCODE available to the main dApp.y engine
2. dapp.py module: Main dApp engine
- register function: Build the web form to get user registration data
- registered function: Execute registration on the blockchain and pass the result to the front-end for display
- vote function: Build the web form to get  voter address and choice of proposal
- voted function: Execute the vote on the blockchain and pass the result to the front-end for display
- winningProposal function: Build the form to fetch the winning proposal
- winner function: Execute the request on the blockchain to get the winning proposal
- count function: Build the request to get the  number of voters per proposal
- getCountresult function: : Execute the request on the blockchain to get the number of vote per proposal
 
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
(insert screenshot of running the app)

## Technology
- Python Flask Framework
- solc solidity compiler
- web3
- ganache-cli
- ??? more...

## License

MIT
