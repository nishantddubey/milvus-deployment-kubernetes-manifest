from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

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
collection_name = "hello_milvus22"
if utility.has_collection(collection_name):
    print(f"Collection {collection_name} already exists.")
else:
    # Create a new collection
    try:
        hello_milvus = Collection(name=collection_name, schema=schema)
        print(f"Collection {collection_name} created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")
        exit(1)
