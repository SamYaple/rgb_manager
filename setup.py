#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="rgb_manager",
    version="0.1.0",
    url="https://github.com/SamYaple/rgb_manager",
    description="Control MSI keyboard and lightbar RGB leds",
    install_requires=[
        "pyusb",
    ],
    author="Sam Yaple",
    author_email="rbgmgr@yaple.net",
    python_requires=">=3.10",
    license="MIT license",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=[
        "rgb_manager",
    ],
    long_description="Control MSI keyboard and lightbar RGB leds",
)
