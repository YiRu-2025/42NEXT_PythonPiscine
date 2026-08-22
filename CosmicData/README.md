# Description
**topic**: Discover Pydantic Models & Validation

**summary**:

Master Pydantic data validation through space-themed exercises. Learn to create robust models, implement custom validation, and handle nested structures while managing cosmic data streams.

**tools**:

This activity includes data generation tools to help you test your Pydantic models:
- data_generator.py - Generate realistic test data for all exercises
- data_exporter.py - Export data in JSON, CSV, and Python formats
- generated_data/ - Pre-generated datasets ready to use

## Key concepts about Pydantic
1. BaseModel
    
    the foundation of all Pydantic models. Inherit from BaseModel to create validated data classes.

2. Field

    Use Field(...) to add validation constraints, descriptions, and default values to model attributes.

    Numeric Constraints

3. model_validator
    
    Use the @model_validator(mode=’after’) decorator for custom validation logic that runs after Pydantic’s built-in validation. This replaces the deprecated @validator decorator from Pydantic v1

# Instruction

This project includes 3 exercises using Pydantic v2 from basic to advanced level.

Before running the python file, make sure to create and activate a virtual environment and install the Pydantic v2 via pip.
## activate virtual env and install pydantic
```bash
python3 -m venv virtual_env
source virtual_env/bin/activate
pip install pydantic
```
## generate and export data for testing
run the python file under data_generator folder to generate and export testing examples
```bash
python3 data_generator/data_generator.py
python3 data_generator/data_exporter.py
```

it will create a folder named generated_data and and put all kinds of testing data

## testing
if not generate the data, you can also directly run the exercise file with two created examples inside.

if use the generator to get some testing examples, you can directly run `python3 testing.py` to do the test.

# Code explanation
## Field arguments for numeric constraints
There are some keyword arguments that can be used to constrain numeric values:

    gt - greater than
    lt - less than
    ge - greater than or equal to
    le - less than or equal to
    multiple_of - a multiple of the given number
    allow_inf_nan - allow 'inf', '-inf', 'nan' values
## Pydantic type conversion
It will try to validate and convert the input, if can't, it raise a ValidationError