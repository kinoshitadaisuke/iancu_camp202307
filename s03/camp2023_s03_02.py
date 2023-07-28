#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 23:22:50 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# importing contextlib module
import contextlib

# file name of database
file_db = 'solsys.db'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # SQL command for querying
    sql_query = f'select name, radius, density, escape_velocity, ' \
        + f'mean_temperature, moons, ring_system from solsys ' \
        + f'where semimajor_axis > 5.0 order by radius;'
    
    # executing SQL command to query database
    cursor.execute (sql_query)

    # fetching results of query
    results = cursor.fetchall ()

    # printing results of query
    print (f'# name, radius, density, v_esc, T, moons, ring')
    for result in results:
        print (f'{result[0]:8s} {result[1]:5.0f} {result[2]:4.0f}' \
               + f' {result[3]:4.1f} {result[4]:+3.0f}' \
               + f' {result[5]:3d} {result[6]:3s}')

    # committing transaction
    conn.commit ()
