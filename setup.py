from setuptools import setup
from setuptools import find_packages


VERSION = '1.1.2'

setup(
    name='Keys',  # package name
    version=VERSION,  # package version
    description='my package',  # package description
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'Keys': ['statics/*.json', 'statics/*.png']
    },
    entry_points = {
        'gui_scripts': [
            'keys = Keys.main:main',
            'keys-config = Keys.main:edit_config'
        ],
    },
    install_requires = [
        'PyQt5==5.15.4',
        "system-hotkey==1.0.3",
        "PyAutoGUI==0.9.50"
    ],
)

# bdist_wheel