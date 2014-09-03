#! /usr/bin/env python

##############################################################################
##  DendroPy Phylogenetic Computing Library.
##
##  Copyright 2010 Jeet Sukumaran and Mark T. Holder.
##  All rights reserved.
##
##  See "LICENSE.txt" for terms and conditions of usage.
##
##  If you use this work or any portion thereof in published work,
##  please cite it as:
##
##     Sukumaran, J. and M. T. Holder. 2010. DendroPy: a Python library
##     for phylogenetic computing. Bioinformatics 26: 1569-1571.
##
##############################################################################

"""
Split calculation and management.
DEPRECATED IN DENDROPY 4: USE `dendropy.calculate.coalescent` instead.
"""

from dendropy.model.coalescent import *
from dendropy.utility import error
error.dendropy_module_migration_warning("dendropy.coalescent", "dendropy.model.coalescent")