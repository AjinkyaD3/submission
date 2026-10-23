#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

// Function to calculate F-measure (Harmonic Mean)
double calculateFMeasure(double precision, double recall) {
    if (precision + recall == 0)
        return 0.0;
    return 2 * (precision * recall) / (precision + recall);
}

// Function to calculate E-measure
double calculateEMeasure(double precision, double recall, double b) {
    double bSquared = b * b;
    double numerator = 1 + bSquared;
    double denominator = (bSquared / recall) + (1 / precision);
    return 1 - (numerator / denominator);
}

int main() {
    double precision, recall, b;

    cout << "Enter Precision (P): ";
    cin >> precision;

    cout << "Enter Recall (R): ";
    cin >> recall;

    cout << "Enter value of beta (b): ";
    cin >> b;

    double fMeasure = calculateFMeasure(precision, recall);
    double eMeasure = calculateEMeasure(precision, recall, b);

    cout << fixed << setprecision(4);
    cout << "\nHarmonic Mean (F-measure) = " << fMeasure << endl;
    cout << "E-measure = " << eMeasure << endl;

    // Explanation based on b
    if (b == 1)
        cout << "Note: For b=1, E-measure is the complement of F-measure.\n";
    else if (b > 1)
        cout << "Note: Higher b (>1) means user gives more importance to precision.\n";
    else
        cout << "Note: Lower b (<1) means user gives more importance to recall.\n";

    return 0;
}
