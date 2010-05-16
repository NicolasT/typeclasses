# typeclasses, an educational implementation of Haskell-style type
# classes, in Python
#
# Copyright (C) 2010 Nicolas Trangez  <eikke eikke com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, version 2.1
# of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301  USA

'''Some demonstrations of the Functor typeclass and its `fmap` function'''

from typeclasses.eq import eq
from typeclasses.functor import fmap

# Make sure instances are registered
import typeclasses.instances.list
import typeclasses.instances.tuple
import typeclasses.instances.function
from typeclasses.instances.maybe import Nothing, Just
from typeclasses.instances.tree import Branch, Leaf

# The function we'll map
f = lambda i: i + 1

# Instances
# =========
# fmap on lists = map to list
demo_list = [0, 1, 2, 3]
assert fmap(f, demo_list) == [1, 2, 3, 4]

# fmap on tuples = map to tuple
demo_tuple = tuple(demo_list)
assert fmap(f, demo_tuple) == (1, 2, 3, 4)

# fmap on functions = function composition
# fmap(f, g) = lambda x: f(g(x))
assert fmap(f, lambda i: i * 3)(1) == 4

# fmap on Maybe = function application on Just, Nothing on Nothing
assert fmap(f, Nothing) == Nothing
assert eq(fmap(f, Just(1)), Just(2))

# fmap on Tree = recursive fmap on branches, application on value in leafs
# I.e., if the original is
#
#    /\
#   / 4
#  /\
# 2 3
#
# applying fmap f will yield
#
#    /\
#   / 5
#  /\
# 3 4
demo_tree = Branch(Branch(Leaf(2), Leaf(3)), Leaf(4))
assert eq(fmap(f, Leaf(1)), Leaf(2))
assert eq(fmap(f, demo_tree), Branch(Branch(Leaf(3), Leaf(4)), Leaf(5)))


# Using infix-style operators
assert (lambda i: i * 2) <<fmap>> (lambda i: i + 1) <<fmap>> demo_list == \
    [2, 4, 6, 8]
assert f <<fmap>> Just(1) <<eq>> Just(2)
assert f <<fmap>> f <<fmap>> Nothing <<eq>> Nothing


# Functor laws
# ============
# fmap id = id
# --------------------
id_ = lambda o: o
fmap_id = lambda x: fmap(id_, x)

# List
assert fmap_id(demo_list) == id_(demo_list)
# Tuple
assert fmap_id(demo_tuple) == id_(demo_tuple)
# Function
# fmap(id_, f) != f, it's a new function with the same behaviour:
#    lambda x: id_(f(x))
assert fmap_id(f)(1) == id_(f(1))
# Maybe
assert eq(fmap_id(Nothing), id_(Nothing))
assert eq(fmap_id(Just(1)), id_(Just(1)))
# Tree
assert eq(fmap_id(demo_tree), id_(demo_tree))

# fmap (g . h) = fmap g . fmap h
# ------------------------------
g = lambda i: i + 2
h = lambda i: i * 3

g_dot_h = lambda x: g(h(x))
fmap_g_dot_h = lambda x: fmap(g_dot_h, x)

fmap_g_dot_fmap_h = lambda x: fmap(g, fmap(h, x))

# List
assert fmap_g_dot_h(demo_list) == fmap_g_dot_fmap_h(demo_list)
# Tuple
assert fmap_g_dot_h(demo_tuple) == fmap_g_dot_fmap_h(demo_tuple)
# Function
# As above, we need to apply the function. This is no proof of equality, I
# know...
assert fmap_g_dot_h(f)(1) == fmap_g_dot_fmap_h(f)(1)
# Maybe
assert eq(fmap_g_dot_h(Nothing), fmap_g_dot_fmap_h(Nothing))
assert eq(fmap_g_dot_h(Just(1)), fmap_g_dot_fmap_h(Just(1)))
# Tree
assert eq(fmap_g_dot_h(demo_tree), fmap_g_dot_fmap_h(demo_tree))
