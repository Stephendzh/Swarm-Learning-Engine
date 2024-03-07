import phe
from phe import paillier
import numpy as np
from tqdm import tqdm

def encrypt_random_vector(vector):
    """
    Encrypts an array with random shape
    :param vector: a numpy array
    :return: the encrypted array reshaped to 1d, the private keyring and the shape of the array
    """
    vector_shape = vector.shape
    vector_1d = vector.reshape(-1)
    keyring = paillier.PaillierPrivateKeyring()
    public_key = []
    encrypted_list = []
    for _ in range(len(vector_1d)):
        pub, priv = paillier.generate_paillier_keypair()
        public_key.append(pub)
        keyring.add(priv)
    for i in tqdm(range(len(vector_1d))):
        encrypted_list.append(public_key[i].encrypt(vector_1d[i]))
    return encrypted_list, keyring, vector_shape

def decrypt_random_vector(encrypted):
    """
    decrypts an array with random shape using the result of the encryption function
    :param encrypted: the result of the encryption function
    :return: the decrypted array
    """
    encrypted_list, keyring, vector_shape = encrypted[0], encrypted[1], encrypted[2]
    decrypted_list = []
    for i in tqdm(range(len(encrypted_list))):
        decrypted_list.append(keyring.decrypt(encrypted_list[i]))
    decrypted_vector = np.array(decrypted_list).reshape(vector_shape)
    return decrypted_vector

def encrypt_paramter_dict(w_dict):
    """we encrypt the parameter tensors in dictionary"""
    key_list, tuple_list = [], []
    for key, value in tqdm(w_dict.items()):
        print(value)
        print(np.array(value, dtype=np.float64))
        tuple_encryption = encrypt_random_vector(np.array(value, dtype=np.float64))
        tuple_list.append(tuple_encryption)
        key_list.append(key)
    return key_list, tuple_list

def decypt_order_dict(encrypted_pair):
    """Designed to decrypt the dict of the global parameters"""
    # 传入的参数是一对列表，第一个列表中包含字典的key，第二个包含一系列tuple用于解密
    key_list, tuple_list = encrypted_pair[0], encrypted_pair[1]
    decrypted_dict = {}
    for index, en_tuple in enumerate(tuple_list):
        decrypted_dict[key_list[index]] = decrypt_random_vector(en_tuple)
    return decrypted_dict