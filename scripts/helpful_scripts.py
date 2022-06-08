from brownie import network, config, accounts, MockV3Aggregator

FORKED_BLOCKCHAIN = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_ETH_PRICE = 180000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_BLOCKCHAIN
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["DEV01"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mock aggregator..")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_ETH_PRICE, {"from": get_account()})
    print("Mock deployed!")
