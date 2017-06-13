from setuptools import setup, find_packages
setup(
  name="flix",
  packages=find_packages(exclude=["tests*"]),
  install_requires=[
    "click==6.7",
    "flixster==0.0.2",
    "colored==1.3.5",
    "python-dateutil==2.6.0",
    "terminaltables==3.1.0",
    "enum34==1.1.6"
  ],
  version="0.0.1",
  description="Movie CLI",
  author="Jae Bradley",
  author_email="jae.b.bradley@gmail.com",
  url="https://github.com/jaebradley/flix",
  download_url="https://github.com/jaebradley/flix/tarball/0.1",
  keywords=["flixster", "movies", "cli"],
  classifiers=[],
  entry_points={
    "console_scripts": [
        "flix = scripts.flix:flix"
    ],
  },
)