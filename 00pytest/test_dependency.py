#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import pytest

class TestCase:

    @pytest.mark.dependency(name='a')
    def test_1(self):
        assert True

    @pytest.mark.dependency(depends=['a'])
    def test_2(self):
        assert True

if __name__ == '__main__':
    pytest.main(['-s','-v','test_dependency.py'])