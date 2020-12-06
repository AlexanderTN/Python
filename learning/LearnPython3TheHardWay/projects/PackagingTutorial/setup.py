import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-TamNguy", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="nguyenhoangtam@me.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    script="bin/math.py",
    python_requires='>=3.6',
    zip_safe=False
)
