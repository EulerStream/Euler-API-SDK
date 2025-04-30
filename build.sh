echo "Fetching latest OpenAPI spec from EulerStream..."

# Get the spec
wget -O ./build/openapi.json https://tiktok.eulerstream.com/dashboard/openapi

# Generate
openapi-generator-cli generate -i ./build/openapi.json -g typescript-axios -o ./src/sdk