import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BenBotfnAPI-mistxbrain", # Replace with your own username
    version="0.0.1",
    author="mistxbrain",
    description="Python library used to communicate with the benbotfn.tk server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BigBrain21/BenBotfnAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
