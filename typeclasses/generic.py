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

'''A basic implementation of generic functions

Generic functions are functions for which multiple implementations can be
registered. When applying the function on a given value, an implementation will
be chosen based on the type of this value.

In this implementation, the function implementation will be selected based on
the type of the last argument provided during function application.
'''

import threading

def _subclass_cmp(a, b):
    '''A helper function to sort a list of generic function implementations

    This function is used to compare 2 types. When sorting a list of types
    using this comparison operator, the list should be ordered from
    most-specific types to most-general.
    '''

    if issubclass(a, b):
        return -1

    if issubclass(b, a):
        return 1

    return 0


class Function(object):
    '''A simple generic function implementation'''

    def __init__(self, num_arguments):
        '''Initialize a new generic function

        The `num_arguments` argument defines the number of arguments (excluding
        the value on which to operate) the function accepts, for sanity
        checking.

        :param num_arguments: The number of arguments (except the value
            argument) this function accepts
        :type num_arguments: `number`
        '''

        self._num_arguments = num_arguments

        self._impls = []

        self._lock = threading.Lock()

    def __call__(self, *args):
        assert len(args) == self._num_arguments + 1

        obj = args[-1]

        self._lock.acquire()
        try:
            impls = tuple(self._impls)
        finally:
            self._lock.release()

        for impl_type, impl in impls:
            if isinstance(obj, impl_type):
                return impl(*args)

        raise NotImplementedError('Missing implementation for type %s' %
                        type(obj).__name__)

    def register_impl(self, type_, impl):
        '''Register a new implementation of the generic function

        :param type_: Value type for which this implementation should be used
        :type type_: `type`
        :param impl: Implementation
        :type impl: `callable`
        '''

        assert type_ not in (a for (a, _) in tuple(self._impls))

        self._lock.acquire()

        try:
            assert type_ not in (a for (a, _) in self._impls)

            self._impls.append((type_, impl))
            self._impls.sort(cmp=lambda (a, _1), (b, _2): _subclass_cmp(a, b))
        finally:
            self._lock.release()

    def __rlshift__(self, other):
        '''Infix-style operator setup function

        This is based on the idea found at
        http://code.activestate.com/recipes/384122-infix-operators/
        '''

        return _InfixHelper(lambda x: self(other, x))


class _InfixHelper(object):
    '''Helper type for infix style (<<fun>>) calculations'''

    def __init__(self, fun):
        '''Initialize a new helper instance

        :param fun: Function to call
        :type fun: `callable`
        '''

        self.fun = fun

    def __rshift__(self, other):
        return self.fun(other)
