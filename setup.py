import setuptools

GENERAL_REQUIRES = [
    'flask'
]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wpda",
    version="0.0.1",
    author="Nicholas Heller",
    author_email="helle246@umn.edu",
    description="Web-based Platform for Distributed Annotation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neheller/wpda",
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only"
    ),
    license="MIT",
    keywords="annotate annotation label semantic segmentation",
    install_requires=GENERAL_REQUIRES,
    python_requires='>=3',
    package_data={
        'wpda': ['data/default_configuration.json']
    },
    entry_points={
        'console_scripts': ['wpda=wpda.utils.cli:serve']
    }
)
