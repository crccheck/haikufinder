# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from unittest import TestCase

from . import LineSyllablizer, count_syllables, syllables


class LineSyllablizerTest(TestCase):
    instance = LineSyllablizer('the day, Kerr’s son put a golf ball')

    def test_init_tokenizes_words(self):
        assert self.instance.words == [
            'the', 'day,', 'Kerr’s', 'son', 'put', 'a', 'golf', 'ball']

    def test_clean_cleans_words(self):
        samples = [
            ('the', 'THE'),
            ('day', 'DAY'),
            ('day,', 'DAY'),
            ("there's", "THERE'S"),
            ("There's", "THERE'S"),
            ("Kerr's", "KERR'S"),
            ('Kerr’s', "KERR'S"),
        ]
        for in_word, cleaned_word in samples:
            assert self.instance.clean(in_word) == cleaned_word

    def test__count_syllables(self):
        samples = [
            ('THE', 1),
            ("THERE'S", 1),
            ("KERR", 1),
            ("KERR'S", 1),
            ("DOGS'", 1),
            ("WE'RE", 1),
        ]
        for in_word, count in samples:
            assert self.instance._count_syllables(in_word) == count


def test_count_syllables():
    counts = [
        ('', 0),
        ('a', 1),
        ('the day, Kerr’s son put a golf ball', 8),
        ('We’re somewhere in between.', 6),
        ('those kids—Charles, Edward, Anne', 6),  # em dash
        ('those kids-Charles, Edward, Anne', 6),
        ('those_kids_Charles,_Edward,_Anne', 6),
    ]
    for phrase, count in counts:
        assert count_syllables(phrase) == count


def test_syllables_dictionary_count():
    """Document the number of entries. When it changes, just update this number."""
    assert len(syllables) == 123563
