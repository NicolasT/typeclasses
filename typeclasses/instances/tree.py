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

'''Definition and typeclass instance definitions of the 'Tree' type'''

from typeclasses import instance
from typeclasses.eq import Eq, eq
from typeclasses.functor import Functor, fmap

class Tree(object):
    pass

class Leaf(Tree):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Leaf %r' % self.value

    def __repr__(self):
        return 'Leaf %r' % self.value


class Branch(Tree):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return 'Branch (%r) (%r)' % (self.left, self.right)

    def __repr__(self):
        return 'Branch (%r) (%r)' % (self.left, self.right)


instance(Functor, Tree, lambda f, o: Leaf(f(o.value)) if isinstance(o, Leaf)
         else Branch(fmap(f, o.left), fmap(f, o.right)))

instance(Eq, Tree,
         lambda a, b:
             a.value == b.value if (
                 isinstance(a, Leaf) and isinstance(b, Leaf))
             else (eq(a.left, b.left) and eq(a.right, b.right)) if (
                 isinstance(a, Branch) and isinstance(b, Branch))
            else False,
         None)
