# from pathlib import Path
#
#
# def wc(file_ : Path):
#     """Takes an absolute file path/name, calculates the number of
#        lines/words/chars, and returns a string of these numbers + file, e.g.:
#        3 12 60 /tmp/somefile
#        (both tabs and spaces are allowed as separator)"""
#     line_count, word_count, char_count = 0, 0, 0
#     with open(file_,'rb') as input_file:
#         for l in input_file:
#             line_count += 1
#             char_count += len(l)
#             word_list =  l.split()
#             word_count += len(word_list)
#
#     return f"{line_count} {word_count} {char_count} {file_.name}"
#
#
# if __name__ == '__main__':
#     # make it work from cli like original unix wc
#     import sys
#     print(wc(sys.argv[1]))
#
#
# from pathlib import Path
# from typing import List
#
#
# def tail(filepath: Path, n: int) -> List[str]:
#     """
#     Similate Unix' "tail -n" command:
#     - Read in the file ("filepath").
#     - Parse it into a list of lines, stripping trailing newlines.
#     - Return the last "n" lines.
#     """
#     with open(filepath, 'r') as input_file:
#         lines = [l.strip() for l in input_file.readlines()]
#         return lines[-n:]
#
#
# text = 'abc'.lstrip('')
# import math
#
# def round_even(number):
#     """Takes a number and returns it rounded even"""
#     if (math.ceil(number) - number) > (number- math.floor(number)):
#         return math.floor(number)
#     elif (math.ceil(number) - number) < (number- math.floor(number)):
#         return math.ceil(number)
#     elif math.ceil(number)%2==0:
#         return math.ceil(number)
#     else:
#         return math.floor(number)
#
# from datetime import datetime
#
# THIS_YEAR = 2018
#
# def years_ago(date):
#     """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
#        Convert this date str to a datetime object (use strptime).
#        Then extract the year from the obtained datetime object and subtract
#        it from the THIS_YEAR constant above, returning the int difference.
#        So in this example you would get: 2018 - 2015 = 3"""
#
#     dt = datetime.strptime(date,"%d %b, %Y")
#     return THIS_YEAR - dt.year
#
#
# def convert_eu_to_us_date(date):
#     """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
#        Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
#        To enforce the use of datetime's strptime / strftime (over slicing)
#        the tests check if a ValueError is raised for invalid day/month/year
#        ranges (no need to code this, datetime does this out of the box)"""
#     dt = datetime.strptime(date, "%d/%m/%Y")
#     return dt.strftime("%m/%d/%Y")
#
# import requests
#
# CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'
#
# # pre-work: load JSON data into program
#
# with requests.Session() as s:
#     data = s.get(CAR_DATA).json()
#
# import json
# from collections import Counter
#
# example_data = [{"id":1,"automaker":"Dodge","model":"Ram Van 1500","year":1999},
#    {"id":2,"automaker":"Chrysler","model":"Town & Country","year":2002},
#    {"id":3,"automaker":"Porsche","model":"Cayenne","year":2008},
#   ]
#
# year = 2006
# model_list =[car_dict.get("automaker") for car_dict in data if car_dict.get("year")==year]
# results = Counter(model_list).most_common(1)[0][0]
#
# models =set(car_dict.get("model") for car_dict in data if car_dict.get("year")==year and car_dict.get("automaker")=='Nissan')
#
# import re
# str1 ='https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X'
#
# re_pattern = re.compile(r"\S+/dp/(?P<dp>\w+)/?")
# match_result = re.search(re_pattern, str1)
# dp_str = match_result.group("dp")
# f"http://www.amazon.com/dp/{dp_str}/?tag=pyb0f-20"
# print(dp_str)
#
# str1.split('dp/')

#
# """
# Write a function which checks the red blood cell compatibility between donor and recipient.
# https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
# For simplicity, the appearance of 8 basic types of blood is considered.
# The input of blood type can be in the form of:
#     pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
#     value of the pre-defined Bloodtype 0..7
#     pre defined text  e.g. "0-", "B+", "AB+", ...
#     If input value is not a required type TypeError is raised.
#     If input value is not in defined interval ValueError is raised.
# Keywords: enum, exception handling, multi type input
# """
# import string
#
# from import_close_day_balance import title

# import numpy as np

# import datetime
# import itertools
# import re
# import typing
# from itertools import count
# from operator import itemgetter
#
# import bs4.element
# from nbclient.exceptions import timeout_err_msg
# from sqlalchemy import false
#
# from alkami_profile_time import directory

# from collections import deque, OrderedDict
# from csv import DictReader
# from axiom_cd import result


#
# from enum import Enum
#
#
# class Bloodtype(Enum):
#     ZERO_NEG = 0
#     ZERO_POS = 1
#     B_NEG = 2
#     B_POS = 3
#     A_NEG = 4
#     A_POS = 5
#     AB_NEG = 6
#     AB_POS = 7
#
#
# blood_type_text = {
#     "0-": Bloodtype.ZERO_NEG,
#     "0+": Bloodtype.ZERO_POS,
#     "B-": Bloodtype.B_NEG,
#     "B+": Bloodtype.B_POS,
#     "A-": Bloodtype.A_NEG,
#     "A+": Bloodtype.A_POS,
#     "AB-": Bloodtype.AB_NEG,
#     "AB+": Bloodtype.AB_POS,
# }
#
# def check_typ(obj):
#     if not isinstance(obj,(Enum,str,int)):
#         raise TypeError
#
#     if type(obj) == int and (obj < 0 or obj > 7):
#         raise ValueError
#
#     if type(obj) == str and (obj not in blood_type_text.keys() ):
#         raise ValueError
#
# def convert_type(obj):
#     if isinstance(obj, Enum):
#         return obj.value
#
#     elif type(obj) == str:
#         return blood_type_text[obj].value
#
#     else:
#         return obj
#
# # complete :
# def check_bt(donor, recipient):
#     """ Checks red blood cell compatibility based on 8 blood types
#         Args:
#         donor (int | str | Bloodtype): red blood cell type of the donor
#         recipient (int | str | Bloodtype): red blood cell type of the recipient
#         Returns:
#         bool: True for compatability, False otherwise.
#     """
#     check_typ(donor)
#     check_typ(recipient)
#
#     donor = convert_type(donor)
#     recipient =  convert_type(recipient)
#
#     return all(num >= 0 for num in _particular_antigen_comp(donor, recipient))
#
#
# # hint
# def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
#     """Returns a particalar antigen compatibility, where each tuple member
#     marks a compatibility for a particular antigen  (A, B, Rh-D).
#     If tuple member is non-negative there is a compatibility.
#     For red blood cell compatibility is required that
#     all tuple members are non-negative (i.e. compatibility for all 3 antigens).
#     0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
#     Examples:
#     _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
#     _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
#     _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
#     _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
#     """
#     return (
#         ((recipient // 4) % 2) - ((donor // 4) % 2),
#         ((recipient // 2) % 2) - ((donor // 2) % 2),
#         (recipient % 2) - (donor % 2),
#     )
#
# NOT_FOUND = "Not found"
#
# group1 = {'tim': 30, 'bob': 17, 'ana': 24}
# group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
# group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}
#
#
# def get_person_age(name):
#     """Look up name (case insensitive search) and return age.
#        If name in > 1 dict, return the match of the group with
#        greatest N (so group3 > group2 > group1)
#     """
#     if type(name) != str:
#         return NOT_FOUND
#     lookup = [dictionary.get(name.lower()) for dictionary in (group1, group2, group3)]
#     result = list(filter(lambda x: x, lookup))
#     return result[-1] if len(result) >0 else NOT_FOUND
#
# def get_person_age(name):
#     """Look up name (case insensitive search) and return age.
#        If name in > 1 dict, return the match of the group with
#        greatest N (so group3 > group2 > group1)
#     """
#     name = name.lower() if isinstance(name, str) else name
#     # search goes in order of addition so as per requirements
#     # we insert groups from gt (#3) to lt (#1)
#     m = ChainMap(group3, group2, group1)
#     return m.get(name, NOT_FOUND)
# print(get_person_age('tim'))
#
# def sort_words_case_insensitively(words :list[str]):
#     """Sort the provided word list ignoring case, and numbers last
#        (1995, 19ab = numbers / Happy, happy4you = strings, hence for
#         numbers you only need to check the first char of the word)
#     """
#
#     return sorted(words,key= lambda word: ( word[0].isdigit() , word.casefold()))
# #
#
#
# sorted([(True,4  ), (False,3  ), (True, 6)],reverse=True)
#
# from datetime import datetime
# import re
#
# date_pattern = re.compile(r"Heritage.+_(?P<date>.+).csv")
#
# def get_process_date(file_name: str) -> int:
#     """Returns the processDate for a given csv file.
#     ProcessDate is needed for
#     Example file name: HeritageFCU_OLB.EDTOUT.VISEQSCR.OUTPUT_mm.dd.yyyy.csv
#     Example ProcessDate 20241106
#     """
#     match_result = re.search(date_pattern, file_name)
#     dt_str = match_result.group("date")
#     if dt_str is None:
#         print(f"Unable to parse process date:{file_name}")
#     date_obj = datetime.strptime(dt_str,"%m.%d.%Y")
#     return int(date_obj.strftime("%Y%m%d"))
#
# print(get_process_date('HeritageFCU_OLB.EDTOUT.VISEQSCR.OUTPUT_3.4.2024.csv'))
# import math
# # math.ceil(2.4)
# # math.floor(2.59)
#
# def round_up_or_down(transactions, up=True):
#     """Round the list of transactions passed in.
#        If up=True (default) round up, else round down.
#        Return a new list of rounded values
#     """
#     func = math.ceil if up else math.floor
#     return [func(transaction) for transaction in transactions]
#
# import os
#
#
#
# def count_dirs_and_files(directory='.'):
#     """Count the amount of of directories and files in passed in "directory" arg.
#        Return a tuple of (number_of_directories, number_of_files)
#     """
#     dir_count = 0
#     file_count = 0
#     for root, dirs, names in os.walk(top=directory):
#         dir_count += len(dirs)
#         file_count += len(names)
#     return dir_count, file_count
#
# from typing import List
#
# import re
# DEFAULT_SHELL = 'bash'
# # https://github.com/avar/git-anyonecanedit-etc/blob/master/passwd
# PASSWD_OUTPUT = """root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/bin/sh
# bin:x:2:2:bin:/bin:/bin/sh
# sys:x:3:3:sys:/dev:/bin/sh
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/bin/sh
# man:x:6:12:man:/var/cache/man:/bin/sh
# lp:x:7:7:lp:/var/spool/lpd:/bin/sh
# mail:x:8:8:mail:/var/mail:/bin/sh
# news:x:9:9:news:/var/spool/news:/bin/sh
# uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
# proxy:x:13:13:proxy:/bin:/bin/sh
# www-data:x:33:33:www-data:/var/www:/bin/sh
# backup:x:34:34:backup:/var/backups:/bin/sh
# list:x:38:38:Mailing List Manager:/var/list:/bin/sh
# irc:x:39:39:ircd:/var/run/ircd:/bin/sh
# gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
# nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
# libuuid:x:100:101::/var/lib/libuuid:/bin/sh
# Debian-exim:x:101:103::/var/spool/exim4:/bin/false
# statd:x:102:65534::/var/lib/nfs:/bin/false
# sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin
# ftp:x:104:65534::/home/ftp:/bin/false
# messagebus:x:105:106::/var/run/dbus:/bin/false
# mysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false
# avar:x:1000:1000::/home/avar:/bin/bash
# chad:x:1001:1001::/home/chad:/bin/bash
# git-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash
# gerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash
# avahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
# postfix:x:108:112::/var/spool/postfix:/bin/false
# ssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash
# artagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash"""
#
# def get_users_for_shell(passwd_output: str = PASSWD_OUTPUT,
#                         grep_shell: str = DEFAULT_SHELL) -> List[str]:
#     """Match the passwd_output string for users with grep_shell.
#        Return a list of users.
#     """
#     lines = passwd_output.splitlines()
#     return [line.split(":")[0] for line in lines if line.split("/")[-1]==grep_shell]
#

#
# def get_users_for_shell(passwd_output: str = PASSWD_OUTPUT,
#                         grep_shell: str = DEFAULT_SHELL) -> List[str]:
#     """Match the passwd_output string for users with grep_shell.
#        Return a list of users.
#     """
#     output = []
#     lines = passwd_output.splitlines()
#     for line in lines:
#         if line.split("/")[-1] == grep_shell:
#             output.append(line.split(":")[0])
#     return output

#
# def get_users_for_shell(passwd_output: str = PASSWD_OUTPUT,
#                         grep_shell: str = DEFAULT_SHELL) -> List[str]:
#     """Match the passwd_output string for users with grep_shell.
#        Return a list of users.
#     """
#     pattern = r"^(?P<user>[-A-Za-z0-9]+):.+/(?P<shell>\w+)$"
#     output = []
#     lines = passwd_output.splitlines()
#     for line in lines:
#         result = re.match(pattern, line)
#         if result and result.group("shell") == grep_shell:
#             output.append(result.group("user"))
#     return output
# get_users_for_shell()
#
# class User:
#     """A User class
#        (Django's User model inspired us)
#     """
#
#     def __init__(self, first_name, last_name):
#         """Constructor, base values"""
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def get_full_name(self):
#         """Return first and last name separated by a whitespace
#            and using title case for both.
#         """
#         return f'{self.first_name.title().strip()} {self.last_name.title().strip()}'
#
#
#
#
#     @property
#     def username(self):
#         """A username consists of the first char of
#            the user's first_name and the first 7 chars
#            of the user's last_name, both lowercased.
#
#            If this is your first property, check out:
#            https://pybit.es/articles/property-decorator/
#         """
#         # TODO 2: you code
#         return f"{self.first_name[0].lower()}{self.last_name.lower()[0:7]}"
#
#     # TODO 3: you code
#     #
#     # add a __str__ and a __repr__
#     # see: https://stackoverflow.com/a/1438297
#     # "__repr__ is for devs, __str__ is for customers"
#     #
#     # see also TESTS for required output
#
#     def __str__(self):
#         return f"{self.get_full_name} ({self.username})"
#
#     def __repr__(self):
#         """Don't hardcode the class name, hint: use a
#            special attribute of self.__class__ ...
#         """
#         class_name = self.__class__.__name__
#         return f"{class_name}('{self.first_name}', '{self.last_name}')"
# def convert(value: float, fmt: str) -> float:
#     """Converts the value to the designated format.
#
#     :param value: The value to be converted must be numeric or raise a TypeError
#     :param fmt: String indicating format to convert to
#     :return: Float rounded to 4 decimal places after conversion
#     """
#     value_type = type(value)
#     fmt=fmt.lower()
#     if (value_type != int) and (value_type != float):
#         raise TypeError
#
#     if fmt!='cm' and fmt!='in':
#         raise ValueError
#
#     if fmt=='cm':
#         return round(value * 2.54, 4)
#
#     if fmt=='in':
#         return round(value * 0.39370079,4)

#
# def convert(value: float, fmt: str) -> float:
#     """Converts the value to the designated format.
#
#     :param value: The value to be converted must be numeric or raise a TypeError
#     :param fmt: String indicating format to convert to
#     :return: Float rounded to 4 decimal places after conversion
#     """
#     fmt = fmt.lower()
#
#     if fmt not in FORMATS.keys():
#         raise ValueError(f"{fmt} is an unsupported format!")
#
#     try:
#         return round(value * FORMATS[fmt], 4)
#     except TypeError as e:
#         raise TypeError(f"{e} must be a numeric!")
#
# from functools import partial
#
# # create 2 partials:
# # - 'rounder_int' rounds to int (0 places)
# # - 'rounder_detailed' rounds to 4 places
# rounder_int = partial(round) # you code
# rounder_detailed = partial(round, ndigits=4) # you code
#
# rounder_int(23)
#
# WHITE, BLACK = ' ', '#'
#
#
# def create_chessboard(size=8):
#     """Create a chessboard with of the size passed in.
#        Don't return anything, print the output to stdout"""
#     for i in range(size // 2):
#         print_row(indent=True, n_stars= size // 2)
#         print_row(indent=False, n_stars = size//2)
#
# def print_row(indent:bool, n_stars):
#     star_str = " ".join([ '#' for i in range(n_stars)])
#     indent_str = ' ' + star_str if indent else star_str + ' '
#     print(indent_str)
#
# create_chessboard(8)
#
# from collections import defaultdict
#
# from jedi.parser_utils import find_statement_documentation
#
# # fake data from https://www.mockaroo.com
# data = """last_name,first_name,country_code
# Watsham,Husain,ID
# Harrold,Alphonso,BR
# Apdell,Margo,CN
# Tomblings,Deerdre,RU
# Wasielewski,Sula,ID
# Jeffry,Rudolph,TD
# Brenston,Luke,SE
# Parrett,Ines,CN
# Braunle,Kermit,PL
# Halbard,Davie,CN"""
#
#
# def group_names_by_country(data: str = data) -> defaultdict:
#     countries = defaultdict(list)
#     lines = data.splitlines()
#     for line in lines[1:]:
#         last_name, first_name, country_code = line.split(",")
#         countries[country_code].append(f"{first_name} {last_name}")
#     return countries

# import bisect
#
#
# class OrderedList:
#
#     def __init__(self):
#         self._numbers = []
#
#     def add(self, num):
#         # you complete
#         #bisect.insort(self._numbers, num)
#         indx=bisect.bisect(self._numbers, num)
#         self._numbers.insert(indx, num )
#
#     def __str__(self):
#         return ', '.join(str(num) for num in self._numbers)
#
# import os
# import statistics
# from urllib.request import urlretrieve
#
# TMP = os.getenv("TMP", "/tmp")
# S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# DATA = 'testfiles_number_loc.txt'
# STATS = os.path.join(TMP, DATA)
# if not os.path.isfile(STATS):
#     urlretrieve(os.path.join(S3, DATA), STATS)
#
# STATS_OUTPUT = """
# Basic statistics:
# - count     : {count:7d}
# - min       : {min_:7d}
# - max       : {max_:7d}
# - mean      : {mean:7.2f}
#
# Population variance:
# - pstdev    : {pstdev:7.2f}
# - pvariance : {pvariance:7.2f}
#
# Estimated variance for sample:
# - count     : {sample_count:7.2f}
# - stdev     : {sample_stdev:7.2f}
# - variance  : {sample_variance:7.2f}
# """

#
# def get_all_line_counts(data: str = STATS) -> list:
#     """Get all 186 line counts from the STATS file,
#        returning a list of ints"""
#     # TODO 1: get the 186 ints from downloaded STATS file
#     with open(data, 'r') as f:
#         return [int(line.split()[0]) for line in f]
#
#
# def create_stats_report(data=None):
#     if data is None:
#         # converting to a list in case a generator was returned
#         data = list(get_all_line_counts())
#
#     # taking a sample for the last section
#     sample = list(data)[::2]
#
#     # TODO 2: complete this dict, use data list and
#     # for the last 3 sample_ variables, use sample list
#     stats = dict(count=len(data),
#                  min_=min(data),
#                  max_=max(data),
#                  mean=statistics.mean(data),
#                  pstdev=statistics.pstdev(data),
#                  pvariance=statistics.pvariance(data),
#                  sample_count=len(sample),
#                  sample_stdev=statistics.stdev(sample),
#                  sample_variance=statistics.variance(sample),
#                  )
#
#     return STATS_OUTPUT.format(**stats)
#
# print(create_stats_report())
#
# IGNORE_CHAR = 'b'
# QUIT_CHAR = 'q'
# MAX_NAMES = 5

#
# def filter_names(names:list[str]) -> list[str]:
#     filtered_list=[]
#     for name in names:
#         if name[0] == QUIT_CHAR or len(filtered_list)==5:
#             break
#         if name[0] == IGNORE_CHAR or not name.isalpha():
#             continue
#         filtered_list.append(name)
#     return filtered_list

#
# def filter_names(names:list[str]) -> str:
#     count = 0
#     for name in names:
#         if name[0] == QUIT_CHAR or count==5:
#             return
#         if name[0] == IGNORE_CHAR or not name.isalpha():
#             return
#         count += 1
#         yield name
#
#
# import logging
# from typing import Callable
#
# logger = logging.getLogger("pybites_logger")
#
# DEBUG = logger.debug
# INFO = logger.info
# WARNING = logger.warning
# ERROR = logger.error
# CRITICAL = logger.critical
#
#
# def log_it(level: Callable, msg: str) -> None:
#     level(msg)
#
#
# if __name__ == "__main__":
#     log_it(DEBUG, "This is a debug message.")
#     log_it(INFO, "This is an info message.")
#     log_it(WARNING, "This is a warning message.")
#     log_it(ERROR, "This is an error message.")
#     log_it(CRITICAL, "This is a critical message.")
#
# import itertools
#
# def find_number_pairs(numbers, N=10):
#     combinations = itertools.combinations(numbers, 2)
#     return [ combo for combo in combinations if (combo[0] + combo[1] ==N) ]
# def sum_numbers(numbers:list[int]) -> int:
#     """Sums numbers
#
#     :param numbers: a list of numbers
#     :type numbers: list
#     :raises TypeError: if not all numeric values passed in
#     :return: sum of numbers
#     :rtype: int
#     """
#
# def countdown():
#     """Write a generator that counts from 100 to 1"""
#     return (i for i in range(100,0,-1) )

# import re
#
#
# def validate_license(key: str) -> bool:
#     """Write a regex that matches a PyBites license key
#        (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
#     """
#     pattern = r'^PB(?:-[A-Z0-9]{8}){4}$'
#     return bool(re.search(pattern, key))
# from functools import wraps
#
# UPPER_SLICE = "=== Upper bread slice ==="
# LOWER_SLICE = "=== Lower bread slice ==="
#
#
# def sandwich(func):
#     """Write a decorator that prints UPPER_SLICE and
#        LOWER_SLICE before and after calling the function (func)
#        that is passed in  (@wraps is to preserve the original
#        func's docstring)
#     """
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print(UPPER_SLICE)
#         func(*args, **kwargs)
#         print(LOWER_SLICE)
#     return wrapped
#
#
# @sandwich
# def sayhello():
#     print("Hello")
#
#
# sayhello()
#
# @sandwich
# def add(x,y):
#     return x+y
# add(3,4)
# PYBITES = "pybites"
#
# def convert_pybites_chars(text:str):
#     """Swap case all characters in the word pybites for the given text.
#        Return the resulting string."""
#
#     return ''.join([letter.swapcase() if letter.lower() in PYBITES.lower() else letter for letter in text ])

#
# print(convert_pybites_chars("Hello"))
# print(convert_pybites_chars(PYBITES))
#
# import re
# from typing import List
#
# # https://stackoverflow.com/a/43147265
# # just for exercise sake, real life use emoji lib
# IS_EMOJI = re.compile(r'[^\w\s,]')
#
#
# def get_emoji_indices(text: str) -> List[int]:
#     """Given a text return indices of emoji characters"""
#     return [i for i, t in enumerate(text) if re.search(IS_EMOJI,t)]
#
# from functools import cache
#
# @cache
# def fib(n):
#    if n < 0:
#         raise ValueError
#    elif n in (0, 1):
#        return n
#    else:
#        return fib(n-1) + fib(n-2)
#

#
# from typing import List
#
# def list_to_decimal(nums: List[int]) -> int:
#     """Accept a list of positive integers in the range(0, 10)
#        and return a integer where each int of the given list represents
#        decimal place values from first element to last.  E.g
#         [1,7,5] => 175
#         [0,3,1,2] => 312
#         Place values are 10**n where n represents the digit position
#         Eg to calculate 1345, we have 5 1's, 4 10's, 3 100's and 1 1000's
#         1,     3  ,  4  , 5
#         1000's, 100's, 10's, 1's
#     """
#     for num in nums:
#         if isinstance(num, bool) or not isinstance(num, int):
#             raise TypeError
#         elif not num in range(0, 10):
#             raise ValueError
#
#     return int(''.join(map(str, nums)))
#
# WORKOUTS = {'mon': 'upper body #1',
#             'tue': 'lower body #1',
#             'wed': '30 min cardio',
#             'thu': 'upper body #2',
#             'fri': 'lower body #2'}
#
#
# def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
#     """Print the days (comma separated and title cased) of my_workouts
#        that (partially) match the workout string passed in. If no
#        workout matches, print 'No matching workout'
#     """
#     days = [day.title() for day, wo in my_workouts.items()
#             if workout.lower() in wo.lower()]
#     print(', '.join(days) if days else 'No matching workout')
#
# import string
# import numpy as np
# import pandas as pd
#
#
# def basic_series() -> pd.Series:
#     """Create a pandas Series containing the values 1, 2, 3, 4, 5
#     Don't worry about the indexes for now.
#     The name of the series should be 'Fred'
#     """
#     return pd.Series(range(1,6), name='Fred')
#
#
#
# def float_series() -> pd.Series:
#     """Create a pandas Series containing the all the values
#     from 0.000 -> 1.000 e.g. 0.000, 0.001, 0.002... 0.999, 1.000
#     Don't worry about the indexes or the series name.
#     """
#     return pd.Series(np.linspace(0,1,1001))
#
#
# def alpha_index_series() -> pd.Series:
#     """Create a Series with values 1, 2, ... 25, 26 of type int64
#     and add an index with values a, b, ... y, z
#     so index 'a'=1, 'b'=2 ... 'y'=25, 'z'=26
#     Don't worry about the series name.
#     """
#     return pd.Series(range(1,27), index=(c for c in string.ascii_lowercase))
#
#
#
# def object_values_series() -> pd.Series:
#     """Create a Series with values A, B, ... Y, Z of type object
#     and add an index with values 101, 102, ... 125, 126
#     so index 101='A', 102='B' ... 125='Y', 126='Z'
#     Don't worry about the series name.
#     """
#     return pd.Series(data=(c for c in string.ascii_uppercase),
#                      index=range(101,127))
#
# import numpy as np
# import pandas as pd
#
#
# def return_at_index(ser: pd.Series, idx: int) -> object:
#     """Return the Object at the given index of the Series
#     If you want to be extra careful catch and raise an error if
#        the index does not exist.
#     """
#     return ser[idx]
#
#
# def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
#     """Return the slice of the given Series in the range between
#     start and end.
#     """
#     return ser[start:end]
#
#
# def get_slice_inclusive(ser: pd.Series,
#                         start: int, end: int) -> pd.core.series.Series:
#     """Return the slice of the given Series in the range between
#     start and end inclusive.
#     """
#     return ser[start:end+1]
#
#
# def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
#     """Return the first num elements of the given Series.
#     """
#     return ser.head(num)
#
#
#
# def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
#     """Return the last num elements of the given Series.
#     """
#     return ser.tail(num)
#
#
# def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
#     """Return all indexes of the given Series.
#     """
#     return ser.index
#
#
# def get_values(ser: pd.Series) -> np.ndarray:
#     """Return all the values of the given Series.
#     """
#     return ser.values
#
#
# def get_every_second_indexes(ser: pd.Series,
#                              even_index=True) -> pd.core.series.Series:
#     """Return all rows where the index is either even or odd.
#     If even_index is True return every index where idx % 2 == 0
#     If even_index is False return every index where idx % 2 != 0
#     Assume default indexing i.e. 0 -> n
#     """
#     if even_index:
#         return ser[0::2]
#     return ser[1::2]
#
# num_hundreds = -1
#
# def sum_numbers(numbers: list) -> int:
#     """Sums passed in numbers returning the total, also
#        update the global variable num_hundreds with the amount
#        of times 100 fits in total"""
#     total=sum(numbers)
#     global num_hundreds
#     num_hundreds += (total//100)
#     return  total
#
# import re
#
#
# def get_users(passwd: str) -> dict:
#     """Split password output by newline,
#       extract user and name (1st and 5th columns),
#       strip trailing commas from name,
#       replace multiple commas in name with a single space
#       return dict of keys = user, values = name.
#     """
#     lines = passwd.strip().splitlines()
#     user_dict = {}
#     for line in lines:
#         fields = line.split(':')
#         user, name = fields[0], fields[4].rstrip(',')
#         if name == '':
#             name = 'unknown'
#         name = re.sub(r',+', ' ', name)
#         user_dict[user] = name
#     return user_dict
#
# def calculate_gc_content(sequence):
#     """
#     Receives a DNA sequence (A, G, C, or T)
#     Returns the percentage of GC content (rounded to the last two digits)
#     """
#     total, gc_count = 0, 0
#     for char in sequence:
#         c = char.lower()
#         if c in ('c','g'):
#             gc_count += 1
#         if c in ('a' ,'c', 't', 'g'):
#             total += 1
#     return round((gc_count/total*100),2)

#
# from collections import Counter
#
#
# def freq_digit(num: int) -> int:
#     ctr=Counter(str(num))
#     return int(ctr.most_common(1)[0][0])
#
# from collections import Counter
#
# def major_n_minor(numbers):
#     """
#     Input: an array with integer numbers
#     Output: the majority and minority number
#     """
#     num_list = list(Counter(numbers).most_common())
#     return num_list[0][0], num_list[-1][0]
# def is_armstrong(n: int) -> bool:
#     n_str = str(n)
#     total = 0
#     for c in n_str:
#         total+=pow(int(c),len(n_str))
#     return total==n

# def is_armstrong(n: int) -> bool:
#     n_str = str(n)
#     return sum([pow(int(c), len(n_str)) for c in n_str]) == n
#
# from datetime import datetime,timedelta
#
# def tomorrow(today:datetime.date=None)->datetime.date:
#     if not today:
#         today=datetime.now().date()
#     return today + timedelta(days=1)
#
# from typing import List
# from functools import reduce
#
# def minimum_number(digits: List[int]) -> int:
#     # make into unique digits
#     # sort the digits from small to large
#     # convert back to int.
#
#     return int(reduce (lambda x,y: x+y , map(str, sorted(set(digits))))) if digits else 0
#
# from math import ceil
#
# def round_to_next(number: int, multiple: int):
#     return ceil(number / multiple) * multiple
#
# from typing import List, TypeVar
#
# from avid_test_file import new_line
#
# T = TypeVar('T', int, float)
# from functools import reduce
#
# def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
#     if n < 1:
#         raise ValueError
#     return list(map(digit_helper,numbers,[n for _ in range(len(numbers))]))
#
# def get_digits(number:int)->List[int]:
#     return [int(c) for c in str(number) if c not in ('.','-')]
#
# def digit_helper(number, n):
#     number_is_negative = True if number < 0 else False
#     num_list = get_digits(number)
#     new_number_str = reduce(lambda x, y: x + y, map(str, num_list[:n]))
#     new_number=int(new_number_str.ljust(n,'0'))
#     return new_number * -1 if number_is_negative else new_number

#
# from typing import List, Union
#
#
# def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
#     if lst_of_lst:
#         new_list =[]
#         for lst in lst_of_lst:
#             new_list = [*new_list, *lst, sep]
#         new_list.pop()
#         return new_list
#
# def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
#     if lst_of_lst:
#         new_list =[]
#         for lst in lst_of_lst:
#             new_list = [*new_list, *lst, sep]
#         new_list.pop()
#         return new_list
#
#
# join_lists([['1','2'],['3','4']],'&')
#
# def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
#     if lst_of_lst == []:
#         return None
#     new_list = []
#     iter1 = iter(lst_of_lst)
#     lst = next(iter1, 'end')
#     while lst!='end':
#         for item in lst:
#             new_list.append(item)
#         new_list.append(sep)
#         lst = next(iter1, 'end')
#         if lst=='end':
#             new_list.pop()
#     return new_list
#
# from typing import List  # not needed when we upgrade to 3.9
#
# def names():
#     return ["Bob", "Julian", "Tim", "Sara", "Eva", "Ana", "Jake", "Maria"]
#
#
# def print_names_to_columns(names: List[str], cols: int = 2) -> None:
#     formated_names = ''.join(['| '+ name.strip().ljust(10) +'\n' if (i+1)%cols==0 else '| '+ name.strip().ljust(10) for i,name in enumerate(names) ])
#     print(formated_names)

# print_names_to_columns(names())
#
# from datetime import date
# import os
# from pathlib import Path
# import pickle
# from typing import Sequence, NamedTuple
# from urllib.request import urlretrieve
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
# PICKLE_INFILE = TMP / 'input.pkl'
# PICKLE_OUTFILE = TMP / 'output.pkl'
#
#
# class MovieRented(NamedTuple):
#     title: str
#     price: int
#     date: date
#
#
# def download_pickle_file():
#     """download a pickle file we created with a
#        list of namedtuples
#     """
#     urlretrieve(f'{S3}/bite317.pkl', PICKLE_INFILE)
#
#
# def deserialize(pkl_file: Path = PICKLE_INFILE) -> Sequence[NamedTuple]:
#     """Load the list of namedtuples from the pickle file passed in"""
#     with open(pkl_file,'rb') as f:
#         return pickle.load(f)
#
# def serialize(pkl_file: Path = PICKLE_OUTFILE,
#               data: Sequence[NamedTuple] = None) -> None:
#     """Save the data passed in to the pickle file passed in"""
#     if data is None:
#         data = deserialize()
#     with open(pkl_file,'wb') as f:
#         pickle.dump(data, f)
#
#
#
# import base64
# import csv
# from typing import List  # will remove with 3.9
#
#
# def get_credit_cards(data: bytes) -> List[str]:
#     """Decode the base64 encoded data which gives you a csv
#     of "first_name,last_name,credit_card", from which you have
#     to extract the credit card numbers.
#     """
#     return [line.split(',')[2] for i, line in enumerate(base64.b64decode(data).decode().splitlines()) if i > 0]
#
# TODO: Fix age and same_configuration functions (see test results)
# class Car:
#     """
#     Car class
#     -> Have a closer look at lines marked with '# *'
#     """
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def __eq__(self, other_car):
#         return (
#             self.model.lower() == other_car.model.lower()
#             and self.color.lower() == other_car.color.lower()
#         )
#
#     @staticmethod
#     def age(days):
#         """if / elif / else for exercise sake, if there would
#            be more conditions we would use a dict / mapping
#         """
#         if days == 7:  # *
#             return "A week old"
#         elif days == 365:  # *
#             return "A year old"
#         else:
#             return "Neither a week, nor a year old"
#
#     @staticmethod
#     def has_same_configuration(config1, config2):
#         if type(config1) != list or type(config2) != list:  # *
#             raise TypeError()
#         return config1 == config2  # *
#
#
# # TODO: Complete function
# def is_same_car_color_and_model(car1, car2):
#     """
#     Returns true if car1 and car2 are the of same model and color
#     """
#     return car1.model.lower() == car2.model.lower() and car1.color.lower() == car2.color.lower()
#
#
#
# # TODO: Complete function
# def is_same_instance_of_car(car1, car2):
#     """
#     Returns true if car1 and car2 are exactly the same object (instance)
#     """
#     return car1 is car2


#
#
# from datetime import datetime
#
#
# def ontrack_reading(books_goal: int, books_read: int,
#                     day_of_year: int = None) -> bool:
#     if not day_of_year:
#         day_of_year = datetime.now().timetuple().tm_yday
#     target_rate = books_goal / 365
#     current_rate = books_read / day_of_year
#     return current_rate >= target_rate
#
# print(ontrack_reading(10,10,365))
#
# import functools
# from typing import Iterable, Set, Any
#
# def intersection_helper(s1=None, s2=None):
#     s1 = set() if s1 is None else set(s1)
#     s2 = set() if s2 is None else set(s2)
#
#     if not s1:
#         return s2
#     if not s2:
#         return s1
#     return s1 & s2
#
#
# def intersection(*args: Iterable) -> Set[Any]:
#     return functools.reduce(intersection_helper, args,set())
#

#
# import pprint
# from typing import Any
#
#
# def pretty_string(obj: Any) -> str:
#     # TODO: your code
#     return pprint.pformat(obj, width=60, depth=2, sort_dicts=True)

# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# async def root()->dict:
#     return {"message":"Hello World"}
#
# from pydantic import BaseModel
#
# # write a Food pydantic model
# class Food(BaseModel):
#     id: int
#     name: str
#     serving_size: str
#     kcal_per_serving: int
#     protein_grams: float
#     fibre_grams: float = 0.0

# from enum import Enum
#
# class Hand(str, Enum):
#     RIGHT = "right"
#     LEFT = "left"
#     BOTH = "both"
#
#
# LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
# RIGHT_HAND_CHARS = set("YUIOPHJKLNM")
#
#
# def get_hand_for_word(word: str) -> Hand:
#     """
#     Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
#     if the passed in word can be written with only the left or right
#     hand, or if both hands are needed.
#     """
#     left_needed, right_needed = False, False
#
#     for char in word:
#         if char.upper() in LEFT_HAND_CHARS:
#             left_needed = True
#         if char.upper() in RIGHT_HAND_CHARS:
#             right_needed = True
#
#         if left_needed and right_needed:
#             return Hand.BOTH
#
#     return Hand.LEFT if left_needed else Hand.RIGHT
#
#
# import typer  # use typer.run and typer.Argument
# from typing_extensions import Annotated
#
# def sum_numbers(a: int, b: int):
#     """Sums two numbers"""
#     return a + b
#
#
# def main(a:Annotated[int, typer.Argument(help="The value of the first summand")],
#          b:Annotated[int, typer.Argument(help="The value of the second summand")]
# ):
#     """
#     CLI that allows you to add two numbers
#     """
#     print(sum_numbers(a,b))  # edit this
#
#
# if __name__ == "__main__":
#     typer.run(main)

# import typer
#
# def sum_numbers(a: int, b: int):
#     return a + b
#
# app = typer.Typer()
# @app.command()
# def sum(
#     a: int = typer.Argument(..., help='The value of the first summand'),
#     b: int = typer.Argument(..., help='The value of the second summand')
# ):
#     """Command that allows you to add two numbers."""
#     sum_ab = sum_numbers(a, b)
#
#     print(f"The sum is {sum_ab}")
#
#
# @app.command()
# def compare(
#     c: int = typer.Argument(..., help='First number to compare against.'),
#     d: int = typer.Argument(..., help='Second number that is compared against first number.')
# ):
#     """Command that checks whether a number d is greater than a number c."""
#
#     STRING_TRUE = "greater"
#     STRING_FALSE = "not greater"
#
#     c_evaluation = STRING_TRUE if d > c else STRING_FALSE
#
#     print(f"{d=} is {c_evaluation} than {c=}")
#
#
# if __name__ == "__main__":
#     app()
#
#
# import time
# import typer
# from rich.progress import track
#
# app = typer.Typer()
#
# @app.command()
# def progress():
#     total = 0
#     for value in track(range(100), description="Processing..."):
#         # Fake processing time
#         time.sleep(0.01)
#         total += 1
#     print(f"Processed {total} things.")
#
#
# if __name__ == "__main__":
#     app()
#
# def combine_and_count(a: dict, b: dict) -> dict:
#     """Combine two dictionaries.
#
#     Return  new dictionary with the combined keys and values.
#     For any key found in both dictionaries,
#     return the sum of the values for that key.
#
#     Args:
#       a: The first dictionary.
#       b: The second dictionary.
#
#     Returns:
#       A dictionary with the contents of both.
#       Values of any shared keys are summed.
#     """
#     # Your code goes here.
#     # find common keys from both dictionries
#     # sum them
#     if type(a) != dict or type(b) != dict:
#         raise TypeError
#
#     common_dict = { key_a: a[key_a]+b[key_b] for key_a in a.keys() for key_b in b.keys() if key_a == key_b}
#     return a | b | common_dict
#
# import string
#
#
# def validate_pangram(sentence: str) -> bool:
#     """Check if a sentence is a pangram
#     A pangram is a sentence containing every letter in the English alphabet.
#     The input `sentence` should be a string containing only English letters.
#     The function returns True if the sentence is a pangram, and False otherwise.
#     """
#     return not {c.upper() for c in string.ascii_uppercase}.difference({c.upper() for c in sentence})
#
#
#
# if __name__ == "__main__":
#     validate_pangram()
# import string as STR
#
# def reverse_letters(string: str) -> str:
#     """Reverse letters in a string but keep the order of the non-letters the same"""
#     location_dict = {}
#     letter_list = []
#
#     for i, char in enumerate(string):
#         if char.upper() not in STR.ascii_uppercase:
#             location_dict[i]=char
#         else:
#             letter_list.append(char)
#
#     return ''.join([ location_dict[i] if i in location_dict.keys() else letter_list.pop() for i in range(len(string))])
#
#
#
#
# if __name__ == "__main__":
#     reverse_letters()
#
# import string
#
# VOWELS = "aeiou"
# EXTENSIONS = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]
#
#
# def upper_helper(text: str) -> str:
#     new_str = ''
#     for char in text:
#         if char.lower() not in string.ascii_lowercase:
#             new_str += ' '
#         elif char.lower() in VOWELS:
#             new_str += char.upper()
#         else:
#             new_str += char.lower()
#     return new_str
#
# def is_file_name(text:str) -> bool:
#     for e in EXTENSIONS:
#         if text.endswith(e):
#             return True
#     return  False
#
# def uppercase_vowels(text: str) -> str:
#     if is_file_name(text):
#         file_name, extension = text.split('.')
#         return upper_helper(file_name) + '.' + extension
#     return upper_helper(text)

#
# import os
# import urllib.request
#
# # PREWORK
# TMP = os.getenv("TMP", "/tmp")
# S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# DICT = 'dictionary.txt'
# DICTIONARY = os.path.join(TMP, DICT)
# urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)
#
# scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
#                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
# LETTER_SCORES = {letter: score for score, letters in scrabble_scores
#                  for letter in letters.split()}
#
# # start coding
#
# def load_words():
#     """Load the words dictionary (DICTIONARY constant) into a list and return it"""
#     with open(DICTIONARY, 'r') as f:
#         return [line.strip() for line in f]
#
#
# def calc_word_value(word):
#     """Given a word calculate its value using the LETTER_SCORES dict"""
#     return sum([ LETTER_SCORES[c.upper()] if c.upper() in LETTER_SCORES else 0 for c in word  ])
#
#
# def max_word_value(words):
#     """Given a list of words calculate the word with the maximum value and return it"""
#     return max(words, key=calc_word_value)
#
# import os
# from collections import Counter
# import urllib.request
# import xml.etree.ElementTree as ET
#
# # prep
# tmp = os.getenv("TMP", "/tmp")
# tempfile = os.path.join(tmp, 'feed')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/feed',
#     tempfile
# )
#
# with open(tempfile) as f:
#     content = f.read().lower()
#
#
# def get_pybites_top_tags(n=10):
#     """use Counter to get the top 10 PyBites tags from the feed
#        data already loaded into the content variable"""
#
#     category_list = [j for line in content.split('<category>') for j in line.split('</category>') if
#                      len(j.split()) <= 3 and j != '']
#     tags = Counter(category_list)
#     return tags.most_common(n)
#
#
# get_pybites_top_tags()

# from collections import Counter, namedtuple
# import os
# import urllib.request
#
# # prep
# tmp = os.getenv("TMP", "/tmp")
# tempfile = os.path.join(tmp, 'dirnames')
# # urllib.request.urlretrieve(
# #     'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
# #     tempfile
# # )
#
# IGNORE = ['static', 'templates', 'data', 'pybites', 'bbelderbos', 'hobojoe1848']
#
# Stats = namedtuple('Stats', 'user challenge')
#
#
# # code
#
# def gen_files(tempfile=tempfile):
#     """
#     Parse the tempfile passed in, filtering out directory names
#     (first column) using the last "is_dir" column.
#
#     Lowercase these directory names and return them as a generator.
#
#     "tempfile" has the following format:
#     challenge<int>/file_or_dir<str>,is_dir<bool>
#
#     For example:
#     03/rss.xml,False
#     03/tags.html,False
#     03/Mridubhatnagar,True
#     03/aleksandarknezevic,True
#
#     => Here you would return 03/mridubhatnagar (lowercased!)
#        followed by 03/aleksandarknezevic
#     """
#     with open(tempfile,'r') as f:
#         for line in f:
#             if line.split(',')[1].strip()=='True':
#                 num_, dir_ = line.split('/')
#                 yield num_ + '/' + dir_.lower().strip().split(',')[0]
#
#
#
#
# def diehard_pybites(files=None):
#     """
#     Return a Stats namedtuple (defined above) that contains:
#     1. the user that made the most pull requests (ignoring the users in IGNORE), and
#     2. a tuple of:
#         ("most popular challenge id", "amount of pull requests for that challenge")
#
#     Calling this function on the default dirnames.txt should return:
#
#     Stats(user='clamytoe', challenge=('01', 7))
#     """
#     if files is None:
#         files = gen_files()
#
#     users = Counter()
#     popular_challenges = Counter()
#
#     # your code
#     files = list(files)
#     users.update([line.split('/')[1]  for line in files if line.split('/')[1] not in IGNORE] )
#     most_prolific_user = users.most_common(1)
#     popular_challenges.update([line.split('/')[0]  for line in files if line.split('/')[1] not in IGNORE] )
#     most_popular_challenge = popular_challenges.most_common(1)
#     return Stats(most_prolific_user[0][0], most_popular_challenge[0])
#
#
# from datetime import datetime
# import os
# import urllib.request
#
# SHUTDOWN_EVENT = 'Shutdown initiated'
#
# # prep: read in the logfile
# tmp = os.getenv("TMP", "/tmp")
# logfile = os.path.join(tmp, 'log')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
#     logfile
# )
#
# with open(logfile) as f:
#     loglines = f.readlines()
#
#
# # for you to code:
#
# def convert_to_datetime(line):
#     """TODO 1:
#        Extract timestamp from logline and convert it to a datetime object.
#        For example calling the function with:
#        INFO 2014-07-03T23:27:51 supybot Shutdown complete.
#        returns:
#        datetime(2014, 7, 3, 23, 27, 51)
#     """
#     return datetime.strptime(line.split()[1],'%Y-%m-%dT%H:%M:%S')
#
#
#
# def time_between_shutdowns(loglines):
#     """TODO 2:
#        Extract shutdown events ("Shutdown initiated") from loglines and
#        calculate the timedelta between the first and last one.
#        Return this datetime.timedelta object.
#     """
#     shut_down_start = None
#     shut_down_complete = None
#     found_shut_down_start = False
#     for line in loglines:
#         words = line.split()
#         if words[-2] == 'Shutdown' and words[-1] == 'initiated.' and not found_shut_down_start:
#             shut_down_start = convert_to_datetime(line)
#             found_shut_down_start = True
#         elif words[-2] == 'Shutdown' and words[-1] == 'complete.' :
#             shut_down_complete = convert_to_datetime(line)
#
#     return shut_down_complete - shut_down_start


# """A palindrome is a word, phrase, number, or other sequence of characters
# which reads the same backward as forward"""
# import os
# import urllib.request
# import string
#
# TMP = os.getenv("TMP", "/tmp")
# DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
#     DICTIONARY
# )
#
#
# def load_dictionary():
#     """Load dictionary (sample) and return as generator (done)"""
#     with open(DICTIONARY) as f:
#         return (word.lower().strip() for word in f.readlines())
#
# def is_palidrome_helper(char_list:list):
#     if len(char_list)<=1:
#         return True
#     elif char_list[0]!=char_list[-1]:
#         return False
#     else:
#         return is_palidrome_helper(char_list[1:-1])
#
# def is_palindrome(word):
#     """Return if word is palindrome, 'madam' would be one.
#        Case insensitive, so Madam is valid too.
#        It should work for phrases too so strip all but alphanumeric chars.
#        So "No 'x' in 'Nixon'" should pass (see tests for more)"""
#
#     # strip off
#     char_only_list = [char.upper() for char in word if char in string.ascii_letters]
#     return is_palidrome_helper(char_only_list)
#
#
# def get_longest_palindrome(words=None):
#     """Given a list of words return the longest palindrome
#        If called without argument use the load_dictionary helper
#        to populate the words list"""
#     if words is None:
#         words = load_dictionary()
#
#     palindrom_words = [w for w in words if is_palindrome(w)]
#     return max(palindrom_words, key=len)
#

#
# def positive_divide(numerator, denominator):
#     if type(numerator) != float and type(numerator) != int:
#         raise TypeError
#
#     if type(denominator) != float and type(denominator) != int:
#         raise TypeError
#
#     if numerator * denominator < 0:
#         raise ValueError
#
#     try:
#         result= numerator / denominator
#
#     except ZeroDivisionError:
#         return 0
#
#     return result
#
# print(positive_divide(1,2))
#
# def positive_divide(numerator, denominator):
#     try:
#         result = numerator/denominator
#     except ZeroDivisionError:
#         return 0
#     except (TypeError, ValueError):
#         raise
#     else:
#         if result < 0:
#             raise ValueError('Cannot be negative')
#         return result
#
# from collections import namedtuple
#
# User = namedtuple('User', 'name role expired')
# USER, ADMIN = 'user', 'admin'
# SECRET = 'I am a very secret token'
#
# julian = User(name='Julian', role=USER, expired=False)
# bob = User(name='Bob', role=USER, expired=True)
# pybites = User(name='PyBites', role=ADMIN, expired=False)
# USERS = (julian, bob, pybites)
#
# # define exception classes here
# class UserDoesNotExist(Exception):
#     pass
#
# class UserAccessExpired(Exception):
#     pass
#
# class UserNoPermission(Exception):
#     pass
#
#
# def get_secret_token(username:str):
#     # find user
#     valid_user = None
#     for user in USERS:
#         if username == user.name:
#             valid_user = user
#
#     if valid_user is None:
#         raise UserDoesNotExist()
#
#     if valid_user.expired:
#         raise UserAccessExpired()
#
#     if valid_user.role != 'admin':
#         raise UserNoPermission
#
#     return SECRET
#
# get_secret_token('PyBites') == SECRET

# from collections import namedtuple
# from datetime import datetime
# import json
# from typing import NamedTuple
#
# blog = dict(name='PyBites',
#             founders=('Julian', 'Bob'),
#             started=datetime(year=2016, month=12, day=19),
#             tags=['Python', 'Code Challenges', 'Learn by Doing'],
#             location='Spain/Australia',
#             site='https://pybit.es')
#
#
# # define namedtuple here
# # Nt = namedtuple('Nt',['name', 'founders','started', 'tags', 'location', 'site' ])
# Nt = namedtuple('Nt', blog.keys())
#
# def dict2nt(dict_):
#     return Nt(**dict_)
#     #return Nt( *(value for value in dict_.values()) )
#     #return Nt(** {key: value for key, value in dict_.items()} )
#
# def nt2json(nt):
#     dt_obj: datetime = nt.started
#     nt = nt._replace(started=str(dt_obj))
#     return json.dumps(nt._asdict())
#
# import random
#
# names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
# aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
# points = random.sample(range(81, 101), 6)
# awake = [True, False] * 3
# SEPARATOR = ' | '
#
#
# def generate_table(*args):
#   return (SEPARATOR.join( list (map(str, element) )) for element in zip(*args))
# import itertools
#
#
# def friends_teams(friends, team_size=2, order_does_matter=False):
#     # if order_does_matter:
#     #     return itertools.permutations(friends, team_size)
#     # return itertools.combinations(friends, team_size)
#
#     return itertools.permutations(friends, team_size) if order_does_matter else itertools.combinations(friends, team_size)
#
# import os
# import urllib.request
# from collections import Counter
#
# # data provided
# tmp = os.getenv("TMP", "/tmp")
# stopwords_file = os.path.join(tmp, 'stopwords')
# harry_text = os.path.join(tmp, 'harry')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
#     stopwords_file
# )
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
#     harry_text
# )
#
# # generator for the text
# def get_text():
#     with open(harry_text,'r', encoding='utf-8') as f:
#         for line in f:
#             for word in line.split():
#                 valid_word = ''.join(filter(str.isalnum, word.strip().lower()))
#                 if valid_word:
#                     yield valid_word
#
# # generator for the stop words
# def get_stop_words():
#     with open(stopwords_file,'r', encoding='utf-8') as f:
#         for line in f:
#             yield line.lower().strip()
#
# # generator for the valid words
# def get_valid_words():
#     return (text_word for text_word in get_text() if text_word not in get_stop_words() )
#
# def get_harry_most_common_word():
#     return Counter(get_valid_words()).most_common(1)[0]
#
# from functools import wraps, reduce
#
# def make_html(element):
#     def factory(func):
#         def wrapper(*args):
#             return f"<{element}>{func(*args)}</{element}>"
#         return wrapper
#     return factory


#
# from functools import wraps
#
#
# def int_args(func):
#     @wraps(func)
#     # complete this decorator
#     def wrapper(*args):
#         for i in args:
#
#             if type(i) !=int:
#                 raise TypeError
#             if i<0:
#                 raise ValueError
#
#         return func(*args)
#     return wrapper
#
# @int_args
# def my_add(a,b,c):
#     return a+b+c

#
# print(my_add(1,2,3))
# print(my_add(1,'2',3))

# import string
#
# PUNCTUATION_CHARS = list(string.punctuation)
# used_passwords = set('PassWord@1 PyBit$s9'.split())
#
# def string_contains(password, characters, number_of_occurrences):
#     return len([c for c in password if c in characters]) >= number_of_occurrences
# def check_length(password):
#     return 6 <= len(password) <= 12
# def check_digit(password):
#     return string_contains(password, string.digits, 1)
# def check_lower_case(password):
#     return string_contains(password, string.ascii_lowercase, 2)
# def check_upper_case(password):
#     return string_contains(password, string.ascii_uppercase, 1)
# def check_punctuation_mark(password):
#     return string_contains(password, PUNCTUATION_CHARS, 1)
# def check_previous_use(password):
#     return password not in used_passwords
#
# PW_CRITIRIA ={
#     'password_length': check_length,
#     'contains_digit': check_digit,
#     'has_lower_case': check_lower_case,
#     'has_upper_case': check_upper_case,
#     'has_punctuation': check_punctuation_mark,
#     'has_not_been_used': check_previous_use,
# }
#
# def validate_password(password):
#     for criteria in PW_CRITIRIA.values():
#         if not criteria(password):
#             return False
#     used_passwords.add(password)
#     return True
#
# import functools
#
# known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
# loggedin_users = ['mike', 'sue']
#
# def login_required(func):
#     @functools.wraps(func)
#     def wrapper(user):
#         if user not in known_users:
#             return "please create an account"
#         if user not in loggedin_users:
#             return "please login"
#         return func(user)
#     return wrapper
#
# @login_required
# def welcome(user):
#     '''Return a welcome message if logged in'''
#     return f'welcome back {user}'
#
# import random
#
# BITES = {6: 'PyBites Die Hard',
#          7: 'Parsing dates from logs',
#          9: 'Palindromes',
#          10: 'Practice exceptions',
#          11: 'Enrich a class with dunder methods',
#          12: 'Write a user validation function',
#          13: 'Convert dict in namedtuple/json',
#          14: 'Generate a table of n sequences',
#          15: 'Enumerate 2 sequences',
#          16: 'Special PyBites date generator',
#          17: 'Form teams from a group of friends',
#          18: 'Find the most common word',
#          19: 'Write a simple property',
#          20: 'Write a context manager',
#          21: 'Query a nested data structure'}
# BITES_DONE = {6, 10, 16, 18, 21}
#
#
# class NoBitesAvailable(Exception):
#     """There are no more Bites available to pick from"""
#
#
# class Promo:
#     def __init__(self):
#         # updated Bite to make local copies (avoid globals!)
#         self.all_bites = BITES.copy()
#         self.bites_done = BITES_DONE.copy()
#
#     def _pick_random_bite(self):
#         """Pick a random Bite that is not done yet, if all
#            Bites are done, raise a NoBitesAvailable exception"""
#
#         if len(self.bites_done) == len(BITES):
#             raise NoBitesAvailable
#
#         # get Bites that are not done
#         return random.choice([key for key in self.all_bites.keys() if key not in self.bites_done])
#
#
#     def new_bite(self):
#         """Get  a random Bite using _pick_random_bite,
#            add it to self.bites_done, then return it"""
#         random_bite = self._pick_random_bite()
#         self.bites_done.add(random_bite)
#         return random_bite
#
# # #
# # p1 = Promo()
# # print(p1.new_bite())
# #
# # p2 = Promo()
# # print(p2.new_bite())
# BITES.keys() - BITES_DONE
# self.all_bites.keys() - self.bites_done
# set([1,2,3]) - set([1])

#
#
# import json
#
#
# def get_movie_data(files: list) -> list:
#     """Parse movie json files into a list of dicts"""
#     movie_data=[]
#     for file_path in files:
#         with open(file_path, 'r') as f:
#             data = json.load(f)
#             movie_data.append(data)
#     return movie_data
#
#
# def get_single_comedy(movies: list) -> str:
#     """return the movie with Comedy in Genres"""
#     for movie in movies:
#         if 'Comedy' in movie.get('Genre'):
#             return movie.get('Title')
#
# def get_movie_most_nominations(movies: list) -> str:
#     """Return the movie that had the most nominations"""
#     nomination_dict = {movie.get('Title'): movie.get('imdbVotes') for movie in movies}
#     return max(nomination_dict, key=lambda k: int(nomination_dict[k].replace(',','')))
#
# def get_movie_longest_runtime(movies: list) -> str:
#     """Return the movie that has the longest runtime"""
#     runtime_dict = {movie.get('Title'): movie.get('Runtime') for movie in movies}
#     return max(runtime_dict, key=lambda k: int(runtime_dict[k].split()[0]))
#
# import json
# import re
#
#
# def get_movie_data(files: list) -> list:
#     """Parse movie json files into a list of dicts"""
#     movies = []
#     for fi in files:
#         with open(fi) as f:
#             json_ = json.loads(f.read())
#         movies.append(json_)
#     return movies
#
#
# def _grep_movies(movies, key):
#     for movie in movies:
#         yield movie.get('Title'), movie.get(key)
#
#
# def get_single_comedy(movies: list) -> str:
#     """Return the movie with Comedy in Genres"""
#     movies = dict(_grep_movies(movies, 'Genre'))
#     comedies = {k: v for k, v in movies.items() if 'Comedy' in v}
#     return list(comedies.keys())[0]
#
#
# def get_movie_most_nominations(movies: list) -> str:
#     """Return the movie that had the most nominations"""
#     movies = dict(_grep_movies(movies, 'Awards'))
#     extract_nominations = lambda m: int(re.sub(r'.*\s(\d+)\snomin.*', r'\1', m[1]))  # noqa E731 E501
#     return max(movies.items(), key=extract_nominations)[0]
#
#
# def get_movie_longest_runtime(movies: list) -> str:
#     """Return the movie that has the longest runtime"""
#     movies = dict(_grep_movies(movies, 'Runtime'))
#     extract_runtime = lambda m: int(m[1].split()[0])  # noqa E731
#     return max(movies.items(), key=extract_runtime)[0]
#
# import collections
# from datetime import datetime
# import os
# import re
# from urllib.request import urlretrieve
# from collections import Counter
#
# BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# RSS_FEED = 'pybites_feed.rss.xml'
# PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
# TMP = os.getenv("TMP", "/tmp")
#
#
# def _get_dates():
#     """Downloads PyBites feed and parses out all pub dates returning
#        a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
#        'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
#     remote = os.path.join(BASE_URL, RSS_FEED)
#     local = os.path.join(TMP, RSS_FEED)
#     urlretrieve(remote, local)
#
#     with open(local) as f:
#         return PUB_DATE.findall(f.read())
#
# def convert_to_datetime(date_str):
#     """Receives a date str and convert it into a datetime object"""
#     return datetime.strptime(date_str,'%a, %d %b %Y %H:%M:%S %z')
#
# def get_month_most_posts(dates):
#     """Receives a list of datetimes and returns the month (format YYYY-MM)
#        that occurs most"""
#     return Counter([datetime.strftime(dt,'%Y-%m') for dt in dates]).most_common(1)[0][0]
#
# import csv
# from collections import defaultdict, namedtuple
# import os
# from urllib.request import urlretrieve
#
# BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
# TMP = os.getenv("TMP", "/tmp")
#
# fname = 'movie_metadata.csv'
# remote = os.path.join(BASE_URL, fname)
# local = os.path.join(TMP, fname)
# urlretrieve(remote, local)
#
# MOVIE_DATA = local
# MIN_MOVIES = 4
# MIN_YEAR = 1960
#
# Movie = namedtuple('Movie', 'title year score')
#
# def get_movies_by_director():
#     """Extracts all movies from csv and stores them in a dict,
#     where keys are directors, and values are a list of movies,
#     use the defined Movie namedtuple"""
#     director_dict = defaultdict(list)
#     with (open(local,'r' ,encoding='utf-8') as f):
#         reader = csv.DictReader(f)
#         for line in reader:
#             if all((line['director_name'], line['movie_title'], line['title_year'], float(line['imdb_score']))) and int(line['title_year'])>1960:
#                 director_key = line['director_name']
#                 movie_val = Movie(line['movie_title'].strip(), int(line['title_year']), float(line['imdb_score'])  )
#                 director_dict[director_key].append(movie_val)
#     return director_dict
#
#
#
# def calc_mean_score(movies):
#     """Helper method to calculate mean of list of Movie namedtuples,
#        round the mean to 1 decimal place"""
#     scores_list = [movie.score for movie in movies]
#     return round(sum(scores_list) / len(scores_list),1)
#
#
# def get_average_scores(directors):
#     """Iterate through the directors dict (returned by get_movies_by_director),
#        return a list of tuples (director, average_score) ordered by highest
#        score in descending order. Only take directors into account
#        with >= MIN_MOVIES"""
#     #directors = get_movies_by_director()
#     return sorted([(director, round(sum(m.score for m in movies )/len(movies),1)) for director, movies in directors.items() if len(movies) >= MIN_MOVIES],
#            key= lambda x: x[1], reverse=True)
#
# def transpose(data):
#     """Transpose a data structure
#     1. dict
#     data = {'2017-8': 19, '2017-9': 13}
#     In:  transpose(data)
#     Out: [('2017-8', '2017-9'), (19, 13)]
#
#     2. list of (named)tuples
#     data = [Member(name='Bob', since_days=60, karma_points=60,
#                    bitecoin_earned=56),
#             Member(name='Julian', since_days=221, karma_points=34,
#                    bitecoin_earned=78)]
#     In: transpose(data)
#     Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
#     """
#     if type(data)==dict:
#         return [tuple(key for key in data.keys()), tuple(value for value in data.values())]
#
#     # If it is namedtuple
#     output=[]
#     for field in data[0]._fields:
#         a = tuple(getattr(entry ,field) for entry in data)
#         output.append(a)
#     return output
#
# list(zip(*data))
#
# from datetime import datetime
# import heapq
#
# numbers = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]
# dates = [datetime(2018, 1, 23, 0, 0),
#          datetime(2017, 12, 19, 0, 0),
#          datetime(2017, 10, 15, 0, 0),
#          datetime(2019, 2, 27, 0, 0),
#          datetime(2017, 3, 29, 0, 0),
#          datetime(2018, 8, 11, 0, 0),
#          datetime(2018, 5, 3, 0, 0),
#          datetime(2018, 12, 19, 0, 0),
#          datetime(2018, 11, 19, 0, 0),
#          datetime(2017, 7, 7, 0, 0)]
# # static (outdated) copy of:
# # https://www.forbes.com/celebrities/list
# earnings_mln = [
#     {'name': 'Kevin Durant', 'earnings': 60.6},
#     {'name': 'Adele', 'earnings': 69},
#     {'name': 'Lionel Messi', 'earnings': 80},
#     {'name': 'J.K. Rowling', 'earnings': 95},
#     {'name': 'Elton John', 'earnings': 60},
#     {'name': 'Chris Rock', 'earnings': 57},
#     {'name': 'Justin Bieber', 'earnings': 83.5},
#     {'name': 'Cristiano Ronaldo', 'earnings': 93},
#     {'name': 'Beyoncé Knowles', 'earnings': 105},
#     {'name': 'Jackie Chan', 'earnings': 49},
# ]
#
#
# def get_largest_number(numbers, n=3):
#     heapq.heapify(numbers)
#     return heapq.nlargest(n,numbers)
#
#
# def get_latest_dates(dates, n=3):
#     heapq.heapify(dates)
#     return heapq.nlargest(n, dates)
#
#
# def get_highest_earnings(earnings_mln, n=3):
#     # heapq expects list to work with
#     # biuld a list of tuples where the first element is the earning, and the second is the dict
#     earning_list = [ (earning_dict['earnings'], earning_dict) for earning_dict in earnings_mln]
#     heapq.heapify(earning_list)
#     return [item[1] for item in heapq.nlargest(n,earning_list)]
#
# def get_profile(name, age, *args, **kwargs ):
#     if type(age) != int:
#         raise ValueError
#     if len(args) > 5:
#         raise ValueError
#     profile_dict={
#         'name':name,
#         'age':age,
#     }
#     if args:
#         profile_dict.update({'sports': sorted(args)})
#
#     if kwargs:
#         profile_dict.update({ 'awards': kwargs})
#
#     return profile_dict
#
# from datetime import datetime, timedelta
# import os
# import re
# from pickletools import string1
# from time import struct_time
# from typing import List
# import urllib.request
# from pathlib import Path

# getting the data
# COURSE_TIMES = os.path.join(
#     os.getenv("TMP", "/tmp"),
#     'course_timings'
# )
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
#     COURSE_TIMES
# )
#
# def get_all_timestamps() -> List[str]:
#     """Read in the COURSE_TIMES and extract all MM:SS timestamps.
#        Here is a snippet of the input file:
#
#        Start  What is Practical JavaScript? (3:47)
#        Start  The voice in your ear (4:41)
#        Start  Is this course right for you? (1:21)
#        ...
#
#         Return a list of MM:SS timestamps
#     """
#     pattern = r'Start .*\((?P<time>\d+:\d+)\)'
#     time_duration_list = []
#     with open(COURSE_TIMES,'r', newline='') as f:
#         for line in f:
#             a = re.match(pattern, line)
#             if a:
#                 time_duration_list.append(a.group("time"))
#     return time_duration_list
#
#
# def calc_total_course_duration(timestamps) -> str:
#     """Takes timestamps list as returned by get_all_timestamps
#        and calculates the total duration as HH:MM:SS"""
#     total_seconds = timedelta()
#     for t in timestamps:
#         min, sec =map(int,t.split(':'))
#         total_seconds += timedelta(minutes=min, seconds=sec)
#     minutes, seconds =divmod(total_seconds.seconds, 60)
#     hours, minutes = divmod(minutes, 60)
#     return f"{hours}:{minutes}:{seconds}"
#
# import os
# import urllib.request
#
# TMP = os.getenv("TMP", "/tmp")
# DATA = 'safari.logs'
# SAFARI_LOGS = os.path.join(TMP, DATA)
# PY_BOOK, OTHER_BOOK = '🐍', '.'
#
# urllib.request.urlretrieve(
#     f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
#     SAFARI_LOGS
# )
#
#
# def create_chart():
#     with open(SAFARI_LOGS,'r') as f:
#         previous_line = next(f)
#         previous_date = previous_line.split()[0]
#         print(f"{previous_date} ", end='')
#         for current_line in f:
#             current_date = current_line.split()[0]
#             if 'sending to slack channel' in current_line:
#                 if current_date != previous_date:
#                     print(f"\n{current_date} ", end='')
#                     previous_date = current_date
#                 if 'python' in previous_line.lower():
#                     print('🐍', end='')
#                 else:
#                     print('.', end='')
#             # keep track of states before moving on to next line
#             previous_line = current_line
#
# from collections import namedtuple
#
# from bs4 import BeautifulSoup as Soup
# import requests
#
# PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
# CONTENT = requests.get(PACKT).text
#
# Book = namedtuple('Book', 'title description image link')
#
#
# def get_book():
#     """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
#     soup = Soup(CONTENT, "html.parser")
#     title = soup.find(class_ ="dotd-title").text.strip()
#     book_info = soup.select('div.dotd-title ~ div')
#     description = book_info[0].text.strip()
#     image = soup.select("div.dotd-main-book-image img[src]")[0].attrs['src']
#     link = soup.select("div.dotd-main-book-image a")[0].attrs['href']
#     return Book(title,description,image,link)
#
# from datetime import datetime
#
# # https://pythonclock.org/
# PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
# BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
#
#
# def py2_earth_hours_left(start_date=BITE_CREATED_DT):
#     """Return how many hours, rounded to 2 decimals, Python 2 has
#        left on Planet Earth (calculated from start_date)"""
#     return round((PY2_DEATH_DT - start_date).total_seconds() / (60 * 60),2)
#
#
# def py2_miller_min_left(start_date=BITE_CREATED_DT):
#     """Return how many minutes, rounded to 2 decimals, Python 2 has
#        left on Planet Miller (calculated from start_date)"""
#     return round((PY2_DEATH_DT - start_date).total_seconds() / (60 *  24 * 365 * 7),2)
#
# import argparse
# from functools import reduce
# from operator import add,sub,mul,truediv
#
# def calculator(operation, numbers):
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#     operation_dict ={
#         'add': add,
#         'sub': sub,
#         'mul': mul,
#         'div': truediv,
#     }
#     if not numbers:
#         raise SystemExit
#
#     return round(reduce(operation_dict[operation], map(float,numbers)),2)
#
#
# def create_parser():
#     """TODO 2:
#        Create an ArgumentParser object:
#        - have one operation argument,
#        - have one or more integers that can be operated on.
#        Returns a argparse.ArgumentParser object.
#
#        Note that type=float times out here so do the casting in the calculator
#        function above!"""
#     parser = argparse.ArgumentParser(description='A simple calculator')
#     parser.add_argument('-a', '--add', help='Sums numbers', nargs='*')
#     parser.add_argument('-s', '--sub', help='Subtracts numbers', nargs='*')
#     parser.add_argument('-m', '--mul', help='Multiplies numbers', nargs='*')
#     parser.add_argument('-d', '--div', help='Divides numbers', nargs='*')
#     return parser
#
#
# def call_calculator(args=None, stdout=False):
#     """Provided/done:
#        Calls calculator with provided args object.
#        If args are not provided get them via create_parser,
#        if stdout is True print the result"""
#     parser = create_parser()
#
#     if args is None:
#         args = parser.parse_args()
#
#     # taking the first operation in args namespace
#     # if combo, e.g. -a and -s, take the first one
#     for operation, numbers in vars(args).items():
#         if numbers is None:
#             continue
#
#         try:
#             res = calculator(operation, numbers)
#         except ZeroDivisionError:
#             res = 0
#
#         if stdout:
#             print(res)
#
#         return res
#
# #
# # if __name__ == '__main__':
# #     call_calculator(stdout=True)
#
# create_parser()
#

#
# class MultiplicationTable:
#
#     def __init__(self, length):
#         """Create a 2D self._table of (x, y) coordinates and
#            their calculations (form of caching)"""
#         if type(length) == int:
#             self.x = self.y = length
#         else:
#             self.x, self.y = length
#
#         self.table = [[ i*j for j in range(1, self.y+1)] for i in range(1, self.x+1)]
#
#     def __len__(self):
#         """Returns the area of the table (len x* len y)"""
#         return self.x * self.y
#
#     def __str__(self):
#         """Returns a string representation of the table"""
#         output=''
#         for sublist in self.table:
#             output += ' | '.join(map(str,sublist)) + '\n'
#         return output
#
#
#     def calc_cell(self, x, y):
#         """Takes x and y coords and returns the re-calculated result"""
#         if x * y > self.x * self.y:
#             raise IndexError
#         self.x, self.y = x, y
#
#         return self.__len__()
#
# from collections import namedtuple
#
# SUITS = 'Red Green Yellow Blue'.split()
#
# UnoCard = namedtuple('UnoCard', 'suit name')
#
#
# def create_uno_deck():
#     """Create a deck of 108 Uno cards.
#        Return a list of UnoCard namedtuples
#        (for cards w/o suit use None in the namedtuple)"""
#     two_cards = [str(i) for i in range(1,10)]
#     additional_two_cards =['Draw Two', 'Skip', 'Reverse']
#     two_cards = two_cards + additional_two_cards
#     two_cards = [i for i in two_cards for j in range(2)]
#     four_cards = ['Wild', 'Wild Draw Four']
#     four_cards = [ UnoCard(None, i) for i in four_cards for j in range(4)]
#     one_card = ['0']
#     all_cards = one_card + two_cards
#     return [ UnoCard(i,j) for i in SUITS for j in all_cards] + four_cards
# from string import ascii_lowercase
# from functools import wraps
# from time import time
# from typing import Deque, List, Set, Generator
# from collections import deque
#
# def timing(f):
#     """A simple timer decorator to print the elapsed time of
#        the execution of the function it wraps.
#        Returns (timing, result) tuple"""
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = f(*args, **kwargs)
#         end = time()
#         duration = end - start
#         print(f'Elapsed time {f.__name__}: {duration}')
#         return duration, result
#     return wrapper
#
#
# @timing
# def contains(sequence: List[int], num: int) -> bool:
#     for n in sequence:
#         if n == num:
#             return True
#     return False
#
#
# @timing
# def contains_fast(sequence: Set[int], num: int) -> bool:
#     return num in sequence
#
#
# @timing
# def ordered_list_max(sequence: List[int]) -> int:
#     return max(sequence)
#
#
# @timing
# def ordered_list_max_fast(sequence: List[int]) -> int:
#     return sequence[-1]
#
#
# @timing
# def list_concat(sequence: List[str]) -> str:
#     bigstr = ''
#     for i in sequence:
#         bigstr += str(i)
#     return bigstr
#
#
# @timing
# def list_concat_fast(sequence: List[str]) -> str:
#     return ''.join(sequence)
#
#
# @timing
# def list_inserts(n: int) -> List[int]:
#     lst: List[int] = []
#     for i in range(n):
#         lst.insert(0, i)
#     return lst
#
#
# @timing
# def list_inserts_fast(n: int) -> Deque[int]:
#     dq = deque()
#     for i in range(n):
#         dq.appendleft(i)
#     return dq
#
# @timing
# def list_creation(n: int) -> List[int]:
#     lst = []
#     for i in range(n):
#         lst.append(i)
#     return lst
#
#
# @timing
# def list_creation_fast(n: int) -> Generator[int, None, None]:
#     return (i for i in range(n))


# This bite is essentially to find the max words from a draw

# steps:
# 1) Find all permutations of letters from a "draw" of letters
# 2) Check if the word is in the dictionary, if it is, return the word.
#
#
# import itertools
# import os
# import urllib.request
#
# # PREWORK
# TMP = os.getenv("TMP", "/tmp")
# DICT = 'dictionary.txt'
# DICTIONARY = os.path.join(TMP, DICT)
# urllib.request.urlretrieve(
#     f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
#     DICTIONARY
# )
#
# with open(DICTIONARY) as f:
#     dictionary = set([word.strip().lower() for word in f.read().split()])
#
#
# def get_possible_dict_words(draw):
#     """Get all possible words from a draw (list of letters) which are
#        valid dictionary words. Use _get_permutations_draw and provided
#        dictionary"""
#     all_permutation = _get_permutations_draw(draw)
#     return [p.lower() for p in all_permutation if p.lower() in dictionary]
#
# def _get_permutations_draw(draw):
#     """Helper to get all permutations of a draw (list of letters), hint:
#        use itertools.permutations (order of letters matters)"""
#     return [''.join(j) for i in range(1,len(draw)+1) for j in itertools.permutations(draw,i) ]
#
# from random import choice
#
# COLORS = 'red blue green yellow brown purple'.split()
#
#
# class EggCreator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current < self.limit:
#             self.current+=1
#             return choice(COLORS)
#         raise StopIteration
#
# class RecordScore():
#     """Class to track a game's maximum score"""
#     def __init__(self):
#         self.number = None
#
#     def __call__(self, number):
#         if not self.number:
#             self.number = number
#         elif number > self.number:
#             self.number = number
#         return self.number
# #
# import bisect
# scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
# belts = 'white yellow orange green blue brown black paneled red'.split()
#
#
# def get_belt(user_score, scores=scores, belts=belts):
#     position = bisect.bisect_right(scores,user_score)
#     if not position:
#         return None
#     return belts[position-1]
#
#
#
# def get_belt(user_score):
#     """new solution (see forum for old solution)"""
#     for score, belt in zip(scores[::-1], belts[::-1]):
#         if user_score >= score:
#             return belt
#
# from datetime import datetime
# from zoneinfo import ZoneInfo, available_timezones
#
# MIN_MEETING_HOUR = 6
# MAX_MEETING_HOUR = 22
# TIMEZONES = set(available_timezones())
#
#
# def within_schedule(utc: datetime, *timezones):
#     """
#     Receive a UTC datetime and one or more timezones and check if
#     they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
#     (both included).
#     """
#     tz_aware_datetime = utc.replace(tzinfo=ZoneInfo("UTC"))
#
#     for t in timezones:
#         if t not in TIMEZONES:
#             raise ValueError
#
#         local_hour = tz_aware_datetime.astimezone(ZoneInfo(t)).hour
#
#         if not MIN_MEETING_HOUR <= local_hour <= MAX_MEETING_HOUR:
#             return False
#     return True
# from functools import reduce
#
# def common_languages(programmers):
#     """Receive a dict of keys -> names and values -> a sequence of
#        of programming languages, return the common languages"""
#
#     languages_set = [set(s) for s in programmers.values()]
#     return reduce(lambda x,y:x&y,languages_set)
#
# import csv
#
# import requests
#
# CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'
# from collections import Counter
#
# def get_csv():
#     """Use requests to download the csv and return the
#        decoded content"""
#     response = requests.get(CSV_URL)
#     for line in response.text.split():
#         yield line
#
#
# def create_user_bar_chart(content):
#     """Receives csv file (decoded) content and print a table of timezones
#        and their corresponding member counts in pluses to standard output
#     """
#     iter = get_csv()
#     next(iter)
#     places =[line.split(',')[-1] for line in iter]
#     tally=Counter(places)
#     tally_dict = (sorted(tally.items()))
#
#     # Work on the printing function next
#     for country,count in tally_dict:
#         print(f"{country:<21}| " + '+'*count)
# from typing import NamedTuple
# from operator import attrgetter, lt, gt
#
#
# class Tweet(NamedTuple):
#     text: str
#     polarity: float
#
#
# tweets = [
#     Tweet(
#         text="It's shocking that the vast majority of online banking "
#         "systems have critical vulnerabilities leaving customer "
#         "accounts unprotected.",
#         polarity=-0.3333333333333333,
#     ),
#     Tweet(
#         text="The most unbelievable aspect of the Star Trek universe "
#         "is that every ship they meet has compatible video "
#         "conferencing facilities.",
#         polarity=0.125,
#     ),
#     Tweet(
#         text="Excellent set of tips for managing a PostgreSQL cluster "
#         "in production.",
#         polarity=1.0,
#     ),
#     Tweet(
#         text="This tutorial has a great line-by-line breakdown of how "
#         "to train a pong RL agent in PyTorch.",
#         polarity=0.8,
#     ),
#     Tweet(
#         text="This is some masterful reporting by ... It's also an "
#         "infuriating story. ... is trying to erase debt by preying "
#         "on the city’s residents. The poorest get hit the worst. "
#         "It’s shameful.",
#         polarity=-0.19999999999999998,
#     ),
# ]
#
#
# def filter_tweets_on_polarity(
#     tweets: list[Tweet], keep_positive: bool = True
# ) -> list[Tweet]:
#     """Filter the tweets based on their polarity score.
#
#     Args:
#         tweets (list): A list of Tweet namedtuples, each with a polarity score.
#         keep_positive (bool): If True, keeps only tweets with a positive polarity (polarity > 0).
#                               If False, keeps only tweets with a negative polarity (polarity < 0).
#
#     Returns:
#         list: A list of tweets filtered by the specified polarity condition.
#     """
#     func = gt if keep_positive else lt
#     return [tweet for tweet in tweets if func(tweet.polarity,0) ]
#
#
# def order_tweets_by_polarity(
#     tweets: list[Tweet], positive_highest: bool = True
# ) -> list[Tweet]:
#     """Sort tweets by their polarity score.
#
#     Args:
#         tweets (list): A list of Tweet namedtuples, each with a polarity score.
#         positive_highest (bool): If True, sorts tweets in descending order with the highest positive polarity first.
#                                  If False, sorts tweets in ascending order with the most negative polarity first.
#
#     Returns:
#         list: A list of tweets sorted by polarity according to the specified order.
#     """
#     reverse_status = True if positive_highest else False
#     return sorted(tweets,key=attrgetter('polarity'), reverse=reverse_status)
#
# from enum import Enum
#
# THUMBS_UP = '👍'  # in case you go f-string ...
#
# # move these into an Enum:
# BEGINNER = 2
# INTERMEDIATE = 3
# ADVANCED = 4
# CHEATED = 1
#
# class Score(Enum):
#     BEGINNER = 2
#     INTERMEDIATE = 3
#     ADVANCED = 4
#     CHEATED = 1
#
#     def __str__(self):
#         return f"{self.name} => {THUMBS_UP*self.value}"
#
#     @classmethod
#     def average(cls):
#         return sum([s.value for s in cls]) / len(cls)
#
# for level in Score:
#     print(str(level))
#
# def flatten(list_of_lists):
#     lst = []
#     for element in list_of_lists:
#         if type(element) == list or type(element)==tuple:
#             lst.extend(flatten(element))
#         else:
#             lst.append(element)
#     return lst
#
# inp = [1, (2, 3) ]
#
# print(flatten(inp))
#
#
# def dec_to_hex(number):
#     base10_to_base16_dict = {i:str(i) for i in range(10)}
#     letter_dict = { num:letter  for num, letter in zip(range(10,16), 'A B C D E F'.split())}
#     base10_to_base16_dict.update(letter_dict)
#     return f"{base10_to_base16_dict[number//16]}{base10_to_base16_dict[number%16]}"
#
#
# def rgb_to_hex(rgb):
#     """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
#        boundaries (0, 255) and returns its converted hex, for example:
#        Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
#     for base_10 in rgb:
#         if not ( 0<=base_10<=255 ):
#             raise ValueError
#     return f'#{"".join([dec_to_hex(base_10) for base_10 in rgb])}'

# How to convert decimal number to base 16 number
#
# from collections import OrderedDict
#
# def romanize(decimal_number):
#     """Takes a decimal number int and converts its Roman Numeral str"""
#     if not ((type(decimal_number)==int) and (0<decimal_number<4000)):
#         raise ValueError
#
#     roman_orderd_dict = OrderedDict(
#         [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#          (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')])
#
#     roman_list = []
#     for num, letter in roman_orderd_dict.items():
#         if decimal_number>=num:
#             quotient = decimal_number//num
#             roman_list.append(letter*quotient)
#             decimal_number = decimal_number % num
#
#     roman_numeral = ''.join(roman_list)
#     return roman_numeral
# us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
#                    'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
#                    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
#                    'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
#                    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
#                    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
#                    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
#                    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
#                    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
#                    'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
#                    'New Mexico': 'NM', 'New York': 'NY',
#                    'North Carolina': 'NC', 'North Dakota': 'ND',
#                    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
#                    'Pennsylvania': 'PA', 'Rhode Island': 'RI',
#                    'South Carolina': 'SC', 'South Dakota': 'SD',
#                    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
#                    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
#                    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}
#
# states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
#           'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
#           'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
#           'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
#           'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
#           'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
#           'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
#           'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
#           'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
#           'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
#           'Illinois', 'Iowa', 'Michigan', 'Delaware']
#
# NOT_FOUND = 'N/A'
#
#
# def get_every_nth_state(states=states, n=10):
#     """Return a list with every nth item (default argument n=10, so every
#        10th item) of the states list above (remember: lists keep order)"""
#
#     return [state for index, state in enumerate(states, start=1) if index%n==0]
#
#
# def get_state_abbrev(state_name, us_state_abbrev=us_state_abbrev):
#     """Look up a state abbreviation by querying the us_state_abbrev
#        dict by full state name, for instance 'Alabama' returns 'AL',
#        'Illinois' returns 'IL'.
#        If the state is not in the dict, return 'N/A' which we stored
#        in the NOT_FOUND constant (takeaway: dicts are great for lookups)"""
#     return us_state_abbrev.get(state_name,'N/A')
#
#
# def get_longest_state(data):
#     """Receives data, which can be the us_state_abbrev dict or the states
#        list (see above). It returns the longest state measured by the length
#        of the string"""
#
#     return max(data,key=len)
#
#
#
# def combine_state_names_and_abbreviations(us_state_abbrev=us_state_abbrev,
#                                           states=states):
#     """Get the first 10 state abbreviations from the (sorted) us_state_abbrev dict,
#        and the last 10 states from the (sorted) states list (see also above).
#        Combine these two lists into a new list and return it.
#        Here is the truncated resulting list (see also the tests):
#        ['AK', 'AL', 'AZ', ..., 'West Virginia', 'Wisconsin', 'Wyoming']"""
#     sorted_state_abbr = [us_state_abbrev[state] for state in sorted(us_state_abbrev,key = lambda x: us_state_abbrev[x])]
#     abbre_lst = sorted_state_abbr[:10]
#     state_lst = sorted(states)[-10:]
#     return abbre_lst + state_lst
#     #return sorted(us_state_abbrev.values())[:10] + sorted(states)[-10:]
#
# from collections import Counter, defaultdict
# import csv
# import requests
# import io
#
# CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501
#
#
# def get_season_csv_file(season):
#     """Receives a season int, and downloads loads in its
#        corresponding CSV_URL"""
#     with requests.Session() as s:
#         download = s.get(CSV_URL.format(season))
#         return download.content.decode('utf-8')
#
#
# def get_num_words_spoken_by_character_per_episode(content):
#     """Receives loaded csv content (str) and returns a dict of
#        keys=characters and values=Counter object,
#        which is a mapping of episode=>words spoken"""
#
#     data_file = io.StringIO(content)
#     reader = csv.DictReader(data_file)
#     characters_dict = defaultdict(lambda: Counter())
#
#     for row in reader:
#         characters_dict[row['Character']][row['Episode']] += len(row['Line'].split())
#     return characters_dict
#
# from collections import namedtuple
# from datetime import datetime
#
# TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')
#
# NOW = datetime.now()
# MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
# TIME_OFFSETS = (
#     TimeOffset(10, 'just now', None),
#     TimeOffset(MINUTE, '{} seconds ago', None),
#     TimeOffset(2*MINUTE, 'a minute ago', None),
#     TimeOffset(HOUR, '{} minutes ago', MINUTE),
#     TimeOffset(2*HOUR, 'an hour ago', None),
#     TimeOffset(DAY, '{} hours ago', HOUR),
#     TimeOffset(2*DAY, 'yesterday', None),
# )
#
#
# def pretty_date(date):
#     """Receives a datetime object and converts/returns a readable string
#        using TIME_OFFSETS"""
#     pass
#
# from collections import UserDict
# from datetime import date
# from xdrlib import raise_conversion_error
#
# from Demos.security.set_file_audit import dir_name
#
# MSG = 'Hey {}, there are more people with your birthday!'

#
#
# class BirthdayDict(UserDict):
#     """
#     Override UserDict to print a message every time a new person is added
#     that has the same birthday (day+month) as somebody already in the dict
#     """
#
#     def __setitem__(self, name, birthday):
#         has_birthday = any(birthday.strftime('%d/%m') == dt.strftime('%d/%m')
#                            for dt in self.values())
#
#         if has_birthday:
#             print(MSG.format(name))
#
#         super().__setitem__(name, birthday)


#
# class BirthdayDict(UserDict):
#     """
#     Override UserDict to print a message every time a new person is added
#     that has the same birthday (day+month) as somebody already in the dict
#     """
#
#     def __setitem__(self, key, value):
#         # Your logic here
#         for name, birthday in self.data.items():
#             birthday: date
#             if birthday.month == value.month and birthday.day == value.day:
#                 print(MSG.format(key))
#                 break
#
#         super().__setitem__(key, value)
#         # Check if there are any existing birthdays that matches.
#
#
#
# class BirthdayDict(UserDict):
#     """
#     Override UserDict to print a message every time a new person is added
#     that has the same birthday (day+month) as somebody already in the dict
#     """
#     def __setitem__(self, key, value):
#         # Your logic here
#         has_data = any(value.strftime('%m%d') ==birthday.strftime('%m%d')  for name, birthday in self.data.items())
#         if has_data:
#             print(MSG.format(key))
#         super().__setitem__(key, value)
#
#
#
#         # Check if there are any existing birthdays that matches.
#
#
#
# new_data={'Jim':date(1972,12,2)}
# b1 = BirthdayDict(new_data)
# b1['Mary'] = date(1900,12,2)
#
# bd = BirthdayDict()
# from collections import defaultdict
# import os
# from urllib.request import urlretrieve
#
# from bs4 import BeautifulSoup
#
#
# # prep data
# tmp = os.getenv("TMP", "/tmp")
# page = 'us_holidays.html'
# holidays_page = os.path.join(tmp, page)
# urlretrieve(
#     f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
#     holidays_page
# )
#
# with open(holidays_page) as f:
#     content = f.read()
#
# holidays = defaultdict(list)
#
#
# def get_us_bank_holidays(content=content):
#     """Receive scraped html output, make a BS object, parse the bank
#        holiday table (css class = list-table), and return a dict of
#        keys -> months and values -> list of bank holidays"""
#
#     soup = BeautifulSoup(content, "html.parser")
#     data_table =soup.find('table', class_='list-table').contents[4]
#     for time, name, in zip(data_table.find_all('time'), data_table.find_all('a')):
#         holidays[time.string.split('-')[1]].append(name.string.strip())
#     return holidays
#
# from itertools import cycle
# import string
#
# def sequence_generator():
#     for letter,number in zip(cycle(string.ascii_uppercase), cycle(range(1,len(string.ascii_uppercase)+1))):
#         yield number
#         yield letter
#
# import requests
#
# IPINFO_URL = 'http://ipinfo.io/{}/json'
#
#
# def get_ip_country(ip_address):
#     """Receives ip address string, use IPINFO_URL to get geo data,
#        parse the json response returning the country code of the IP"""
#
#     new_address = IPINFO_URL.format(ip_address)
#     response = requests.get(new_address)
#     ip_info = response.json()
#     return ip_info.get("country")
#


# def extract_non_ascii_words(text):
#     """Filter a text returning a list of non-ascii words"""
#     filter_list = []
#     for word in text.split():
#         for char in word:
#             if not 0<=ord(char)<128:
#                 filter_list.append(word)
#                 break
#     return filter_list
#
# def extract_non_ascii_words(text):
#     return [word for word in text.split() if any(char for char in word if not 0<=ord(char)<128)]
#
# import os
# import sys
# import urllib.request
#
# # PREWORK (don't modify): import colors, save to temp file and import
# tmp = os.getenv("TMP", "/tmp")
# color_values_module = os.path.join(tmp, 'color_values.py')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
#     color_values_module
# )
# sys.path.append(tmp)
#
# # should be importable now
# from color_values import COLOR_NAMES  # noqa E402
#
#
# class Color:
#     """Color class.
#
#     Takes the string of a color name and returns its RGB value.
#     """
#     def __init__(self, color:str):
#         self.color = color
#         self.rgb = COLOR_NAMES.get(color.upper())
#
#     @staticmethod
#     def hex2rgb(hex_str):
#         """Class method that converts a hex value into an rgb one"""
#
#         # Check valid format
#         if not (hex_str[0] == '#' and len(hex_str) == 7):
#             raise ValueError
#
#         for char in hex_str[1:]:
#             if not (48 <=ord(char)<=57 or 97 <=ord(char) <= 102):
#                 raise ValueError
#
#         letters_only_str = hex_str[1:]
#         return tuple([int(letters_only_str[index:index+2],16) for index, item in enumerate(letters_only_str) if index%2==0])
#
#
#
#     @staticmethod
#     def rgb2hex(rgb_tuple):
#         """Class method that converts an rgb value into a hex one"""
#         if type(rgb_tuple) != tuple:
#             raise ValueError
#
#         for val in rgb_tuple:
#             if not 0 <= val <=255:
#                 raise ValueError
#         return '#' + ''.join(["{:02x}".format(val) for val in rgb_tuple])
#
#
#     def __repr__(self):
#         """Returns the repl of the object"""
#         return f"Color('{self.color}')"
#
#     def __str__(self):
#         """Returns the string value of the color object"""
#         return str(self.rgb) if self.rgb else "Unknown"
#
# import os
# ONE_KB = 1024
# import glob

#
# def get_files(dirname, size_in_kb):
#     """Return files in dirname that are >= size_in_kb"""
#
#     file_list = []
#     for file in os.listdir(dirname):
#         complete_path = os.path.join(dirname,file)
#         if os.path.isfile(complete_path):
#             if os.stat(complete_path).st_size/ONE_KB >= size_in_kb:
#                 file_list.append(file)
#     return file_list
#
# def get_files(dirname, size_in_kb):
#     """Return files in dirname that are >= size_in_kb"""
#     return (file for file in glob.glob(f"{dirname}/*")
#         if os.stat(file).st_size/ONE_KB >= size_in_kb)
#
# from functools import wraps
#
#
# DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
#                 'new PyBites Code Challenges (PCCs) in your inbox')
# DOT = '.'
#
#
# def strip_range(start, end):
#     """Decorator that replaces characters of a text by dots, from 'start'
#        (inclusive) to 'end' (exclusive) = like range.
#
#         So applying this decorator on a function like this and 'text'
#         being 'Hello world' it would convert it into 'Hel.. world' when
#         applied like this:
#
#         @strip_range(3, 5)
#         def gen_output(text):
#             return text
#     """
#     def wrapper(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             my_str = func(*args, **kwargs)
#             return ''.join([DOT if start <= index < end else char for index, char in enumerate(my_str)])
#         return inner
#     return wrapper
#
# @strip_range(3, 5)
# def gen_output(text):
#     return text
#
# print(gen_output('My name is John. '))
#
# def get_duplicate_indices(words):
#     """Given a list of words, loop through the words and check for each
#        word if it occurs more than once.
#        If so return the index of its first occurrence.
#        For example in the following list 'is' and 'it'
#        occur more than once, and they are at indices 0 and 1 so you would
#        return [0, 1]:
#        ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
#        Make sure the returning list is unique and sorted in ascending order."""
#     word_location_dict = {}
#     word_index = []
#     for index, word in enumerate(words):
#         if  word_location_dict.get(word,None) is None:
#             word_location_dict[word] = index
#         else:
#             word_index.append(word_location_dict.get(word))
#     return sorted(set(word_index))
#
#
# from io import StringIO
#
# def generate_xmas_tree(rows=10):
#     """Generate a xmas tree of stars (*) for given rows (default 10).
#        Each row has row_number*2-1 stars, simple example: for rows=3 the
#        output would be like this (ignore docstring's indentation):
#          *
#         ***
#        *****"""
#
#     buffer = StringIO()
#     for i in range(1, rows + 1):
#         for j in range(1, rows + i):
#             if j > (rows - i):
#                 buffer.write("*")
#             else:
#                 buffer.write(" ")
#         buffer.write("\n")
#
#     return buffer.getvalue().rstrip()
#
# class Vehicle:
#     def __init__(self, brand: str, model: str, wheels: int):
#         # TODO: store brand, model, and wheels on self
#         self.brand = brand
#         self.model = model
#         self.wheels = wheels
#
#     def description(self) -> str:
#         """Return a string in the format '<brand> <model> with <wheels> wheels'"""
#         return f"{self.brand} {self.model} with {self.wheels} wheels"
#
#
# class Car(Vehicle):
#     def __init__(self, brand: str, model: str, wheels: int, doors: int):
#         # TODO: call parent __init__ using super()
#         # TODO: store doors
#         super().__init__(brand, model, wheels)
#         self.doors = doors
#
#     def honk(self) -> str:
#         """Return 'Beep beep!'"""
#         return "Beep beep!"
#
#
# class Motorbike(Vehicle):
#     def __init__(self, brand: str, model: str, wheels: int, engine_cc: int):
#         # TODO: call parent __init__ using super()
#         # TODO: store engine_cc
#         super().__init__(brand, model,wheels)
#         self.engine_cc = engine_cc
#
#     def rev_engine(self) -> str:
#         """Return '<parent class's description method> goes Vroom vroom!'"""
#         return f"{super().description()} goes Vroom vroom!"
#
# def is_anagram(word1, word2):
#     """Receives two words and returns True/False (boolean) if word2 is
#        an anagram of word1, ignore case and spacing.
#        About anagrams: https://en.wikipedia.org/wiki/Anagram"""
#
#     w1_list = [char.lower() for char in word1 if char != ' ']
#     w2_list = [char.lower() for char in word2 if char != ' ']
#     for char in w1_list:
#         try:
#             w2_list.remove(char)
#         except ValueError :
#             return False
#     if len(w2_list) > 0:
#         return False
#     return True
#
# from collections import defaultdict
#
# names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
# ids = range(len(names))
# users = dict(zip(ids, names))  # 0: bob, 1: julian, etc
#
# friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
#                (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
#                (6, 8), (7, 8), (8, 9)]
#
#
# def get_friend_with_most_friends(friendships, users=users):
#     """Receives the friendships list of user ID pairs,
#        parse it to see who has most friends, return a tuple
#        of (name_friend_with_most_friends, his_or_her_friends)"""
#     friendship_dict=defaultdict(set)
#     #insert into dictionary
#     for user, friend in friendships:
#        friendship_dict[user].add(friend)
#        friendship_dict[friend].add(user)
#
#         #sort dictionary based on length of dict
#     most_popular_key=sorted(friendship_dict,key=lambda key:len(friendship_dict[key]), reverse=True)[0]
#     return users[most_popular_key] , sorted([users[key] for key in friendship_dict[most_popular_key]])
#
# from collections import Counter
#
# from bs4 import BeautifulSoup
# import requests
# AMAZON = "amazon.com"
# # static copy
# TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
#             'tribe-mentors-books.html')
# MIN_COUNT = 3
#
#
# def load_page():
#     """Download the blog html and return its decoded content"""
#     with requests.Session() as session:
#         return session.get(TIM_BLOG).content.decode('utf-8')
#
#
# def get_top_books(content=None):
#     """Make a BeautifulSoup object loading in content,
#        find all links that contain AMAZON, extract the book title
#        (stripping spacing characters), and count them.
#        Return a list of (title, count) tuples where
#        count is at least MIN_COUNT
#     """
#     if content is None:
#         content = load_page()
#     # code here ...

# soup = BeautifulSoup(content, 'html.parser')
# b = soup.find_all('a', href=True)
# counter = Counter()
# for link in b:
#     if AMAZON in link['href'].lower():
#         counter.update([link.text.strip()] )
# filtered_counter = [(k,v) for k, v in counter.items() if v >= MIN_COUNT]
# return sorted(filtered_counter,key=lambda x: x[1], reverse=True)
#
# def get_ordinal_suffix(number):
#     """Receives a number int and returns it appended with its ordinal suffix,
#        so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.
#
#        Rules:
#        https://en.wikipedia.org/wiki/Ordinal_indicator#English
#        - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
#        - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
#        - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
#        - As an exception to the above rules, all the "teen" numbers ending with
#          11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
#          pronounced one hundred [and] twelfth)
#        - th is used for all other numbers (e.g. 9th, pronounced ninth).
#        """
#     if number%100 in (11, 12, 13):
#         return f"{number}th"
#
#     mod_10 = number%10
#     match mod_10:
#         case 1:
#             return f"{number}st"
#         case 2:
#             return f"{number}nd"
#         case 3:
#             return f"{number}rd"
#         case _:
#             return f"{number}th"

# Single Dispatch:
# from functools import singledispatch

# # data types to handle:
# # int,
# # str,
# # float,
# # list,
# # set,
# # tuple
# # dict
#
#
#
#
#
# @singledispatch
# def count_down(data_type):
#     # TODO: Learn how to use singledispatch!
#     pass

#
# import requests
# from collections import Counter
#
# STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'
#
# # pre-work: load JSON data into program
#
# with requests.Session() as s:
#     data = s.get(STOCK_DATA).json()
#
#
# # your turn:
#
# data1 = data[0]
#
# def _cap_str_to_mln_float(cap):
#     """If cap = 'n/a' return 0, else:
#        - strip off leading '$',
#        - if 'M' in cap value, strip it off and return value as float,
#        - if 'B', strip it off, multiply by 1,000 and return
#          value as float"""
#     if cap == 'n/a':
#         return 0
#     cap=cap.strip('$')
#     val = float(cap[:-1])
#     if cap[-1]=='B':
#         val*=1000
#     return val
#
# def get_industry_cap(industry):
#     """Return the sum of all cap values for given industry, use
#        the _cap_str_to_mln_float to parse the cap values,
#        return a float with 2 digit precision"""
#     cap_vals : list = [ _cap_str_to_mln_float(i.get("cap")) for i in data if i.get("industry")==industry]
#     return round(sum(cap_vals),2)
#
# def get_stock_symbol_with_highest_cap():
#     """Return the stock symbol (e.g. PACD) with the highest cap, use
#        the _cap_str_to_mln_float to parse the cap values"""
#
#     return max(data, key=lambda x: _cap_str_to_mln_float(x["cap"])).get('symbol')
#
#
# def get_sectors_with_max_and_min_stocks():
#     """Return a tuple of the sectors with most and least stocks,
#        discard n/a"""
#
#     sectors_list = [company['sector'] for company in data if company['sector']!='n/a']
#     counter=Counter(sectors_list)
#     return (counter.most_common()[0][0], counter.most_common()[-1][0])
#
# VOWELS = list('aeiou')
#
#
# def get_word_max_vowels(text):
#     """Get the case insensitive word in text that has most vowels.
#        Return a tuple of the matching word and the vowel count, e.g.
#        ('object-oriented', 6)"""
#     # break sentence into words
#     current_max = 0
#     current_word = ''
#     for word in text.split():
#         vowel_count = sum([1 for char in word if char.lower() in VOWELS])
#         if vowel_count > current_max:
#             current_word = word.lower()
#             current_max = vowel_count
#     return (current_word, current_max)
#
# VOWELS = list('aeiou')
#
#
# def _count_vowels(word):
#     return len([c for c in word if c in VOWELS])
#
#
# def get_word_max_vowels(text):
#     """Get the case insensitive word in text that has most vowels.
#        Return a tuple of the matching word and the vowel count, e.g.
#        ('object-oriented', 6)"""
#
#     words = text.lower().split()
#     words = [(word, _count_vowels(word)) for word in words]
#
#     return max(words, key=lambda x: x[1])


#
# from collections import namedtuple
# from datetime import datetime
# from operator import attrgetter
#
# Book = namedtuple('Book', 'title authors pages published')
#
# books = [
#     Book(title="Python Interviews",
#          authors="Michael Driscoll",
#          pages=366,
#          published="2018-02-28"),
#     Book(title="Python Cookbook",
#          authors="David Beazley, Brian K. Jones",
#          pages=706,
#          published="2013-05-10"),
#     Book(title="The Quick Python Book",
#          authors="Naomi Ceder",
#          pages=362,
#          published="2010-01-15"),
#     Book(title="Fluent Python",
#          authors="Luciano Ramalho",
#          pages=792,
#          published="2015-07-30"),
#     Book(title="Automate the Boring Stuff with Python",
#          authors="Al Sweigart",
#          pages=504,
#          published="2015-04-14"),
# ]
#
#
# # all functions return books sorted in ascending order.
#
# def sort_books_by_len_of_title(books=books):
#     """
#     Expected last book in list:
#     Automate the Boring Stuff with Python
#     """
#     return sorted(books, key=lambda book:len(book.title))
#
# def sort_books_by_first_authors_last_name(books=books):
#     """
#     Expected last book in list:
#     Automate the Boring Stuff with Python
#     """
#     return sorted(books, key=lambda book:book.authors.split(',')[0].split()[-1])
#
#
# def sort_books_by_number_of_page(books=books):
#     """
#     Expected last book in list:
#     Fluent Python
#     """
#     return sorted(books, key=lambda book:book.pages)
#
#
# def sort_books_by_published_date(books=books):
#     """
#     Expected last book in list:
#     Python Interviews
#     """
#     return sorted(books, key=lambda book:book.published)


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""
#
# from collections import Counter
# import operator
#
# CHEESES = [
#     "Red Leicester",
#     "Tilsit",
#     "Caerphilly",
#     "Bel Paese",
#     "Red Windsor",
#     "Stilton",
#     "Emmental",
#     "Gruyère",
#     "Norwegian Jarlsberg",
#     "Liptauer",
#     "Lancashire",
#     "White Stilton",
#     "Danish Blue",
#     "Double Gloucester",
#     "Cheshire",
#     "Dorset Blue Vinney",
#     "Brie",
#     "Roquefort",
#     "Pont l'Evêque",
#     "Port Salut",
#     "Savoyard",
#     "Saint-Paulin",
#     "Carré de l'Est",
#     "Bresse-Bleu",
#     "Boursin",
#     "Camembert",
#     "Gouda",
#     "Edam",
#     "Caithness",
#     "Smoked Austrian",
#     "Japanese Sage Derby",
#     "Wensleydale",
#     "Greek Feta",
#     "Gorgonzola",
#     "Parmesan",
#     "Mozzarella",
#     "Pipo Crème",
#     "Danish Fynbo",
#     "Czech sheep's milk",
#     "Venezuelan Beaver Cheese",
#     "Cheddar",
#     "Ilchester",
#     "Limburger",
# ]
#
# RED_WINES = [
#     "Châteauneuf-du-Pape",  # 95% of production is red
#     "Syrah",
#     "Merlot",
#     "Cabernet sauvignon",
#     "Malbec",
#     "Pinot noir",
#     "Zinfandel",
#     "Sangiovese",
#     "Barbera",
#     "Barolo",
#     "Rioja",
#     "Garnacha",
# ]
#
# WHITE_WINES = [
#     "Chardonnay",
#     "Sauvignon blanc",
#     "Semillon",
#     "Moscato",
#     "Pinot grigio",
#     "Gewürztraminer",
#     "Riesling",
# ]
#
# SPARKLING_WINES = [
#     "Cava",
#     "Champagne",
#     "Crémant d’Alsace",
#     "Moscato d’Asti",
#     "Prosecco",
#     "Franciacorta",
#     "Lambrusco",
# ]
#
# def _pair_score(wd1,wd2):
#     counter1, counter2 = Counter(wd1.lower()), Counter(wd2.lower())
#     common_len = sum((counter1 & counter2).values())
#     return common_len / (1 + pow(len(wd1) - len(wd2), 2))
#
# def _best_match_per_wine_type(wine_type):
#     wine_type_mapping ={
#         'red':RED_WINES,
#         'white':WHITE_WINES,
#         'sparkling':SPARKLING_WINES,
#     }
#     return max([(wine, cheese, _pair_score(wine, cheese)) for wine in wine_type_mapping[wine_type] for cheese in CHEESES], key=lambda x:x[2])
#
#
# def best_match_per_wine(wine_type="all"):
#     """ wine cheese pair with the highest match score
#     returns a tuple which contains wine, cheese, score
#     """
#     if wine_type not in ('red','white','sparkling','all'):
#         raise ValueError
#
#     if wine_type=='all':
#         wine_list = ['red','white','sparkling']
#     else:
#         wine_list = [wine_type]
#
#     return max([_best_match_per_wine_type(wine_type) for wine_type in wine_list], key=lambda x:x[2])
#
# def _best_cheese_per_wine(wine):
#     cheese_list=sorted([(cheese, _pair_score(wine, cheese)) for cheese in CHEESES], key=lambda x: (-x[1],x[0] ))
#     return [cheese[0] for index, cheese in enumerate(cheese_list) if index <5]
#
# def match_wine_5cheeses():
#     """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
#     where each tuple contains: wine, list of 5 best matching cheeses.
#     List of cheeses is sorted by score descending then alphabetically ascending.
#     e.g: [
#     ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
#     ...
#     ...
#     ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
#     ]
#     """
#     wine_list = RED_WINES + WHITE_WINES + SPARKLING_WINES
#     return sorted([(wine,_best_cheese_per_wine(wine)) for wine in wine_list], key=lambda x: x[0])

#
# from collections import Counter
# import operator
#
# CHEESES = [
#     "Red Leicester",
#     "Tilsit",
#     "Caerphilly",
#     "Bel Paese",
#     "Red Windsor",
#     "Stilton",
#     "Emmental",
#     "Gruyère",
#     "Norwegian Jarlsberg",
#     "Liptauer",
#     "Lancashire",
#     "White Stilton",
#     "Danish Blue",
#     "Double Gloucester",
#     "Cheshire",
#     "Dorset Blue Vinney",
#     "Brie",
#     "Roquefort",
#     "Pont l'Evêque",
#     "Port Salut",
#     "Savoyard",
#     "Saint-Paulin",
#     "Carré de l'Est",
#     "Bresse-Bleu",
#     "Boursin",
#     "Camembert",
#     "Gouda",
#     "Edam",
#     "Caithness",
#     "Smoked Austrian",
#     "Japanese Sage Derby",
#     "Wensleydale",
#     "Greek Feta",
#     "Gorgonzola",
#     "Parmesan",
#     "Mozzarella",
#     "Pipo Crème",
#     "Danish Fynbo",
#     "Czech sheep's milk",
#     "Venezuelan Beaver Cheese",
#     "Cheddar",
#     "Ilchester",
#     "Limburger",
# ]
#
# RED_WINES = [
#     "Châteauneuf-du-Pape",  # 95% of production is red
#     "Syrah",
#     "Merlot",
#     "Cabernet sauvignon",
#     "Malbec",
#     "Pinot noir",
#     "Zinfandel",
#     "Sangiovese",
#     "Barbera",
#     "Barolo",
#     "Rioja",
#     "Garnacha",
# ]
#
# WHITE_WINES = [
#     "Chardonnay",
#     "Sauvignon blanc",
#     "Semillon",
#     "Moscato",
#     "Pinot grigio",
#     "Gewürztraminer",
#     "Riesling",
# ]
#
# SPARKLING_WINES = [
#     "Cava",
#     "Champagne",
#     "Crémant d’Alsace",
#     "Moscato d’Asti",
#     "Prosecco",
#     "Franciacorta",
#     "Lambrusco",
# ]
#
#
# def _score(wine_type="all"):
#     """ scores wine-cheese pairs by similiarity of names
#                  sum of values of intersection of char counters of names
#     similarity = -------------------------------------------------------
#                  1 + square of length difference of names
#     returns a list of tuples, where each tuple contains: cheese, wine, score
#     """
#     wine_types = {"white": WHITE_WINES, "red": RED_WINES, "sparkling": SPARKLING_WINES}
#     if wine_type == "all":
#         wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
#     else:
#         if wine_type not in wine_types.keys():
#             raise ValueError("unrecognized wine type")
#         wines = wine_types[wine_type]
#     wi_ch_pairs = []
#     for cheese in CHEESES:
#         ch_cnt = Counter(cheese.lower())
#         for wine in wines:
#             wi_cnt = Counter(wine.lower())
#             wi_cnt_ch_cnt = wi_cnt & ch_cnt
#             square_len_diff = (len(cheese) - len(wine)) ** 2
#             similarity = sum(wi_cnt_ch_cnt.values()) / (1 + square_len_diff)
#             wi_ch_pairs.append((wine, cheese, similarity))
#     return wi_ch_pairs
#
#
# def best_match_per_wine(wine_type="all"):
#     """ wine cheese pair with the highest score
#     returns a tuple which contains wine, cheese, score
#     """
#     return sorted(_score(wine_type), key=lambda x: x[2])[-1]
#
#
# def match_wine_5cheeses():
#     """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
#     where each tuple contains: wine, list of 5 best matching cheeses
#     list of cheeses is sorted by score descending then alphabetically ascending
#     """
#     pre_sort = sorted(_score(), key=lambda x: x[1], reverse=True)
#     wi_ch_pairs_srt = sorted(pre_sort, key=operator.itemgetter(0, 2))
#     matches_wine_5cheeses = []
#     len_c = len(CHEESES)
#
#     for i in range(0, len(wi_ch_pairs_srt), len_c):
#         w = wi_ch_pairs_srt[i][0]
#         cheeses_5 = []
#         for j in range(i + len_c - 1, i + len_c - 6, -1):
#             cheeses_5.append(wi_ch_pairs_srt[j][1])
#         matches_wine_5cheeses.append((w, cheeses_5))
#     return matches_wine_5cheeses
# class Animal:
#     start_val = 10001
#     animal_list = []
#
#     def __init__(self, name:str):
#         self.index = Animal.start_val
#         self.name = name.title()
#         Animal.animal_list.append(self)
#         Animal.start_val+=1
#
#     def __str__(self):
#         return f"{self.index}. {self.name}"
#
#     @classmethod
#     def zoo(cls):
#         return "\n".join((str(animal) for animal in Animal.animal_list))

#
# dog = Animal('dog')
# print(dog)
# cat = Animal('cat')
# fish = Animal('fish')
# lion = Animal('lion')
# mouse = Animal('mouse')
# print(Animal.zoo())
#
# import pandas as pd
#
# data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
#
#
# def athletes_most_medals(data: str = data) -> pd.Series:
#     df = pd.read_csv(data)
#     df_by_athlete_gender = df.groupby(['Athlete', 'Gender'])
#     df_by_ag_count = df_by_athlete_gender['Medal'].count()
#     df_flat = df_by_ag_count.reset_index()
#     df_athlete = df_flat.set_index('Athlete')
#     df_athlete_medal =df_athlete['Medal']
#     df_gender_athelte_idx=df_athlete.groupby('Gender').idxmax()
#     b = df_gender_athelte_idx['Medal']
#     return df_athlete_medal[b]
#
# from enum import Enum
# from datetime import datetime
# from collections import Counter
#
#
# class DateFormat(Enum):
#     DDMMYY = 0  # dd/mm/yy
#     MMDDYY = 1  # mm/dd/yy
#     YYMMDD = 2  # yy/mm/dd
#     NONPARSABLE = -999
#
#     @classmethod
#     def get_d_parse_formats(cls, val=None):
#         """ Arg:
#         val(int | None) enum member value
#         Returns:
#         1. for val=None a list of explicit format strings
#             for all supported date formats in this enum
#         2. for val=n an explicit format string for a given enum member value
#         """
#         d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
#         if val is None:
#             return d_parse_formats
#         if 0 <= val <= len(d_parse_formats):
#             return d_parse_formats[val]
#         raise ValueError
#
#
# class InfDateFmtError(Exception):
#     """custom exception when it is not possible to infer a date format
#     e.g. too many NONPARSABLE or a tie """
#     pass
#
#
# def _maybe_DateFormats(date_str):
#     """ Args:
#     date_str (str) string representing a date in unknown format
#     Returns:
#     a list of enum members, where each member represents
#     a possible date format for the input date_str
#     """
#     d_parse_formats = DateFormat.get_d_parse_formats()
#     maybe_formats = []
#     for idx, d_parse_fmt in enumerate(d_parse_formats):
#         try:
#             _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
#             maybe_formats.append(DateFormat(idx))
#         except ValueError:
#             pass
#     if len(maybe_formats) == 0:
#         maybe_formats.append(DateFormat.NONPARSABLE)
#     return maybe_formats
#
#
# def get_dates(dates):
#     """ Args:
#     dates (list) list of date strings
#     where each list item represents a date in unknown format
#     Returns:
#     list of date strings, where each list item represents
#     a date in yyyy-mm-dd format. Date format of input date strings is
#     inferred based on the most prevalent format in the dates list.
#     Allowed/supported date formats are defined in a DF enum class.
#     """
#
#     # set up the counter
#     counter = Counter()
#     # make list of possible formats
#     dt_list_of_list = [_maybe_DateFormats(dt) for dt in dates]
#     # count the possible formats
#     for lst in dt_list_of_list:
#         counter.update(lst)
#     # Non parsable
#     if counter.most_common()[0][0]==DateFormat.NONPARSABLE:
#         raise InfDateFmtError
#     # See if the top two have the same count
#     if len(counter.most_common())>2 and counter.most_common()[0][1] == counter.most_common()[1][1]:
#         raise InfDateFmtError
#
#     # There is one dominant format.
#     most_common_format = counter.most_common()[0][0]
#     return_list = []
#     for dt in dates:
#         try:
#             _parsed_date = datetime.strptime(dt,DateFormat.get_d_parse_formats(most_common_format.value))
#             return_list.append(_parsed_date.strftime("%Y-%m-%d"))
#         except ValueError:
#             return_list.append('Invalid')
#
#     return return_list
#
# from collections import namedtuple
#
# MIN_SCORE = 4
# DICE_VALUES = range(1, 7)
#
# Player = namedtuple('Player', 'name scores')
#
#
# def calculate_score(scores):
#     """Based on a list of score ints (dice roll), calculate the
#        total score only taking into account >= MIN_SCORE
#        (= eyes of the dice roll).
#
#        If one of the scores is not a valid dice roll (1-6)
#        raise a ValueError.
#
#        Returns int of the sum of the scores.
#     """
#     total = 0
#     for score in scores:
#         if type(score)!= int or not 0 <= score <= 6:
#             raise ValueError
#         if score >= MIN_SCORE:
#             total += score
#     return total
#
#
#
# def get_winner(players):
#     """Given a list of Player namedtuples return the player
#        with the highest score using calculate_score.
#
#        If the length of the scores lists of the players passed in
#        don't match up raise a ValueError.
#
#        Returns a Player namedtuple of the winner.
#        You can assume there is only one winner.
#
#        For example - input:
#          Player(name='player 1', scores=[1, 3, 2, 5])
#          Player(name='player 2', scores=[1, 1, 1, 1])
#          Player(name='player 3', scores=[4, 5, 1, 2])
#
#        output:
#          Player(name='player 3', scores=[4, 5, 1, 2])
#     """
#     for index, player in enumerate(players):
#         player : Player
#         if index == 0:
#             num_scores =  len(player.scores)
#             max_score = calculate_score(player.scores)
#             winner = player
#         else:
#              if num_scores != len(player.scores):
#                  raise ValueError
#              if max_score < calculate_score(player.scores):
#                  winner = player
#     return winner
#
# I like the solution better than mine.
#     # score_lengths = {len(player.scores) for player in players}
#     # if len(score_lengths) > 1:
#     #     raise ValueError('Players with different amount of score')
#     #
#     # return max(players, key=lambda x: calculate_score(x.scores))
#
# from datetime import date
# from dateutil.relativedelta import relativedelta
#
# START_DATE = date(2018, 11, 1)
# MIN_DAYS_TO_COUNT_AS_MONTH = 10
# MONTHS_PER_YEAR = 12
#
#
# def calc_months_passed(year, month, day):
#     """Construct a date object from the passed in arguments.
#        If this fails due to bad inputs reraise the exception.
#        Also if the new date is < START_DATE raise a ValueError.
#
#        Then calculate how many months have passed since the
#        START_DATE constant. We suggest using dateutil.relativedelta!
#
#        One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
#        days in, it counts as an extra  month.
#
#        For example:
#        date(2018, 11, 10) = 9 days in => 0 months
#        date(2018, 11, 11) = 10 days in => 1 month
#        date(2018, 12, 11) = 1 month + 10 days in => 2 months
#        date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
#        etc.
#
#        See the tests for more examples.
#
#        Return the number of months passed int.
#     """
#
#
#     new_date = date(year, month, day)
#     if START_DATE > new_date:
#         raise ValueError
#
#     difference = relativedelta(new_date, START_DATE)
#     num_months = difference.months
#     if difference.days >= 10:
#         num_months += 1
#
#     num_months += difference.years * MONTHS_PER_YEAR
#
#     return num_months
#
# STAR = '*'
#
# def gen_rhombus(width):
#     """Create a generator that yields the rows of a rhombus row
#        by row. So if width = 5 it should generate the following
#        rows one by one:
#
#        gen = gen_rhombus(5)
#        for row in gen:
#            print(row)
#
#         output:
#           *
#          ***
#         *****
#          ***
#           *
#     """
#     # center_row = int((1 + width) / 2)
#     # for row in range(1, width+1):
#     #     dis_from_center_row = abs(row - center_row)
#     #     spaces = 2 * dis_from_center_row
#     #     num_stars = width - spaces
#     #     yield (STAR*num_stars).center(width)
#
#
#
# #
# # # utilize ^ for center align
# # def _print_row(i, width):
# #     return f'{STAR*i: ^{width}}'
# # _print_row(6,3)
# #
# # # range can take positive and negative steps
# from datetime import date
#
# from dateutil.relativedelta import relativedelta
# from dateutil.rrule import rrule, WEEKLY, MO,TU,WE,TH,FR
# from datetime import datetime
# TODAY = date(year=2018, month=11, day=29)

#
# def get_hundred_weekdays(start_date=TODAY):
#     """Return a list of hundred date objects starting from
#        start_date up till 100 weekdays later, so +100 days
#        skipping Saturdays and Sundays"""
#     day_count = 0
#     weekday_list = []
#     current_day = start_date
#     while day_count < 100:
#
#         if current_day.weekday() < 5:
#             weekday_list.append(current_day)
#             day_count += 1
#         current_day = current_day + relativedelta(days=1)
#     return weekday_list
#
# def get_hundred_weekdays(start_date=TODAY):
#     """Return a list of hundred date objects starting from
#        start_date up till 100 weekdays later, so +100 days
#        skipping Saturdays and Sundays"""
#
#     dt_gen = rrule(WEEKLY, byweekday=[MO, TU, WE, TH, FR], dtstart=start_date, count=100)
#     return [dt.date() for dt in dt_gen]
#
#
# from itertools import groupby
# from collections import defaultdict
#
# cars = [
#     # need mock data? -> https://www.mockaroo.com == awesome
#     ('Mercedes-Benz', '300D'), ('Mercedes-Benz', '600SEL'),
#     ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
#     ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
#     ('Mercedes-Benz', 'E-Class'), ('Hyundai', 'Elantra'),
#     ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
#     ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
#     ('Ford', 'Mustang'), ('Kia', 'Optima'),
#     ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
#     ('Volkswagen', 'Routan'), ('Hyundai', 'Sonata'),
#     ('Kia', 'Sorento'), ('Kia', 'Sportage'),
#     ('Ford', 'Taurus'), ('Nissan', 'Titan'),
#     ('Toyota', 'Tundra'), ('Hyundai', 'Veracruz'),
# ]
#
#
# def group_cars_by_manufacturer(cars):
#     """Iterate though the list of (manufacturer, model) tuples
#        of the cars list defined above and generate the output as described
#        in the Bite description (see the tests for the full output).
#
#        No return here, just print to the console. We use pytest > capfd to
#        validate your output :)
#     """
#     car_dict =  defaultdict(list)
#     for make, model in cars:
#         car_dict[make].append(model)
#
#     # sort by make
#     sorted_car_dict = sorted(car_dict)
#
#     for make in sorted_car_dict:
#         print(make.upper())
#         for model in sorted(car_dict.get(make)):
#             print(f"- {model}")
#         print()
#
# import json
#
# members = """
# id,first_name,last_name,email
# 1,Junie,Kybert;jkybert0@army.mil
# 2,Sid,Churching|schurching1@tumblr.com
# 3,Cherry;Dudbridge,cdudbridge2@nifty.com
# 4,Merrilee,Kleiser;mkleiser3@reference.com
# 5,Umeko,Cray;ucray4@foxnews.com
# 6,Jenifer,Dale|jdale@hubpages.com
# 7,Deeanne;Gabbett,dgabbett6@ucoz.com
# 8,Hymie,Valentin;hvalentin7@blogs.com
# 9,Alphonso,Berwick|aberwick8@symantec.com
# 10,Wyn;Serginson,wserginson9@naver.com
# """
#
#
# def convert_to_json(members=members):
#     lines = members.splitlines()
#     header = lines[1]
#     data = lines[2:]
#     header_fields = header.split(',')
#     delimiters =['|',';',',']
#
#     output = []
#     for line in data:
#         for delimiter in delimiters:
#             line = line.replace(delimiter, ' ')
#         fields = line.split(' ')
#         output.append(dict(zip(header_fields,fields)))
#     return json.dumps(output)

# from collections import namedtuple
# from datetime import datetime
#
# Composer = namedtuple('Composer', 'name born died')
# Opera = namedtuple('Opera', 'author play date')
#
# composers = {
#     "beethoven": Composer("Ludwig van Beethoven",
#                           "17 December 1770", "26 March 1827"),
#     "wagner": Composer("Richard Wagner",
#                        "22 May 1813", "13 February 1883"),
#     "verdi": Composer("Giuseppe Verdi",
#                       "9 October 1813", "27 January 1901"),
#     "mozart": Composer("Wolfgang Amadeus Mozart",
#                        "27 January 1756", "5 December 1791"),
# }
#
# operas = [
#     Opera("mozart", "Apollo and Hyacinth", "13 May 1767"),
#     Opera("mozart", "Marriage of Figaro", "1 May 1786"),
#     Opera("mozart", "Don Giovanni", "29 October 1787"),
#     Opera("mozart", "Così fan tutte", "6 January 1790"),
#     Opera("mozart", "The Clemency of Titus", "6 September 1791"),
#     Opera("mozart", "The Magic Flute", "30 September 1791"),
#     Opera("wagner", "The Fairies", "29 June 1888"),
#     Opera("wagner", "Rienzi", "20 October 1842"),
#     Opera("wagner", "The Flying Dutchman", "2 January 1843"),
#     Opera("wagner", "Tannhäuser", "19 October 1845"),
#     Opera("wagner", "Lohengrin", "28 August 1850"),
#     Opera("wagner", "The Rhinegold", "22 September 1869"),
#     Opera("wagner", "The Valkyrie", "26 June 1870"),
#     Opera("wagner", "Siegfried", "16 August 1876"),
#     Opera("wagner", "Twilight of the Gods", "17 August 1876"),
#     Opera("wagner", "Tristan and Isolde", "10 June 1865"),
#     Opera("wagner", "The Master-Singers of Nuremberg", "21 June 1868"),
#     Opera("wagner", "Parsifal", "26 July 1882"),
#     Opera("beethoven", "Fidelio", "20 November 1805"),
#     Opera("verdi", "Nabucco", "9 March 1842"),
#     Opera("verdi", "Ernani", "9 March 1844"),
#     Opera("verdi", "Macbeth", "14 March 1847"),
#     Opera("verdi", "Il corsaro", "25 October 1848"),
#     Opera("verdi", "Rigoletto", "11 March 1851"),
#     Opera("verdi", "La traviata", "6 March 1853"),
#     Opera("verdi", "Aroldo", "16 August 1857"),
#     Opera("verdi", "Macbeth", "21 April 1865"),
#     Opera("verdi", "Don Carlos", "11 March 1867"),
#     Opera("verdi", "Aida", "24 December 1871"),
#     Opera("verdi", "Otello", "5 February 1887"),
#     Opera("verdi", "Falstaff", "9 February 1893"),
# ]
#
#
# def _get_date(date_str):
#     return datetime.date(datetime.strptime(date_str, "%d %B %Y"))
#
# def _is_alive(opera:Opera, guest:Composer):
#     """
#     This boolean function determines if a composer is alive when an opera premiers
#     :param opera:
#     :param composer:
#     :return:
#     """
#     opera_date = _get_date(opera.date)
#     guest_birth = _get_date(guest.born)
#     guest_death = _get_date(guest.died)
#     return guest_birth <= opera_date <= guest_death
#
# def operas_both_at_premiere(guest, composer):
#     """Retrieves a list of titles of operas, where the guest and the composer
#        could have been together at premiere.
#
#        That is the Opera.author matches the composer passed in, and both guest
#        and composer are alive at the time of Opera.date.
#
#        If guest and/or composer are not in the composers dict, raise a
#        ValueError
#
#        Args:
#        guest (str): one of the composers but not the author of an opera
#        composer (str): the author of an opera
#
#        Returns a list (or generator) of titles of operas.
#     """
#     #for each opera
#     #  if the author is the composer
#     #  if the guest is NOT the composer
#     #  if the guest is alive during that opera
#         # add the composer
#     if not (guest in composers and composer in composers):
#         raise ValueError
#
#     return [opera.play for opera in operas if (opera.author==composer) and
#             guest != composer and _is_alive(opera, composers[guest]) and
#             _is_alive(opera, composers[composer])]
#
# verdi_wagner = list(operas_both_at_premiere("verdi", "wagner"))
#
# from dataclasses import dataclass, field
#
# @dataclass(order=)
# class Bite:
#     number: int
#     title: str
#     level: str = field(default='Beginner')
#
#     def __post_init__(self):
#         title_list = self.title.split()
#         title_list[0] = title_list[0].title()
#         self.title = ' '.join(title_list)
#
#     def __lt__(self, other):
#         return self.number < other.number
#
# b1 = Bite(3,"my name is Jane")

#
# @dataclass(order=True)
# class Bite:
#     number: int
#     title: str
#     level: str = 'Beginner'
#
#     def __post_init__(self):
#         self.title = self.title.capitalize()
# import re
#
# def split_words_and_quoted_text(text):
#     """Split string text by space unless it is
#        wrapped inside double quotes, returning a list
#        of the elements.
#
#        For example
#        if text =
#        'Should give "3 elements only"'
#
#        the resulting list would be:
#        ['Should', 'give', '3 elements only']
#     """
#     pattern = r'(?P<bg>.*)"(?P<dq>.+)"(?P<ed>.*)'
#     match = re.match(pattern, text)
#     match_dict = match.groupdict()
#     lst = []
#     if match_dict['bg']:
#         lst.extend(match_dict['bg'].split())
#     lst.append(match_dict['dq'])
#     if match_dict['ed']:
#         lst.extend(match_dict['ed'].split())
#
#     return lst
#
# def split_words_and_quoted_text(text: str) -> List:
#     match = re.search(r'(.+)?"(.+)"(.+)?', text)
#     if match:
#         groups = match.groups()
#         return (
#             (groups[0].split() if groups[0] else []) +
#             [groups[1] if groups[1] else []] +
#             (groups[2].split() if groups[2] else [])
#         )
#
# from collections import defaultdict
#
# CHARACTERS = ['Red Riding Hood',
#               # we're omitting 'mother' here for simplicity
#               # (= substring grandmother)
#               ('Grandmother', 'Grandma', 'Granny'),
#               'wolf', 'woodsman']
#
# text = """
# Once upon a time, there was a little girl who lived in a village near the forest.  Whenever she went out, the little girl wore a red riding cloak, so everyone in the village called her Little Red Riding Hood.
# One morning, Little Red Riding Hood asked her mother if she could go to visit her grandmother as it had been awhile since they'd seen each other.
# "That's a good idea," her mother said.  So they packed a nice basket for Little Red Riding Hood to take to her grandmother.
# When the basket was ready, the little girl put on her red cloak and kissed her mother goodbye.
# "Remember, go straight to Grandma's house," her mother cautioned.  "Don't dawdle along the way and please don't talk to strangers!  The woods are dangerous."
# "Don't worry, mommy," said Little Red Riding Hood, "I'll be careful."
# But when Little Red Riding Hood noticed some lovely flowers in the woods, she forgot her promise to her mother.  She picked a few, watched the butterflies flit about for awhile, listened to the frogs croaking and then picked a few more.
# Little Red Riding Hood was enjoying the warm summer day so much, that she didn't notice a dark shadow approaching out of the forest behind her...
# Suddenly, the wolf appeared beside her.
# "What are you doing out here, little girl?" the wolf asked in a voice as friendly as he could muster.
# "I'm on my way to see my Grandma who lives through the forest, near the brook,"  Little Red Riding Hood replied.
# Then she realized how late she was and quickly excused herself, rushing down the path to her Grandma's house.
# The wolf, in the meantime, took a shortcut...
# The wolf, a little out of breath from running, arrived at Grandma's and knocked lightly at the door.
# "Oh thank goodness dear!  Come in, come in!  I was worried sick that something had happened to you in the forest," said Grandma thinking that the knock was her granddaughter.
# The wolf let himself in.  Poor Granny did not have time to say another word, before the wolf gobbled her up!
# The wolf let out a satisfied burp, and then poked through Granny's wardrobe to find a nightgown that he liked.  He added a frilly sleeping cap, and for good measure, dabbed some of Granny's perfume behind his pointy ears.
# A few minutes later, Red Riding Hood knocked on the door.  The wolf jumped into bed and pulled the covers over his nose.  "Who is it?" he called in a cackly voice.
# "It's me, Little Red Riding Hood."
# "Oh how lovely!  Do come in, my dear," croaked the wolf.
# When Little Red Riding Hood entered the little cottage, she could scarcely recognize her Grandmother.
# "Grandmother!  Your voice sounds so odd.  Is something the matter?" she asked.
# "Oh, I just have touch of a cold," squeaked the wolf adding a cough at the end to prove the point.
# "But Grandmother!  What big ears you have," said Little Red Riding Hood as she edged closer to the bed.
# "The better to hear you with, my dear," replied the wolf.
# "But Grandmother!  What big eyes you have," said Little Red Riding Hood.
# "The better to see you with, my dear," replied the wolf.
# "But Grandmother!  What big teeth you have," said Little Red Riding Hood her voice quivering slightly.
# "The better to eat you with, my dear," roared the wolf and he leapt out of the bed and began to chase the little girl.
# Almost too late, Little Red Riding Hood realized that the person in the bed was not her Grandmother, but a hungry wolf.
# She ran across the room and through the door, shouting, "Help!  Wolf!" as loudly as she could.
# A woodsman who was chopping logs nearby heard her cry and ran towards the cottage as fast as he could.
# He grabbed the wolf and made him spit out the poor Grandmother who was a bit frazzled by the whole experience, but still in one piece."Oh Grandma, I was so scared!"  sobbed Little Red Riding Hood, "I'll never speak to strangers or dawdle in the forest again."
# "There, there, child.  You've learned an important lesson.  Thank goodness you shouted loud enough for this kind woodsman to hear you!"
# The woodsman knocked out the wolf and carried him deep into the forest where he wouldn't bother people any longer.
# Little Red Riding Hood and her Grandmother had a nice lunch and a long chat.
# """
#
#
# def make_character_index(text=text, characters=CHARACTERS):
#     """Return a dict with keys are characters (lowercased) and values
#        the lines they appear in sorted order.
#        Matches should be case insensitive.
#        If a character has multiple synonyms
#        - e.g. ('Grandmother', 'Grandma', 'Granny') -
#        then return the former as key.
#     """
#     index = defaultdict(set)
#
#     for lineno, line in enumerate(text.strip().splitlines(), 1):
#         for character in characters:
#             names = [character] if isinstance(character, str) else character
#             for name in names:
#                 if name.lower() in line.lower():
#                     index[names[0].lower()].add(lineno)
#
#     return {character: sorted(lines)
#             for character, lines in index.items()}
#
# def filter_accents(text):
#     """Return a sequence of accented characters found in
#        the passed in lowercased text string
#     """
#     return sorted(list(set([char.lower() for char in text if ord(char)>128])))
#
# text = ("Denominada en Euskera como Donostia, está "
#      "situada en el Golfo de Vizcaya en la provincia "
#      "de Guipúzcoa. San Sebastián no es solo conocida "
#      "por su afamado festival de cine, sino también "
#      "por la belleza de sus calles, las cuales tienen "
#      "un corte francés y aburguesado que atraen cada "
#      "año a centenares de turistas.")
#
# for char in text:
#     if ord(char) > 128:
#     print(f"{char}: {ord(char)}")
#
# from operator import add, sub, mul, truediv
#
# def simple_calculator(calculation):
#     """Receives 'calculation' and returns the calculated result,
#
#        Examples - input -> output:
#        '2 * 3' -> 6
#        '2 + 6' -> 8
#
#        Support +, -, * and /, use "true" division (so 2/3 is .66
#        rather than 0)
#
#        Make sure you convert both numbers to ints.
#        If bad data is passed in, raise a ValueError.
#     """
#
#     function_table = {
#         '+':add,
#         '-':sub,
#         '*':mul,
#         '/':truediv,
#     }
#
#     try:
#         operand_1 = calculation.split()[0]
#         operand_2 = calculation.split()[2]
#         operation = calculation.split()[1]
#
#         return function_table[operation](int(operand_1),int(operand_2))
#     except:
#         raise ValueError
#
#   (My above code currently buries the actual error!!)
# Solution code is below.

#     # try:
#     #     num1, sign, num2 = calculation.split()
#     #     return CALCULATIONS[sign](int(num1), int(num2))
#     # except (KeyError, ValueError, ZeroDivisionError) as exc:
#     #     print(exc)
#     #     raise ValueError
#
# HTML_SPACE = '&nbsp;'

# def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
#     """Prepend value with fill_char for given column_length"""
#     value_length = len(str(value))
#     fill_length = column_length - value_length
#     return f"{fill_char*fill_length}{value}"
#
# def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
#     """Prepend value with fill_char for given column_length"""
#     return f"{value:>{column_length}}".replace(" ", fill_char)
#
# from packaging.version import Version
#
# # Parse the requirement into a data structure (dict of Version)
# def mak_requirement_dict(requirements):
#     return { item.split("==")[0]:Version(item.split("==")[1]) for item in requirements.strip().splitlines()}
#
#
#
# def changed_dependencies(old_reqs: str, new_reqs: str) -> list[str]:
#     """Compare old vs new requirement multiline strings
#     and return a list of dependencies that have been upgraded
#     (have a newer version)
#     """
#
# # Plan:
# # Parse the requirement into a data structure (dict of Version)
# # get 2.
# # iterate through the dicts and if they are th
# # list comprehension
#
#     old_requirements_dict = mak_requirement_dict(old_reqs)
#     new_requirements_dict = mak_requirement_dict(new_reqs)
#     return [new[0] for old, new in zip(old_requirements_dict.items(),new_requirements_dict.items()) if new[1] > old[1]]
#

#
# import configparser
# import re
#
#
# class ToxIniParser:
#
#     def __init__(self, ini_file):
#         """Use configparser to load ini_file into self.config"""
#         self.ConfigParser = configparser.ConfigParser()
#         self.ConfigParser.read(ini_file)
#
#
#     @property
#     def number_of_sections(self):
#         """Return the number of sections in the ini file.
#            New to properties? -> https://pybit.es/articles/property-decorator
#         """
#         return len(self.ConfigParser.sections())
#
#     @property
#     def environments(self):
#         delimiters =r"[,|'\n']"
#         """Return a list of environments
#            (= "envlist" attribute of [tox] section)"""
#         return [env.strip() for env in re.split(delimiters, self.ConfigParser['tox']['envlist']) if env.strip()]
#
#
#     @property
#     def base_python_versions(self):
#         """Return a list of all basepython across the ini file"""
#         return list(set([self.ConfigParser.get(section, 'basepython', fallback='') for section in self.ConfigParser.sections()
#                 if self.ConfigParser.get(section, 'basepython', fallback='') ]))
#
# cp2 = configparser.ConfigParser()
# cp2.read_string(oeuvre)
# cp2['tox']['envlist']
#
# [env.strip() for env in cp2['tox']['envlist'].split(',')]
#
#
# list(set([cp2.get(section, 'basepython', fallback='') for section in cp2.sections()
#  if cp2.get(section, 'basepython', fallback='')]))
#
# from datetime import datetime, timedelta
# import re
# from functools import reduce
#
# NOW = datetime(year=2019, month=2, day=6,
#                hour=22, minute=0, second=0)
#
#
# def add_todo(delay_time: str, task: str,
#              start_time: datetime = NOW) -> str:
#     """
#     Add a todo list item in the future with a delay time.
#
#     Parse out the time unit from the passed in delay_time str:
#     - 30d = 30 days
#     - 1h 10m = 1 hour and 10 min
#     - 5m 3s = 5 min and 3 seconds
#     - 45 or 45s = 45 seconds
#
#     Return the task and planned time which is calculated from
#     provided start_time (here default = NOW):
#     >>> add_todo("1h 10m", "Wash my car")
#     >>> "Wash my car @ 2019-02-06 23:10:00"
#     """
#     return f"{task} @ {start_time + convert_timedelta(delay_time)}"
#
#
# time_dict = {'d': lambda x: timedelta(days=x),
#              'h': lambda x: timedelta(hours=x) ,
#              'm': lambda x: timedelta(minutes=x),
#              's': lambda x: timedelta(seconds=x),
#              }
#
#
# def _str_to_timedelta(time_str: str):
#     return time_dict[time_str[-1]](int(time_str[:-1])) if time_str[-1] in time_dict else time_dict['s'](int(time_str))
#
# def convert_timedelta(time_str):
#     time_deltas = [_str_to_timedelta( element) for element in time_str.split()]
#     return reduce(lambda x, y: x + y, time_deltas)
#
# from datetime import timedelta
#
# def get_missing_dates(dates):
#     """Receives a range of dates and returns a sequence
#        of missing datetime.date objects (no worries about order).
#
#        You can assume that the first and last date of the
#        range is always present (assumption made in tests).
#
#        See the Bite description and tests for example outputs.
#     """
#     date_set = set()
#     max_date = max(dates)
#     min_date = min(dates)
#     current_date = min_date + timedelta(days=1)
#     while current_date<max_date:
#         if current_date not in dates:
#             date_set.add(current_date)
#         current_date = current_date + timedelta(days=1)
#
#     return list(date_set)
#
# import datetime
# from dateutil import rrule
#
# def get_missing_dates(dates):
#     """Receives a range of dates and returns a sequence
#        of missing datetime.date objects (no worries about order).
#
#        You can assume that the first and last date of the
#        range is always present (assumption made in tests).
#
#        See the Bite description and tests for example outputs.
#     """
#     min_date = min(dates)
#     count  = (max(dates) - min_date).days
#     return set([day.date() for day in rrule.rrule(freq=rrule.DAILY, dtstart = min_date, count=count )]) - set(dates)

#
# import os
# from urllib.request import urlretrieve
# import re
# from dateutil.parser import parse
# from collections import defaultdict
# from operator import itemgetter
# commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
# urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)
#
# # you can use this constant as key to the yyyymm:count dict
# YEAR_MONTH = "{y}-{m:02d}"
#
# def parse_commitdate_changes(line):
#     date_str, change_str = line.split("|")[0], line.split("|")[1]
#
#     # parse out year/month
#     dt = parse(date_str[6:])
#     key = dt.strftime('%Y-%m')
#
#     # parse out total for insertions & deletions
#     pattern = r"\d+ files? changed,( (?P<inserts>\d+) insertions?\(\+\))?,?( (?P<deletes>\d+) deletions?\(\-\))?,?"
#     #change_str ='3 files changed, 5 insertions(+), 1 deletion(-)'
#     match = re.search(pattern, change_str.strip())
#     insert_count = int(match.groupdict().get('inserts')) if match.groupdict().get('inserts') else 0
#     delete_count = int(match.groupdict().get('deletes')) if match.groupdict().get('deletes') else 0
#     count = insert_count + delete_count
#     return key, count
#
# def get_min_max_amount_of_commits(
#     commit_log: str = commits, year: int | None = None
# ) -> tuple[str, str]:
#     """
#     Calculate the amount of inserts / deletes per month from the
#     provided commit log.
#
#     Takes optional year arg, if provided only look at lines for
#     that year, if not, use the entire file.
#
#     Returns a tuple of (least_active_month, most_active_month)
#     """
#
# # Plan
# # Parse each line
#     commit_dict = defaultdict(int)
#     with open(commits,'r+') as file:
#         for line in file:
#             #print(line)
#             commit_date, change_count = parse_commitdate_changes(line)
#             commit_dict[commit_date]+=change_count
#     if year:
#         filter_dict ={key:val for key, val in commit_dict.items() if int(key.split('-')[0])==year}
#         commit_dict = filter_dict
#
#     max_key = max(commit_dict.items(), key=itemgetter(1))
#     min_key = min(commit_dict.items(), key=itemgetter(1))
#     return min_key[0], max_key[0]
#
# # Add to a dictionary # defaultdict with int
#
# # Loop through the dictionary, to find the max and the min for the month or the year.
#
#
#
# if __name__ == "__main__":
#     get_min_max_amount_of_commits()
#
# from bs4 import BeautifulSoup
# import re
#
# # source: https://www.virgin.com/richard-branson/my-top-10-quotes-living-life-better
# HTML = """<!DOCTYPE html>
# <head>
#   <meta charset="utf-8" />
#   <title>My top 10 quotes on living life better | Virgin</title>
# </head>
# <body>
#   <div class="content">
#     <p>I’m striving this year to maintain my fitness and to always be learning new things. The new theme on Virgin.com is Live Life Better – a series shining a spotlight on how we can all lead happier, healthier and more fulfilled lives. Virgin has always wanted to make things better for our team and customers and to improve their experiences.</p>
#     <p>Here are my top 10 quotes on living life better for some New Year inspiration:</p>
#     <p>10. "The beautiful thing about learning is nobody can take it away from you." - B.B King</p>
#     <p>9. "Inexperience is an asset. Embrace it." - Wendy Kopp</p>
#     <p>8. "Change will not come if we wait for some other person, or if we wait for some other time. We are the ones we’ve been waiting for. We are the change that we seek." - Barack Obama</p>
#     <p>7. "The sky is not my limit… I am." - T.F. Hodge</p>
#     <p>6. "Life is either a daring adventure or nothing at all." - Helen Keller</p>
#     <p>5. "It does not matter how slowly you go as long as you do not stop." - Confucius</p>
#     <p>4. "Too many of us are not living our dreams because we are living our fears." - Les Brown</p>
#     <p>3. "Continuous efforts – not strength or intelligence – is the key to unlocking our potential." - Winston Churchill</p>
#     <p>2. "Believe you can and you’re halfway there." - Theodore Roosevelt</p>
#     <p>1. "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be." - Zig Ziglar</p>
#     <p>How do you try and live a healthier, happier life?</p>
#   </div>
# </body>
# </html>"""
#
#
# def extract_quotes(html: str = HTML) -> dict:
#     """See instructions in the Bite description"""
#     soup = BeautifulSoup(html)
#
#     # use find_all method with regular expression to find substrings.
#     quotes=soup.find_all('p', string=re.compile("-"))
#     quote_dict = {}
#     for quote in quotes:
#         [_quote, author]=quote.string.split("-")
#         quote_dict[author.strip()] = _quote.split('"')[1].strip()
#     return quote_dict

# source: https://www.virgin.com/richard-branson/my-top-10-quotes-living-life-better
# HTML = """<!DOCTYPE html>
# <head>
#   <meta charset="utf-8" />
#   <title>My top 10 quotes on living life better | Virgin</title>
# </head>
# <body>
#   <div class="content">
#     <p>I’m striving this year to maintain my fitness and to always be learning new things. The new theme on Virgin.com is Live Life Better – a series shining a spotlight on how we can all lead happier, healthier and more fulfilled lives. Virgin has always wanted to make things better for our team and customers and to improve their experiences.</p>
#     <p>Here are my top 10 quotes on living life better for some New Year inspiration:</p>
#     <p>10. "The beautiful thing about learning is nobody can take it away from you." - B.B King</p>
#     <p>9. "Inexperience is an asset. Embrace it." - Wendy Kopp</p>
#     <p>8. "Change will not come if we wait for some other person, or if we wait for some other time. We are the ones we’ve been waiting for. We are the change that we seek." - Barack Obama</p>
#     <p>7. "The sky is not my limit… I am." - T.F. Hodge</p>
#     <p>6. "Life is either a daring adventure or nothing at all." - Helen Keller</p>
#     <p>5. "It does not matter how slowly you go as long as you do not stop." - Confucius</p>
#     <p>4. "Too many of us are not living our dreams because we are living our fears." - Les Brown</p>
#     <p>3. "Continuous efforts – not strength or intelligence – is the key to unlocking our potential." - Winston Churchill</p>
#     <p>2. "Believe you can and you’re halfway there." - Theodore Roosevelt</p>
#     <p>1. "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be." - Zig Ziglar</p>
#     <p>How do you try and live a healthier, happier life?</p>
#   </div>
# </body>
# </html>"""
#
#
# def extract_quotes(html: str = HTML) -> dict:
#     """See instructions in the Bite description"""
#
#     pattern = r'<p>\d+\. "(?P<quote>.+)" - (?P<author>.+)</p>'
#
#     group_dict = {}
#     for line in html.splitlines():
#         match = re.search(pattern, line)
#         if match:
#             group_dict[match.groupdict()['author'].strip()] = match.groupdict()['quote'].strip()
#     return group_dict
#
#
#
# def extract_quotes(html: str = HTML) -> dict:
#     # (.*?)
#     paras = re.findall('<p>\d+\.(.*?)</p>', html)
#     quotes = {}
#     for p in paras:
#         quote, author = p.strip().split('-')
#         quotes[author.strip()] = quote.strip('" ')
#     return quotes
#
# from csv import DictReader
# import os
# from urllib.request import urlretrieve
# from collections import Counter
#
# TMP = os.getenv("TMP", "/tmp")
# LOGS = 'bite_output_log.txt'
# DATA = os.path.join(TMP, LOGS)
# S3 = 'https://bites-data.s3.us-east-2.amazonaws.com'
# if not os.path.isfile(DATA):
#     urlretrieve(f'{S3}/{LOGS}', DATA)
#
# rows = []
# with open(DATA,'r+') as file:
#     reader = DictReader(file)
#     for line in reader:
#         rows.append(line)


# len(set([row['bite'] for row in self.rows]))

#
# class BiteStats:
#
#     def __init__(self, data=DATA):
#         self.rows = []
#         # you code ...
#         with open(DATA, 'r+') as file:
#             reader = DictReader(file)
#             for line in reader:
#                 self.rows.append(line)
#
#     @property
#     def number_bites_accessed(self) -> int:
#         """Get the number of unique Bites accessed"""
#         # alternative syntax : len({row['bite'] for row in self.rows}) # set comprehension
#         return len(set([row['bite'] for row in self.rows]))
#
#     @property
#     def number_bites_resolved(self) -> int:
#         """Get the number of unique Bites resolved (completed=True)"""
#         return len(set([row['bite'] for row in self.rows if row['completed'] == 'True']))
#
#     @property
#     def number_users_active(self) -> int:
#         """Get the number of unique users in the data set"""
#         return len(set([row['user'] for row in self.rows]))
#
#     @property
#     def number_users_solving_bites(self) -> int:
#         """Get the number of unique users that resolved
#            one or more Bites"""
#         return len(set([row['user'] for row in self.rows if row['completed'] == 'True']))
#
#     @property
#     def top_bite_by_number_of_clicks(self) -> str:
#         """Get the Bite that got accessed the most
#            (= in most rows)"""
#         return Counter([row['bite'] for row in self.rows]).most_common()[0][0]
#
#     @property
#     def top_user_by_bites_completed(self) -> str:
#         """Get the user that completed the most Bites"""
#
#         return Counter([row['user'] for row in self.rows if row['completed'] == 'True']).most_common()[0][0]
#
# from difflib import SequenceMatcher, get_close_matches
# import os
# from typing import Union
# from urllib.request import urlretrieve
#
# TMP = os.getenv("TMP", "/tmp")
# DICTIONARY = os.path.join(TMP, 'dictionary.txt')
# if not os.path.isfile(DICTIONARY):
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt',
#         DICTIONARY
#     )
#
#
# def load_words():
#     'return dict of words in DICTIONARY'
#     with open(DICTIONARY) as f:
#         return {word.strip().lower() for word in f.readlines()}
#
#
# def suggest_word(misspelled_word: str, words: Union[set, None]) -> str:
#     """Return a valid alternative word that best matches
#        the entered misspelled word"""
#     if words is None:
#         words = load_words()
#
#     return get_close_matches(misspelled_word, words, n=1)[0]
#
# from datetime import datetime
# from dateutil.parser import parse
# import math
#
# # work with a static date for tests, real use = datetime.now()
# NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
# WEEKS_PER_YEAR = 52
#
#
# def get_number_books_read(books_per_year_goal: int,
#                           at_date: str = None) -> int:
#     """Based on books_per_year_goal and at_date, return the
#        number of books that should have been read.
#        If books_per_year_goal negative or 0, or at_date is in the
#        past, raise a ValueError."""
#     at_date = at_date or str(NOW)
#     # TODOs
#
#     # 1. use dateutil's parse to convert at_date into a
#     # datetime object
#
#     at_dt :datetime = parse(at_date)
#
#     # 2. check books_per_year_goal and at_date and raise
#     # a ValueError if goal <= 0 or at_date in the past (< NOW)
#     if books_per_year_goal <= 0 or at_dt < NOW:
#         raise ValueError("Invalid value!")
#
#     # 3. check the offset of at_date in the year ("week of the
#     # year" - e.g. whatweekisit.com) and based on the books_per_year_goal,
#     # calculate the number of books that should have been read / completed
#
#     at_week = at_dt.isocalendar()[1]
#     return math.floor(at_week / WEEKS_PER_YEAR * books_per_year_goal)
#
# from dataclasses import dataclass
# import dateutil
#
#
# @dataclass
# class Actor:
#     name: str
#     born: str
#
#
# @dataclass
# class Movie:
#     title: str
#     release_date: str
#
#
# def get_age(actor: Actor, movie: Movie) -> str:
#     """Calculates age of actor / actress when movie was released,
#        return a string like this:
#
#        {name} was {age} years old when {movie} came out.
#        e.g.
#        Wesley Snipes was 28 years old when New Jack City came out.
#     """
#     # use relativedelta would have been a better choice here.
#     # age = relativedelta(parse(movie.release_date), parse(actor.born))
#     # return f'{actor.name} was {age.years} years old when {movie.title} came out.'
#
#
#     movie_date = dateutil.parser.parse(movie.release_date)
#     actor_bd_date = dateutil.parser.parse(actor.born)
#     age = int((movie_date - actor_bd_date).days / 365)
#     return f"{actor.name} was {age} years old when {movie.title} came out."
#
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
# import xml.etree.ElementTree as ET
# from collections import defaultdict
#
# # import the countries xml file
# tmp = Path(os.getenv("TMP", "/tmp"))
# countries = tmp / 'countries.xml'
#
# if not countries.exists():
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
#         countries
#     )
#
# def get_income_distribution(xml=countries):
#     """
#     - Read in the countries xml as stored in countries variable.
#     - Parse the XML
#     - Return a dict of:
#       - keys = incomes (wb:incomeLevel)
#       - values = list of country names (wb:name)
#     """
#     income_dict = defaultdict(list)
#     xml = countries
#     tree = ET.parse(xml)
#     countries_node = tree.getroot()
#
#     namespace ={ 'wb':'http://www.worldbank.org' }
#     all_countries = countries_node.findall('wb:country', namespace)
#
#     for country in all_countries:
#         country_name = country.find('wb:name',namespace).text
#         country_income = country.find('wb:incomeLevel', namespace).text
#         income_dict[country_income].append(country_name)
#
#     return income_dict
#
#
# data = """Luke Skywalker,172,77
#           C-3PO,167,75
#           R2-D2,96,32
#           Darth Vader,202,136
#           Leia Organa,150,49
#           Owen Lars,178,120
#           Beru Whitesun lars,165,75
#           R5-D4,97,32
#           Biggs Darklighter,183,84
#           Obi-Wan Kenobi,182,77
#           Anakin Skywalker,188,84
#           Chewbacca,228,112
#           Han Solo,180,80
#           Greedo,173,74
#           Jek Tono Porkins,180,110
#           Yoda,66,17
#           Palpatine,170,75
#           Boba Fett,183,78.2
#           IG-88,200,140
#           Bossk,190,113
# """

#
# def person_max_bmi(data=data):
#     """Return (name, BMI float) of the character in data that
#        has the highest BMI (rounded on 2 decimals)"""
#     pass
#
#     bmi_dict = {}
#     for person_data in data.splitlines():
#         person, height, mass = person_data.split(',')
#         bmi_dict[person.strip()] = round(float(mass) / ((int(height) / 100) ** 2 ),2)
#
#     return max(bmi_dict.items(), key=lambda x : x[1])
#
# import requests
# from bs4 import BeautifulSoup
#
# cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'
#
#
# def top_python_questions(url=cached_so_url):
#     """Use requests to retrieve the url / html,
#        parse the questions out of the html with BeautifulSoup,
#        filter them by >= 1m views ("..m views").
#        Return a list of (question, num_votes) tuples ordered
#        by num_votes descending (see tests for expected output).
#     """
#
#     response = requests.get(cached_so_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     question_summary_list =soup.find_all('div', attrs={'class':'question-summary'})
#
#     # Parse out the question, vote count, and
#     candidate_list = [(entry.find('a', recursive=True).text,
#                        int(entry.find('span', class_='vote-count-post').text),
#                        entry.find('div', class_='views').text.strip().split()[0])
#                       for entry in question_summary_list]
#
#     return sorted([(candidate[0], candidate[1]) for candidate in candidate_list if candidate[2][-1] == 'm'],
#            key=lambda x: x[1], reverse=True)
#
# from functools import cache
#
# @cache
# def cached_fib(n):
#     if n in (0, 1):
#         return n
#     return cached_fib(n - 1) + cached_fib (n - 2)

#
# from collections import namedtuple
# import csv
# import os
# from pathlib import Path
# import sqlite3
# import random
# import string
#
# import requests
#
# DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
# TMP = Path(os.getenv("TMP", "/tmp"))
#
# salt = ''.join(
#     random.choice(string.ascii_lowercase) for i in range(20)
# )
# DB = TMP / f'nba_{salt}.db'
#
# Player = namedtuple('Player', ('name year first_year team college active '
#                                'games avg_min avg_points'))
#
# conn = sqlite3.connect(DB)
# cur = conn.cursor()
#
#
# def import_data():
#     with requests.Session() as session:
#         content = session.get(DATA_URL).content.decode('utf-8')
#
#     reader = csv.DictReader(content.splitlines(), delimiter=',')
#
#     players = []
#     for row in reader:
#         players.append(Player(name=row['Player'],
#                               year=row['Draft_Yr'],
#                               first_year=row['first_year'],
#                               team=row['Team'],
#                               college=row['College'],
#                               active=row['Yrs'],
#                               games=row['Games'],
#                               avg_min=row['Minutes.per.Game'],
#                               avg_points=row['Points.per.Game']))
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS players
#                   (name, year, first_year, team, college, active,
#                   games, avg_min, avg_points)''')
#     cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
#     conn.commit()
#
#
# import_data()
#
#
# # you code:
#
# def player_with_max_points_per_game():
#     """The player with highest average points per game (don't forget to CAST to
#        numeric in your SQL query)"""
#
#
#     result = cur.execute('''
#     Select name
#     from players
#     where cast(avg_points as REAL) = (select max(CAST(players.avg_points AS REAL))
#     from players);
#                          ''').fetchall()
#     return result[0][0]
#
#
# def number_of_players_from_duke():
#     """Return the number of players with college == Duke University"""
#
#     result = cur.execute("""
#     Select count(name)
#     from players
#     where college = 'Duke University'
#     """).fetchall()
#     return result[0][0]
#
#
# def avg_years_active_players_stanford():
#     """Return the average years that players from "Stanford University
#        are active ("active" column)"""
#     result = cur.execute("""
#                          Select round(avg(active),2)
#                          from players
#                         where college = 'Stanford University'
#                          """).fetchall()
#     return result[0][0]
#
#
# def year_with_most_new_players():
#     """Return the year with the most new players.
#        Hint: you can use GROUP BY on the year column.
#     """
#     result = cur.execute("""
#                         select year
#                         from players
#                         group by year
#                         order by count(name) desc
#                         limit 1
#                          """).fetchall()
#     return result[0][0]
#
# from datetime import date
# from dateutil.relativedelta import relativedelta
#
# def get_mothers_day_date(year):
#     """Given the passed in year int, return the date Mother's Day
#        is celebrated assuming it's the 2nd Sunday of May."""
#
#     # find what day of the week the first day of the month is
#     may_1 = date(year, 5, 1)
#     days_away = 6 - may_1.weekday()
#     # find the first Sunday
#     return  may_1 + relativedelta(days=(7+days_away))
# from datetime import date
#
# from dateutil.relativedelta import relativedelta, SU
#
# MAY = 5
#
#
# def get_mothers_day_date(year):
#     """Given the passed in year int, return the date Mother's Day
#        is celebrated assuming it's the 2nd Sunday of May."""
#     first_of_may = date(year=year, month=MAY, day=1)
#     return first_of_may + relativedelta(weeks=1, weekday=SU)

#
# class Person:
#     def __str__(self):
#         return "I am a person"
#
# class Father(Person):
#     def __str__(self):
#         return f"{super().__str__()} and cool daddy"
#
# class Mother(Person):
#     def __str__(self):
#         return f"{super().__str__()} and awesome mom"
#
# class Child(Father, Mother):
#     def __str__(self):
#         return f"I am the coolest kid"
#
# person = Person()
# dad = Father()
# mom = Mother()
# child = Child()
#
# print(person)
# print(dad)
# print(mom)
# print(child)
#
# import requests
#
#
# def nxapi_show_version():
#     url =  """https://sbx-nxos-mgmt.cisco.com:443/ins"""
#     switchuser = """admin"""
#     switchpassword = """Admin_1234!"""
#
#     http_headers = {
#     "Content-Type": "application/json-rpc",
# }
#     payload = {"jsonrpc": "2.0",
#                 "method": """cli_ascii""",
#                 "params": {"cmd": """show version""",
#                            "version": 1}, "id": 1}
#     # 1. use requests to post to the switch
#     response = requests.post(url=url, data=payload, auth=(switchuser, switchpassword) , headers=http_headers, verify=False)

# 2. retrieve and return the kickstart_ver_str from the response
# example response json:
# {'result': {'body': {'bios_cmpl_time': '05/17/2018',
#                      'kick_tmstmp': '07/11/2018 00:01:44',
#                      'kickstart_ver_str': '9.2(1)',
#                      ...
#                      }
#             }
# }
#    version = response.json()['result']['body']['kickstart_ver_str']
#     return version
#
#
# #  Solution version
# # def nxapi_show_version():
# #     url = 'https://sbx-nxos-mgmt.cisco.com/ins'
# #     switchuser = 'admin'
# #     switchpassword = 'Admin_1234!'
# #
# #     http_headers = {'content-type': 'application/json-rpc'}
# #     payload = [{"jsonrpc": "2.0",
# #                 "method": "cli",
# #                 "params": {
# #                     "cmd": "show version",
# #                     "version": 1
# #                 }, "id": 1}]
# #     response = requests.post(url,
# #                              json=payload,
# #                              headers=http_headers,
# #                              auth=(switchuser, switchpassword),
# #                              verify=False)
# #
# #     version = response.json()['result']['body']['kickstart_ver_str']
# #     return version
#
#
#
#
#
# if __name__ == '__main__':
#     result = nxapi_show_version()
#     print(result)
#
# import csv
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
# import re
#
# data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
# TMP = Path(os.getenv("TMP", "/tmp"))
# stats = TMP / 'bites.csv'
#
# if not stats.exists():
#     urlretrieve(data, stats)
#
#
# def get_most_complex_bites(N=10, stats=stats):
#     """Parse the bites.csv file (= stats variable passed in), see example
#        output in the Bite description.
#        Return a list of Bite IDs (int or str values are fine) of the N
#        most complex Bites.
#     """
#     # parse the bite.csv file
#     pattern=r'Bite (?P<BiteNum>\d+)\..+;(?P<difficulty>.+)'#a
#
#     with open(stats, 'r') as f_read:
#         bite_difficulty={}
#         next(f_read)
#         for line in f_read:
#
#             match = re.search(pattern, line)
#             if match:
#                 bite_num = match.groupdict()['BiteNum'].strip()
#                 diff_score = match.groupdict()['difficulty'].strip()
#                 d_score    = 0 if diff_score == 'None' else float(diff_score)
#                 bite_difficulty[bite_num] = d_score
#
#     # sort the bite
#     sorted_scores=sorted(bite_difficulty.items(), key=lambda x:x[1], reverse=True)
#     return [item[0] for i, item in enumerate(sorted_scores) if i< N]
#
# if __name__ == '__main__':
#     res = get_most_complex_bites()
#     print(res)
#
# from dataclasses import dataclass
#
# @dataclass
# class Employee:
#     """Simple Employee class
#
#     :param first_name: String of first name
#     :param last_name: String of last name
#     :param days_per_week: Integer of how many days per week worked
#     :param hours_per_day: Float of hours worked per day
#     :param wage: Float of hourly pay
#     :param weekly_pay: Property which returns a string for weekly pay
#     """
#
#     first_name: str
#     last_name: str
#     days_per_week: int
#     hours_per_day: float
#     wage: float
#
#     def _rounder(self, number:float, places:int)->str:
#         """Rounds a number the specified number of places
#
#         :param number: Float of number of round
#         :param places: Integer of places to round to
#         :return: String representation of the rounded number in US $
#         """
#         amount = round(number, places)
#         return f"${amount:0.2f}"
#
#     @property
#     def weekly_pay(self)->str:
#         """Returns amount of weekly pay in US currency
#
#         For instance: $250.75
#         """
#         total_hours = self.hours_per_day * self.days_per_week
#         total_wage = total_hours * self.wage
#         return self._rounder(total_wage, 2)
#
#
#
# if __name__ == "__main__":
#     coder = Employee("Joe", "Blow", 5, 8, 18.0)
#     print(coder.weekly_pay)
#
# from urllib.request import urlretrieve
# import os
# from pathlib import Path
# import gender_guesser.detector as gender
# from bs4 import BeautifulSoup as Soup
# import re
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# PYCON_HTML = TMP / "pycon2019.html"
# PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
#               'pycon2019.html')
#
# if not PYCON_HTML.exists():
#     urlretrieve(PYCON_PAGE, PYCON_HTML)
#
#
# def _get_soup(html=PYCON_HTML):
#     return Soup(html.read_text(encoding="utf-8"), "html.parser")

# # Refactor
# def _get_first_name(name):
#     return name.strip().split()[0]
#
# def split_and_get_first_name(name_str, sep):
#     return [ _get_first_name(name) for name in name_str.strip().split(sep)]
#
# def get_pycon_speaker_first_names(soup=None):
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     soup = _get_soup()
#     speaker_list = soup.find_all('span',class_='speaker')
#     result_list = []
#     for speaker in speaker_list:
#         if ',' in speaker.text.strip():
#             names = split_and_get_first_name(speaker.text,',')
#             result_list.extend(names)
#         elif '/' in speaker.text.strip():
#             names = split_and_get_first_name(speaker.text, '/')
#             result_list.extend(names)
#         else:
#             result_list.append(_get_first_name(speaker.text))
#
#     return result_list

#
# def _extract_names(names):
#     for name in names:
#         extracted_names = re.split(r'[,/]', name)
#         for en in extracted_names:
#             yield en.strip()
#
#
# def _get_first_names(names):
#     return [n.split()[0] for n in names]
#
#
# def get_pycon_speaker_first_names(soup=None):
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     if soup is None:
#         soup = _get_soup()
#
#     speakers = soup.find_all("span", {"class": "speaker"})
#     names = [speaker.text.strip() for speaker in speakers]
#
#     names = list(_extract_names(names))
#     return _get_first_names(names)

#
# def extract_names(speaker_list):
#     for speaker in speaker_list:
#         print(speaker.text.strip())
#         names = re.split(r'[,/]', speaker.text.strip())
#         for name in names:
#             yield name
#
#
# def get_pycon_speaker_first_names(soup=None):
#     """Parse the PYCON_HTML using BeautifulSoup, extracting all
#        speakers (class "speaker"). Note that some items contain
#        multiple speakers so you need to extract them.
#        Return a list of first names
#     """
#     soup = _get_soup()
#     speaker_list = soup.find_all('span',class_='speaker')
#
#         # Extract out all the names
#     names = list(extract_names(speaker_list))
#
#         # Extract out the first names
#     return [name.split()[0] for name in names]
#
# def get_percentage_of_female_speakers(first_names):
#     """Run gender_guesser on the names returning a percentage
#        of female speakers (female and mostly_female),
#        rounded to 2 decimal places."""
#     d = gender.Detector()
#     return round(100 * (sum([1 for name in first_names if 'female' in d.get_gender(name)]) /
#         len(first_names)), 2)
#
#
#
#
# if __name__ == '__main__':
#     names = get_pycon_speaker_first_names()
#     perc = get_percentage_of_female_speakers(names)
#     print(perc)
#
# from decimal import Decimal
#
# def check_split(item_total, tax_rate, tip, people):
#     """Calculate check value and evenly split.
#
#        :param item_total: str (e.g. '$8.68')
#        :param tax_rate: str (e.g. '4.75%)
#        :param tip: str (e.g. '10%')
#        :param people: int (e.g. 3)
#
#        :return: tuple of (grand_total: str, splits: list)
#                 e.g. ('$10.00', [3.34, 3.33, 3.33])
#     """
#     total_d = Decimal(item_total[1:])
#     rate_d = Decimal(tax_rate[:-1])/100
#     tip_d = Decimal(tip[:-1])/100
#     with_tip = (total_d * (1 + rate_d)).quantize(Decimal('.01'), rounding='ROUND_HALF_UP')
#     grand_total = (with_tip * (1 + tip_d)).quantize(Decimal('.01'), rounding='ROUND_HALF_UP')
#     grand_str = f"${grand_total}"
#
#     # Divide by the number of people
#     individual = (grand_total/people).quantize(Decimal('.01'))
#
#     # sum to n-1
#     splits = [individual for i in range(people - 1 )]
#
#     # total - subtotal
#     splits.append(grand_total - sum(splits))
#     return (grand_str, splits)
#
# from contextlib import suppress
#
#
# def sum_numbers(numbers):
#     """This generator divides each nummber by its consecutive number.
#        So if it gets passed in [4, 2, 1] it yields 4/2 and 2/1.
#        It ignores ZeroDivisionError and TypeError exceptions (latter happens
#        when a string or other non-numeric data type is in numbers)
#
#        Task: use contextlib's suppress twice to make the code below more concise.
#     """
#     for i, j in zip(numbers, numbers[1:]):
#         # replace the block below
#         with suppress(TypeError, ZeroDivisionError):
#             yield i/j

#
# from contextlib import redirect_stdout
# from io import StringIO
# from types import BuiltinFunctionType
#
#
# def get_len_help_text(builtin: BuiltinFunctionType) -> int:
#     """Receives a builtin, and returns the length of its help text.
#        You need to redirect stdout from the help builtin.
#        If the the object passed in is not a builtin, raise a ValueError.
#     """
#
#     if not isinstance(builtin, BuiltinFunctionType):
#        raise ValueError("Not a Build-in Type")
#
#     output = StringIO()
#     with redirect_stdout(output):
#         help(builtin)
#
#     return len(output.getvalue())

#
# from datetime import date, timedelta
#
# TODAY = date.today()
#
#
# def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
#     day = 0
#     while True:
#         day += num_days
#         for i in range(num_bites):
#             yield start_date + timedelta(days=day)

#
# def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
#     for j in itertools.count(num_days, num_days):
#         for i in range(num_bites):
#             yield start_date + timedelta(days=j)

#
# num_bites=3
# num_days=2
# start_date=TODAY
# gen = gen_bite_planning(num_bites, num_days, start_date)
# list(islice(gen, 10))
#
# start_date + timedelta(days=num_days)
# [start_date + timedelta(days=num_days) for i in range(num_days) for j in range(num_bites)]

#
# (for j in range(num_bites))
#         print(TODAY + timedelta(days=i))

# Learned about patching for this bite
#
# import requests
#
# YOUR_KEY = '123abc'
# DEFAULT_LIST = 'hardcover-nonfiction'
#
# URL_NON_FICTION = (f'https://api.nytimes.com/svc/books/v3/lists/current/'
#                    f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')
# URL_FICTION = URL_NON_FICTION.replace('nonfiction', 'fiction')
#
#
# def get_best_seller_titles(url=URL_NON_FICTION):
#     """Use the NY Times Books API endpoint above to get the titles that are
#        on the best seller list for the longest time.
#
#        Return a list of (title, weeks_on_list) tuples, e.g. for the nonfiction:
#
#        [('BETWEEN THE WORLD AND ME', 86),
#         ('EDUCATED', 79),
#         ('BECOMING', 41),
#         ('THE SECOND MOUNTAIN', 18),
#          ... 11 more ...
#        ]
#
#        Dev docs: https://developer.nytimes.com/docs/books-product/1/overview
#     """
#     response_dict = requests.get(url).json()
#     book_list = response_dict['results']['books']
#     return sorted([(book['title'], book['weeks_on_list']) for book in book_list], key=lambda x: x[1], reverse=True)
#
#
#
#
# if __name__ == '__main__':
#     ret = get_best_seller_titles()
#     print(ret)
#
# import types
# from itertools import islice
#
# def group(iterable, n):
#     """Splits an iterable set into groups of size n and a group
#        of the remaining elements if needed.
#
#        Args:
#          iterable (list): The list whose elements are to be split into
#                           groups of size n.
#          n (int): The number of elements per group.
#
#        Returns:
#          list: The list of groups of size n,
#                where each group is a list of n elements.
#     """
#    # This needs to be a generator.
#     if not isinstance(iterable, typing.Generator):
#         iterable = (i for i in iterable)
#
#     output=[]
#     while True:
#         row = list(islice(iterable, n))
#         if not row:
#             break
#         output.append(row)
#
#     return output

#
# def group(iterable, n):
#     """Splits an iterable set into groups of size n and a group
#        of the remaining elements if needed.
#
#        Args:
#          iterable (list): The list whose elements are to be split into
#                           groups of size n.
#          n (int): The number of elements per group.
#
#        Returns:
#          list: The list of groups of size n,
#                where each group is a list of n elements.
#     """
#     # To split an iterable into groups of n
#     # overall algorith:
#     # Find the index
#
#     iterable = list(iterable)
#     i=0
#     output=[]
#     while i < len(iterable):
#         output.append(list(islice(iterable, i, i+n)))
#         i+=n
#     return output
#


#
#
# import types
# from itertools import islice
# def group(iterable, n):
#     """Splits an iterable set into groups of size n and a group
#        of the remaining elements if needed.
#
#        Args:
#          iterable (list): The list whose elements are to be split into
#                           groups of size n.
#          n (int): The number of elements per group.
#
#        Returns:
#          list: The list of groups of size n,
#                where each group is a list of n elements.
#     """
#     pass
#


#
#
# if __name__ == '__main__':
#     iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     n = 3
#     ret = group(iterable, n)
#     print(ret)
#
# score_dict={
#     'r':4,
#     'w':2,
#     'x':1,
#     '-':0
# }
#
# def _triplet_score(triplet):
#     return str(sum([score_dict[letter] for letter in triplet]))
#
# def get_octal_from_file_permission(rwx: str) -> str:
#     """Receive a Unix file permission and convert it to
#        its octal representation.
#
#        In Unix you have user, group and other permissions,
#        each can have read (r), write (w), and execute (x)
#        permissions expressed by r, w and x.
#
#        Each has a number:
#        r = 4
#        w = 2
#        x = 1
#
#        So this leads to the following input/ outputs examples:
#        rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
#        rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
#        r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
#     """
#     triplets = [rwx[_istep3:_istep3 + 3] for _istep3 in range(0, len(rwx), 3)]
#     return ''.join([_triplet_score(triplet) for triplet in triplets])
#
# from collections import namedtuple
# import re
# from bs4 import BeautifulSoup
# import requests
#
# # feed = https://news.python.sc/, to get predictable results we cached
# # first two pages - use these:
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# # https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html
#
# Entry = namedtuple('Entry', 'title points comments')
#
#
# def _create_soup_obj(url):
#     """Need utf-8 to properly parse emojis"""
#     resp = requests.get(url)
#     resp.encoding = "utf-8"
#     return BeautifulSoup(resp.text, "html.parser")
#
#
# def get_top_titles(url, top=5):
#     """Parse the titles (class 'title') using the soup object.
#        Return a list of top (default = 5) titles ordered descending
#        by number of points and comments.
#     """
#     soup = _create_soup_obj(url)
#     # your code ...
#
#     # strategy:
#     # parse out each part of the namedtuple
#     # create a list
#     # sort and return
#
#     titles = soup.find_all('span',class_='title')
#     points = soup.find_all(string=re.compile(r'points'))
#     comments = soup.find_all(string=re.compile(r'\d+ comments'))
#     sorted_entries = sorted([Entry(t.text.strip(), int(p.strip().split()[0]), int(c.split()[0])) for t,p,c in zip(titles, points, comments)],
#            key=lambda x: x[1]+x[2],reverse=True)
#     return [e for i, e in enumerate(sorted_entries) if i < top]
#
# import os
# from pathlib import Path
# import csv
# import json
# from json.decoder import JSONDecodeError
#
#
# EXCEPTION = 'exception caught'
# TMP = Path(os.getenv("TMP", "/tmp"))
#
#
# def convert_to_csv(json_file):
#     """Read/load the json_file (local file downloaded to /tmp) and
#        convert/write it to defined csv_file.
#         The data is in mounts > collected
#
#        Catch bad JSON (JSONDecodeError) file content, in that case print the defined
#        EXCEPTION string ('exception caught') to stdout reraising the exception.
#        This is to make sure you actually caught this exception.
#
#        Example csv output:
#        creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
#        32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
#        63502,ability_mount_hordescorpionamber,True,...
#        ...
#     """  # noqa E501
#     csv_file = TMP / json_file.name.replace('.json', '.csv')
#
#     # you code
#     # load the json file to memory.
#     with open(json_file,'r+') as fr, open(csv_file, 'w+', newline='') as fw:
#         try:
#             dict1=json.load(fr)
#         except JSONDecodeError:
#             print(EXCEPTION)
#             raise
#
#         dict_list = dict1['mounts']['collected']
#         fields = 'creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId'.split(',')
#
#         writer = csv.DictWriter(fw, fieldnames=fields)
#         writer.writeheader()
#         writer.writerows(dict_list)
#
# import hashlib
#
# GRAVATAR_URL = ("https://www.gravatar.com/avatar/"
#                 "{hashed_email}?s={size}&r=g&d=robohash")
#
#
# def create_gravatar_url(email, size=200):
#     """Use GRAVATAR_URL above to create a gravatar URL.
#
#        You need to create a hash of the email passed in.
#
#        PHP example: https://en.gravatar.com/site/implement/hash/
#
#        For Python check hashlib check out (md5 / hexdigest):
#        https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
#     """
#
#     hash_object = hashlib.md5()
#     hash_object.update(email.strip().lower().encode("utf-8"))
#     hashed_email = hash_object.hexdigest()
#     return f"https://www.gravatar.com/avatar/{hashed_email}?s={size}&r=g&d=robohash"
#
# import bisect
# THUMBS_UP, THUMBS_DOWN = '👍', '👎'
#
# class Thumbs:
#     def __mul__(self, other):
#         if int(other) == 0:
#             raise ValueError
#
#         sorted_list =[-3, 0, 4]
#         position=bisect.bisect_right(sorted_list,other)
#         match position:
#             case 0:
#                 return f"{THUMBS_DOWN} ({abs(other)}x)"
#             case 1:
#                 return "".join([THUMBS_DOWN for i in range(abs(other))])
#             case 2:
#                 return "".join([THUMBS_UP for i in range(other)])
#             case 3:
#                 return f"{THUMBS_UP} ({other}x)"
#     def __rmul__(self, other):
#         return self.__mul__(other)

#
# THUMBS_UP, THUMBS_DOWN = '👍', '👎'
#
# class Thumbs:
#     def __mul__(self, other):
#         if int(other) == 0:
#             raise ValueError
#
#         emoji = THUMBS_UP if other> 0 else THUMBS_DOWN
#         count = abs(other)
#         return f"{emoji} ({count}x)" if count>3 else f"{emoji * count}"
#
#
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
# from typing import Tuple
# from operator import itemgetter
#
# # https://pkgstore.datahub.io/core/gold-prices/annual_csv/data/343f626dd4f7bae813cfaac23fccd1bc/annual_csv.csv
# gold_prices = """
# 1950-12,34.720 1951-12,34.660 1952-12,34.790 1953-12,34.850 1954-12,35.040
# 1955-12,34.970 1956-12,34.900 1957-12,34.990 1958-12,35.090 1959-12,35.050
# 1960-12,35.540 1961-12,35.150 1962-12,35.080 1963-12,35.080 1964-12,35.120
# 1965-12,35.130 1966-12,35.180 1967-12,35.190 1968-12,41.113 1969-12,35.189
# 1970-12,37.434 1971-12,43.455 1972-12,63.779 1973-12,106.236 1974-12,183.683
# 1975-12,139.279 1976-12,133.674 1977-12,160.480 1978-12,207.895 1979-12,463.666
# 1980-12,596.712 1981-12,410.119 1982-12,444.776 1983-12,388.060 1984-12,319.622
# 1985-12,321.985 1986-12,391.595 1987-12,487.079 1988-12,419.248 1989-12,409.655
# 1990-12,378.161 1991-12,361.875 1992-12,334.657 1993-12,383.243 1994-12,379.480
# 1995-12,387.445 1996-12,369.338 1997-12,288.776 1998-12,291.357 1999-12,283.743
# 2000-12,271.892 2001-12,275.992 2002-12,333.300 2003-12,407.674 2004-12,442.974
# 2005-12,509.423 2006-12,629.513 2007-12,803.618 2008-12,819.940 2009-12,1135.012
# 2010-12,1393.512 2011-12,1652.725 2012-12,1687.342 2013-12,1221.588 2014-12,1200.440
# 2015-12,1068.317 2016-12,1152.165 2017-12,1265.674 2018-12,1249.887
# """  # noqa E501
#
#
# def years_gold_value_decreased(gold_prices: str = gold_prices) -> Tuple[int, int]:
#     """Analyze gold_prices returning a tuple of the year the gold price
#        decreased the most and the year the gold price increased the most.
#     """
#
#     # split into each year
#
#     price_each_year =[year.split(',') for year in gold_prices.split()]
#     yearly_change = [(price_each_year[i][0].split('-')[0], round(float(price_each_year[i][1]) - float(price_each_year[i - 1][1]), 2))
#     for i in range(1, len(price_each_year))]
#     return int(min(yearly_change, key=itemgetter(1))[0]), int(max(yearly_change, key=itemgetter(1))[0])
#
# from datetime import datetime
# import os
# from pathlib import Path
# from zipfile import ZipFile
# from operator import itemgetter
#
#
# TMP = Path(os.getenv("TMP", "/tmp"))
# LOG_DIR = TMP / 'logs'
# ZIP_FILE = 'logs.zip'

#
# def zip_last_n_files(directory: Path = LOG_DIR,
#                      zip_file: str = ZIP_FILE, n: int = 3):
#
#     file_paths = [(f,f.split('.')[0] + '_' +
#                    datetime.fromtimestamp(os.path.getctime(directory / f)).strftime('%Y-%m-%d') +
#                        '.log',
#                    os.path.getctime(directory / f))
#                   for f in os.listdir(directory)
#                   if os.path.isfile(directory / f )]
#
#     # sort them by creation time stamp
#     sorted_files = sorted(file_paths, key=itemgetter(2), reverse=True)
#
#     # zip the file
#     with ZipFile(directory / zip_file,'w') as zip:
#         for f in sorted_files[:n]:
#             zip.write(directory / f[0], arcname=f[1])

# Pybite solution
# def zip_last_n_files(directory: Path = LOG_DIR,
#                      zip_file: str = ZIP_FILE, n: int = 3):
#     with ZipFile(zip_file, 'w') as z:
#         for fi in sorted(directory.iterdir(),
#                          key=lambda x: x.stat().st_ctime,
#                          reverse=True)[:n]:
#             name, ext = fi.stem, fi.suffix
#             cdate = datetime.fromtimestamp(
#                 fi.stat().st_ctime
#             ).strftime('%Y-%m-%d')
#             out_file = f'{name}_{cdate}{ext}'
#             z.write(fi, arcname=out_file)

#
# def zip_last_n_files(directory: Path = LOG_DIR,
#                      zip_file: str = ZIP_FILE, n: int = 3):
#
# # try using pathlib instead
# # get the last n files based on created time
#
#     with ZipFile(directory / zip_file, 'w') as zip:
#
#         for f in sorted(directory.iterdir(),
#                         key = lambda x: x.stat().st_ctime,
#                         reverse=True
#                         )[:n]:
#             dt_str = datetime.fromtimestamp(f.stat().st_ctime).strftime('%Y-%m-%d')
#             file_name = f.stem + '_' + dt_str + f.suffix
#             zip.write(f, arcname=file_name)


# import re
#
# def capitalize_sentences(text: str) -> str:
#     """Return text capitalizing the sentences. Note that sentences can end
#        in dot (.), question mark (?) and exclamation mark (!)"""
#     sentences = re.split(r'([.?!])',text)
#     return ' '.join([sentence.lstrip().capitalize() for sentence in sentences]).replace(' ?','?').replace(' .','.').replace(' !','!').strip()
#
#

# Beautiful code
# def capitalize_sentences(text: str) -> str:
#     """Return text capitalizing the sentences. Note that sentences can end
#        in dot (.), question mark (?) and exclamation mark (!)"""
#     sentences = re.findall(r'(.*?[.?!])\s?', text)
#     return ' '.join([sentence.capitalize() for sentence in sentences])
#
# import re
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
#
# tmp = Path(os.getenv("TMP", "/tmp"))
# timings_log = tmp / 'pytest_timings.out'
# if not timings_log.exists():
#     urlretrieve(
#         'https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out',
#         timings_log
#     )
#
# pattern = r'(?P<test_num>^\d+) =+ (?P<num_passed>\d+) passed.* in (?P<seconds>[\d.]*) seconds?'
# def _parse_line(line):
#     match = re.search(pattern,line)
#     if match:
#         return match.groupdict()['test_num'], int(match.groupdict()['num_passed']), float(match.groupdict()['seconds'])
#     return ()
#
# def get_bite_with_fastest_avg_test(timings: list) -> str:
#     """Return the bite which has the fastest average time per test"""
#     time_dict = {}
#     for line in timings:
#         try:
#             test_num, num_passed, seconds = _parse_line(line)
#             time_dict[test_num] = seconds / num_passed
#         except:
#            pass
#
#     return min(time_dict.items(), key=lambda x:x[1])[0]

#
# def get_bite_with_fastest_avg_test(timings: list) -> str:
#     """Return the bite which has the fastest average time per test"""
#     pat = re.compile(
#         r'^(\d+) .*?(\d+) passed.* in ([0-9.]+) seconds.*$'
#     )
#     scores = {}
#     for timing in timings:
#         m = pat.match(timing.rstrip())
#         if not m:
#             continue
#         bite, num_tests, seconds = m.groups()
#         scores[bite] = float(seconds) / int(num_tests)
#     return min(scores.items(), key=itemgetter(1))[0]
#
#
# from pathlib import Path
# from pathlib import PosixPath
# import difflib
#
#
# def get_matching_files(directory: PosixPath, filter_str: str) -> list:
#     """Get all file names in "directory" and (case insensitive) match the ones
#        that exactly match "filter_str"
#
#        In case there is no exact match, return closely matching files.
#        If there are no closely matching files either, return an empty list.
#        (Return file names, not full paths).
#
#        For example:
#
#        d = Path('.')
#        files in dir: bite1 test output
#
#        get_matching_files(d, 'bite1') => ['bite1']
#        get_matching_files(d, 'Bite') => ['bite1']
#        get_matching_files(d, 'pybites') => ['bite1']
#        get_matching_files(d, 'test') => ['test']
#        get_matching_files(d, 'test2') => ['test']
#        get_matching_files(d, 'output') => ['output']
#        get_matching_files(d, 'o$tput') => ['output']
#        get_matching_files(d, 'nonsense') => []
#     """
#     cut_off = 0.6
#     files = [f.name for f in Path(directory).iterdir() if f.is_file()]
#     return [name.lower() for name in files if difflib.SequenceMatcher(None,name,filter_str).ratio()> cut_off ]
#
# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'Fizz Buzz'
#     elif num % 3 == 0:
#         return 'Fizz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     else:
#         return num
#
# import json
# from contextlib import suppress
# from dataclasses import dataclass
# from ipaddress import AddressValueError, IPv4Address, IPv4Network
# from pathlib import Path
# from typing import List
#
#
# @dataclass(frozen=True)
# class ServiceIPRange:
#     """
#     Represents an IPv4 public network range, allocated by AWS for use with
#     a specific service and region.
#     """
#
#     service: str
#     region: str
#     cidr: IPv4Network
#
#     def __str__(self):
#         return (f"{self.cidr} is allocated to the {self.service} "
#                 f"service in the {self.region} region")
#
#
# def parse_ipv4_service_ranges(source: Path) -> List[ServiceIPRange]:
#     """
#     Given a JSON file containing AWS public IP addresses, return a list of
#     ServiceIPRange objects representing all IPv4 network ranges. See also:
#
#     https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
#     """
#     data = json.loads(source.read_text())
#     with suppress(AddressValueError):
#         prefixes = data["prefixes"]
#         ipv4_service_ranges = [
#             ServiceIPRange(
#                 service=prefix["service"],
#                 region=prefix["region"],
#                 cidr=IPv4Network(prefix["ip_prefix"]),
#             )
#             for prefix in prefixes
#         ]
#     return ipv4_service_ranges
#
#
# def get_aws_service_range(address: str,
#                           service_ranges: list) -> List[ServiceIPRange]:
#     """
#     Return a list of ServiceIPRange objects representing all AWS public
#     IP ranges that contain `address`. Raise a ValueError if `address`
#     is not a valid IPv4 address.
#     """
#     try:
#         ipv4_address = IPv4Address(address)
#     except AddressValueError:
#         raise ValueError("Address must be a valid IPv4 address")
#
#     return [range_ for range_ in service_ranges
#             if ipv4_address in range_.cidr]
#
# import os
# from pathlib import Path
# from typing import List, Optional
# from urllib.request import urlretrieve
#
# S3 = "https://bites-data.s3.us-east-2.amazonaws.com/{}"
# FILE_NAME = "mutpy.out"
# TMP = os.getenv("TMP", "/tmp")
# PATH = Path(TMP, FILE_NAME)
#
# if not PATH.exists():
#     urlretrieve(S3.format(FILE_NAME), PATH)
#
#
# def _get_data(path=PATH):
#     with open(path) as f:
#         return [line.rstrip() for line in f.readlines()]
#
#
# def filter_killed_mutants(
#     mutpy_output: Optional[List[str]] = None
# ) -> List[str]:
#     """Read in the passed in mutpy output and filter out the code snippets of
#        mutation tests that were killed. Surviving mutants should be shown in
#        full, as well the surrounding output.
#
#        For example, this is a killed mutant:
#
#          - [#  15] DDL account:
#       --------------------------------------------------------------------------------
#         23:         if not (isinstance(amount, int)):
#         24:             raise ValueError('please use int for amount')
#         25:         self._transactions.append(amount)
#         26:
#       - 27:     @property
#       - 28:     def balance(self):
#       + 27:     def balance(\
#       + 28:         self):
#         29:         return self.amount + sum(self._transactions)
#         30:
#         31:     def __len__(self):
#         32:         return len(self._transactions)
#       --------------------------------------------------------------------------------
#       [0.10240 s] killed by test_account.py::test_balance
#
#       You should reduce this to:
#
#          - [#  15] DDL account:
#       [0.10240 s] killed by test_account.py::test_balance
#
#       So you mute all that is in between the two dashed lines.
#
#       You do the same for incompetent mutants, for example:
#          - [#   3] AOR account:
#       --------------------------------------------------------------------------------
#         43:     def __add__(self, other):
#         44:         owner = '{}&{}'.format(self.owner, other.owner)
#         45:         start_amount = self.amount + other.amount
#         46:         acc = Account(owner, start_amount)
#       - 47:         for t in list(self) + list(other):
#       + 47:         for t in list(self) - list(other):
#         48:             acc.add_transaction(t)
#         49:         return acc
#       --------------------------------------------------------------------------------
#       [0.10011 s] incompetent
#
#       ... becomes:
#          - [#   3] AOR account:
#       [0.10011 s] incompetent
#
#       Return the filtered output as a list of lines.
#     """
#     if mutpy_output is None:
#         mutpy_output = _get_data()
#
#     final_output = []
#     in_section = False
#     section_lines = []
#
#     for line in mutpy_output:
#         if line.startswith('-------'):
#             in_section = not in_section
#             section_lines.append(line)
#             continue
#
#         if in_section:
#             section_lines.append(line)
#             continue
#
#         if "killed by" in line or "] incompetent" in line:
#             section_lines = []
#             final_output.append(line)
#             continue
#
#         if not in_section and len(section_lines)>0:
#             for l in section_lines:
#                 final_output.append(l)
#             section_lines = []
#
#         final_output.append(line)
#
#     return final_output
#
#
# import os
# from pathlib import Path
# from typing import Dict, Generator, List, Optional
# from urllib.request import urlretrieve
#
# S3 = "https://bites-data.s3.us-east-2.amazonaws.com/{}"
# FILE_NAME = "mutpy.out"
# TMP = os.getenv("TMP", "/tmp")
# PATH = Path(TMP, FILE_NAME)
#
# if not PATH.exists():
#     urlretrieve(S3.format(FILE_NAME), PATH)
#
# START = "[*] Start mutants generation and execution:"
# END = "[*] Mutation score "
#
#
# def _get_data(path=PATH):
#     with open(path) as f:
#         return [line.rstrip() for line in f.readlines()]
#
#
# def filter_killed_mutants(
#     mutpy_output: Optional[List[str]] = None
# ) -> Generator:
#     """Read in the passed in mutpy output and filter out the code snippets of
#        mutation tests that were killed. Surviving mutants should be shown in
#        full, as well the surrounding output.
#
#        For example, this is a killed mutant:
#
#          - [#  15] DDL account:
#       --------------------------------------------------------------------------------
#         23:         if not (isinstance(amount, int)):
#         24:             raise ValueError('please use int for amount')
#         25:         self._transactions.append(amount)
#         26:
#       - 27:     @property
#       - 28:     def balance(self):
#       + 27:     def balance(\
#       + 28:         self):
#         29:         return self.amount + sum(self._transactions)
#         30:
#         31:     def __len__(self):
#         32:         return len(self._transactions)
#       --------------------------------------------------------------------------------
#       [0.10240 s] killed by test_account.py::test_balance
#
#       You should reduce this to:
#
#          - [#  15] DDL account:
#       [0.10240 s] killed by test_account.py::test_balance
#
#       So you mute all that is in between the two dashed lines.
#
#       You do the same for incompetent mutants, for example:
#          - [#   3] AOR account:
#       --------------------------------------------------------------------------------
#         43:     def __add__(self, other):
#         44:         owner = '{}&{}'.format(self.owner, other.owner)
#         45:         start_amount = self.amount + other.amount
#         46:         acc = Account(owner, start_amount)
#       - 47:         for t in list(self) + list(other):
#       + 47:         for t in list(self) - list(other):
#         48:             acc.add_transaction(t)
#         49:         return acc
#       --------------------------------------------------------------------------------
#       [0.10011 s] incompetent
#
#       ... becomes:
#          - [#   3] AOR account:
#       [0.10011 s] incompetent
#
#       Return the filtered output as a list of lines.
#     """
#     if mutpy_output is None:
#         mutpy_output = _get_data()
#
#     start_index = 0
#     end_index = 0
#     for i, line in enumerate(mutpy_output):
#         if line.startswith(START):
#             start_index = i
#         elif line.startswith(END):
#             end_index = i
#
#     mutants: Dict[str, List[str]] = {}
#     key = ""
#     for line in mutpy_output[start_index + 1:end_index]:
#         if line.startswith('   - [#'):
#             key = line
#             mutants[key] = []
#             continue
#         mutants[key].append(line)
#
#     yield from mutpy_output[:start_index+1]
#
#     for key, output in mutants.items():
#         survived = 'survived' in output[-1]
#         yield key
#         if survived:
#             yield from output
#         else:
#             yield output[-1]
#
#     yield from mutpy_output[end_index:]
#

#
# STAR = "+"
# LEAF = "*"
# TRUNK = "|"
#
#
# def generate_improved_xmas_tree(rows=10):
#     """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
#        for given rows of leafs (default 10).
#        For more information see the test and the bite description"""
#
#     width = rows*2 -1
#     string_list = [f"{STAR:^{width}}"]
#
#     for i in range(1,rows+1):
#         num_stars = i * 2 - 1
#         string_list.append(f"{LEAF * num_stars:^{width}}")
#
#     trunk_width = round(width/2)
#     if (width - trunk_width%2) !=0 :
#         trunk_width+=1
#
#     for _ in range(2):
#         string_list.append(f"{TRUNK * trunk_width:^{width}}")
#     return '\n'.join(string_list)
#
# from random import sample
#
#
# def gen_hex_color():
#     while True:
#         r, g, b = sample(range(0, 256), 3)
#         yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()
#
# generator = gen_hex_color()
# for i in range(5):
#     print(next(generator))
#
# result = [next(generator) for i in range(3)]
#
# print(next(generator))
# type(next(generator))
#
# def square(x):
#     return x*x
#
# from random import sample
#
#
# def gen_hex_color():
#     while True:
#         r, g, b = sample(range(0, 256), 3)
#         yield '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()
#
# #'#{:02x}{:02x}{:02x}'.format(0, 0, 0).upper()
#
# import pandas as pd
# from operator import add, sub, mul, truediv
# from functools import reduce
#
# def series_simple_math(
#     ser: pd.Series, function: str, number: int
# ) -> pd.core.series.Series:
#     """Write some simple math helper functions for series.
#     Take the given series, perfrom the required operation and
#         return the new series.
#     For example. Give the series:
#         0    0
#         1    1
#         2    2
#         dtype: int64
#     Function 'add' and 'number' 2 you should return
#         0     2
#         1     3
#         2     4
#         dtype: int64
#     :param ser: Series to perform operation on
#     :param function: The operation to perform
#     :param number: The number to apply the operation to
#     """
#     func_dict = {'add':add, 'sub':sub, 'mul':mul, 'div':truediv}
#     return ser.apply(lambda x,func,y:func(x,y), args=(func_dict[function],number))
#
# def complex_series_maths(
#     ser_01: pd.Series, ser_02: pd.Series, function: str
# ) -> pd.core.series.Series:
#     """Write some math helper functions for series.
#     Take the two given series, perfrom the required operation and
#         return the new series.
#     For example. Give the series:
#         0    0
#         1    1
#         2    2
#         dtype: int64
#
#     And the series:
#         0     2
#         1     3
#         2     4
#         dtype: int64
#
#     If the function given is 'add' you should return
#         0     2
#         1     4
#         2     6
#         dtype: int64
#
#     :param ser_01: Primary series to perform operation on
#     :param ser_02: Secondary series to perform operation on
#     :param function: The operation to perform
#
#     Note:
#     For this function always add ser_02 to ser_01,
#         subtract ser_02 from ser_01,
#         multiply ser_01 by ser_02,
#         divide ser_01 by ser_02
#     Don't worry about None's and NaN and divide by zero.
#         Let pandas do the work for you.
#     """
#     func_dict = {'add': 'add', 'sub': 'sub', 'mul': 'mul', 'div': 'truediv'}
#     return getattr(ser_01, func_dict[function])(ser_02)
#
#
# def create_series_mask(ser: pd.Series, mask: list) -> pd.core.series.Series:
#     """Write a trivial function to create a pandas series mask of a list
#     of letters.
#     Be careful, although this sounds very similar to the .mask() method,
#         that's not what we're looking for here.
#     For example. Give the series x:
#         0    0
#         1    1
#         2    2
#         3    3
#         4    4
#         dtype: int64
#
#     You can create a mask for even numbers like this:
#     >>> mask = x % 2 == 0
#     >>> mask
#         0     True
#         1    False
#         2     True
#         3    False
#         4     True
#         dtype: bool
#
#     And then apply the mask:
#     >>> x[mask]
#         0    0
#         2    2
#         4    4
#         dtype: int64
#
#     Of course for simpler masks you can just do this:
#     >>> x[x %2 == 0]
#         0    0
#         2    2
#         4    4
#         dtype: int64
#
#     :param ser: Series to perform operation on
#     :param mask: The list of letters to be masked
#     """
#     return ser.apply(lambda x: x in mask)
#
#
# def _range_helper(ser, target_val, within_range):
#     return (ser-target_val).abs() <= within_range
#
# def custom_series_function(ser: pd.Series,
#                            within: float) -> pd.core.series.Series:
#     """A more challenging mask to apply.
#     When passed a series of floats, return all values
#         within the given rage of:
#          - the minimum value
#          - the 1st quartile value
#          - the second quartile value
#          - the mean
#          - the third quartile value
#          - the maximum value
#     You may want to brush up on some simple statistics to help you here.
#     Also, the series is passed to you sorted assending.
#         Be sure that you don't return values out of sequence.
#
#     So, for example if you mean is 5.0 and within is 0.1
#         return all value between 4.9 and 5.1 inclusive
#
#     :param ser: Series to perform operation on
#     :param within: The value to calculate the range of number within
#     """
#     # key stats
#     min_val = ser.min()
#     fq_val = ser.quantile(0.25)
#     sq_val = ser.quantile(0.50)
#     mean_val = ser.mean()
#     tq_val = ser.quantile(0.75)
#     max_val = ser.max()
#
#     targets = [min_val,fq_val,sq_val,mean_val,tq_val,max_val]
#     # loop through all the stats & figure out which ones to keep
#     indexes = [_range_helper(ser, target, within) for target in targets]
#     # combine all the indexes
#     mask = reduce(lambda x,y: x|y, indexes)
#     return ser[mask]
#
# import pandas as pd
#
# # Study this solution. Learn from it next.
# def custom_series_function(ser: pd.Series,
#                            within: float) -> pd.core.series.Series:
#     """A more challenging mask to apply.
#     When passed a series of floats, return all values
#         within the given rage of:
#          - the minimum value
#          - the 1st quartile value
#          - the second quartile value
#          - the mean
#          - the third quartile value
#          - the maximum value
#     You may want to brush up on some simple statistics to help you here.
#     Also, the series is passed to you sorted assending.
#         Be sure that you don't return values out of sequence.
#
#     So, for example if you mean is 5.0 and within is 0.1
#         return all value between 4.9 and 5.1 inclusive
#
#     :param ser: Series to perform operation on
#     :param within: The value to calculate the range of number within
#     """
#     def sepal_filter(value, stats, within):
#         # The statistics from describe are passed in as a dictionary
#         for k, v in stats.items():
#             # We want to ignore the count and the standard deviation
#             if (k == "count") or (k == "std"):
#                 next
#
#             # For clarity create the min / max rage
#             range_min = v - within
#             range_max = v + within
#
#             # If the current value is in the range return true
#             if range_min <= value <= range_max:
#                 return True
#
#         # Return False if the value does not match any of the ranges
#         return False
#
#     # Create a dictionary of the series statistics
#     measures = ser.describe().to_dict()
#
#     return ser[ser.apply(sepal_filter, args=(measures, within))]
#
# import pandas as pd
# # Study this solution. Learn from it next.
#
#
# # write a filter function to
# def filter_cell_val(cell_val, stat_dict, within):
#     for stat, stat_val  in stat_dict.items():
#         if abs(cell_val-stat_val)<= within:
#             return True
#     return False
#
# def custom_series_function(ser: pd.Series,
#                            within: float) -> pd.core.series.Series:
#     """A more challenging mask to apply.
#     When passed a series of floats, return all values
#         within the given rage of:
#          - the minimum value
#          - the 1st quartile value
#          - the second quartile value
#          - the mean
#          - the third quartile value
#          - the maximum value
#     You may want to brush up on some simple statistics to help you here.
#     Also, the series is passed to you sorted assending.
#         Be sure that you don't return values out of sequence.
#
#     So, for example if you mean is 5.0 and within is 0.1
#         return all value between 4.9 and 5.1 inclusive
#
#     :param ser: Series to perform operation on
#     :param within: The value to calculate the range of number within
#     """
#
#     # rewrite myself from the official solution:
#     # steps:
#     # Make a dictionary of all the stats and the cut off values
#     stat_dict = ser.describe().to_dict()
#     del stat_dict['count']
#     del stat_dict['std']
#
#     return ser[ser.apply(filter_cell_val, args=(stat_dict,within))]
#


#
# # My solution
# import os
# from urllib.request import urlretrieve
# from collections import Counter
# from dataclasses import dataclass
# from io import StringIO
#
#
# # Translation Table:
# # https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# # Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# # All Base 'T's need to be converted to 'U's to convert DNA to RNA
# TRANSL_TABLE_11 = """
#     AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
#   Starts = ---M------**--*----M------------MMMM---------------M------------
#   Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
#   Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
#   Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
# """
#
# # Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"
#
# # Order of bases in the table
# BASE_ORDER = ["U", "C", "A", "G"]
#
# @dataclass
# class CodonUsage:
#     codon: str
#     aa: str
#     freq: float=0
#     count: int=0
#
#     def __str__(self):
#         return f"  {self.codon}:  {self.aa:<3} {round(self.freq,1):>4}  {self.count:>5}  "
#
# u1=CodonUsage('UUU','F',32.7,26200)
# print(CodonUsage('UUU','F',32.7,26200))
#
# def _preload_sequences(url=URL):
#     """
#     Provided helper function
#     Returns coding sequences, one sequence each line
#     """
#     filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
#     if not os.path.isfile(filename):
#         urlretrieve(url, filename)
#     with open(filename, "r") as f:
#         return f.readlines()
#
#
# # Run the translation table through all the sequences
# def get_counts(sequence):
#     sequence=sequence.strip()
#     seq_gen = (sequence[i:i+3] for i in range(0, len(sequence),3))
#     return Counter(seq_gen)
#
#
# def return_codon_usage_table(
#     sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
# ):
#     """
#     Receives a list of gene sequences and a translation table string
#     Returns a string with all bases and their frequencies in a table
#     with the following fields:
#     codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences
#
#     Skip invalid coding sequences:
#        --> must consist entirely of codons (3-base triplet)
#     """
#
#     # Parse translation table to a data structure
#     translation_table_str=TRANSL_TABLE_11
#     translation_list = [seq.strip().split()[-1].replace('T','U') for seq in translation_table_str.strip().split('\n')]
#     translation_list.pop(1) # take out the unused
#     translation_list[0]=translation_list[0].replace('U','T')
#         # Instantiate dataclass
#     condon_dict = {''.join(t[1:]):CodonUsage(''.join(t[1:]),t[0]) for t in zip(translation_list[0],translation_list[1],translation_list[2],translation_list[3])}
#
#     # loop through all of them
#     aa_counts = Counter()
#
#     for s in sequences:
#         aa_counts.update(get_counts(s))
#
#     # Calculate usage
#     total_bases = sum(val for key, val in aa_counts.items())
#     for key, val in aa_counts.items():
#         condon_dict[key].count=val
#         condon_dict[key].freq=round(val/total_bases,4 )*1000
#
#     # Output/Display table
#     string_io = StringIO()
#     header_str = ''.join([ '|  Codon AA  Freq  Count  '  for i in range(4)]) +'|\n'
#     string_io.write(header_str)
#     divider_str = '-'*105 + '\n'
#     string_io.write(divider_str)
#
#     codon_order = 'UUU UCU UAU UGU UUC UCC UAC UGC UUA UCA UAA UGA UUG UCG UAG UGG CUU CCU CAU CGU CUC CCC CAC CGC CUA CCA CAA CGA CUG CCG CAG CGG AUU ACU AAU AGU AUC ACC AAC AGC AUA ACA AAA AGA AUG ACG AAG AGG GUU GCU GAU GGU GUC GCC GAC GGC GUA GCA GAA GGA GUG GCG GAG GGG'.split()
#     for i, val in enumerate(codon_order, 1):
#         string_io.write(f"|{condon_dict[val]}")
#         if i % 4 == 0:
#             string_io.write(f"|\n")
#         if i % 16 == 0:
#             string_io.write(divider_str)
#
#     return string_io.getvalue()
#
#
#
#
#
# if __name__ == "__main__":
#     print(return_codon_usage_table())
#
#
#
# import os
# from urllib.request import urlretrieve
# from textwrap import wrap
# from collections import Counter
#
# # Translation Table:
# # https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# # Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# # All Base 'T's need to be converted to 'U's to convert DNA to RNA
# TRANSL_TABLE_11 = """
#     AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
#   Starts = ---M------**--*----M------------MMMM---------------M------------
#   Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
#   Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
#   Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
# """
#
# # Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"
#
# # Order of bases in the table
# BASE_ORDER = ["U", "C", "A", "G"]
#
#
# def _preload_sequences(url=URL):
#     """
#     Provided helper function
#     Returns coding sequences, one sequence each line
#     """
#     filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
#     if not os.path.isfile(filename):
#         urlretrieve(url, filename)
#     with open(filename, "r") as f:
#         return f.readlines()
#
#
# def _get_translation_table(translation_table_str):
#     """
#     Receives a translation table string
#     Returns a dict of {'UUU': 'F', 'UUC': 'F', 'UUA': 'L' ..}
#     """
#     lines = translation_table_str.strip().split("\n")
#     truncated = [line.split("= ")[1] for line in lines]
#     zipped = zip(*truncated)
#     return {
#         "".join([base1, base2, base3]).replace("T", "U"): codon
#         for (codon, _, base1, base2, base3) in zipped
#     }
#
#
# def _count_codons(sequences):
#     """
#     Receives list of genes
#     Returns codon Counter for all sequences supplied
#     """
#     counts = Counter()
#     for sequence in sequences:
#         sequence = sequence.strip()
#         if len(sequence) % 3 != 0:  # Skip partial genes
#             continue
#         counts.update(Counter(wrap(sequence, 3)))
#     return counts
#
#
# def return_codon_usage_table(
#     sequences=_preload_sequences(), translation_table_str=TRANSL_TABLE_11
# ):
#     """
#     Receives a list of gene sequences and a translation table string
#     Returns a string with all bases and their frequencies in a table
#     with the following fields:
#     codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences
#
#     Skip invalid coding sequences:
#        --> must consist entirely of codons (3-base triplet)
#     """
#
#     translation_table = _get_translation_table(translation_table_str)
#
#     counts = _count_codons(sequences)
#     codon_sum = sum(counts.values())
#
#     header = "|  Codon AA  Freq  Count  " * 4 + "|"
#     divider = "-" * len(header)
#
#     table = f"{header}\n{divider}\n"
#
#     for base1 in BASE_ORDER:
#         for base3 in BASE_ORDER:
#             for base2 in BASE_ORDER:
#                 codon = f"{base1}{base2}{base3}"
#                 codon_count = counts[codon]
#                 amino_acid = translation_table[codon]
#                 freq = round(float(codon_count) / codon_sum * 1000, 1)
#                 table += f"|  {codon}:  {amino_acid}  {freq: >5}  {codon_count: >5}  "  # noqa E501
#             table += "|\n"
#         table += f"{divider}\n"
#     return table
#
#
# if __name__ == "__main__":
#     print(return_codon_usage_table())
#
# import json
# from collections import namedtuple
# from typing import List
#
# import requests
# from bs4 import BeautifulSoup as Soup
# from dateutil.parser import parse
#
# PYCON_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"
#
# PyCon = namedtuple("PyCon", "name city country start_date end_date url")
#
# country_lookup = {
#     "Africa": [
#         "Algeria", "Angola", "Benin", "Botswana",
#         "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
#         "Central African Republic", "Chad", "Comoros",
#         "Democratic Republic of the Congo",
#         "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
#         "Ethiopia", "Gabon", "Ghana", "Guinea", "Guinea-Bissau",
#         "Ivory Coast", "Kenya", "Lesotho", "Liberia",
#         "Libya", "Madagascar", "Malawi", "Mali",
#         "Mauritania", "Mauritius", "Morocco", "Mozambique",
#         "Namibia", "Niger", "Nigeria", "Republic of the Congo",
#         "Rwanda", "São Tome and Principe", "Senegal", "Seychelles",
#         "Sierra Leone", "Somalia", "South Africa", "South Sudan",
#         "Sudan", "Swaziland", "Tanzania", "The Gambia",
#         "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe",
#     ],
#     "Asia": [
#         "Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
#         "Bangladesh", "Bhutan", "Brunei", "Cambodia",
#         "China", "East Timor", "Georgia", "India",
#         "Indonesia", "Iran", "Iraq", "Israel",
#         "Japan", "Jordan", "Kazakhstan", "Kuwait",
#         "Kyrgyzstan", "Laos", "Lebanon", "Malaysia",
#         "Maldives", "Mongolia", "Myanmar", "Nepal",
#         "North Korea", "Oman", "Pakistan", "Palestinian territories",
#         "Philippines", "Qatar", "Saudi Arabia", "Singapore",
#         "South Korea", "Sri Lanka", "Syria", "Taiwan",
#         "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
#         "United Arab Emirates", "Uzbekistan", "Vietnam",
#         "Yemen",
#     ],
#     "Australia and Oceania": [
#         "Australia", "Federated States of Micronesia", "Fiji",
#         "Kiribati", "Marshall Islands", "Nauru", "New Zealand",
#         "Palau", "Papua New Guinea", "Samoa", "Solomon Islands",
#         "Tonga", "Tuvalu", "Vanuatu",
#     ],
#     "Europe": [
#         "Albania", "Andorra", "Austria", "Belarus", "Belgium",
#         "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus",
#         "Czech Republic", "Denmark", "Estonia", "Finland",
#         "France", "Germany", "Greece", "Hungary", "Iceland",
#         "Italy", "Latvia", "Liechtenstein", "Lithuania",
#         "Luxembourg", "Malta", "Moldova", "Monaco",
#         "Montenegro", "Netherlands", "Norway", "Poland",
#         "Portugal", "Republic of Ireland", "Republic of Macedonia",
#         "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
#         "Slovenia", "Spain", "Sweden", "Switzerland",
#         "Ukraine", "United Kingdom", "U.K.", "Vatican City",
#     ],
#     "North America": [
#         "Antigua and Barbuda", "Barbados", "Belize",
#         "Canada", "Costa Rica", "Cuba", "Dominica",
#         "Dominican Republic", "El Salvador", "Grenada",
#         "Guatemala", "Haiti", "Honduras", "Jamaica",
#         "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
#         "Saint Lucia", "Saint Vincent and the Grenadines",
#         "The Bahamas", "Trinidad and Tobago",
#         "United States of America", "U.S.A.",
#     ],
#     "South America": [
#         "Argentina", "Bolivia", "Brazil", "Chile",
#         "Colombia", "Ecuador", "Guyana", "Paraguay",
#         "Peru", "Suriname", "Uruguay", "Venezuela",
#     ],
# }
#
#
# def get_continent(country: str) -> str:
#     """
#     Given a country name returns the associated continent of the country.
#
#     :param country: The name of the country
#     :type country: str
#     :returns: The continent of the country
#     :rtype: str
#     """
#     for continent, countries in country_lookup.items():
#         for c in countries:
#             if country.lower() in c.lower():
#                 return continent
#
#
# def _get_pycon_data():
#     """Helper function that retrieves the required PyCon data"""
#     with requests.Session() as session:
#         return session.get(PYCON_DATA).content.decode("utf-8")
#
#
# def get_pycon_events(data=_get_pycon_data()) -> List[PyCon]:
#     """
#     Scrape the PyCon events from the given website data and
#     return a list of PyCon namedtuples. Pay attention to the
#     application/ld+json data structure website data.
#     """
#     data = _get_pycon_data()
#     soup = Soup(data, 'html.parser')
#     ldjson = soup.find_all('script', type='application/ld+json')
#
#     # parse with json package
#     pycon_events = []
#     for d in ldjson:
#         data_dict = json.loads(d.contents[0].strip())
#         name = data_dict['name']
#         city = data_dict['location']['address']['addressLocality']
#         country = data_dict['location']['address']['addressCountry']
#         start_date = parse(data_dict['startDate'])
#         end_date = parse(data_dict['endDate'])
#         url = data_dict['url']
#         event = PyCon(name, city, country, start_date, end_date, url)
#         if "pycon" in name.lower():
#             pycon_events.append(event)
#     return pycon_events
#
#
# def filter_pycons(pycons: List[PyCon],
#                   year: int = 2019,
#                   continent: str = "Europe") -> List[PyCon]:
#     """
#     Given a list of PyCons a year and a continent return
#     a list of PyCons that take place in that year and on
#     that continent.
#     """
#     return [event for event in pycons if year == event.start_date.year and get_continent(event.country)==continent]
#
# from urllib.request import urlretrieve
# from pathlib import Path
# import os
# from csv import DictReader
#
# XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
# THRESHOLDS = (5000, 0.05)
#
# def calculate_flux(XYZ: str) -> list:
#     """Read the data in from xyz.csv
#     add two new columns, one to calculate dollar flux,
#     and the other to calculate percentage flux
#     return as a list of tuples
#     """
#     tmp = os.getenv("TMP", "/tmp")
#     path = Path(tmp, "xyz.csv")
#     urlretrieve(XYZ, path)
#     rows = []
#     with open(path,'r') as f_read:
#         reader = DictReader(f_read)
#         for line in reader:
#             row=line['Account']
#             start=int(line['12/31/19'])
#             end=int(line['12/31/20'])
#             dollar_flux = end - start
#             percent_flux = dollar_flux / start
#             row_data = (row, end, start, dollar_flux, percent_flux)
#             rows.append(row_data)
#     return  rows
#
#
# def identify_flux(xyz: list) -> list:
#     """Load the list of tuples, iterate through
#     each item and determine if it is above both
#     thresholds. if so, add to the list
#     """
#
#     flagged_lines = []
#     all_fluxes=calculate_flux(XYZ)
#     for row in all_fluxes:
#         if abs(row[3])>THRESHOLDS[0] and abs(row[4])>THRESHOLDS[1]:
#             flagged_lines.append(row)
#
#     return flagged_lines
#
# # See tests for a more comprehensive complementary table
# SIMPLE_COMPLEMENTS_STR = """#Reduced table with bases A, G, C, T
#  Base	Complementary Base
#  A	T
#  T	A
#  G	C
#  C	G
# """
#
# # a function to parse complement table -> dict
#
# def make_complement_dict(str_table):
#     complement_dict ={}
#     rows=str_table.split('\n')
#     for row in rows:
#         if '\t' in row:
#             elements = row.split('\t')
#         else:
#             elements=row.split('  ')
#         print(f"elements: {elements}")
#         if elements and len(elements[0].strip())==1:
#             complement_dict[elements[0].strip().upper()] = elements[-1].strip().upper()
#     return complement_dict
#
#
# # Recommended helper function
# def _clean_sequence(sequence, str_table):
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns all sequences converted to upper case and remove invalid
#     characters
#     t!t%ttttAACCG --> TTTTTTAACCG
#     """
#     complement_dict = make_complement_dict(str_table)
#     alphbets = complement_dict.keys()
#     return ''.join([char for char in sequence.upper() if char in alphbets])
#
#
# def reverse(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a reversed string of sequence while removing all characters
#     not found in str_table characters
#     e.g. t!t%ttttAACCG --> GCCAATTTTTT
#     """
#     clean_seq = _clean_sequence(sequence, str_table)
#     return ''.join(reversed(clean_seq))
#
# def complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a string containing complementary bases as defined in
#     str_table while removing non input_sequence characters
#     e.g. t!t%ttttAACCG --> AAAAAATTGGC
#     """
#     complement_dict = make_complement_dict(str_table)
#     clean_seq = _clean_sequence(sequence, str_table)
#     return clean_seq.translate(str.maketrans(complement_dict))
#
#
# def reverse_complement(sequence, str_table=SIMPLE_COMPLEMENTS_STR):
#     """
#     Receives a DNA sequence and a str_table that defines valid (and
#     complementary) bases
#     Returns a string containing complementary bases as defined in str_table
#     while removing non input_sequence characters
#     e.g. t!t%ttttAACCG --> CGGTTAAAAAA
#     """
#     return complement(reverse(sequence,str_table),str_table)
#
# #reverse_complement()
#
# import json
# from dataclasses import dataclass
# from datetime import datetime
# from math import acos, cos, radians, sin
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
#
# from dateutil.parser import parse
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
# RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"
#
# tmp = Path(os.getenv("TMP", "/tmp"))
# pycons_file = tmp / "pycons-europe-2019.json"
# nominatim_responses = tmp / "nominatim_responses.json"
#
# if not pycons_file.exists() or not nominatim_responses.exists():
#     urlretrieve(URL, pycons_file)
#     urlretrieve(RESPONSES, nominatim_responses)
#
#
# @dataclass
# class PyCon:
#     name: str
#     city: str
#     country: str
#     start_date: datetime
#     end_date: datetime
#     URL: str
#     lat: float = None
#     lon: float = None
#
#
# @dataclass
# class Trip:
#     origin: PyCon
#     destination: PyCon
#     distance: float
#
#
# def _get_pycons():
#     """Helper function that retrieves required PyCon data
#        and returns a list of PyCon objects
#     """
#     with open(pycons_file, "r", encoding="utf-8") as f:
#         return [
#             PyCon(
#                 pycon["name"],
#                 pycon["city"],
#                 pycon["country"],
#                 parse(pycon["start_date"]),
#                 parse(pycon["end_date"]),
#                 pycon["url"],
#             )
#             for pycon in json.load(f)
#         ]
#
#
# def _km_distance(origin, destination):
#     """ Helper function that retrieves the air distance in kilometers for two pycons """
#     lon1, lat1, lon2, lat2 = map(
#         radians, [origin.lon, origin.lat, destination.lon, destination.lat]
#     )
#     return 6371 * (
#         acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
#     )
#
#
# # Your code #
# def update_pycons_lat_lon(pycons):
#     """
#     Update the latitudes and longitudes based on the city and country
#     the PyCon takes places. Use requests from the Nominatim API stored in the
#     nominatim_responses json file.
#     """
#     # parse api response
#     with open(nominatim_responses,'r') as nominatim_read:
#         responses = json.load(nominatim_read)
#
#     for p in pycons:
#         key = f"https://nominatim.openstreetmap.org/search?q={p.city},{p.country}&format=json&accept-language=en"
#         p.lat = float(responses[key][0]['lat'])
#         p.lon = float(responses[key][0]['lon'])
#
#     return pycons
#
#
#
# def create_travel_plan(pycons):
#     """
#     Create your travel plan to visit all the PyCons.
#     Assume it's now the start of 2019!
#     Return a list of Trips with each Trip containing the origin PyCon,
#     the destination PyCon and the travel distance between the PyCons.
#     """
#     pycons=update_pycons_lat_lon(pycons)
#     sorted_pycons = sorted(pycons,key = lambda x: x.start_date)
#     trip_plan = []
#     for i in range(1,len(sorted_pycons)):
#         start_city = sorted_pycons[i-1]
#         destination_city = sorted_pycons[i]
#         distance = _km_distance(start_city,destination_city)
#         trip_plan.append(Trip(start_city,destination_city,distance ))
#     return trip_plan
#
# def total_travel_distance(journey):
#     """
#     Return the total travel distance of your PyCon journey in kilometers
#     rounded to one decimal.
#     """
#     return round(sum(trip.distance for trip in journey),1)
#
# from itertools import tee
# def pairwise(iterable):
#     "s -> (s0,s1), (s1,s2), (s2, s3), ..."
#     a, b = tee(iterable)
#     next(b, None)
#     return zip(a, b)
#
# def _get_connected_neighbor(pair,grid):
#     x, y = pair
#     up = (x, y - 1)
#     down = (x, y + 1)
#     left = (x - 1, y)
#     right = (x + 1, y)
#     neighbors = [up, down, left, right]
#     return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid) and grid[neighbor[0]][neighbor[1]]==1 ]
#
#
# # make a copy of squares initializes to 0 to keep track of the member ship of the island
# def _get_island_cells(grid):
#     for i in range(len(grid)): # loop y
#         for j in range(len(grid[0])):  # loop x
#             cell_position = (j,i)
#             cell_val = grid[j][i]
#             if cell_val:
#                 yield cell_position
#
#
# def has_not_visited(position, visited):
#     x,y=position
#     return not visited[x][y]
#
#
# def dfs(cell, grid, visited):
#     visited[cell[0]][cell[1]]=1
#     for neighbor in _get_connected_neighbor(cell, grid):
#         if has_not_visited(neighbor,visited):
#             dfs(neighbor, grid, visited)
#
# def count_islands(grid):
#     """
#     Input: 2D matrix, each item is [x, y] -> row, col.
#     Output: number of islands, or 0 if found none.
#     Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
#         connected vertically or horizontally  by '1's.
#     It's also preferred to check/mark the visited islands:
#     - eg. using the helper function - mark_islands().
#     """
#
#     islands = 0
#     visited = [ [0]* len(innerlist) for innerlist in grid]
#
#     for cell in _get_island_cells(grid):
#         if has_not_visited(cell, visited):
#             dfs(cell, grid, visited)
#             islands+=1
#     return islands
#
#

#
# import base64
# from cryptography.fernet import Fernet  # type: ignore
# from cryptography.hazmat.backends import default_backend  # type: ignore
# from cryptography.hazmat.primitives import hashes  # type: ignore
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
# from os import urandom
# from typing import ByteString, Tuple, Optional
#
#
# class ClamyFernet:
#     """Fernet implementation by clamytoe
#
#     Takes a bytestring as a password and derives a Fernet
#     key from it. If a key is provided, that key will be used.
#
#     :param password: ByteString of the password to use
#     :param key: ByteString of the key to use, else defaults to None
#
#     Other class variables that you should implement that are hard set:
#
#     salt, algorithm, length, iterations, backend, and generate a base64
#     urlsafe_b64encoded key using self.clf().
#     """
#
# # steps:
#     # take a password -> derive a key -> url-64 it. -> pass to Fernat class
#
#     def __init__(self, password:ByteString= b"pybites", key:ByteString=None):
#         self.password = password
#         if not key:
#             kdf =self.kdf
#             key = base64.urlsafe_b64encode(kdf.derive(self.password))
#         self.key = key
#         self.fernat = self.clf
#
#
#     @property
#     def kdf(self):
#         """Derives the key from the password
#
#         Uses PBKDF2HMAC to generate a secure key. This is where you will
#         use the salt, algorithm, length, iterations, and backend variables.
#         """
#         kdfunc = PBKDF2HMAC(
#             algorithm=hashes.SHA256(),
#             length=32,
#             salt=urandom(16),
#             iterations=1_200_000,
#         )
#         return kdfunc
#
#
#     @property
#     def clf(self):
#         """Generates a Fernet object
#
#         Key that is derived from cryptogrophy's fermet.
#         """
#         return Fernet(self.key)
#
#     def encrypt(self, message: str) -> ByteString:
#         """Encrypts the message passed to it"""
#         return self.fernat.encrypt(message.encode('utf-8'))
#
#     def decrypt(self, token: ByteString) -> str:
#         """Decrypts the encrypted message passed to it"""
#         return self.fernat.decrypt(token).decode('utf-8')
#


# My dynamic programming solution!!!!!
# My own solution.
# Key takeaway. Work out the small example on paper.
# identify the recursive smaller subproblems.
# Build up the solution bottom-up


# IMPOSSIBLE = 'Mission impossible. No one can contribute.'
#
#
# def max_fund(village):
#     """Find a contiguous subarray with the largest sum."""
#     # Hint: while iterating, you could save the best_sum collected so far
#     # return total, starting, ending
#     if max(village)<=0:
#         return (0,0,0)
#
#     running_scores = []
#     locations = []
#     running_scores.append(village[0])
#     locations.append((0, 0))
#
#     for i in range(1, len(village)):
#         score = village[i]
#         if running_scores[i - 1] > 0:
#             running_scores.append(running_scores[i - 1] + score)
#             start, end = locations[i - 1]
#             locations.append((start, i))
#         else:
#             running_scores.append(0 + score)
#             locations.append((i, i))
#     max_score = max (running_scores)
#     max_index = running_scores.index(max_score)
#     start, end = locations[max_index]
#     return max_score, start+1, end+1

# Pybites solution
# IMPOSSIBLE = 'Mission impossible. No one can contribute.'
#
#
# def max_fund(village):
#     """Find a contiguous subarray with the largest sum."""
#     best_sum, current_sum = 0, 0
#     best_start, best_end = 0, 0
#
#     # 1. extreme case - all poor
#     if all(n <= 0 for n in village):
#         print(IMPOSSIBLE)
#         return (0, 0, 0)
#
#     # 2. mission is possible - start the trip now
#     for current_end, x in enumerate(village):
#         if current_sum <= 0:
#             current_start = current_end
#             current_sum = x
#         else:
#             current_sum += x
#         if current_sum > best_sum:
#             best_sum = current_sum
#             best_start = current_start
#             best_end = current_end
#     # index offset:  start + 1, end + 1
#     return best_sum, best_start + 1, best_end + 1

# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.

#
# def _get_connected_neighbor(island_cells, x, y):
#     up = (x, y - 1)
#     down = (x, y + 1)
#     left = (x - 1, y)
#     right = (x + 1, y)
#     neighbors = [up, down, left, right]
#     return len([neighbor for neighbor in neighbors if neighbor in island_cells])
#
#
# def island_size(map_):
#     island_cells = [(column, row) for row in range(len(map_)) for column in range(len(map_[0])) if
#                     map_[row][column] == 1]
#     return sum([4 - _get_connected_neighbor(island_cells, cell[0], cell[1]) for cell in island_cells])

# Pybites solution
# def get_others(map_, r, c):
#     """Go through the map and check the size of the island
#        (= summing up all the 1s that are part of the island)
#
#        Input - the map, row, column position
#        Output - return the total number
#     """
#     num = 0
#
#     if r > 0:
#         num += map_[r-1][c] == 1
#
#     if r < len(map_) - 1:
#         num += map_[r+1][c] == 1
#
#     if c > 0:
#         num += map_[r][c-1] == 1
#
#     if c < len(map_[0]) - 1:
#         num += map_[r][c+1] == 1
#
#     return num
#
#
# def island_size(map_):
#     """Hint: use the get_others helper
#
#     Input: the map
#     Output: the perimeter of the island
#     """
#     perimeter = 0
#
#     for r, row in enumerate(map_):
#         for c, val in enumerate(row):
#             if val == 1:
#                 perimeter += 4 - get_others(map_, r, c)
#     return perimeter
#
# import inspect
# import string
#
# def get_classes(mod):
#
#     """Return a list of all classes in module 'mod'"""
#     print(f"pause")
#     return [name for name, obj in inspect.getmembers(mod) if
#      inspect.isclass(obj) and name[0] in string.ascii_uppercase ]
#
# from typing import List
# def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
#     """
#     Input:  Two sentences - each is a  list of words in case insensitive ways.
#     Output: those common words appearing in both sentences. Capital and lowercase
#             words are treated as the same word.
#
#             If there are duplicate words in the results, just choose one word.
#             Returned words should be sorted by word's length.
#     """
#
#
#     return sorted(list(set([word.lower() for word in sentence1]) & set([word.lower() for word in sentence2])),key=lambda x: len(x))
#
# def dec_to_base(number, base):
#     """
#     Input: number is the number to be converted
#            base is the new base  (eg. 2, 6, or 8)
#     Output: the converted number in the new base without the prefix (eg. '0b')
#     """
#     if number < base:
#         return number
#     quotient = number // base
#     remainder = number % base
#     return  10 * dec_to_base(quotient,base) + remainder
#
#
# from collections import Counter
#
# import bs4
# import requests
#
# COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
#                   "common-domains.html")
# TARGET_DIV = {"class": "middle_info_noborder"}
#
# def get_common_domains(url=COMMON_DOMAINS):
#     """Scrape the url return the 100 most common domain names"""
#
#     #url = COMMON_DOMAINS
#     html_content = requests.get(url).text
#     soup = bs4.BeautifulSoup(html_content, 'html.parser')
#     domain_tag = soup.find('div', attrs = TARGET_DIV)
#     table_tags= domain_tag.find('table')
#
#     result = []
#     for row in table_tags.find_all("tr"):
#         # Get all cells in the row
#         cells = row.find_all(["td"])
#         # Extract text from each cell
#         cell_data = [cell.get_text(strip=True) for cell in cells][2]
#         result.append(cell_data)
#     return result
#
# def get_most_common_domains(emails, common_domains=None):
#     """Given a list of emails return the most common domain names,
#        ignoring the list (or set) of common_domains"""
#     if common_domains is None:
#         common_domains = get_common_domains()
#
#     # your code
#
#     filtered_email = [email.split('@')[1] for email in emails if email.split('@')[1] not in common_domains]
#     c1 = Counter(filtered_email)
#     return c1.most_common()
#
# from collections import Counter
#
# import bs4
# import requests
#
# COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
#                   "common-domains.html")
# TARGET_DIV = {"class": "middle_info_noborder"}
#
#
# def get_common_domains(url=COMMON_DOMAINS):
#     """Scrape the url return the 100 most common domain names"""
#     resp = requests.get(url)
#     soup = bs4.BeautifulSoup(resp.text, "html.parser")
#     trs = soup.find("div", TARGET_DIV).find_all('tr')
#     return [tr.find_all("td")[2].text for tr in trs]
#
#
# def get_most_common_domains(emails, common_domains=None):
#     """Given a list of emails return the most common domain names,
#        ignoring the list (or set) of common_domains"""
#     if common_domains is None:
#         common_domains = get_common_domains()
#
#     # for multiple lookups a set is faster
#     common_domains = set(common_domains)
#
#     domains = Counter()
#     for email in emails:
#         name, domain = email.split('@')
#         domain = domain.lower()
#         if domain in common_domains:
#             continue
#         domains[domain] += 1
#
#     return domains.most_common()
#
# from typing import List
# import math
#
# def pascal(N: int) -> List[int]:
#     """
#     Return the Nth row of Pascal triangle
#     """
#     # you code ...
#     return [math.comb(N-1,i)  for i in range(N)]


# 2nd solution. Using recursion
# from typing import List
# import math
# def p_helper(row,col):
#     print(f"row:{row},col:{col}")
#     if col==0 or col==row :
#         return 1
#     return p_helper(row-1,col-1) + p_helper(row-1,col)
# def pascal(N: int) -> List[int]:
#     """
#     Return the Nth row of Pascal triangle
#     """
#     # you code ...
#     return [p_helper(N-1,i) for i in range(N)]


# 3rd solution. Using recursion with memoization
# from typing import List
# import math
# cache = {}
# def p_helper(row,col):
#     print(f"row:{row},col:{col}")
#     if cache.get((row,col)):
#         print(f"Retrive from cache:({row},{col}={cache[row,col]})")
#         return cache.get((row,col))
#
#     if col==0 or col==row :
#         cache[row, col] = 1
#         return 1
#
#     result = p_helper(row-1,col-1) + p_helper(row-1,col)
#     cache[row,col]=result
#     return result
#
#
# def pascal(N: int) -> List[int]:
#     """
#     Return the Nth row of Pascal triangle
#     """
#     # you code ...
#     return [p_helper(N-1,i) for i in range(N)]
#
# import string
#
# def parse_ip(data):
#     if len(data)>=4 and data[0]=='ip' and data[2]=='mask' and data[1][0] and data[3]:
#         ip = data[1][0].replace('"','')
#         mask = data[3][0]
#         if ip and not any([True for s in string.ascii_lowercase if s in ip]) and mask:
#             return ip,mask
#     return None
#
# def parse_list(data_list, output):
#     parsed_tuple = parse_ip(data_list)
#     if parsed_tuple and parsed_tuple not in output:
#         output.append(parsed_tuple)
#
#     for data in data_list:
#         if type(data)==list:
#             parsed_tuple = parse_ip(data)
#             if parsed_tuple and parsed_tuple not in output:
#                 output.append(parsed_tuple)
#             parse_list(data, output)

#
#
# def extract_ipv4(data):
#     """
#     Given a nested list of data return a list of IPv4 address information that can be extracted
#     """
#     output = []
#     parse_list(data, output)
#     return output

# pybites solution.
# import re
#
# def extract_ipv4(data):
#     """
#     Given a nested list of data return a list of IPv4 address information that can be extracted
#     """
#     return re.findall(r"'ip', \['\"(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\"'\], 'mask', \['(?P<mask>\d{1,2})'\]", str(data))

# My solution
# from typing import Dict
#
# def decompress(string: str, table: Dict[str, str]) -> str:
#     if not string or not table:
#         return string
#
#     while True:
#         string_copy = str(string)
#         for key in table.keys():
#             string = string.replace(key,table[key])
#         if string==string_copy:
#             break
#     return string

#
# from typing import Dict
# def decompress(string: str, table: Dict[str, str]) -> str:
#     """
#     Characters in the input string are converted by looking them up in the input table (recursively).
#     """
#
#     new_string = ''
#     for char in string:
#         new_char = table.get(char)
#         if new_char:
#             new_string += decompress(new_char, table)
#         else:
#             new_string += char
#
#     return new_string
#
# from typing import List
# from collections import defaultdict
# from itertools import accumulate
#
# def sum_indices(items: List[str]) -> int:
#     # Algorithm:
#
#     # take a list
#     # make a defaultdict of lists
#     # enumerate for each item in the list
#     #   make a dictionary entry of all the positions for that letter
#     # Calculate the cumsum for each of the list
#     # sum all the lists
#
#     char_indices_dict = defaultdict(list)
#     for i, item in enumerate(items):
#         char_indices_dict[item].append(i)
#
#     total_sum = 0
#     for index_list in char_indices_dict.values():
#         total_sum += sum(accumulate(index_list))
#     return total_sum

# from typing import List
# def sum_indices(items: List[str]) -> int:
#     """
#     Calculates the total of the indices of items in the input list, accumulating the indices for duplicate items.
#     Example: ['a', 'b', 'b', 'c'] => 0 + 1 + (1+2) + 3 = 7
#     """
#     seen, total = {}, 0
#     for idx, item in enumerate(items):
#
#         seen[item] = (new_idx := idx + seen.get(item, 0))
#         total += new_idx
#
#     return total

#
# import csv
# import re
#
# pattern = r',".*",'
# def class_rosters(input_file):
#     ''' Read the input_file and modify the data
#         according to the Bite description.
#         Return a list holding one item per student
#         per class, correctly formatted.'''
#     with open(input_file, 'r') as f_read:
#         output = []
#         for line in f_read.readlines():
#
#             if line:
#                 sid, courses = re.split(pattern,line)
#                 course_list = courses.split(',')
#                 for course in course_list:
#                     if course:
#                         course_name = course.split(' - ')[0]
#                         if course_name.strip():
#                             output.append(f"{course_name},2020,{sid}")
#     return output
#
# pybite solution
# import csv
#
# YEAR = 2020
#
#
# def class_rosters(input_file):
#     rosters = []
#     with open(input_file) as csvfile:
#         file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for row in file_reader:
#             student_id, _, *classes = row
#             for class_ in classes:
#                 if not class_:
#                     continue
#                 class_name = class_.split(" - ")[0]
#                 rosters.append(
#                     f"{class_name},{YEAR},{student_id}")
#     return rosters

#
# from typing import List
# from dateutil import parser
#
#
# def get_srt_section_ids(text: str) -> List[int]:
#     """Parse a caption (srt) text passed in and return a
#        list of section numbers ordered descending by
#        highest speech speed
#        (= ratio of "time past:characters spoken")
#
#        e.g. this section:
#
#        1
#        00:00:00,000 --> 00:00:01,000
#        let's code
#
#        (10 chars in 1 second)
#
#        has a higher ratio then:
#
#        2
#        00:00:00,000 --> 00:00:03,000
#        code
#
#        (4 chars in 3 seconds)
#
#        You can ignore milliseconds for this exercise.
#     """
#     time_dict = {}
#     for lines in text.split('\n\n'):
#         section, times, caption = lines.strip().split('\n')
#         start_time, end_time = times.split(' --> ')
#         dt_start, dt_end = parser.parse(start_time),parser.parse(end_time)
#         time_dict[int(section)] = len(caption)/ (dt_end - dt_start).total_seconds()
#
#     return sorted(time_dict,key=lambda x:time_dict[x],reverse=True)
# from typing import List
# from itertools import zip_longest
#
#
# def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
#     return list(map(list, zip(*zip_longest(*lst_of_lst, fillvalue=fillvalue))))
#
#
# # Pybites solution
# from itertools import zip_longest
# from typing import List
#
#
# def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
#     """Fills in a jagged list by padding each sublist to the desired length"""
#     return [list(lst) for lst in
#             zip(*zip_longest(*lst_of_lst, fillvalue=fillvalue))]
# import os
# import urllib
#
# # Fetched and truncated from
# # https://www.uniprot.org/uniprot/?query=database%3A%28type%3Aembl+AE017195%29&format=fasta (Aug 01, 2020)
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/fasta_genes.fasta"
# FASTA_FILE = os.path.join(os.getenv("TMP", "/tmp"), "fasta_genes.fasta")
# if not os.path.isfile(FASTA_FILE):
#     urllib.request.urlretrieve(URL, FASTA_FILE)
#
# def fasta_to_2line_fasta(fasta_file: str, fasta_2line_file: str) -> int:
#     """
#     :param fasta_file: Filename of multi-line FASTA file
#     :param fasta_2line_file: Filename of 2-line FASTA file
#     :return: Number of records
#     """
# #
#     with open(fasta_file,'r') as f_read, open(fasta_2line_file,'w') as f_write:
#         output = []
#         cum_line = ''
#         count=0
#         in_seq=False
#         for line in f_read:
#             if line.startswith('>'):
#                 in_seq=True
#                 if cum_line:
#                     f_write.write(cum_line+'\n')
#                     count+=1
#                     cum_line=''
#                     f_write.write(line)
#                     continue
#
#                 if in_seq:
#                     f_write.write(line.strip()+'\n')
#                     count += 1
#                     continue
#             if in_seq:
#                 cum_line+=line.strip()
#         if in_seq:
#             f_write.write(cum_line+'\n')
#         return count


#
# # Pybites Solution without using biopython
# def fasta_to_2line_fasta_2(fasta_file: str, fasta_2line_file: str) -> int:
#     """
#     :param fasta_file: Filename of multi-line FASTA file
#     :param fasta_2line_file: Filename of 2-line FASTA file
#     :return: Number of records
#     """
#     with open(fasta_file, "r") as f_in, open(fasta_2line_file, "w") as f_out:
#         num_sequences = 0
#         for line in f_in.readlines():
#             if line[0] != ">":
#                 if num_sequences > 0:
#                     f_out.write(line.strip())
#             else:
#                 if num_sequences > 0:
#                     f_out.write("\n")
#                 f_out.write(line)
#                 num_sequences += 1
#     return num_sequences
#

#
# if __name__ == "__main__":
#     fasta_to_2line_fasta(FASTA_FILE, f"{FASTA_FILE}_converted.fasta")
#
# import string
# def convert(number: int, base: int = 2) -> str:
#     """Converts an integer into any base between 2 and 36 inclusive
#
#     Args:
#         number (int): Integer to convert
#         base (int, optional): The base to convert the integer to. Defaults to 2.
#
#     Raises:
#         Exception (ValueError): If base is less than 2 or greater than 36
#         TypeError: If number is not an integer
#
#     Returns:
#         str: The returned value as a string
#     """
#     if type(base)!=int or not 1<base<36:
#         raise ValueError
#
#     # Make translation tables:
#     trans_table = {i:str(i) for i in range(10)}
#     trans_table.update({i:val for i, val in enumerate(string.ascii_uppercase, start=10)})
#
#     output=''
#
#     while number>=base:
#         next_round_number=number//base
#         current_digit_number=number%base
#         output=f"{trans_table[current_digit_number]}{output}"
#         number = next_round_number
#     return f"{trans_table[number]}{output}"
#
# l1 = [i for i in range(10)]
# l2 = [i for i in range(10,20)]
# dict(zip(l1,l2))
#
# # Pybite solution.
# from string import ascii_uppercase, digits
#
# number_to_numberletter = dict(zip(range(37), digits + ascii_uppercase))
# def convert(number: int, base: int = 2) -> str:
#     """Converts an integer into any base between 2 and 36 inclusive
#
#     Args:
#         number (int): Integer to convert
#         base (int, optional): The base to convert the integer to. Defaults to 2.
#
#     Raises:
#         Exception (ValueError): If base is less than 2 or greater than 36
#
#     Returns:
#         str: The returned value as a string
#     """
#     if base not in range(2,37):
#         raise ValueError(f'base {base} not supported')
#
#     result = ''
#
#     quotient = number
#
#     while quotient >= base:
#         quotient, remainder = divmod(quotient, base)
#         result = number_to_numberletter[remainder] + result
#
#     return number_to_numberletter[quotient] + result
#
# import os
# from datetime import date, timedelta
# from pathlib import Path
# from typing import Dict, List
# from urllib.request import urlretrieve
# import json
# from collections import OrderedDict
# from dateutil import parser
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
# TMP = Path(os.getenv("TMP", "/tmp"))
# RATES_FILE = TMP / "exchangerates.json"
#
# if not RATES_FILE.exists():
#     urlretrieve(URL, RATES_FILE)
#
#
# def get_all_days(start_date: date, end_date: date) -> List[date]:
#     return [start_date + timedelta(days=i) for i in range((end_date-start_date).days + 1)]
#
#
#
# # Need to fix matching dict
# def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
#     all_days_list = get_all_days(start,end)
#     match_days = []
#     sorted_dates = sorted([parser.parse(key).date() for key in daily_rates.keys()])
#     for i, day in enumerate(sorted_dates):
#         if day < start:
#             continue
#         break
#     latest_date = sorted_dates[i-1]
#     for day in all_days_list:
#         if day.strftime('%Y-%m-%d') in daily_rates:
#             match_days.append(day)
#             latest_date = day
#         else:
#             match_days.append(latest_date)
#     return dict(zip(all_days_list,match_days))
#
#
# def exchange_rates(
#     start_date: str = "2020-01-01", end_date: str = "2020-09-01"
# ) -> Dict[date, dict]:
#     start = parser.parse(start_date).date()
#     end = parser.parse(end_date).date()
#     if start < date(2019, 1, 2) or end > date(2020, 9, 1):
#         raise ValueError("Invalid date range")
#     with open(RATES_FILE, 'r') as f_read:
#         dates_json = json.load(f_read)
#     daily_rates = dates_json['rates']
#
#     matching_dict = match_daily_rates(start,end, daily_rates )
#     result = OrderedDict()
#     for key, val in matching_dict.items():
#         result[key] = {"Base Date":val,
#                        "USD":daily_rates[val.strftime('%Y-%m-%d')]['USD'],
#                        "GBP": daily_rates[val.strftime('%Y-%m-%d')]['GBP'],
#                        }
#     return result
#
# '2019-01-02'in daily_rates
#
# daily_rates = dates_json['rates']
#
#
# start = date(2020, 1, 15)
# end = date(2020, 1, 20)
# with open(RATES_FILE, 'r') as f_read:
#     dates_json = json.load(f_read)
#
# import pprint
# pprint.pprint(dates_json)
#     pass
#
# daily_rates = dates_json['rates']
#
#
# start = date(2020, 1, 15)
# end = date(2020, 1, 20)
#
# import json
# import os
# from datetime import date, timedelta
# from pathlib import Path
# from typing import Dict, List
# from urllib.request import urlopen, urlretrieve
#
# URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
# TMP = Path(os.getenv("TMP", "/tmp"))
# RATES_FILE = TMP / "exchangerates.json"
#
# if not RATES_FILE.exists():
#     urlretrieve(URL, RATES_FILE)
#
#
# def get_all_days(start_date: date, end_date: date) -> List[date]:
#     delta = end_date - start_date
#     return sorted(start_date + timedelta(days=n) for n in range(delta.days + 1))
#
#
# def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
#
#     all_days = get_all_days(start, end)
#     known_days = [date.fromisoformat(day) for day in daily_rates.keys()]
#     unknown_days = sorted(set(all_days) - set(known_days))
#
#     matching = {}
#     for unknown_day in unknown_days:
#         previous_days = [day for day in known_days if day < unknown_day]
#
#         if not previous_days:
#             continue
#
#         closest_previous = min(previous_days, key=lambda x: abs(unknown_day - x))
#         matching[unknown_day] = closest_previous
#     return matching
#
#
# def exchange_rates(
#     start_date: str = "2020-01-01", end_date: str = "2020-09-01"
# ) -> Dict[date, dict]:
#
#     data = json.loads(RATES_FILE.read_text())
#     start, end = date.fromisoformat(start_date), date.fromisoformat(end_date)
#
#     data_start = date.fromisoformat(data["start_at"])
#     data_end = date.fromisoformat(data["end_at"])
#     if start < data_start or end > data_end:
#         raise ValueError("Start or end date not in data range")
#
#     daily_rates = data["rates"]
#     matching = match_daily_rates(start, end, daily_rates)
#
#     complete_rates = {}
#     for day in get_all_days(start, end):
#
#         day_key = day.strftime("%Y-%m-%d")
#         try:
#             complete_rates[day] = daily_rates[day_key]
#             complete_rates[day]["Base Date"] = day
#         except KeyError:
#             matching_day = matching.get(day, None)
#             if not matching_day:
#                 continue
#
#             matching_day_key = matching_day.strftime("%Y-%m-%d")
#             complete_rates[day] = daily_rates[matching_day_key]
#             complete_rates[day]["Base Date"] = matching_day
#
#     return complete_rates
#
# import os
# from pathlib import Path
# from urllib.request import urlretrieve
# import json
# import re
#
# filename = "my_code.json"
# url = "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
# tmp = Path(os.getenv("TMP", "/tmp"))
# json_input_file = tmp / filename
#
# if not json_input_file.exists():
#     urlretrieve(url.format(filename=filename), json_input_file)
#
#
# def get_json_data():
#     with open(json_input_file) as file_in:
#         return json.load(file_in)
#
#
# json_data = get_json_data()
#
#
# def get_passing_code(json_data=json_data):
#     """Get all passing code and write the code for each bite to individual files.
#        Output file names should be the bite name and number with a .py extension,
#        but not including the description.  For example, if the bite name is
#        'Bite 124. Marvel data analysis' the output file name should be Bite124.py.
#        Remove any/all spaces from the file name.
#        Write to /tmp (tmp variable).
#     """
#
#     bite_list=json_data['bites']
#     for bite in bite_list:
#         raw_name = bite['bite']
#         pattern = r'Bite \d+'
#         re.search(pattern,raw_name).group()
#         file_name = f"{re.search(pattern,raw_name).group()}.py".replace(" ",'')
#         with open(tmp / file_name,'w') as f_write:
#             f_write.write(bite.get('passing_code'))

#
# from typing import Tuple
# from collections import Counter
#
# def max_letter_word(text: str) -> Tuple[str, str, int]:
#     """
#     Find the word in text with the most repeated letters. If more than one word
#     has the highest number of repeated letters choose the first one. Return a
#     tuple of the word, the (first) repeated letter and the count of that letter
#     in the word.
#     >>> max_letter_word('I have just returned from a visit...')
#     ('returned', 'r', 2)
#     >>> max_letter_word('$5000 !!')
#     ('', '', 0)
#     """
#     if type(text) != str:
#         raise ValueError
#     # filter on the word key level
#     filter_chars = '0123456789!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\n'
#     for char in text:
#         if char in filter_chars:
#             text = text.replace(char,'')
#             continue
#         if ord(char)>=128515: # remove emoji
#             text = text.replace(char, '')
#             continue
#         if 171<=ord(char)<=191:
#             text = text.replace(char, '')
#             continue
#     word_list = text.split()
#     # Break out each word and go through the letters
#     word_dict = {}
#     letter_filter = '-'
#     for word in word_list:
#         keeper = []
#         no_trail_word = word.strip("'")
#         for letter in no_trail_word.casefold():
#             # letter filter step
#             if letter in letter_filter:
#                 continue
#             keeper.append(letter)
#         if Counter(keeper).most_common():
#             word_dict[no_trail_word]=Counter(keeper).most_common()[0]
#     if not word_dict:
#         return '', '', 0
#     most_common_word=list(sorted(word_dict.items(),key=lambda x: x[1][1], reverse=True))[0]
#     return most_common_word[0],most_common_word[1][0],most_common_word[1][1]
#
# # Pybite solution
# from typing import Tuple
# from collections import Counter
# import re
#
# def trim(word: str) -> str:
#     """
#     Return the string without surrounding punctuation, symbols or digits
#     >>> trim("¿5000?  ")
#     ''
#     >>> trim("")
#     ''
#     >>> trim("Zig-zag!")
#     'Zig-zag'
#     """
#     return re.match(r'[\W\d_]*(.*?)[\W\d_]*$', word).group(1)
#
#
# def match_string(word: str) -> str:
#     """
#     Return the cleaned up version of word:
#       - Remove all non-letter characters
#       - Casefold the characters for comparison
#     >>> match_string("They're")
#     'theyre'
#     """
#     return ''.join(ch.casefold() for ch in word if ch.isalpha())
#
#
# def max_letter_word(text: str) -> Tuple[str, str, int]:
#     """
#     Find the word in text with the most repeated letters. If more than one word
#     has the highest number of repeated letters choose the first one. Return a
#     tuple of the word, the (first) repeated letter and the count of that letter
#     in the word.
#     >>> max_letter_word('I have just returned from a visit...')
#     ('returned', 'r', 2)
#     >>> max_letter_word('$5000 !!')
#     ('', '', 0)
#     """
#     try:
#         cleaned_words = [trim(word) for word in text.split()]
#     except AttributeError:
#         raise ValueError(
#             f"expected text to be str, got {type(text)}") from None
#     # Build a list of (word, max_letter, max_count) tuples,
#     counters = []
#     for word in cleaned_words:
#         if not word:
#             continue
#         letter, count = Counter(match_string(word)).most_common(1)[0]
#         counters.append((word, letter, count))
#     if not counters:
#         return ('', '', 0)
#     return max(counters, key=lambda item: item[2])

#
# from typing import List
#
#
# def split_once(text: str, separators: str = None) -> List[str]:
#     if not text:
#         return ['']
#     if not separators:
#         separators='\r\n\t\v\f '
#     return_list = []
#     begin_index = 0
#     for i, letter in enumerate(text):
#         if not separators:
#             return_list.append(text[begin_index:])
#             begin_index=len(text)
#             break
#         if letter in separators:
#             substring = text[begin_index:i]
#             return_list.append(substring)
#             begin_index = i+1
#             separators = separators.replace(letter,'')
#     if begin_index != len(text):
#         return_list.append(text[begin_index:])
#
#     return return_list

# idea:
"""
create a list of separatort
enumerate through the text by letter
    if the letter is in the list,
        split out the string, and remove the separator from the list


"""


# from string import whitespace
# from typing import List
#
# def split_once(text: str, separators: str = None) -> List[str]:
#     result, buffer = [], []
#     separators = set(separators or whitespace)
#
#     for character in text:
#         try:
#             separators.remove(character)
#         except KeyError:
#             buffer.append(character)
#         else:
#             result.append(''.join(buffer))
#             buffer.clear()
#
#     result.append(''.join(buffer))
#     return result
#
# from Bio.Seq import Seq
#
#
# def translate_cds(cds: str, translation_table: str) -> str:
#     """
#     :param cds: str: DNA coding sequence (CDS)
#     :param translation_table: str: translation table as defined in Bio.Seq.Seq.CodonTable.ambiguous_generic_by_name
#     :return: str: Protein sequence
#     """
#     cds = cds.upper()
#     for char in cds:
#         if char not in 'ATCGR':
#             cds =cds.replace(char,'')
#
#     return str(Seq(cds).translate(table=translation_table, cds=True))


#
# import sqlite3
# from enum import Enum
# from typing import Any, Dict, List, Optional, Tuple, Union
#
#
# class SQLiteType(Enum):
#     """Enum matching SQLite data types to corresponding Python types.
#
#     Supported SQLite types:
#         https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types.
#
#     This Enum is uses in the definition of a table schema to define
#         the allowed data type of a column.
#
#     Example: SQLiteType.INTEGER is the ENUM,
#         SQLiteType.INTEGER.name is "INTEGER",
#         SQLiteType.INTEGER.value is int.
#     """
#
#     NULL = None
#     INTEGER = int
#     REAL = float
#     TEXT = str
#     BLOB = bytes
#
#
# class SchemaError(Exception):
#     """Base Schema error class if a table schema is not respected."""
#
#     pass
#
#
# class DB:
#     """SQLite Database class.
#
#     Supports all major CRUD operations.
#     This DB operates in-memory only by default.
#
#     Attributes:
#         location (str): The location of the database.
#             Either a .db file or the special :memory: value for an
#             in-memory database connection.
#         connection (sqlite3.Connection): Connection object used to interact with
#             the SQLite database.
#         cursor (sqlite3.Cursor): Cursor object used to send SQL statements
#             to a SQLite database.
#         table_schemas (dict): The table schemas of the database.
#             The key is the table name and the value is a list of pairs of
#             column name and column type.
#     """
#
#     def __init__(self, location: Optional[str] = ":memory:"):
#         raise NotImplementedError("You have to implement this method first.")
#
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.location)
#         self.cursor = self.connection.cursor()
#
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.connection.close()
#
#     def create(
#             self, table: str, schema: List[Tuple[str, SQLiteType]], primary_key: str
#     ):
#         """Creates a new table.
#
#         Makes use of the SQLiteType enum class.
#         Updates the table_schemas attribute.
#
#         You can declare any column of the schema to serve as the primary key by adding
#             'primary key' after the column name in the SQL statement.
#
#         If the primary key is not part of the schema,
#             a SchemaError should be raised with the message:
#             "The provided primary key must be part of the schema."
#
#         Args:
#             table (str): The table's name.
#             schema (list): A list of columns and their SQLite data types.
#                 Example: [("make", SQLiteType.TEXT), ("year", SQLiteType.INTEGER)].
#             primary_key (str): The primary key column of the provided schema.
#
#         Raises:
#             SchemaError: If the given primary key is not part of the schema.
#         """
#         raise NotImplementedError("You have to implement this method first.")
#
#     def delete(self, table: str, target: Tuple[str, Any]):
#         """Deletes rows from the table.
#
#         Args:
#             table (str): The table's name.
#             target (tuple): What to delete from the table. The tuple consists
#                 of the column name and the actual value. For example, if you
#                 wanted to remove the row(s) with the year 1999, you would pass it
#                 ("year", 1999). Only supports "=" operator in this bite.
#         """
#         raise NotImplementedError("You have to implement this method first.")
#
#     def insert(self, table: str, values: List[Tuple]):
#         """Inserts one or multiple new records into the database.
#
#         Before inserting a value, you should make sure
#             that the schema for the table is respected.
#
#         If there are more or less values than columns,
#             a SchemaError should be raised with the message:
#             "Table <table-name> expects items with <table-columns-count> values."
#
#         If the type of a value does not respect the type of the column,
#             a SchemaError should be raised with the message:
#             "Column <column-name> expects values of type <column-type>."
#
#         To add several values with a single command, you might want to look into
#             [executemany](https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany)
#
#         Args:
#             table (str): The table's name.
#             values (list): A list of values to insert.
#                 Values must respect the table schema.
#                 The tuple consists of the values for each column in the table.
#                 Example: [("VW", 2001), ("Tesla", 2020)]
#
#         Raises:
#             SchemaError: If a value does not respect the table schema or
#                 if there are more values than columns for the given table.
#         """
#         raise NotImplementedError("You have to implement this method first.")
#
#     def select(
#             self,
#             table: str,
#             columns: Optional[List[str]] = None,
#             target: Optional[Tuple[str, Optional[str], Any]] = None,
#     ) -> List[Tuple]:
#         """Selects records from the database.
#
#         If there are no columns given, select all available columns as default.
#
#         If a target is given, but no operator (length of target < 3), assume equality check.
#
#         Args:
#             table (str): The table's name.
#             columns (list, optional): List of the column names that you want to retrieve.
#                 Defaults to None.
#             target (tuple, optional): If you want to narrow down the records returned,
#                 you can specify the column name, the operator and a value to look for.
#                 Defaults to None. Example: ("year", 1999) <-> ("year", "=", 1999).
#
#         Returns:
#             list: The output returned from the sql command
#         """
#         raise NotImplementedError("You have to implement this method first.")
#
#     def update(self, table: str, new_value: Tuple[str, Any], target: Tuple[str, Any]):
#         """Update a record in the database.
#
#         Args:
#             table (str): The table's name.
#             new_value (tuple): The new value that you want to enter. For example,
#                 if you wanted to change "year" to 2001 you would pass it ("year", 2001).
#             target (tuple): The row/record to modify. Example ("year", 1991)
#         """
#         raise NotImplementedError("You have to implement this method first.")
#
#     @property
#     def num_transactions(self) -> int:
#         """The total number of changes since the database connection was opened.
#
#         Returns:
#             int: Returns the total number of database rows that have been modified.
#         """
#         raise NotImplementedError("You have to implement this method first.")
# import copy
#
#
# items = [{'id': 1, 'name': 'laptop', 'value': 1000},
#          {'id': 2, 'name': 'chair', 'value': 300},
#          {'id': 3, 'name': 'book', 'value': 20}]
# b = copy.deepcopy(items)
# # a = items[:]
#
# def duplicate_items(items):
#     return copy.deepcopy(items)
#
# import xml.etree.ElementTree as ET
#
# # from OMDB
# xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
# <root response="True">
#   <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
#   <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
#   <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
#   <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
#   <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
# </root>'''  # noqa E501
# #
# #
#
#
# def get_tree():
#     """You probably want to use ET.fromstring"""
#     return ET.fromstring(xmlstring)
#
#
#
#
# def get_movies():
#     """Call get_tree and retrieve all movie titles, return a list or generator"""
#     movies = []
#     root = ET.fromstring(xmlstring)
#     for child in root:
#         movies.append(child.attrib['title'])
#     return movies
#
#
#
# def get_movie_longest_runtime():
#     """Call get_tree again and return the movie title for the movie with the longest
#        runtime in minutes, for latter consider adding a _get_runtime helper"""
#     runtimes = {}
#     root = ET.fromstring(xmlstring)
#     for runtime in root:
#         runtimes[runtime.attrib['title']] = int(runtime.attrib['runtime'].split()[0])
#     max_key = max(runtimes, key=runtimes.get)
#     return max_key
#     # runtimes = [int(runtime.attrib['runtime'].split()[0]) for runtime in root ]
#
#
# #
# # my_dict = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}
# #
# # my_dict.items()
# # max_item = max(my_dict.items(), key=lambda item: item[1])
#

#
# from collections import deque
#
# def my_queue(n=5):
#
#
#
# if __name__ == '__main__':
#     mq = my_queue()
#     for i in range(10):
#         mq.append(i)
#         print((i, list(mq)))
#
#     """Queue size does not go beyond n int, this outputs:
#     (0, [0])
#     (1, [0, 1])
#     (2, [0, 1, 2])
#     (3, [0, 1, 2, 3])
#     (4, [0, 1, 2, 3, 4])
#     (5, [1, 2, 3, 4, 5])
#     (6, [2, 3, 4, 5, 6])
#     (7, [3, 4, 5, 6, 7])
#     (8, [4, 5, 6, 7, 8])
#     (9, [5, 6, 7, 8, 9])
#     """
#
# import sqlite3
# from enum import Enum
# from typing import Any, Dict, List, Optional, Tuple, Union
#
#
# class SQLiteType(Enum):
#     """Enum matching SQLite data types to corresponding Python types.
#
#     Supported SQLite types:
#         https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types.
#
#     This Enum is uses in the definition of a table schema to define
#         the allowed data type of a column.
#
#     Example: SQLiteType.INTEGER is the ENUM,
#         SQLiteType.INTEGER.name is "INTEGER",
#         SQLiteType.INTEGER.value is int.
#     """
#
#     NULL = None
#     INTEGER = int
#     REAL = float
#     TEXT = str
#     BLOB = bytes
#
#
# class SchemaError(Exception):
#     """Base Schema error class if a table schema is not respected."""
#
#     pass
#
#
# class DB:
#     """SQLite Database class.
#
#     Supports all major CRUD operations.
#     This DB operates in-memory only by default.
#
#     Attributes:
#         location (str): The location of the database.
#             Either a .db file or the special :memory: value for an
#             in-memory database connection.
#         connection (sqlite3.Connection): Connection object used to interact with
#             the SQLite database.
#         cursor (sqlite3.Cursor): Cursor object used to send SQL statements
#             to a SQLite database.
#         table_schemas (dict): The table schemas of the database.
#             The key is the table name and the value is a list of pairs of
#             column name and column type.
#     """
#
#     def __init__(self, location: Optional[str] = ":memory:"):
#         self.location = location
#         self.connection = None
#         self.cursor = None
#         self.table_schemas = {}
#         self._num_transactions = 0
#
#
#
#     def __enter__(self):
#         self.connection = sqlite3.connect(self.location)
#         self.cursor = self.connection.cursor()
#
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.connection.close()
#
#     def _make_create_table_statement(self,table:str, schema: List[Tuple[str, SQLiteType]], primary_key: str):
#         body_statement = ', '.join([f"{col_name} {data_type.name} PRIMARY KEY" if primary_key==col_name else f"{col_name} {data_type.name}" for col_name, data_type in schema])
#
#         full_statement = f"""
#             CREATE TABLE IF NOT EXISTS {table} (
#                  {body_statement}
#                )
#         """
#         print(full_statement)
#         return full_statement
#
#
#     def _make_insert_table_statement(self,table:str, schema: List[Tuple[str, SQLiteType]], primary_key: str):
#
#         body_statement = ', '.join([f"{col_name} {data_type.name}" for col_name, data_type in schema])
#
#         full_statement = f"""
#             CREATE TABLE IF NOT EXISTS {table} (
#                  {body_statement}
#                )
#         """
#         print(full_statement)
#         return full_statement
#
#     def _execute_sql_commit(self,statement):
#         print(statement)
#         self.cursor.execute(statement)
#         self.connection.commit()
#
#     def create(
#             self, table: str, schema: List[Tuple[str, SQLiteType]], primary_key: str
#     ):
#         """Creates a new table.
#
#         Makes use of the SQLiteType enum class.
#         Updates the table_schemas attribute.
#
#         You can declare any column of the schema to serve as the primary key by adding
#             'primary key' after the column name in the SQL statement.
#
#         If the primary key is not part of the schema,
#             a SchemaError should be raised with the message:
#             "The provided primary key must be part of the schema."
#
#         Args:
#             table (str): The table's name.
#             schema (list): A list of columns and their SQLite data types.
#                 Example: [("make", SQLiteType.TEXT), ("year", SQLiteType.INTEGER)].
#             primary_key (str): The primary key column of the provided schema.
#
#         Raises:
#             SchemaError: If the given primary key is not part of the schema.
#         """
#         # Check if primary key is in the schema
#         if primary_key not in [column_name for column_name, data_type in schema]:
#             raise SchemaError("The provided primary key must be part of the schema.")
#
#         # Check if the table name already exists in the schema
#         if table in self.table_schemas:
#             raise sqlite3.OperationalError(f"table {table} already exists")
#
#         # Add schema to the dict
#         self.table_schemas[table] = schema
#
#         # Creates the actual SQLite Table
#         statement =self._make_create_table_statement(table, schema, primary_key)
#         self._execute_sql_commit(statement)
#
#     def delete(self, table: str, target: Tuple[str, Any]):
#         """Deletes rows from the table.
#
#         Args:
#             table (str): The table's name.
#             target (tuple): What to delete from the table. The tuple consists
#                 of the column name and the actual value. For example, if you
#                 wanted to remove the row(s) with the year 1999, you would pass it
#                 ("year", 1999). Only supports "=" operator in this bite.
#         """
#
#         where_clause = self._make_where_clause(target)
#         print(f"Where clause: {where_clause}")
#         delete_statement = f"Delete from {table} {where_clause}"
#         print(delete_statement)
#         self.cursor.execute(delete_statement)
#         return self.cursor.fetchall()
#
#
#     def insert(self, table: str, values: List[Tuple]):
#         """Inserts one or multiple new records into the database.
#
#         Before inserting a value, you should make sure
#             that the schema for the table is respected.
#
#         If there are more or less values than columns,
#             a SchemaError should be raised with the message:
#             "Table <table-name> expects items with <table-columns-count> values."
#
#         If the type of a value does not respect the type of the column,
#             a SchemaError should be raised with the message:
#             "Column <column-name> expects values of type <column-type>."
#
#         To add several values with a single command, you might want to look into
#             [executemany](https://docs.python.org/2/library/sqlite3.html#sqlite3.Cursor.executemany)
#
#         Args:
#             table (str): The table's name.
#             values (list): A list of values to insert.
#                 Values must respect the table schema.
#                 The tuple consists of the values for each column in the table.
#                 Example: [("VW", 2001), ("Tesla", 2020)]
#
#         Raises:
#             SchemaError: If a value does not respect the table schema or
#                 if there are more values than columns for the given table.
#         """
#
#         schema = self.table_schemas[table]
#         expected_arg_numbers = len(schema)
#         col_names = [col for col, data_type in schema]
#
#         if any([True for val in values if len(val) != expected_arg_numbers]):
#             raise SchemaError(f"Table {table} expects items with {expected_arg_numbers} values.")
#
#         # Check data types matches for each row
#         for row in values:
#             for (col, data_type), data in zip(schema,row):
#                 if data_type.value!=type(data):
#                     raise SchemaError(f"Column {col} expects values of type {str(data_type.value.__name__)}.")
#         question_mark_str = ', '.join(["?" for _ in col_names])
#         sql_statement = f"Insert into {table}({", ".join(col_names)})  values ({question_mark_str})"
#         self.cursor.executemany(sql_statement, values)
#         self.num_transactions += len(values)
#
#     def _make_where_clause(self, target):
#         if target is None:
#             return ''
#         if len(target)==2:
#             operator = '='
#             val = target[1]
#         else:
#             operator = target[1]
#             val = target[2]
#
#         if type(val).__name__=='str':
#             val = f"'{val}'"
#         return f" Where {target[0]} {operator} {val}"
#
#     def select(
#             self,
#             table: str,
#             columns: Optional[List[str]] = None,
#             target: Optional[Tuple[str, Optional[str], Any]] = None,
#     ) -> List[Tuple]:
#         """Selects records from the database.
#
#         If there are no columns given, select all available columns as default.
#
#         If a target is given, but no operator (length of target < 3), assume equality check.
#
#         Args:
#             table (str): The table's name.
#             columns (list, optional): List of the column names that you want to retrieve.
#                 Defaults to None.
#             target (tuple, optional): If you want to narrow down the records returned,
#                 you can specify the column name, the operator and a value to look for.
#                 Defaults to None. Example: ("year", 1999) <-> ("year", "=", 1999).
#
#         Returns:
#             list: The output returned from the sql command
#         """
#
#         col_name = ','.join([col for col in columns]) if columns else '*'
#         where_clause = self._make_where_clause(target)
#         select_statement = f"Select {col_name} from {table} {where_clause}"
#         self.cursor.execute(select_statement)
#         return self.cursor.fetchall()
#
#
#     def update(self, table: str, new_value: Tuple[str, Any], target: Tuple[str, Any]):
#         """Update a record in the database.
#
#         Args:
#             table (str): The table's name.
#             new_value (tuple): The new value that you want to enter. For example,
#                 if you wanted to change "year" to 2001 you would pass it ("year", 2001).
#             target (tuple): The row/record to modify. Example ("year", 1991)
#         """
#         result = self.select(table, columns=None, target=target)
#         self.num_transactions += len(result)
#         where_clause = self._make_where_clause(target)
#         print(f"Where clause: {where_clause}")
#         if type(new_value[1]).__name__ == 'str':
#             val = f"'{new_value[1]}'"
#         else:
#             val = new_value[1]
#         update_statement = (f"""Update {table}
#                                 Set {new_value[0]} = {val}
#                               {where_clause}""")
#         print(update_statement)
#         self.cursor.execute(update_statement)
#
#
#     @property
#     def num_transactions(self) -> int:
#         """The total number of changes since the database connection was opened.
#
#         Returns:
#             int: Returns the total number of database rows that have been modified.
#         """
#         return self._num_transactions
#
#     @num_transactions.setter
#     def num_transactions(self, value):
#         """The total number of changes since the database connection was opened.
#
#         Returns:
#             int: Returns the total number of database rows that have been modified.
#         """
#         self._num_transactions = value
#
import math
def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    total_number_of_items = sum(d.values())
    first_index, second_index = find_index_of_mid_two_nums(total_number_of_items)
    # Isolate the middle two numbers

    # Find the value of the nth value in the list
    # sort the keys by
    first_val = find_nth_value_from_dict(d, first_index)
    second_val = find_nth_value_from_dict(d, second_index)
    median = (first_val + second_val) / 2
    return median


    # Find the mid points.
def find_index_of_mid_two_nums(total_number_of_items)-> tuple:
        mid_point = total_number_of_items/2
        if total_number_of_items%2 == 0: #even
                first_item = int(mid_point)
                second_item = first_item + 1

        else: # odd
                first_item = math.ceil(mid_point)
                second_item = first_item
        return first_item, second_item

def make_intervals(slots):
        beginning = 1
        intervals = []
        for slot in slots:
                intervals.append((beginning, beginning + slot - 1))
                beginning = beginning + slot
        return intervals


def find_nth_value_from_dict(my_dict, target) -> int | None:
    ordered_keys = sorted(my_dict.keys())
    ordered_slots = list([my_dict[i] for i in ordered_keys])

    for key, current_range in zip(ordered_keys, make_intervals(ordered_slots)):
        if current_range[1] >= target >= current_range[0]:
            return key

    return None


