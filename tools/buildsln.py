import os

try:
    VS_BUILD_PATH = os.environ["VS_BUILD_PATH"][8:-1]
except Exception as e:
    print(e)

print(VS_BUILD_PATH)