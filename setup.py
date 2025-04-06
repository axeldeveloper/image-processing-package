from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='proc_img_plot',
    version='0.0.1',
    author="Axel Alexander",
    author_email="axelpatton@gmail.com",
    description="Procesador de imagem e combinação",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
)