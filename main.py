import os
import httpx
from util import *
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=['*'],
  allow_credentials=True,
  allow_headers=['Authorization', 'Content-Type']
)

load_dotenv()
NUMBER_URL = os.getenv('NUMBER_URL')

class NumberModel(BaseModel):
  number: int
  is_prime: bool
  is_perfect: bool
  properties: list
  digit_sum: int
  fun_fact: str

@app.get('/api/classify-number', response_model=NumberModel)
async def get_number_detail(number: str = '0'):
  try:
    number = int(number)
  except ValueError:
    return JSONResponse(
      status_code=400,
      content={"number": number, "error": True}
    )

  async with httpx.AsyncClient() as client:
    response = await client.get(f'{NUMBER_URL}/{number}/math')
  fun_fact = response.text  # Get the plain text

  num_prop = []
  if number % 2 == 0:
    num_prop.append('even')
  else:
    num_prop.append('odd')

  if is_armstrong(number):
    num_prop.insert(0, 'armstrong')
  return NumberModel(
    number=number,
    is_prime=is_prime(number),
    is_perfect=is_perfect(number),
    properties=num_prop,
    digit_sum=digit_sum(number),
    fun_fact=fun_fact
  )
