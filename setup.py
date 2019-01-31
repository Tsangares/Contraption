import setuptools

setuptools.setup(
    name="contraption",
    version="0.0.1",
    author="William Wyatt",
    author_email="wwyatt@ucsc.edu",
    description="pyvisa support for powersupplies DPO and DAQs (Aglient, Keithley, Tektronix, Lecroy)",
    long_description="pyvisa support for powersupplies DPO and DAQs (Aglient, Keithley, Tektronix, Lecroy)",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Tsangares/Devices",
    #scripts=['probecard/bin/probecard'],
    install_requires=[
        "matplotlib==3.0.2",
        "numpy==1.15.4",
        "PyVISA==1.9.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
