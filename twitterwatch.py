#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2015 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Launch Twitterwatch
'''Launch Twitterwatch'''

import sys
from twitterwatch.main import Main


class Twitterwatch(object):
    '''Twitterwatch class'''
    def __init__(self):
        '''Constructor of the Twitterwatch class'''
        self.main()

    def main(self):
        '''main of the Main class'''
        Main()

if __name__ == '__main__':
    Main()
    sys.exit(0)
