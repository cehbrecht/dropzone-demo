from setuptools import setup, find_packages

setup(
    name='dzapp',
    version='0.1',
    description='Your Pyramid application with Dropzone.js integration',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'pyramid',
        'waitress',
        'pyramid_chameleon',
        'pyramid_storage',
        # Add other dependencies here
    ],
    entry_points={
        'paste.app_factory': [
            'main = dzapp:main'
        ],
    },
)
