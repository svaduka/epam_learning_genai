from setuptools import setup, find_packages

setup(
    name='epam_learning_genai',
    version='0.1.0',
    author='Sainagaraju Vaduka',
    author_email='sainagaraju.vaduak@gmail.com',
    description='This is the test for GenAI Solutions Development Bootcamp [Global]',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/svaduka/epam_learning_genai.git',
    packages=find_packages(),
    install_requires=[
        'langchain==0.3.0',
        'requests==2.32.3',
        'openai==1.45.0',
        'pytest==8.2.0'
    ],
    classifiers=[
        'Development Status :: 1- Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={ 
        'console_scripts': [
            'my_script=src.main:main', 
        ],
    },
    include_package_data=True, 
    zip_safe=False 
)
