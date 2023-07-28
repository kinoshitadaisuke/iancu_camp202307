#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 22:42:05 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# importing contextlib module
import contextlib

# file name of database
file_db = 'solsys.db'

# SQL command to make a table
sql_maketable = f'create table solsys ' \
    + f'(name text primary key, mass real, radius real, ' \
    + f'density real, escape_velocity real, ' \
    + f'rotation_period real, orbital_period real, ' \
    + f'semimajor_axis real, eccentricity real, inclination real, ' \
    + f'mean_temperature real, moons integer, ' \
    + f'ring_system text, global_magnetic_field text);'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # executing SQL command to make a table
    cursor.execute (sql_maketable)

    # committing transaction
    conn.commit ()
