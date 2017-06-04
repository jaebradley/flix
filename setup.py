from setuptools import setup, find_packages
setup(
  name="flix",
  packages=find_packages(exclude=["tests*"]),
  install_requires=["flixster", "click"],
  version="0.0.1",
  description="Movie CLI",
  author="Jae Bradley",
  author_email="jae.b.bradley@gmail.com",
  url="https://github.com/jaebradley/flix",
  download_url="https://github.com/jaebradley/flix/tarball/0.1",
  keywords=["flixster", "movies", "cli"],
  classifiers=[],
)