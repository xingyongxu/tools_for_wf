#coding:utf-8
import fnmatch
import os
import heapq
from xlrd import XLRDError
from xlrd import open_workbook
import pprint
import xlwt
import argparse

def pars_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='d', type=str, help='excel dir')
    parser.add_argument("-v", "--version", action="store_true", help="show version info")
    args = parser.parse_args()
    if args.version:
        print "excel v 0.0.1, all rights reserved@yongxu"
    return args

def find_second_phase(file_path):
    wb = open_workbook(file_path)
    try:
        s = wb.sheet_by_name(u'二阶段项目数据')
    except XLRDError as e:
        print e
        exit(-1)
    return s
    #for s in wb.sheets():
    #if True:
    #    if s.name == u'二阶段项目数据':
    #        print 'Sheet:',s.name
    #        values = []
    #        for row in range(s.nrows):
    #            col_value = []
    #            for col in range(s.ncols):
    #                value  = (s.cell(row,col).value)
    #                try : value = str(int(value))
    #                except : pass
    #                col_value.append(value)
    #            values.append(col_value)
    #        pprint.pprint(values)




def find_all_excels(excel_dir):
    matches = []
    for root, dirnames, filenames in os.walk(excel_dir):
        for filename in fnmatch.filter(filenames, '*.xlsx'):
            matches.append(os.path.join(root, filename))
    return matches


if __name__ == "__main__":
    args = pars_arg()
    cnt_list = []
    wb = xlwt.Workbook()
    ws = wb.add_sheet(u'二阶段')
    sr = 0
    for f in find_all_excels(args.path):
        print f
        #sheet = find_second_phase(f)
        wbr = open_workbook(f)
        sheet = None
        try:
            sheet = wbr.sheet_by_name(u'二阶段项目数据')
        except XLRDError as e:
            print e
            #exit(-1)
            continue

        numRow = sheet.nrows
        numCol = sheet.ncols

        for row in xrange(numRow):
            #  Get all the rows in the sheet (each rows is a list)
            rowList = sheet.row_values(row)
            for col in xrange(numCol):
                #  Get all the values in each list
                oneValue = rowList[col]
                #  Copy the values to target worksheet
                ws.write(sr + row, col, oneValue)
        sr += numRow
        print sr,'\t  ', numRow
        heapq.heappush(cnt_list, (numRow, f))

    wb.save('Merged_Result.xls')
    #l =  heapq.nlargest(10, cnt_list, lambda x: x[0])
    #for e in l:
    #    print e[0], ':\t', e[1]


