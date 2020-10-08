#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

void red() {
  printf("\033[1;31m");
}

void green() {
  printf("\033[0;32m");
}

void reset() {
  printf("\033[0m");
}
