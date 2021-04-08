import os

class Decryption:
	def __init__(self):
		pass

	def decrypt(self, fileName, outName):
		os.system(f"openssl enc -aes-256-cbc -d -in {fileName} -out {outName}")
		print("Decrypted data:\n", open(f"{outName}", "r").read())

if __name__ == "__main__":
	test = Decryption()
	test.decrypt("tester.bin", "tester")