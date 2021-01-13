from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="templaton",
    version="0.1.0",
    author="Roy Assis",
    author_email="royassisg@gmail.com",
    description="Testing package creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

    include_package_data=True,
    entry_points = {

        'console_scripts': ['mktmp=dir_template_cli.command_line:main']
    }


)
