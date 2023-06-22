from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def get_private_key_and_address(mnemonic):
    # Генерируем сид-фразу
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Создаем BIP44 кошелек
    bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)

    # Получаем первый приватный ключ и адрес
    bip_obj_acc = bip_obj_mst.Purpose().Coin().Account(0)
    bip_obj_chain = bip_obj_acc.Change(Bip44Changes.CHAIN_EXT)
    bip_obj_addr = bip_obj_chain.AddressIndex(0)
    
    private_key = bip_obj_addr.PrivateKey().Raw().ToHex()
    address = bip_obj_addr.PublicKey().ToAddress()

    return private_key, address

mnemonic = 'your 12-word seed phrase goes here'
private_key, address = get_private_key_and_address(mnemonic)
print('Private key:', private_key)
print('Address:', address)
