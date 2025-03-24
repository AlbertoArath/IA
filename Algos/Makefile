# Define the C++ compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11 -g
LDFLAGS =

# List all source files for the project
SRCS = DfsBfs.cpp 

# Automatically generate object file names from the source files
OBJS = $(SRCS:.cpp=.o)

# Name of the final executable
TARGET = myprogram

# Default target to build the executable
all: $(TARGET)

# Rule to link object files into the final executable
$(TARGET): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^

# Pattern rule to compile source files into object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean target to remove generated files
clean:
	del /F /Q $(OBJS) $(TARGET).exe