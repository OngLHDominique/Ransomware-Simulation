===== OVERVIEW =====
The ransomware.py is a python program that simulates a simple ransomware attack.
Assuming that the attacker breaks into a machine that has OpenSSL installed, and the attacker puts the public key into the victim's machine.
The victim has a file named 'my_secrets.txt' that is in the root directory.
The ransomware will randomly generate a 16-byte symmetric key and uses it to encrypt the victim's data (my_secrets.txt) into 'data_cipher.txt'.
To ensure that the victim is unable to decrypt their data without paying the ransom/without attacker's permission, the symmetric key is encrypted using the attacker's public key into 'key_cipher.txt'.
The original data and the unencrypted symmetric key are deleted.
This ensures that the victim only has the encrypted data and an encrypted key, which requires the attacker's private key to unlock.
The 'subprocess' module is utilised in the program to directly invoke standard Kali OpenSSL commands from within the script.
All ciphertext outputs are forced into human-readable base64 format using '-a' flag or piping to 'base64'.

Files:
1. ransomware.py

===== REQUIREMENTS =====
ENVIRONMENT:
1. Kali Linux VM

LANGUAGE: PYTHON
LANGUAGE VERSION: 3.14.6

===== INSTALLATION OF LIBRARY =====
Before running this script, ensure that you have Python3 installed and configured. If not, use the code below to install Python3.
(*Remember to use 'sudo' to install with root privileges.)

To install Python3 : 'sudo pip3 install python3'

===== HOW TO RUN THE PROGRAM =====
1. Ensure that Kali (attacker) VM is running, and navigate to the file location.
2. On Kali, open the terminal and run the command 'sudo python3 ransomware.py'.
3. The program will prompt a series of messages in the terminal. It will display,
3a. Generating of symmetric key
3b. Generating of attacker RSA key pair
3c. Encryption of the file (my_secrets.txt)
3d. Encryption of symmetric key
3e. Deletion of original files (my_secrets.txt and unencrypted symmetric key)
4. The program will display a warning message in the terminal that tells the user that 'my_secrets.txt' is encrypted. The user has to pay a ransom and send 'key_cipher.txt' to the attacker to be able to decrypt the file.
5. User has to press the 'enter' key on the keyboard to simulate paying the ransom.
6. Once the 'Enter' key is pressed, the program will display a message that says that the ransom has been paid, and proceed to decrypt the file.
7. The program will display a completion of decryption message to inform the user that 'my_secrets.txt' has been restored.

Example, (*Refer to the attached images for the screenshots of the successful runs.)
The test case is exactly the same as the usage mentioned above. Check the file directory before running the python program to see the original files. Check the file directory again once the python program has ran, ensure that user does not press the 'enter' key to be able to see the changes once the ransomware is active. Then check the file directory once the simulation of the ransom has been paid to see the decrypted file.

===== EXPECTED RESULTS =====
Once the program is executed, 'key.txt' and RSA keys 'public.pem' and 'private.pem' will be generated. Next, 'data_cipher.txt' and 'key_cipher.txt' will be created in base64 format. The original 'key.txt' and 'my_secrets.txt' will then be deleted from the root directory. The ransom message will print to the console to ask for the ransom. Upon pressing the 'enter' key, 'key.txt' and 'data_cipher.txt' will be decrypted back into the original 'my_secrets.txt'.
