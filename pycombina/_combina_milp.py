#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This file is part of pycombina.
#
# Copyright 2017-2018 Adrian Bürger, Clemens Zeile, Sebastian Sager, Moritz Diehl
#
# pycombina is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pycombina is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pycombina. If not, see <http://www.gnu.org/licenses/>.


class CombinaMILP():

    '''
    Solve a binary approximation problem by combinatorial integral approximation
    using mixed-integer linear programming and Gurobi.

    The following options of :class:`pycombina.BinApprox` are supported:

    - Maximum number of switches
    - Minimum up-times
    - Minimum down-times
    - Valid control transitions (b_adjacencies)
    - Valid controls per interval (b_valid)
    - Active control at time point t_0-1 (b_bin_pre)

    All other options are ignored without further notice.

    :param BinApprox: Binary approximation problem

    '''

    def __new__(cls, *args, solver=None, **kwargs):
        if solver is None:
            solver = cls.default_solver
        if solver is None:
            raise RuntimeError('no solvers registered')
        return cls.solver_registry[solver](*args, **kwargs)

    @classmethod
    def register_solver(cls, name, factory, make_default=False):
        '''Register a new solver factory.

        Parameters:
        -----------
        name : str
            Name of the factory
        factory : callable
            Factory function that accepts arbitrary positional and keyword
            arguments and returns a standard Combina solver object.
        make_default : bool, optional
            Indicates whether this factory should override the current default
            factory. By default, the current factory is not overwritten unless
            there is currently no default setting.
        '''
        cls.solver_registry[name] = factory
        if make_default or cls.default_solver is None:
            cls.default_solver = name

    solver_registry = dict()
    default_solver = None
