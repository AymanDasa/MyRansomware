# WARNING: USE AT YOUR OWN RISK
This script is intended for educational and testing purposes only.
Use of this script to encrypt files without proper backups or safeguards can result in permanent data loss. It is your responsibility to ensure that all data is properly backed up and that encryption keys are kept secure and not shared with unauthorized parties. The author of this script accepts no liability for any damages or losses resulting from the use of this script. Use at your own risk.

For your own safety, it is highly recommended that you run this script in a virtual machine environment to avoid potential damage to your system or data. Running the script in a virtual machine will allow you to test its functionality without risking any harm to your physical system. 
Please ensure that the virtual machine environment is properly configured and that you have a backup of all important data before running the script.
The author of this script is not responsible for any damage or loss of data that may result from the use of this script. 
# Use at your own risk.

This Python script encrypts selected files in specified directories using the Fernet encryption algorithm. Here is a brief explanation of the script's functionality:
1. The script generates a new encryption key using the Fernet module and writes it to a file named "thekey.key".
2. The script defines a list of root directories to search for files to encrypt.
3. The script uses the os.walk() function to recursively search each root directory and its subdirectories for files.
4. For each file found, the script checks if the file has a supported file extension (".py", ".key", ".xml", ".iml", ".ignore") and is not a directory. If the file has a supported extension and is not a directory, the script proceeds to encrypt the file's contents.
5. The script opens the file, reads its contents, encrypts the contents using the encryption key generated earlier, and writes the encrypted contents back to the file. The script also prints information about the file's original size and encrypted size.
6. If any errors occur during the encryption process, the script simply ignores them and continues processing the remaining files.

# Note 
That this script should be used with caution, as encrypting files without a backup can potentially result in permanent data loss if the encryption key is lost or damaged. It is also important to ensure that the encryption key is kept secure and not shared with unauthorized parties.
