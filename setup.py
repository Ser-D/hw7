from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Very useful code',
    url='http://github.com/no_name',
    author='me',
    author_email='metest_noname@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean_folder = clean_folder.sort:run_func']}
)