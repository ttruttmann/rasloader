RasLoader: Load Rigaku .ras files
==================================

RasLoader is a python package that loads .ras files from Rigaku diffractometers. It returns a RasLoader object that contains metadata, axis data, and intensity data.

To install:

.. code-block:: zsh

    $ pip install git+https://github.com/ttruttmann/rasloader

To load files:

.. code-block:: python

    >>> from rasloader import RasLoader
    >>> XRD_scan  = RasLoader('example_scan.ras')

A RasLoader object consists of three instances variables. The first is ``metadata``, which stores miscallaneous information in a python dictionary:

.. code-block:: python

    >>> XRD_scan.metadata['FILE_SAMPLE']
    'LAO Substrate'
    >>> XRD_scan.metadata['HW_GONIOMETER_NAME']
    'StandardInplane'

The second is ``axisdata``, which stores the position, resolution, etc. of the each of the various instrument axes in a pandas DataFrame:

.. code-block:: python

    >>> XRD_scan.axisdata.head()
                        name_internal  offset position resolution  state unit
    name                                                                    
    ThetaS                    ThetaS  0.9267      0.0     0.0001  Fixed  deg
    ThetaD                    ThetaD  0.2322      0.0     0.0001  Fixed  deg
    PrimaryGeometry  PrimaryGeometry       0    Right             Fixed     
    Version_HV            Version_HV       0      NaN        1.0  Fixed     
    Version_CW            Version_CW       0      NaN        1.0  Fixed     
    >>> XRD_scan.axisdata.loc['Rx']['position']
    0.02178

The final is ``intdata`` which stores the intensity data in a pandas DataFrame:

.. code-block:: python

    >>> XRD_scan.intdata
          TwoThetaOmega        I
    0             10.00   9.5853
    1             10.02   8.7793
    2             10.04  13.7946
    3             10.06  11.7690
    4             10.08   7.3853
    ...             ...      ...
    4496          99.92   1.0309
    4497          99.94   2.1402
    4498          99.96   0.0000
    4499          99.98   1.0459
    4500         100.00   2.1602

It is easy to load multipe files into one RasLoader object: 

.. code-block:: python

    >>> XRD_scan.append_file_inline('example_scan.ras')
    >>> XRD_scan.intdata
          TwoThetaOmega        I
    0             10.00   9.5853
    1             10.02   8.7793
    2             10.04  13.7946
    3             10.06  11.7690
    4             10.08   7.3853
    ...             ...      ...
    8997          99.92   1.0309
    8998          99.94   2.1402
    8999          99.96   0.0000
    9000          99.98   1.0459
    9001         100.00   2.1602

RasLoader also supports loading reciprocal space maps (RSMs), however **LOADING RSMs is currently very slow**, taking ~1 minute to load a typical RSM:

.. code-block:: python

    >>> XRD_RSM = RasLoader('example_rsm.ras')
    >>> XRD_RSM.intdata
        Omega  TwoTheta       I
    0        22.1     44.20  0.6716
    1        22.1     44.21  0.8835
    2        22.1     44.22  1.6768
    3        22.1     44.23  2.1423
    4        22.1     44.24  2.3673
    ...       ...       ...     ...
    145156   24.0     47.96  1.6649
    145157   24.0     47.97  1.3047
    145158   24.0     47.98  1.1406
    145159   24.0     47.99  1.0060
    145160   24.0     48.00  0.9083

