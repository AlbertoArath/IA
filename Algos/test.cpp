#include <gtest/gtest.h>
#include <gmock/gmock.h>

// Function to test
int add(int a, int b) {
    return a + b;
}

// Test case
TEST(AdditionTest, HandlesPositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}


