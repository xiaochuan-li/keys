from setuptools import setup
from setuptools import find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
VERSION = "1.1.6"

setup(
    name="keys-manager",
    version=VERSION,
    packages=find_packages(),
    author="Xiaochuan Li",
    author_email="lixiaochuan822@gmail.com",
    description="A simple key manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaochuan-li/keys",
    zip_safe=False,
    package_data={"Keys": ["statics/*.json", "statics/*.png"]},
    entry_points={
        "gui_scripts": ["keys = Keys.main:main", "keys-config = Keys.main:edit_config"],
    },
    install_requires=["PyQt5==5.15.4", "keyboard==0.13.5", "PyAutoGUI==0.9.50"],
)

# bdist_wheel
