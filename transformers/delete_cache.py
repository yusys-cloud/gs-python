import shutil
import transformers

# Get the default cache directory
cache_directory = transformers.file_utils.default_cache_path
print(cache_directory)
# Delete the cache directory
shutil.rmtree(cache_directory)