"""
test_perma_base.py
  tests of the perma_base component of permamodel
"""

from permamodel.components import frost_number
import os
import numpy as np

# ---------------------------------------------------
# Tests of reading precipitation from CRU geotiff files
# ---------------------------------------------------
def test_can_get_precipitation_filename_from_date_and_location():
    fn = frost_number.frostnumber_method()
    fn.initialize(cfg_file="/home/scotts/permamodel/permamodel/examples/Fairbanks_frostnumber_method.cfg",
                 SILENT=True)
    # Given year and month, calculate the tiff_filename
    fname = fn.get_precipitation_tiff_filename(fn.year, 6)
    assert(fname != None)

def test_get_precipitation_from_cru_indexes():
    fn = frost_number.frostnumber_method()
    fn.initialize(cfg_file="/home/scotts/permamodel/permamodel/examples/Fairbanks_frostnumber_method.cfg",
                 SILENT=True)

    # Test using data file for June of 2009
    month = 6
    year = 2009

    # We know that the temperature at x=2640 y=924 is 42.0
    i = 2640
    j = 924
    temp = fn.get_precipitation_from_cru_indexes(i, j, month, year)
    np.testing.assert_almost_equal(temp, 42.0, decimal=3)

    # We know that the temperature at x=2640 y=924 is 55.0
    i = 2612
    j = 1328
    temp = fn.get_precipitation_from_cru_indexes(i, j, month, year)
    np.testing.assert_almost_equal(temp, 55.0, decimal=3)

def test_get_precipitation_from_cru():
    fn = frost_number.frostnumber_method()
    fn.initialize(cfg_file="/home/scotts/permamodel/permamodel/examples/Fairbanks_frostnumber_method.cfg",SILENT=True)
    month = 6
    year = 2009

    # I can see the rightmost value on the geotiff at (4761, 1973)
    #   is 79.0 for precipitation
    i = 4761
    j = 1973
    (lon, lat) = fn.get_lon_lat_from_cru_indexes(i, j, month, year)
    temperature = fn.get_precipitation_from_cru(lon, lat, month, year)
    assert(abs(temperature - 79.0) < 1e-3)

