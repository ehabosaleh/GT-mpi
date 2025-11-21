#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#ifndef ARRAY_ALIGNMENT
#define ARRAY_ALIGNMENT 64
#endif

static double now_seconds(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

static void *aligned_alloc_bytes(size_t bytes) {
    void *ptr = NULL;
    if (posix_memalign(&ptr, ARRAY_ALIGNMENT, bytes) != 0) {
        return NULL;
    }
    return ptr;
}

static double measure_write_bandwidth(double *restrict array, size_t count, int iterations) {
    const size_t bytes = count * sizeof(double);
    double best_bandwidth = 0.0;

    for (int it = 0; it < iterations; ++it) {
        const double start = now_seconds();
        for (size_t i = 0; i < count; ++i) {
            array[i] = (double)i;
        }
        const double elapsed = now_seconds() - start;
        if (elapsed > 0.0) {
            const double bandwidth = (double)bytes / elapsed / (1024.0 * 1024.0 * 1024.0);
            if (bandwidth > best_bandwidth) {
                best_bandwidth = bandwidth;
            }
        }
    }

    return best_bandwidth;
}

static double measure_read_bandwidth(const double *restrict array, size_t count, int iterations) {
    const size_t bytes = count * sizeof(double);
    volatile double sink = 0.0;
    double best_bandwidth = 0.0;

    for (int it = 0; it < iterations; ++it) {
        const double start = now_seconds();
        for (size_t i = 0; i < count; ++i) {
            sink += array[i];
        }
        const double elapsed = now_seconds() - start;
        if (elapsed > 0.0) {
            const double bandwidth = (double)bytes / elapsed / (1024.0 * 1024.0 * 1024.0);
            if (bandwidth > best_bandwidth) {
                best_bandwidth = bandwidth;
            }
        }
    }

    if (sink == 0.123) {
        printf("(ignore) %f\n", sink);
    }

    return best_bandwidth;
}

int main(int argc, char *argv[]) {
    const size_t default_mb = 256;
    const int default_iterations = 5;

    size_t megabytes = default_mb;
    int iterations = default_iterations;

    if (argc > 1) {
        megabytes = (size_t)strtoull(argv[1], NULL, 10);
        if (megabytes == 0) {
            fprintf(stderr, "Invalid buffer size.\n");
            return EXIT_FAILURE;
        }
    }
    if (argc > 2) {
        iterations = atoi(argv[2]);
        if (iterations <= 0) {
            fprintf(stderr, "Invalid iteration count.\n");
            return EXIT_FAILURE;
        }
    }

    const size_t total_bytes = megabytes * 1024 * 1024;
    const size_t element_count = total_bytes / sizeof(double);

    double *buffer = aligned_alloc_bytes(element_count * sizeof(double));
    if (buffer == NULL) {
        fprintf(stderr, "Failed to allocate %zu MB buffer.\n", megabytes);
        return EXIT_FAILURE;
    }
    memset(buffer, 0, element_count * sizeof(double));

    printf("Memory bandwidth benchmark\n");
    printf("Buffer size: %zu MB\n", megabytes);
    printf("Iterations: %d (best bandwidth reported)\n\n", iterations);

    const double write_bw = measure_write_bandwidth(buffer, element_count, iterations);
    const double read_bw = measure_read_bandwidth(buffer, element_count, iterations);

    printf("Write bandwidth: %.2f GB/s\n", write_bw);
    printf("Read bandwidth : %.2f GB/s\n", read_bw);

    free(buffer);
    return EXIT_SUCCESS;
}
