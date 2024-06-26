# main.py
from fastapi import FastAPI, HTTPException
from models import ConversionRequest, ConversionResponse

app = FastAPI()

# Conversion factors
conversion_factors = {
    'length': {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084
    },
    'weight': {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274
    },
    'time': {
        'seconds': 1,
        'minutes': 1/60,
        'hours': 1/3600
    }
}

@app.post("/convert", response_model=ConversionResponse)
def convert(request: ConversionRequest):
    value = request.value
    unit = request.unit.lower()
    convert_to = request.convert_to.lower()

    if unit == convert_to:
        return ConversionResponse(value=value, unit=convert_to)

    # Length conversion
    if unit in conversion_factors['length'] and convert_to in conversion_factors['length']:
        base_value = value / conversion_factors['length'][unit]
        converted_value = base_value * conversion_factors['length'][convert_to]
        return ConversionResponse(value=converted_value, unit=convert_to)
    
    # Weight conversion
    if unit in conversion_factors['weight'] and convert_to in conversion_factors['weight']:
        base_value = value / conversion_factors['weight'][unit]
        converted_value = base_value * conversion_factors['weight'][convert_to]
        return ConversionResponse(value=converted_value, unit=convert_to)
    
    # Time conversion
    if unit in conversion_factors['time'] and convert_to in conversion_factors['time']:
        base_value = value / conversion_factors['time'][unit]
        converted_value = base_value * conversion_factors['time'][convert_to]
        return ConversionResponse(value=converted_value, unit=convert_to)
    
    # Temperature conversion
    if unit == 'celsius' and convert_to == 'fahrenheit':
        converted_value = (value * 9/5) + 32
        return ConversionResponse(value=converted_value, unit=convert_to)
    elif unit == 'fahrenheit' and convert_to == 'celsius':
        converted_value = (value - 32) * 5/9
        return ConversionResponse(value=converted_value, unit=convert_to)
    
    raise HTTPException(status_code=400, detail="Invalid unit or conversion type")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
