#!/usr/bin/env python3

import csv, os

PROJ_DIR   = os.path.abspath(os.path.dirname(__file__))
ASN_CSV    = os.path.join(PROJ_DIR, 'bad-asn-list.csv')
CSV_FIELDS = ('ASN', 'Entity')


def load_db():
    def asn_to_int(row_dict):
        row_dict['ASN'] = int(row_dict['ASN'])
        return row_dict

    def sort_by_asn(row_dict):
        return row_dict['ASN']

    with open(ASN_CSV, 'r') as fp:
        cdr = csv.DictReader(fp)
        entries = list(map(asn_to_int, cdr))
        entries.sort(key=sort_by_asn)

    return entries

def dump_db(entries):
    with open(ASN_CSV, 'w') as fp:
        cdw = csv.DictWriter(fp, CSV_FIELDS)
        cdw.writeheader()
        cdw.writerows(entries)

dump_db(load_db())