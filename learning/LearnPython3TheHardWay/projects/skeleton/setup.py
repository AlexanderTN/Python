try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Skeleton Project',
    'author': 'Nguyen Hoang Tam',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dragonazvn@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],    
    'name': 'Skeleton',
    'zip_safe':False
}

setup(**config)

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
#     version="0.0.1",
#     author="Example Author",
#     author_email="author@example.com",
#     description="A small example package",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     packages=setuptools.find_packages(),
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3.6',
# )
