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

'''Definition and typeclass instance definitions of the 'Maybe' type'''

from typeclasses import instance
from typeclasses.functor import Functor

class Maybe(object):
    pass

class _Nothing(Maybe):
    def __str__(self):
        return 'Nothing'

    def __repr__(self):
        return 'Nothing'

Nothing = _Nothing()
del _Nothing

class Just(Maybe):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Just %r' % self.value

    def __repr__(self):
        return 'Just %r' % self.value

    def __eq__(self, other):
        if type(other) != Just:
            return NotImplemented

        return self.value == other.value

    def __ne__(self, other):
        if type(other) != Just:
            return NotImplemented

        return self.value != other.value


instance(Functor, Maybe, lambda f, o: Just(f(o.value)) if o is not Nothing
         else Nothing)
