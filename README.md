# Password Generator & COVID-19 Statistics API

Welcome to the Password Generator & COVID-19 Statistics API! This API provides two main functionalities: password generation and access to COVID-19 statistics for various countries. With these features, users can generate secure passwords and stay informed about the  COVID-19 data worldwide.

## Password Generator API

The Password Generator API allows users to generate strong and secure passwords based on their specific criteria. With customizable options such as password length and character types, users can create passwords tailored to their needs.

### Introduction

The Password Generator API simplifies the process of creating secure passwords for various applications. Built on FastAPI and Python, it ensures reliability and efficiency in password generation tasks. Whether you need passwords for user accounts, authentication systems, or any other purpose, this API has you covered.

### Key Features

- **Customizable Password Generation**: Generate passwords with specified length and character options, including uppercase letters, lowercase letters, numbers, and special characters.
- **Secure and Reliable**: Built using industry-standard encryption techniques and tested for reliability, ensuring the security of generated passwords.
- **User-Friendly Interface**: Intuitive API endpoints make it easy to integrate password generation functionality into your applications with minimal effort.

### Getting Started

To start using the Password Generator API, follow the installation instructions provided below. Once set up, you can integrate the API into your projects and begin generating secure passwords instantly.

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

3. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

### Usage

#### Password Generation

Use the `/generate-password` endpoint to create passwords with custom length and character options. Simply specify the desired password length and select the character types you want to include.

#### API Documentation

Comprehensive documentation for each endpoint is available within the codebase. Refer to the inline comments and docstrings for detailed information on request parameters, response formats, and error handling.

#### Testing with Swagger UI

The Password Generator API can be easily tested using Swagger UI, a user-friendly interface for exploring and testing API endpoints. To access Swagger UI, navigate to `http://localhost:8000/docs` in your web browser after starting the FastAPI server.

### Examples

#### Positive Example (Valid Request)

**Request:**

```json
{
  "length": 16,
  "uppercase": true,
  "lowercase": true,
  "numbers": true,
  "special_characters": true
}
```

**Response:**

```json
{
  "password": "R3&x@2sL9qI#8gF1",
  "length": 16
}
```

#### Negative Example (Invalid Request)

**Request:**

```json
{
  "length": 14,
  "uppercase": false,
  "lowercase": false,
  "numbers": false,
  "special_characters": false
}
```

**Response:**

```json
{
  "detail": "At least one character type should be included"
}
```

## COVID-19 Statistics API

The COVID-19 Statistics API provides access to real-time data on COVID-19 cases, deaths, and recoveries for various countries. Users can retrieve up-to-date information on the pandemic's impact worldwide.

### Introduction

Stay informed about the latest COVID-19 statistics with the COVID-19 Statistics API. Built on FastAPI and Python, this API offers reliable access to accurate data sourced from reputable sources.

### Key Features

- **Real-Time Data**: Access up-to-date statistics on COVID-19 cases, deaths, and recoveries for individual countries or globally.
- **Customizable Queries**: Retrieve data for specific countries or regions by specifying query parameters.
- **Easy Integration**: Intuitive API endpoints make it simple to integrate COVID-19 statistics functionality into your applications or dashboards.

### Getting Started with COVID-19 Statistics API

To start using the COVID-19 Statistics API, you need to obtain a RapidAPI key. RapidAPI provides access to various APIs, including the COVID-19 Statistics API. Follow the steps below to obtain your RapidAPI key:

1. Sign up on [RapidAPI](https://rapidapi.com/).
2. Once logged in, navigate to the COVID-19 Statistics API page.
3. Subscribe to the API to obtain your RapidAPI key.
4. Use the provided key (`RAPIDAPI_KEY`) in your requests to access COVID-19 statistics data.

### Usage

#### Get Countries Affected by COVID-19

Use the `/countries` endpoint to retrieve a list of countries affected by COVID-19. You can also search for specific countries using query parameters.

#### Get COVID-19 Statistics

Use the `/statistics` endpoint to retrieve current statistics of COVID-19 spread in a specific country. You can specify the country name as a query parameter to retrieve country-specific data.

### Authors

- [Baha Rehaan](https://github.com/rehaan17) - baha.rehaan17@gmail.com
