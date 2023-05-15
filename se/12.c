#include <stdio.h>
#include <math.h>
int main()

{
    // Declare variables
    float op_distinct, opd_distinct, op_total, opd_total;        // Number of distinct operators and operands
    float length, vocab_size, volume, level, difficulty, effort; // Halstead metrics
    float time;                                                  // Time to implement
    float k = 18;                                                // Stroud number (constant)

    // Accept input
    printf("\n Enter the value of number of distinct operators: ");
    scanf("%f", &op_distinct);
    printf("\n Enter the value of number of distinct operands: ");
    scanf("%f", &opd_distinct);
    printf("\n Enter the value of total number of operators: ");
    scanf("%f", &op_total);
    printf("\n Enter the value of total number of operands: ");
    scanf("%f", &opd_total);

    // Calculate Halstead metrics
    vocab_size = op_distinct + opd_distinct;                // Program vocabulary
    length = op_total + opd_total;                          // Program length
    volume = length * log(vocab_size);                      // Program volume
    level = (op_distinct / 2) * (opd_total / opd_distinct); // Program level
    difficulty = 1 / level;                                 // Program difficulty
    effort = volume * difficulty;                           // Program effort
    time = effort / k;                                      // Time to implement

    // Display output
    printf("\n Program Vocabulary: %f", vocab_size);
    printf("\n Program Length: %f", length);
    printf("\n Calculated Program Length: %f", volume);
    printf("\n Volume: %f", volume);
    printf("\n Difficulty: %f", difficulty);
    printf("\n Effort: %f", effort);
    printf("\n Time to implement: %f", time);

    // Return from main function with 0
    return 0;
}
