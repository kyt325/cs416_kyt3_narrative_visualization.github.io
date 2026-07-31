import kagglehub

# Download latest version
path = kagglehub.dataset_download("rishavsvault/most-streamed-artists-on-spotify")

print("Path to dataset files:", path)