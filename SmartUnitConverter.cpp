#include <iostream>
#include <iomanip>
using namespace std;

// Function prototypes
void lengthConversion();
void weightConversion();
void temperatureConversion();
void currencyConversion();

int main() {
    int choice;
    cout << "=============================================\n";
    cout << "          SMART UNIT CONVERTER v1.0          \n";
    cout << "=============================================\n";

    do {
        cout << "\nChoose a conversion type:\n";
        cout << "1. Length\n";
        cout << "2. Weight\n";
        cout << "3. Temperature\n";
        cout << "4. Currency\n";
        cout << "5. Exit\n";
        cout << "---------------------------------------------\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: lengthConversion(); break;
            case 2: weightConversion(); break;
            case 3: temperatureConversion(); break;
            case 4: currencyConversion(); break;
            case 5: cout << "\nThank you for using Smart Unit Converter!\n"; break;
            default: cout << "\nInvalid choice! Please try again.\n";
        }
    } while (choice != 5);

    return 0;
}

// ---------------- Length Conversion ----------------
void lengthConversion() {
    double meter;
    cout << "\nEnter length in meters: ";
    cin >> meter;

    cout << fixed << setprecision(2);
    cout << meter << " meters = " << meter * 100 << " centimeters\n";
    cout << meter << " meters = " << meter * 39.37 << " inches\n";
    cout << meter << " meters = " << meter * 3.281 << " feet\n";
}

// ---------------- Weight Conversion ----------------
void weightConversion() {
    double kg;
    cout << "\nEnter weight in kilograms: ";
    cin >> kg;

    cout << fixed << setprecision(2);
    cout << kg << " kilograms = " << kg * 1000 << " grams\n";
    cout << kg << " kilograms = " << kg * 2.205 << " pounds\n";
    cout << kg << " kilograms = " << kg * 35.274 << " ounces\n";
}

// ---------------- Temperature Conversion ----------------
void temperatureConversion() {
    double celsius;
    cout << "\nEnter temperature in Celsius: ";
    cin >> celsius;

    double fahrenheit = (celsius * 9 / 5) + 32;
    double kelvin = celsius + 273.15;

    cout << fixed << setprecision(2);
    cout << celsius << "°C = " << fahrenheit << "°F\n";
    cout << celsius << "°C = " << kelvin << " K\n";
}

// ---------------- Currency Conversion ----------------
void currencyConversion() {
    double usd;
    cout << "\nEnter amount in USD: ";
    cin >> usd;

    const double rateIDR = 15700; // Example rate
    const double rateEUR = 0.92;
    const double rateJPY = 151.2;

    cout << fixed << setprecision(2);
    cout << "$" << usd << " = Rp" << usd * rateIDR << " IDR\n";
    cout << "$" << usd << " = " << usd * rateEUR << " EUR\n";
    cout << "$" << usd << " = " << usd * rateJPY << " JPY\n";
}
