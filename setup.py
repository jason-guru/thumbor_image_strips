from setuptools import find_packages, setup
setup(
    name='watermark_image_strips_filter',
    packages=find_packages(),
    version='0.1.0',
    description='Product image text strips filter.',
    author='G.Jason.Sharma',
    license='MIT',
    include_package_data=True,
    install_requires=[
        'pillow',
    ],
)