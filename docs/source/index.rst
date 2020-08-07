.. FiniteDifferenceElectrostatics documentation master file, created by
   sphinx-quickstart on Fri Aug  7 09:07:12 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FiniteDifferenceElectrostatics's documentation!
==========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

    about_me

Introduction
============
This is an electrostatics solver written in python which uses the Finite Difference Method (FDM). You define as an "input" a set of "electrodes" - regions of space which have a known voltage. Currently these are defined programmatically in a python input script. By default the outer boundary of the simulation region is set to 0V. The solver then determines what the resulting voltage throughout all of space is, and from there can compute the electric fields, energy density, and capacitance.

Theory
======

.. math::
    \nabla x \overrightarrow{E} = 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
