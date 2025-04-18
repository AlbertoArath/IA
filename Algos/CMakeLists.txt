cmake_minimum_required(VERSION 3.10)
project(MyTestProject)

# Add Google Test
add_subdirectory(googletest)

# Your test file
add_executable(runTests test.cpp)

# Link gtest and gtest_main
target_link_libraries(runTests gtest gtest_main)

# Ensure proper C++ standard
set_target_properties(runTests PROPERTIES
  CXX_STANDARD 11
  CXX_STANDARD_REQUIRED YES
)