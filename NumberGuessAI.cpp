#include <iostream>
using namespace std;

int main() {
    int low = 1, high = 100, mid;
    char response;
    
    cout << "=========================================\n";
    cout << "         AI NUMBER GUESSING GAME          \n";
    cout << "=========================================\n";
    cout << "Think of a number between 1 and 100.\n";
    cout << "The AI will try to guess it!\n";
    cout << "-----------------------------------------\n";
    cout << "Please respond with:\n";
    cout << "'>' if your number is higher\n";
    cout << "'<' if your number is lower\n";
    cout << "'=' if the AI guessed correctly\n";
    cout << "-----------------------------------------\n";

    while (low <= high) {
        mid = (low + high) / 2;
        cout << "\nIs your number " << mid << "? (>, <, =): ";
        cin >> response;

        if (response == '>') {
            low = mid + 1;
        } else if (response == '<') {
            high = mid - 1;
        } else if (response == '=') {
            cout << "\nYay! The AI guessed your number correctly!\n";
            break;
        } else {
            cout << "Invalid input. Please use '>', '<', or '='.\n";
        }
    }

    if (low > high) {
        cout << "\nHmm... It seems there was a misunderstanding.\n";
        cout << "Maybe try again with consistent responses!\n";
    }

    cout << "\nThanks for playing the AI Number Guessing Game!\n";
    return 0;
}
