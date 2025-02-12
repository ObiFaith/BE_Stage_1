import os
import httpx
import asyncio
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
async def get_number_detail(number: str | None = None):
  if number is None or number == "":
    return JSONResponse(
      status_code=400,
      content={"number": None, "error": True}
    )

  try:
    number = int(number)
  except ValueError:
    return JSONResponse(
      status_code=400,
      content={"number": number, "error": True}
    )

  async with httpx.AsyncClient() as client:
    response = await client.get(f'{NUMBER_URL}/{number}/math')
  fun_fact = response.text

  is_prime_result, is_perfect_result, properties_result, digit_sum_result = await asyncio.gather(
    is_prime(number), is_perfect(number), get_num_prop(number), digit_sum(number)
  )

  return NumberModel(
    number=number,
    is_prime=is_prime_result,
    is_perfect=is_perfect_result,
    properties=properties_result,
    digit_sum=digit_sum_result,
    fun_fact=fun_fact
  )
