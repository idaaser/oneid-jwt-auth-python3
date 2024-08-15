from setuptools import setup, find_packages

setup(
    name='oneid-jwt-auth-python3',
    version='0.0.1',
    description='oneid-jwt-auth-python3',
    author='oneid',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'PyJWT',
        'cryptography'
    ],
    python_requires='>3.0',
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ]
)
