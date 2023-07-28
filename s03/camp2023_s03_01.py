#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/07/27 23:00:29 (CST) daisuke>
#

# importing sqlite3 module
import sqlite3

# importing contextlib module
import contextlib

# file name of database
file_db = 'solsys.db'

# data file name
file_data = 'solsys.data'

# connecting to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # opening data file for reading
    with open (file_data) as fh_in:
        # reading file line-by-line
        for line in fh_in:
            # if line starts with '#', then skip
            if (line[0] == '#'):
                continue
            # splitting line
            (name, mass_str, radius_str, density_str, v_esc_str, \
             rot_per_str, orb_per_str, a_str, e_str, i_str, T_str, \
             n_moons_str, ring, magnetic_field) = line.split ()
            # converting string into float or int
            mass    = float (mass_str)
            radius  = float (radius_str)
            density = float (density_str)
            v_esc   = float (v_esc_str)
            rot_per = float (rot_per_str)
            orb_per = float (orb_per_str)
            a       = float (a_str)
            e       = float (e_str)
            i       = float (i_str)
            T       = float (T_str)
            n_moons = int (n_moons_str)

            # SQL command to add data
            sql_adddata = f'insert into solsys values (' \
                + f'"{name}", {mass}, {radius}, {density}, {v_esc}, ' \
                + f'{rot_per}, {orb_per}, {a}, {e}, {i}, {T}, ' \
                + f'{n_moons}, "{ring}", "{magnetic_field}");'
    
            # executing SQL command to add data to table
            cursor.execute (sql_adddata)

    # committing transaction
    conn.commit ()
