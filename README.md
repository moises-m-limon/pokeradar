# pokeradar

Got to catch them call!

[Vending Machine](https://support.pokemoncenter.com/hc/en-us/sections/13360842288916-Pok%C3%A9mon-Automated-Retail-Vending-Machines)

## Create a Virtual Environment

First, create a virtual environment to isolate your project dependencies. Open a terminal and navigate to the project directory, then run:

For macOS/Linux:
```bash
python3 -m venv venv
```
For Windows:
```bash
python -m venv venv
```

This will create a venv folder in your project directory.

Activate the Virtual Environment

For macOS/Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash

venv\Scripts\activate
```

You should now see (venv) in your terminal, indicating that the virtual environment is active.

Install Dependencies

With the virtual environment activated, install the required dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```
This will install pandas, selenium, and any other libraries specified in the requirements.txt file.