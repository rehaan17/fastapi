import logging
import secrets
import string
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI instance
app = FastAPI()

# Request model for generating password
class PasswordRequest(BaseModel):
    length: int
    uppercase: bool = Field(True, description="Include uppercase characters in the password.")
    lowercase: bool = Field(True, description="Include lowercase characters in the password.")
    numbers: bool = Field(True, description="Include numbers in the password.")
    special_characters: bool = Field(True, description="Include special characters in the password.")

# Response model for returning password
class PasswordResponse(BaseModel):
    password: str
    length: int

def generate_password(request: PasswordRequest) -> str:
    logger.info(f"Generating password with parameters: {request}")
    allowed_characters = ""

    if request.uppercase:
        allowed_characters += string.ascii_uppercase
    if request.lowercase:
        allowed_characters += string.ascii_lowercase
    if request.numbers:
        allowed_characters += string.digits
    if request.special_characters:
        allowed_characters += string.punctuation

    # Check if any character type is included
    if not any([request.uppercase, request.lowercase, request.numbers, request.special_characters]):
        raise HTTPException(status_code=400, detail="At least one character type should be included")

    # Generate password
    password = ''.join(secrets.choice(allowed_characters) for _ in range(request.length))

    return password

@app.post("/generate-password/", response_model=PasswordResponse, summary="Generate a secure password")
async def generate_password_route(request: PasswordRequest):
    try:
        length = request.length
        generated_password = generate_password(request)
        logger.info(f"Generated password with length {length}")
        return PasswordResponse(password=generated_password, length=length)
    except HTTPException as e:
        logger.error(f"HTTPException: {e}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Compulsory: Provide basic documentation for the root URL
@app.get("/", summary="Root endpoint", description="Welcome to the Password Generator API. Use /generate-password/ to generate a password.")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Password Generator API. Use /generate-password/ to generate a password."}

# Compulsory: Provide error handling for invalid routes
@app.exception_handler(404)
async def not_found(request, exc):
    logger.error("Invalid endpoint accessed")
    return {"message": "Endpoint not found"}, 404

# RapidAPI key and host
RAPIDAPI_KEY = "2ae43ad0e8msh2aee06c3f9197f1p1480a9jsn12d7ba80f98b"
RAPIDAPI_HOST = "covid-193.p.rapidapi.com"

# Get countries endpoint with error handling
@app.get("/countries")
def get_countries(search: str = Query(None)):
    """
    Get the list of countries affected by Coronavirus.

    Parameters:
    - search (str, optional): Name of a country to search.

    Returns:
    - list: List of countries affected by Coronavirus.
    """
    logger.info(f"Getting countries with search parameter: {search}")
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    url = f"https://{RAPIDAPI_HOST}/countries"
    if search:
        url += f"?search={search}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error retrieving countries: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except KeyError:
        logger.error("No countries found for the given search criteria")
        raise HTTPException(status_code=404, detail="No countries found for the given search criteria")

# Get statistics endpoint with error handling
@app.get("/statistics")
def get_statistics(country: str = Query("all")):
    """
    Get the current statistics of Coronavirus spread in a country.

    Parameters:
    - country (str): Name of a country to get statistics for. Default is 'all' for global statistics.

    Returns:
    - dict: Current statistics of Coronavirus spread in the specified country.
    """
    logger.info(f"Getting statistics for country: {country}")
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    url = f"https://{RAPIDAPI_HOST}/statistics"
    if country.lower() != "all":
        url += f"?country={country}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error retrieving statistics: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except KeyError:
        logger.error("No statistics found for the given country")
        raise HTTPException(404, "No statistics found for the given country")
