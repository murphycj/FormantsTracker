import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="formantstracker",
    packages=setuptools.find_packages(),
    version="1.0.0",
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murphycj/FormantsTracker",
    project_urls={},
    include_package_data=True,
    install_requires=[
        "boltons==21.0.0",
        "hydra-core==1.3.2",
        "matplotlib==3.6.2",
        "numpy==1.23.4",
        "PyYAML==6.0",
        "PyYAML==6.0",
        "scipy==1.10.1",
        "torch==1.13.1",
        "torchaudio==0.13.1",
        "tqdm==4.64.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
