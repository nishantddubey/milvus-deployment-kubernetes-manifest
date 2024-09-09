from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
import random

# Connect to Milvus
try:
    connections.connect(alias="default", host="192.168.49.2", port="30003")
    print("Successfully connected to Milvus.")
except Exception as e:
    print(f"Error connecting to Milvus: {e}")
    exit(1)

# Create a collection schema
fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="random", dtype=DataType.DOUBLE),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8)
]
schema = CollectionSchema(fields, description="hello_milvus is the simplest demo to introduce the APIs")

# Check if the collection already exists
collection_name = "hello_milvus"
if utility.has_collection(collection_name):
    print(f"Collection {collection_name} already exists.")
    hello_milvus = Collection(name=collection_name)
else:
    # Create a new collection
    try:
        hello_milvus = Collection(name=collection_name, schema=schema)
        print(f"Collection {collection_name} created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")
        exit(1)

# Insert data
data = [
    [i for i in range(10)],  # primary key field: 10 int64 values
    [random.random() for _ in range(10)],  # random field: 10 float values
    [[random.random() for _ in range(8)] for _ in range(10)]  # embeddings field: 10 vectors, each with 8 dimensions
]

try:
    insert_result = hello_milvus.insert(data)
    print(f"Inserted data into {collection_name}. Insert result: {insert_result.primary_keys}")
except Exception as e:
    print(f"Error inserting data: {e}")
    exit(1)

# Flush the collection to ensure data persistence
try:
    hello_milvus.flush()
    print(f"Flushed data for {collection_name}.")
except Exception as e:
    print(f"Error flushing data: {e}")
    exit(1)

# Create an index on the embeddings field
try:
    index_params = {
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128},
        "metric_type": "L2"
    }
    hello_milvus.create_index(field_name="embeddings", index_params=index_params)
    print(f"Index created on collection {collection_name}.")
except Exception as e:
    print(f"Error creating index: {e}")
    exit(1)

# Load the collection into memory
try:
    hello_milvus.load()
    print(f"Collection {collection_name} loaded into memory.")
except Exception as e:
    print(f"Error loading collection into memory: {e}")

# Query the collection to retrieve inserted entities
try:
    results = hello_milvus.query(expr="pk >= 0", output_fields=["pk", "random", "embeddings"])
    print(f"Queried entities: {results}")
except Exception as e:
    print(f"Error querying collection: {e}")
