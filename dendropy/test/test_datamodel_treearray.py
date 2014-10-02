#! /usr/bin/env python

##############################################################################
##  DendroPy Phylogenetic Computing Library.
##
##  Copyright 2010-2014 Jeet Sukumaran and Mark T. Holder.
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

import unittest
from dendropy.test.support import pathmap
import dendropy

class TreeArrayBasicTreeAccession(unittest.TestCase):

    def get_trees(self, taxon_namespace=None):
        trees = dendropy.TreeList.get_from_path(pathmap.tree_source_path(
                "pythonidae.reference-trees.nexus"),
                "nexus",
                taxon_namespace=taxon_namespace)
        return trees

    def verify_tree_array(self, tree_array, source_trees):
        self.assertEqual(len(tree_array), len(source_trees))
        for idx, source_tree in enumerate(source_trees):
            source_tree.encode_splits()
            source_splits = list(source_tree.split_edge_map.keys())
            tss_splits, tss_edges = tree_array[idx]
            self.assertEqual(len(tss_splits), len(source_splits))
            self.assertEqual(set(tss_splits), set(source_splits))
            for idx, nd in enumerate(source_tree.preorder_node_iter()):
                source_split = nd.edge.split_bitmask
                tss_split = tss_splits[idx]
                tss_edge_length = tss_edges[idx]
                self.assertEqual(source_split, tss_split)
                if nd.edge.length is None:
                    self.assertEqual(tss_edge_length, 0)
                else:
                    self.assertAlmostEqual(tss_edge_length, nd.edge.length)

    def test_add_tree(self):
        trees = self.get_trees()
        tree_array = dendropy.TreeArray(taxon_namespace=trees.taxon_namespace)
        for tree in trees:
            tree_array.add_tree(tree)
        self.verify_tree_array(tree_array, trees)


if __name__ == "__main__":
    unittest.main()