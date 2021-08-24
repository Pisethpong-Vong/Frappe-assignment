from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in phone_shop/__init__.py
from phone_shop import __version__ as version

setup(
	name="phone_shop",
	version=version,
	description="Phone Shop System",
	author="nomotoji",
	author_email="nomotoji@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
