from brownie import accounts, network, config, MockV3Aggregator

FORKED_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
decimals = 8
value = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def mockpricefeed():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(decimals, value, {"from": get_account()})
