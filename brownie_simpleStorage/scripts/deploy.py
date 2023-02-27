from brownie import SimpleStorage,accounts,network


def get_account():
    if(network.show_active()=="ganache-local"):
        return accounts[1]
    else:
        accounts[0]

def deploy_Simple_storage():
    account = get_account()
    ss = SimpleStorage.deploy({
        "from":account
    # print(ss)
    # getting the initial value
    storval = ss.retrieve()
    print(storval)
    # storing the value
    transaction = ss.store(15,{
        "from":account
    })
    #  waiting for block conformation
    transaction.wait(1)
    # getting the updated value
    updated_val = ss.retrieve()
    print(updated_val)


def main():

    deploy_Simple_storage()
