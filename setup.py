from setuptools import setup, find_packages

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='ansi_colours',
    version='1.0.0',
    url='https://github.com/sarcoma/Python_ANSI_Colours',
    license='MIT',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    description='Library of static methods for colouring text in terminal output',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    project_urls={
        'Order & Chaos Creative': 'https://orderandchaoscreative.com',
    }
)
