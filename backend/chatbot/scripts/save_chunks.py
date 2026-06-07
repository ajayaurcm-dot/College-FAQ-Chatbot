import os
import pickle

# Path
OUTPUT_PATH = "app/data/processed/chunks.pkl"

# Sample processed data
chunks = [
    {
        "text": "Students must follow hostel timings strictly.",
        "source": "rules.txt"
    },
    {
        "text": "Visitors are not allowed after 8 PM.",
        "source": "hostel.txt"
    },
    {
        "text": "Library is open from 8 AM to 8 PM.",
        "source": "library.txt"
    }
]

# Ensure folder exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Save file
with open(OUTPUT_PATH, "wb") as f:
    pickle.dump(chunks, f)

print("✅ chunks.pkl created successfully!")