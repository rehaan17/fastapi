# Password Generator & COVID-19 Statistics API

Welcome to the Password Generator & COVID-19 Statistics API! This API provides two main functionalities: password generation and access to COVID-19 statistics for various countries. With these features, users can generate secure passwords and stay informed about the latest COVID-19 data worldwide.

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

### Example

**Request:**

```json
{
  "length": 12,
  "uppercase": true,
  "lowercase": true,
  "numbers": true,
  "special_characters": true
}
```

**Responses:**

1. Password: `Ex@mpleP@ssw0rd123`
2. Password: `S3cureP@ssword!`

## COVID-19 Statistics API

The COVID-19 Statistics API provides access to real-time data on COVID-19 cases, deaths, and recoveries for various countries. Users can retrieve up-to-date information on the pandemic's impact worldwide.

### Introduction

Stay informed about the latest COVID-19 statistics with the COVID-19 Statistics API. Built on FastAPI and Python, this API offers reliable access to accurate data sourced from reputable sources.

### Key Features

- **Real-Time Data**: Access up-to-date statistics on COVID-19 cases, deaths, and recoveries for individual countries or globally.
- **Customizable Queries**: Retrieve data for specific countries or regions by specifying query parameters.
- **Easy Integration**: Intuitive API endpoints make it simple to integrate COVID-19 statistics functionality into your applications or dashboards.

### Usage

#### Get Countries Affected by COVID-19

Use the `/countries` endpoint to retrieve a list of countries affected by COVID-19. You can also search for specific countries using query parameters.

#### Get COVID-19 Statistics

Use the `/statistics` endpoint to retrieve current statistics of COVID-19 spread in a specific country. You can specify the country name as a query parameter to retrieve country-specific data.

### Example

**Request:**

```json
{
  "country": "USA"
}
```

**Response:**

```json
{
  "country": "USA",
  "cases": 4000000,
  "deaths": 200000,
  "recovered": 3000000
}
```

### Authors

- [Baha Rehaan](https://github.com/rehaan17) - baha.rehaan17@gmail.com
