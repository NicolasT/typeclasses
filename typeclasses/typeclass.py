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

'''Typeclass definition and instance definition functions'''

from itertools import izip

from typeclasses.utils import map_

# A typeclass is nothing but a tuple of generic functions
TypeClass = lambda *funs: tuple(funs)


def has_default(fun):
    '''
    Check whether a defined typeclass function has a default implementation
    '''
    try:
        fun, default = fun
    except (ValueError, TypeError):
        pass
    else:
        return True

    return False


default = lambda (_, default_): default_
fun = lambda (fun_, _): fun_


def instance(typeclass, type_, *funs):
    '''Define an instance of a typeclass for a given type

    :param typeclass: Typeclass for which to define an instance
    :type typeclass: `TypeClass`
    :param type_: Type for which to define an instance
    :type type_: `type`
    :param funs: Typeclass function implementations
    :type funs: `callable`
    '''

    assert len(funs) == len(typeclass)

    for (typeclass_fun, impl) in izip(typeclass, funs):
        if not impl and not has_default(typeclass_fun):
            raise ValueError('No default implementation')

        if not impl:
            fun(typeclass_fun).register_impl(type_, default(typeclass_fun))
        elif has_default(typeclass_fun):
            fun(typeclass_fun).register_impl(type_, impl)
        else:
            typeclass_fun.register_impl(type_, impl)
