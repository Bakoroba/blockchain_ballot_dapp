"""
Decentralized Application
"""
# Flask requirements
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired

import pprint
import numpy
import io
# DAPP Requirements
from hexbytes import HexBytes
from web3.auto import w3
from deploycontract import ASSETREGISTER
from deploycontract import Ballot
from web3 import Web3, HTTPProvider
# set the provider (interface) to be used for web3 (ganache-cli)
WEB3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

APP = Flask(__name__)
BOOTSTRAP = Bootstrap(APP)
APP.config['SECRET_KEY'] = 'TempSecretKey'

# Registration Form for the application
class BuildForm(FlaskForm):
    """
    Drop down form field for choosing the ethereum address.
    SelectField specifies that this will be a drop down field.
    """
    ethereum_address = SelectField('Ethereum Address', choices=[])
    proposals = SelectField('Choose a proposal', choices=[])

# Application routes
@APP.route("/")
def home():
    """
    return the home.html template
    Pass the contract address to the home.html template
    """
    return render_template(
        'home.html',
        contractaddress=ASSETREGISTER.address
    )

@APP.route("/register", methods=['GET'])
def register():
    """
    # pass the register form to the register.html template
    # pass the contract address to the register.html template
    """
    form = BuildForm()
    form.ethereum_address.choices = []
    minus_one = -1
    for chooseaccount in WEB3.eth.accounts:
        minus_one = minus_one+1
        form.ethereum_address.choices += [(minus_one, chooseaccount)]
    return render_template(
        'register.html',
        registerform=form,
        contractaddress=ASSETREGISTER.address
    )
@APP.route("/vote", methods=['GET'])
def vote():
    """

    # pass the vote form to the vote.html template
    # pass the contract address and proposals register.html template
    """
    form = BuildForm()
    form.proposals.choices = ["Financial Programming", "Machine Learning Applications in Finance","Blockchain and Cryptocurrency", "FinTech Bootcamp"]

    form.ethereum_address.choices = []
    minus_one = -1
    for chooseaccount in WEB3.eth.accounts:
        minus_one = minus_one+1
        form.ethereum_address.choices += [(minus_one, chooseaccount)]
        
    return render_template(
        'vote.html',
        voteform=form,
        contractaddress=ASSETREGISTER.address
    
    )
@APP.route("/winningproposal", methods=['GET'])
def winningproposal():
    """

    # pass the winning proposal to winningproposal.html
    # pass the contract address to the register.html template
    """
    form = BuildForm()
    return render_template(
        'winningproposal.html',
        winningproposalform=form,
        contractaddress=ASSETREGISTER.address
    )
@APP.route("/getcount", methods=['GET'])
def getcount():
    """
    # pass the number of vote per proposal to count.html
    """
    form = BuildForm()
    return render_template(
        'getcount.html',
        winningproposalform=form,
        contractaddress=ASSETREGISTER.address
    )
    
@APP.route("/registered", methods=['POST'])
def registered():
    address = WEB3.eth.accounts[0]
    private_key = "0x83036aa7c3ace17b58e64130f313013a3e28a71524d995d2f61d2809ff6a1d13"
   
    # create the transaction
    call_contract_function = ASSETREGISTER.functions.register(
        w3.eth.accounts[int(request.form['ethereum_address'])]).transact({'from':address}) 
    transaction_info = WEB3.eth.get_transaction(call_contract_function)
    return render_template(
        'registered.html',
        # pass these variables to the html template
        reg_ethaddress=WEB3.eth.accounts[int(request.form['ethereum_address'])],
        #reg_serial=request.form['some_string'],
        reg_accountnumber=request.form['ethereum_address'],
        reg_receipt=WEB3.eth.get_transaction_receipt(call_contract_function),
        reg_txhash=HexBytes.hex(transaction_info['hash']),
        reg_txdata=HexBytes(transaction_info['input']),
        contractaddress=ASSETREGISTER.address
    )
@APP.route("/voted", methods=['POST'])
def voted():
    address = WEB3.eth.accounts[0]
    private_key = "0x83036aa7c3ace17b58e64130f313013a3e28a71524d995d2f61d2809ff6a1d13"
   
    if str((request.form['proposals'])) == "Financial Programming":
        proposal = 0
    if str((request.form['proposals'])) == "Machine Learning Applications in Finance":
        proposal = 1
   
    if str((request.form['proposals'])) == "Blockchain and Cryptocurrency":
        proposal = 2
   
    if str((request.form['proposals'])) == "FinTech Bootcamp":
        proposal = 3
    #"Financial Programming", "Machine Learning Applications in Finance","Blockchain and Cryptocurrency", "FinTech Bootcamp")
    
    # create the transaction
    call_contract_function1 = ASSETREGISTER.functions.vote(proposal).transact({'from':address}) 
    transaction_info = WEB3.eth.get_transaction(call_contract_function1)
    return render_template(
        'voted.html',
        # pass these variables to the html template
        reg_ethaddress=address,
        #reg_serial=request.form['some_string'],
        reg_accountnumber=address,
        reg_receipt=WEB3.eth.get_transaction_receipt(call_contract_function1),
        reg_txhash=HexBytes.hex(transaction_info['hash']),
        reg_txdata=HexBytes(transaction_info['input']),
        contractaddress=ASSETREGISTER.address,
        reg_serial = request.form['proposals']
    )
@APP.route("/winner", methods=['POST'])
def winner():
    address = WEB3.eth.accounts[0]
    private_key = "0x83036aa7c3ace17b58e64130f313013a3e28a71524d995d2f61d2809ff6a1d13"
 
    call_contract_function1 = ASSETREGISTER.functions.winningProposal().call() # create the transaction
    #transaction_info = WEB3.eth.get_transaction(call_contract_function1)
    print('call_contract_function1 ', call_contract_function1)
    if int(call_contract_function1) == 0 :
        print ('it is 1')
        winpro = "Financial Programming"
    if int(call_contract_function1) == 1 :
        winpro = "Machine Learning Applications in Finance"
    if int(call_contract_function1) == 2 :
        winpro = "Blockchain and Cryptocurrency" 
    if int(call_contract_function1) == 3 :
        winpro = "FinTech Bootcamp"
        
    return render_template(
        'winner.html',
        # pass these variables to the html template
        #reg_ethaddress=call_contract_function1
        reg_ethaddress = winpro
    )
@APP.route("/getcountresult", methods=['POST'])
def getcountresult():
    address = WEB3.eth.accounts[0]
    private_key = "0x83036aa7c3ace17b58e64130f313013a3e28a71524d995d2f61d2809ff6a1d13"
    
    #dictionary = dict(zip(keys, values))
    proposal_list = ["Financial Programming", "Machine Learning Applications in Finance","Blockchain and Cryptocurrency", "FinTech Bootcamp"]
    call_contract_function1 = ASSETREGISTER.functions.getCount().call() # create the transaction
    #transaction_info = WEB3.eth.get_transaction(call_contract_function1)
    
    #merge call_contract_function1 = [0,0,0,0] and proposal_list into a dictionary 
    # to describe the selected proposal to the web UI
    # call_contract_function1 = 
    proposal_dict = dict(zip(proposal_list, call_contract_function1))
    proposal_list = ["Financial Programming", "Machine Learning Applications in Finance","Blockchain and Cryptocurrency", "FinTech Bootcamp"]
    f = io.StringIO()
    pprint.pprint(proposal_dict, f) 
    f.seek(0) # move pointer to start of dictionary file
    print(f.read())
    return render_template(
        'getcountresult.html',
        # pass these variables to the html template
        #reg_ethaddress=call_contract_function1
        #reg_ethaddress = pprint(dict(zip(proposal_list, call_contract_function1)))
        reg_ethaddress = f.getvalue()
    )
  
# Wrapper
if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=5000)
