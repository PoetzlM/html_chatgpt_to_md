# -*- coding: utf-8 -*-
"""
Created on Tue Jan 7 17:36:52 2025
@author: PoetzlM
"""

from setuptools import setup, find_packages

setup(
    name='html_chatgpt_to_md',
    version='0.1.0',
    packages=find_packages(),
    description='A simple HTML to Markdown converter specifically for chat logs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='PoetzlM',
    url='URL_zu_Ihrem_Projekt',  # Optional
    license='MIT',
    install_requires=[
        'beautifulsoup4',
        'markdownify'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)