from brownie import SimpleStorage,accounts

def test_deploy():
    #arrange
    user = accounts[0]
    #act
    simple_storage = SimpleStorage.deploy({
        "from":user,
    })
    starting_val = simple_storage.retrieve()
    expected = 0
    #assert
    assert starting_val==expected

def test_updating_storage():
    #arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    #act
    expected = 15
    simple_storage.store(expected,{"from":account})
    #assert
    assert simple_storage.retrieve()==expected