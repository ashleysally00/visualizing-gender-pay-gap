import pandas as pd  # For loading and exploring the dataset
import nltk  # For text processing
from nltk.corpus import stopwords  # To remove common words

# Step 1: Download NLTK stopwords (only run this once)
nltk.download('stopwords')

# Step 2: Load the paygap dataset (Make sure 'paygap.csv' is in the same folder)
data = pd.read_csv('paygap.csv')

# Step 3: Check the first few rows to explore the dataset
print("Dataset Preview:")
print(data.head())

# Step 4: Check the column names to understand the data structure
print("\nColumns in the Dataset:")
print(data.columns)

# Step 5: Preprocess the text column (if your dataset has text data)
# Adjust 'text_column_name' to match the actual text column in your dataset
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Remove stopwords and convert to lowercase."""
    return ' '.join(word.lower() for word in text.split() if word.lower() not in stop_words)

# Apply text cleaning (Update 'text_column_name' with the appropriate column name)
if 'text_column_name' in data.columns:
    data['cleaned_text'] = data['text_column_name'].apply(clean_text)
    print("\nCleaned Text Preview:")
    print(data[['text_column_name', 'cleaned_text']].head())
else:
    print("\nNo text column found to clean.")

# Step 6: Optional - Describe numeric columns (e.g., wage_gap, etc.)
print("\nSummary Statistics:")
print(data.describe())
