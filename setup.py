from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SimpleHTTP",
    version="0.2.5",
    author="Aman Goyal",
    author_email="amangoyal8110@gmail.com",
    description="Simple python http webserver. No BS. Unstable. Just works. No third party dependency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goyal-aman/SimpleHTTP",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "SimpleHTTP=SimpleHTTP.app:main",  # Adjust this if you have a CLI entry point
        ],
    },
)