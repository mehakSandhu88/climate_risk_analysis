#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void calculate_statistics(float data[], int n, float *mean, float *median, float *mode, float *std_dev) {
    float sum = 0.0, variance = 0.0;
    int i, j;
    float temp;

    // Calculate mean
    for (i = 0; i < n; i++) {
        sum += data[i];
    }
    *mean = sum / n;

    // Sort data for median and mode
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (data[i] > data[j]) {
                temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }

    // Calculate median
    if (n % 2 == 0) {
        *median = (data[n / 2 - 1] + data[n / 2]) / 2;
    } else {
        *median = data[n / 2];
    }

    // Calculate standard deviation
    for (i = 0; i < n; i++) {
        variance += pow(data[i] - *mean, 2);
    }
    variance /= n;
    *std_dev = sqrt(variance);

    // Mode calculation (simplified for demonstration)
    int count = 1, max_count = 1;
    *mode = data[0];
    for (i = 1; i < n; i++) {
        if (data[i] == data[i - 1]) {
            count++;
            if (count > max_count) {
                max_count = count;
                *mode = data[i];
            }
        } else {
            count = 1;
        }
    }
}

int main() {
    float data[] = {15.3, 16.1, 14.8, 15.3, 16.1};
    int n = sizeof(data) / sizeof(data[0]);
    float mean, median, mode, std_dev;

    calculate_statistics(data, n, &mean, &median, &mode, &std_dev);

    printf("Mean: %.2f\n", mean);
    printf("Median: %.2f\n", median);
    printf("Mode: %.2f\n", mode);
    printf("Standard Deviation: %.2f\n", std_dev);

    return 0;
}
