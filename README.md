# FastAPI Application

This is a FastAPI application that demonstrates basic usage.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/OAkinbode/ET-AIModel.git
cd ET-AIModel

```

### 2. Install all dependencies using either of the following:

pip install -r requirements.txt

or

pip3 install -r requirements.txt

### 3. Run the application using for mac

uvicorn app.main:app --reload

### 3. Run the application using for windows

python.exe -m uvicorn.main app.main:app --reload

### 4. Use application in browser

visit http://localhost:8000

### 5. How this application works and what to do with it.

You will be provided a json file in addition to this code. When you upload the json file, the middleware simply returns the file. Your task is to write code in the middleware file (processPrompt) that uses publicly available LLM apis e.g. LLama, or OpenAI, or other open-source models (perhaps from Huggingface.io), to do the following:

##1. Look at each of the json objects in the array, and use the description/product details/taxonomy fields to find more information on the internet about that equipment/product. You are to produce more information about each product and write that into the product json object in a new field called "augmented_data".
##2. This new field must contain data that improves on what we already have in that object under the fields description/product details/taxonomy.
##3. This workflow would involve scrapping data about the product described in realtime dynamically.

Optional:
##4. if the price of the product object is 0, scrap that data from the internet and provide a price recommendation. If your middle ware finds a price suggestion, then write that into the price field. 
##5. If you can, find the product weight and write that into a new field called product_weight.
