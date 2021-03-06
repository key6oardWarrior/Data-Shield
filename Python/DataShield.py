import os
from platform import python_version

from Encryption import EncryptFile, EncryptInput
from Decryption import Decryption

class DataShield:
	__PATH = os.path.dirname(__file__)

	def __init__(self):
		pass

	def __responceHandler(self, query):
		'''
		Handle yes and no responces

		@param <class 'str'> query to the user\n
		@return <class 'str'> user's responce
		'''
		responce = input(query).upper().strip()

		while((responce != "Y") and (responce != "N")):
			print("\nResponce must be either Y/N")
			responce = input(query).upper().strip()

		return responce

	def __fileHandler(self):
		'''
		ask user to enter file and handle I/O errors

		@param <class 'str'> the path of the user's file
		'''
		filePath = input("Enter file path: ")

		while(os.path.exists(filePath) == False):
			print(f"\nFile {filePath} does not exists")
			filePath = input("Enter file path: ")

		return filePath

	def main(self):
		responce = input("If you want to encrypt a file type Y? If you want to input data to be encrypted type N. If you want to decrypt data type NN. Y/N/NN ").upper().strip()

		while((responce != "Y") and (responce != "N") and (responce != "NN")):
			print("\nResponce must be either Y/N/NN")
			responce = input("If you want to encrypt a file type Y? If you want to input data to be encrypted type N. If you want to decrypt data type NN. Y/N/NN ").upper().strip()

		if responce == "Y": # encrypt existing file
			filePath = self.__fileHandler()

			encryption = EncryptFile(filePath)
			encryption.encAlg(filePath, encryption.encFile())

			responce = self.__responceHandler("Do you want to delete the unencrypted file? Y/N (Y is recommended) ")
			
			if responce == "Y":
				os.remove(os.path.join(self.__PATH, filePath))

		elif responce == "NN": # decrypt an encrypted file
			filePath = self.__fileHandler()
			outName = input("Enter name of output file: ")

			while os.path.exists(outName):
				responce = self.__responceHandler(f"Are you sure you want to overwrite {outName}? Y/N ")

				if responce == "Y":
					break

			decrypt = Decryption()
			decrypt.decrypt(filePath, outName)

			responce = self.__responceHandler("Do you want to delete the encrypted file Y/N ")
			if responce == "Y":
				os.remove(filePath)

		else: # encrypt user input
			data = input("Enter data to be encryped: ")
			encData = EncryptInput(data)
			encData.encAlg(outName=encData.encData())

			os.remove(os.path.join(self.__PATH, "data.txt"))

try:
	if python_version()[0] != "3":
		raise RuntimeError("Python version must be 3.X.X, or greater")
except:
	raise RuntimeError("Python version must be 3.X.X, or greater")

dataShield = DataShield()
dataShield.main()
