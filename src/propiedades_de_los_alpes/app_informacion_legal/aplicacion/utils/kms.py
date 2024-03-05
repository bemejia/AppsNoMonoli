import boto3

class KmsEncryptor:
    def __init__(self, kms_key_id):
        self.kms_client = boto3.client('kms', region_name='us-west-2')
        self.kms_key_id = kms_key_id

    def encrypt(self, plaintext):
        response = self.kms_client.encrypt(
            KeyId=self.kms_key_id,
            Plaintext=plaintext
        )
        ciphertext = response['CiphertextBlob']
        return ciphertext

    def decrypt(self, ciphertext):
        response = self.kms_client.decrypt(
            CiphertextBlob=ciphertext
        )
        plaintext = response['Plaintext']
        return plaintext