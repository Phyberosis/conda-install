import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

pks = ['test_package']

setuptools.setup(
    name="testpk-txyl",
    version="0.0.1",
    author="Tony Liu",
    author_email="contacttonyliu@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tony-xy-Liu/Limes",
    project_urls={
        "Bug Tracker": "https://github.com/Tony-xy-Liu/Limes/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=pks,
    package_data={
        # "":["*.txt"],
        # "package-name": ["*.txt"],
        "test_package": ["res/*.txt"],
    },
    python_requires=">=3.9",
)