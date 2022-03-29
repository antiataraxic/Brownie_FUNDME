from brownie import accounts, config, FundMe, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    mockpricefeed,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pf_address = config["networks"][network.show_active()]["eth_usd_price_feed"]

    else:
        account = get_account()
        print(f"The current network is {network.show_active()}")

        mockpricefeed()
        pf_address = MockV3Aggregator[-1].address

    Fund_Me = FundMe.deploy(pf_address, {"from": account})

    print(f"Contract deployed to {Fund_Me.address}")


def main():
    deploy_fund_me()
