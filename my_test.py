# from wc import sandwich
#
# SANDWICH_BACON = """=== Upper bread slice ===
# bacon / lettuce / tomato
# === Lower bread slice ===
# """
# SANDWICH_EGG = """=== Upper bread slice ===
# fried egg / tomato / cucumber
# === Lower bread slice ===
# """
#
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' / '.join(ingredients))
#
#
# def test_bacon_sandwich(capfd):
#     ingredients = ['bacon', 'lettuce', 'tomato']
#     add_ingredients(ingredients)
#     actual = capfd.readouterr()[0]
#     assert actual == SANDWICH_BACON
#
#
# def test_fried_egg_sandwich(capfd):
#     ingredients = ['fried egg', 'tomato', 'cucumber']
#     add_ingredients(ingredients)
#     actual = capfd.readouterr()[0]
#     assert actual == SANDWICH_EGG
#
# import pytest
#
# from wc import convert_pybites_chars
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do",
#      "LorEm IPSum dolor SIT amET, conSEcTETur adIPIScIng ElIT, SEd do"),
#     ("Vestibulum morbi blandit cursus risus at ultrices",
#      "VESTIBulum morBI BlandIT curSuS rISuS aT ulTrIcES"),
#     ("Aliquet nibh praesent tristique magna sit amet purus gravida quis",
#      "AlIquET nIBh PraESEnT TrISTIquE magna SIT amET PuruS gravIda quIS"),
#     ("Fames ac turpis egestas maecenas pharetra",
#      "FamES ac TurPIS EgESTaS maEcEnaS PharETra"),
#     ("Vitae purus faucibus ornare suspendisse sed nisi lacus",
#      "VITaE PuruS faucIBuS ornarE SuSPEndISSE SEd nISI lacuS"),
#     ("Pharetra massa massa ultricies mi quis",
#      "pharETra maSSa maSSa ulTrIcIES mI quIS"),
#     ("Senectus et netus et malesuada fames",
#      "sEnEcTuS ET nETuS ET malESuada famES"),
#     ("Arcu non sodales neque sodales ut etiam sit",
#      "Arcu non SodalES nEquE SodalES uT ETIam SIT"),
#     ("Natoque penatibus et magnis dis parturient montes nascetur",
#      "NaToquE PEnaTIBuS ET magnIS dIS ParTurIEnT monTES naScETur"),
#     ("Urna cursus eget nunc scelerisque viverra mauris in aliquam",
#      "Urna curSuS EgET nunc ScElErISquE vIvErra maurIS In alIquam"),
#     ("Vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt",
#      "VESTIBulum maTTIS ullamcorPEr vElIT SEd ullamcorPEr morBI TIncIdunT"),
#     ("Tempus urna et pharetra pharetra",
#      "tEmPuS urna ET PharETra PharETra"),
#     ("Ullamcorper a lacus vestibulum sed",
#      "UllamcorPEr a lacuS vESTIBulum SEd"),
#     ("Cursus risus at ultrices mi",
#      "CurSuS rISuS aT ulTrIcES mI"),
#     ("Egestas congue quisque egestas diam in arcu",
#      "egESTaS conguE quISquE EgESTaS dIam In arcu"),
#     ("Sit amet tellus cras adipiscing enim eu",
#      "sIT amET TElluS craS adIPIScIng EnIm Eu"),
#     ("Imperdiet sed euismod nisi porta lorem mollis aliquam",
#      "imPErdIET SEd EuISmod nISI PorTa lorEm mollIS alIquam"),
#     ("Adipiscing tristique risus nec feugiat in fermentum posuere urna",
#      "AdIPIScIng TrISTIquE rISuS nEc fEugIaT In fErmEnTum PoSuErE urna"),
#     ("Et magnis dis parturient montes",
#      "eT magnIS dIS ParTurIEnT monTES"),
#     ("Elementum curabitur vitae nunc sed velit dignissim sodales ut.",
#      "elEmEnTum curaBITur vITaE nunc SEd vElIT dIgnISSIm SodalES uT."),
# ])
# def test_convert_pybites_chars(arg, expected):
#     assert convert_pybites_chars(arg) == expected
#
# import pytest
#
# from wc import get_emoji_indices
#
#
# @pytest.mark.parametrize("emojis, expected", [
#     ('We 💜 Python 🐍', [3, 12]),
#     ('We are so happy 😊😍 seeing you all coding', [16, 17]),
#     ('😂 ROFL that is funny 😂', [0, 21]),
#     ('No way 😭, that is not cool 🤔', [7, 27]),
#     ('Great job 👌 hitting that Ninja 💪 belt', [10, 31]),
#     ('Good luck with your 100 days of code 💯', [37]),
#     ('Our 🥋 ninjas are on fire 🔥', [4, 25]),
#     ('Happy Valentine 💕, buy some gifts 🎁', [16, 34]),
#     ('pytest is so cool 😎, after grasping it 🤯', [18, 39]),
#     ('Books can be boring 😴, better to code 💪❗', [20, 38, 39]),
# ])
# def test_get_emoji_indices(emojis, expected):
#     assert get_emoji_indices(emojis) == expected
#
# import pytest
# from wc import fib

# write one or more pytest functions below, they need to start with test_
# def add(x,y):
#     return x+y
#
# def test_add():
#     output = add(2,3)
#     assert output == 5

#
# @pytest.mark.parametrize("test_input,expect",
#                          [ (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13),
#                           (8, 21), (9, 34) ,(10,55),(-1,pytest.raises(ValueError)) ])
# def test_fib(test_input: int, expect):
#     if test_input < 0:
#         with pytest.raises(ValueError):
#             output = fib(test_input)
#     else:
#         output = fib(test_input)
#         assert output == expect

#(-1,pytest.raises(ValueError)),
#
# import pytest
#
# from wc import list_to_decimal
#
#
# @pytest.mark.parametrize("test_input,expect",[([6,2, True],pytest.raises(TypeError) )])
# def test_type_error(test_input, expect):
#     with pytest.raises(TypeError):
#         list_to_decimal(test_input)
#
#
#
# def test_type_error_simple():
#     with pytest.raises(TypeError):
#         list_to_decimal([6,2, True])
#
#
# @pytest.mark.parametrize("test_input,expect",[([-3, 12],pytest.raises(ValueError) )])
# def test_value_errror(test_input, expect):
#     with pytest.raises(ValueError):
#         list_to_decimal(test_input)
#
# @pytest.mark.parametrize("test_input,expect",
#                           [ ([0, 4, 2, 8], 428),
#                             ([1,2], 12),
#                             ([3], 3),
#                             ])
# def test_zero_ten_range(test_input, expect):
#     assert list_to_decimal(test_input) == expect
#
# import pytest
#
# from wc import print_workout_days
#
# @pytest.mark.parametrize("test_input,expect",[('upper body #1','Mon'),
#                                                ('shoulder','No matching workout'),
#                                               ('lower body #1','Tue')])
# def test_print_workout_days(test_input,expect,capsys):
#     print_workout_days(test_input)
#     captured = capsys.readouterr()
#     assert captured.out.strip() ==expect
#
# import string
#
# import pandas as pd
#
# import wc as se
#
#
# def test_basic_series():
#     ser = se.basic_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.name == "Fred"
#     assert ser.dtype == "int64"
#     assert all(n in [1, 2, 3, 4, 5] for n in ser.values)
#     assert len(ser.values) == 5
#
#
# def test_floats_series():
#     ser = se.float_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.dtype == "float64"
#     assert len(ser) == 1001
#     assert ser.sum() == 500.5
#
#
# def test_alpha_index_series():
#     ser = se.alpha_index_series()
#     assert isinstance(ser, pd.Series)
#     assert ser.dtype == "int64"
#     assert len(ser) == 26
#     assert sum(ser.values) == 351
#     assert all(c in string.ascii_lowercase for c in ser.index)
#
#
# def test_object_values_series():
#     ser = se.object_values_series()
#     assert isinstance(ser, pd.Series)
#     assert len(ser) == 26
#     assert all(c in string.ascii_uppercase for c in ser.values)
#     assert ser[101] == "A"
#     assert ser[126] == "Z"

# import inspect
# import string
#
# import pytest
# import numpy as np
# import pandas as pd
#
# import wc as se
#
#
# @pytest.fixture()
# def float_series():
#     """Returns a pandas Series containing floats"""
#     return pd.Series([float(n) / 1000 for n in range(0, 1001)])
#
#
# @pytest.fixture()
# def alpha_series():
#     """Returns a pandas Series containing floats"""
#     dictionary = dict(zip(string.ascii_lowercase, range(1, 27)))
#     return pd.Series(dictionary)
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (0, 0.000), (500, 0.500), (1000, 1.000)
# ])
# def test_return_at_index(float_series, arg, expected):
#     assert se.return_at_index(float_series, arg) == expected
#
#
# def test_return_at_index_raise_exception(float_series):
#     with pytest.raises(KeyError):
#         float_series[1111]
#
#
# def test_get_slice(float_series):
#     slce = se.get_slice(float_series, 20, 25)
#     assert isinstance(slce, pd.core.series.Series)
#     assert len(slce) == 5
#     assert slce[24] == 0.024
#
#
# def test_get_slice_inclusive(float_series):
#     slce = se.get_slice_inclusive(float_series, 20, 25)
#     assert isinstance(slce, pd.core.series.Series)
#     assert len(slce) == 6
#     assert slce[25] == 0.025
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (0, 0.000), (5, 0.005), (9, 0.009)
# ])
# def test_return_head(float_series, arg, expected):
#     assert se.return_head(float_series, 10)[arg] == expected
#     assert ".head" in inspect.getsource(se.return_head)
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (991, 0.991), (995, 0.995), (1000, 1.000)
# ])
# def test_return_tail(float_series, arg, expected):
#     assert se.return_tail(float_series, 10)[arg] == expected
#     assert ".tail" in inspect.getsource(se.return_tail)
#
#
# def test_get_index(alpha_series):
#     idx = se.get_index(alpha_series)
#     assert isinstance(idx, pd.core.indexes.base.Index)
#     assert len(idx) == 26
#     assert all(c in string.ascii_lowercase for c in idx.values)
#     assert ".index" in inspect.getsource(se.get_index)
#
#
# def test_get_values(alpha_series):
#     vals = se.get_values(alpha_series)
#     assert isinstance(vals, np.ndarray)
#     assert len(vals) == 26
#     assert all(c in range(1, 27) for c in vals)
#
#
# def test_all_even_indexes_returned(float_series):
#     ser = se.get_every_second_indexes(float_series, True)
#     assert all(n % 2 == 0 for n in ser.index)
#     assert round(sum(ser), 1) == 250.5
#
#
# def test_all_odd_indexes_returned(float_series):
#     ser = se.get_every_second_indexes(float_series, False)
#     assert all(n % 2 == 1 for n in ser.index)
#     assert round(sum(ser), 1) == 250.0
#

#
# import pytest
#
# from wc import sum_numbers
#
#
# @pytest.mark.parametrize("arg, ret, hundreds_value", [
#     ([], 0, -1),
#     ([1, 2, 3], 6, -1),
#     ([40, 50, 60], 150, 0),
#     ([140, 50, 60], 250, 2),
#     ([140, 150, 160], 450, 6),
#     ([1140, 150, 160], 1450, 20),
# ])
# def test_sum_numbers(arg, ret, hundreds_value):
#     assert sum_numbers(arg) == ret
#     from wc import num_hundreds
#     assert num_hundreds == hundreds_value

#
# import pytest
#
# from wc import get_users
#
#
# pw1 = """
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/bin/sh
# bin:x:2:2:bin:/bin:/bin/sh
# sys:x:3:3:sys:/dev:/bin/sh
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/bin/sh
# man:x:6:12:man:/var/cache/man:/bin/sh
# lp:x:7:7:lp:/var/spool/lpd:/bin/sh
# """
# pw2 = """
# mail:x:8:8:mail:/var/mail:/bin/sh
# news:x:9:9:news:/var/spool/news:/bin/sh
# uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
# proxy:x:13:13:proxy:/bin:/bin/sh
# www-data:x:33:33:www-data:/var/www:/bin/sh
# backup:x:34:34:backup:/var/backups:/bin/sh
# list:x:38:38:Mailing List Manager:/var/list:/bin/sh
# """
# pw3 = """
# irc:x:39:39:ircd:/var/run/ircd:/bin/sh
# gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
# nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
# libuuid:x:100:101::/var/lib/libuuid:/bin/sh
# Debian-exim:x:101:103::/var/spool/exim4:/bin/false
# statd:x:102:65534::/var/lib/nfs:/bin/false
# sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin
# ftp:x:104:65534::/home/ftp:/bin/false
# messagebus:x:105:106::/var/run/dbus:/bin/false
# """
# pw4 = """
# mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
# avar:x:1000:1000::/home/avar:/bin/bash
# chad:x:1001:1001::/home/chad:/bin/bash
# git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
# gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
# avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
# postfix:x:108:112::/var/spool/postfix:/bin/false
# ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
# artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash
# """
#
#
# @pytest.mark.parametrize("input_, expected", [
#     (pw1, {'root': 'root', 'daemon': 'daemon', 'bin': 'bin',
#            'sys': 'sys', 'sync': 'sync', 'games': 'games',
#            'man': 'man', 'lp': 'lp'}),
#     (pw2, {'mail': 'mail', 'news': 'news', 'uucp': 'uucp',
#            'proxy': 'proxy', 'www-data': 'www-data',
#            'backup': 'backup', 'list': 'Mailing List Manager'}),
#     (pw3, {'irc': 'ircd', 'gnats': 'Gnats Bug-Reporting System (admin)',
#            'nobody': 'nobody', 'libuuid': 'unknown', 'Debian-exim': 'unknown',
#            'statd': 'unknown', 'sshd': 'unknown', 'ftp': 'unknown',
#            'messagebus': 'unknown'}),
#     (pw4, {'mysql': 'MySQL Server', 'avar': 'unknown', 'chad': 'unknown',
#            'git-svn-mirror': 'Git mirror', 'gerrit2': 'Gerrit User',
#            'avahi': 'Avahi mDNS daemon', 'postfix': 'unknown',
#            'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}),
# ])
# def test_users(input_, expected):
#     assert get_users(input_) == expected
#
"""
Tests for gc_content.py
Uses various DNA sequences retrieved from NCBI as input
Compares user function with calculated GC content
Inputs are modified to check how the function deals with unknown characters
"""
#
# import pytest
# from wc import calculate_gc_content
#
# DNA_SEQUENCES = [
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3
#             "tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
#             "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
#             "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
#             "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
#             "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
#             "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
#             "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
#             "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
#             "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
#             "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
#             "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
#             "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
#             "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
#             "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
#             "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
#             "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
#             "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
#             "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
#             "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
#             "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
#             "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"
#         ),
#         51.35,
#     ),
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
#             "gttaatatttatgattcctgaaaagaaatcaatcgcaatcatgaaagaactaagcattgg"
#             "aaatacaaagcaaatgctgatgattaatggagttgacgtgaaaaatccattgctgctttt"
#             "tttacatggcgggccgggaacgccgcaaatcggatatgttagacattatcaaaaagagct"
#             "ggaacagtattttacagtagttcattgggatcagagaggatcggggctttcttattctaa"
#             "gcgaatttcgcatcactctatgacaataaatcacttcattaaagatacaatccaagtcac"
#             "tcaatggcttttagctcatttttcaaaatcaaaactttacctagccggtcattcttgggg"
#             "atcaatactggcgcttcatgtgctgcagcagcgtcctgatttattttacacgtattatgg"
#             "aatcagccaggttgttaacccgcaagatgaagaatcaactgcttatcaacatattcgtga"
#             "aatttccgaatcaaaaaaagccagcatattatctttccttacacgtttcattggtgctcc"
#             "gccttggaagcaggatatccagcaccttatctatcggttttgtgttgagctaaccagggg"
#             "aggattcactcaccgtcatcgtcaatctctcgctgtattatttcaaatgcttactggcaa"
#             "tgagtatggagtgcggaacatgcacagcttccttaatggattgcgcttcagtaaaaaaca"
#             "tttaactgatgagttgtaccggtttaatgcttttacatcagttccttctattaaagtacc"
#             "gtgtgttttcatttcagggaaacatgacttaattgttcctgcagaaatatcgaaacagta"
#             "ttatcaagaacttgaggcacctgaaaagcgctggtttcaatttgagaattcagctcacac"
#             "cccgcatattgaggagccatcattattcgcgaacacattaagtcggcatgcacgacacca"
#             "tttatgatagatccttgataaataagaaaaacccctgtataataaaaaaagtgtgcaaat"
#             "catgcatattttaaataagtcttgcaacatgcgcctattttctgtataatggtgtatgtt"
#             "ggtctttgactgcgatgaagtgagaggttgctgacacacccggccgctttgccatggcaa"
#             "ggtgttcaggtttttctcacggagaactgtctaacgtgatgtaggcgaaaaggagggaaa"
#             "ataatggcaaaacaaaaaattcgtattcgtttgaaagcatatgatcatagaatccttgat"
#         ),
#         39.37,
#     ),
#     (
#         (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
#             # but all As removed, upper and lower case
#             "gtttttttgttcctggtctcgctctggctgcttgg"
#             "tcgctgctgtgtttgggttgcgtgtccttgctgctttt"
#             "tttctggcgggccgggcgccgctcggttgttgctttcggct"
#             "ggcgtttttcgtgttcttgggtcggggtcggggctttcttttct"
#             "gcgtttcgctcctcttgcttccttcttgtctccgtcc"
#             "tctggcttttgctctttttctcctttcctgccggtcttcttgggg"
#             "tctctggcgcttctgtgctgcgcgcgtcctgtttttttccgttttgg"
#             "tcgccggttgttcccgcgtGGtcctgctttcctttcgtg"
#             "tttccgtcgccgcttttctttccttccgtttcttggtgctcc"
#             "gccttgggcggttccgccctttcttcggttttgtgttggctccgggg"
#             "ggttcctcccgtctcgtctctctcgctgttttttctgcttctggc"
#             "tggttgggtgcggctgccgcttcctttggttgcgcttcgtc"
#             "tttctgtggttgtccggttttgcttttctcgttccttctttgtcc"
#             "gtgtgttttctttcgggCtgcttttgttcctgcgttcgcgt"
#         ),
#         55.88,
#     ),
# ]
#
#
# @pytest.mark.parametrize("dna,gc_content", DNA_SEQUENCES)
# def test_calculate_gc_content(dna, gc_content):
#
#     assert calculate_gc_content(dna) == gc_content
#
#     dna_with_spaces = "".join([base + " " for base in dna])
#     assert calculate_gc_content(dna_with_spaces) == gc_content
#
#     dna_with_special_chars = "".join([base + ".!?/," for base in dna])
#     assert calculate_gc_content(dna_with_special_chars) == gc_content
#
#     dna_line_breaks = "\n" + dna + "\n" + dna + "\n"
#     assert calculate_gc_content(dna_line_breaks) == gc_content
#
#
#
# import pytest
#
# from wc import freq_digit
#
#
# @pytest.mark.parametrize("data, expected", [
#     (2020, 2), (177, 7), (1998, 9),
#     (12345, 1), (994145467, 4),
#     (748791789189717891789, 7)
# ])
# def test_freq_digit(data, expected):
#     assert freq_digit(data) == expected
#
# import pytest
#
# from wc import major_n_minor
#
#
# @pytest.mark.parametrize("data, expected", [
#     ([1, 2, 3, 2, 2, 2, 3], (2, 1)),
#     ([0, 0, 0, 1, 2, 2], (0, 1)),
#     ([9, 8, 7, 8, 8, 9], (8, 7)),
#     ([2, 0, 2, 0, 2, 1], (2, 1)),
#     ([1, 3, 5, 7, 8, 8, 9, 9, 3, 5, 8, 7], (8, 1)),
#     ([9, 0, 5, 7, 8, 8, 9, 0, 5, 9, 9, 5], (9, 7)),
# ])
# def test_frequency(data, expected):
#     assert major_n_minor(data) == expected
#
# import pytest
#
# from wc import is_armstrong
#
#
# @pytest.mark.parametrize('number, expected', [
#     (5, True),  (153, True), (370, True),
#     (371, True),  (4150, False), (2020, False),
#     (9474, True), (1989, False), (11, False),
# ])
# def test_armstrong(number, expected):
#     assert is_armstrong(number) == expected
#
# import datetime
# from random import randint
#
# from freezegun import freeze_time
#
# from wc import tomorrow
#
#
# @freeze_time('2020-07-09')
# def test_no_args():
#     assert tomorrow() == datetime.date(2020, 7, 10)
#
#
# def test_next_day():
#     assert tomorrow(datetime.date(2020, 5, 1)) == datetime.date(2020, 5, 2)
#
#
# def test_next_year():
#     assert tomorrow(datetime.date(2019, 12, 31)) == datetime.date(2020, 1, 1)
#
#
# def test_leap_year():
#     assert tomorrow(datetime.date(2020, 2, 28)) == datetime.date(2020, 2, 29)
#
#
# def test_non_leap_year():
#     assert tomorrow(datetime.date(2021, 2, 28)) == datetime.date(2021, 3, 1)
#
#
# def test_random_date():
#     year, month, day = randint(2000, 2020), randint(1, 12), randint(1, 27)
#     assert tomorrow(datetime.date(year, month, day)) == datetime.date(year, month, day + 1)
#
# from random import sample
#
# import pytest
#
# from wc import minimum_number
#
#
# @pytest.mark.parametrize('test_input, expected', [
#                         ([], 0),
#                         ([0], 0),
#                         ([1], 1),
#                         ([5], 5),
#                         ([1, 1], 1),
#                         ([7, 1], 17),
#                         ([1, 7], 17),
#                         ([3, 2, 1], 123),
#                         ([1, 9, 5, 9, 1], 159),
#                         ([0, 9, 5, 9], 59),
#                         ([9, 3, 1, 2, 7, 9, 4, 5, 7, 9, 8, 6, 1], 123456789),
#                         ([4, 2], 24),
#                         ([1, 5, 2, 3, 4, 1, 4, 2, 3], 12345),
#                         (sample(range(1, 6), 5), 12345),
#                         (sample(range(0, 6), 6), 12345),
#                          ])
#
# def test_minimum_number(test_input, expected):
#     assert minimum_number(test_input) == expected
#
# from random import choice
#
# import pytest
#
# from wc import round_to_next
#
#
# @pytest.mark.parametrize('test_input, expected', [
#                         ((0, 5), 0),
#                         ((2, 5), 5),
#                         ((5, 5), 5),
#                         ((42, 5), 45),
#                         ((-6, 10), 0),
#                         ((-6, -10), -10),
#                         ((-10, 10), -10),
#                         ((-10, -10), -10),
#                         ((17, 1), 17),
#                         ((12_345, 42), 12348),
#                         ((15, choice([3, 5, 15])), 15),
#                          ])
# def test_round_to_next(test_input, expected):
#     assert round_to_next(*test_input) == expected
#
# import pytest
#
# from wc import n_digit_numbers
#
#
# @pytest.mark.parametrize('input_list, n, expected', [
#     ([], 1, []),
#     ([1, 2, 3], 1, [1, 2, 3]),
#     ([1, 2, 3], 2, [10, 20, 30]),
#     ([0, 1, 2, 3], 2, [0, 10, 20, 30]),
#     ([8, 9, 10], 2, [80, 90, 10]),
#     ([5.2, 1600, 520, 3600, 13, 55, 4000], 2,
#      [52, 16, 52, 36, 13, 55, 40]),
#     ([-1.1, 2.22, -3.333], 3, [-110, 222, -333]),
#     ([-1.1, 2.22, -3.333, 4444, 55555], 4,
#      [-1100, 2220, -3333, 4444, 5555]),
# ])
# def test_n_digit_numbers(input_list, n, expected):
#     assert n_digit_numbers(input_list, n) == expected
#
#
# def test_invalid_n():
#     with pytest.raises(ValueError):
#         n_digit_numbers([1, 2, 3], 0)
#
# import pytest
#
# from wc import join_lists
# import pytest
#
# from wc import print_names_to_columns
#
#
# @pytest.fixture
# def names():
#     return ["Bob", "Julian", "Tim", "Sara", "Eva", "Ana", "Jake", "Maria"]
#
#
# def test_default(capfd, names):
#     print_names_to_columns(names)
#     actual = capfd.readouterr()[0].strip()
#     expected = (
#         "| Bob       | Julian    \n"
#         "| Tim       | Sara      \n"
#         "| Eva       | Ana       \n"
#         "| Jake      | Maria"
#     )
#     assert actual == expected
#
#
# def test_three_columns(capfd, names):
#     print_names_to_columns(names, cols=3)
#     actual = capfd.readouterr()[0].strip()
#     expected = (
#         "| Bob       | Julian    | Tim       \n"
#         "| Sara      | Eva       | Ana       \n"
#         "| Jake      | Maria"
#     )
#     assert actual == expected
#
#
# def test_four_columns(capfd, names):
#     print_names_to_columns(names, cols=4)
#     actual = capfd.readouterr()[0].strip()
#     expected = (
#         "| Bob       | Julian    | Tim       | Sara      \n"
#         "| Eva       | Ana       | Jake      | Maria"
#     )
#     assert actual == expected
#
# @pytest.mark.parametrize('input_list, sep, expected', [
#                         ([], '&', None),
#                         ([['a']], '|', ['a']),
#                         ([['a', 'b']], '&', ['a', 'b']),
#                         ([['a', 'b'], ['c']], '&', ['a', 'b', '&', 'c']),
#                         ([['a', 'b'], ['c'], ['d', 'e']], '+',
#                          ['a', 'b', '+', 'c', '+', 'd', 'e']),
# ])
# def test_join_lists(input_list, sep, expected):
#     assert join_lists(input_list, sep) == expected
#
# from datetime import date
# import time
# from typing import NamedTuple
#
# from wc import (download_pickle_file,
#                            deserialize,
#                            serialize,
#                            TMP,
#                            MovieRented)
#
#
# class Bite(NamedTuple):
#     title: str
#     number: int
#     level: str
#
#
# def test_deserialize_movie_rented_data():
#     download_pickle_file()
#     expected = [
#         MovieRented('Mad Max Fury Road', 4, date(2020, 12, 1)),
#         MovieRented('Mad Max Fury Road', 4, date(2020, 12, 17)),
#         MovieRented('Die Hard', 4, date(2020, 12, 3)),
#         MovieRented('Tenet', 20, date(2020, 12, 1)),
#         MovieRented('Breach', 7, date(2020, 11, 17)),
#         MovieRented('Spider-Man', 12, date(2020, 12, 28)),
#         MovieRented('Sonic', 10, date(2020, 11, 4))
#     ]
#     actual = deserialize()
#     assert actual == expected
#
#
# def test_serialize_and_deserialize_other_data():
#     data = [
#         Bite('Sum of Numbers', 1, 'Beginner'),
#         Bite('Regex Fun', 2, 'Advanced'),
#     ]
#     pkl_file = TMP / str(int(time.time()))
#     serialize(pkl_file, data=data)
#     actual = deserialize(pkl_file)
#     expected = data
#     assert actual == expected
#
# import pytest
#
# from wc import get_credit_cards
#
# csv1 = b"""
# Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKS2VlbGJ5LE1hY0NhZmZlcmt5LD
# YzOTM3MTk0MzMzMjk5MjQKTGlubmVsbCxDbGVtbWV0dCwzNTU1NTg0OTI0MDkzOTU0CkVs
# eXNoYSxNZWlnaGFuLDYzODU3OTU3OTM4OTcxMDYKS2F0YWxpbixFdGhlcnRvbiwzNTg0Mj
# MwMDExNjgwNzAwCkZpbmEsUGFzZWssNTEwMDEzNjYzMTY2NDY4NwpBcmRlbGxhLEJyYXpp
# ZXIsMjAxNzEyNjEzNjUzMzc0CkRvcnRoZWEsS2FycGluc2tpLDMwNTAyNjYxMjUxMTcyCl
# Jhbm5hLER1ZmYsMzU3NjM5MzA1NjQ5MzMxMgpDaW5uYW1vbixLYWFzbWFuLDU0NDIwMjgx
# NTA4MDg1NzAKSmFjbGluLFRvbmdlLDM1NDk4NTIxMDQ3MjQ1MjcK
# """
# csv2 = b"""
# Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKTWVsaXNlbmRhLENyb3NmaWVsZC
# wzNTg0MTY2NjgwNjE3MjAzCkxpYW5hLFNlbnRlbiw2NzYyMDgzNDMwNjM3MjU2NwpEZWVy
# ZHJlLE1hdGNoYW0sMzU0ODI2OTgzOTkwNDUzMwpDYXNzZXksQmxleW1hbiwzNzQ2MjI3MD
# Y3OTU3OTUKRG9kaSxMZXlkb24sMzU3NTkwNDg5MzQyMjc5MgpDb25ub3IsQmVybmFyZG90
# dGksMzUyODYwMjY2NDk0NDkxNQpMZXdpc3MsQnJhbnNieSw1MTAwMTM4NTUzNDQ2OTQ1Ck
# p1bmllLFRhbXNldHQsMzU3MDUwNDQwNDkzMzMwNgpDb3JpbGxhLEhvZiwzMDI4NzM1NDg2
# NTcyNApCb2JiaSxGZnJlbmNoLDM1NjYxMTA3Njc2NTcxNTUK
# """
# expected1 = [
#     '6393719433329924', '3555584924093954', '6385795793897106',
#     '3584230011680700', '5100136631664687', '201712613653374',
#     '30502661251172', '3576393056493312', '5442028150808570',
#     '3549852104724527']
# expected2 = [
#     '3584166680617203', '67620834306372567', '3548269839904533',
#     '374622706795795', '3575904893422792', '3528602664944915',
#     '5100138553446945', '3570504404933306', '30287354865724',
#     '3566110767657155'
# ]
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (csv1, expected1), (csv2, expected2)
# ])
# def test_get_credit_cards(arg, expected):
#     assert get_credit_cards(arg) == expected

#
# import pytest
#
# from wc import (
#     Car,
#     is_same_car_color_and_model,
#     is_same_instance_of_car,
# )
#
#
# # `NewList` for tests
# class NewList(list):
#     pass
#
#
# # A bunch of lists to test
# l1 = [["gas", "electro", "hybrid"], "200 PS", "radio"]
# l2 = l1
# l3 = l1.copy()
# l4 = l1[0]
# l5 = [l4, "digital radio"]
# l6 = [l1[0], "digital radio"]
# l7 = NewList(l1)
# l8 = ["unleaded"]
#
# # A bunch of `Car`s
# my_car = Car("Toyota Corolla", "black")
# other_car1 = my_car
# other_car2 = Car("Toyota Corolla", "black")
# other_car3 = Car("Toyota Corolla", "red")
# other_car4 = Car("Porsche Cayenne", "black")
#
#
# # Test staticmethod Car.age
# @pytest.mark.parametrize(
#     "days, expected",
#     [
#         (7, "A week old"),  # week
#         (365, "A year old"),  # year
#         (2, "Neither a week, nor a year old"),  # Other number
#     ],
# )
# def test_car_age(days, expected):
#     assert Car.age(days) == expected
#
#
# # Test staticmethod Car.age
# @pytest.mark.parametrize(
#     "list1, list2, expected",
#     [
#         ([], [], True),  # Empty
#         (l1, l2, True),  # same instance
#         (l1, l1[:], True),  # full copy
#         (l1, l3, True),  # full copy
#         (l5, l6, True),  # Two identical short lists
#         (l5[0], l6[0], True),  # First element of short lists (same instances)
#         (l1, l7, True),  # One list, one NewList, same contents
#         (l1, l8, False),  # Two completely different lists
#     ],
# )
# def test_the_same_configuration(list1, list2, expected):
#     assert Car.has_same_configuration(list1, list2) == expected
#
#
# @pytest.mark.parametrize(
#     "car1, car2, expected",
#     [
#         (my_car, my_car, True),  # Identical cars (same instance)
#         (my_car, other_car1, True),  # Identical cars (same instance)
#         (my_car, other_car2, True),  # Car of the same model and color
#         (other_car2, other_car3, False),  # Completely different cars
#     ],
# )
# def test_is_same_car_color_and_model(car1, car2, expected):
#     assert is_same_car_color_and_model(car1, car2) == expected
#
#
# @pytest.mark.parametrize(
#     "car1, car2, expected",
#     [
#         (my_car, my_car, True),  # Same instance
#         (my_car, other_car1, True),  # Same Car, different instance
#         (other_car1, other_car2, False),  # Completely different cars
#     ],
# )
# def test_is_the_same_instance_of_car(car1, car2, expected):
#     assert is_same_instance_of_car(car1, car2) == expected
#
# from wc import ontrack_reading
#
#
# @pytest.mark.parametrize("args, expected", [
#     ((60, 2, 3), True),
#     ((60, 0, 3), False),
#     ((60, 0.5, 3), True),
#     ((30, 16, 180), True),
#     ((30, 8, 180), False),
#     ((40, 1, 40), False),
#     ((40, 10, 40), True),
#     ((10, 10, 300), True),
#     ((10, 8, 300), False),
#     ((10, 8.2, 300), False),
#     ((10, 8.22, 300), True),
#     ((10, 10, 365), True),
# ])
# def test_ontrack_reading(args, expected):
#     assert ontrack_reading(*args) == expected
#
#
# @freeze_time('2021-07-09')
# def test_without_days_arg_current_date_july():
#     assert ontrack_reading(60, 31) is False
#     assert ontrack_reading(60, 34) is True
#
#
# @freeze_time('2021-12-09')
# def test_without_days_arg_current_date_december():
#     assert ontrack_reading(30, 28) is False
#     assert ontrack_reading(30, 29) is True

# import pytest
#
# from wc import intersection
#
#
# @pytest.mark.parametrize(
#     "inputs,expected",
#     [
#         [({1, 2, 3}, {2, 3, 4}, {3, 4}), {3}],
#         [([1, 2, 3, 1], {1, -1}, {}), {1}],
#         [({1, "2", "3"}, {1, "3"}), {1, "3"}],
#         [
#             # mixing lists/sets/tuples
#             ([1, 2, 3, 4, 5, 1, 2, 3, 2, 3], {0, 10, 5}, ("a", 5)),
#             {
#                 5,
#             },
#         ],
#         [("do you like this bite?", "i hope so"), {"o", "i", "h", "e", "s", " "}],
#     ],
# )
# def test_basic(inputs, expected):
#     results = intersection(*inputs)
#     assert results == expected
#
#
# @pytest.mark.parametrize(
#     "inputs,expected",
#     [
#         [((None, "this is a string")), {" ", "a", "g", "h", "i", "n", "r", "s", "t"}],
#         [
#             # no input
#             (None,),
#             set(),
#         ],
#         [
#             # multiple None inputs
#             (None, {1, 2, 3}, None, list(range(10)), None),
#             {1, 2, 3},
#         ],
#         [([1, 2, 3, 3, 2, 1],), {1, 2, 3}],  # single input
#     ],
# )
# def test_edgecases(inputs, expected):
#     results = intersection(*inputs)
#     assert results == expected
#
# import pytest
#
# from wc import pretty_string
#
#
# @pytest.mark.parametrize(
#     "input_obj, expected_result",
#     [
#         (list(range(10)), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"),
#         (
#             [["A"] * 11, ["A"] * 12],
#             (
#                 "[['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],\n"
#                 " ['A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A',\n"
#                 "  'A']]"
#             ),
#         ),
#         ([1, [2, [3, [4]]]], "[1, [2, [...]]]"),
#         (
#             ["a" * 30] + [["b" * 30]] + [[3.0, [1]]],
#             "['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',\n"
#             " ['bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'],\n"
#             " [3.0, [...]]]",
#         ),
#         ({"z": 1, "c": 2, "a": 3}, "{'a': 3, 'c': 2, 'z': 1}"),
#         (
#             {
#                 "font-family": "serif",
#                 "speak": "none",
#                 "font-style": "normal",
#                 "font-weight": "400",
#                 "font-variant": "normal",
#                 "text-transform": "none",
#                 "line-height": "1",
#             },
#             (
#                 "{'font-family': 'serif',\n"
#                 " 'font-style': 'normal',\n"
#                 " 'font-variant': 'normal',\n"
#                 " 'font-weight': '400',\n"
#                 " 'line-height': '1',\n"
#                 " 'speak': 'none',\n"
#                 " 'text-transform': 'none'}"
#             ),
#         ),
#     ],
# )
# def test_pretty_str(input_obj, expected_result):
#     result = pretty_string(input_obj)
#     assert result == expected_result
# import pytest
# from fastapi.testclient import TestClient
#
# from wc import app
#
#
# @pytest.fixture
# def client():
#     client = TestClient(app)
#     return client
#
#
# def test_root_endpoint_with_get(client):
#     resp = client.get("/")
#     assert resp.status_code == 200
#     msg = "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
#     expected = {"message": msg}
#     assert resp.json() == expected
#
#
# def test_root_endpoint_only_get(client):
#     resp = client.post("/")
#     assert resp.status_code == 405
#     assert resp.json() == {"detail": "Method Not Allowed"}
#
# import pytest
# from pydantic import ValidationError
#
# from wc import Food
#
#
# def test_create_food_object():
#     food = Food(
#         id=1,
#         name="egg",
#         serving_size="piece",
#         kcal_per_serving=78,
#         protein_grams=6.3,
#         fibre_grams=0,
#     )
#     assert type(food) == Food
#     assert food.id == 1
#     assert food.name == "egg"
#     assert food.serving_size == "piece"
#     assert food.kcal_per_serving == 78
#     assert food.protein_grams == 6.3
#     assert food.fibre_grams == 0
#
#
# def test_create_food_without_fibre():
#     # no fibre in constructor
#     food = Food(
#         id=1, name="egg", serving_size="piece", kcal_per_serving=78, protein_grams=6.3
#     )
#     # hence it's set to default 0
#     assert food.fibre_grams == 0
#
#
# def test_create_food_required_attrs():
#     with pytest.raises(ValidationError):
#         # missing attrs like serving_size, kcal_per_serving, etc.
#         Food(id=1, name="egg")
#
#
# def test_create_food_wrong_serving_type():
#     with pytest.raises(ValidationError):
#         # note that name=2 is ok with pydantic, it gets casted
#         Food(
#             id=1,
#             name="egg",
#             serving_size="piece",
#             kcal_per_serving="2ab",
#             protein_grams=6.3,
#             fibre_grams=1.2,
#         )
#
#
# def test_create_food_casting_no_exception():
#     # "78" is ok, so is an int for protein's float type
#     assert Food(
#         id=1,
#         name="egg",
#         serving_size="piece",
#         kcal_per_serving="78",
#         protein_grams=6,
#         fibre_grams=1.2,
#     )
#
# import pytest
#
# from wc import Hand, get_hand_for_word
#
#
# @pytest.mark.parametrize("word, expected", [
#     ("aam", Hand.BOTH),
#     ("unpicketed", Hand.BOTH),
#     ("muscot", Hand.BOTH),
#     ("aspirer", Hand.BOTH),
#     ("quadribasic", Hand.BOTH),
#     ("holothurioid", Hand.BOTH),
#     ("cloamen", Hand.BOTH),
#     ("antereformational", Hand.BOTH),
#     ("baal", Hand.BOTH),
#     ("moirette", Hand.BOTH),
#     ("terret", Hand.LEFT),
#     ("refederate", Hand.LEFT),
#     ("awee", Hand.LEFT),
#     ("crewer", Hand.LEFT),
#     ("addressee", Hand.LEFT),
#     ("reaward", Hand.LEFT),
#     ("verve", Hand.LEFT),
#     ("tearcat", Hand.LEFT),
#     ("extra", Hand.LEFT),
#     ("Geez", Hand.LEFT),
#     ("exeat", Hand.LEFT),
#     ("Hui", Hand.RIGHT),
#     ("miny", Hand.RIGHT),
#     ("kinkly", Hand.RIGHT),
#     ("Lui", Hand.RIGHT),
#     ("pull", Hand.RIGHT),
#     ("kop", Hand.RIGHT),
#     ("Ji", Hand.RIGHT),
#     ("nymph", Hand.RIGHT),
#     ("unjoin", Hand.RIGHT),
#     ("Luo", Hand.RIGHT),
# ])
# def test_get_hand_for_word(word, expected):
#     result = get_hand_for_word(word)
#     assert result == expected

#
# import pytest
# import typer
# from typer.testing import CliRunner
#
# from wc import main
#
# runner = CliRunner()
# app = typer.Typer()
# app.command()(main)
#
#
# @pytest.mark.parametrize(
#     "a, b, expected_result",
#     [
#         ("3", "4", "7"),
#         ("2", "5", "7"),
#     ],
# )
# def test_app_sum(a, b, expected_result):
#     result = runner.invoke(app, [a, b])
#     assert result.exit_code == 0
#     assert result.stdout.strip() == expected_result
#
#
# @pytest.mark.parametrize(
#     "expected_descriptions",
#     [
#         (
#             [
#                 "CLI that allows you to add two numbers",
#                 "The value of the first summand",
#                 "The value of the second summand",
#             ]
#         ),
#     ],
# )
# def test_app_help(expected_descriptions):
#     result = runner.invoke(app, ["--help"])
#     assert result.exit_code == 0
#
#     for description in expected_descriptions:
#         assert description in result.stdout

# from typing import List
#
# import pytest
# from typer.testing import CliRunner
#
# from wc import app
#
#
# @pytest.fixture()
# def runner() -> CliRunner:
#     return CliRunner()
#
#
# @pytest.mark.parametrize(
#     "a, b, expected_result",
#     [
#         ("3", "4", "The sum is 7"),
#         ("2", "5", "The sum is 7"),
#     ],
# )
# def test_app_sum(a: str, b: str, expected_result: str, runner: CliRunner) -> None:
#     result = runner.invoke(app, ["sum", a, b])
#     assert result.exit_code == 0
#     assert result.stdout.strip() == expected_result
#
#
# @pytest.mark.parametrize(
#     "expected_descriptions",
#     [
#         (
#             [
#                 "Command that allows you to add two numbers.",
#                 "The value of the first summand",
#                 "The value of the second summand",
#             ]
#         ),
#     ],
# )
# def test_app_sum_help(expected_descriptions: List[str], runner: CliRunner) -> None:
#     result = runner.invoke(app, ["sum", "--help"])
#     assert result.exit_code == 0
#     for description in expected_descriptions:
#         assert description in result.stdout
#
#
# @pytest.mark.parametrize(
#     "c, d, expected_result",
#     [
#         ("5", "4", "d=4 is not greater than c=5"),
#         ("2", "7", "d=7 is greater than c=2"),
#     ],
# )
# def test_app_compare(c: str, d: str, expected_result: str, runner: CliRunner) -> None:
#     result = runner.invoke(app, ["compare", c, d])
#     assert result.exit_code == 0
#     assert result.stdout.strip() == expected_result
#
#
# @pytest.mark.parametrize(
#     "expected_descriptions",
#     [
#         (
#             [
#                 "Command that checks whether a number d is greater than a number c.",
#                 "First number to compare against.",
#                 "Second number that is compared against first number.",
#             ]
#         ),
#     ],
# )
# def test_app_compare_help(expected_descriptions: List[str], runner: CliRunner) -> None:
#     result = runner.invoke(app, ["compare", "--help"])
#     assert result.exit_code == 0
#     for description in expected_descriptions:
#         assert description in result.stdout
#
# import re
#
# import pytest
# from typer.testing import CliRunner
#
# from wc import app
#
#
# @pytest.fixture()
# def runner() -> CliRunner:
#     return CliRunner()
#
#
# def test_progress(capfd, runner):
#     result = runner.invoke(app, [])
#     pat = re.compile(r'^Processing... ━+ 100% 0:\d+:\d+\nProcessed \d+ things.$')
#     assert result.exit_code == 0
#     assert pat.match(result.output.strip())
#
# from typing import Dict, Optional
#
# import pytest  # type: ignore
#
# from wc import combine_and_count
#
# fruit = {"apple": 3, "banana": 2, "orange": 1}
# veggies = {"radish": 5, "artichoke": 2, "chard": 1}
#
#
# def test_non_overlapping_dicts() -> None:
#     """The union of disjoint dicts is their sum."""
#     assert combine_and_count(fruit, veggies) == {
#         "apple": 3,
#         "banana": 2,
#         "orange": 1,
#         "radish": 5,
#         "artichoke": 2,
#         "chard": 1,
#     }
#
#
# def test_overlapping_dicts() -> None:
#     """Add values of identical keys."""
#     more_fruit = {"pear": 5, "orange": 2, "kiwi": 1}
#     assert combine_and_count(fruit, more_fruit) == {
#         "apple": 3,
#         "banana": 2,
#         "orange": 3,
#         "pear": 5,
#         "kiwi": 1,
#     }
#
#
# def test_union_with_empty_dict() -> None:
#     """If either arg is an empty dictionary, return the other."""
#     empty_sack: Dict[Optional[str], Optional[int]] = {}
#     assert combine_and_count(fruit, empty_sack) == fruit
#     assert combine_and_count(empty_sack, fruit) == fruit
#     assert combine_and_count(empty_sack, empty_sack) == empty_sack
#
#
# def test_bad_union() -> None:
#     """Trying to combine the uncombinable raises TypeError.
#
#     This doesn't exhaustively check all possible bad-args handling,
#     but does try a couple of cases.
#     """
#     bad_fruit = {"orange": "two", "durian": 1}  # value you can't add
#     not_a_dict = "What am I, chopped liver?"  # not even a dictionary
#     with pytest.raises(TypeError):
#         combine_and_count(fruit, bad_fruit)
#     with pytest.raises(TypeError):
#         combine_and_count(not_a_dict, fruit)  # type: ignore
#
# import pytest
#
# from wc import validate_pangram
#
# @pytest.mark.parametrize(
#     "pangram",
#     [
#         "thequickbrownfoxjumpsoverthelazydog",
#         "The quick brown fox jumps over a lazy dog",
#         "The five boxing wizards jump quickly",
#         "Pack my box with five dozen liquor jugs",
#         "Amazingly few discotheques provide jukeboxes",
#         "The quick onyx goblin jumps over the lazy dwarf",
#     ],
# )
# def test_validate_pangram(pangram):
#     assert validate_pangram(pangram)
#
#
# @pytest.mark.parametrize(
#     "non_pangram",
#     [
#         "PYBITES IS A COMMUNITY OF PYTHON CODERS",
#         "pybites",
#         "pretty much anything else",
#     ],
# )
# def test_validate_non_pangram(non_pangram):
#     assert not validate_pangram(non_pangram)
#
# import pytest
#
# from wc import reverse_letters
#
#
# @pytest.mark.parametrize(
#     "input_str, expected_output",
#     [
#         ("ab-cd", "dc-ba"),
#         ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
#         ("ab5dEf", "fE5dba"),
#     ],
# )
# def test_reverse_letters(input_str, expected_output):
#     assert reverse_letters(input_str) == expected_output

# from wc import uppercase_vowels
#
#
# def test_uppercase_vowels_simple():
#     assert uppercase_vowels("abCDefghijkl") == "AbcdEfghIjkl"
#     assert (
#         uppercase_vowels("This test should pass itself")
#         == "thIs tEst shOUld pAss ItsElf"
#     )
#     assert uppercase_vowels("data.jpg foul") == "dAtA jpg fOUl"
#
#
# def test_uppercase_vowels_punctuation():
#     assert uppercase_vowels(".") == " "
#     assert uppercase_vowels("-,.?~a") == "     A"
#     assert uppercase_vowels("_.aBCEDF") == "  AbcEdf"
#
#
# def test_uppercase_vowels_files():
#     assert uppercase_vowels("sample.mp3") == "sAmplE.mp3"
#     assert uppercase_vowels("MUSIC.jpeg") == "mUsIc.jpeg"
#     assert uppercase_vowels("what is file.pdf") == "whAt Is fIlE.pdf"
#

#
# from wc import load_words, calc_word_value, max_word_value
#
# words = load_words()
#
# def test_load_words():
#     assert type(words) == list
#     assert len(words) == 235886
#     assert words[0] == 'A'
#     assert words[-1] == 'Zyzzogeton'
#     assert ' ' not in ''.join(words)
#
#
# def test_calc_word_value():
#     assert calc_word_value('bob') == 7
#     assert calc_word_value('JuliaN') == 13
#     assert calc_word_value('PyBites') == 14
#     assert calc_word_value('benzalphenylhydrazone') == 56
#
#
# def test_max_word_value():
#     test_words = ['bob', 'julian', 'pybites', 'quit', 'barbeque']
#     assert max_word_value(test_words) == 'barbeque'
#     assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'
#
#
# def test_non_scrabble_characters():
#     # thanks Joakim
#     assert max_word_value(["a", "åäö"]) == "a"
#
# from wc import get_pybites_top_tags
#
#
# def test_get_pybites_top_10_tags():
#     expected = [('python', 79),
#                 ('learning', 79),
#                 ('codechallenges', 72),
#                 ('twitter', 62),
#                 ('tips', 61),
#                 ('flask', 52),
#                 ('news', 49),
#                 ('django', 37),
#                 ('code', 25),
#                 ('github', 24)]
#     actual = get_pybites_top_tags()
#     assert actual == expected
#
#
# def test_get_pybites_top_5_tags():
#     expected = [('python', 79),
#                 ('learning', 79),
#                 ('codechallenges', 72),
#                 ('twitter', 62),
#                 ('tips', 61)]
#     actual = get_pybites_top_tags(n=5)
#     assert actual == expected
#
# from wc import (diehard_pybites,
#                        gen_files, Stats)
#
#
# def test_gen_files():
#     ret = list(gen_files())
#     assert ret[:3] == ["03/mridubhatnagar",
#                        "03/aleksandarknezevic",
#                        "04/blair_young"]
#     assert ret[-3:] == ["22/wonderfulboyx",
#                         "25/bbelderbos",
#                         "25/santiagobenitez"]
#
#
# def test_diehard_pybites():
#     ret = diehard_pybites()
#     assert ret == Stats(user='clamytoe', challenge=('01', 7))
#
#
# def test_diehard_other_input():
#     ret = diehard_pybites(
#         files=[
#             "22/wonderfulboyx",
#             "25/bbelderbos",  # ignored
#             "25/clamytoe",
#             "21/wonderfulboyx",
#             "25/santiagobenitez",
#             "23/santiagobenitez",
#             "07/santiagobenitez"
#         ])
#     assert ret == Stats(user='santiagobenitez', challenge=('25', 2))

# from datetime import datetime, timedelta
#
# from wc import loglines, convert_to_datetime, time_between_shutdowns
#
#
# def test_convert_to_datetime():
#     line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
#     line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
#     line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
#     assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
#     assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
#     assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)
#
#
# def test_time_between_events():
#     diff = time_between_shutdowns(loglines)
#     assert type(diff) == timedelta
#     assert str(diff) == '0:03:31'
#
# from wc import load_dictionary, is_palindrome, get_longest_palindrome
#
#
# def test_is_palindrome():
#     assert is_palindrome('Aibohphobia')
#     assert is_palindrome('Avid diva')
#     assert is_palindrome('Avid diva. ')
#     assert is_palindrome('A Toyota’s a Toyota.')
#     assert is_palindrome('A man, a plan, a canal: Panama')
#     assert is_palindrome("No 'x' in 'Nixon'")
#     assert is_palindrome('malayalam')
#
#     assert not is_palindrome('PyBites')
#     assert not is_palindrome('malayalan')
#     assert not is_palindrome('toyota')
#     assert not is_palindrome('palindrome')
#
#
# def test_get_longest_palindrome():
#     words = load_dictionary()
#     assert get_longest_palindrome() == 'malayalam'
#
#     new_longest = 'A car, a man, a maraca.'
#     words = list(words) + [new_longest]
#     assert get_longest_palindrome(words) == new_longest
#

#
# import pytest
#
# from wc import positive_divide
#
#
# def test_positive_divide_good_values():
#     assert positive_divide(1, 2) == 0.5
#     assert positive_divide(1, 0) == 0
#     assert positive_divide(-1, -2) == 0.5
#     assert positive_divide(1.5, 2) == 0.75
#
#
# def test_positive_divide_exceptions():
#     try:
#         positive_divide(2, 0)
#     except ZeroDivisionError:
#         pytest.fail("Unexpected ZeroDivisionError!")
#     with pytest.raises(TypeError):
#         positive_divide(1, 's')
#         positive_divide([], 2)
#     with pytest.raises(ValueError):
#         positive_divide(1, -2)
#         positive_divide(-1, 2)


#
# import pytest
#
# from wc import (get_secret_token, SECRET,
#                       UserDoesNotExist, UserAccessExpired, UserNoPermission)
#
#
# def test_get_secret_token():
#     assert issubclass(UserDoesNotExist, Exception)
#     assert issubclass(UserAccessExpired, Exception)
#     assert issubclass(UserNoPermission, Exception)
#
#     with pytest.raises(UserDoesNotExist):
#         get_secret_token('Tim')
#     with pytest.raises(UserAccessExpired):
#         get_secret_token('Bob')
#     with pytest.raises(UserNoPermission):
#         get_secret_token('Julian')
#
#     assert get_secret_token('PyBites') == SECRET
#
# import json
#
# from wc import blog, dict2nt, nt2json
#
# nt = dict2nt(blog)
#
#
# def test_dict2nt():
#     assert nt.name == 'PyBites'
#     assert nt.founders[1] == 'Bob'
#     assert nt.tags[2] == 'Learn by Doing'
#     assert nt.started.year == 2016
#
#     assert nt.__class__.__base__ == tuple
#     assert hasattr(nt, '_asdict')
#
#
# def test_nt2json():
#     output = nt2json(nt)
#     assert type(output) == str
#
#     data = json.loads(output)
#     assert data['name'] == 'PyBites'
#     assert data['founders'][0] == 'Julian'
#     assert data['tags'][0] == 'Python'
#     assert data['started'][:4] == '2016'
#
# import re
#
# from wc import (names, aliases, points, awake,
#                    SEPARATOR, generate_table)
#
# # cast to list in case of generator
# table1 = list(generate_table(names))
# table2 = list(generate_table(names, aliases))
# table3 = list(generate_table(names, aliases, points))
# table4 = list(generate_table(names, aliases, points, awake))
#
#
# def test_generate_table():
#     assert len(table1) == len(table2) == len(table3) == len(table4) == 6
#
#     assert table1[0].count(SEPARATOR) == 0
#     assert table2[0].count(SEPARATOR) == 1
#     assert table3[0].count(SEPARATOR) == 2
#     assert table4[0].count(SEPARATOR) == 3
#
#     assert table1[1].split(SEPARATOR)[0] == 'Bob'
#     assert table2[1].split(SEPARATOR)[1] == 'Nerd'
#     assert re.match(r'\d+', table3[2].split(SEPARATOR)[2])
#     assert table4[2].split(SEPARATOR)[3]
#
# import pytest
#
# from wc import friends_teams
#
# friends = 'Bob Dante Julian Martin'.split()
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante'), True),
#     (('Bob', 'Julian'), True),
#     (('Bob', 'Martin'), True),
#     (('Dante', 'Julian'), True),
#     (('Dante', 'Martin'), True),
#     (('Julian', 'Martin'), True),
#     # order does not matter
#     (('Dante', 'Bob'), False),
#     (('Julian', 'Bob'), False),
#     (('Martin', 'Bob'), False),
#     (('Julian', 'Dante'), False),
#     (('Martin', 'Dante'), False),
#     (('Martin', 'Julian'), False),
#     # not with self
#     (('Julian', 'Julian'), False),
# ])
# def test_team_of_two_order_does_not_matter(test_input, expected):
#     """First test lists all combos"""
#     combos = list(friends_teams(friends, team_size=2, order_does_matter=False))
#     assert len(combos) == 6
#     if expected:
#         assert test_input in combos
#     else:
#         assert test_input not in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante'), True),
#     (('Dante', 'Julian'), True),
#     (('Dante', 'Martin'), True),
#     # order does matter
#     (('Dante', 'Bob'), True),
#     (('Julian', 'Dante'), True),
#     (('Martin', 'Dante'), True),
# ])
# def test_team_of_two_order_does_matter(test_input, expected):
#     """From here on just test a subset of combos"""
#     combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
#     assert len(combos) == 12
#     assert test_input in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), True),
#     (('Bob', 'Dante', 'Martin'), True),
#     (('Bob', 'Julian', 'Martin'), True),
#     (('Dante', 'Julian', 'Martin'), True),
#     # order does not matter
#     (('Dante', 'Bob', 'Martin'), False),
#     (('Julian', 'Martin', 'Dante'), False),
#     # no one goes twice
#     (('Dante', 'Dante', 'Martin'), False),
# ])
# def test_team_of_three_order_does_not_matter(test_input, expected):
#     combos = list(friends_teams(friends, team_size=3, order_does_matter=False))
#     assert len(combos) == 4
#     if expected:
#         assert test_input in combos
#     else:
#         assert test_input not in combos
#
#
# @pytest.mark.parametrize('test_input,expected', [
#     (('Bob', 'Dante', 'Julian'), True),
#     (('Bob', 'Dante', 'Martin'), True),
#     (('Bob', 'Julian', 'Martin'), True),
#     (('Dante', 'Julian', 'Martin'), True),
#     # order does matter
#     (('Dante', 'Bob', 'Martin'), True),
#     (('Julian', 'Martin', 'Dante'), True),
# ])
# def test_team_of_three_order_does_matter(test_input, expected):
#     combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
#     assert len(combos) == 24
#     assert test_input in combos
#
#
# def test_default_team_size():
#     friends = ("Bob", "Dante", "Julian")
#     combos = list(friends_teams(friends, order_does_matter=True))
#     assert len(combos) == 6
#     assert ("Bob", "Dante") in combos
#
#
# def test_default_order_matters():
#     friends = ("Bob", "Dante", "Julian")
#     combos = list(friends_teams(friends, team_size=2))
#     assert len(combos) == 3
#     combos = list(friends_teams(friends, team_size=2, order_does_matter=True))
#     assert len(combos) == 6
#
# from wc import get_harry_most_common_word
#
#
# def test_get_harry_most_common_word():
#     top_word = get_harry_most_common_word()
#     assert type(top_word) == tuple
#     assert top_word[0] == 'dursley'
#     assert top_word[1] == 45
#
# from wc import make_html
#
#
# def test_make_html():
#     @make_html('p')
#     @make_html('strong')
#     def get_text(text='I code with PyBites'):
#         return text
#
#     assert get_text() == '<p><strong>I code with PyBites</strong></p>'
#
# import pytest
#
# from wc import int_args
#
#
# @int_args
# def sum_numbers(*numbers):
#     return sum(numbers)
#
#
# def test_valid_args():
#     assert sum_numbers(1, 2, 3) == 6
#
#
# def test_invalid_type_str():
#     with pytest.raises(TypeError):
#         sum_numbers(1, 'string', 3)
#
#
# def test_invalid_type_float():
#     with pytest.raises(TypeError):
#         sum_numbers(1, 2.1, 3)
#
#
# def test_negative_number():
#     with pytest.raises(ValueError):
#         sum_numbers(1, 2, -3)
#
# from wc import validate_password, used_passwords
#
#
# def test_password_len():
#     assert not validate_password('short')
#     assert not validate_password('waytoolongpassword')
#
#
# def test_password_missing_chars():
#     assert not validate_password('UPPERCASE')
#     assert not validate_password('lowercase')
#     assert not validate_password('PW_no_digits')
#     assert not validate_password('Pw9NoPunc')
#     assert not validate_password('_password_')
#     assert not validate_password('@#$$)==1')
#
#
# def test_password_only_one_letter():
#     assert not validate_password('@#$$)==1a')
#
#
# def test_validate_password_good_pws():
#     assert validate_password('passWord9_')
#     assert validate_password('another>4Y')
#     assert validate_password('PyBites@1912')
#     assert validate_password('We<3Python')
#
#
# def test_password_not_used_before():
#     assert not validate_password('PassWord@1')
#     assert not validate_password('PyBit$s9')
#
#
# def test_password_cache_cannot_reuse():
#     num_passwords_use = len(used_passwords)
#     assert validate_password('go1@PW')
#     assert len(used_passwords) == num_passwords_use + 1
#     assert not validate_password('go1@PW')
#
#
# def test_password_needs_two_lowercase_chars():
#     assert not validate_password('ABCa@;1')
#     assert not validate_password('PyBIT;$')
# from wc import welcome
#
#
# def test_no_account():
#     """User is not on the system"""
#     assert welcome('anonymous') == 'please create an account'
#
#
# def test_not_loggedin():
#     """User is on the system but not logged in"""
#     assert welcome('julian') == 'please login'
#
#
# def test_loggedin():
#     """User is on the system and logged in"""
#     assert welcome('sue') == 'welcome back sue'
#
#
# def test_docstring():
#     """Decorator should not lose function's docstring"""
#     assert welcome.__doc__ == 'Return a welcome message if logged in'
# import inspect
# from unittest.mock import patch
#
# import pytest
#
# from wc import Promo, NoBitesAvailable
#
#
# def grab_bites(promo, amount=10):
#     # _ is a throw-away variable (just want a loop)
#     for _ in range(amount):
#         promo.new_bite()
#
#
# @pytest.fixture
# def promo():
#     """Make a fresh new promo object for each test"""
#     return Promo()
#
#
# def test_bites_not_done_start(promo):
#     assert len(promo.all_bites) == 15
#     assert len(promo.bites_done) == 5
#
#
# @patch('random.choice', side_effect=[7, 9, 11])
# @patch('random.sample', side_effect=[[7], [9], [11]])
# def test_new_bite(choice_mock, sample_mock, promo):
#     assert promo.new_bite() == 7
#     assert promo.new_bite() == 9
#     assert promo.new_bite() == 11
#
#
# def test_random_is_used(promo):
#     src = inspect.getsource(promo._pick_random_bite)
#     assert 'sample' in src or 'choice' in src
#
#
# def test_pick_random_bite_returns_not_done_bite(promo):
#     for _ in range(10):
#         bite = promo._pick_random_bite()
#         assert type(bite) == int
#         assert bite in promo.all_bites
#         assert bite not in promo.bites_done
#
#
# def test_internal_data_structures(promo):
#     # fixture = new data = start over
#     assert len(promo.bites_done) == 5
#     grab_bites(promo, amount=7)
#     # bites_done incremented with 7
#     assert len(promo.bites_done) == 12
#
#
# def test_raise_exception_if_no_more_bites(promo):
#     assert len(promo.bites_done) == 5
#     grab_bites(promo)
#     # exhausted bites
#     with pytest.raises(NoBitesAvailable):
#         promo._pick_random_bite()
#
#
# def test_work_with_2_users_and_promo_instances(promo):
#     alices_promo = Promo()
#     grab_bites(alices_promo)
#     assert len(alices_promo.bites_done) == 15
#     # exhausted Bites:
#     with pytest.raises(NoBitesAvailable):
#         alices_promo.new_bite()
#     # another user = new independent Promo instance
#     bobs_promo = Promo()
#     assert len(bobs_promo.bites_done) == 5
#
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
#
# import pytest
#
# from wc import (get_movie_data,
#                   get_single_comedy,
#                   get_movie_most_nominations,
#                   get_movie_longest_runtime)
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# DATA = 'omdb_data'
#
# DATA_LOCAL = TMP / DATA
# if not Path(DATA_LOCAL).exists():
#     urlretrieve(S3 + DATA, DATA_LOCAL)
#
#
# @pytest.fixture(scope="module")
# def movies():
#     files = []
#     with open(DATA_LOCAL) as f:
#         for i, line in enumerate(f.readlines(), 1):
#             movie_json = TMP / f'{i}.json'
#             with open(movie_json, 'w') as f:
#                 f.write(f'{line}\n')
#             files.append(movie_json)
#
#     yield get_movie_data(files)
#
#     # teardown
#     for file_ in files:
#         file_.unlink()
#
#
# def test_len_movie_data(movies):
#     assert len(movies) == 5
#
#
# def test_type_of_movie_elements(movies):
#     assert all(type(m) == dict for m in movies)
#
#
# @pytest.mark.parametrize("func, expected", [
#     (get_single_comedy, 'Horrible Bosses'),
#     (get_movie_most_nominations, 'Fight Club'),
#     (get_movie_longest_runtime, 'Blade Runner 2049'),
# ])
# def test_data_analysis(func, expected, movies):
#     assert func(movies) == expected
#
# from datetime import datetime
#
# import pytest
#
# from wc import _get_dates, convert_to_datetime, get_month_most_posts
#
#
# @pytest.fixture(scope="module")
# def dates():
#     return _get_dates()
#
#
# @pytest.mark.parametrize("date_str, expected", [
#     ('Thu, 04 May 2017 20:46:00 +0200', datetime(2017, 5, 4, 20, 46)),
#     ('Wed, 22 Mar 2017 12:42:00 +0100', datetime(2017, 3, 22, 12, 42)),
#     ('Mon, 20 Feb 2017 00:01:00 +0100', datetime(2017, 2, 20, 0, 1)),
#     ('Sun, 07 Jan 2018 12:00:00 +0100', datetime(2018, 1, 7, 12, 0)),
#     ('Sat, 15 Apr 2017 01:00:00 +0200', datetime(2017, 4, 15, 1, 0))
# ])
# def test_convert_to_datetime(date_str, expected):
#     dt = convert_to_datetime(date_str)
#     # support tz aware datetimes
#     assert dt.replace(tzinfo=None) == expected.replace(tzinfo=None)
#
#
# def test_get_month_most_posts(dates):
#     converted_dates = [convert_to_datetime(d) for d in dates]
#     assert get_month_most_posts(converted_dates) == '2017-01'
#
#
# def test_get_month_most_posts_more_in_2018(dates):
#     # make Jan 2018 > Jan 2017
#     for _ in range(25):
#         dates.append('Sun, 07 Jan 2018 12:00:00 +0100')
#
#     converted_dates = [convert_to_datetime(d) for d in dates]
#     assert get_month_most_posts(converted_dates) == '2018-01'
#
# from collections import defaultdict
#
# import pytest
#
# from wc import (get_movies_by_director, get_average_scores,
#                        calc_mean_score, Movie)
#
#
# @pytest.fixture(scope="module")
# def movies():
#     return get_movies_by_director()
#
#
# @pytest.fixture(scope="module")
# def scores(movies):
#     return get_average_scores(movies)
#
#
# def test_get_movies_by_director(movies):
#     assert 'Sergio Leone' in movies
#     assert len(movies['Sergio Leone']) == 4
#     assert len(movies['Peter Jackson']) == 12
#
#
# def test_director_movies_data_structure(movies):
#     assert type(movies) in (dict, defaultdict)
#     assert type(movies['Peter Jackson']) == list
#     assert type(movies['Peter Jackson'][0]) == Movie
#
#
# def test_calc_mean_score(movies):
#     movies_sergio = movies['Sergio Leone']
#     movies_nolan = movies['Christopher Nolan']
#     assert calc_mean_score(movies_sergio) == 8.5
#     assert calc_mean_score(movies_nolan) == 8.4
#
#
# def test_get_average_scores_top_directors(scores):
#     expected = [('Sergio Leone', 8.5),
#                 ('Christopher Nolan', 8.4),
#                 ('Quentin Tarantino', 8.2),
#                 ('Hayao Miyazaki', 8.2),
#                 ('Frank Darabont', 8.0),
#                 ('Stanley Kubrick', 8.0),
#                 ('James Cameron', 7.9),
#                 ('Joss Whedon', 7.9)]
#     assert scores[0:8] == expected
#
#
# @pytest.mark.parametrize("director", [
#     'Quentin Tarantino', 'Hayao Miyazaki',
#     'Frank Darabont', 'Stanley Kubrick',
#     'James Cameron', 'Joss Whedon',
#     'Alejandro G. Iñárritu',
# ])
# def test_director_in_top_scores(director, scores):
#     # order / score might slightly change depending the way the mean
#     # is calculated so only test director names in top scores
#     top_scores = scores[2:13]
#     directors = {score[0] for score in top_scores}
#     assert director in directors
#
#
# def test_ignore_older_movies(movies):
#     """Lowell Sherman's Black and White is from 1933 and should
#        be skipped"""
#     assert len(movies["Lowell Sherman"]) == 0
#
# from random import randint
# from collections import namedtuple
#
# from wc import transpose
#
# POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
#          '2017-11': 12, '2017-12': 11, '2018-1': 3}
# NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']
#
# Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')
#
#
# def _gen_community():
#     for name in NAMES:
#         yield Member(name=name,
#                      since_days=randint(1, 365),
#                      karma_points=randint(1, 100),
#                      bitecoin_earned=randint(1, 100))
#
#
# def test_transpose_dict():
#     months, num_posts = transpose(POSTS)
#     assert list(months) == ['2017-8', '2017-9', '2017-10',
#                             '2017-11', '2017-12', '2018-1']
#     assert list(num_posts) == [19, 13, 13, 12, 11, 3]
#
#
# def test_transpose_list_tuplies():
#     community = list(_gen_community())
#     names, days, karma, bitecoin = transpose(community)
#     assert list(names) == NAMES
#     assert list(days) == [m.since_days for m in community]
#     assert list(karma) == [m.karma_points for m in community]
#     assert list(bitecoin) == [m.bitecoin_earned for m in community]
#
# from datetime import datetime
# import inspect
#
# from wc import (numbers, dates, earnings_mln,
#                    get_largest_number, get_latest_dates,
#                    get_highest_earnings)

#
# def test_get_top_n():
#     assert get_largest_number(numbers) == [6, 5, 4]
#     assert get_largest_number(numbers, n=2) == [6, 5]
#     assert get_largest_number(numbers, n=4) == [6, 5, 4, 3]
#
#     assert get_latest_dates(dates) == [datetime(2019, 2, 27, 0, 0),
#                                        datetime(2018, 12, 19, 0, 0),
#                                        datetime(2018, 11, 19, 0, 0)]
#     assert get_latest_dates(dates, n=1) == [datetime(2019, 2, 27, 0, 0)]
#
#     assert get_highest_earnings(earnings_mln) == [{'name': 'Beyoncé Knowles',
#                                                    'earnings': 105},
#                                                   {'name': 'J.K. Rowling',
#                                                    'earnings': 95},
#                                                   {'name': 'Cristiano Ronaldo',
#                                                    'earnings': 93}]
#
#
# def test_heapq_used():
#     err_msg = 'We want you to play with heapq for this one :)'
#     assert 'heapq' in inspect.getsource(get_largest_number), err_msg
#     assert 'heapq' in inspect.getsource(get_latest_dates), err_msg
#     assert 'heapq' in inspect.getsource(get_highest_earnings), err_msg
#
# import pytest
#
# from wc import get_profile
#
#
# def test_get_profile_no_name():
#     with pytest.raises(TypeError):
#         assert get_profile()
#
#
# def test_get_profile_no_age():
#     with pytest.raises(TypeError):
#         assert get_profile('tim')
#
#
# def test_get_profile_valueerror():
#     with pytest.raises(ValueError):
#         assert get_profile('tim', 'nonint')
#
#
# def test_get_profile_too_many_sports():
#     with pytest.raises(ValueError):
#         sports = ['tennis', 'basketball', 'badminton',
#                   'baseball', 'volleyball', 'boxing']
#         assert get_profile('tim', 36, *sports)
#
#
# def test_get_profile_dict():
#     assert get_profile('tim', 36) == {'name': 'tim', 'age': 36}
#
#
# def test_get_profile_one_sport():
#     expected = {'name': 'tim', 'age': 36,
#                 'sports': ['tennis']}
#     assert get_profile('tim', 36, 'tennis') == expected
#
#
# def test_get_profile_two_sports():
#     expected = {'name': 'tim', 'age': 36,
#                 'sports': ['basketball', 'tennis']}
#     assert get_profile('tim', 36, 'tennis', 'basketball') == expected
#
#
# def test_get_profile_award():
#     expected = {'name': 'tim', 'age': 36,
#                 'awards': {'champ': 'helped out team in crisis'}}
#     assert get_profile('tim', 36,
#                        champ='helped out team in crisis') == expected
#
#
# def test_get_profile_two_sports_and_one_award():
#     expected = {'name': 'tim', 'age': 36,
#                 'sports': ['basketball', 'tennis'],
#                 'awards': {'champ': 'helped out team in crisis'}}
#     assert get_profile('tim', 36, 'tennis', 'basketball',
#                        champ='helped out team in crisis') == expected
#
#
# def test_get_profile_two_sports_and_three_awards():
#     expected = {'name': 'tim', 'age': 36,
#                 'sports': ['basketball', 'tennis'],
#                 'awards': {'champ': 'helped out the team in crisis',
#                            'service': 'going the extra mile for our customers',
#                            'attitude': 'unbeatable positive + uplifting'}}
#     assert get_profile('tim', 36, 'tennis', 'basketball',
#                        service='going the extra mile for our customers',
#                        champ='helped out the team in crisis',
#                        attitude='unbeatable positive + uplifting') == expected
#
# from wc import get_all_timestamps, calc_total_course_duration
#
#
# def test_get_all_timestamps():
#     timestamps = get_all_timestamps()
#     assert len(timestamps) == 99
#     assert '2:29' in timestamps
#     assert '4:19' in timestamps
#     assert '6:06' in timestamps
#     assert '8:39' in timestamps
#
#
# def test_calc_total_course_duration():
#     timestamps = get_all_timestamps()
#     assert '6:50:31' in calc_total_course_duration(timestamps)
#
# from wc import create_chart
#
# expected_lines = """02-13 ...........
# 02-14 ..............
# 02-15 .................
# 02-16 ............
# 02-19 🐍.......🐍
# 02-20 ...
# 02-21 ..............🐍
# 02-22 🐍...................""".split('\n')
#
# def test_valid_output(capfd):
#     create_chart()
#     out, _ = capfd.readouterr()
#     for line in expected_lines:
#         assert line in out, f'"{line}" should be in output of create_chart'
#
# from wc import get_book
#
# book = get_book()
#
#
# def test_type():
#     assert isinstance(book, tuple)
#
#
# def test_book_title():
#     assert book.title == 'Mastering TypeScript - Second Edition'
#
#
# def test_book_description():
#     assert book.description == ('Build enterprise-ready, industrial-strength '
#                                 'web applications using '
#                                 'TypeScript and leading JavaScript frameworks')
#
#
# def test_book_image():
#     assert book.image == '//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png'  # noqa E501
#
#
# def test_book_link():
#     assert book.link == '/application-development/mastering-typescript-second-edition'  # noqa E501
#
# from datetime import timedelta
#
# from wc import (py2_earth_hours_left, py2_miller_min_left,
#                     BITE_CREATED_DT)
#
# START_DATE = BITE_CREATED_DT - timedelta(days=1000)
#
#
# def test_py2_earth_hours_left():
#     assert py2_earth_hours_left() == 16152.6
#
#
# def test_py2_miller_min_left():
#     assert py2_miller_min_left() == 15.8
#
#
# def test_py2_earth_hours_left_another_start_date():
#     assert py2_earth_hours_left(START_DATE) == 40152.6
#
#
# def test_py2_miller_min_left_another_start_date():
#     assert py2_miller_min_left(START_DATE) == 39.29
#
# import pytest
# from wc import create_parser, call_calculator
#
#
# @pytest.fixture
# def parser():
#     return create_parser()
#
#
# def test_one_arg_no_numbers_exits(parser):
#     with pytest.raises(SystemExit):
#         args = parser.parse_args(['--add'])
#         call_calculator(args=args)
#
#
# def test_call_with_wrong_operation(parser):
#     with pytest.raises(SystemExit):
#         args = parser.parse_args(['--sum', '10'])
#         call_calculator(args=args)
#
#
# def test_help_text_hints(parser, capfd):
#     with pytest.raises(SystemExit):
#         parser.parse_args(['-h'])
#
#     output = capfd.readouterr()[0].lower()
#     assert 'usage' in output
#     assert 'a simple calculator' in output
#     for op in 'add sub mul div'.split():
#         assert op in output
#
#
# @pytest.mark.parametrize("args, expected", [
#     (['1'], 1),
#     (['1', '2'], 3),
#     (['1', '2', '3'], 6),
#     (['1', '2', '3', '4.5'], 10.5),
# ])
# def test_add_operations(parser, args, expected):
#     args = parser.parse_args(['--add'] + args)
#     assert call_calculator(args) == expected
#
#
# @pytest.mark.parametrize("args, expected", [
#     (['1'], 1),
#     (['1', '2'], -1),
#     (['10', '7', '0.5'], 2.5),
#     (['11', '9', '2.2', '1.8'], -2),
# ])
# def test_sub_operations(parser, args, expected):
#     args = parser.parse_args(['--sub'] + args)
#     assert call_calculator(args) == expected
#
#
# @pytest.mark.parametrize("args, expected", [
#     (['1'], 1),
#     (['1', '2'], 2),
#     (['3.5', '2', '4.2'], 29.4),
#     (['3.5', '2', '4.2', '-1'], -29.4),
# ])
# def test_mul_operations(parser, args, expected):
#     args = parser.parse_args(['--mul'] + args)
#     assert call_calculator(args) == expected
#
#
# @pytest.mark.parametrize("args, expected", [
#     (['2'], 2),
#     (['1', '0'], 0),
#     (['2.2', '7', '1.1'], 0.29),
#     (['3', '2', '3', '5'], 0.1),
# ])
# def test_div_operations(parser, args, expected):
#     args = parser.parse_args(['--div'] + args)
#     assert call_calculator(args) == expected
#
# import pytest
#
# from wc import MultiplicationTable
#
#
# @pytest.fixture
# def t10():
#     return MultiplicationTable(10)
#
#
# @pytest.fixture
# def t3():
#     return MultiplicationTable(3)
#
#
# @pytest.mark.parametrize("arg, ret", [
#     (1, 1),
#     (5, 25),
#     (10, 100),
#     (100, 10000),
#
# ])
# def test_table_len(arg, ret):
#     assert len(MultiplicationTable(arg)) == ret
#
#
# @pytest.mark.parametrize("arg, ret", [
#     ((6, 6), 36),
#     ((4, 2), 8),
#     ((7, 6), 42),
#     ((8, 8), 64),
#     ((10, 10), 100),
# ])
# def test_calc(t10, arg, ret):
#     assert t10.calc_cell(*arg) == ret
#
#
# def test_calc_exception(t3, capfd):
#     with pytest.raises(IndexError):
#         t3.calc_cell(3, 4)
#     with pytest.raises(IndexError):
#         t3.calc_cell(4, 3)
#
#
# def test_table_str(t3):
#     output = str(t3)
#     assert '1 | 2 | 3' in output
#     assert '2 | 4 | 6' in output
#     assert '3 | 6 | 9' in output
#
# import pytest
#
# from wc import create_uno_deck, SUITS, UnoCard
#
#
# def _count_suits(deck, suit):
#     return len([card for card in deck if card.suit == suit])
#
#
# def _count_suitcard(deck, suit, name):
#     return sum(1 for card in deck if card.suit == suit
#                and str(card.name) == name)



#
#
# @pytest.fixture(scope="module")
# def deck():
#     return create_uno_deck()
#
#
# def test_create_uno_deck_len(deck):
#     assert len(deck) == 108
#
#
# def test_create_uno_deck_type(deck):
#     assert type(deck) == list
#     assert all(type(card) == UnoCard for card in deck)
#
#
# @pytest.mark.parametrize("suit, count", [
#     ('Red', 25),
#     ('Green', 25),
#     ('Yellow', 25),
#     ('Blue', 25),
#     (None, 8),  # wild cards don't have an associated suit
# ])
# def test_create_uno_deck_suit_distribution(deck, suit, count):
#     assert _count_suits(deck, suit) == count
#
#
# @pytest.mark.parametrize("name, count", [
#     ('0', 1), ('1', 2), ('2', 2), ('3', 2), ('4', 2),
#     ('5', 2), ('6', 2), ('7', 2), ('8', 2), ('9', 2),
#     ('Draw Two', 2), ('Skip', 2), ('Reverse', 2),
# ])
# def test_create_uno_deck_suit_cards(deck, name, count):
#     for suit in SUITS:
#         _count_suitcard(deck, suit, name) == count
#
# from string import ascii_lowercase
#
# from wc import (contains, contains_fast,
#                          ordered_list_max, ordered_list_max_fast,
#                          list_concat, list_concat_fast,
#                          list_inserts, list_inserts_fast,
#                          list_creation, list_creation_fast)
#
# alist = list(range(1000000))
# aset = set(alist)
# listofstrings = list(ascii_lowercase) * 1000
#
#
# def test_contains():
#     t1, res1 = contains(alist, 500)
#     t2, res2 = contains_fast(aset, 1000)
#     assert res1 == res2
#     assert t1 > t2
#
#
# def test_ordered_max():
#     t1, res1 = ordered_list_max(alist)
#     t2, res2 = ordered_list_max_fast(alist)
#     assert res1 == res2
#     assert t1 > t2
#
#
# def test_concat():
#     t1, res1 = list_concat(listofstrings)
#     t2, res2 = list_concat_fast(listofstrings)
#     assert res1 == res2
#     assert t1 > t2
#
#
# def test_list_insert():
#     t1, res1 = list_inserts(10000)
#     t2, res2 = list_inserts_fast(10000)
#     assert list(res1) == list(res2)
#     assert t1 > t2
#
#
# def test_list_creation():
#     t1, res1 = list_creation(10000)
#     t2, res2 = list_creation_fast(10000)
#     assert list(res1) == list(res2)
#     assert t1 > t2
#
# import pytest
#
# from wc import get_possible_dict_words
#
# scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
#                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
# LETTER_SCORES = {letter: score for score, letters in scrabble_scores
#                  for letter in letters.split()}
#
#
# def calc_word_value(word):
#     """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
#     return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)
#
#
# def max_word_value(words):
#     """Calc the max value of a collection of words"""
#     return max(words, key=calc_word_value)
#
#
# @pytest.mark.parametrize("draw, expected", [
#     ('T, I, I, G, T, T, L', 'gilt'),
#     ('O, N, V, R, A, Z, H', 'zonar'),
#     ('E, P, A, E, I, O, A', ('apio', 'peai')),
#     ('B, R, C, O, O, E, O', 'boce'),
#     ('G, A, R, Y, T, E, V', 'garvey'),
# ])
# def test_max_word(draw, expected):
#     draw = draw.split(', ')
#     words = get_possible_dict_words(draw)
#     if len(expected) > 1:
#         assert max_word_value(words) in expected
#     else:
#         assert max_word_value(words) == expected
# import pytest
#
# from wc import EggCreator, COLORS
#
#
# def test_iterator_type():
#     eg = EggCreator(10)
#     assert type(eg) == EggCreator
#
#
# def test_len_iterator_is_limit_input_arg():
#     ec = EggCreator(2)
#     assert len(list(ec)) == 2
#     ec = EggCreator(5)
#     assert len(list(ec)) == 5
#
#
# def test_call_next_on_iterator():
#     ec = EggCreator(2)
#     next_egg = next(ec)
#     assert next_egg.split()[0] in COLORS


#
# def test_iterator_raises_stop_iteration_exception():
#     ec = EggCreator(2)
#     next(ec)
#     next(ec)
#     with pytest.raises(StopIteration):
#         next(ec)
#
#
# def test_iterator_generates_random_colors():
#     ec = EggCreator(20)
#     output1 = list(ec)
#     ec = EggCreator(20)
#     output2 = list(ec)
#     assert output1 != output2
# import pytest
#
# from wc import RecordScore
#
#
# @pytest.fixture()
# def record():
#     """Make a RecordScore object with a few scores"""
#     record = RecordScore()
#     record(10)
#     record(9)
#     record(11)  # initial max
#     record(5)
#     return record
#
#
# def test_record_unbeaten(record):
#     assert record(9) == 11
#     record(10)
#     record(2)
#     assert record(4) == 11
#
#
# def test_record_got_beaten(record):
#     assert record(4) == 11
#     record(3)
#     record(12)  # new max
#     assert record(4) == 12
#     record(5)
#     record(16)  # new max
#     assert record(4) == 16
#
#
# def test_record_got_beaten_negative_values():
#     record = RecordScore()
#     record(-5)
#     assert record(-4) == -4
#     assert record(-6) == -4
#     assert record(-2) == -2
#
# import pytest
#
# from wc import get_belt
#
#
# @pytest.mark.parametrize("input_argument, expected_return", [
#     (0, None),
#     (9, None),
#     (10, 'white'),
#     (48, 'white'),
#     (50, 'yellow'),
#     (101, 'orange'),
#     (249, 'green'),
#     (250, 'blue'),
#     (251, 'blue'),
#     (400, 'brown'),
#     (599, 'brown'),
#     (600, 'black'),
#     (788, 'black'),
#     (800, 'paneled'),
#     (999, 'paneled'),
#     (1000, 'red'),
#     (1200, 'red'),
# ])
# def test_get_belt(input_argument, expected_return):
#     assert get_belt(input_argument) == expected_return
# from datetime import datetime
#
# import pytest
#
# from wc import within_schedule
#
#
# def test_too_late_aus():
#     # local hours [15, 23, 8]
#     dt = datetime(2018, 4, 18, 13, 28)
#     timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
#     assert not within_schedule(dt, *timezones)
#
#
# def test_all_good_aus_just_in_time_summertime():
#     # local hours [14, 22, 7]
#     dt = datetime(2018, 4, 18, 12, 28)
#     timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
#     assert within_schedule(dt, *timezones)
#
#
# def test_change_winter_time_aus_now_too_late():
#     # local hours [14, 23, 7]
#     dt = datetime(2018, 10, 18, 12, 28)
#     timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
#     assert not within_schedule(dt, *timezones)
#
#
# def test_too_late_for_chicago():
#     # local hours [8, 16, 1]
#     dt = datetime(2018, 4, 18, 6, 45)
#     timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
#     assert not within_schedule(dt, *timezones)
#
#
# def test_wrong_timezone():
#     dt = datetime(2018, 4, 18, 12, 28)
#     timezones = ['Europe/Madrid', 'bogus']
#     with pytest.raises(ValueError):
#         within_schedule(dt, *timezones)
#
# import pytest
#
# from wc import common_languages
#
#
# @pytest.fixture()
# def programmers():
#     return dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
#                 tim=['Python', 'Haskell', 'C++', 'JS'],
#                 sara=['Perl', 'C', 'Java', 'Python', 'JS'],
#                 paul=['C++', 'JS', 'Python'])
#
#
# def test_common_languages(programmers):
#     expected = ['JS', 'Python']
#     actual = common_languages(programmers)
#     assert sorted(list(actual)) == expected
#
#
# def test_adding_programmer_without_js(programmers):
#     programmers['sue'] = ['Scala', 'Python']
#     expected = ['Python']
#     actual = common_languages(programmers)
#     assert list(actual) == expected
#
#
# def test_adding_programmer_without_js_nor_python(programmers):
#     programmers['fabio'] = ['PHP']
#     expected = []
#     actual = common_languages(programmers)
#     assert list(actual) == expected
#
#
# def test_common_languages_adding_new_common_language(programmers):
#     programmers['bob'].append('C++')
#     programmers['sara'].append('C++')
#     expected = ['C++', 'JS', 'Python']
#     actual = common_languages(programmers)
#     assert sorted(list(actual)) == expected
#
# from wc import get_csv, create_user_bar_chart
#
#
# # making sure to call requests just once!
# content = get_csv()
#
# expected_output = """Africa/Algiers       | ++
# Africa/Cairo         | +
# Africa/Monrovia      | +
# Africa/Nairobi       | ++++
# America/Buenos_Aires | +
# America/Chicago      | ++++++++++++++
# America/Denver       | ++++
# America/Fortaleza    | +
# America/Los_Angeles  | +++++++++++++++++++++++++++++++++++
# America/Manaus       | +
# America/Mexico_City  | +++
# America/New_York     | +++++++++++++++++++++++++++
# America/Regina       | +
# America/Santiago     | +
# America/Sao_Paulo    | ++++
# Asia/Amman           | +
# Asia/Bangkok         | +
# Asia/Chongqing       | ++++
# Asia/Dhaka           | +
# Asia/Istanbul        | ++
# Asia/Jerusalem       | +
# Asia/Kolkata         | +++++++++++++
# Asia/Kuala_Lumpur    | +
# Asia/Muscat          | +
# Asia/Taipei          | +
# Australia/Brisbane   | +
# Australia/Canberra   | ++++++
# Australia/Perth      | +
# Europe/Amsterdam     | ++++++++++++++
# Europe/Athens        | ++
# Europe/Belgrade      | +
# Europe/Helsinki      | +
# Europe/London        | ++++++++++++
# Europe/Moscow        | ++
# Europe/Warsaw        | ++
# Pacific/Honolulu     | +
# """.splitlines()
#
#
# def test_output(capfd):
#     create_user_bar_chart(content)
#     actual_output = [line.strip().replace(' ', '') for line in
#                      capfd.readouterr()[0].splitlines()]
#
#     for line in expected_output:
#         assert line.strip().replace(' ', '') in actual_output, \
#                f'{line} not in {actual_output}'

# from wc import (tweets, filter_tweets_on_polarity,
#                            order_tweets_by_polarity)
#
#
# def test_filter_tweets_keep_positive():
#     actual = filter_tweets_on_polarity(tweets)
#     expected = tweets[1:4]
#     assert actual == expected
#
#
# def test_filter_tweets_keep_negative():
#     actual = filter_tweets_on_polarity(tweets, keep_positive=False)
#     expected = [tweets[0], tweets[-1]]
#     assert actual == expected
#
#
# def test_order_tweets_positive_highest():
#     actual = [tweet.polarity for tweet in order_tweets_by_polarity(tweets)]
#     expected = [1.0, 0.8, 0.125, -0.19999999999999998,
#                 -0.3333333333333333]
#     assert actual == expected
#
#
# def test_order_tweets_negative_highest():
#     actual = [tweet.polarity for tweet in
#               order_tweets_by_polarity(tweets, positive_highest=False)]
#     expected = [-0.3333333333333333, -0.19999999999999998,
#                 0.125, 0.8, 1.0]
#     assert actual == expected
#
# from wc import Score
#
#
# def test_enum_content():
#     assert list(Score) == [Score.BEGINNER, Score.INTERMEDIATE,
#                            Score.ADVANCED, Score.CHEATED]
#
#
# def test_equality_comparison():
#     assert Score.BEGINNER is Score.BEGINNER
#     assert Score.INTERMEDIATE is not Score.ADVANCED
#
#
# def test_str_using_thumbsup():
#     assert str(Score.BEGINNER) == 'BEGINNER => 👍👍'
#     assert str(Score.INTERMEDIATE) == 'INTERMEDIATE => 👍👍👍'
#     assert str(Score.ADVANCED) == 'ADVANCED => 👍👍👍👍'
#     assert str(Score.CHEATED) == 'CHEATED => 👍'
#
#
# def test_average():
#     assert Score.average() == 2.5
# from wc import flatten
#
#
# def test_flatten_various_levels():
#     inp = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
#     expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     assert list(flatten(inp)) == expected
#
#
# def test_flatten_various_levels_different_contant():
#     inp = [1, 2, [3, 4], [5, [6, 7]], [8, [9, [10]]],
#            [11, [12, 13], [14, [15, 16, [17, 18, [19, 20]]]]]]
#     expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
#                 14, 15, 16, 17, 18, 19, 20]
#     assert list(flatten(inp)) == expected
#
#
# def test_flatten_ints_and_chars():
#     inp = ['a', 'b', [1, 2, 3],
#            ['c', 'd', ['e', 'f', ['g', 'h']]],
#            [4, [5, 6, [7, [8]]]]]
#     expected = ['a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g',
#                 'h', 4, 5, 6, 7, 8]
#     assert list(flatten(inp)) == expected
#
#
# def test_works_with_tuple_as_well():
#     inp = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
#     expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     assert list(flatten(inp)) == expected
# import pytest
#
# from wc import rgb_to_hex
#
#
# @pytest.mark.parametrize("rgb, hex_", [
#     # https://www.rapidtables.com/web/color/RGB_Color.html
#     ((0, 0, 0), '#000000'),  # black
#     ((255, 255, 255), '#FFFFFF'),  # white
#     ((255, 0, 0), '#FF0000'),  # red
#     ((0, 255, 0), '#00FF00'),  # lime
#     ((0, 0, 255), '#0000FF'),  # blue
#     ((255, 255, 0), '#FFFF00'),  # yellow
#     ((0, 255, 255), '#00FFFF'),  # cyan / aqua
#     ((255, 0, 255), '#FF00FF'),  # magenta / fuchsia
#     ((192, 192, 192), '#C0C0C0'),  # silver
#     ((128, 128, 128), '#808080'),  # gray
#     ((128, 0, 0), '#800000'),  # maroon
#     ((128, 128, 0), '#808000'),  # olive
#     ((0, 128, 0), '#008000'),  # green
#     ((128, 0, 128), '#800080'),  # purple
#     ((0, 128, 128), '#008080'),  # teal
#     ((0, 0, 128), '#000080'),  # navy
# ])
# def test_rgb_to_hex(rgb, hex_):
#     assert rgb_to_hex(rgb) == hex_
#
#
# def test_wrong_values():
#     with pytest.raises(ValueError):
#         rgb_to_hex((-1, 100, 100))
#         rgb_to_hex((100, 300, 200))
#         rgb_to_hex((100, 200, 256))
#
# import pytest
#
# from wc import romanize
#
# @pytest.mark.parametrize("number, numeral", [
#     (1000, 'M'),
#     (500, 'D'),
#     (100, 'C'),
#     (50, 'L'),
#     (10, 'X'),
#     (5, 'V'),
#     (1, 'I'),
#     (177, 'CLXXVII'),
#     (244, 'CCXLIV'),
#     (87, 'LXXXVII'),  # Bite LXXXVII
#     (1033, 'MXXXIII'),
#     (997, 'CMXCVII'),
#     (3999, 'MMMCMXCIX'),
#     (13, 'XIII'),
#     (777, 'DCCLXXVII'),
#     (1652, 'MDCLII'),
#     (1981, 'MCMLXXXI'),
#     (2018, 'MMXVIII'),
#     (3500, 'MMMD'),
# ])
# def test_romanize(number, numeral):
#     assert romanize(number) == numeral
#
#
# def test_boundaries():
#     with pytest.raises(ValueError):
#         romanize('string')
#         romanize(-1)
#         romanize(0)
#         romanize(4000)
#         romanize(10000)
#
# from wc import (get_every_nth_state, get_state_abbrev,
#                     get_longest_state, combine_state_names_and_abbreviations,
#                     states, us_state_abbrev, NOT_FOUND)
#
#
# def test_get_every_nth_state():
#     expected = ['Massachusetts', 'Missouri', 'Hawaii',
#                 'Vermont', 'Delaware']
#     assert list(get_every_nth_state()) == expected
#     expected = ['Missouri', 'Vermont']
#     assert list(get_every_nth_state(n=20)) == expected
#
#
# def test_get_state_abbrev():
#     assert get_state_abbrev('Illinois') == 'IL'
#     assert get_state_abbrev('North Dakota') == 'ND'
#     assert get_state_abbrev('bogus') == NOT_FOUND
#
#
# def test_get_longest_state():
#     # depending the direction of the sort (reversed or not)
#     # both North and South Carolina are correct
#     possible_answers = ('North Carolina', 'South Carolina')
#     assert get_longest_state(us_state_abbrev) in possible_answers
#     assert get_longest_state(states) in possible_answers
#
#
# def test_combine_state_names_and_abbreviations():
#     expected = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
#                 'South Dakota', 'Tennessee', 'Texas', 'Utah',
#                 'Vermont', 'Virginia', 'Washington', 'West Virginia',
#                 'Wisconsin', 'Wyoming']
#     assert combine_state_names_and_abbreviations() == expected
#
# import pytest
#
# from wc import (get_season_csv_file,
#                        get_num_words_spoken_by_character_per_episode)
#
#
# @pytest.fixture(scope="module")
# def words_spoken_s1():
#     # module scope to not call requests for every test function
#     content = get_season_csv_file(season=1)
#     return get_num_words_spoken_by_character_per_episode(content)
#
#
# @pytest.fixture(scope="module")
# def words_spoken_s5():
#     content = get_season_csv_file(season=5)
#     return get_num_words_spoken_by_character_per_episode(content)
#
#
# def test_get_words_spoken_season1_stan(words_spoken_s1):
#     expected = [('4', 615), ('6', 572), ('5', 514)]
#     assert words_spoken_s1['Stan'].most_common()[:3] == expected
#
#
# def test_get_words_spoken_season1_cartman(words_spoken_s1):
#     expected = [('1', 735), ('10', 669), ('13', 621)]
#     alt_expected = [('1', 738), ('10', 669), ('13', 621)]
#     assert words_spoken_s1['Cartman'].most_common()[:3] in (expected,
#                                                             alt_expected)
#
#
# def test_get_words_spoken_season1_cartman_least_talkative(words_spoken_s1):
#     expected = [('11', 285), ('6', 264), ('4', 244)]
#     assert words_spoken_s1['Cartman'].most_common()[-3:] == expected
#
# def get_words_spoken_non_existing_character(words_spoken_s1):
#     assert words_spoken_s1['bogus'].most_common() == []
#
#
# # let's look at another season and other characters
#
# def test_get_words_spoken_season5_sheila(words_spoken_s5):
#     expected = [('11', 295), ('6', 212), ('7', 52)]
#     assert words_spoken_s5['Sheila'].most_common()[:3] == expected
#
#
# def test_get_words_spoken_season5_choksondik(words_spoken_s5):
#     expected = [('7', 749), ('10', 131), ('1', 129)]
#     alt_expected = [('7', 749), ('10', 130), ('1', 129)]  # no comma
#     assert words_spoken_s5['Ms. Choksondik'].most_common()[:3] in (
#         expected,
#         alt_expected)
#
# from datetime import timedelta
#
# import pytest
#
# from wc import pretty_date, NOW
#
#
# def n_days_ago_str(days):
#     return (NOW - timedelta(days=days)).strftime('%m/%d/%y')
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (NOW - timedelta(seconds=2), 'just now'),
#     (NOW - timedelta(seconds=9), 'just now'),
#     (NOW - timedelta(seconds=10), '10 seconds ago'),
#     (NOW - timedelta(seconds=59), '59 seconds ago'),
#     (NOW - timedelta(minutes=1), 'a minute ago'),
#     (NOW - timedelta(minutes=1, seconds=40), 'a minute ago'),
#     (NOW - timedelta(minutes=2), '2 minutes ago'),
#     (NOW - timedelta(minutes=59), '59 minutes ago'),
#     (NOW - timedelta(hours=1), 'an hour ago'),
#     (NOW - timedelta(hours=2), '2 hours ago'),
#     (NOW - timedelta(hours=23), '23 hours ago'),
#     (NOW - timedelta(hours=24), 'yesterday'),
#     (NOW - timedelta(hours=47), 'yesterday'),
#     (NOW - timedelta(days=1), 'yesterday'),
#     (NOW - timedelta(days=2), n_days_ago_str(2)),
#     (NOW - timedelta(days=7), n_days_ago_str(7)),
#     (NOW - timedelta(days=100), n_days_ago_str(100)),
#     (NOW - timedelta(days=365), n_days_ago_str(365)),
# ])
# def test_pretty_date(arg, expected):
#     assert pretty_date(arg) == expected
#
#
# def test_input_variable_of_wrong_type():
#     with pytest.raises(ValueError):
#         pretty_date(123)
#
#
# def test_input_variable_future_date():
#     with pytest.raises(ValueError):
#         pretty_date(NOW + timedelta(days=1))
#
# from datetime import date
#
# import pytest
#
# from wc import BirthdayDict, MSG
#
#
# @pytest.fixture(scope='module')
# def bd():
#     """This creates a bday dict that can be shared among the tests
#        (scope = module)"""
#     return BirthdayDict()
#
#
# def test_2_bdays_different_dates_not_print_msg(bd, capfd):
#     bd['bob'] = date(1987, 6, 15)
#     bd['tim'] = date(1984, 7, 15)
#     output = capfd.readouterr()[0].strip()
#     assert not output.strip()
#
#
# def test_another_bday_same_yymmdd_print_msg(bd, capfd):
#     bd['mary'] = date(1987, 6, 15)
#     output = capfd.readouterr()[0].strip()
#     assert output == MSG.format('mary')  # exactly the same as bob
#
#
# def test_another_bday_same_yymm_diff_day_not_print_msg(bd, capfd):
#     # not a bday match
#     bd['sara'] = date(1987, 6, 14)
#     output = capfd.readouterr()[0].strip()
#     assert not output.strip()
#
#
# def test_another_bday_same_mmdd_diff_year_print_msg(bd, capfd):
#     # if same day and month, but different year = match
#     bd['mike'] = date(1981, 7, 15)  # same as tim, except year
#     output = capfd.readouterr()[0].strip()
#     assert output == MSG.format('mike')
#
# import pytest
#
# from wc import get_us_bank_holidays
#
#
# holidays = get_us_bank_holidays()
#
#
# @pytest.mark.parametrize("month, holiday", [
#     ("01", ["New Year's Day", "Martin Luther King Jr. Day"]),
#     ("02", ["Presidents' Day"]),
#     ("04", ["Emancipation Day"]),
#     ("05", ["Mother's Day", "Memorial Day"]),
#     ("06", ["Father's Day"]),
#     ("07", ["Independence Day"]),
#     ("09", ["Labor Day"]),
#     ("10", ["Columbus Day"]),
#     ("11", ["Veterans Day", "Thanksgiving", "Day after Thanksgiving"]),
#     ("12", ["Christmas Day"]),
# ])
# def test_get_us_bank_holidays(month, holiday):
#     assert holidays.get(month) == holiday

# from itertools import islice
#
# import pytest
#
# from wc import sequence_generator
#
#
# @pytest.fixture
# def gen():
#     """Return a fresh new generator object for each test"""
#     return sequence_generator()
#
#
# def test_first_ten_first_round(gen):
#     expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
#     # generators == use islice, a regular slicing on a list object == hang
#     # because it tries to load in an infinite iterator = not good.
#     # don't believe me? change the line below to: `actual = list(gen)[:10]`
#     actual = list(islice(gen, 10))
#     assert expected == actual
#
#
# def test_first_ten_second_round(gen):
#     expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
#     actual = list(islice(gen, 52, 62))  # zero-based
#     assert expected == actual
#
#
# def test_last_ten_third_round(gen):
#     expected = [22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z']
#     actual = list(islice(gen, 146, 156))
#     assert expected == actual
#
# import json
# from unittest.mock import patch, Mock
#
# import requests
#
# from wc import get_ip_country
#
#
# @patch.object(requests, 'get')
# def test_ipinfo_mexican_ip(mockget):
#     # hardcoding a requests response
#     content = (b'{\n  "ip": "187.190.38.36",\n  "hostname": "domain.net",\n'
#                b'  "city": "Mexico City",\n  "region": "Mexico City",\n  '
#                b'"country": "MX",\n ' b'"loc": "11.0000,-00.1111",\n  '
#                b'"postal": "12345",\n  "org": "some org"\n}')
#     mockget.return_value = Mock(content=content,
#                                 text=content.decode("utf-8"),
#                                 json=lambda: json.loads(content),
#                                 status_code=200)
#     assert get_ip_country('187.190.38.36') == 'MX'
#
#
# @patch.object(requests, 'get')
# def test_ipinfo_japan_ip(mockget):
#     # and another IP in Japan
#     content = (b'{\n  "ip": "185.161.200.10",\n  "city": "Tokyo",\n  '
#                b'"region": "Tokyo",\n ' b'"country": "JP",\n  "loc": '
#                b'"00.1111,11.0000",\n  "postal": "123-4567",\n  '
#                b'"org": "some other org"\n}')
#     mockget.return_value = Mock(content=content,
#                                 text=content.decode("utf-8"),
#                                 json=lambda: json.loads(content),
#                                 status_code=200)
#     assert get_ip_country('185.161.200.10') == 'JP'
#
# import pytest
#
# from wc import extract_non_ascii_words
#
#
# @pytest.mark.parametrize("phrase, expected", [
#     ('An preost wes on leoden, Laȝamon was ihoten', ['Laȝamon']),
#     ('He wes Leovenaðes sone -- liðe him be Drihten', ['Leovenaðes', 'liðe']),
#     ('He wonede at Ernleȝe at æðelen are chirechen', ['Ernleȝe', 'æðelen']),
#     ('Uppen Sevarne staþe sel þar him þuhte', ['staþe', 'þar', 'þuhte']),
#     ('Onfest Radestone, þer he bock radde', ['þer']),
#     ('Fichier non trouvé', ['trouvé']),
#     ('Over \u0e55\u0e57 57 flavours', ['๕๗']),
#     ('Sí ... habrá que saber algo de Unicode', ['Sí', 'habrá']),
#     ('This string only contains ascii words', []),
# ])
# def test_extract_non_ascii_words(phrase, expected):
#     assert extract_non_ascii_words(phrase) == expected
#
# import pytest
#
# from wc import Color
#
#
# @pytest.mark.parametrize("color, expected", [
#     ("white", (255, 255, 255)),
#     ("black", (0, 0, 0)),
#     ("blue", (0, 0, 255)),
#     ("red", (255, 0, 0)),
#     ("green", (0, 128, 0)),
#     ("orange", (255, 128, 0)),
#     ("puke", None),
# ])
# def test_color_class(color, expected):
#     c = Color(color)
#     assert c.rgb == expected
#
#
# @pytest.mark.parametrize("rgb, expected", [
#     ((255, 255, 255), "#ffffff"),
#     ((0, 0, 0), "#000000"),
#     ((0, 0, 255), "#0000ff"),
#     ((255, 0, 0), "#ff0000"),
#     ((0, 128, 0), "#008000"),
#     ((255, 128, 0), "#ff8000"),
# ])
# def test_color_staticmethod_rgb2hex(rgb, expected):
#     assert Color.rgb2hex(rgb) == expected
#
#
# @pytest.mark.parametrize("rgb", [
#     ("puke"),
#     ("0, 0, 0"),
#     ((0, -5, 255)),
#     ((256, 0, 0)),
# ])
#
# def test_color_rgb2hex_bad_value(rgb):
#     with pytest.raises(ValueError):
#         Color.rgb2hex(rgb)
#
#
# @pytest.mark.parametrize("hex, expected", [
#     ("#ffffff", (255, 255, 255)),
#     ("#000000", (0, 0, 0)),
#     ("#0000ff", (0, 0, 255)),
#     ("#ff0000", (255, 0, 0)),
#     ("#008000", (0, 128, 0)),
#     ("#ff8000", (255, 128, 0)),
# ])
# def test_color_staticmethod_hex2rgb(hex, expected):
#     assert Color.hex2rgb(hex) == expected
#
#
# @pytest.mark.parametrize("value", [
#     ("puke"),
#     ("#ccc"),
#     ("#stopit"),
#     ("pink"),
# ])
# def test_color_hex2rgb_bad_value(value):
#     with pytest.raises(ValueError):
#         Color.hex2rgb(value)
#
#
# def test_color_string_output():
#     color = Color("brown")
#     assert str(color) == "(165, 42, 42)"
#
#
# def test_color_repr_output():
#     color = Color("brown")
#     assert repr(color) == "Color('brown')"
#
#
# def test_unknown_color():
#     color = Color("puke green")
#     assert str(color) == "Unknown"

#
# import os
# from pathlib import Path
# from tempfile import TemporaryDirectory
#
# import pytest
#
# from wc import get_files
#
# TMP = Path(os.getenv("TMP", "/tmp"))
#
#
# @pytest.mark.parametrize("byte_sizes, size_in_kb, expected", [
#     ([800, 1000, 1200], 1, ['1200']),
#     ([1024, 1025], 1, ['1024', '1025']),
#     ([1024, 1025], 1.026, []),
#     ([1000, 1300, 1777, 900], 1.25, ['1300', '1777']),
#     ([1024, 2047, 2048, 2500], 2, ['2048', '2500']),
# ])
# def test_get_files(byte_sizes, size_in_kb, expected):
#     with TemporaryDirectory(dir=TMP) as dirname:
#         for size in byte_sizes:
#             with open(os.path.join(dirname, str(size)), 'wb') as f:
#                 f.write(os.urandom(size))
#
#         actual = [os.path.basename(fi) for fi in
#                   get_files(dirname, size_in_kb)]
#         assert sorted(actual) == sorted(expected)
#
# import pytest
#
# from wc import strip_range
#
#
# TEXTS = ['Hello world', 'Welcome to PyBites',
#          'Decorators for fun and profit',
#          'Hello world Hello']
#
#
# @pytest.mark.parametrize("start, end, arg, expected", [
#     (3, 5, TEXTS[0], 'Hel.. world'),
#     (4, 8, TEXTS[0], 'Hell....rld'),
#     (0, 3, TEXTS[1], '...come to PyBites'),
#     (-1, 3, TEXTS[1], '...come to PyBites'),
#     (0, -1, TEXTS[1], 'Welcome to PyBites'),
#     (5, 10, TEXTS[2], 'Decor..... for fun and profit'),
#     (100, 110, TEXTS[2], 'Decorators for fun and profit'),
#     (20, 100, TEXTS[2], 'Decorators for fun a.........'),
#     (3, 5, TEXTS[3], 'Hel.. world Hello'),
# ])
# def test_strip_range(start, end, arg, expected):
#     @strip_range(start, end)
#     def gen_output(text):
#         return text
#     actual = gen_output(text=arg)
#     assert actual == expected
#
# from wc import get_duplicate_indices
#
#
# def test_get_duplicate_indices_docstring():
#     words = ['is', 'it', 'true', 'or', 'is', 'it', 'not']
#     assert get_duplicate_indices(words) == [0, 1]
#
#
# def test_get_duplicate_indices_bite_text():
#     words = ['this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this',
#              'bite', 'will', 'teach', 'you', 'something', 'new']
#     assert get_duplicate_indices(words) == [0, 3, 4]
#
#
# def test_get_duplicate_indices_another_text():
#     # keeping it simple with split on space, so lists != lists.
#     words = ('List comprehensions provide a concise way to create '
#              'lists. Common applications are to make new lists where '
#              'each element is the result of some operations applied '
#              'to each member of another sequence or iterable, or to '
#              'create a subsequence of those elements that satisfy a '
#              'certain condition').split()
#     assert get_duplicate_indices(words) == [3, 6, 7, 17, 22, 32]
#
# from wc import generate_xmas_tree
#
# default_tree = """
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
# """
# smaller_tree = """
#   *
#  ***
# *****
# """
#
#
# def test_height_xmas_tree():
#     assert len(generate_xmas_tree().split('\n')) == 10  # default arg
#     assert len(generate_xmas_tree(5).split('\n')) == 5
#     assert len(generate_xmas_tree(20).split('\n')) == 20
#
#
# def test_num_stars_used():
#     assert generate_xmas_tree(3).count('*') == 9
#     assert generate_xmas_tree(5).count('*') == 25
#     assert generate_xmas_tree(20).count('*') == 400
#
#
# def test_outputs():
#     actual_tree = generate_xmas_tree().strip('\n').split('\n')
#     expected_tree = default_tree.strip('\n').split('\n')
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()
#
#     actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
#     expected_tree = smaller_tree.strip('\n').split('\n')
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()
# from wc import Vehicle, Car, Motorbike
#
#
# def test_vehicle_description():
#     v = Vehicle("Generic", "ModelX", 4)
#     assert v.description() == "Generic ModelX with 4 wheels"
#
#
# def test_car_inherits_vehicle():
#     c = Car("Toyota", "Corolla", 4, 4)
#     assert c.brand == "Toyota"
#     assert c.model == "Corolla"
#     assert c.wheels == 4
#     assert c.doors == 4
#     assert c.honk() == "Beep beep!"
#     assert c.description() == "Toyota Corolla with 4 wheels"
#
#
# def test_motorbike_inherits_vehicle():
#     m = Motorbike("Yamaha", "R3", 2, 321)
#     assert m.brand == "Yamaha"
#     assert m.model == "R3"
#     assert m.wheels == 2
#     assert m.engine_cc == 321
#     assert m.rev_engine() == "Yamaha R3 with 2 wheels goes Vroom vroom!"
#     assert m.description() == "Yamaha R3 with 2 wheels`"
#
# import pytest
#
# from wc import is_anagram
#
#
# @pytest.mark.parametrize("word1, word2", [
#     ("rail safety", "fairy tales"),
#     ("roast beef", "eat for BSE"),
#     # An anagram which means the opposite of its subject is
#     # called an "antigram". For example:
#     ("restful", "fluster"),
#     ("funeral", "real fun"),
#     ("adultery", "true lady"),
#     ("customers", "store scum"),
#     ("forty five", "over fifty"),
#     # They can sometimes change from a proper noun or personal
#     # name into an appropriate sentence:
#     ("William Shakespeare", "I am a weakish speller"),
#     ("Madam Curie", "Radium came"),
# ])
# def test_is_anagram(word1, word2):
#     assert is_anagram(word1, word2)
#
#
# @pytest.mark.parametrize("word1, word2", [
#     ("rail safety", "fairy fun"),
#     ("roast beef", "eat for ME"),
#     ("restful", "fluester"),
#     ("funeral", "real funny"),
#     ("adultery", "true ladie"),
#     ("customers", "store scam"),
#     ("forty five", "over fifty1"),
#     ("William Shakespeare", "I am a strong speller"),
#     ("Madam Curie", "Radium come"),
# ])
# def test_is_not_anagram(word1, word2):
#     assert not is_anagram(word1, word2)
#
# from wc import get_friend_with_most_friends, friendships
#
# def test_default_friendships_list():
#     user, friends = get_friend_with_most_friends(friendships)
#     assert user == 'sara'
#     assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']
#
#
# def test_different_friendships_list():
#     friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
#                    (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
#                    (6, 7), (6, 8), (6, 9)]
#     user, friends = get_friend_with_most_friends(friendships)
#     assert user == 'joyce'
#     assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
#                                      'rod', 'sara']
#
#
# def test_friendships_list_with_duplicate_names():
#     names = 'bob bob tim tim julian julian'.split()
#     ids = range(len(names))
#     users = dict(zip(ids, names))
#
#     friendships = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3),
#                    (2, 4), (4, 5)]
#     user, friends = get_friend_with_most_friends(friendships, users=users)
#     assert user == 'bob'
#     assert sorted(list(friends)) == ['bob', 'julian', 'julian', 'tim']


#
# import pytest
#
# from wc import get_top_books, load_page
#
#
# @pytest.fixture(scope='module')
# def content():
#     """Load content once for all test"""
#     return load_page()
#
#
# def test_return(content):
#     books = get_top_books(content=content)
#     assert len(books) == 16
#     assert type(books) == list
#     assert all(type(book) == tuple for book in books)
#
#
# @pytest.mark.parametrize("title, count", [
#   ('Man’s Search For Meaning', 6),
#   ('Tao Te Ching', 5),
#   (('The 4-Hour Workweek: Escape the 9-5, '
#     'Live Anywhere and Join the New Rich'), 4),
#   ('The Fountainhead', 4),
#   ('Sapiens: A Brief History of Humankind', 4),
#   ('The Better Angels of our Nature: Why Violence Has Declined', 3),
#   ('The Beginning of Infinity: Explanations That Transform the World', 3),
#   (('The War of Art: Break Through the Blocks and Win Your '
#     'Inner Creative Battles'), 3),
#   ('The Hero with a Thousand Faces', 3),
#   ('Poor Charlie’s Almanack', 3),
#   ('The Chronicles of Narnia', 3),
#   ('The Selfish Gene', 3),
#   ('Tools of Titans', 3),
#   ('Song of Solomon', 3),
#   ('The Alchemist', 3),
# ])
# def test_counts(content, title, count):
#     books = get_top_books(content=content)
#     assert (title, count) in books
#
# import pytest
#
# from wc import get_ordinal_suffix
#
#
# @pytest.mark.parametrize("input_argument, expected_return", [
#     (0, '0th'),
#     (1, '1st'),
#     (2, '2nd'),
#     (3, '3rd'),
#     (4, '4th'),
#     (9, '9th'),
#     (10, '10th'),
#     (11, '11th'),
#     (12, '12th'),
#     (13, '13th'),
#     (20, '20th'),
#     (21, '21st'),
#     (22, '22nd'),
#     (23, '23rd'),
#     (24, '24th'),
#     (25, '25th'),
#     (30, '30th'),
#     (50, '50th'),
#     (51, '51st'),
#     (52, '52nd'),
#     (53, '53rd'),
#     (54, '54th'),
#     (55, '55th'),
#     (99, '99th'),
#     (100, '100th'),
#     (101, '101st'),
#     (102, '102nd'),
#     (103, '103rd'),
#     (104, '104th'),
#     (110, '110th'),
#     (111, '111th'),
#     (1001, '1001st'),
#     (1003, '1003rd'),
#     (1111, '1111th'),
# ])
# def test_ordinal(input_argument, expected_return):
#     assert get_ordinal_suffix(input_argument) == expected_return
# from datetime import datetime
# from itertools import compress
# import inspect
# import re
#


#
# import pytest
#
# from wc import count_down
#
# DEFAULT_EXPECTED_OUTPUT = '1234\n123\n12\n1\n'
#
#
# def test_code_uses_singledispatch_decorator():
#     assert '@singledispatch' in inspect.getsource(count_down)
#
#
# @pytest.mark.parametrize("input_argument", [
#     '1234',
#     1234,
#     [1, 2, 3, 4],
#     ['1', '2', '3', '4'],
#     (1, 2, 3, 4),
#     ('1', '2', '3', '4'),
#     {1: 'one', 2: 'two', 3: 'three', 4: 'four'},
#     {'1': 'one', '2': 'two', '3': 'three', '4': 'four'},
#     range(1, 5),
#     {x for x in range(1, 5)},
# ])
# def test_count_down_good_inputs(input_argument, capfd):
#     count_down(input_argument)
#     output = capfd.readouterr()[0]
#     assert output == DEFAULT_EXPECTED_OUTPUT
#
#
# @pytest.mark.parametrize("input_argument", [
#     compress([1, 2, 3, 4], [1, 1, 1, 1]),
#     datetime(2018, 4, 21),
#     re.compile(r'\d{4}'),
# ])
# def test_count_down_bad_inputs(input_argument, capfd):
#     with pytest.raises(ValueError):
#         count_down(input_argument)
#
#
# def test_count_down_float(capfd):
#     expected = '12.34\n12.3\n12.\n12\n1\n'
#     number = 12.34
#     count_down(number)
#     output = capfd.readouterr()[0]
#     assert output == expected



# from wc import (_cap_str_to_mln_float,
#                     get_stock_symbol_with_highest_cap,
#                     get_industry_cap,
#                     get_sectors_with_max_and_min_stocks)
#
#
# def test_cap_str_to_mln_float():
#     assert _cap_str_to_mln_float('n/a') == 0
#     assert _cap_str_to_mln_float('$100.45M') == 100.45
#     assert _cap_str_to_mln_float('$20.9B') == 20900
#
#
# def test_get_stock_symbol_with_highest_cap():
#     assert get_stock_symbol_with_highest_cap() == 'JNJ'
#
#
# def test_get_industry_cap():
#     assert get_industry_cap("Business Services") == 368853.27
#     assert get_industry_cap("Real Estate Investment Trusts") == 243295.36
#
#
# def test_get_sectors_with_max_and_min_stocks():
#     assert get_sectors_with_max_and_min_stocks() == ('Finance',
#                                                      'Transportation')

#
# import pytest
#
# from wc import get_word_max_vowels
#
# paragraphs = [
#     ("Python is an easy to learn, powerful programming language."
#      "It has efficient high-level data structures and a simple "
#      "but effective approach to object-oriented programming. "
#      "Python’s elegant syntax and dynamic typing, together with "
#      "its interpreted nature, make it an ideal language for "
#      "scripting and rapid application development in many areas "
#      "on most platforms."),
#     ("The Python interpreter and the extensive standard library "
#      "are freely available in source or binary form for all major "
#      "platforms from the Python Web site, https://www.python.org/, "
#      "and may be freely distributed. The same site also contains "
#      "distributions of and pointers to many free third party Python "
#      "modules, programs and tools, and additional documentation."),
#     ("The Python interpreter is easily extended with new functions "
#      "and data types implemented in C or C++ (or other languages "
#      "callable from C). Python is also suitable as an extension "
#      "language for customizable applications."),
#     ("This tutorial introduces the reader informally to the basic "
#      "concepts and features of the Python language and system. "
#      "It helps to have a Python interpreter handy for hands-on "
#      "experience, but all examples are self-contained, so the "
#      "tutorial can be read off-line as well."),
#     ("For a description of standard objects and modules, see The "
#      "Python Standard Library. The Python Language Reference gives "
#      "a more formal definition of the language. To write extensions "
#      "in C or C++, read Extending and Embedding the Python "
#      "Interpreter and Python/C API Reference Manual. There are "
#      "also several books covering Python in depth."),
#     ("This tutorial does not attempt to be comprehensive and cover "
#      "every single feature, or even every commonly used feature. "
#      "Instead, it introduces many of Python’s most noteworthy "
#      "features, and will give you a good idea of the language’s "
#      "flavor and style. After reading it, you will be able to read and "
#      "write Python modules and programs, and you will be ready to "
#      "learn more about the various Python library modules described "
#      "in The Python Standard Library."),
#     ("This tutorial does not attempt to be COMPREHENSIVE and cover "
#      "every single feature, or even every commonly used feature. "
#      "Instead, it introduces many of Python’s most noteworthy "
#      "features, and will give you a good idea of the language’s "
#      "flavor and style. After reading it, you will be able to read and "
#      "write Python modules and programs, and you will be ready to "
#      "learn more about the various Python library modules described "
#      "in The Python Standard Library."),
# ]
# expected = [
#     [('object-oriented', 6)],  # only one word with 6 vowels
#     [('documentation.', 6)],  # ditto
#     [('customizable', 5), ('applications.', 5)],  # here we have two options
#     [('self-contained,', 5), ('experience,', 5)],  # ditto
#     [('definition', 5)],  # only one word with 5 vowels
#     [('comprehensive', 5)],  # ditto
#     [('comprehensive', 5)],  # test upper / lower case
# ]
#
#
# @pytest.mark.parametrize('text, result', zip(paragraphs, expected))
# def test_get_word_max_vowels(text, result):
#     assert get_word_max_vowels(text) in result
#
# from wc import (sort_books_by_len_of_title,
#                    sort_books_by_first_authors_last_name,
#                    sort_books_by_number_of_page,
#                    sort_books_by_published_date)
#
#
# def test_sort_books_by_len_of_title():
#     last_book = sort_books_by_len_of_title()[-1]
#     assert last_book.title == 'Automate the Boring Stuff with Python'
#
#
# def test_sort_books_by_first_authors_last_name():
#     last_book = sort_books_by_first_authors_last_name()[-1]
#     assert last_book.title == 'Automate the Boring Stuff with Python'
#
#
# def test_sort_books_by_number_of_page():
#     last_book = sort_books_by_number_of_page()[-1]
#     assert last_book.title == 'Fluent Python'
#
#
# def test_sort_books_by_published_date():
#     last_book = sort_books_by_published_date()[-1]
#     assert last_book.title == 'Python Interviews'
#
# import pytest
# from wc import best_match_per_wine, match_wine_5cheeses
#
#
# def test_best_match_per_wine_all():
#     assert best_match_per_wine()[2] == 13.0
#
#
# cases_best_by_wine = [
#     ("white", "Sauvignon blanc", "Smoked Austrian", 8.0),
#     ("red", "Cabernet sauvignon", "Dorset Blue Vinney", 13.0),
#     ("sparkling", "Moscato d’Asti", "Carré de l'Est", 6.0),
# ]
#
#
# @pytest.mark.parametrize("case", cases_best_by_wine)
# def test_best_match_per_wine_type(case):
#     wine_type, *result = case
#     assert best_match_per_wine(wine_type) == tuple(result)
#
#
# def test_invalid_wine_type():
#     with pytest.raises(ValueError):
#         best_match_per_wine("cocacola")
#
#
# def test_all_wines_included():
#     assert len(match_wine_5cheeses()) == 26
#
#
# mw5c = match_wine_5cheeses()
# cases = [
#     (0, "Barbera", ["Cheddar", "Gruyère", "Boursin", "Parmesan", "Liptauer"]),
#     (1, "Barolo", ["Boursin", "Cheddar", "Gouda", "Stilton", "Tilsit"]),
#     (
#         2,
#         "Cabernet sauvignon",
#         [
#             "Dorset Blue Vinney",
#             "Norwegian Jarlsberg",
#             "Czech sheep's milk",
#             "Double Gloucester",
#             "Japanese Sage Derby",
#         ],
#     ),
#     (3, "Cava", ["Edam", "Gouda", "Cheddar", "Savoyard", "Parmesan"]),
#     (
#         4,
#         "Champagne",
#         ["Caithness", "Camembert", "Bel Paese", "Ilchester", "Lancashire"],
#     ),
#     (-2, "Syrah", ["Gouda", "Cheddar", "Brie", "Edam", "Tilsit"]),
#     (
#         -1,
#         "Zinfandel",
#         ["Caithness", "Bel Paese", "Ilchester", "Limburger", "Lancashire"],
#     ),
# ]
#
#
# @pytest.mark.parametrize("case", cases)
# def test_match_wine_5cheeses(case):
#     """ test of presence of first 2 cheeses only
#     because if score is same for more pairs, order of pairs cannot be assumed
#     """
#     idx, wine, cheeses = case
#     assert mw5c[idx][0] == wine
#     assert mw5c[idx][1] == cheeses
#
# from wc import Animal
#
#
# def test_zoo_5_animals():
#     for animal in 'dog cat fish lion mouse'.split():
#         Animal(animal)
#     zoo = Animal.zoo()
#     expected = ("10001. Dog",
#                 "10002. Cat",
#                 "10003. Fish",
#                 "10004. Lion",
#                 "10005. Mouse")
#     assert zoo == '\n'.join(expected)
#
#
# def test_animal_instance_str():
#     horse = Animal('horse')
#     assert str(horse) == "10006. Horse"
#     monkey = Animal('monkey')
#     assert str(monkey) == "10007. Monkey"
#
# from wc import data, athletes_most_medals
#
# def test_athletes_most_medals_default_csv():
#     ret = athletes_most_medals()
#     assert len(ret) == 2
#     assert ret["LATYNINA, Larisa"] == 18
#     assert ret["PHELPS, Michael"] == 22
#
#
# def test_smaller_csv_and_guarantee_checking_male_and_female():
#     ret = athletes_most_medals(
#         data.replace('summer', 'summer_2008-2012')
#     )
#     assert len(ret) == 2
#     assert ret["PHELPS, Michael"] == 14
#     assert ret["COUGHLIN, Natalie"] == 7  # not LOCHTE, Ryan
#
#
# import pytest
# from wc import get_dates, InfDateFmtError
#
#
# def test_tie():
#     """ any date string can be parsed using the following formats:
#     dd/mm/yy , mm/dd/yy, yy/mm/dd
#     so no the prevalent format cannot be inferred """
#     dates = [
#         "11/11/07",
#         "01/05/07",
#         "05/12/04",
#         "06/11/01",
#         "10/03/09",
#         "10/08/09",
#         "04/11/11",
#         "02/05/10",
#         "05/10/08",
#         "12/03/01",
#         "10/10/12",
#         "03/10/02",
#     ]
#     with pytest.raises(InfDateFmtError):
#         get_dates(dates)
#
#
# def test_too_many_nonparsable():
#     """{<DateFormat.MMDDYY: 1>: 2,  <DateFormat.NONPARSABLE: -999>: 5,
#          <DateFormat.DDMMYY: 0>: 2, <DateFormat.YYMMDD: 2>: 3}
#     """
#     dates = [
#         "12/22/68",
#         "31/09/87",
#         "37/13/29",
#         "41/28/13",
#         "13/03/32",
#         "18/08/74",
#         "46/09/27",
#         "49/07/10",
#         "05/31/88",
#         "28/13/17",
#         "71/14/19",
#         "85/08/09",
#     ]
#     with pytest.raises(InfDateFmtError):
#         get_dates(dates)
#
#
# def test_mmddyy():
#     """ {<DateFormat.MMDDYY: 1>: 7, <DateFormat.DDMMYY: 0>: 5,
#          <DateFormat.YYMMDD: 2>: 5, <DateFormat.NONPARSABLE: -999>: 2}
#         the single most prevalent format is mm/dd/yy
#     """
#     dates = [
#         "04/25/79",
#         "08/09/70",
#         "08/04/10",
#         "95/31/10",
#         "06/13/34",
#         "04/03/22",
#         "67/12/17",
#         "34/10/12",
#         "04/05/94",
#         "07/12/41",
#         "88/11/05",
#         "96/26/08",
#     ]
#     results = [
#         "1979-04-25",
#         "1970-08-09",
#         "2010-08-04",
#         "Invalid",
#         "2034-06-13",
#         "2022-04-03",
#         "Invalid",
#         "Invalid",
#         "1994-04-05",
#         "2041-07-12",
#         "Invalid",
#         "Invalid",
#     ]
#     assert get_dates(dates) == results
#
#
# def test_yymmdd():
#     """ {<DateFormat.YYMMDD: 2>: 7, <DateFormat.NONPARSABLE: -999>: 1,
#          <DateFormat.MMDDYY: 1>: 3, <DateFormat.DDMMYY: 0>: 3}
#          the single most prevalent format is yy/mm/dd """
#     dates = [
#         "68/12/22",
#         "31/09/87",
#         "37/03/29",
#         "11/28/03",
#         "02/03/32",
#         "18/08/74",
#         "46/09/27",
#         "49/07/10",
#         "05/31/88",
#         "28/12/17",
#         "71/04/19",
#         "85/08/09",
#     ]
#     results = [
#         "2068-12-22",
#         "Invalid",
#         "2037-03-29",
#         "Invalid",
#         "Invalid",
#         "Invalid",
#         "2046-09-27",
#         "2049-07-10",
#         "Invalid",
#         "2028-12-17",
#         "1971-04-19",
#         "1985-08-09",
#     ]
#     assert get_dates(dates) == results
#
#
# def test_ddmmyy():
#     """ {<DateFormat.MMDDYY: 1>: 7, <DateFormat.DDMMYY: 0>: 9,
#         <DateFormat.YYMMDD: 2>: 4}
#         the single most prevalent format is dd/mm/yy """
#     dates = [
#         "12/16/30",
#         "16/03/54",
#         "97/07/26",
#         "04/04/31",
#         "01/08/07",
#         "02/02/29",
#         "73/03/08",
#         "06/07/55",
#         "10/09/77",
#         "18/03/43",
#         "30/11/24",
#         "08/01/51",
#     ]
#     results = [
#         "Invalid",
#         "2054-03-16",
#         "Invalid",
#         "2031-04-04",
#         "2007-08-01",
#         "2029-02-02",
#         "Invalid",
#         "2055-07-06",
#         "1977-09-10",
#         "2043-03-18",
#         "2024-11-30",
#         "2051-01-08",
#     ]
#     assert get_dates(dates) == results
#
#
# def test_different_enum():
#     """ Modified enum - now it supports 4 different time formats.
#         Order of formats is changed as well"""
#     from enum import Enum
#     # import the module with the tested code which contains the original emum
#     import primitive_date_inferrer as pdi
#
#     class DateFormat_ext(Enum):
#         DDMMYYYY = 0
#         DDMMYY = 1
#         YYMMDD = 2
#         MMDDYY = 3
#         NONPARSABLE = -999
#
#         @classmethod
#         def get_d_parse_formats(cls, idx=None):
#             d_parse_formats = ["%d.%m.%Y", "%d/%m/%y", "%y/%m/%d", "%m/%d/%y"]
#             if idx is None:
#                 return d_parse_formats
#             if 0 <= idx <= len(d_parse_formats):
#                 return d_parse_formats[idx]
#             raise ValueError
#
#     # override the enum in the tested code module
#     pdi.DateFormat = DateFormat_ext
#
#     dates = [
#         "12/16/30",
#         "16.03.1954",
#         "97/07/26",
#         "04.04.1931",
#         "01.08.1907",
#         "02/02/29",
#         "73/03/08",
#         "06.07.1955",
#         "10.09.1977",
#         "18.03.1943",
#         "30/11/24",
#         "08.01.1951",
#     ]
#     results = [
#         "Invalid",
#         "1954-03-16",
#         "Invalid",
#         "1931-04-04",
#         "1907-08-01",
#         "Invalid",
#         "Invalid",
#         "1955-07-06",
#         "1977-09-10",
#         "1943-03-18",
#         "Invalid",
#         "1951-01-08",
#     ]
#     assert get_dates(dates) == results
# import pytest
#
# from wc import Player, calculate_score, get_winner
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ([1, 3, 2, 5], 5),
#     ([1, 4, 2, 5], 9),
#     ([1, 1, 1, 1], 0),
#     ([4, 5, 1, 2], 9),
#     ([6, 6, 5, 5], 22),
# ])
# def test_calculate_score(arg, expected):
#     assert calculate_score(arg) == expected
#
#
# @pytest.mark.parametrize("arg", [
#     [4, 5, 6, 'a'],
#     [4, -5, -1, 2],
#     [4, 7, 6, 2],
# ])
# def test_wrong_inputs(arg):
#     with pytest.raises(ValueError):
#         calculate_score(arg)
#
#
# def test_winner_3_players():
#     players = [
#       Player(name='player 1', scores=[1, 3, 2, 5]),
#       Player(name='player 2', scores=[1, 1, 1, 1]),
#       Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
#     ]
#     assert get_winner(players) == players[-1]
#
#
# def test_winner_shorter_score_len_raises_exception():
#     players = [
#       Player(name='player 1', scores=[4, 3, 5, 5]),
#       Player(name='player 2', scores=[4, 4, 6]),  # lacks one score
#       Player(name='player 3', scores=[4, 5, 6, 6]),
#     ]
#     with pytest.raises(ValueError):
#         get_winner(players)
#
#
# def test_winner_longer_score_len_raises_exception():
#     players = [
#       Player(name='player 1', scores=[4, 3, 5, 5, 4]),
#       Player(name='player 2', scores=[4, 4, 6, 6, 3, 2]),  # 1 more
#       Player(name='player 3', scores=[4, 5, 6, 6, 5]),
#     ]
#     with pytest.raises(ValueError):
#         get_winner(players)
# import pytest
#
# from wc import calc_months_passed
#
#
# def test_same_date():
#     assert calc_months_passed(2018, 11, 1) == 0
#
#
# def test_nine_days_later():
#     assert calc_months_passed(2018, 11, 10) == 0
#
#
# def test_ten_days_later():
#     assert calc_months_passed(2018, 11, 11) == 1
#
#
# def test_one_month_and_nine_days_later():
#     assert calc_months_passed(2018, 12, 10) == 1
#
#
# def test_one_month_and_ten_day_later():
#     assert calc_months_passed(2018, 12, 11) == 2
#
#
# def test_one_year_one_month_and_nine_days_later():
#     assert calc_months_passed(2019, 12, 10) == 13
#
#
# def test_one_year_one_month_and_ten_days_later():
#     assert calc_months_passed(2019, 12, 11) == 14
#
#
# def test_non_int_input_args():
#     with pytest.raises(TypeError):
#         calc_months_passed('a', 10, 1)
#     with pytest.raises(TypeError):
#         calc_months_passed(2018, 'b', 1)
#     with pytest.raises(TypeError):
#         calc_months_passed(2018, 10, 'c')
#
#
# def test_out_of_dt_range_args():
#     with pytest.raises(ValueError):
#         calc_months_passed(-1000, 11, 1)
#     with pytest.raises(ValueError):
#         calc_months_passed(2018, 13, 1)
#     with pytest.raises(ValueError):
#         calc_months_passed(2018, 11, 34)
#
#
# def test_new_date_in_past_raises_value_error():
#     with pytest.raises(ValueError):
#         calc_months_passed(2018, 10, 1)
#
# from wc import gen_rhombus
#
#
# def test_rhombus_width3():
#     # recommended: actual before expected
#     # https://twitter.com/brianokken/status/1063337328553295876
#     actual = list(gen_rhombus(3))
#     expected = [' * ', '***', ' * ']
#     assert actual == expected
#
#
# def test_rhombus_width5():
#     actual = list(gen_rhombus(5))
#     expected = ['  *  ', ' *** ', '*****',
#                 ' *** ', '  *  ']
#     assert actual == expected
#
#
# def test_rhombus_width11():
#     """print('\n'.join(expected)) would give (ignore indents):
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *
#     """
#     actual = list(gen_rhombus(11))
#     expected = ['     *     ', '    ***    ', '   *****   ',
#                 '  *******  ', ' ********* ', '***********', ' ********* ',
#                 '  *******  ', '   *****   ', '    ***    ', '     *     ']
#     assert actual == expected
#
# from datetime import date, timedelta

#
# from wc import get_hundred_weekdays, TODAY
#
# OTHER_START_DATE = TODAY + timedelta(days=55)
#
#
# def test_get_hundred_weekdays_default_start_date():
#     days = get_hundred_weekdays(start_date=TODAY)
#     assert len(days) == 100
#     # check start and end dates
#     assert days[0] == TODAY
#     assert days[-1] == date(2019, 4, 17)
#     # check if weekends are not included
#     assert days[1] == date(2018, 11, 30)
#     assert days[2] == date(2018, 12, 3)
#     fri_index = days.index(date(2019, 1, 18))
#     assert days[fri_index + 1] == date(2019, 1, 21)
#
#
# def test_get_hundred_weekdays_different_start_date():
#     days = get_hundred_weekdays(start_date=OTHER_START_DATE)
#     assert len(days) == 100
#     # check start and end dates
#     assert days[0] == OTHER_START_DATE
#     assert days[-1] == date(2019, 6, 11)
#     # check if weekends are not included
#     assert days[2] == date(2019, 1, 25)
#     assert days[3] == date(2019, 1, 28)
#     fri_index = days.index(date(2019, 6, 7))
#     assert days[fri_index + 1] == date(2019, 6, 10)

#
# from wc import cars, group_cars_by_manufacturer
#
# expected_output = """
# CHEVROLET
# - Cavalier
# - Corvette
# - Impala
#
# FORD
# - Bronco
# - Mustang
# - Taurus
#
# HYUNDAI
# - Elantra
# - Sonata
# - Veracruz
#
# KIA
# - Optima
# - Sorento
# - Sportage
#
# MERCEDES-BENZ
# - 300D
# - 600SEL
# - E-Class
#
# NISSAN
# - Maxima
# - Pathfinder
# - Titan
#
# TOYOTA
# - Avalon
# - Highlander
# - Tundra
#
# VOLKSWAGEN
# - GTI
# - Passat
# - Routan
# """
#
#
# def test_group_cars_by_manufacturer(capfd):
#     group_cars_by_manufacturer(cars)
#     actual_output, _ = capfd.readouterr()
#     assert actual_output.strip() == expected_output.strip()
#
# import json
#
# import pytest
#
# from wc import convert_to_json
#
# @pytest.fixture(scope="module")
# def output():
#     return convert_to_json()
#
# def test_return_type(output):
#     assert type(output) == str
#
# def test_extracted_data_is_correct(output):
#     data = json.loads(output)
#     assert type(data) == list
#     assert len(data) == 10
#     for row in [{"id": "1", "first_name": "Junie", "last_name": "Kybert",
#                  "email": "jkybert0@army.mil"},
#                 {"id": "2", "first_name": "Sid", "last_name": "Churching",
#                  "email": "schurching1@tumblr.com"},
#                 {"id": "3", "first_name": "Cherry", "last_name": "Dudbridge",
#                  "email": "cdudbridge2@nifty.com"},
#                 {"id": "4", "first_name": "Merrilee", "last_name": "Kleiser",
#                  "email": "mkleiser3@reference.com"},
#                 {"id": "5", "first_name": "Umeko", "last_name": "Cray",
#                  "email": "ucray4@foxnews.com"},
#                 {"id": "6", "first_name": "Jenifer",
#                  "last_name": "Dale", "email": "jdale@hubpages.com"},
#                 {"id": "7", "first_name": "Deeanne", "last_name": "Gabbett",
#                  "email": "dgabbett6@ucoz.com"},
#                 {"id": "8", "first_name": "Hymie", "last_name": "Valentin",
#                  "email": "hvalentin7@blogs.com"},
#                 {"id": "9", "first_name": "Alphonso", "last_name":
#                  "Berwick", "email": "aberwick8@symantec.com"},
#                 {"id": "10", "first_name": "Wyn", "last_name": "Serginson",
#                  "email": "wserginson9@naver.com"}]:
#         assert row in data, f"{row} not in output of convert_to_json"
#
# import pytest
#
# from wc import operas_both_at_premiere
#
#
# def test_wagner_verdi():
#     # materializing to list to support generator as return
#     wagner_verdi = list(operas_both_at_premiere("wagner", "verdi"))
#     assert len(wagner_verdi) == 10
#     assert "Otello" not in wagner_verdi
#
#
# def test_verdi_wagner():
#     verdi_wagner = list(operas_both_at_premiere("verdi", "wagner"))
#     assert len(verdi_wagner) == 11
#
#     # premiere after Wagner's death (composed in 1833)
#     assert "The Fairies" not in verdi_wagner
#
#
# def test_beethoven_wagner():
#     beethoven_wagner = list(operas_both_at_premiere("beethoven", "wagner"))
#     assert len(beethoven_wagner) == 0
#
#
# def test_wagner_beethoven():
#     wagner_beethoven = list(operas_both_at_premiere("wagner", "beethoven"))
#     assert len(wagner_beethoven) == 0
#
#
# def test_beethoven_mozart():
#     beethoven_mozart = list(operas_both_at_premiere("beethoven", "mozart"))
#     assert len(beethoven_mozart) == 5
#     assert "Apollo and Hyacinth" not in beethoven_mozart
#
#
# def test_non_listed_composer():
#     with pytest.raises(ValueError):
#         list(operas_both_at_premiere("verdi", "dvorak"))
#
#
# def test_non_listed_guest():
#     # a guest must be in the list of composers
#     with pytest.raises(ValueError):
#         list(operas_both_at_premiere("dvorak", "verdi"))
# from dataclasses import astuple, replace
#
# import pytest
#
# from wc import Bite
#
#
# @pytest.fixture()
# def bites():
#     b1 = Bite(number=1, title="sum of numbers")
#     b2 = Bite(number=2, title="a second bite", level="Intermediate")
#     b3 = Bite(number=3, title="a hard bite", level="Advanced")
#     bites = [b1, b2, b3]
#     return bites
#
#
# def test_type_annotations():
#     assert Bite.__annotations__ == {'number': int, 'title': str, 'level': str}
#
#
# def test_getting_str_for_free(bites):
#     expected = Bite(number=1, title='Sum of numbers', level='Beginner')
#     assert bites[0] == expected
#
#
# def test_default_level_arg_first_bite(bites):
#     assert bites[0].level == 'Beginner'
#
#
# def test_attribute_access_second_bite(bites):
#     assert bites[1].number == 2
#     # title should get capitalized (use the __post_init__ method)
#     assert bites[1].title == 'A second bite'
#     assert bites[1].level == 'Intermediate'
#
#
# def test_my_data_class_is_mutable(bites):
#     b3 = bites[-1]
#     assert b3.level == 'Advanced'
#     # named tuples are immutable so would not allow this:
#     b3 = replace(b3, level='super hard')
#     assert b3.level == 'super hard'
#
#
# def test_can_order_bites(bites):
#     # not out of the box, need to set something on the data class ...
#     sorted_bites = sorted(bites, reverse=True)
#     assert sorted_bites[0].number == 3
#     assert sorted_bites[-1].number == 1
#
#
# def test_data_class_are_not_hashable(bites):
#     # this would work if namedtuples, but Bites are data classes here
#     with pytest.raises(TypeError):
#         set(bites)
#
#
# def test_data_class_can_only_be_unpacked_when_casted_to_tuple(bites):
#     with pytest.raises(TypeError):
#         number, title, level = bites[0]
#     # but this works:
#     number, title, level = astuple(bites[0])
#     assert number == 1
#     assert level == 'Beginner'
#
# import pytest
#
# from wc import split_words_and_quoted_text
#
# some_strings = (
#     'Should give "3 words only"',
#     'Our first program was "Hello PyBites"',
#     'Because "Hello World" is really cliche',
#     ('PyBites is a "A Community that Masters '
#      'Python through Code Challenges"')
# )
# expected_returns = (
#     ['Should', 'give', '3 words only'],
#     ['Our', 'first', 'program', 'was', 'Hello PyBites'],
#     ['Because', 'Hello World', 'is', 'really', 'cliche'],
#     ['PyBites', 'is', 'a', ('A Community that Masters Python '
#                             'through Code Challenges')]
# )
#
#
# @pytest.mark.parametrize("arg, ret",
#                          zip(some_strings, expected_returns))
#
# def test_split_words_and_quoted_text(arg, ret):
#     assert split_words_and_quoted_text(arg) == ret
# from wc import make_character_index
#
#
# the_neetle_tree = """
# There were once two brothers who lived on the edge of a forest.
# The elder brother was very mean to his younger brother and ate up all the food and took all his good clothes.
# One day, the elder brother went into the forest to find some firewood to sell in the market.
# As he went around chopping the branches of a tree after tree, he came upon a magical tree.
# The tree said to him, ‘Oh kind sir, please do not cut my branches.
# If you spare me, I will give you my golden apples’.
# The elder brother agreed but was disappointed with the number apples the tree gave him.
# Greed overcame him, and he threatened to cut the entire trunk if the tree didn’t give him more apples.
# The magical tree instead showered upon the elder brother hundreds upon hundreds of tiny needles.
# The elder brother lay on the ground crying in pain as the sun began to lower down the horizon.
# The younger brother grew worried and went in search of his elder brother.
# He found him with hundreds of needles on his skin.
# He rushed to his brother and removed each needle with painstaking love.
# After he finished, the elder brother apologised for treating him badly and promised to be better.
# The tree saw the change in the elder brother’s heart and gave them all the golden apples they could ever need.
# """
# characters = ('elder brother', 'younger brother', ('the tree', 'magical tree'))
#
#
# def test_make_character_index_with_default_args():
#     keys = ('red riding hood', 'grandmother', 'wolf', 'woodsman')
#     values = (
#         [1, 2, 3, 6, 7, 8, 11, 18, 19, 21, 24, 26, 28, 30, 33, 36],
#         [2, 3, 5, 11, 12, 14, 15, 16, 17, 21, 22, 24, 26, 28, 30, 33, 36],
#         [9, 10, 13, 14, 16, 17, 18, 20, 23, 25, 27, 29, 30, 31, 33, 35],
#         [32, 34, 35]
#     )
#     expected = dict(zip(keys, values))
#     actual = make_character_index()
#     assert actual == expected
#
#
# def test_make_character_index_with_other_args():
#     keys = ('elder brother', 'younger brother', 'the tree')
#     values = (
#         [2, 3, 7, 9, 10, 11, 14, 15],
#         [2, 11],
#         [4, 5, 7, 8, 9, 15],
#     )
#     actual = make_character_index(text=the_neetle_tree,
#                                   characters=characters)
#     expected = dict(zip(keys, values))
#     assert actual == expected
#
# import pytest
#
# from wc import filter_accents
#
# # texts taken from:
# # https://losviajesdedomi.com/las-15-ciudades-mas-bonitas-de-espana/
# # and:
# # https://www2.rocketlanguages.com/french/lessons/french-accents/
# texts = (
#     ("Denominada en Euskera como Donostia, está "
#      "situada en el Golfo de Vizcaya en la provincia "
#      "de Guipúzcoa. San Sebastián no es solo conocida "
#      "por su afamado festival de cine, sino también "
#      "por la belleza de sus calles, las cuales tienen "
#      "un corte francés y aburguesado que atraen cada "
#      "año a centenares de turistas."),
#     ("La capital de Cataluña, es la ciudad más visitada "
#      "de España y la segunda más poblada. Barcelona es "
#      "también una de las ciudades europeas más "
#      "cosmopolitas y todo un símbolo cultural, "
#      "financiero, comercial y turístico. Para muchos "
#      "Barcelona es la ciudad más atractiva de España y "
#      "una de las más bonitas."),
#     ("Sevilla es la capital de Andalucía, y para muchos, "
#      "la ciudad más bonita de España. Pasear por sus calles, "
#      "contemplar la Giralda, la Catedral o la Torre del Oro "
#      "es una auténtica gozada. En primavera el olor a azahar "
#      "lo envuelve todo. Al igual que Granada, toda la ciudad "
#      "es una auténtica delicia. Su clima hace propensa la "
#      "visita en casi cualquier época del año."),
#     ("The 5 French accents;"
#      "The cédille (cedilla) Ç ..."
#      "The accent aigu (acute accent) é ..."
#      "The accent circonflexe (circumflex) â, ê, î, ô, û ..."
#      "The accent grave (grave accent) à, è, ù ..."
#      "The accent tréma (dieresis/umlaut) ë, ï, ü"),
# )
# expected = (
#     ['á', 'é', 'ñ', 'ú'],
#     ['á', 'é', 'í', 'ñ'],
#     ['á', 'é', 'í', 'ñ'],
#     ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü'],
# )
#
#
# @pytest.mark.parametrize("text, expected", zip(texts, expected))
# def test_filter_accents(text, expected):
#     # get rid of duplicates and sort results
#     result = filter_accents(text)
#     actual = sorted(list(set(result)))
#     assert actual == expected
#
# import pytest
#
# from wc import simple_calculator
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ('2 + 3', 5),
#     ('5 + 11', 16),
#     ('12 + 18', 30),
# ])
# def test_sum(arg, expected):
#     assert simple_calculator(arg) == expected
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ('3 - 2', 1),
#     ('16 - 11', 5),
#     ('12 - 18', -6),
# ])
# def test_subtract(arg, expected):
#     assert simple_calculator(arg) == expected
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ('2 * 3', 6),
#     ('-5 * -11', 55),
#     ('3 * -6', -18),
# ])
# def test_multiply(arg, expected):
#     assert simple_calculator(arg) == expected
#
#
# @pytest.mark.parametrize("arg, expected", [
#     ('2 / 3', 0.67),
#     ('1 / 5', 0.2),
#     ('-2 / 175', -0.01),
# ])
# def test_true_division(arg, expected):
#     assert round(simple_calculator(arg), 2) == expected
#
#
# @pytest.mark.parametrize("arg", [
#     'a / 3', '2 / b', 'c / d', '1 2 3', '1 ^ 2',
#     '1 x 2', 'some random string', '1 / 0',
#     'really_bad_data'
# ])
# def test_bad_inputs(arg):
#     with pytest.raises(ValueError):
#         simple_calculator(arg)
#
# import pytest
#
# from wc import prefill_with_character, HTML_SPACE
#
# DIFF_FILL = 'x'
#
#
# @pytest.mark.parametrize("value, len_, fill, result", [
#     (1, 4, HTML_SPACE, f'{HTML_SPACE*3}1'),
#     (20, 4, HTML_SPACE, f'{HTML_SPACE*2}20'),
#     (315, 4, HTML_SPACE, f'{HTML_SPACE}315'),
#     (1239, 4, HTML_SPACE, '1239'),
#     (8, 5, DIFF_FILL, f'{DIFF_FILL*4}8'),
#     (12, 5, DIFF_FILL, f'{DIFF_FILL*3}12'),
#     (139, 5, DIFF_FILL, f'{DIFF_FILL*2}139'),
#     (9827, 5, DIFF_FILL, f'{DIFF_FILL}9827'),
#     (12345, 5, DIFF_FILL, '12345'),
# ])
# def test_prefill_with_character(value, len_, fill, result):
#     assert prefill_with_character(value, column_length=len_,
#                                     fill_char=fill) == result
#
# from wc import changed_dependencies
#
# # version might be fictitious for testing purposes
# old_reqs = """
# certifi==2017.4.17
# chardet==3.0.4
# click==6.7
# Faker==0.7.12
# Flask==0.12.1
# """
# new_reqs = """
# certifi==2016.11.29
# chardet==2.0.4
# click==5.0
# Faker==1.0.2
# Flask==1.0.2
# """
# other_old_reqs = """
# twilio==6.23.1
# urllib3==1.21.1
# Werkzeug==0.12.1
# WTForms==1.19.0
# """
# other_new_reqs = """
# twilio==6.3.0
# urllib3==1.21.1
# Werkzeug==0.14.1
# WTForms==2.1
# """
#
#
# def test_changed_dependencies_old_vs_new():
#     actual = changed_dependencies(old_reqs, new_reqs)
#     expected = ['Faker', 'Flask']
#     assert sorted(actual) == expected
#
#
# def test_changed_dependencies_other_data():
#     actual = changed_dependencies(other_old_reqs, other_new_reqs)
#     expected = ['WTForms', 'Werkzeug']
#     assert sorted(actual) == expected
#
# import pytest
#
# from wc import ToxIniParser
#
# cookiecutter = """[tox]
# envlist = py27, py34, py35, py36, pypy, flake8
#
# [testenv]
# passenv = LC_ALL, LANG, HOME
# commands = pytest --cov=cookiecutter {posargs:tests}
# deps = -rtest_requirements.txt
#
# [testenv:flake8]
# deps =
#     flake8==3.5.0
# commands =
#     flake8 cookiecutter tests setup.py
#
# [testenv:cov-report]
# commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""
#
# django = """# Tox (https://tox.readthedocs.io/) is a tool for running tests in multiple
# # virtualenvs. This configuration file helps to run the test suite on all
# # supported Python versions. To use it, "pip install tox" and then run "tox"
# # from this directory.
# #
# # copied from: https://github.com/django/django/blob/master/tox.ini
#
# [tox]
# skipsdist = true
# envlist =
#     py3
#     flake8
#     docs
#     isort
#
# # Add environment to use the default python3 installation
# [testenv:py3]
# basepython = python3
#
# [testenv]
# usedevelop = true
# passenv = DJANGO_SETTINGS_MODULE PYTHONPATH HOME DISPLAY
# setenv =
#     PYTHONDONTWRITEBYTECODE=1
# deps =
#     py{3,35,36,37}: -rtests/requirements/py3.txt
#     postgres: -rtests/requirements/postgres.txt
#     mysql: -rtests/requirements/mysql.txt
#     oracle: -rtests/requirements/oracle.txt
# changedir = tests
# commands =
#     {envpython} runtests.py {posargs}
#
# [testenv:flake8]
# basepython = python3
# usedevelop = false
# deps = flake8
# changedir = {toxinidir}
# commands = flake8 .
#
# [testenv:docs]
# basepython = python3
# usedevelop = false
# whitelist_externals =
#     make
# deps =
#     Sphinx
#     pyenchant
#     sphinxcontrib-spelling
# changedir = docs
# commands =
#     make spelling
#
# [testenv:isort]
# basepython = python3
# usedevelop = false
# deps = isort
# changedir = {toxinidir}
# commands = isort --recursive --check-only --diff django tests scripts
#
# [testenv:javascript]
# usedevelop = false
# deps =
# changedir = {toxinidir}
# whitelist_externals = npm
# commands =
#     npm install
#     npm test"""
#
# oeuvre = """[tox]
# minversion=2.3.1
# envlist = py27,py33,py34,py35,py36,flake8,linters,docs
#
# [testenv]
# deps =
#     mock>=2.0.0
#     pytest!=3.0.5
#     coverage
# commands =
#     coverage run --parallel-mode -m pytest {posargs}
#     coverage combine
#     coverage report -m
#
# [testenv:venv]
# deps =
#     .
# commands = {posargs}
#
# # Linters
# [testenv:flake8]
# basepython = python3
# skip_install = true
# deps =
#     flake8
#     flake8-docstrings>=0.2.7
#     flake8-import-order>=0.9
# commands =
#     flake8 src/oeuvre/ tests/ setup.py
#
# [testenv:pylint]
# basepython = python3
# skip_install = true
# deps =
#     pyflakes
#     pylint
# commands =
#     pylint src/oeuvre
#
# [testenv:doc8]
# basepython = python3
# skip_install = true
# deps =
#     sphinx
#     doc8
# commands =
#     doc8 docs/source/
#
# [testenv:bandit]
# basepython = python3
# skip_install = true
# deps =
#     bandit
# commands =
#     bandit -r src/oeuvre/ -c .bandit.yml
#
# [testenv:linters]
# basepython = python3
# skip_install = true
# deps =
#     {[testenv:flake8]deps}
#     {[testenv:pylint]deps}
#     {[testenv:doc8]deps}
#     {[testenv:readme]deps}
#     {[testenv:bandit]deps}
# commands =
#     {[testenv:flake8]commands}
#     {[testenv:pylint]commands}
#     {[testenv:doc8]commands}
#     {[testenv:readme]commands}
#     {[testenv:bandit]commands}
#
# # Documentation
# [testenv:docs]
# basepython = python3
# deps =
#     sphinx>=1.3.0
#     sphinx_rtd_theme
# commands =
#     sphinx-build -E -W -c docs/source/ -b html docs/source/ docs/build/html
#     sphinx-build -E -W -c docs/source/ -b man docs/source/ docs/build/man
#
# [testenv:serve-docs]
# basepython = python3
# skip_install = true
# changedir = docs/build/html
# deps =
# commands =
#     python -m http.server {posargs}
#
# [testenv:readme]
# basepython = python3
# deps =
#     readme_renderer
# commands =
#     python setup.py check -r -s
#
# # Release tooling
# [testenv:build]
# basepython = python3
# skip_install = true
# deps =
#     wheel
#     setuptools
# commands =
#     python setup.py -q sdist bdist_wheel
#
# [testenv:release]
# basepython = python3
# skip_install = true
# deps =
#     {[testenv:build]deps}
#     twine >= 1.5.0
# commands =
#     {[testenv:build]commands}
#     twine upload --skip-existing dist/*
#
# # Flake8 Configuration
# [flake8]
# # Ignore some flake8-docstrings errors
# ignore = D203
# exclude =
#     .tox,
#     .git,
#     __pycache__,
#     docs/source/conf.py,
#     build,
#     dist,
#     *.pyc,
#     *.egg-info,
#     .cache,
#     .eggs
# max-complexity = 10
# import-order-style = google
# application-import-names = oeuvre"""
#
# pyramid = """[tox]
# envlist =
#     lint,
#     py34,py35,py36,py37,pypy3,
#     docs,py36-cover,coverage,
#
# [testenv]
# commands =
#     cover: coverage run \
#     {envbindir}/nosetests --with-xunit --xunit-file=...
# extras =
#     testing
# deps =
#     cover: coverage
# setenv =
#     COVERAGE_FILE=.coverage.{envname}
#
# [testenv:lint]
# skip_install = true
# basepython = python3.6
# commands =
#     flake8 src/pyramid tests setup.py
#     black --check --diff src/pyramid tests setup.py
#     python setup.py check -r -s -m
#     check-manifest
# deps =
#     flake8
#     black
#     readme_renderer
#     check-manifest
#
# [testenv:docs]
# # pin to 3.5 to match what RTD uses
# basepython = python3.5
# whitelist_externals = make
# commands =
#     make -C docs doctest html epub BUILDDIR={envdir} "SPHINXOPTS=-W -E"
# extras =
#     docs
#
# [testenv:pdf]
# basepython = python3.5
# whitelist_externals = make
# commands =
#     make -C docs latexpdf BUILDDIR={envdir} "SPHINXOPTS=-W -E"
# extras =
#     docs
#
# [testenv:coverage]
# skip_install = true
# basepython = python3.6
# commands =
#     coverage combine
#     coverage xml
#     coverage report --fail-under=100
# deps =
#     coverage
# setenv =
#     COVERAGE_FILE=.coverage
#
# [testenv:black]
# skip_install = true
# basepython = python3.6
# commands =
#     black src/pyramid tests setup.py
# deps =
#     black
#
# [testenv:build]
# skip_install = true
# basepython = python3.6
# commands =
#     # clean up build/ and dist/ folders
#     python -c 'import shutil; shutil.rmtree("dist", ignore_errors=True)'
#     python setup.py clean --all
#     # build sdist
#     python setup.py sdist --dist-dir {toxinidir}/dist
#     # build wheel from sdist
#     pip wheel -v --no-deps --no-index --no-build-isolation ...
# deps =
#     setuptools
#     wheel"""
#
# ini_files = (cookiecutter, django, oeuvre, pyramid)
#
#
# @pytest.mark.parametrize("ini_file, num_sections, envs, base_pys", [
#     (cookiecutter, 4,
#      ['flake8', 'py34', 'py35', 'py36', 'pypy', 'py27'],
#      []),
#     (django, 7,
#      ['docs', 'flake8', 'isort', 'py3'],
#      ['python3']),
#     (pyramid, 8,
#      ['coverage', 'docs', 'lint', 'py34', 'py35', 'py36', 'py36-cover',
#       'py37', 'pypy3'],
#      ['python3.5', 'python3.6']),
#     (oeuvre, 14,
#      ['docs', 'flake8', 'linters', 'py27', 'py33', 'py34',
#       'py35', 'py36'],
#      ['python3']),
# ])
# def test_tox_ini_parser(ini_file, num_sections, envs, base_pys, tmp_path):
#     f = tmp_path / "some_file.txt"
#     f.write_bytes(ini_file.encode())  # https://bugs.python.org/issue17271
#
#     tip = ToxIniParser(f.resolve())
#
#     assert tip.number_of_sections == num_sections
#     assert sorted(tip.environments) == sorted(envs)
#     assert sorted(tip.base_python_versions) == sorted(base_pys)

#
# from wc import add_todo
#
# def test_wash_car_tomorrow_morning():
#     actual = add_todo("11h 10m", "Wash my car")
#     expected = "Wash my car @ 2019-02-07 09:10:00"
#     assert actual == expected
#
#
# def test_code_bite_tomorrow_same_time():
#     actual = add_todo("30d", "Code a Bite")
#     expected = "Code a Bite @ 2019-03-08 22:00:00"
#     assert actual == expected
#
#
# def test_go_to_bed_in_five_min_and_three_seconds():
#     actual = add_todo("5m 3s", "Go to Bed")
#     expected = "Go to Bed @ 2019-02-06 22:05:03"
#     assert actual == expected
#
#
# def test_finish_this_test_in_seconds_as_int():
#     actual = add_todo("45", "Finish this Test")
#     expected = "Finish this Test @ 2019-02-06 22:00:45"
#     assert actual == expected
#
#
# def test_study_data_science_at_d_h_m_s():
#     actual = add_todo("1d 10h 47m 17s", "Study some Python")
#     expected = "Study some Python @ 2019-02-08 08:47:17"
#     assert actual == expected
#
# from datetime import date, timedelta
# from random import shuffle
#
# import pytest
#
# from wc import get_missing_dates
#
#
# def _create_dates(missing, year=2019, month=2):
#     """Helper function to build up test cases.
#
#        Returns a list of dates omitting days given
#        in the missing argument.
#
#        You can optionally specify year and month.
#     """
#     first = date(year=year, month=month, day=1)
#     last = first.replace(month=month+1) - timedelta(days=1)
#
#     # always yield first and last, for the in between dates
#     # only the ones not in missing
#     yield first
#
#     for day in range(first.day + 1, last.day):
#         if day not in missing:
#             yield first.replace(day=day)
#
#     yield last
#
#
# @pytest.mark.parametrize("missing, month", [
#     ([2, 7, 11], 2),
#     (list(range(2, 12, 2)), 3),
#     ([14, 12], 3),
#     ([2, 3, 7, 9], 4),
#     ([1, 3, 7, 31], 5),  # expected = 3, 7, not start/end month
#     (list(range(1, 31)), 6),  # 0 missing
# ])
# def test_get_missing_dates(missing, month):
#     my_date_range = list(_create_dates(missing, month=month))
#     start, end = my_date_range[0].day, my_date_range[-1].day
#
#     # order passed in arg should not matter
#     shuffle(my_date_range)
#
#     # get days from return sequence
#     actual = sorted(d.day for d in
#                     get_missing_dates(my_date_range))
#
#     # filter out begin and end dates of range
#     expected = sorted(d for d in missing if
#                       d not in (start, end))
#
#     assert actual == expected
#
# import pytest
#
# from wc import get_min_max_amount_of_commits
#
#
# @pytest.mark.parametrize('year, expected', [
#     (None, ('2018-02', '2017-01')),  # parse the whole file
#     (2017, ('2017-11', '2017-01')),
#     (2018, ('2018-02', '2018-10')),
#     (2019, ('2019-01', '2019-03')),
# ])
# def test_get_min_max_amount_of_commits(year, expected):
#     actual = get_min_max_amount_of_commits(year=year)
#     assert actual == expected
#
# import pytest
#
# from wc import extract_quotes
#
#
# expected_authors = [
#     'B.B King', 'Wendy Kopp', 'Barack Obama', 'T.F. Hodge',
#     'Helen Keller', 'Confucius', 'Les Brown', 'Winston Churchill',
#     'Theodore Roosevelt', 'Zig Ziglar'
# ]
#
# expected_quotes = [
#     ('The beautiful thing about learning is nobody can take it away'
#      ' from you.'),
#     'Inexperience is an asset. Embrace it.',
#     ('Change will not come if we wait for some other person, or if '
#      'we wait for some other time. We are the ones we’ve been '
#      'waiting for. We are the change that we seek.'),
#     'The sky is not my limit… I am.',
#     'Life is either a daring adventure or nothing at all.',
#     'It does not matter how slowly you go as long as you do not stop.',
#     ('Too many of us are not living our dreams because we are '
#      'living our fears.'),
#     ('Continuous efforts – not strength or intelligence – is the '
#      'key to unlocking our potential.'),
#     'Believe you can and you’re halfway there.',
#     ('Success means doing the best we can with what we have. '
#      'Success is the doing, not the getting; in the trying, '
#      'not the triumph. Success is a personal standard, reaching '
#      'for the highest that is in us, becoming all that we can be.')
# ]
#
#
# @pytest.fixture(scope="module")
# def output_your_code():
#     return extract_quotes()
#
#
# def test_quotes_type(output_your_code):
#     assert type(output_your_code) == dict
#
#
# def test_quotes_len(output_your_code):
#     assert len(output_your_code) == 10
#
#
# @pytest.mark.parametrize("author, quote",
#                          zip(expected_authors, expected_quotes))
# def test_quotes_dict_content(author, quote, output_your_code):
#     assert output_your_code.get(author) == quote
#
# import pytest
#
# from wc import BiteStats
#
#
# @pytest.fixture(scope="module")
# def bite_stats():
#     return BiteStats()
#
#
# def test_number_bites_accessed(bite_stats):
#     assert bite_stats.number_bites_accessed == 176
#
#
# def test_number_bites_resolved(bite_stats):
#     assert bite_stats.number_bites_resolved == 115
#
#
# def test_number_users_active(bite_stats):
#     assert bite_stats.number_users_active == 114
#
#
# def test_number_users_solving_bites(bite_stats):
#     assert bite_stats.number_users_solving_bites == 76
#
#
# def test_top_bite_by_number_of_clicks(bite_stats):
#     assert int(bite_stats.top_bite_by_number_of_clicks) == 101
#
#
# def test_top_user_by_bites_completed(bite_stats):
#     assert bite_stats.top_user_by_bites_completed == 'mcaberasu'
#
# import string
#
# import pytest
#
# from wc import suggest_word, load_words
#
#
# @pytest.fixture(scope='module')
# def a_words():
#     """Get only a[abcdefghijklm]-words to speed up tests"""
#     words = load_words()
#     return {word for word in words
#             if word.startswith('a') and len(word) > 1
#             and word[1] in string.ascii_letters[:13]}
#
#
# @pytest.mark.parametrize("word, expected", [
#     ('acheive', 'achieve'),
#     ('accross', 'across'),
#     ('acceptible', 'acceptable'),
#     ('allmost', 'almost'),
#     ('aquire', 'acquire'),
#     ('agressive', 'aggressive'),
#     ('accomodate', 'accommodate'),
#     ('accidentaly', 'accidentally'),
# ])
# def test_suggest_word(word, expected, a_words):
#     assert suggest_word(word, words=a_words) == expected
#
# import pytest
#
# from wc import get_number_books_read
#
#
# @pytest.mark.parametrize("goal, date_str, expected", [
#     (52, 'Sunday, March 18th, 2019', 12),
#     (52, 'Sunday, March 25th, 2019', 13),
#     (52, 'April 2nd, 2019', 14),
#     (100, 'Sunday, March 18th, 2019', 23),
#     (100, 'Sunday, March 25th, 2019', 25),
#     (100, '2019-04-02', 26),
#     (52, None, 11),
#     (100, None, 21),
#     (100, '11-20-2019', 90),
#     (100, '5/20/2019', 40),
# ])
# def test_get_number_books_read(goal, date_str, expected):
#     assert get_number_books_read(goal, date_str) == expected
#
#
# def test_not_positive_goal_exception():
#     with pytest.raises(ValueError):
#         get_number_books_read(0)
#     with pytest.raises(ValueError):
#         get_number_books_read(-1)
#
#
# def test_past_date_exception():
#     with pytest.raises(ValueError):
#         get_number_books_read(52, '5-20-2018')

# import pytest
#
# from wc import Actor, Movie, get_age
#
#
# actors = [
#     Actor('Wesley Snipes', 'July 31, 1962'),
#     Actor('Robert de Niro', 'August 17, 1943'),
#     Actor('Jennifer Aniston', 'February 11, 1969'),
#     Actor('Mikey Rourke', 'September 16, 1952'),
#     Actor('Al Pacino', 'July 31, 1962'),
#     Actor('Alec Baldwin', 'July 31, 1962'),
#     Actor('Michelle Pfeiffer', 'April 29, 1958'),
# ]
# movies = [
#     Movie('New Jack City', 'January 17, 1991'),
#     Movie('Goodfellas', 'October 19, 1990'),
#     Movie('Horrible Bosses', 'September 16, 2011'),
#     Movie('Harley Davidson and the Marlboro Man', 'December 28, 1991'),
#     Movie('Heat', 'December 15, 1995'),
#     Movie('Glengarry Glen Ross', 'September 29, 1992'),
#     Movie('Scarface', 'March 12, 1984'),
# ]
# return_strings = [
#     'Wesley Snipes was 28 years old when New Jack City came out.',
#     'Robert de Niro was 47 years old when Goodfellas came out.',
#     'Jennifer Aniston was 42 years old when Horrible Bosses came out.',
#     'Mikey Rourke was 39 years old when Harley Davidson and the Marlboro Man came out.',  # noqa E501
#     'Al Pacino was 33 years old when Heat came out.',
#     'Alec Baldwin was 30 years old when Glengarry Glen Ross came out.',
#     'Michelle Pfeiffer was 25 years old when Scarface came out.',
# ]
#
#
# @pytest.mark.parametrize('actor, movie, expected',
#                          zip(actors, movies, return_strings))
# def test_get_age(actor, movie, expected):
#     assert get_age(actor, movie) == expected
#
# import pytest
#
# from wc import get_income_distribution
#
# EXPECTED = {'High income': ['Aruba',
#                             'Argentina',
#                             'Antigua and Barbuda',
#                             'Bahamas, The',
#                             'Barbados',
#                             'Chile',
#                             'Curacao',
#                             'Cayman Islands',
#                             'St. Kitts and Nevis',
#                             'St. Martin (French part)',
#                             'Panama',
#                             'Puerto Rico',
#                             'Sint Maarten (Dutch part)',
#                             'Turks and Caicos Islands',
#                             'Trinidad and Tobago',
#                             'Uruguay',
#                             'British Virgin Islands',
#                             'Virgin Islands (U.S.)'],
#             'Low income': ['Haiti'],
#             'Lower middle income': ['Bolivia',
#                                     'Honduras',
#                                     'Nicaragua',
#                                     'El Salvador'],
#             'Upper middle income': ['Belize',
#                                     'Brazil',
#                                     'Colombia',
#                                     'Costa Rica',
#                                     'Cuba',
#                                     'Dominica',
#                                     'Dominican Republic',
#                                     'Ecuador',
#                                     'Grenada',
#                                     'Guatemala',
#                                     'Guyana',
#                                     'Jamaica',
#                                     'St. Lucia',
#                                     'Mexico',
#                                     'Peru',
#                                     'Paraguay',
#                                     'Suriname',
#                                     'St. Vincent and the Grenadines',
#                                     'Venezuela, RB']}
#
#
# @pytest.fixture(scope="module")
# def actual():
#     return get_income_distribution()
#
#
# @pytest.mark.parametrize("income, countries", EXPECTED.items())
# def test_return_function(actual, income, countries):
#     assert income in actual
#     assert sorted(actual[income]) == sorted(countries)
#
# from wc import person_max_bmi, data
#
#
# def test_person_max_bmi():
#     assert person_max_bmi() == ('Yoda', 39.03)
#
#
# def test_person_max_bmi_smaller_dataset():
#     newdata = '\n'.join(data.splitlines()[:10])
#     assert person_max_bmi(newdata) == ('Owen Lars', 37.87)
#
#
# def test_person_max_bmi_another_smaller_dataset():
#     newdata = '\n'.join([row for row in data.splitlines()
#                          if row.lstrip()[:4] not in ('Owen', 'Yoda')])
#     assert person_max_bmi(newdata) == ('IG-88', 35.0)
# import pytest
# from wc import top_python_questions
#
# actual_return = top_python_questions()
# expected_return = [
#     ('What does the “yield” keyword do?', 9169),
#     ('Does Python have a ternary conditional operator?', 5135),
#     ('What does if __name__ == “__main__”: do?', 4927),
#     ('Calling an external command in Python', 4190),
#     ('How to merge two dictionaries in a single expression?', 3874),
#     ('How do I sort a dictionary by value?', 3394),
#     ('Using global variables in a function', 2768),
#     ('Understanding slice notation', 2707),
#     ('How to make a flat list out of list of lists', 2545),
#     ('How do I install pip on Windows?', 2388),
#     ('How do I pass a variable by reference?', 2295),
#     ('How to clone or copy a list?', 2063),
#     ('How to read a file line-by-line into a list?', 2000),
#     ('Converting string into datetime', 1816),
#     ('How to print without newline or space?', 1615),
#     ('Select rows from a DataFrame based on '
#      'values in a column in pandas', 1304),
#     ("Why does comparing strings using either '==' or 'is' "
#      'sometimes produce a different result?', 1008)
# ]
#
#
# @pytest.mark.parametrize('actual, expected',
#                          zip(actual_return, expected_return)
#                          )
# def test_top_python_questions(actual, expected):
#     assert actual == expected
#
# from time import time
#
# import pytest
#
# from wc import cached_fib
#
# N = 30
#
#
# def nocache_fib(n):
#     if n < 2:
#         return n
#     return nocache_fib(n - 1) + nocache_fib(n - 2)
#
#
# def _run(func):
#     start = time()
#     ret = func(N)
#     end = time()
#     return ret, end - start
#
#
# @pytest.fixture(scope='module')
# def not_cached():
#     return _run(nocache_fib)
#
#
# @pytest.fixture(scope='module')
# def cached():
#     return _run(cached_fib)
#
#
# def test_correct_fibonacci(cached):
#     ret, _ = cached
#     err = 'Did not assert fibonacci return for n=30'
#     assert ret == 832040, err
#
#
# def test_cached_faster_than_non_cached(not_cached, cached):
#     _, t1 = not_cached
#     _, t2 = cached
#     err = 'Cached version is not at least 10x faster'
#     assert t2 < t1/10, err
#
# from wc import (cur,
#                  player_with_max_points_per_game,
#                  number_of_players_from_duke,
#                  avg_years_active_players_stanford,
#                  year_with_most_new_players)
#
#
# def test_total_row_count_after_import():
#     sql = '''SELECT COUNT(*) FROM players'''
#     cur.execute(sql)
#     ret = cur.fetchall()
#     assert ret[0][0] == 3961
#
#
# def test_player_with_max_points_per_game():
#     assert player_with_max_points_per_game() == 'Michael Jordan'
#
#
# def test_number_of_players_from_duke():
#     assert number_of_players_from_duke() == 58
#
#
# def test_avg_years_active_players_stanford():
#     assert round(avg_years_active_players_stanford(), 2) == 4.58
#
#
# def test_year_with_most_new_players():
#     assert int(year_with_most_new_players()) == 1984

#
# from datetime import date
#
# import pytest
#
#
# from wc import get_mothers_day_date
#
#
# def test_check_type():
#     assert type(get_mothers_day_date(2019)) == date
#
#
# @pytest.mark.parametrize('arg,expected', [
#     (2014, date(2014, 5, 11)),
#     (2015, date(2015, 5, 10)),
#     (2016, date(2016, 5, 8)),
#     (2017, date(2017, 5, 14)),
#     (2018, date(2018, 5, 13)),
#     (2019, date(2019, 5, 12)),
#     (2020, date(2020, 5, 10)),
#     (2021, date(2021, 5, 9)),
#     (2022, date(2022, 5, 8)),
#     (2023, date(2023, 5, 14)),
#     (2024, date(2024, 5, 12)),
# ])
# def test_return_various_years(arg, expected):
#     assert get_mothers_day_date(arg) == expected
# import inspect
#
# import pytest
#
# from wc import Person, Father, Mother, Child
#
#
# @pytest.fixture
# def person():
#     return Person()
#
#
# @pytest.fixture
# def dad():
#     return Father()
#
#
# @pytest.fixture
# def mom():
#     return Mother()
#
#
# @pytest.fixture
# def child():
#     return Child()
#
#
# def test_string_repr_person(person):
#     assert str(person) == 'I am a person'
#
#
# def test_string_repr_dad(dad):
#     assert str(dad) == 'I am a person and cool daddy'
#
#
# def test_string_repr_mom(mom):
#     assert str(mom) == 'I am a person and awesome mom'
#
#
# def test_string_repr_child(child):
#     assert str(child) == 'I am the coolest kid'
#
#
# def test_mro_of_person():
#     assert Person.__mro__ == (Person, object)
#
#
# def test_mro_of_dad():
#     assert Father.__mro__ == (Father, Person, object)
#
#
# def test_mro_of_mom():
#     assert Mother.__mro__ == (Mother, Person, object)
#
#
# def test_mro_of_child():
#     assert Child.__mro__ == (Child, Father, Mother, Person, object)
#
#
# def test_subclass_person():
#     assert issubclass(Person, object)
#
#
# def test_subclass_dad():
#     assert issubclass(Father, Person)
#     assert issubclass(Father, object)
#
#
# def test_subclass_mom():
#     assert issubclass(Mother, Person)
#     assert issubclass(Mother, object)
#
#
# def test_subclass_child():
#     assert issubclass(Child, Father)
#     assert issubclass(Child, Mother)
#     assert issubclass(Child, Person)
#     assert issubclass(Child, object)
#
#
# def test_use_inheritance():
#     # dry code!
#     # should not duplicate substr in subclass
#     substr = 'I am a person'
#     for src in (inspect.getsource(Father),
#                 inspect.getsource(Mother)):
#         assert substr not in src
#
# from unittest.mock import patch, Mock
#
# import requests
#
# from wc import nxapi_show_version
#
# switch_output = dict(
#     kern_uptm_secs=21,
#     kick_file_name='bootflash:///nxos.9.2.1.bin.S2460',
#     rr_service=None,
#     module_id='Supervisor Module',
#     kick_tmstmp='07/11/2018 00:01:44',
#     bios_cmpl_time='05/17/2018',
#     bootflash_size=20971520,
#     kickstart_ver_str='9.2(1)',
#     kick_cmpl_time='7/9/2018 9:00:00',
#     chassis_id='Nexus9000 C9504 (4 Slot) Chassis',
#     proc_board_id='SAL171211LX',
#     memory=16077872,
#     manufacturer='Cisco Systems, Inc.',
#     kern_uptm_mins=26,
#     bios_ver_str='05.31',
#     cpu_name='Intel(R) Xeon(R) CPU D-1528 @ 1.90GHz',
#     kern_uptm_hrs=2,
#     rr_usecs=816550,
#     rr_sys_ver='9.2(1)0',
#     rr_reason='Reset Requested by CLI command reload',
#     rr_ctime='Wed Jul 11 20:44:39 2018',
#     header_str='Cisco Nexus Operating System (NX-OS) Software',
# )
#
#
# @patch.object(requests, 'post')
# def test_get_version(mock_post):
#     response = dict(result=dict(body=switch_output))
#     mock_post.return_value = Mock(json=lambda: response)
#     assert nxapi_show_version() == "9.2(1)"
#
#
# @patch.object(requests, 'post')
# def test_get_different_version(mock_post):
#     switch_output['kickstart_ver_str'] = "7.2(0)"
#     response = dict(result=dict(body=switch_output))
#     mock_post.return_value = Mock(json=lambda: response)
#     assert nxapi_show_version() == "7.2(0)"
#
# from pathlib import Path
# from tempfile import TemporaryDirectory
#
# import pytest
#
# from wc import get_most_complex_bites, TMP
#
# BITES_CSV = TMP / 'intro_bites.csv'
# INTRO_BITE_STATS = """Bite;Difficulty
# Bite 101. f-strings and a simple if/else;3.52
# Bite 102. Infinite loop, input, continue and break;3.59
# Bite 103. Loop through a dictionary and pluralise a word;3.21
# Bite 104. Split and join;2.91
# Bite 105. Slice and dice;5.0
# Bite 106. Strip out vowels and count the number of replacements;4.73
# Bite 107. Filter numbers with a list comprehension;1.89
# Bite 108. Loop over a dict of namedtuples calculating a total score;4.83
# Bite 109. Workout dict lookups and raising an exception;2.75
# Bite 110. Type conversion and exception handling;1.5
# """
#
#
# @pytest.fixture
# def intro_bites():
#     with TemporaryDirectory(dir=TMP):
#         with open(BITES_CSV, 'w') as f:
#             f.write(INTRO_BITE_STATS)
#     return BITES_CSV
#
#
# @pytest.mark.parametrize("N, expected", [
#     (2, ['88', '31']),
#     (6, ['88', '31', '50', '90', '179', '98']),
#     (10, ['88', '31', '50', '90', '179', '98', '190', '42', '69', '40']),
# ])
# def test_different_args_for_N(N, expected):
#     actual = get_most_complex_bites(N)
#     # str or int for IDs is fine with us
#     actual = [str(i) for i in actual]
#     assert actual == expected
#
#
# @pytest.mark.parametrize("N, expected", [
#     (1, ['105']),
#     (3, ['105', '108', '106']),
#     # res is max = size of bites in file:
#     (15, ['105', '108', '106', '102', '101', '103',
#           '104', '109', '107', '110']),
# ])
# def test_only_intro_bites(intro_bites, N, expected):
#     actual = get_most_complex_bites(N, stats=intro_bites)
#     # str or int for IDs is fine with us
#     actual = [str(i) for i in actual]
#     assert actual == expected
#
# from typing import get_type_hints
#
# import pytest
#
# from wc import Employee
#
#
# @pytest.fixture(scope="module")
# def employee():
#     return Employee("Mohhinder", "Suresh", 5, 8, 12.75)
#
#
# def test_employee_type_hints(employee):
#     actual = get_type_hints(employee)
#     expected_type_hints = {
#         "first_name": str,
#         "last_name": str,
#         "days_per_week": int,
#         "hours_per_day": float,
#         "wage": float,
#     }
#     assert actual == expected_type_hints
#
#
# def test_rounder_type_hints(employee):
#     actual = get_type_hints(employee._rounder)
#     expected_type_hints = {
#         "number": float,
#         "places": int,
#         "return": str,
#     }
#     assert actual == expected_type_hints
#
#
# def test_weekly_pay(employee):
#     assert isinstance(employee.weekly_pay, str)
#
# import pytest
#
# from wc import (get_pycon_speaker_first_names,
#                      get_percentage_of_female_speakers)
#
#
# @pytest.fixture(scope='module')
# def first_names():
#     return get_pycon_speaker_first_names()
#
#
# def test_get_pycon_speaker_first_names(first_names):
#     assert len(first_names) == 112
#     assert 'Luciano' in first_names
#     assert 'Erin' in first_names
#     assert 'Rachael' in first_names
#
#
# def test_get_percentage_of_female_speakers(first_names):
#     actual = get_percentage_of_female_speakers(first_names)
#     expected = 28.57
#     assert actual == expected
#
# import pytest
#
# from wc import check_split
#
#
# @pytest.mark.parametrize("args, expected", [
#     (('$8.68', '4.75%', '10%', 3), '$10.00'),
#     (('$8.44', '6.75%', '11%', 3), '$10.00'),
#     (('$9.99', '3.25%', '10%', 2), '$11.34'),
#     (('$186.70', '6.75%', '18%', 6), '$235.17'),
#     (('$191.57', '6.75%', '15%', 6), '$235.18'),
#     (('$0.00', '0%', '0%', 1), '$0.00'),
#     (('$100.03', '0%', '0%', 4), '$100.03'),
#     (('$141.86', '2%', '18%', 9), '$170.75'),
#     (('$16.99', '10%', '20%', 1), '$22.43'),
#     (('$16.99', '10%', '20%', 2), '$22.43'),
#     (('$16.99', '10%', '20%', 3), '$22.43'),
#     (('$16.99', '10%', '20%', 4), '$22.43'),
# ])
# def test_check_split(args, expected):
#     grand_total, splits = check_split(*args)
#     assert grand_total == expected
#     assert grand_total == f'${sum(splits)}'
#
# import inspect
#
# from wc import sum_numbers
#
#
# def test_functionality():
#     numbers = [1, 2, 0, 4, 5, 12, 'a', 3]
#     actual = list(sum_numbers(numbers))
#     expected = [0.5, 0.0, 0.8, 0.4166666666666667]
#     assert actual == expected
#
#
# def test_use_of_idioms():
#     src = inspect.getsource(sum_numbers)
#     assert 'try' not in src
#     assert 'except ' not in src
#     assert 'yield' in src
#     assert 'TypeError' in src
#     assert 'ZeroDivisionError' in src
#     assert src.count('suppress(') in (1, 2)
#     assert src.count('with') in (1, 2)
#
# import inspect
#
# import pytest
#
# from wc import get_len_help_text
#
#
# def test_pow():
#     assert get_len_help_text(pow) == 280
#
#
# def test_max():
#     assert get_len_help_text(max) == 398
#
#
# def test_bad_input():
#     max1 = object()
#     with pytest.raises(ValueError):
#         get_len_help_text(max1)
#
#
# def test_another_bad_input():
#     with pytest.raises(ValueError):
#         get_len_help_text('string')
#
#
# def test_src():
#     src = inspect.getsource(get_len_help_text)
#     assert 'help' in src
#     assert 'redirect_stdout' in src
# from datetime import date
# from itertools import islice
#
# from wc import gen_bite_planning
#
# TODAY = date(2019, 8, 25)
#
#
# def test_one_bite_a_day():
#     gen = gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY)
#     actual = list(islice(gen, 10))
#     expected = [date(2019, 8, 26), date(2019, 8, 27),
#                 date(2019, 8, 28), date(2019, 8, 29),
#                 date(2019, 8, 30), date(2019, 8, 31),
#                 date(2019, 9, 1), date(2019, 9, 2),
#                 date(2019, 9, 3), date(2019, 9, 4)]
#     assert actual == expected
#
#
# def test_two_bites_every_three_days():
#     gen = gen_bite_planning(num_bites=2, num_days=3, start_date=TODAY)
#     actual = list(islice(gen, 10))
#     expected = [date(2019, 8, 28), date(2019, 8, 28),
#                 date(2019, 8, 31), date(2019, 8, 31),
#                 date(2019, 9, 3), date(2019, 9, 3),
#                 date(2019, 9, 6), date(2019, 9, 6),
#                 date(2019, 9, 9), date(2019, 9, 9)]
#     assert actual == expected
#
#
# def test_one_bite_every_other_day():
#     gen = gen_bite_planning(num_bites=1, num_days=2, start_date=TODAY)
#     actual = list(islice(gen, 10))
#     expected = [date(2019, 8, 27), date(2019, 8, 29),
#                 date(2019, 8, 31), date(2019, 9, 2),
#                 date(2019, 9, 4), date(2019, 9, 6),
#                 date(2019, 9, 8), date(2019, 9, 10),
#                 date(2019, 9, 12), date(2019, 9, 14)]
#     assert actual == expected
#
# import json
# import os
# from pathlib import Path
# from unittest.mock import patch
# from urllib.request import urlretrieve
#
# from wc import (get_best_seller_titles,
#                  URL_NON_FICTION, URL_FICTION)
#
# TMP = Path(os.getenv("TMP", "/tmp"))
#
# FICTION = TMP / 'nyt-fiction.json'
# if not FICTION.exists():
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/nyt-fiction.json',
#         FICTION
#     )
#
# NON_FICTION = TMP / 'nyt-nonfiction.json'
# if not NON_FICTION.exists():
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/nyt-nonfiction.json',
#         NON_FICTION
#     )
#
#
# def mocked_requests_get(*args, **kwargs):
#     """https://stackoverflow.com/a/28507806"""
#
#     class MockResponse:
#
#         def __init__(self, json_data, status_code):
#             self.json_data = json_data
#             self.status_code = status_code
#             self.ok = True
#
#         def json(self):
#             return self.json_data
#
#         def raise_for_status(self):
#             pass
#
#     url = args[0]
#     fname = NON_FICTION if 'nonfiction' in url else FICTION
#     with open(fname) as f:
#         return MockResponse(json.loads(f.read()), 200)
#
#     return MockResponse(None, 404)
#
#
# @patch('requests.get', side_effect=mocked_requests_get)
# def test_response_nonfiction(mock_get):
#     assert get_best_seller_titles(url=URL_NON_FICTION) == [
#         ('BETWEEN THE WORLD AND ME', 86),
#         ('EDUCATED', 79),
#         ('BECOMING', 41),
#         ('THE SECOND MOUNTAIN', 18),
#         ('THE PIONEERS', 16),
#         ('MAYBE YOU SHOULD TALK TO SOMEONE', 14),
#         ('UNFREEDOM OF THE PRESS', 14),
#         ('RANGE', 9),
#         ('THREE WOMEN', 7),
#         ('TRICK MIRROR', 3),
#         ('HOW TO BE AN ANTIRACIST', 2),
#         ('KOCHLAND', 2),
#         ('THANK YOU FOR MY SERVICE', 1),
#         ('THE OUTLAW OCEAN', 1),
#         ('GODS OF THE UPPER AIR', 1)
#     ]
#
#
# @patch('requests.get', side_effect=mocked_requests_get)
# def test_response_fiction(mock_get):
#     assert get_best_seller_titles(url=URL_FICTION) == [
#         ('WHERE THE CRAWDADS SING', 51),
#         ('THE SILENT PATIENT', 25),
#         ('EVVIE DRAKE STARTS OVER', 7),
#         ('THE NICKEL BOYS', 6),
#         ('ASK AGAIN, YES', 6),
#         ('ONE GOOD DEED', 5),
#         ('THE INN', 3),
#         ('THE TURN OF THE KEY', 3),
#         ('OUTFOX', 3),
#         ('THE BITTERROOTS', 2),
#         ('INLAND', 2),
#         ('OLD BONES', 1),
#         ('THE LAST WIDOW', 1),
#         ('THE WHISPER MAN', 1),
#         ('TIDELANDS', 1)
#     ]
#
#
#
# import types
#
# from wc import group
#
#
# def test_split_10_ints_by_3():
#     iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     n = 3
#     actual = group(iterable, n)
#     expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
#     assert actual == expected
#
#
# def test_passing_in_tuple():
#     iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     n = 3
#     actual = group(iterable, n)
#     expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
#     assert actual == expected
#
#
# def test_passing_in_generator():
#     iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     gen = (i for i in iterable)
#     assert isinstance(gen, types.GeneratorType)
#     n = 3
#     actual = group(gen, n)
#     expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     assert actual == expected
#
#
# def test_different_iterable_size():
#     iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
#     n = 3
#     actual = group(iterable, n)
#     expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2],
#                 [3, 4, 5], [6, 7, 8], [9, 10]]
#     assert actual == expected
#
#
# def test_different_n():
#     iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
#     n = 5
#     actual = group(iterable, n)
#     expected = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
#                 [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#     assert actual == expected
#
# import pytest
#
# from wc import get_octal_from_file_permission
#
#
# @pytest.mark.parametrize("input_arg, expected", [
#     ('-----x-w-', '012'), ('-----x-wx', '013'), ('-----xr--', '014'),
#     ('-----xr-x', '015'), ('-----xrw-', '016'), ('-----xrwx', '017'),
#     ('----w--wx', '023'), ('----w-r--', '024'), ('----w-r-x', '025'),
#     ('----w-rw-', '026'), ('----w-rwx', '027'), ('----wxr--', '034'),
#     ('----wxr-x', '035'), ('----wxrw-', '036'), ('----wxrwx', '037'),
#     ('---r--r-x', '045'), ('---r--rw-', '046'), ('---r--rwx', '047'),
#     ('---r-xrw-', '056'), ('---r-xrwx', '057'), ('---rw-rwx', '067'),
#     ('--x-w--wx', '123'), ('--x-w-r--', '124'), ('--x-w-r-x', '125'),
#     ('--x-w-rw-', '126'), ('--x-w-rwx', '127'), ('--x-wxr--', '134'),
#     ('--x-wxr-x', '135'), ('--x-wxrw-', '136'), ('--x-wxrwx', '137'),
#     ('--xr--r-x', '145'), ('--xr--rw-', '146'), ('--xr--rwx', '147'),
#     ('--xr-xrw-', '156'), ('--xr-xrwx', '157'), ('--xrw-rwx', '167'),
#     ('-w--wxr--', '234'), ('-w--wxr-x', '235'), ('-w--wxrw-', '236'),
#     ('-w--wxrwx', '237'), ('-w-r--r-x', '245'), ('-w-r--rw-', '246'),
#     ('-w-r--rwx', '247'), ('-w-r-xrw-', '256'), ('-w-r-xrwx', '257'),
#     ('-w-rw-rwx', '267'), ('-wxr--r-x', '345'), ('-wxr--rw-', '346'),
#     ('-wxr--rwx', '347'), ('-wxr-xrw-', '356'), ('-wxr-xrwx', '357'),
#     ('-wxrw-rwx', '367'), ('r--r-xrw-', '456'), ('r--r-xrwx', '457'),
#     ('r--rw-rwx', '467'), ('r-xrw-rwx', '567'),
# ])
# def test_octal_results_for_different_rwx_combinations(input_arg, expected):
#     assert get_octal_from_file_permission(input_arg) == expected
#
# from wc import get_top_titles, Entry
#
# homepage = ("https://bites-data.s3.us-east-2.amazonaws.com/"
#             "news.python.sc/index.html")
# page2 = ("https://bites-data.s3.us-east-2.amazonaws.com/"
#          "news.python.sc/index2.html")
#
#
# def test_homepage():
#     actual = get_top_titles(homepage)
#     expected = [
#         Entry(title='How do you set up your Python development environment?',
#               points=15, comments=8),
#         Entry(title='Python alternative to Docker (www.mattlayman.com)',
#               points=9, comments=4),
#         Entry(title='Debugging Python programs (stribny.name)',
#               points=9, comments=3),
#         Entry(title='New features planned for Python 4.0 (charlesleifer.com)',
#               points=9, comments=2),
#         Entry(title='Python 3.8 is out (www.python.org)',
#               points=9, comments=0),
#     ]
#     assert actual == expected
#
#
# def test_page2():
#     actual = get_top_titles(page2, top=2)
#     expected = [
#         Entry(title='Django REST Framework - Typed Views (github.com)',
#               points=4, comments=0),
#         Entry(title=('Show 🐍: A news aggregator for the Python community '
#                      'written in Python/Django (github.com)'),
#               points=3, comments=1),
#     ]
#     assert actual == expected
#
# import csv
# from json.decoder import JSONDecodeError
# from urllib.request import urlretrieve
#
# import pytest
#
# from wc import convert_to_csv, EXCEPTION, TMP
#
# mount_data = (
#     'https://bites-data.s3.us-east-2.amazonaws.com/'
#     'mount-data{}.json'
# )
#
# mount1_expected = [
#     ['creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
#      'itemId', 'name', 'qualityId', 'spellId'],
#     ['32158', 'ability_mount_drake_blue', 'False', 'True', 'True', 'False',
#      '44178', 'Albino Drake', '4', '60025'],
#     ['63502', 'ability_mount_hordescorpionamber', 'True', 'False', 'True',
#      'True', '85262', 'Amber Scorpion', '4', '123886'],
#     ['24487', 'ability_mount_warhippogryph', 'False', 'True', 'True', 'False',
#      '45725', 'Argent Hippogryph', '4', '232412'],
# ]
#
# mount2_expected = [
#     ['creatureId', 'icon', 'isAquatic', 'isFlying', 'isGround', 'isJumping',
#      'itemId', 'name', 'qualityId', 'spellId'],
#     ['71381', 'ability_mount_dragonhawkarmorallliance', 'False', 'True',
#      'True', 'False', '98259', 'Armored Blue Dragonhawk', '4', '142478'],
#     ['304', 'spell_nature_swiftness', 'True', 'False', 'True', 'True', '0',
#      'Felsteed', '1', '5784'],
#     ['119386', 'inv_warlockmount', 'False', 'True', 'True', 'False', '0',
#      "Netherlord's Chaotic Wrathsteed", '1', '232412'],
# ]
#
#
# @pytest.mark.parametrize("file_no, expected, exception", [
#     (1, mount1_expected, False),
#     (2, mount2_expected, False),
#     (3, None, True),
# ])
# def test_json2csv(file_no, expected, exception, capfd):
#     mount_json = TMP / f'mount{file_no}.json'
#     mount_csv = TMP / f'mount{file_no}.csv'
#
#     urlretrieve(mount_data.format(file_no), mount_json)
#
#     if exception:
#         with pytest.raises(JSONDecodeError) as exc:
#             convert_to_csv(mount_json)
#             assert 'Invalid control character' in str(exc)
#
#         # testing you actually caught the exception!
#         output = capfd.readouterr()[0].strip()
#         assert output == EXCEPTION
#         return
#
#     convert_to_csv(mount_json)
#     with open(mount_csv) as csv_file:
#         actual = list(csv.reader(csv_file))
#         assert actual == expected
#
# import pytest
#
# from wc import create_gravatar_url
#
# BASE_URL = "https://www.gravatar.com/avatar/"
# HASHED_INFO_EMAIL = "ff2de96de035e1ccdb39ca31d3fe4a5c"
# HASHED_SUPPORT_EMAIL = "1c888a408baa7a685c7c06155e48de84"
# SIZE, DEFAULT = 200, 'robohash'
#
# EXPECTED = iter([  # make an iterator
#     f'{BASE_URL}{HASHED_INFO_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
#     f'{BASE_URL}{HASHED_INFO_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
#     f'{BASE_URL}{HASHED_INFO_EMAIL}?s=40&r=g&d={DEFAULT}',
#     f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
#     f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s={SIZE}&r=g&d={DEFAULT}',
#     f'{BASE_URL}{HASHED_SUPPORT_EMAIL}?s=1000&r=g&d={DEFAULT}',
# ])
#
#
# @pytest.mark.parametrize("email, size", [
#     ("info@pybit.es", 200),
#     ("info@pybit.es ", 200),
#     ('info@pybit.ES', 40),
#     ('support@pybit.es', 200),
#     ('support@PYBIT.es', 200),
#     (' support@pybit.es', 1000),
# ])
# def test_gravatar(email, size):
#     actual = create_gravatar_url(email, size=size)
#     expected = next(EXPECTED)
#     assert actual == expected
#
# import pytest
#
# from wc import Thumbs
#
#
# @pytest.fixture(scope="module")
# def thumbs():
#     return Thumbs()
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (-10, "👎 (10x)"),
#     (-9, "👎 (9x)"),
#     (-8, "👎 (8x)"),
#     (-7, "👎 (7x)"),
#     (-6, "👎 (6x)"),
#     (-5, "👎 (5x)"),
#     (-4, "👎 (4x)"),
#     (-3, "👎👎👎"),
#     (-2, "👎👎"),
#     (-1, "👎"),
#     (1, "👍"),
#     (2, "👍👍"),
#     (3, "👍👍👍"),
#     (4, "👍 (4x)"),
#     (5, "👍 (5x)"),
#     (6, "👍 (6x)"),
#     (7, "👍 (7x)"),
#     (8, "👍 (8x)"),
#     (9, "👍 (9x)"),
#     (10, "👍 (10x)"),
# ])
# def test_operator_overloading_works_both_ways(arg, expected, thumbs):
#     assert thumbs * arg == arg * thumbs == expected
#
#
# def test_exception(thumbs):
#     with pytest.raises(ValueError):
#         thumbs * 0
#     with pytest.raises(ValueError):
#         0 * thumbs
#
# from wc import gold_prices, years_gold_value_decreased
#
#
# def test_gold_prices_full_data_set():
#     actual = years_gold_value_decreased()
#     expected = (2013, 2009)
#     assert actual == expected
#
#
# def test_gold_prices_1950_1999():
#     data = '\n'.join(gold_prices.strip().splitlines()[:10])
#     actual = years_gold_value_decreased(data)
#     expected = (1981, 1979)
#     assert actual == expected
#
#
# def test_gold_prices_till_1980_1989():
#     data = '\n'.join(gold_prices.strip().splitlines()[-8:-6])
#     actual = years_gold_value_decreased(data)
#     expected = (1981, 1987)
#     assert actual == expected
#
# from pathlib import Path
# import re
# from time import sleep
# from zipfile import ZipFile
#
# from wc import zip_last_n_files, ZIP_FILE, TMP
#
# LOG_DIR = TMP / 'logs'
#
#
# def test_zip_3_last_files(tmp_path):
#     log_dir = tmp_path / "logs"
#     log_dir.mkdir()
#     for i in range(1, 10, 2):
#         sleep(0.01)
#         p = log_dir / f"{i}.log"
#         p.write_text('log line')
#     zip_file = tmp_path / ZIP_FILE
#     zip_last_n_files(directory=log_dir, zip_file=zip_file)
#     zip_ = ZipFile(zip_file)
#     files = sorted(zip_.namelist())
#     assert len(files) == 3
#     f1, f2, f3 = files
#     assert re.match(r'^5_\d{4}-\d{2}-\d{2}.log$', f1)
#     assert re.match(r'^7_\d{4}-\d{2}-\d{2}.log$', f2)
#     assert re.match(r'^9_\d{4}-\d{2}-\d{2}.log$', f3)
#
#
# def test_zip_2_last_files(tmp_path):
#     log_dir = tmp_path / "logs2"
#     log_dir.mkdir()
#     for i in range(20, 6, -3):
#         sleep(0.01)
#         p = log_dir / f"{i}.log"
#         p.write_text('log line')
#     zip_file = tmp_path / ZIP_FILE
#     zip_last_n_files(directory=log_dir, zip_file=zip_file, n=2)
#     zip_ = ZipFile(zip_file)
#     files = sorted(zip_.namelist())
#     assert len(files) == 2
#     f1, f2 = files
#     assert re.match(r'^11_\d{4}-\d{2}-\d{2}.log$', f1)
#     assert re.match(r'^8_\d{4}-\d{2}-\d{2}.log$', f2)
#
# import pytest
#
# from wc import capitalize_sentences
#
# lorem_ipsum = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor!
# Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat?
# Sed viverra tellus in hac habitasse platea dictumst vestibulum.
# Morbi tempus iaculis urna id volutpat.
# Enim blandit volutpat maecenas volutpat.
# Morbi tristique senectus et netus!
# Massa tincidunt nunc pulvinar sapien?
# Nunc aliquet bibendum enim facilisis gravida neque convallis a.
# Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.
# Id diam maecenas ultricies mi eget mauris?
# Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare!
# Gravida in fermentum et sollicitudin ac orci phasellus!
# Ut diam quam nulla porttitor massa id neque aliquam.
# Sit amet dictum sit amet justo donec enim diam vulputate.
# Risus sed vulputate odio ut?
# Justo eget magna fermentum iaculis eu non!
# At auctor urna nunc id.
# At erat pellentesque adipiscing commodo elit at imperdiet!
# Molestie nunc non blandit massa enim nec dui?
# Lorem donec massa sapien faucibus et molestie ac feugiat.
# """.strip().splitlines()
# text1, text2, text3 = lorem_ipsum[:5], lorem_ipsum[5:13], lorem_ipsum[13:]
#
#
# @pytest.mark.parametrize("text", [
#     text1, text2, text3
# ])
# def test_capitalize_sentences(text):
#     expected = " ".join(text)
#     arg = expected.lower()
#     assert capitalize_sentences(arg) == expected
#
# import pytest
#
# from wc import timings_log, get_bite_with_fastest_avg_test
#
#
# @pytest.fixture(scope='module')
# def timings():
#     with open(timings_log) as f:
#         return f.readlines()
#
#
# @pytest.mark.parametrize("rows, expected_bites", [
#     (50, '121'),
#     (100, '169'),
#     (150, '169'),
#     (200, '46'),
#     (250, ('60', '87')),
# ])
# def test_get_bite_with_fastest_avg_test(rows, expected_bites, timings):
#     actual = str(get_bite_with_fastest_avg_test(timings[:rows]))
#     if type(expected_bites) == tuple:
#         assert actual in expected_bites
#     else:
#         assert actual == expected_bites
#
# import pytest
#
# from wc import get_matching_files
#
# FILES = ('bite.html commands.sh out_grepped pytest_testrun.out '
#          'pytest_timings.out test_timings.py timings-template.py '
#          'timings.py').split()
#
#
# @pytest.mark.parametrize("filter_str, expected", [
#    ('bite1', ['bite1']),
#    ('Bite', ['bite1']),
#    ('pybites', ['bite1']),
#    ('test', ['test']),
#    ('test2', ['test']),
#    ('output', ['output']),
#    ('o$tput', ['output']),
#    ('nonsense', []),
# ])
# def test_example_docstring(tmp_path, filter_str, expected):
#     # let's create some files in tmp
#     for fi in 'bite1 test output'.split():
#         open(tmp_path / fi, 'a').close()
#     actual = get_matching_files(tmp_path, filter_str)
#     assert sorted(actual) == sorted(expected)
#
#
# @pytest.mark.parametrize("filter_str, expected", [
#    ('bite.html', ['bite.html']),
#    ('bite.htm1', ['bite.html']),
#    ('bit$.htm1', ['bite.html']),
#    ('bite.txt', ['bite.html']),
#    ('_timing', ['timings.py', 'test_timings.py']),
#    ('commando', ['commands.sh']),
#    ('pytest_testruns.out', ['pytest_testrun.out', 'pytest_timings.out']),
#    ('out_greped', ['out_grepped']),
#    ('nonsensical', []),
#    ('commands.py', ['commands.sh']),
#    ('pytest_t', ['pytest_testrun.out', 'pytest_timings.out']),
#    ('timings-templates.PY', ['timings-template.py']),
# ])
# def test_other_files(tmp_path, filter_str, expected):
#     # let's create some files in tmp
#     for fi in FILES:
#         open(tmp_path / fi, 'a').close()
#     actual = get_matching_files(tmp_path, filter_str)
#     assert sorted(actual) == sorted(expected)
#
# from wc import fizzbuzz
# import pytest
#
# # write one or more pytest functions below, they need to start with test_
#
# @pytest.mark.parametrize('num, output',[(1,1), (2,2),(3,'Fizz'),(5,'Buzz'), (15,'Fizz Buzz')])
# def test_fizzbuzz(num, output):
#     assert fizzbuzz(num)==output
#
# import os
# from pathlib import Path
# from ipaddress import IPv4Network
# from urllib.request import urlretrieve
#
# import pytest
#
# from wc import (ServiceIPRange, parse_ipv4_service_ranges,
#                  get_aws_service_range)
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
# TMP = os.getenv("TMP", "/tmp")
# PATH = Path(TMP, "ip-ranges.json")
# IP = IPv4Network('192.0.2.8/29')
#
#
# @pytest.fixture(scope='module')
# def json_file():
#     """Import data into tmp folder"""
#     urlretrieve(URL, PATH)
#     return PATH
#
#
# # write your pytest code ...
# def test_parse_ipv4_service_ranges(json_file):
#     addresses = parse_ipv4_service_ranges(PATH)
#     assert len(addresses) == 1886
#
#
# def test_get_aws_service_range(json_file):
#     addresses = parse_ipv4_service_ranges(PATH)
#     assert len(addresses) == 1886
#     service_range = get_aws_service_range('13.248.118.0', addresses)
#     assert len(service_range) == 2
#
# def test_ServiceIPRange_str(json_file):
#     addresses = parse_ipv4_service_ranges(PATH)
#     address_str = str(addresses[0])
#     assert address_str == '13.248.118.0/24 is allocated to the AMAZON service in the eu-west-1 region'
#
# import os
# from pathlib import Path
# from ipaddress import IPv4Network
# from urllib.request import urlretrieve
#
# import pytest
#
# from ips import (ServiceIPRange, parse_ipv4_service_ranges,
#                  get_aws_service_range)
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
# TMP = os.getenv("TMP", "/tmp")
# PATH = Path(TMP, "ip-ranges.json")
# IP = IPv4Network('192.0.2.8/29')
#
#
# @pytest.fixture(scope='module')
# def json_file():
#     """Import data into tmp folder"""
#     urlretrieve(URL, PATH)
#     return PATH
#
#
# def test_dataclass():
#     expected = ("192.0.2.8/29 is allocated to the pybites service "
#                 "in the US region")
#     assert str(ServiceIPRange('pybites', 'US', IP)) == expected
#
#
# def test_parse_ranges(json_file):
#     out = parse_ipv4_service_ranges(json_file)
#     assert len(out) == 1886
#
#     assert type(out) == list
#     assert all(type(element) == ServiceIPRange for element in out)
#     assert str(out[0]) == ("13.248.118.0/24 is allocated to the AMAZON "
#                            "service in the eu-west-1 region")
#
#
# def test_get_aws_service_range_zero_hits(json_file):
#     assert get_aws_service_range('13.248.118.0', []) == []
#
#
# def test_get_aws_service_range_two_hits(json_file):
#     service_range = parse_ipv4_service_ranges(json_file)
#     expected = [
#         ServiceIPRange(service='AMAZON', region='eu-west-1',
#                        cidr=IPv4Network('13.248.118.0/24')),
#         ServiceIPRange(service='GLOBALACCELERATOR', region='eu-west-1',
#                        cidr=IPv4Network('13.248.118.0/24'))
#     ]
#     assert get_aws_service_range('13.248.118.0', service_range) == expected
#
#
# def test_get_aws_service_range_exception(json_file):
#     with pytest.raises(ValueError) as exc:
#         get_aws_service_range('nonsense', {})
#     assert str(exc.value) == "Address must be a valid IPv4 address"
#
# import pytest
#
# from wc import filter_killed_mutants, _get_data
#
# EXPECTED_OUTPUT = """
# [*] Start mutation process:
#    - targets: account
#    - tests: /tmp/test_account.py
# [*] 9 tests passed:
#    - test_account [0.12459 s]
# [*] Start mutants generation and execution:
#    - [#   1] AOR account:
# [0.12042 s] killed by test_account.py::test_balance
#    - [#   2] AOR account:
# [0.10003 s] killed by test_account.py::test_merge_account
#    - [#   3] AOR account:
# [0.10011 s] incompetent
#    - [#   4] COD account:
# [0.11709 s] killed by test_account.py::test_balance
#    - [#   5] COI account:
# [0.11089 s] killed by test_account.py::test_balance
#    - [#   6] CRP account:
# [0.09470 s] killed by test_account.py::test_balance
#    - [#   7] CRP account:
# [0.09643 s] killed by test_account.py::test_repr
#    - [#   8] CRP account:
# [0.09736 s] killed by test_account.py::test_repr
#    - [#   9] CRP account:
# [0.09909 s] killed by test_account.py::test_str
#    - [#  10] CRP account:
# [0.09923 s] killed by test_account.py::test_str
#    - [#  11] CRP account:
# --------------------------------------------------------------------------------
#   20:             self.amount)
#   21:
#   22:     def add_transaction(self, amount):
#   23:         if not (isinstance(amount, int)):
# - 24:             raise ValueError('please use int for amount')
# + 24:             raise ValueError('mutpy')
#   25:         self._transactions.append(amount)
#   26:
#   27:     @property
#   28:     def balance(self):
# --------------------------------------------------------------------------------
# [0.09799 s] survived
#    - [#  12] CRP account:
# --------------------------------------------------------------------------------
#   20:             self.amount)
#   21:
#   22:     def add_transaction(self, amount):
#   23:         if not (isinstance(amount, int)):
# - 24:             raise ValueError('please use int for amount')
# + 24:             raise ValueError('')
#   25:         self._transactions.append(amount)
#   26:
#   27:     @property
#   28:     def balance(self):
# --------------------------------------------------------------------------------
# [0.09931 s] survived
#    - [#  13] CRP account:
# [0.10067 s] killed by test_account.py::test_merge_account
#    - [#  14] CRP account:
# [0.10083 s] killed by test_account.py::test_merge_account
#    - [#  15] DDL account:
# [0.10240 s] killed by test_account.py::test_balance
#    - [#  16] ROR account:
# [0.09937 s] killed by test_account.py::test_comparison
#    - [#  17] ROR account:
# [0.09987 s] killed by test_account.py::test_comparison
#    - [#  18] ROR account:
# --------------------------------------------------------------------------------
#   37:     def __eq__(self, other):
#   38:         return self.balance == other.balance
#   39:
#   40:     def __lt__(self, other):
# - 41:         return self.balance < other.balance
# + 41:         return self.balance <= other.balance
#   42:
#   43:     def __add__(self, other):
#   44:         owner = '{}&{}'.format(self.owner, other.owner)
#   45:         start_amount = self.amount + other.amount
# --------------------------------------------------------------------------------
# [0.10084 s] survived
# [*] Mutation score [7.08526 s]: 82.4%
#    - all: 18
#    - killed: 14 (77.8%)
#    - survived: 3 (16.7%)
#    - incompetent: 1 (5.6%)
#    - timeout: 0 (0.0%)
# [*] Coverage: 240 of 240 AST nodes (100.0%)
# """
# EXPECTED_OUTPUT_WITH_GAP = """
# [*] Start mutation process:
#    - targets: account
#    - tests: /tmp/test_account.py
# [*] 9 tests passed:
#    - test_account [0.12459 s]
# [*] Start mutants generation and execution:
#    - [#   1] AOR account:
# [0.12042 s] killed by test_account.py::test_balance
#    - [#   2] AOR account:
# [0.10003 s] killed by test_account.py::test_merge_account
#    - [#   3] AOR account:
# [0.10011 s] incompetent
#    - [#   4] COD account:
# [0.11709 s] killed by test_account.py::test_balance
#    - [#   5] COI account:
# [0.11089 s] killed by test_account.py::test_balance
#    - [#   6] CRP account:
# [0.09470 s] killed by test_account.py::test_balance
#    - [#   7] CRP account:
# [0.09643 s] killed by test_account.py::test_repr
#    - [#   8] CRP account:
# [0.09736 s] killed by test_account.py::test_repr
#    - [#   9] CRP account:
# [0.09909 s] killed by test_account.py::test_str
#    - [#  12] CRP account:
# --------------------------------------------------------------------------------
#   20:             self.amount)
#   21:
#   22:     def add_transaction(self, amount):
#   23:         if not (isinstance(amount, int)):
# - 24:             raise ValueError('please use int for amount')
# + 24:             raise ValueError('')
#   25:         self._transactions.append(amount)
#   26:
#   27:     @property
#   28:     def balance(self):
# --------------------------------------------------------------------------------
# [0.09931 s] survived
#    - [#  13] CRP account:
# [0.10067 s] killed by test_account.py::test_merge_account
#    - [#  14] CRP account:
# [0.10083 s] killed by test_account.py::test_merge_account
#    - [#  15] DDL account:
# [0.10240 s] killed by test_account.py::test_balance
#    - [#  16] ROR account:
# [0.09937 s] killed by test_account.py::test_comparison
#    - [#  17] ROR account:
# [0.09987 s] killed by test_account.py::test_comparison
#    - [#  18] ROR account:
# --------------------------------------------------------------------------------
#   37:     def __eq__(self, other):
#   38:         return self.balance == other.balance
#   39:
#   40:     def __lt__(self, other):
# - 41:         return self.balance < other.balance
# + 41:         return self.balance <= other.balance
#   42:
#   43:     def __add__(self, other):
#   44:         owner = '{}&{}'.format(self.owner, other.owner)
#   45:         start_amount = self.amount + other.amount
# --------------------------------------------------------------------------------
# [0.10084 s] survived
# [*] Mutation score [7.08526 s]: 82.4%
#    - all: 18
#    - killed: 14 (77.8%)
#    - survived: 3 (16.7%)
#    - incompetent: 1 (5.6%)
#    - timeout: 0 (0.0%)
# [*] Coverage: 240 of 240 AST nodes (100.0%)
# """
#
#
# @pytest.fixture(scope='module')
# def actual():
#     return [line.rstrip() for line in filter_killed_mutants()]
#
#
# @pytest.fixture(scope='module')
# def actual2():
#     """Same output but filter out test 10 (killed) and 11 (survived),
#        to avoid the hardcoded output gets returned from function
#     """
#     mutpy_output = _get_data()
#     test10 = mutpy_output.index('   - [#  10] CRP account:')
#     test12 = mutpy_output.index('   - [#  12] CRP account:')
#     output = mutpy_output[:test10] + mutpy_output[test12:]
#     return [line.rstrip() for line in filter_killed_mutants(output)]
#
#
# def test_output_matches(actual):
#     expected = [line.rstrip() for line in
#                 EXPECTED_OUTPUT.strip().splitlines()]
#     assert actual == expected
#
#
# def test_different_output(actual2):
#     expected = [line.rstrip() for line in
#                 EXPECTED_OUTPUT_WITH_GAP.strip().splitlines()]
#     assert actual2 == expected
#
# import pytest
#
# from wc import generate_improved_xmas_tree
#
# default_tree = """
#          +
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
#     |||||||||||
#     |||||||||||
# """
# smaller_tree = """
#   +
#   *
#  ***
# *****
#  |||
#  |||
# """
#
#
# @pytest.mark.parametrize("size, expected", [(10, 13), (5, 8), (20, 23)])
# def test_height_xmas_tree(size, expected):
#     actual = len(generate_improved_xmas_tree(size).rstrip().splitlines())
#     assert actual == expected
#
#
# @pytest.mark.parametrize("size, expected", [(3, 9), (5, 25), (20, 400)])
# def test_num_leafs_used(size, expected):
#     assert generate_improved_xmas_tree(size).count("*") == expected
#
#
# @pytest.mark.parametrize("size, expected", [(3, 1), (5, 1), (20, 1)])
# def test_star_used(size, expected):
#     assert generate_improved_xmas_tree(size).count("+") == expected
#
#
# @pytest.mark.parametrize("size, expected", [(3, 6), (5, 10), (20, 42)])
# def test_trunk_used(size, expected):
#     assert generate_improved_xmas_tree(size).count("|") == expected
#
#
# def test_outputs():
#     actual_tree = generate_improved_xmas_tree().strip("\n").split("\n")
#     expected_tree = default_tree.strip("\n").split("\n")
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()
#
#     actual_tree = generate_improved_xmas_tree(3).strip("\n").split("\n")
#     expected_tree = smaller_tree.strip("\n").split("\n")
#     for i, j in zip(actual_tree, expected_tree):
#         assert i.rstrip() == j.rstrip()
#
# from unittest.mock import patch
#
# import pytest
# from more_itertools.more import side_effect
#
# import wc
#
#
# @pytest.fixture(scope="module")
# def gen():
#     return wc.gen_hex_color()
#
# @patch('wc.gen_hex_color')
# def test_gen_hex_color(gen):
#     str1 = gen()
#     assert next(gen) == '#1588DD'


#
# import pytest
# from wc import square

#
# def test_always_positive():
#     assert True
#
# def test_always_negative():
#     assert False
#
#
# # Testing.
# print(square(3))
# #

# Test function
# def test_square():
#     assert square(4)==16


# Test parameterized

# Test fixture
# load a dictionary
#
# @pytest.fixture()
# def load_my_dict():
#     return {'a':1, 'b':2}
#
# def test_dict(load_my_dict):
#     a = load_my_dict
#     print("hello")

# set up a fixture
#
# @pytest.fixture
# def set_up_dict():
#     return {1:2, 2:3}
#
#
# def test_dict(set_up_dict):
#     assert set_up_dict[1]==2
#
# # set up a parameterized query:
#
# def add_2(x):
#     return x + 2
# #
# @pytest.mark.parametrize('x,ans',[(1,3),(2,4),(3,5)])
# def test_add_2(x,ans):
#     assert add_2(x)==ans

# Can I combine a fixture and parameterization?
#
# @pytest.mark.parametrize('arg, result',[(1,6),(2,8)])
# def test_add2_fix(arg, result, set_up_dict):
#     assert add_2(arg)*set_up_dict[1]==result

#
# from unittest.mock import patch
#
# def get_data():
#     return 9
#
# @patch('my_test.get_data')
# def test_patch(mock_obj):
#     mock_obj.return_value=4
#     assert get_data()==mock_obj()
#
# from unittest.mock import patch
#
# # patch the function
# def square(x):
#     return x*x
#
# def sum_square(x,y):
#     return x + square(y)
#
# @patch('my_test.square')
# def test_sum_square(mock_obj):
#     mock_obj.return_value=5
#     z = sum_square(1,2)
#     print(z)
#     assert z==5
# from unittest.mock import patch
#
# import pytest
# import wc
#
#
# @pytest.fixture(scope="module")
# def gen():
#     return wc.gen_hex_color()
#
# @patch('wc.sample')
# def test_gen_hex_color(mock_obj,gen):
#     mock_obj.return_value=(0,0,0)
#     a = next(gen)
#     assert a=='#000000'
#
# import string
#
# import pytest
# import pandas as pd
#
# import wc as se
#
# file_name = "https://bites-data.s3.us-east-2.amazonaws.com/iris.csv"
# df = pd.read_csv(file_name)
#
#
# @pytest.fixture()
# def sepal_length_series():
#     """Returns the Sepal Length Series from the Iris DataFrame"""
#     return df.sepal_length.sort_values().reset_index(drop=True)
#
#
# @pytest.fixture()
# def int_series_vsmall():
#     """Returns a pandas Series containing ints"""
#     return pd.Series(range(1, 6))
#
#
# @pytest.fixture()
# def int_series_small():
#     """Returns a pandas Series containing ints"""
#     return pd.Series(range(10))
#
#
# @pytest.fixture()
# def int_series_vsmall_offset_index():
#     """Returns a pandas Series containing ints"""
#     return pd.Series(range(0, 10, 2), index=range(0, 10, 2))
#
#
# @pytest.fixture()
# def letters_series():
#     """Returns a pandas Series containing all lower case letters"""
#     return pd.Series(list(string.ascii_lowercase))
#
#
# @pytest.mark.parametrize(
#     "arg, expected",
#     [
#         (("add", 5), [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
#         (("add", 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         (("add", -15), [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6]),
#         (("sub", 5), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]),
#         (("sub", 0), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         (("sub", -15), [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
#         (("mul", 5), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]),
#         (("mul", 0), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
#         (("mul", -15), [0, -15, -30, -45, -60, -75, -90, -105, -120, -135]),
#         (("div", 5), [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8]),
#         (("div", -5), [-0.0, -0.2, -0.4, -0.6, -0.8, -1.0,
#                        -1.2, -1.4, -1.6, -1.8]),
#     ],
# )
# def test_series_simple_math(int_series_small, arg, expected):
#     assert all(
#         expected[idx] == val
#         for idx, val in enumerate(
#             se.series_simple_math(int_series_small, arg[0], arg[1])
#         )
#     )
#
#
# @pytest.mark.parametrize(
#     "arg, expected",
#     [
#         ("add", [1.0, "nan", 5.0, "nan", 9.0, "nan", "nan"]),
#         ("sub", [1.0, "nan", 1.0, "nan", 1.0, "nan", "nan"]),
#         ("mul", [0.0, "nan", 6.0, "nan", 20.0, "nan", "nan"]),
#         ("div", ["inf", "nan", 1.5, "nan", 1.25, "nan", "nan"]),
#     ],
# )
# def test_complex_series_maths(
#     int_series_vsmall, int_series_vsmall_offset_index, arg, expected
# ):
#     result = se.complex_series_maths(
#         int_series_vsmall, int_series_vsmall_offset_index, arg
#     )
#     result = ",".join(str(n) for n in result)
#     expected = ",".join(str(n) for n in expected)
#     assert result == expected
#
#
# @pytest.mark.parametrize(
#     "arg, expected",
#     [
#         (
#             ["a", "e", "i", "o", "u"],
#             [
#                 True,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#             ],
#         ),
#         (
#             ["j", "k", "q", "x", "z"],
#             [
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 True,
#                 True,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 False,
#                 True,
#                 False,
#                 True,
#             ],
#         ),
#     ],
# )
# def test_create_series_mask(letters_series, arg, expected):
#     result = se.create_series_mask(letters_series, arg)
#     assert all([result[idx] == exp for idx, exp in enumerate(expected)])
#     assert all(l in arg for l in letters_series[result])
#
#
# def test_custom_series_function(sepal_length_series):
#     result = se.custom_series_function(sepal_length_series, 0.1)
#     assert len(result) == 51
#     assert round(result.mean(), 4) == 5.6725
#     assert max(result.index) == 149 and max(result.values) == 7.9
#     assert min(result.index) == 0 and min(result.values) == 4.3
#     assert result[82] == 5.9
#     assert result.iloc[10] == 5.0
#     assert result.iloc[11] == 5.1
#     assert result.iloc[20] == 5.7
#     assert result.iloc[37] == 5.9
#     assert result.iloc[38] == 6.4
#
# import re
# import pytest
# import wc
#
# EXPECTED = """
# |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |
# ---------------------------------------------------------------------------------------------------------
# |  UUU:  F   32.7  26200  |  UCU:  S   12.9  10309  |  UAU:  Y   30.4  24332  |  UGU:  C    4.9   3919  |
# |  UUC:  F   12.1   9716  |  UCC:  S    1.6   1310  |  UAC:  Y    8.6   6887  |  UGC:  C    1.2    992  |
# |  UUA:  L   53.8  43053  |  UCA:  S   20.3  16267  |  UAA:  *    2.4   1909  |  UGA:  *    0.4    299  |
# |  UUG:  L   13.5  10801  |  UCG:  S    4.0   3172  |  UAG:  *    0.5    405  |  UGG:  W    7.6   6055  |
# ---------------------------------------------------------------------------------------------------------
# |  CUU:  L   10.6   8462  |  CCU:  P   10.8   8642  |  CAU:  H   18.2  14550  |  CGU:  R   13.2  10569  |
# |  CUC:  L    1.9   1560  |  CCC:  P    1.0    773  |  CAC:  H    4.5   3625  |  CGC:  R    3.1   2512  |
# |  CUA:  L    8.5   6808  |  CCA:  P   16.3  13009  |  CAA:  Q   36.3  29048  |  CGA:  R    4.9   3914  |
# |  CUG:  L    2.3   1826  |  CCG:  P    4.1   3262  |  CAG:  Q    5.0   3977  |  CGG:  R    0.4    348  |
# ---------------------------------------------------------------------------------------------------------
# |  AUU:  I   52.0  41646  |  ACU:  T   16.8  13481  |  AAU:  N   43.0  34398  |  AGU:  S   16.7  13345  |
# |  AUC:  I   14.9  11905  |  ACC:  T    2.6   2077  |  AAC:  N   13.9  11135  |  AGC:  S    5.2   4152  |
# |  AUA:  I   18.8  15063  |  ACA:  T   28.9  23134  |  AAA:  K   61.1  48950  |  AGA:  R   11.7   9372  |
# |  AUG:  M   25.9  20717  |  ACG:  T    9.5   7638  |  AAG:  K   14.3  11428  |  AGG:  R    1.5   1217  |
# ---------------------------------------------------------------------------------------------------------
# |  GUU:  V   27.4  21938  |  GCU:  A   20.4  16291  |  GAU:  D   45.6  36531  |  GGU:  G   32.6  26104  |
# |  GUC:  V    7.3   5873  |  GCC:  A    4.4   3507  |  GAC:  D   12.8  10229  |  GGC:  G    9.4   7525  |
# |  GUA:  V   22.8  18270  |  GCA:  A   29.9  23954  |  GAA:  E   54.6  43675  |  GGA:  G   14.2  11399  |
# |  GUG:  V    9.5   7584  |  GCG:  A    9.4   7550  |  GAG:  E   10.6   8458  |  GGG:  G    4.4   3483  |
# ---------------------------------------------------------------------------------------------------------
# """.strip()  # noqa E501
#
#
# # ############################################################################
# # Helper functions
# # ############################################################################
#
#
# def get_whole_table(table):
#     """
#     Receives a results table
#     Returns all results in a list of lists with whitespace removed
#     """
#     return [
#         entry.strip().split()
#         for line in table.strip().split("\n")
#         for entry in line.split("|")
#         if entry.replace("-", "") != "" and entry.strip() != ""
#     ]
#
#
# def get_field(table, field_number):
#     """
#     Helper function to get a specific field from table
#     Receives a results table
#     Returns a list of queried field
#     """
#     return [entry[field_number] for entry in get_whole_table(table)]
#
#
# def get_codons(table):
#     """
#     Get field "codons" from table
#     Receives a results table
#     Returns a list of queried field
#     """
#     return get_field(table, 0)
#
#
# def get_amino_acids(table):
#     """
#     Get field "amino acids" from table
#     Receives a results table
#     Returns a list of amino acids
#     """
#     return get_field(table, 1)
#
#
# def get_frequencies(table):
#     """
#     Get field "frequencies" from table
#     Receives a results table
#     Returns a list of frequencies
#     """
#     return get_field(table, 2)
#
#
# def get_absolute_numbers(table):
#     """
#     Get field "absolute numbers" from table
#     Receives a results table
#     Returns a list of absolute codon numbers
#     """
#     return get_field(table, 3)
#
#
# def get_table_bars(table):
#     """
#     Receives a results table
#     Returns a list of bars/pipes (|) per line
#     """
#     return [len(re.findall(r"\|", line)) for line in table.split("\n")]
#
#
# def get_table_dividers(table):
#     """
#     Receives a results table
#     Returns a list of divider rows (------)
#     """
#     return [len(re.findall(r"^-{3,}$", line)) for line in table.split("\n")]
#
#
# # ############################################################################
# # Test functions
# # ############################################################################
#
#
# @pytest.fixture(scope="module")
# def result():
#     """
#     Provide codon usage table for tests
#     """
#     return wc.return_codon_usage_table().strip()
#
#
# @pytest.mark.parametrize(
#     "function",
#     [
#         get_table_bars,
#         get_table_dividers,
#         get_codons,
#         get_amino_acids,
#         get_frequencies,
#         get_absolute_numbers,
#         get_whole_table,
#     ],
# )
# def test_table(result, function):
#     """
#     Helper function to run all tests
#     """
#     print(f"Executing function '{function.__name__}'")
#     assert function(result) == function(EXPECTED)
#
# t1 = get_whole_table(EXPECTED)
# codon_order = [c[0][:-1]  for c in t1 if c[0]!='Codon']
# condon_order_str = " ".join(codon_order)
# get_table_bars(EXPECTED)
# get_table_dividers(EXPECTED)
#
# import datetime
#
# import pytest
#
# from wc import (get_pycon_events, filter_pycons,
#                     get_continent)
#
#
# @pytest.fixture(scope="session")
# def pycon_events():
#     events = get_pycon_events()
#     return events
#
#
# @pytest.fixture(scope="session")
# def filtered_pycons(pycon_events):
#     filtered = filter_pycons(pycon_events)
#     return filtered
#
#
# def test_get_pycon_events_number(pycon_events):
#     assert len(pycon_events) == 21
#
#
# def test_get_pycon_events_cities(pycon_events):
#     actual = {event.city for event in pycon_events}
#     expected = {
#         "Accra", "Belgrade", "Berlin",
#         "Bratislava", "Cardiff", "Cleveland, OH", "Dublin",
#         "Florence", "Hyderabad", "Jakarta", "Johannesburg",
#         "Makati", "Munich", "Nairobi", "Odessa",
#         "Ostrava", "Puerto Vallarta", "Sydney",
#         "Taipei", "Toronto",
#     }
#     assert actual == expected
#
#
# def test_get_pycon_events_dates(pycon_events):
#     assert all(
#         isinstance(event.start_date, datetime.datetime)
#         for event in pycon_events
#     )
#     assert all(isinstance(event.end_date, datetime.datetime)
#                for event in pycon_events)
#
#
# def test_filter_pycons_number(filtered_pycons):
#     actual = len(filtered_pycons)
#     expected = 9
#     assert actual == expected
#
#
# def test_filter_pycons_cities(filtered_pycons):
#     actual = {event.city for event in filtered_pycons}
#     expected = {
#         "Belgrade", "Berlin", "Bratislava", "Cardiff",
#         "Dublin", "Florence", "Munich", "Odessa",
#         "Ostrava",
#     }
#     assert actual == expected
#
#
# def test_filter_pycons_dates(filtered_pycons):
#     assert all(
#         isinstance(event.start_date, datetime.datetime)
#         for event in filtered_pycons
#     )
#     assert all(
#         isinstance(event.end_date, datetime.datetime)
#         for event in filtered_pycons
#     )
#
#
# def test_filter_pycons_year(filtered_pycons):
#     actual = {pycon.start_date.year for pycon in filtered_pycons}
#     expected = {2019}
#     assert actual == expected
#
#
# def test_filter_pycons_continent(filtered_pycons):
#     actual = {get_continent(pycon.country) for pycon in filtered_pycons}
#     expected = {"Europe"}
#     assert actual == expected
#
# from wc import XYZ, calculate_flux, identify_flux
#
#
# def test_calculate():
#     calc = calculate_flux(XYZ)
#     assert isinstance(calc, list)
#     assert len(calc) == 11
#     assert len(calc[0]) == 5
#
#     *orig, dol, perc = calc[0]
#     assert orig == ["Cash", 120000, 115000]
#     assert dol == 5000
#     assert round(perc, 2) == 0.04
#
#
# def test_identify():
#     flux = identify_flux(calculate_flux(XYZ))
#     assert isinstance(flux, list)
#     assert len(flux) == 5
#     assert [act for act, *_ in flux] == [
#         "Accounts Receivable",
#         "Inventory",
#         "Notes Receivable",
#         "Accrued Payroll",
#         "Retained Earnings",
#     ]
#
# import pytest
#
# import wc
#
# # Table copied from
# # http://arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.html
# # Note that this table is different from the simple table in the template
# # This table includes additional rules which are used in more advanced
# # reverse complement generators. Please ensure that your functions work
# # with both tables (complementary base always in last column)
#
# COMPLEMENTS_STR = """# Full table with ambigous bases
#  Base	Name	Bases Represented	Complementary Base
#  A	Adenine	A	T
#  T	Thymidine	T 	A
#  U	Uridine(RNA only)	U	A
#  G	Guanidine	G	C
#  C	Cytidine	C	G
#  Y	pYrimidine	C T	R
#  R	puRine	A G	Y
#  S	Strong(3Hbonds)	G C	S
#  W	Weak(2Hbonds)	A T	W
#  K	Keto	T/U G	M
#  M	aMino	A C	K
#  B	not A	C G T	V
#  D	not C	A G T	H
#  H	not G	A C T	D
#  V	not T/U	A C G	B
#  N	Unknown	A C G T	N
# """
#
# # ############################################################################
# # Use default table from bite template and test functions
# # ############################################################################
#
# ACGT_BASES_ONLY = [
#     "ACGT",
#     "TTTAAAGGGCCC",
#     ("TACTGGTACTAATGCCTAAGTGACCGGCAGCAAAATGTTGCAGCACTGACCCTTTTGGGACCGCAATGGGT"
#      "TGAATTAGCGGAACGTCGTGTAGGGGGAAAGCGGTCGACCGCATTATCGCTTCTCCGGGCGTGGCTAGCGG"
#      "GAAGGGTTGTCAACGCGTCGGACTTACCGCTTACCGCGAAACGGACCAAAGGCCGTGGTCTTCGCCACGGC"
#      "CTTTCGACCGACCTCACGCTAGAAGGA"),
# ]
# MIXED_CASE_DNA = [
#     "AcgT",
#     "TTTaaaGGGCCc",
#     ("TACtGGTACTAATGCCtAAGtGaccggcagCAAAATGTTGCAGCACTGACCCTTTTGGGACCGCAATGGGT"
#      "TGAATTAGCGGAACGTCGTGTAGGGGGAAAgcgGTCGACCGCATTATCGCTTCTCCGGGCGTGGCTAGCGG"
#      "GAAGGGTTGTCAACGCGTCGGACTTACCGCttaCCGCGAAACGGAccAAAGGCCGTGGTCTTCGCCACGGC"
#      "CTTtcGACCGACCTCACGCTAGAAGGA"),
# ]
# DIRTY_DNA = [
#     "335>\nA c g T",
#     ">\nT-TT-AAA-  GGGCCC!!!",
#     ("TAC TGG TAC TAA TGC CTA AGT GAC CGG CAG CAA AAT GTT GCA GCA CTG ACC CTT"
#      " TTG GGA CCG CAA TGG GTT GAA TTA GCG GAA CGT CGT GTA GGG GGA AAG CGG TC"
#      "G ACC GCA TTA TCG CTT CTC CGG GCG TGG CTA GCG GGA AGG GTT GTC AAC GCG T"
#      "CG GAC TTA CCG CTT ACC GCG AAA CGG ACC AAA GGC CGT GGT CTT CGC CAC GGC "
#      "CTT TCG ACC GAC CTC ACG CTA GAA GGA"),
# ]
#
# CORRECT_ANSWERS_COMPLEMENTED = [
#     "TGCA",
#     "AAATTTCCCGGG",
#     ("ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCA"
#      "ACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCC"
#      "CTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCCTGGTTTCCGGCACCAGAAGCGGTGCCG"
#      "GAAAGCTGGCTGGAGTGCGATCTTCCT"),
# ]
# CORRECT_ANSWERS_REVERSE = [
#     "TGCA",
#     "CCCGGGAAATTT",
#     ("AGGAAGATCGCACTCCAGCCAGCTTTCCGGCACCGCTTCTGGTGCCGGAAACCAGGCAAAGCGCCATTCGC"
#      "CATTCAGGCTGCGCAACTGTTGGGAAGGGCGATCGGTGCGGGCCTCTTCGCTATTACGCCAGCTGGCGAAA"
#      "GGGGGATGTGCTGCAAGGCGATTAAGTTGGGTAACGCCAGGGTTTTCCCAGTCACGACGTTGTAAAACGAC"
#      "GGCCAGTGAATCCGTAATCATGGTCAT"),
# ]
# CORRECT_ANSWERS_REVERSE_COMPLEMENT = [
#     "ACGT",
#     "GGGCCCTTTAAA",
#     ("TCCTTCTAGCGTGAGGTCGGTCGAAAGGCCGTGGCGAAGACCACGGCCTTTGGTCCGTTTCGCGGTAAGCG"
#      "GTAAGTCCGACGCGTTGACAACCCTTCCCGCTAGCCACGCCCGGAGAAGCGATAATGCGGTCGACCGCTTT"
#      "CCCCCTACACGACGTTCCGCTAATTCAACCCATTGCGGTCCCAAAAGGGTCAGTGCTGCAACATTTTGCTG"
#      "CCGGTCACTTAGGCATTAGTACCAGTA"),
# ]
#
# # ############################################################################
# # Test complement function
# # ############################################################################
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(ACGT_BASES_ONLY, CORRECT_ANSWERS_COMPLEMENTED),
# )
# def test_acgt_complement(input_sequence, expected):
#     assert wc.complement(input_sequence).upper() == expected
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(MIXED_CASE_DNA, CORRECT_ANSWERS_COMPLEMENTED),
# )
# def test_mixed_case_complement(input_sequence, expected):
#     assert wc.complement(input_sequence).upper() == expected
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected", zip(DIRTY_DNA, CORRECT_ANSWERS_COMPLEMENTED)
# )
# def test_dirty_complement(input_sequence, expected):
#     assert wc.complement(input_sequence).upper() == expected
#
#
# # ############################################################################
# # Test reverse function
# # ############################################################################
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected", zip(ACGT_BASES_ONLY, CORRECT_ANSWERS_REVERSE)
# )
# def test_acgt_reverse(input_sequence, expected):
#     assert wc.reverse(input_sequence).upper() == expected
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected", zip(MIXED_CASE_DNA, CORRECT_ANSWERS_REVERSE)
# )
# def test_mixed_case_reverse(input_sequence, expected):
#     assert wc.reverse(input_sequence).upper() == expected
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected", zip(DIRTY_DNA, CORRECT_ANSWERS_REVERSE)
# )
# def test_dirty_reverse(input_sequence, expected):
#     assert wc.reverse(input_sequence).upper() == expected
#
#
# # ############################################################################
# # Test reverse complement function
# # ############################################################################
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(ACGT_BASES_ONLY, CORRECT_ANSWERS_REVERSE_COMPLEMENT),
# )
# def test_acgt_reverse_complement(input_sequence, expected):
#     assert (
#         wc.reverse_complement(input_sequence).upper()
#         == expected
#     )
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(MIXED_CASE_DNA, CORRECT_ANSWERS_REVERSE_COMPLEMENT),
# )
# def test_mixed_case_reverse_complement(input_sequence, expected):
#     assert (
#         wc.reverse_complement(input_sequence).upper()
#         == expected
#     )
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(DIRTY_DNA, CORRECT_ANSWERS_REVERSE_COMPLEMENT),
# )
# def test_dirty_reverse_complement(input_sequence, expected):
#     assert (
#         wc.reverse_complement(input_sequence).upper()
#         == expected
#     )
#
#
# # ############################################################################
# # Use more complex complement table
# # ############################################################################
#
#
# AMBIGOUS_DIRTY_DNA = [
#     "AGB Vnc gRy Tvv V",
#     ">\nT-TT-AAA-BDNNSSRYMNXXXX  GGGCCC!!!",
#     ("TAC WSA YBG KGK DVN YRS TGG TAC TAA TGC CTA AGT GAC CGG CAG CAA AAT GTT"
#      " GCA GCA CTG ACC CTT TTG GGA CCG CAA TGG GTT GAA TTA GCG GAA CGT CGT GT"
#      "A GGG GGA AAG CGG TCG ACC GCA TTA TCG CTT CTC CGG GCG TGG CTA GCG GGA A"
#      "GG GTT GTC AAC GCG TCG GAC TTA CCG CTT ACC GCG AAA CGG ACC AAA GGC CGT "
#      "GGT CTT CGC CAC GGC CTT TCG ACC GAC CTC ACG CTA GAA GGA"),
# ]
# CORRECT_ANSWER_AMBIGOUS_DNA_COMPLEMENT = [
#     "TCVBNGCYRABBB",
#     "AAATTTVHNNSSYRKNCCCGGG",
#     ("ATGWSTRVCMCMHBNRYSACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAA"
#      "CCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGG"
#      "CCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCCTGGTTTCCGGCA"
#      "CCAGAAGCGGTGCCGGAAAGCTGGCTGGAGTGCGATCTTCCT"),
# ]
# CORRECT_ANSWER_AMBIGOUS_DNA_REVERSE = [
#     "VVVTYRGCNVBGA",
#     "CCCGGGNMYRSSNNDBAAATTT",
#     ("AGGAAGATCGCACTCCAGCCAGCTTTCCGGCACCGCTTCTGGTGCCGGAAACCAGGCAAAGCGCCATTCGC"
#      "CATTCAGGCTGCGCAACTGTTGGGAAGGGCGATCGGTGCGGGCCTCTTCGCTATTACGCCAGCTGGCGAAA"
#      "GGGGGATGTGCTGCAAGGCGATTAAGTTGGGTAACGCCAGGGTTTTCCCAGTCACGACGTTGTAAAACGAC"
#      "GGCCAGTGAATCCGTAATCATGGTSRYNVDKGKGBYASWCAT"),
# ]
# CORRECT_ANSWER_AMBIGOUS_DNA_REVERSE_COMPLEMENT = [
#     "BBBARYCGNBVCT",
#     "GGGCCCNKRYSSNNHVTTTAAA",
#     ("TCCTTCTAGCGTGAGGTCGGTCGAAAGGCCGTGGCGAAGACCACGGCCTTTGGTCCGTTTCGCGGTAAGCGG"
#      "TAAGTCCGACGCGTTGACAACCCTTCCCGCTAGCCACGCCCGGAGAAGCGATAATGCGGTCGACCGCTTTCC"
#      "CCCTACACGACGTTCCGCTAATTCAACCCATTGCGGTCCCAAAAGGGTCAGTGCTGCAACATTTTGCTGCCG"
#      "GTCACTTAGGCATTAGTACCASYRNBHMCMCVRTSWGTA"),
# ]
#
#
# # ############################################################################
# # Test reverse, complement and rev comp. function with new table
# # ############################################################################
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(AMBIGOUS_DIRTY_DNA, CORRECT_ANSWER_AMBIGOUS_DNA_COMPLEMENT),
# )
# def test_acgt_complement_new_table(input_sequence, expected):
#     assert (
#         wc.complement(input_sequence, COMPLEMENTS_STR).upper()
#         == expected
#     )
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(AMBIGOUS_DIRTY_DNA, CORRECT_ANSWER_AMBIGOUS_DNA_REVERSE),
# )
# def test_mixed_case_reverse_new_table(input_sequence, expected):
#     assert (
#         wc.reverse(input_sequence, COMPLEMENTS_STR).upper()
#         == expected
#     )
#
#
# @pytest.mark.parametrize(
#     "input_sequence,expected",
#     zip(AMBIGOUS_DIRTY_DNA, CORRECT_ANSWER_AMBIGOUS_DNA_REVERSE_COMPLEMENT),
# )
# def test_dirty_reverse_complement_new_table(input_sequence, expected):
#     assert (
#         wc.reverse_complement(
#             input_sequence, COMPLEMENTS_STR
#         ).upper()
#         == expected
#     )
#
# from wc import (
#     _get_pycons,
#     update_pycons_lat_lon,
#     create_travel_plan,
#     total_travel_distance,
# )
#
#
# def test_update_pycons_lat_lon():
#     pycons = _get_pycons()
#     update_pycons_lat_lon(pycons)
#     for pycon in pycons:
#         assert isinstance(pycon.lat, float)
#         assert isinstance(pycon.lon, float)
#
#
# def test_create_travel_plan():
#     pycons = _get_pycons()
#     update_pycons_lat_lon(pycons)
#     travel_plan = create_travel_plan(pycons)
#     assert len(travel_plan) == 8
#     assert travel_plan[0].origin.name == "PyCon Odessa"
#     assert travel_plan[0].destination.name == "PyCon SK"
#     assert travel_plan[-1].origin.name == "PyCon DE & PyData Berlin"
#     assert travel_plan[-1].destination.name == "PyCon Ireland"
#
#
# def test_total_travel_distance():
#     pycons = _get_pycons()
#     update_pycons_lat_lon(pycons)
#     travel_plan = create_travel_plan(pycons)
#     assert total_travel_distance(travel_plan) == 8444.9
#
# import pytest
#
# from wc import count_islands
#
# squares = [[1, 1, 0, 1],
#            [1, 1, 0, 1],
#            [0, 0, 1, 1],
#            [1, 1, 1, 0]]
#
# sparse = [[1, 0, 1],
#           [0, 1, 0],
#           [1, 0, 1]]
#
# empty = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
#
# bad_map = [[]]
#
# circles = [[1, 1, 0, 0, 0, 1],
#            [1, 0, 0, 0, 0, 1],
#            [1, 0, 0, 0, 1, 1],
#            [1, 0, 0, 0, 1, 0],
#            [1, 0, 0, 1, 1, 0],
#            [1, 1, 1, 1, 0, 0]]
#
#
# @pytest.mark.parametrize("data, expected", [
#     (squares, 2),
#     (sparse, 5),
#     (empty, 0),
#     (bad_map, 0),
#     (circles, 1),
# ])
# def test_count_islands(data, expected):
#     assert count_islands(data) == expected
#
# from datetime import datetime
# from random import choice
# from tempfile import NamedTemporaryFile
#
# import pytest
#
# from wc import PBKDF2HMAC, ByteString, ClamyFernet, Fernet
#
# KEYS = (
#     b"rvxePMSDUcZFowEaNxnFb8Pifn1KmhkF70Mz1ZQe2Bw=",
#     b"2gODW4C4Lc7H9bjuuhPyn48HkVHriqa96P8lmstABo8=",
#     b"mAbAfF5CW3EGlngOEEroDqtxlxVlJILzoUE4TJScMIw=",
# )
# MESSAGE = "This is my secret message"
# TMP_FILE = NamedTemporaryFile(delete=False)
# FILE = TMP_FILE.name
#
#
# @pytest.fixture(scope="function")
# def rcf():
#     password = b"#clamybite"
#     key = choice(KEYS)
#     return ClamyFernet(password, key)
#
#
# @pytest.fixture(scope="module")
# def cf():
#     return ClamyFernet(key=KEYS[0])
#
#
# def test_clamyfernet_no_args(rcf):
#     tmp_cf = ClamyFernet()
#     assert tmp_cf.key is not None
#     assert tmp_cf.password == b"pybites"
#
#
# def test_clamyfernet_random_key(rcf):
#     token = rcf.encrypt("secret msg")
#     ts = rcf.clf.extract_timestamp(token)
#     dt = datetime.fromtimestamp(ts)
#     assert isinstance(rcf, ClamyFernet)
#     assert isinstance(rcf.clf, Fernet)
#     assert isinstance(rcf.key, ByteString)
#     assert isinstance(rcf.kdf, PBKDF2HMAC)
#     assert dt.year == datetime.now().year
#
#
# def test_clamyfernet(cf):
#     token = cf.encrypt(MESSAGE)
#     og_message = cf.decrypt(token)
#     assert len(token) == 120
#     assert isinstance(token, bytes)
#     assert cf.key == KEYS[0]
#     assert og_message == MESSAGE
#
#
# def test_clamyfernet_random(rcf):
#     token = rcf.encrypt(MESSAGE)
#     og_message = rcf.decrypt(token)
#     assert len(token) == 120
#     assert isinstance(token, bytes)
#     assert rcf.key in KEYS
#     assert og_message == MESSAGE
#
# import pytest
#
# from wc import max_fund
#
#
# community = [3, 2, 6,  4, 7,  5, -8, -9, 3,  8,  4, -12, 3, -10, -15,
#              2, 6, -10, 6, 3, -1,  5, -5, -8, 11, 7, -9, -5,  -6, -2,
#              7, 8, 11, 8,  6, -1, -6,  9, 8, 6, -3, 4,  -8, 3, -4, 1,
#              2, 8, -2, 9, -3, 8, -10,  -8,  5,  -4, -6,  5, -1, 4, 2,
#              2, 7,  3, -2, 5, 1, 4, -7, 5, 8, 4, 2, 10, -24, -10, -9,
#              -2, 1, 6, 1,  3, -44, 3, 6, -1, 9, -6, 5, 4, 3, 6, -1,
#              0, 11, 4, 8, 16, -33, 8, -2, 4, 5, 3, 2, -8, -7, -5,
#              0, 2, 5, -2, 4, 1, 2, 4, 2, -5, 7, 4, 5, -2, 7, 5, -8]
#
# poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
# some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
# extreme = [-1, -2, -3, -4, -5, -1, -2, -3]
#
#
# @pytest.mark.parametrize("data, expected", [
#     (community, (100, 31, 74)),
#     (poverty, (13, 6, 9)),
#     (some, (50,  9, 12)),
#     (extreme, (0, 0, 0))
# ])
# def test_funds(data, expected):
#     assert max_fund(data) == expected
#
# import pytest
#
# from wc import island_size
#
# rectangle = [[0, 1, 1, 0],
#              [0, 1, 1, 0],
#              [0, 1, 1, 0],
#              [0, 1, 1, 0]]
#
# small = [[0, 0, 0],
#          [0, 1, 0],
#          [0, 0, 0]]
#
# empty = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
#
# whole = [[1, 1, 1],
#          [1, 0, 1],
#          [1, 1, 1]]
#
#
# @pytest.mark.parametrize("map_, expected", [
#     (rectangle, 12),
#     (small, 4),
#     (empty, 0),
#     (whole, 16),
# ])
# def test_island_size(map_, expected):
#     assert island_size(map_) == expected
#
# import csv
# import random
# import re
# import string
#
# import pytest
#
# from wc import get_classes
#
# # note that since 3.8 there is no OrderedDict here anymore
# csv_classes = [
#     'Dialect', 'DictReader', 'DictWriter',
#     'Error', 'Sniffer', 'StringIO'
# ]
# random_classes = ['Random', 'SystemRandom']
# re_classes = ['Match', 'Pattern', 'RegexFlag', 'Scanner']
# string_classes = ['Formatter', 'Template']
#
#
# @pytest.mark.parametrize("mod, expected", [
#     (csv, csv_classes),
#     (random, random_classes),
#     (re, re_classes),
#     (string, string_classes),
# ])
# def test_cls(mod, expected):
#     actual = get_classes(mod)
#     assert sorted(actual) == sorted(expected)
#
# import pytest
#
# from wc import common_words
#
# sentence1 = ['To', 'be', 'or', 'not', 'to', 'be',
#              'that', 'is', 'a', 'question']
# sentence2 = ['To', 'strive', 'to', 'seek', 'to',
#              'find', 'and', 'not', 'to', 'yield']
# sentence3 = ['No', 'two', 'persons', 'ever', 'to',
#              'read', 'the', 'same', 'book', 'You', 'said']
# sentence4 = ['The', 'more', 'read', 'the',
#              'more', 'things', 'will', 'know']
# sentence5 = ['be', 'a', 'good', 'man']
#
#
# @pytest.mark.parametrize("sentence1, sentence2, expected", [
#     (sentence1, sentence2, ['to', 'not']),
#     (sentence3, sentence4, ['the', 'read']),
#     (sentence2, sentence3, ['to']),
#     (sentence5, sentence1, ['a', 'be']),
# ])
# def test_common_words(sentence1, sentence2, expected):
#     actual = common_words(sentence1, sentence2)
#     assert actual == expected
#
# import pytest
# from wc import dec_to_base
#
#
# @pytest.mark.parametrize("number, base, expected", [
#     (6, 2, 110), (7, 2, 111), (10, 2, 1010),
#     (16, 2, 10000), (20, 2, 10100), (10, 6, 14),
#     (24, 6, 40), (177, 6, 453), (256, 6, 1104),
#     (1024, 6, 4424), (10, 8, 12), (24, 8, 30),
#     (177, 8, 261), (256, 8, 400), (1024, 8, 2000),
#     (2020, 8, 3744),
# ])
# def test_dec_to_base(number, base, expected):
#     assert dec_to_base(number, base) == expected
#
# import pytest
#
# from wc import get_common_domains, get_most_common_domains
#
#
# @pytest.fixture(scope="module")
# def common_domains():
#     return list(get_common_domains())
#
#
# def test_get_common_domains(common_domains):
#     assert len(common_domains) == 100
#     first_3 = ['gmail.com', 'yahoo.com', 'hotmail.com']
#     last_3 = ['live.ca', 'aim.com', 'bigpond.net.au']
#     assert common_domains[:3] == first_3
#     assert common_domains[-3:] == last_3
#
#
# @pytest.mark.parametrize("emails, expected", [
#     (["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"],
#      [('pybit.es', 2), ('domain.de', 1)]),
#     (["a@hotmail.com", "b@gmail.com"], []),
#     (["a@hotmail.com", "b@hotmail.se",
#       "c@paris.com", "d@paris.com", "e@hotmail.it"],
#      [('paris.com', 2), ('hotmail.se', 1)]),
#     (["a@gmail.es", "b@googlemail.com", "c@somedomain.com",
#       "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"],
#      [('somedomain.com', 3), ('gmail.es', 1)]),
# ])
# def test_get_most_common_domains(common_domains, emails, expected):
#     assert get_most_common_domains(emails, common_domains) == expected
#
# import pytest
#
# from wc import pascal
#
#
# @pytest.mark.parametrize("arg, expected", [
#     (0, []),
#     (1, [1]),
#     (2, [1, 1]),
#     (5, [1, 4, 6, 4, 1]),
#     (10, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]),
#     (12, [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]),
#     (6, [1, 5, 10, 10, 5, 1]),
# ])
# def test_pascal(arg, expected):
#     assert pascal(arg) == expected

#
# from wc  import extract_ipv4
#
#
# def test_empty_list() :
#     assert extract_ipv4([]) == []
#
#
# def test_flat_list_no_match():
#     assert extract_ipv4(['ip']) == []
#
#
# def test_nested_list_no_match():
#     assert extract_ipv4([['ip', 'mask']]) == []
#
#
# def test_nested_list_no_ip():
#     assert extract_ipv4([['TEST', ['ip', [None], 'mask', ['24'], 'type', ['ip_mask']], 'id']]) == []
#
#
# def test_nested_list_not_an_ip():
#     assert extract_ipv4([['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]) == []
#
#
# def test_nested_list_no_mask():
#     assert extract_ipv4([['TEST', ['ip', ['"1.1.1.0"'], 'mask', [None], 'type', ['ip_mask']], 'id']]) == []
#
#
# def test_flat_list():
#     assert extract_ipv4(['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]) == [('172.16.0.0', '12')]
#
#
# def test_nested_list():
#     assert extract_ipv4(['TEST', 'parent', [], 'uuid', '"khk-yyas4h-323223-wewe-343er-3434-www"', 'display_name', '"services"', 'IPV4', [['ip', ['"192.168.1.0"'], 'mask', ['24'], 'type', ['ip_mask']], ['ip', ['"10.0.0.0"'], 'mask', ['8'], 'type', ['ip_mask']]]]) == [('192.168.1.0', '24'), ('10.0.0.0', '8')]
#
#
# def test_deeply_nested_list():
#     assert extract_ipv4([['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name', ['"services"'], 'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']], ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type', ['ip_mask']]]]]]]) == [('1.1.1.0', '20'), ('2.2.2.2', '32')]
#
# from wc import decompress
#
#
# def test_empty_string():
#     assert decompress('', {'[', 'L'}) == ''
#
#
# def test_empty_table():
#     assert decompress('Hello World!', {}) == 'Hello World!'
#
#
# def test_no_conversions():
#     assert decompress('Hello World!', {'*': 'o', '#': 'h'}) == 'Hello World!'
#
#
# def test_example():
#     table = {'$': 's',
#              '%': 'y',
#              '/': 't'
#              }
#
#     assert decompress('P%Bi/e$', table) == 'PyBites'
#
#
# def test_short():
#     table = {'*': 'c',
#              '#': '00',
#              '$': '*y',
#              }
#
#     assert decompress('$3#', table) == 'cy300'
#
#
# def test_long():
#     table = {'#': 'hem',
#              '@': 'T#',
#              '$': 't#',
#              '&': '$ as',
#              '*': ' do ',
#              '%': ' to',
#              '^': ' someone ',
#              '~': 'for ',
#              '+': '~&',
#              }
#
#     assert decompress("@ as can*has%*+ can't. And^has% speak up + has no voices.", table) == "Them as can do has to " \
#                                                                                              "do for them as can't. " \
#
# import pytest
#
# from wc import sum_indices
#
#
# @pytest.mark.parametrize('test_input, expected', [
#     ([], 0),
#     (['a'], 0),
#     (['a', 'b', 'c'], 3),
#     (['a', 'b', 'b', 'c'], 7),
#     (['a', 'b', 'b', 'c', 'a', 'b', 'a'], 29),
#     (['a', 'b', 'c', 'd', 'e', 'a', 'f', 'a', 'g', 'd', 'a'], 75),
#     (['a', 'b', 'z', 'c', 'd', 'x', 'b', 'x', 'e'], 42), ])
# def test_sum_indices(test_input, expected):
#     assert sum_indices(test_input) == expected
#     "And someone has to " \
#                                                                                              "speak up for them as " \
#                                                                                              "has no voices."
# import pytest
#
# from wc import class_rosters
#
# full = """
# 17409,"Matheson, Rick",,,,,,,,,,
# 36283,"Jones, Tom",SCI09-4 - SU,MATH09-2 - PH,TA09-1 - AB,IS09-4 - LM,SCI09-3 - NdN,MATH09-2 - RB,DE09-3 - KmQ,ENG09-3 - KaR,PE09-3 - PS
# 99415,"Blake, Arnold",,,,,,,,,,
# """  # noqa E501
# partial = """
# 17409,"Jones, Tom",,,,,,,,,,
# 17409,"Matheson, Rick",,IS09-1 - BR,,SCI09-4 - SU,MATH09-2 - RB,,ENG09-4 - LE,,PE09-1 - MR,
# 99415,"Blake, Arnold",,,,,,,,,,
# """  # noqa E501
# empty = """
# 99415,"Blake, Arnold",,,,,,,,,,
# 21692,"Prest, Phil",,,,,,,,,,
# 36283,"Jones, Tom",,,,,,,,,,
# """  # noqa E501
#
#
# @pytest.mark.parametrize("content, expected", [
#     (full, ['SCI09-4,2020,36283',
#             'MATH09-2,2020,36283',
#             'TA09-1,2020,36283',
#             'IS09-4,2020,36283',
#             'SCI09-3,2020,36283',
#             'MATH09-2,2020,36283',
#             'DE09-3,2020,36283',
#             'ENG09-3,2020,36283',
#             'PE09-3,2020,36283']),
#     (partial, ['IS09-1,2020,17409',
#                'SCI09-4,2020,17409',
#                'MATH09-2,2020,17409',
#                'ENG09-4,2020,17409',
#                'PE09-1,2020,17409']),
#     (empty, []),
# ])
# def test_class_rosters(content, expected, tmp_path):
#     csvfile = tmp_path / "content"
#     csvfile.write_text(content.lstrip())
#     actual = class_rosters(csvfile)
#     assert actual == expected
#
# import pytest
#
# from wc import get_srt_section_ids
#
# text1 = """
# 1
# 00:00:00,498 --> 00:00:02,827
# Beautiful is better than ugly.
#
# 2
# 00:00:02,827 --> 00:00:06,383
# Explicit is better than implicit.
#
# 3
# 00:00:06,383 --> 00:00:09,427
# Simple is better than complex.
# """
# text2 = """
# 18
# 00:01:12,100 --> 00:01:17,230
# If you want a bit more minimalistic view, you can actually hide the sidebar.
#
# 19
# 00:01:18,200 --> 00:01:19,500
# If you go to Settings
#
# 20
# 00:01:23,000 --> 00:01:26,150
# scroll down to 'Focus Mode'.
#
# 21
# 00:01:28,200 --> 00:01:35,180
# You can actually hide the sidebar and have only the description and the code editor.
# """  # noqa E501
# text3 = '\n'.join(text1.splitlines()[:9])
# text4 = '\n'.join(text2.splitlines()[5:])
# # testing hours as well
# text5 = """
# 32
# 00:59:45,000 --> 00:59:48,150
# talking quite normal here
#
# 33
# 01:00:00,000 --> 01:00:07,000
# he is talking slooooow
#
# 34
# 02:04:28,000 --> 02:04:30,000
# she is talking super fast here!
# """
#
#
# @pytest.mark.parametrize("text, expected", [
#     (text1, [1, 3, 2]),
#     (text2, [19, 18, 21, 20]),
#     (text3, [1, 2]),
#     (text4, [19, 21, 20]),
#     (text5, [34, 32, 33]),
# ])
# def test_srt(text, expected):
#     assert get_srt_section_ids(text) == expected
#
# import pytest
#
# from wc import jagged_list
#
#
# @pytest.mark.parametrize('input_list, fillvalue, expected',
#                          [
#                              ([], 0, []),
#
#                              ([[0]], 0, [[0]]),
#
#                              ([[0], [1]], 0, [[0], [1]]),
#
#                              ([[1, 1, 1, 1],
#                                [0, 0, 0, 0],
#                                [1]],
#                               1,
#                               [[1, 1, 1, 1],
#                                [0, 0, 0, 0],
#                                [1, 1, 1, 1]]),
#
#                              ([[1, 2, 3],
#                                [1, 2, 3, 4, 5],
#                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                                [1, 2],
#                                [1, 2, 3, 4]],
#                               0,
#                               [[1, 2, 3, 0, 0, 0, 0, 0, 0],
#                                [1, 2, 3, 4, 5, 0, 0, 0, 0],
#                                [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                                [1, 2, 0, 0, 0, 0, 0, 0, 0],
#                                [1, 2, 3, 4, 0, 0, 0, 0, 0]]),
#                          ])
# def test_jagged_list(input_list, fillvalue, expected):
#     assert jagged_list(input_list, fillvalue) == expected
#
# from wc import fasta_to_2line_fasta, FASTA_FILE
#
# EXPECTED_RECORDS = 59
#
#
# def test_well_formed_fasta():
#     """
#     Test if output is correct with well-formed input.
#     """
#
#     CONVERTED_FASTA = f"{FASTA_FILE}-test.fasta"
#
#     assert fasta_to_2line_fasta(FASTA_FILE, CONVERTED_FASTA) == EXPECTED_RECORDS
#     with open(FASTA_FILE, "r") as f:
#         f.readline()
#         assert (
#             f.readline().strip()
#             == "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
#         )
#
#     with open(CONVERTED_FASTA, "r") as f_conv:
#         f_conv.readline()
#         assert (
#             f_conv.readline().strip()
#             == "MNLLSIQPLNRIAIQFGPLTVYWYGIIIGIGILLGLILATREGKKLQVPSNTFTDLVLYA"
#             "LPISILSARIYYVLFEWAYYKNHLNEIFAIWNGGIAIHGGLIGAIVTTIVFTKKRNISF"
#             "WKLADIAAPSLILGQAIGRWGNFMNQEAHGGPVSRTFLESLRLPDIIINQMYINGSYYH"
#             "PTFLYESIWNIIGFVTLLILRKGSLKRGEIFLSYLIWYSIGRFFVEGLRTDSLMLTSSL"
#             "RMAQVMSISLIIISLLLMIYRRRKGLATTRYNELNNNALE"
#         )
#
#
# def test_malformed_fasta():
#     """
#     Test if output is correct with mal-formed input.
#     """
#     MALFORMED_FASTA = f"{FASTA_FILE}.malformed.fasta"
#     CONVERTED_FASTA = f"{FASTA_FILE}.malformed-test.fasta"
#
#     with open(FASTA_FILE, "r") as f_in, open(MALFORMED_FASTA, "w") as f_out:
#         f_out.write(f_in.read()[1:])
#
#     assert (
#         fasta_to_2line_fasta(MALFORMED_FASTA, CONVERTED_FASTA) == EXPECTED_RECORDS - 1
#     )
#
#     with open(CONVERTED_FASTA, "r") as f_conv:
#         assert (
#             f_conv.readline().strip()
#             == ">sp|Q74NT6|ARSC1_BACC1 Arsenate reductase 1 OS=Bacillus cereu"
#             "s (strain ATCC 10987 / NRS 248) OX=222523 GN=arsC1 PE=3 SV=1"
#         )
#         assert (
#             f_conv.readline().strip()
#             == "MENKKTIYFLCTGNSCRSQMAEAWGKKYLGDKWNVLSAGIEAHGVNPNAIKAMKEVDIDIT"
#             "DQTSDIIDRDILDKADLVVTLCGHANDVCPTTPPHVKRVHWGFDDPAGQEWSVFQRVRDE"
#             "IGARIKKYAETGE"
#         )
#
# import pytest
#
# from wc import convert
#
#
# @pytest.mark.parametrize("number, base, expected", [
#     (935, 29, "137"),
#     (74, 27, "2K"),
#     (685, 26, "109"),
#     (203, 18, "B5"),
#     (119, 20, "5J"),
#     (216, 29, "7D"),
#     (764, 16, "2FC"),
#     (411, 14, "215"),
#     (191, 27, "72"),
#     (80, 17, "4C"),
#     (761, 13, "467"),
#     (309, 22, "E1"),
#     (760, 27, "114"),
#     (654, 19, "1F8"),
#     (590, 34, "HC"),
#     (541, 27, "K1"),
#     (137, 4, "2021"),
#     (952, 10, "952"),
#     (483, 13, "2B2"),
#     (279, 27, "A9"),
# ])
# def test_convert(number, base, expected):
#     assert convert(number, base) == expected
#
#
# @pytest.mark.parametrize("number, base", [
#     (100, 37),
#     (100, 0),
#     (100, 1),
#     (100, -20),
# ])
# def test_convert_base_high(number, base):
#     with pytest.raises(ValueError):
#         convert(number, base)
#
#
# def test_convert_non_base10_number():
#     with pytest.raises(TypeError):
#         convert("FF", 10)
# import json
# from datetime import date
#
# import pytest
#
# from wc import RATES_FILE, exchange_rates, get_all_days, match_daily_rates
#
#
# @pytest.fixture(scope="session")
# def exchange_rates_result():
#     return exchange_rates()
#
#
# @pytest.fixture(scope="session")
# def matching_result():
#     start = date(2020, 1, 1)
#     end = date(2020, 9, 1)
#     daily_rates = json.loads(RATES_FILE.read_text())["rates"]
#     return match_daily_rates(start, end, daily_rates)
#
#
# @pytest.mark.parametrize(
#     "start, end, expected",
#     [
#         (date(2020, 1, 1), date(2020, 1, 31), 31),
#         (date(2020, 1, 14), date(2020, 1, 29), 16),
#         (date(2020, 4, 12), date(2020, 4, 14), 3),
#     ],
# )
# def test_get_all_days(start, end, expected):
#     actual = get_all_days(start, end)
#     assert len(actual) == expected
#
#     assert isinstance(actual[0], date)
#     assert isinstance(actual[-1], date)
#
#     assert actual[0] == start
#     assert actual[-1] == end
#
#
# @pytest.mark.parametrize(
#     "date, expected",
#     [
#         (date(2020, 1, 18), date(2020, 1, 17)),
#         (date(2020, 2, 2), date(2020, 1, 31)),
#         (date(2020, 5, 3), date(2020, 4, 30)),
#         (date(2020, 8, 15), date(2020, 8, 14)),
#     ],
# )
# def test_match_daily_rates(date, expected, matching_result):
#     actual = matching_result
#     assert actual[date] == expected
#
#
# @pytest.mark.parametrize(
#     "testdate, expected",
#     [
#         (
#             date(2020, 7, 16),
#             {"Base Date": date(2020, 7, 16), "GBP": 0.90875, "USD": 1.1414},
#         ),
#         (
#             date(2020, 7, 17),
#             {"Base Date": date(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
#         ),
#         (
#             date(2020, 7, 18),
#             {"Base Date": date(2020, 7, 17), "GBP": 0.91078, "USD": 1.1428},
#         ),
#     ],
# )
# def test_exchange_rates_sample(testdate, expected, exchange_rates_result):
#     actual = exchange_rates_result
#
#     assert actual[testdate]["Base Date"] == expected["Base Date"]
#     assert actual[testdate]["GBP"] == expected["GBP"]
#     assert actual[testdate]["USD"] == expected["USD"]
#
#
# def test_exchange_rates_all_dates(exchange_rates_result):
#     assert len(exchange_rates_result) == 245
#
#
# def test_exchange_rates_order(exchange_rates_result):
#     actual = list(exchange_rates_result.keys())
#     expected = sorted(exchange_rates_result.keys())
#
#     assert actual == expected
#
#
# def test_exchange_rates_validate_start():
#     with pytest.raises(ValueError):
#         exchange_rates(start_date="1950-01-01")
#
#
# def test_exchange_rates_validate_end():
#     with pytest.raises(ValueError):
#         exchange_rates(end_date="2050-01-01")
#
# import filecmp
# from urllib.request import urlretrieve
#
# import pytest
#
# from wc import get_passing_code, url, tmp
#
#
# @pytest.mark.parametrize('actual_filename, expected_filename', [
#     ('Bite01.py', 'Bite01_Expected.py'),
#     ('Bite02.py', 'Bite02_Expected.py')
# ])
# def test_compare_files(actual_filename, expected_filename):
#     actual = tmp / actual_filename
#     expected = tmp / expected_filename
#     get_passing_code()
#     urlretrieve(url.format(filename=expected_filename),
#                 expected)
#     assert filecmp.cmp(actual, expected)
#
# import pytest
# from wc import max_letter_word
#
# sample_text = '''It is a truth universally acknowledged, that a single man in
#                     possession of a good fortune, must be in want of a wife.'''
# with_numbers_text = '''20,000 Leagues Under the Sea is a 1954 American
#                     Technicolor science fiction-adventure film...'''
# emoji_text = 'emoji like 😃😃😃😃 are not letters'
# accents_text = 'Société Générale est une des principales banques françaises'
# mixed_case_text = 'Short Plays By Lady Gregory The Knickerbocker Press 1916'
# hyphenated_word_text = 'six-feet-two in height'
# compound_character_text = 'der Schloß is riesig'
# no_repeat_characters_text = 'the quick brown fox jumped over the lazy dog'
# non_ascii_symbols_text = '«¿Tiene sentido la TV pública?»'
# apostrophe_in_word_text = "but we've been there already!!!"
# underscore_torture_text = '"____".isalpha() is True, thus this test text'
# digit_text = '99abc99 __abc__ --abc-- digits _ and - are not letters'
# repeat_words_text = 'test test test test test correct-answer.'
# quoted_text = 'They shouted "Oh no she didn\'t"'
# trailing_apostrophe = "The brothers' feet were muddy."
# no_words_in_text = '1, 2, 3'
# empty_text = ''
#
#
# @pytest.mark.parametrize("given, expected",
#                          [(sample_text, ('possession', 's', 4)),
#                           (with_numbers_text, ('Leagues', 'e', 2)),
#                           (emoji_text, ('letters', 'e', 2)),
#                           (accents_text, ('Société', 'é', 2)),
#                           (mixed_case_text, ('Knickerbocker', 'k', 3)),
#                           (hyphenated_word_text, ('six-feet-two', 'e', 2)),
#                           (compound_character_text, ('Schloß', 's', 3)),
#                           (no_repeat_characters_text, ('the', 't', 1)),
#                           (non_ascii_symbols_text, ('Tiene', 'e', 2)),
#                           (apostrophe_in_word_text, ("we've", 'e', 2)),
#                           (underscore_torture_text, ('isalpha', 'a', 2)),
#                           (digit_text, ('digits', 'i', 2)),
#                           (repeat_words_text, ('correct-answer', 'r', 3)),
#                           (quoted_text, ("didn't", 'd', 2)),
#                           (trailing_apostrophe, ("brothers", 'r', 2)),
#                           (no_words_in_text, ('', '', 0)),
#                           (empty_text, ('', '', 0)),
#                           ])
# def test_max_letter_word(given, expected):
#     result = max_letter_word(given)
#     assert result == expected
#
#
# @pytest.mark.parametrize("bad_input", [None, True, 1, 1.0, [], {}])
# def test_max_letter_word_exceptions(bad_input):
#     with pytest.raises(ValueError):
#         max_letter_word(bad_input)
#
# from textwrap import dedent
#
# import pytest
#
# from wc import split_once
#
#
# @pytest.mark.parametrize('test_input, expected', [
#                         ('', ['']),
#                         ('abc', ['abc']),
#                         ('abc def', ['abc', 'def']),
#                         ('abc\tdef', ['abc', 'def']),
#                         ('abc def ghi', ['abc', 'def ghi']),
#                         ('abc def\tghi', ['abc', 'def', 'ghi']),
#                         ('abc def\tghi jkl\tmno', ['abc', 'def', 'ghi jkl\tmno']),
#                         ('The quick\tbrown\nfox\vjumps \fover\r the\tlazy\vdog\n',
#                          ['The', 'quick', 'brown', 'fox', 'jumps ', 'over', ' the\tlazy\vdog\n']),
# ])
# def test_split_once_whitespace(test_input, expected):
#     assert split_once(test_input) == expected
#
#
# @pytest.mark.parametrize('test_input, expected', [
#                         ('', ['']),
#                         ('abc', ['abc']),
#                         ('abc def', ['abc def']),
#                         ('abc: def: ijk, lmno: pqr - stu, wxy', ['abc', ' def: ijk', ' lmno: pqr ', ' stu, wxy']),
#                         ('lorem ipsum, dolor sit - amet, consectetur : adipiscing elit. Praesent vitae orc',
#                          ['lorem ipsum', ' dolor sit ', ' amet, consectetur ', ' adipiscing elit. Praesent vitae orc']),
# ])
# def test_split_once(test_input, expected):
#     assert split_once(test_input, separators=',-:') == expected
#
#
# @pytest.mark.parametrize('separators, expected', [
#     (None, ['Darmok', 'and Jalad… at Tanagra.', 'Shaka, when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
#     (',-:', ['Darmok and Jalad… at Tanagra.\nShaka', ' when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
#     ('…!.', ['Darmok and Jalad', ' at Tanagra', '\nShaka, when the walls fell.\nTemba, his arms wide', '\nDarmok and Jalad… they left together.\nMirab, with sails unfurled.\n']),
#     ('aeiouy', ['D', 'rm', 'k and Jalad… at Tanagra.\nShaka, wh', 'n the walls fell.\nTemba, h', 's arms wide!\nDarmok and Jalad… the', ' left together.\nMirab, with sails ', 'nfurled.\n']),
#     ('MDJTS', ['', 'armok and ', 'alad… at ', 'anagra.\n', 'haka, when the walls fell.\nTemba, his arms wide!\nDarmok and Jalad… they left together.\n', 'irab, with sails unfurled.\n'])
# ])
# def test_split_once_variable_separators(separators, expected):
#     constant_text = dedent("""\
#                            Darmok and Jalad… at Tanagra.
#                            Shaka, when the walls fell.
#                            Temba, his arms wide!
#                            Darmok and Jalad… they left together.
#                            Mirab, with sails unfurled.
#                            """)
#
#     assert split_once(constant_text, separators=separators) == expected
#
#
# import pytest
#
# from Bio.Data.CodonTable import TranslationError
#
# from wc import translate_cds
#
# # Note on Bio.Seq table ids: These can be found in the
# # Seq.CodonTable.ambiguous_generic_by_name variable
#
#
# @pytest.mark.parametrize(
#     "cds,table,expected",
#     [
#         (
#             "ATGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Vertebrate Mitochondrial",
#             "MPGKAHKKCSTPLHHPG",
#         ),
#         (
#             "GTGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Vertebrate Mitochondrial",
#             "MPGKAHKKCSTPLHHPG",
#         ),
#         (
#             "ATGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Bacterial",
#             "MPGKAHKKCSTPLHHPG",
#         ),
#         (
#             "TTGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Bacterial",
#             "MPGKAHKKCSTPLHHPG",
#         ),
#         (
#             "ATGCCCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTGA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),
#         (
#             "aTgCCcGGGAAAGCGCACaaGAAGTGCTCAACGccccTACATCATCCGGGGtaa",
#             "Bacterial",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # capitalization
#         (
#             "ATGCCRGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTGA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # ambiguous base R, solvable AA, CCR>P
#         (
#             "ATGCRCGGGAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTGA",
#             "Standard",
#             "MXGKAHKKCSTPLHHPG",
#         ),  # ambiguous base R, ambiguous AA, CRC>X
#         (
#             "ATG CCC GGG AAA GCG CAC AAG AAG TGC TCA ACG CCC CTA CAT CAT CCG GGG TGA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # spaces
#         (
#             "ATG CCC GGG     AAAGCGCACAAGAAGTG CTCAACGCCCCTACATCATCCGGGG TAA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # multiple spaces
#         (
#             "ATGCCC\tGGG\tAAAGCGCACAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # tabs
#         (
#             "ATGCCCGGGAAAGCGCACAAGAAGTG\nCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # newline
#         (
#             "ATGC\u00A0CCGGGAAAGCGCA\u2009CAAGAAGTGCTCAACGCCCCTACATCATCCGGGGTAA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # U+00A0: NO-BREAK SPACE; U+2009: THIN SPACE
#         (
#             "ATGC\u00A0CCG\tGGA AAG CGCA\u2009CAAGAAGTG\nCTCAACGC\tCCCTA\rCA TCA TCCGGGGTAA",
#             "Standard",
#             "MPGKAHKKCSTPLHHPG",
#         ),  # lots of whitespace
#     ],
# )
# def test_translate_cds(cds, table, expected):
#     """
#     Test if returned protein sequence and type are correct
#     """
#     result = translate_cds(cds, table)
#     assert isinstance(result, str)
#     assert result.upper() == expected
#
#
# @pytest.mark.parametrize(
#     "cds,table",
#     [
#         ("ATGAA", "Standard"),  # len % 3 != 0
#         ("ATGAAA", "Standard"),  # last codon not stop codon
#         ("TTTTAA", "Standard"),  # no start codon
#         ("ATGTAATAA", "Standard"),  # internal stop codon
#     ],
# )
# def test_translate_cds_fail(cds, table):
#     """
#     Test if function throws error when bad data is fed in
#     """
#     with pytest.raises(TranslationError):
#         translate_cds(cds, table)
#
# import sqlite3
# import pytest
#
# from wc import DB, SQLiteType, SchemaError
#
# NINJAS = [
#     ("taspotts", 906),
#     ("Tomade", 896),
#     ("tasoak", 894),
#     ("clamytoe", 890),
# ]
#
# DB_SCHEMA = [("ninja", SQLiteType.TEXT), ("bitecoins", SQLiteType.INTEGER)]
#
#
# @pytest.fixture
# def db():
#     with DB() as db:
#         db.create("ninjas", DB_SCHEMA, "ninja")
#         db.insert("ninjas", NINJAS)
#
#         yield db
#
#
# def test_empty_db():
#     db = DB()
#     assert db.location == ":memory:"
#     assert db.cursor is None
#     assert db.connection is None
#     assert db.table_schemas == {}
#
#
# @pytest.mark.parametrize(
#     "table, schema, pk",
#     [
#         ("city", [("name", SQLiteType.TEXT), ("population", SQLiteType.REAL)], "name"),
#         ("ninjas", DB_SCHEMA, "ninja"),
#     ],
# )
# def test_create(table, schema, pk):
#     with DB() as db:
#         assert db.num_transactions == 0
#         db.create(table, schema, pk)
#         query = (
#             f"SELECT name FROM sqlite_master WHERE type= 'table' AND name='{table}';"
#         )
#         output = db.cursor.execute(query).fetchall()
#         assert len(output) == 1
#         assert db.num_transactions == 0
#
#
# def test_no_table_twice(db):
#     with pytest.raises(sqlite3.OperationalError) as e:
#         db.create("ninjas", DB_SCHEMA, "ninja")
#     assert str(e.value) == "table ninjas already exists"
#
#
# def test_wrong_pk():
#     with pytest.raises(SchemaError) as e:
#         with DB() as db:
#             db.create("ninjas", DB_SCHEMA, "ID")
#
#     assert str(e.value) == "The provided primary key must be part of the schema."
#
#
# def test_insert(db):
#     assert db.num_transactions == 4
#     query = f"SELECT * FROM ninjas;"
#     output = db.cursor.execute(query).fetchall()
#     assert output == NINJAS
#
#
# def test_insert_twice(db):
#     with pytest.raises(sqlite3.IntegrityError) as e:
#         db.insert("ninjas", NINJAS)
#
#     assert str(e.value) in ("UNIQUE constraint failed: ninjas.ninja",
#                             "column ninja is not unique")
#
#
# @pytest.mark.parametrize(
#     "table, bad_values, expected",
#     [
#         ("ninjas", [("Bob",)], 2),
#         ("ninjas", [("Bob", 1000, 1)], 2),
#         ("ninjas", [tuple()], 2),
#         ("ninjas", [("Bob", 1000), ("pmayd",)], 2),
#     ],
# )
# def test_incorrect_number_of_values_for_insert(db, table, bad_values, expected):
#     with pytest.raises(SchemaError) as e:
#         db.insert(table, bad_values)
#     assert str(e.value) == f"Table {table} expects items with {expected} values."
#
#
# @pytest.mark.parametrize(
#     "table, bad_values, col, expected",
#     [
#         ("ninjas", [("Bob", "1000")], "bitecoins", int),
#         ("ninjas", [(1000, "Bob")], "ninja", str),
#         ("ninjas", [("Bob", 1000), ("pmayd", "128")], "bitecoins", int),
#     ],
# )
# def test_wrong_value_type_for_insert(db, table, bad_values, col, expected):
#     with pytest.raises(SchemaError) as e:
#         db.insert(table, bad_values)
#
#     assert str(e.value) == f"Column {col} expects values of type {expected.__name__}."
#
#
# @pytest.mark.parametrize(
#     "table, col, expected",
#     [
#         ("ninjas", None, NINJAS),
#         ("ninjas", ["ninja"], sorted([(e[0],) for e in NINJAS])),
#         ("ninjas", ["bitecoins"], [(e[1],) for e in NINJAS]),
#     ],
# )
# def test_select(db, table, col, expected):
#     rows = db.select(table, col)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, target, expected",
#     [
#         ("ninjas", ("ninja", "clamytoe"), [e for e in NINJAS if e[0] == "clamytoe"]),
#         ("ninjas", ("bitecoins", 906), [e for e in NINJAS if e[1] == 906]),
#     ],
# )
# def test_select_db_target(db, table, target, expected):
#     row = db.select(table, target=target)
#     assert row == expected
#
#
# @pytest.mark.parametrize(
#     "table, target, expected",
#     [
#         ("ninjas", ("bitecoins", ">", 900), [e for e in NINJAS if e[1] > 900]),
#         ("ninjas", ("ninja", "LIKE", "%pot%"), [e for e in NINJAS if "pot" in e[0]]),
#         ("ninjas", ("ninja", "<>", "Tomade"), [e for e in NINJAS if e[0] != "Tomade"]),
#     ],
# )
# def test_select_operator(db, table, target, expected):
#     rows = db.select(table, target=target)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, new_value, target, expected",
#     [
#         ("ninjas", ("bitecoins", 1000), ("ninja", "clamytoe"), [("clamytoe", 1000)]),
#         ("ninjas", ("ninja", "tomade"), ("ninja", "Tomade"), [("tomade", 896)]),
#     ],
# )
# def test_update_db(db, table, new_value, target, expected):
#     db.update("ninjas", new_value, target)
#     assert db.num_transactions == 5
#
#     rows = db.select(table, target=new_value)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, target", [("ninjas", ("ninja", "clamytoe")), ("ninjas", ("bitecoins", 906))]
# )
# def test_delete_db(db, table, target):
#     db.delete(table, target)
#     rows = db.select(table, target=target)
#     assert rows == [
#     ]
#
# import xml.etree.ElementTree as ET
#
# from wc import get_tree, get_movies, get_movie_longest_runtime
#
#
# def test_get_tree():
#     tree = get_tree()
#     assert type(tree) in (ET.ElementTree, ET.Element)
#     assert len(list(tree.iter(tag='movie'))) == 5
#
#
# def test_get_movies():
#     assert list(get_movies()) == ['The Prestige', 'The Dark Knight',
#                                   'The Dark Knight Rises', 'Dunkirk',
#                                   'Interstellar']
#
#
# def test_get_movie_longest_runtime():
#     assert get_movie_longest_runtime() == 'Interstellar'

#
# import pytest
#
# from wc import my_queue
#
# q1 = my_queue(5)
# q2 = my_queue(3)
# q3 = my_queue(7)
#
#
# @pytest.mark.parametrize('fn_in,expected_result', [
#     (0, [0]),
#     (1, [0, 1]),
#     (2, [0, 1, 2]),
#     (3, [0, 1, 2, 3]),
#     (4, [0, 1, 2, 3, 4]),
#     (5, [1, 2, 3, 4, 5]),
#     (6, [2, 3, 4, 5, 6]),
# ])
# def test_queue_default_arg(fn_in, expected_result):
#     q1.append(fn_in)
#     assert list(q1) == expected_result
#
#
# @pytest.mark.parametrize('fn_in,expected_result', [
#     (0, [0]),
#     (1, [0, 1]),
#     (2, [0, 1, 2]),
#     (3, [1, 2, 3]),
#     (4, [2, 3, 4]),
#     (5, [3, 4, 5]),
#     (6, [4, 5, 6]),
# ])
# def test_queue_less_items(fn_in, expected_result):
#     q2.append(fn_in)
#     assert list(q2) == expected_result
#
#
# @pytest.mark.parametrize('fn_in,expected_result', [
#     (0, [0]),
#     (1, [0, 1]),
#     (2, [0, 1, 2]),
#     (3, [0, 1, 2, 3]),
#     (4, [0, 1, 2, 3, 4]),
#     (5, [0, 1, 2, 3, 4, 5]),
#     (6, [0, 1, 2, 3, 4, 5, 6]),
# ])
# def test_queue_more_items(fn_in, expected_result):
#     q3.append(fn_in)
#     assert list(q3) == expected_result
#
# import sqlite3
# import pytest
#
# from wc import DB, SQLiteType, SchemaError
#
# NINJAS = [
#     ("taspotts", 906),
#     ("Tomade", 896),
#     ("tasoak", 894),
#     ("clamytoe", 890),
# ]
#
# DB_SCHEMA = [("ninja", SQLiteType.TEXT), ("bitecoins", SQLiteType.INTEGER)]
#
#
# @pytest.fixture
# def db():
#     with DB() as db:
#         db.create("ninjas", DB_SCHEMA, "ninja")
#         db.insert("ninjas", NINJAS)
#
#         yield db
#
#
# def test_empty_db():
#     db = DB()
#     assert db.location == ":memory:"
#     assert db.cursor is None
#     assert db.connection is None
#     assert db.table_schemas == {}
#
#
# @pytest.mark.parametrize(
#     "table, schema, pk",
#     [
#         ("city", [("name", SQLiteType.TEXT), ("population", SQLiteType.REAL)], "name"),
#         ("ninjas", DB_SCHEMA, "ninja"),
#     ],
# )
# def test_create(table, schema, pk):
#     with DB() as db:
#         assert db.num_transactions == 0
#         db.create(table, schema, pk)
#         query = (
#             f"SELECT name FROM sqlite_master WHERE type= 'table' AND name='{table}';"
#         )
#         output = db.cursor.execute(query).fetchall()
#         assert len(output) == 1
#         assert db.num_transactions == 0
#
#
# def test_no_table_twice(db):
#     with pytest.raises(sqlite3.OperationalError) as e:
#         db.create("ninjas", DB_SCHEMA, "ninja")
#     assert str(e.value) == "table ninjas already exists"
#
#
# def test_wrong_pk():
#     with pytest.raises(SchemaError) as e:
#         with DB() as db:
#             db.create("ninjas", DB_SCHEMA, "ID")
#
#     assert str(e.value) == "The provided primary key must be part of the schema."
#
#
# def test_insert(db):
#     assert db.num_transactions == 4
#     query = f"SELECT * FROM ninjas;"
#     output = db.cursor.execute(query).fetchall()
#     assert output == NINJAS
#
#
# def test_insert_twice(db):
#     with pytest.raises(sqlite3.IntegrityError) as e:
#         db.insert("ninjas", NINJAS)
#
#     assert str(e.value) in ("UNIQUE constraint failed: ninjas.ninja",
#                             "column ninja is not unique")
#
#
# @pytest.mark.parametrize(
#     "table, bad_values, expected",
#     [
#         ("ninjas", [("Bob",)], 2),
#         ("ninjas", [("Bob", 1000, 1)], 2),
#         ("ninjas", [tuple()], 2),
#         ("ninjas", [("Bob", 1000), ("pmayd",)], 2),
#     ],
# )
# def test_incorrect_number_of_values_for_insert(db, table, bad_values, expected):
#     with pytest.raises(SchemaError) as e:
#         db.insert(table, bad_values)
#     assert str(e.value) == f"Table {table} expects items with {expected} values."
#
#
# @pytest.mark.parametrize(
#     "table, bad_values, col, expected",
#     [
#         ("ninjas", [("Bob", "1000")], "bitecoins", int),
#         ("ninjas", [(1000, "Bob")], "ninja", str),
#         ("ninjas", [("Bob", 1000), ("pmayd", "128")], "bitecoins", int),
#     ],
# )
# def test_wrong_value_type_for_insert(db, table, bad_values, col, expected):
#     with pytest.raises(SchemaError) as e:
#         db.insert(table, bad_values)
#
#     assert str(e.value) == f"Column {col} expects values of type {expected.__name__}."
#
#
# @pytest.mark.parametrize(
#     "table, col, expected",
#     [
#         ("ninjas", None, NINJAS),
#         ("ninjas", ["ninja"], sorted([(e[0],) for e in NINJAS])),
#         ("ninjas", ["bitecoins"], [(e[1],) for e in NINJAS]),
#     ],
# )
# def test_select(db, table, col, expected):
#     rows = db.select(table, col)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, target, expected",
#     [
#         ("ninjas", ("ninja", "clamytoe"), [e for e in NINJAS if e[0] == "clamytoe"]),
#         ("ninjas", ("bitecoins", 906), [e for e in NINJAS if e[1] == 906]),
#     ],
# )
# def test_select_db_target(db, table, target, expected):
#     row = db.select(table, target=target)
#     assert row == expected
#
#
# @pytest.mark.parametrize(
#     "table, target, expected",
#     [
#         ("ninjas", ("bitecoins", ">", 900), [e for e in NINJAS if e[1] > 900]),
#         ("ninjas", ("ninja", "LIKE", "%pot%"), [e for e in NINJAS if "pot" in e[0]]),
#         ("ninjas", ("ninja", "<>", "Tomade"), [e for e in NINJAS if e[0] != "Tomade"]),
#     ],
# )
# def test_select_operator(db, table, target, expected):
#     rows = db.select(table, target=target)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, new_value, target, expected",
#     [
#         ("ninjas", ("bitecoins", 1000), ("ninja", "clamytoe"), [("clamytoe", 1000)]),
#         ("ninjas", ("ninja", "tomade"), ("ninja", "Tomade"), [("tomade", 896)]),
#     ],
# )
# def test_update_db(db, table, new_value, target, expected):
#     db.update("ninjas", new_value, target)
#     assert db.num_transactions == 5
#
#     rows = db.select(table, target=new_value)
#     assert rows == expected
#
#
# @pytest.mark.parametrize(
#     "table, target", [("ninjas", ("ninja", "clamytoe")), ("ninjas", ("bitecoins", 906))]
# )
# def test_delete_db(db, table, target):
#     db.delete(table, target)
#     rows = db.select(table, target=target)
#     assert rows == []
#
#
# from wc import calc_median_from_dict
# import pytest
#
#
# # Small Numbers
# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         ({1: 1}, 1),
#         ({1: 1, 2: 1}, 1.5),
#         ({1: 2, 2: 1, 3: 2}, 2),
#         ({2: 1, 1: 2, 3: 2}, 2),
#         ({1.5: 2, 2.5: 2}, 2),
#         ({1.75: 2, 2.25: 2}, 2),
#         ({-1: 22, +4: 22}, 1.5),
#     ],
# )
# def test_median_from_dict__valid_numbers(test_input, expected):
#     assert calc_median_from_dict(test_input) == expected
#
#
# # Huge numbers
# @pytest.mark.parametrize(
#     "test_input,expected",
#     [
#         ({1: 1_000_000_000_000_000, 2: 1, 3: 1_000_000_000_000_000}, 2),
#         ({1: 1_000_000_000_000_000, 3: 1_000_000_000_000_000}, 2),
#         (
#             {
#                 0: 800_000_000,
#                 1: 200_000_000,
#                 2: 200_000_000,
#                 3: 200_000_000,
#                 4: 200_000_000,
#                 5: 1_000_000_000,
#                 6: 20_000_000_000,
#                 7: 4_000_000_000,
#                 8: 8_000_000_000,
#                 9: 16_000_000_000,
#             },
#             7,
#         ),
#     ],
# )
# def test_median_from_dict_valid_huge_numbers(test_input, expected):
#     assert calc_median_from_dict(test_input) == expected
#
#
# # Errors should be raised when the dict value is not a number
# @pytest.mark.parametrize(
#     "test_input",
#     [
#         ({1: "a"}),
#         ({3: []}),
#     ],
# )
# def test_median_from_dict_raises_error(test_input):
#     with pytest.raises(TypeError):
#         calc_median_from_dict(test_input)
#
# from wc import Exercise, Workout, create_tables, engine
# from sqlalchemy import inspect
#
#
# def test_workout_is_a_table():
#     assert hasattr(Workout, "__table__"), "Workout must have table=True"
#
#
# def test_exercise_is_a_table():
#     assert hasattr(Exercise, "__table__"), "Exercise must have table=True"
#
#
# def test_workout_table_name():
#     assert Workout.__tablename__ == "workout"
#
#
# def test_exercise_table_name():
#     assert Exercise.__tablename__ == "exercise"
#
#
# def test_workout_has_id_field():
#     columns = {col.name: col for col in Workout.__table__.columns}
#     assert "id" in columns, "Workout must have 'id' field"
#     assert columns["id"].primary_key, "id must be a primary key"
#
#
# def test_workout_has_name_field():
#     columns = {col.name: col for col in Workout.__table__.columns}
#     assert "name" in columns, "Workout must have 'name' field"
#
#
# def test_exercise_has_id_field():
#     columns = {col.name: col for col in Exercise.__table__.columns}
#     assert "id" in columns, "Exercise must have 'id' field"
#     assert columns["id"].primary_key, "id must be a primary key"
#
#
# def test_exercise_has_name_field():
#     columns = {col.name: col for col in Exercise.__table__.columns}
#     assert "name" in columns, "Exercise must have 'name' field"
#
#
# def test_create_tables_creates_tables():
#     create_tables()
#
#     inspector = inspect(engine)
#     table_names = inspector.get_table_names()
#
#     assert "workout" in table_names, "workout table should exist after create_tables()"
#     assert (
#         "exercise" in table_names
#     ), "exercise table should exist after create_tables()"
#
#
# def test_engine_is_sqlite():
#     assert "sqlite" in str(engine.url), "Engine should use SQLite"

import pytest
from wc import (
    Exercise,
    Workout,
    add_exercise,
    add_workout,
    create_tables,
    engine,
)
from sqlmodel import Session, select


@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test."""
    create_tables()


def test_add_workout_returns_workout_with_id():
    workout = add_workout("Upper Body Day")

    assert isinstance(workout, Workout)
    assert workout.id is not None, "Workout id should be populated after insert"
    assert workout.name == "Upper Body Day"


def test_add_workout_saves_to_database():
    workout = add_workout("Leg Day")

    # Query the database to confirm it was saved
    with Session(engine) as session:
        statement = select(Workout).where(Workout.id == workout.id)
        result = session.exec(statement).first()

        assert result is not None, "Workout should exist in database"
        assert result.name == "Leg Day"


def test_add_multiple_workouts():
    workout1 = add_workout("Push Day")
    workout2 = add_workout("Pull Day")

    assert workout1.id != workout2.id, "Each workout should have unique id"
    assert workout1.id is not None
    assert workout2.id is not None


def test_add_exercise_returns_exercise_with_id():
    exercise = add_exercise("Bench Press")

    assert isinstance(exercise, Exercise)
    assert exercise.id is not None, "Exercise id should be populated after insert"
    assert exercise.name == "Bench Press"


def test_add_exercise_saves_to_database():
    exercise = add_exercise("Squats")

    # Query the database to confirm it was saved
    with Session(engine) as session:
        statement = select(Exercise).where(Exercise.id == exercise.id)
        result = session.exec(statement).first()

        assert result is not None, "Exercise should exist in database"
        assert result.name == "Squats"


def test_add_multiple_exercises():
    exercise1 = add_exercise("Deadlift")
    exercise2 = add_exercise("Pull Ups")

    assert exercise1.id != exercise2.id, "Each exercise should have unique id"
    assert exercise1.id is not None
    assert exercise2.id is not None


def test_ids_are_auto_incremented():
    workout1 = add_workout("Workout 1")
    workout2 = add_workout("Workout 2")

    assert workout2.id == workout1.id + 1, "IDs should auto-increment"