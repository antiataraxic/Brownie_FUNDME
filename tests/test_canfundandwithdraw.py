from brownie import network, FundMe
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_witdraw():
    account = get_account()
    fundme = deploy_fund_me()
    entrance_fee = fundme.getEntranceFee()
    tx = fundme.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fundme.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)
    assert fundme.adressToAmountFunded(account.address) == 0


def test_onlyowner_canwithdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")

        account = get_account()
        fund_me = deploy_fund_me()
        account2 = accounts.add()
        fund_me.withdraw({"from": account2})
