import os
from platform import python_version

from Encryption import EncryptFile, EncryptInput
from Decryption import Decryption

class DataShield:
	def __init__(self):
		pass

	def main(self):
		responce = input("If you want to encrypt a file type Y? If you want to input data to be encrypted type N. If you want to decrypt data type NN. Y/N/NN ").upper().strip()

		while((responce != "Y") and (responce != "N") and (responce != "NN")):
			print("\nResponce must be either Y/N")
			responce = input("If you want to encrypt a file type Y? If you want to input data to be encrypted type N. If you want to decrypt data type NN. Y/N/NN ").upper().strip()

		if responce == "Y":
			fileName = input("Enter file name: ")

			while(os.path.exists(fileName) == False):
				print(f"\nFile {fileName} does not exists")
				fileName = input("Enter file name: ")

			encryption = EncryptFile(fileName)
			encryption.encAlg(fileName, encryption.encFile())
		elif responce == "NN":
			fileName = input("Enter file name: ")

			while(os.path.exists(fileName) == False):
				print(f"\nFile {fileName} does not exists")
				fileName = input("Enter file name: ")

			outName = input("Enter name of output file: ")

			while os.path.exists(outName):
				responce = input(f"Are you sure you want to overwrite {outName}? Y/N ").upper().strip()

				while((responce != "Y") and (responce != "N")):
					print("\nResponce must be either Y/N")
					responce = input(f"Are you sure you want to overwrite {outName}? Y/N ").upper().strip()

				if responce == "Y":
					break

			decrypt = Decryption()
			decrypt.decrypt(fileName, outName)
		else:
			data = input("Enter data to be encryped: ")
			encData = EncryptInput(data)
			encData.encAlg(outName=encData.encData())

			os.remove(os.path.join(os.path.dirname(__file__), "data.txt"))

try:
	if python_version()[0] != "3":
		raise RuntimeError("Python version must be 3.X.X")
except:
	raise RuntimeError("Python version must be 3.X.X")

dataShield = DataShield()
dataShield.main()
