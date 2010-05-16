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
from typeclasses.eq import Eq

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


instance(Functor, Maybe, lambda f, o: Just(f(o.value)) if o is not Nothing
         else Nothing)

instance(Eq, Maybe,
         lambda a, b: True if a is Nothing and b is Nothing else
            False if a is Nothing or b is Nothing else
            True if a.value == b.value else
            False,
         None)
