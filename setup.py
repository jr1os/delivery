from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="delivery",
    version="0.1.0",
    description="API for delivery created using the flask framework.",
    author="ali rios",
    author_email="ali.rios@gmail.com",
    url="https://github.com/jr1os/delivery",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
