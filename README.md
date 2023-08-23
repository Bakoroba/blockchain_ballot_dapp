# Ethereum Blockchain Ballot System dApp
The objective is to build a blockchain ballot system to allow voters (Ethereum addresses) to vote for one out of 4 proposals. The chairperson of the ballot will register voters thus giving them the right to vote.

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

Ganache-cli is the provider interface to be used for Web3
![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/8646dd51-24c3-461d-a3a6-7ba8a801dce2)


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

![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/54aaf558-71dd-4fd9-b4d1-c72a73b2d53c)


### Backend interface
This is the dApp engine, it  allows interaction between the deployed contract and the front-end interface. 
1. deployconract.py module: 
- Compile and deploy the contract on Ganache local blockchain
- Make the ABI and BYTECODE available to the main dApp.y engine
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
  ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/ca508a20-8775-4cd5-9022-5f28b134234e)

  ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/17bc50a3-6b7b-49b5-9e47-12080c523fc8)

- Use a registered wallet address to vote on only one of the proposals
  To vote (i) Select vote (ii) Select a registered user (iii) select the proposal to vote for (iv) click on 'Vote' (v)    vote 
  confirmation is displayed on the browser

   ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/a8f22206-fe36-4016-b1ce-29bd9f667b9f)

  ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/77301f7d-1b13-49c3-a48b-2d21ac35c05d)


- Get the total number of vote per proposals
  To get the total number of vote per proposal (i) click on 'GET Number of vote per proposals' (ii) The number of vote per proposal is displayed in the browser

  ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/c03ab8aa-89c6-426b-b803-1dc63cedca6f)

  ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/9702653a-de5e-448e-820e-51448119600d)


- Get the winning proposal
    To get the winning proposal (i) click on 'GET winning' (ii) The winning proposal is displayed in the browser
 ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/5ced1947-75bb-4575-a131-d13666be31a3)

 ![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/9c513205-aa6e-48f5-a5c7-44dcbf841c64)

 
## Installation

Linux environment is required for installation. Ubuntu is used for this case. To install clone the repository to your local machine. Follow these steps o run:
i. Open a terminal and launch ganache-cli: ganache-cli
ii. Open a second terminal and launch the: pyhton3 dapp.py
iii. Open a browser and go to the loopback address 12.7.0.0.1:5000
(insert screenshot of running the app)
![image](https://github.com/Bakoroba/blockchain_ballot_dapp/assets/7796158/1355b212-b1d9-43cd-a18a-6db2898fc257)


## Technology
- Python Flask Framework
- solc solidity compiler
- web3
- ganache-cli


## Contributors

-Name: Bakary Sylla, Marcus LeGare, Cherryl Adzang, Yadisa Joiner, and John Nguyen

## License
MIT
