import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="v2client",
    version="1.0.0",
    author="Mostafa Mosavi",
    author_email="mostafa.uwsgi@gmail.com",
    description="A V2Ray/V2Fly client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/its0x4d/v2client",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    python_requires='>=3.6',
)
