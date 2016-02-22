from setuptools import setup


setup(name='typeformPython',
      version='0.1',
      description='A Python Wrapper for the Typeform API',
      url='http://github.com/grobbie94/typeformPython',
      author='Robert Banks',
      license='MIT',
      packages=['typeformPython'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose','unittest'],
      install_requires=['requests'])
