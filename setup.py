from setuptools import setup, find_packages

setup(
    name='spanda_ai_backend',
    version='0.1',
    packages=find_packages(where="src/backend"),
    package_dir={"": "src/backend"},
    install_requires=[
        'flask',
        'fastapi',
        'sqlalchemy',
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'torch',
        'transformers',
        'diffusers',
    ],
)
