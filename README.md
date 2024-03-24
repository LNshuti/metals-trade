# Precious Metals Trade
Use Publicly Available data to create an interactive application explaining the global trade of precious metals

#### Technology Stack 
1. Prototype: Python Streamlit
2. Production deployment: Modal labs

#### Run the app on your machine!

```python
# Step 1: Clone the repo
git clone https://github.com/LNshuti/metals-trade.git

# Step 2: Create an isolated environment to manage dependencies
conda env create --file=environment.yaml

# Step 3: install required Python packages

pip install -r requirements.txt

# Step 4: Inspect the data
$ datasette .\data\processed\rankings.db

# Step 5: Run Python Application
$ streamlit run app.py

# Step 5: Deploy Flask Application with Modal 
$ modal serve app.py
```

#### References 
1. The Atlas of Economic Complexity. https://atlas.cid.harvard.edu/
