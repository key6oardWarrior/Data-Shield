import os

class Encryption:
	def __init__(self):
		pass

	def encAlg(self, inName, outName):
		'''
		Use the AES algorithm to encrypt a file using a 256 bit Cypher block chaining algorthm

		@param <class 'str'> input name of file\n
		@param <class 'str'> output name of file
		'''
		os.system(f"openssl enc -aes-256-cbc -in {inName} -out {outName}.bin")

class EncryptFile(Encryption):
	def __init__(self):
		pass

	def encFile(self):
		'''
		encrypt file data

		@return <class 'str'>
		'''
		newFileName = input("Enter encrypted file's name: ")

		while os.path.exists(newFileName):
			responce = input(f"Are you sure you want to overwrite {newFileName}? Y/N ").upper().strip()

			while((responce != "Y") and (responce != "N")):
				print("\nResponce must be either Y/N")
				responce = input(f"Are you sure you want to overwrite {newFileName}? Y/N ").upper().strip()

			if responce == "Y":
				break

		return newFileName

class EncryptInput(Encryption):
	__PATH = os.path.dirname(__file__)

	def __init__(self, data):
		self.__DATA = data

	def encAlg(self, outName, inName="data.txt"):
		'''
		Use the AES algorithm to encrypt a file using a 256 bit Cypher block chaining algorthm

		@param <class 'str'> output name of file
		@param <class 'str'> input name of file
		'''

		os.system(f"openssl enc -aes-256-cbc -in {os.path.join(self.__PATH, inName)} -out {outName}.bin")

	def encData(self):
		'''
		allow user to enter data to be encrypted

		@return <class 'str'>
		'''
		newFileName = input("Enter encrypted file's name: ")

		open(f"{self.__PATH}\\data.txt", "w").write(self.__DATA)
		while os.path.exists(f"{newFileName}.bin"):
			responce = input(f"Are you sure you want to overwrite {newFileName}? Y/N ").upper().strip()

			while((responce != "Y") and (responce != "N")):
				print("\nResponce must be either Y/N")
				responce = input(f"Are you sure you want to overwrite {newFileName}? Y/N ").upper().strip()

			if responce == "Y":
				break

		return newFileName

if __name__ == "__main__":
	testInput = input("0 or 1 ")

	if testInput == "0":
		enc = EncryptInput("test")
		enc.encAlg(outName=enc.encData())
	else:
		enc = EncryptFile()
		enc.encAlg(input("File name "), enc.encFile())

	os.remove(os.path.join(os.path.dirname(__file__), "data.txt"))