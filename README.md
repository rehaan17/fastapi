# Password Generator API and Integrating an open-source third-party API

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the FastAPI Server](#1-running-the-fastapi-server)
  - [Generate Password](#2-generate-password)
    - [Request](#request)
    - [Parameters](#parameters)
    - [Response](#response)
    - [Sending a POST Request](#sending-a-post-request)
  - [Running Tests for Generate Password Endpoint](#3-running-tests-for-generate-password-endpoint)
    - [How to Run the Tests](#how-to-run-the-tests)
  - [COVID-19 Statistics](#4-covid-19-statistics)
    - [Get Countries Affected by COVID-19](#get-countries-affected-by-covid-19)
      - [Parameters](#parameters-1)
      - [Response](#response-1)
    - [Get COVID-19 Statistics](#get-covid-19-statistics-1)
      - [Parameters](#parameters-2)
      - [Response](#response-2)
- [API Documentation](#api-documentation)
- [APIs Used](#apis-used)
- [Authors](#authors)

## Introduction

Welcome to the Password Generator API! This API enables users to request new passwords based on specified criteria and also provides access to COVID-19 statistics for various countries.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Running the FastAPI Server

Start the FastAPI server by running the following command in your terminal:

```bash
uvicorn main:app --reload
```

### 2. Generate Password

#### Request
- **Endpoint:** `/generate-password`
- **Method:** `POST`
- **Body:**

  ```json
  {
    "length": 12,
    "uppercase": true,
    "lowercase": true,
    "numbers": true,
    "special_characters": true
  }
  ```

#### Parameters

- **length** (`int`): The length of the password to generate.
- **uppercase** (`bool`, optional): Include uppercase characters in the password.
- **lowercase** (`bool`, optional): Include lowercase characters in the password.
- **numbers** (`bool`, optional): Include numbers in the password.
- **special_characters** (`bool`, optional): Include special characters in the password.

#### Response

- **Body:**

  ```json
  {
    "password": "GeneratedPassword123"
  }
  ```

#### Sending a POST Request

Use a tool like curl or Postman to send a POST request to the `/generate-password` endpoint with the required parameters.

### 3. Running Tests for Generate Password Endpoint

#### How to Run the Tests

Ensure your FastAPI application is running.
Open a terminal and navigate to the directory containing your pytest file.

Run the following command:

```bash
pytest --verbose tests/
```

### 4. COVID-19 Statistics

#### Get Countries Affected by COVID-19

- **Endpoint:** `/countries`
- **Method:** GET

##### Parameters

- **search** (`str`, optional): Name of a country to search.

##### Response

- **Type:** List
- **Description:** List of countries affected by COVID-19.

#### Get COVID-19 Statistics

- **Endpoint:** `/statistics`
- **Method:** GET

##### Parameters

- **country** (`str`): Name of a country to get statistics for. Default is 'all' for global statistics.

##### Response

- **Type:** Dictionary
- **Description:** Current statistics of COVID-19 spread in the specified country.

## API Documentation

Additional documentation for API endpoints can be found within the codebase.

## APIs Used

- **RapidAPI**
  - **Key:** You need to sign up on [RapidAPI](https://rapidapi.com/) and obtain the key.
  - **Host:** `<RAPIDAPI_HOST>`
  - **Endpoints:** `/countries` and `/statistics`

## Authors

- [Baha Rehaan](https://github.com/rehaan17) - baha.rehaan17@gmail.com
