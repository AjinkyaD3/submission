#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

// Structure to store BMP header info
#pragma pack(push, 1)
struct BMPHeader {
    unsigned short type;
    unsigned int size;
    unsigned short reserved1;
    unsigned short reserved2;
    unsigned int offset;
};

struct BMPInfoHeader {
    unsigned int size;
    int width;
    int height;
    unsigned short planes;
    unsigned short bitCount;
    unsigned int compression;
    unsigned int imageSize;
    int xPixelsPerMeter;
    int yPixelsPerMeter;
    unsigned int colorsUsed;
    unsigned int importantColors;
};
#pragma pack(pop)

// Function to calculate average brightness of image pixels
double calculateBrightness(const unsigned char* pixelData, int size) {
    long long totalBrightness = 0;
    for (int i = 0; i < size; i++)
        totalBrightness += pixelData[i];
    return (double)totalBrightness / size;
}

// Function to determine dominant color type
string determineColorType(unsigned short bitCount) {
    if (bitCount == 24)
        return "True Color (24-bit RGB)";
    else if (bitCount == 8)
        return "Grayscale (8-bit)";
    else if (bitCount == 32)
        return "RGBA (32-bit with Alpha)";
    else
        return "Unknown / Unsupported Color Depth";
}

int main() {
    string filename;
    cout << "Enter BMP file name (example: sample_image.bmp): ";
    cin >> filename;

    // Open file from same folder
    ifstream file("./" + filename, ios::binary);
    if (!file) {
        cout << "Error: Could not open file. Make sure the BMP is in the same folder as the program.\n";
        return 1;
    }

    BMPHeader header;
    BMPInfoHeader info;

    // Read header
    file.read(reinterpret_cast<char*>(&header), sizeof(header));
    file.read(reinterpret_cast<char*>(&info), sizeof(info));

    if (header.type != 0x4D42) { // 'BM' in hex
        cout << "Not a valid BMP file!" << endl;
        return 1;
    }

    cout << "\n--- IMAGE FEATURES ---\n";
    cout << "File Name: " << filename << endl;
    cout << "File Type: BMP Image\n";
    cout << "Image Width: " << info.width << " pixels\n";
    cout << "Image Height: " << info.height << " pixels\n";
    cout << "Color Depth: " << info.bitCount << " bits\n";
    cout << "Color Type: " << determineColorType(info.bitCount) << endl;
    cout << "Image Size (from header): " << info.imageSize << " bytes\n";

    // Extract pixel data and calculate brightness
    file.seekg(header.offset, ios::beg);
    int pixelArraySize = info.imageSize;
    unsigned char* pixelData = new unsigned char[pixelArraySize];
    file.read(reinterpret_cast<char*>(pixelData), pixelArraySize);

    double brightness = calculateBrightness(pixelData, pixelArraySize);
    cout << "Average Brightness: " << brightness << endl;

    cout << "\nFeature Extraction Completed Successfully.\n";

    delete[] pixelData;
    file.close();
    return 0;
}
