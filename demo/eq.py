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

'''Some demonstrations of the Eq typeclass and its `eq` and `ne` functions'''

from typeclasses.eq import eq, ne

import typeclasses.instances.list
import typeclasses.instances.tuple
from typeclasses.instances.maybe import Just, Nothing
from typeclasses.instances.tree import Branch, Leaf

# List
assert eq([1, 2, 3], [1, 2, 3])
assert ne([0, 1, 2], [1, 2, 3])
# Tuple
assert eq((1, 2, 3, ), (1, 2, 3, ))
assert ne((0, 1, 2, ), (1, 2, 3, ))
# Maybe
assert eq(Nothing, Nothing)
assert eq(Just(1), Just(1))
assert ne(Just(1), Just(2))
assert ne(Just(1), Nothing)
# Tree
assert eq(Branch(Branch(Leaf(0), Leaf(1)), Leaf(2)),
          Branch(Branch(Leaf(0), Leaf(1)), Leaf(2)))
assert ne(Branch(Branch(Leaf(0), Leaf(1)), Leaf(2)),
          Branch(Branch(Leaf(0), Leaf(1)), Branch(Leaf(2), Leaf(3))))
