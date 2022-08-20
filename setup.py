
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='prewl',
      version='0.0.4',
      description='General library wrapping and calling LLMs for prompt engineering.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/queens-supercluster/prewl',
      author='Erin Atacan and Christian Muise',
      author_email='christian.muise@queensu.ca',
      license='MIT',
      packages=['prewl', 'prewl.endpoints'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
      ],
      python_requires='>=3.6',
      install_requires=['requests'],
      zip_safe=False)
