//encryption and decryption using method of transposition technique

#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

// Function to encrypt the message
string encrypt(string message, int key) {
    int len = message.length();
    int rows = ceil((double)len / key);

    char matrix[rows][key];
    int k = 0;

    // Fill the matrix row-wise
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < key; j++) {
            if (k < len)
                matrix[i][j] = message[k++];
            else
                matrix[i][j] = 'X'; // Pad with 'X' if needed
        }
    }

    // Read the matrix column-wise to get the ciphertext
    string ciphertext = "";
    for (int j = 0; j < key; j++) {
        for (int i = 0; i < rows; i++) {
            ciphertext += matrix[i][j];
        }
    }

    return ciphertext;
}

// Function to decrypt the message
string decrypt(string ciphertext, int key) {
    int len = ciphertext.length();
    int rows = ceil((double)len / key);

    char matrix[rows][key];
    int k = 0;

    // Fill the matrix column-wise
    for (int j = 0; j < key; j++) {
        for (int i = 0; i < rows; i++) {
            matrix[i][j] = ciphertext[k++];
        }
    }

    // Read the matrix row-wise to get the plaintext
    string plaintext = "";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < key; j++) {
            plaintext += matrix[i][j];
        }
    }

    return plaintext;
}

int main() {
    string message, encrypted, decrypted;
    int key;

    // Input message and key from user
    cout << "Enter the message to encrypt: ";
    getline(cin, message);
    cout << "Enter the key (number of columns): ";
    cin >> key;

    // Encrypt the message
    encrypted = encrypt(message, key);
    cout << "Encrypted message: " << encrypted << endl;

    // Decrypt the message
    decrypted = decrypt(encrypted, key);
    cout << "Decrypted message: " << decrypted << endl;

    return 0;
}
