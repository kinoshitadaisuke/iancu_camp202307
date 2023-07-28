#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2023/07/28 11:00:58 (CST) daisuke>
#

# importing contextlib module
import contextlib

# importing sqlite3 module
import sqlite3

# database file name
file_db = 'bsc5.db'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # SQL command for querying
    sql_query = f'select hr, name, vmag, bv, sptype, parallax' \
        + f' from bsc5 where (vmag < 1.0) and (vmag > -10.0)' \
        + f' order by vmag;'
    
    # executing SQL command to query star's data to database
    cursor.execute (sql_query)

    # fetching results of query
    results = cursor.fetchall ()

    # printing results of query
    print (f'#')
    print (f'# HR, name, Vmag, B-V, SpType, parallax')
    print (f'#')
    for result in results:
        print (f'{result[0]:4d} {result[1]:10s}' \
               + f' {result[2]:+5.2f} {result[3]:+5.2f}' \
               + f' {result[4]:20s} {result[5]:5.3f}')

    # committing transaction
    conn.commit ()
