#include <stdio.h>

int main() {
    int nodes, edges, components;
    printf("Enter the number of nodes: ");
    scanf("%d", &nodes);
    printf("Enter the number of edges: ");
    scanf("%d", &edges);
    printf("Enter the number of connected components: ");
    scanf("%d", &components);

    int complexity = edges - nodes + 2 * components;
    printf("The cyclomatic complexity is: %d\n", complexity);

    return 0;
}