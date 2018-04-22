from setuptools import setup, find_packages

setup(
    name='ansi_colours',
    version='0.1',
    url='https://github.com/sarcoma/Python_ANSI_Colours',
    license='MIT',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    description='Library of static methods for colouring text in terminal output',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    project_urls={
        'Order & Chaos Creative': 'https://orderandchaoscreative.com',
    }
)
