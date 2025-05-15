# Random Hash Generator

A Python project that generates random SHA-256 hashes and searches for hashes starting with a specific prefix ("00").

## Project Purpose

This project demonstrates:
1. Random cryptographic hash generation in Python
2. Automated testing with pytest
3. CI/CD integration with GitHub Actions
4. Basic principles of MLOps and DevOps

The main task of this project is to generate random 32-character hashes up to 1000 times until it finds a hash that starts with two consecutive zeros ("00").

## How the Hash Generation Works

The process works as follows:

1. Random bytes are generated using `os.urandom(16)` which provides cryptographically secure random data
2. A SHA-256 hash is created from these random bytes using the `hashlib` library
3. The resulting hash is converted to a hexadecimal string representation
4. The program checks if the hash starts with the required prefix ("00")
5. If a matching hash is found within 1000 attempts, the program returns success
6. If no matching hash is found after 1000 attempts, the program returns failure

## Running the Program

To run the program directly:

```bash
python main.py
```

This will attempt to find a hash starting with "00" and print the result to the console.

## Running Tests

The project includes comprehensive tests created with pytest. To run the tests:

```bash
pytest test_random_hash.py -v
```

This will run all the tests with verbose output, showing exactly which tests pass or fail.

For test coverage information:

```bash
coverage run -m pytest test_random_hash.py
coverage report
```

## GitHub Actions Integration

This project includes GitHub Actions workflow configuration that:

- Automatically runs on push to main/master branch
- Sets up Python 3.11.9
- Installs all required dependencies
- Runs the test suite
- Executes the main script to demonstrate functionality

The workflow status can be viewed in the "Actions" tab of the GitHub repository.

## Requirements

- Python 3.11.9
- pytest 7.4.0
- coverage 7.3.2

All dependencies can be installed using:

```bash
pip install -r requirements.txt
```

## License

This project is open source and available under the MIT License.

