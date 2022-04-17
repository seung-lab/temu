import os
import setuptools
import sys

setuptools.setup(
  setup_requires=['pbr'],
  python_requires="~=3.7", # >= 3.7 < 4.0
  include_package_data=True,
  entry_points={
    "console_scripts": [
      "temu=temu:main"
    ],
  },
  pbr=True
)
