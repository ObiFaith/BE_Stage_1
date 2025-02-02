# Number Classifier API

## Overview

The Number Classifier API is a FastAPI-based application that provides detailed information about a number. It classifies the number as prime, perfect, or Armstrong, and returns additional information like the number's properties, digit sum, and a fun fact related to the number.

## Features

- **Prime Check**: Identifies if the number is prime.

- **Perfect Number Check**: Determines if the number is a perfect number.
- **Armstrong Check**: Identifies if the number is an Armstrong number.
- **Number Properties**: Classifies the number as either even or odd.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact related to the number.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ObiFaith/BE_Stage_1.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the root of the project directory and add the NUMBER_URL environment variable:

   ```bash
   NUMBER_URL=https://some-number-api.com
   ```

5. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

The API will be accessible at http://127.0.0.1:8000.

## API Endpoint

`GET /api/classify-number/`

This endpoint receives a number and returns a classification of the number along with additional information.

### Request

- **Query parameter**: `number` (required) – The number to classify (e.g., `5`).

### Response

- **200 OK**: Returns a JSON response with the classification details of the number.

  ### Example:

  ```json
  {
    "number": 6,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 6,
    "fun_fact": "6 is the smallest perfect number."
  }
  ```

- **400 Bad Request**: If the provided `number` is not a valid integer, the response will include an error message.

  ### Example:

  ```json
  {
    "number": "invalid",
    "error": true
  }
  ```

## Contributing

Feel free to fork this repository and submit pull requests for improvements.

If you have any feature suggestions or bug reports, please open an issue on the GitHub repository.

## License

This project is open-source and available under the MIT License.
