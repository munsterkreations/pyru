from setuptools import setup, find_packages

setup(
    name='Pyru',  # Replace 'your_package_name' with the name of your package
    version='0.1.0',  # Replace '0.1.0' with the version number of your package
    packages=find_packages(),  # Automatically discover and include all Python packages
    install_requires=[],  # List any dependencies your package requires
    author='munsterkreations',  # Replace 'Your Name' with your name
    author_email='munsterkreations@users.noreply.github.com',  # Replace 'your@email.com' with your email
    description='Pyru-friendly interface for Ruby libraries"',  # Add a short description
    long_description='A Ruby gem that provides a Pyru-friendly interface for Ruby libraries."',  # Add a long description if necessary
    long_description_content_type='text/markdown',  # Specify the type of long description
    url="https://github.com/munsterkreations/pyru",  # Replace with the URL of your package's repository
    classifiers=[  # Optional: add classifiers to categorize your package
        'Programming Language :: Python :: 3 :: Ruby ::', 
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
