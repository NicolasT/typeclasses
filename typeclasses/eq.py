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

'''Definition of the Eq typeclass'''

from typeclasses import function, TypeClass

eq = function(1)
ne = function(1)

Eq = TypeClass((eq, lambda a, b: not ne(a, b)),
               (ne, lambda a, b: not eq(a, b)))
