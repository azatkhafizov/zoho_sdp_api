from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r', encoding='UTF-8') as f:
    return f.read()


setup(
  name='ZohoSDPlusAPI',
  version='0.0.1',
  author='AzatXafizov',
  author_email='hafizov.azat.m@gmail.com',
  description='Этот модуль умеет работать с REST API Zoho SD Plus Manageengine через requests',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/azatkhafizov/zoho_sdp_api',
  packages=find_packages(),
  install_requires=['aiohttp==3.9.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='Zoho zoho rest REST api API requests',
  project_urls={
    'GitHub': 'https://github.com/azatkhafizov/zoho_sdp_api'
  },
  python_requires='>=3.6'
)