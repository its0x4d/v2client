import setuptools


setuptools.setup(
    name="v2client",
    version="0.0.1",
    author="Mostafa Mosavi",
    author_email="mostafa.uwsgi@gmail.com",
    description="A V2Ray/V2Fly client for Python",
    long_description="A V2Ray/V2Fly client for Python",
    long_description_content_type="text/markdown",
    url="https://github.com/its0x4d/v2client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
