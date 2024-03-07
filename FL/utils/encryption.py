import numpy as np
import phe
from phe import paillier
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
        encrypted_list.append(public_key[i].encrypt(vector_1d[i], precision=1e-5))
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
    keyring_list, shape_list = [], []
    encrypted_dict = {}
    for key, value in w_dict.items():
        tuple_encryption = encrypt_random_vector(np.array(value))
        encrypted_dict[key] = tuple_encryption
        keyring_list.append(tuple_encryption[1])
        shape_list.append(tuple_encryption[2])
    return encrypted_dict, keyring_list, shape_list

def decypt_order_dict(w_dict):
    """Designed to decrypt the dict of the global parameters"""
    return 0