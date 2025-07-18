#!/usr/bin/env python3
"""
Script to run all tests from the parent directory.
This avoids import conflicts by running tests from within each directory.
"""

import subprocess
import sys
import os

def run_tests_in_directory(directory):
    """Run tests in a specific directory."""
    print(f"\n{'='*50}")
    print(f"Running tests in {directory}")
    print(f"{'='*50}")
    
    # Change to the directory
    original_dir = os.getcwd()
    os.chdir(directory)
    
    try:
        # Run pytest
        result = subprocess.run([sys.executable, "-m", "pytest", "-v"], 
                              capture_output=True, text=True)
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
    finally:
        # Change back to original directory
        os.chdir(original_dir)

def main():
    """Run all tests."""
    print("Running all tests...")
    
    # List of directories containing tests
    test_directories = ["three_five", "postcodes_validator"]
    
    all_passed = True
    
    for directory in test_directories:
        if os.path.exists(directory):
            success = run_tests_in_directory(directory)
            if not success:
                all_passed = False
        else:
            print(f"Directory {directory} not found")
            all_passed = False
    
    print(f"\n{'='*50}")
    if all_passed:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    print(f"{'='*50}")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main()) 