from setuptools import setup, find_packages

setup(
    name='map-boxes',
    version='1.0.6',
    description='Function to calculate mAP for set of detected boxes and annotated boxes.',
    author='123',
    packages=find_packages(include=['map_boxes', 'map_boxes.*']),
    install_requires=[
		'pandas',
		'numpy',
    ]
)
