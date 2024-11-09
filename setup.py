from setuptools import setup, find_packages

setup(
    name='PyColorate',
    version='0.1.0',
    author='borgox',
    author_email='',
    description='A lightweight python library to easily colorate text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/borgox/PyColorate',  # Your package's homepage
    packages=find_packages(),  # Automatically find packages in your_module
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',  # Change this based on your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
)