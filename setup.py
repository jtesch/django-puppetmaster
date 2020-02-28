import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puppet_master",
    version="0.0.1",
    author="Josh Tesch",
    author_email="jtesch@overnitecbt.com",
    description="Django Puppet Master for routing react apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/overnite-software/django-puppetmaster",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["beautifulsoup4", "django>=2.2", "requests"],
    include_package_data=True
)