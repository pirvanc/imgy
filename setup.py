from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='imgy',
      version='0.1',
      description='Python client for imgy service api',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='image processing',
      url='https://github.com/pirvanc/imgy',
      author='Cristian Pirvan',
      author_email='pirvan.cristiani@gmail.com',
      license='MIT',
      packages=['imgy'],
      install_requires=[
          'boto3',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False)
