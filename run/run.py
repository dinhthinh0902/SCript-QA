import pyodbc
import pandas as pd
import os
from os import path

HOME_DIR = '/home/nminh/Jupyter/'
LOG_DIR = HOME_DIR + 'log/'
LOG_TC001_DIR = LOG_DIR + 'tc001_csv/'

import sys
sys.path.insert(0, os.path.abspath(HOME_DIR +'mapping'))
import mapping
import dic


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 2000)


#dw connection
server = 'sqldw-prod-vn-di-server.database.windows.net'
database = 'sqldw-prod-vn-di-dw'
username = 'datareader'
password = 'Hm@$aigonThink20PdgReader'
driver= '{ODBC Driver 17 for SQL Server}'
dw = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = dw.cursor()
#----------------------------------------------------

class Ccount:
  fail_ = 0
  pass_ = 0
  none_ = 0
class Ckey:
  src_key = ''
  target_key = ''
class Ctable:
  test = []
class Cstr:
  df = ''
  result = ''

flag_test_table_structure_var_length = False

## TC_001
def TC_001_verify_table_structure(table_name):
    Cstr.result = 'PASS'
    # get column name from dw
    sql = """select COLUMN_NAME 
    from INFORMATION_SCHEMA.COLUMNS 
    where TABLE_NAME = N'{}'
      and TABLE_SCHEMA = 'Dim'"""

    try:
      Cstr.df = pd.read_sql_query(sql.format(table_name[4:]), dw)
    except Exception as e:
      print(e)
      Cstr.result = 'FAIL'

    if 'Empty DataFrame' in str(Cstr.df):
      field_list_on_dw = []
    else:
      field_list_on_dw_raw = str(Cstr.df).splitlines()
      field_list_on_dw_raw = field_list_on_dw_raw[1:] #remove title COLUMN_NAME
      field_list_on_dw = []
      for item in field_list_on_dw_raw:
        if len(item.split()) > 1:
          field_list_on_dw.append(item.split()[1])

    #get column name from MappingFile
    exec('Ctable.test = mapping.' + table_name)
    field_list_on_mapping = []
    for item in Ctable.test:
      field_list_on_mapping.append(item[0])

    #check field on dw is existed on Mapping?
    if field_list_on_dw:
      for item in field_list_on_dw:
        if item not in field_list_on_mapping:
          print(item + ' -- is MISSING in MappingFile')
          Cstr.result = 'FAIL'

    #check field on Mapping is existed on dw?
    if field_list_on_mapping:
      for item in field_list_on_mapping:
        if item not in field_list_on_dw:
          print(item + '  -- is MISSING in dw')
          Cstr.result = 'FAIL'

    #Test number of file:
    print('  number of field:')
    print('  on MappingFile: ', len(field_list_on_mapping))
    print('  on data warehouse: ', len(field_list_on_dw))
    if len(field_list_on_mapping) != len(field_list_on_dw):
      Cstr.result = 'FAIL'

    # Test Length
    if flag_test_table_structure_var_length:
      sql_len = """select CHARACTER_OCTET_LENGTH
      from INFORMATION_SCHEMA.COLUMNS 
      where TABLE_NAME = N'{}'
        and TABLE_SCHEMA = 'Dim' and COLUMN_NAME = N'{}'"""
      for item in field_list_on_mapping:
        if item in field_list_on_dw:

          try:
            Cstr.df = pd.read_sql_query(sql_len.format(table_name[4:], item), dw)
          except Exception as e:
            print(e)
            Cstr.result = 'FAIL'

          field_data_len_raw = str(Cstr.df).splitlines()
          field_data_len_raw = field_data_len_raw[1:] #remove title
          field_data_len = field_data_len_raw[0]
          field_data_len = field_data_len.split()[1]
          print(field_data_len)# --> then compare with item[6] //length

    if Cstr.result == 'PASS':
      Ccount.pass_ += 1
    else:
      Ccount.fail_ += 1

    return Cstr.result

## TC_002
def TC_002_verify_initial_load_data_loaded_fully(table_name):
    print('  number of data in the table:')
    if table_name[:3] == 'DIM' or table_name[:4] == 'FACT':
      src_table = dic.src_table_of[table_name]
      if ( TC_002_count_data_loaded_of(table_name) == \
        TC_002_count_data_loaded_of(src_table)):
        Ccount.pass_ += 1
        print('  data in the table is loaded fully')
        return 'PASS'
      else:
        Ccount.fail_ += 1
        return 'FAIL'
    else:
      Ccount.none_ += 1
      return None

def TC_002_count_data_loaded_of(table_name): #return number of data
    sql = "select count(1) from {} "

    azure_table = name_on_azure(table_name)

    try:
      Cstr.df = pd.read_sql_query(sql.format(azure_table), dw)
    except Exception as e: print(e)

    num_of_data = str(Cstr.df).split()[1]

    print('  ' + table_name + ' :' + num_of_data)

    return num_of_data

## TC_003
def TC_003_verify_initial_source_key(table_name):
    exec('Ckey.src_key = mapping.' + table_name + '[1][2]') #get from second row of table
    exec('Ckey.target_key = mapping.' + table_name + '[1][0]')
    src_table = dic.src_table_of[table_name]
    azure_table = name_on_azure(table_name)

    sql_join = """select count(1) 
    from hmsg.{}  a
    join {} b
      on a.{} = b.{}"""

    # print('src_table = '+ src_table)
    # print('azure_table = '+ azure_table)
    # print('src_key = '+ Ckey.src_key)
    # print('target_key = '+ Ckey.target_key)

    sql_lelf = """select count(1)
    from hmsg.{}  a
    left join {} b
      on a.{} = b.{}
    where b.{} is null"""

    sql_right = """select count(1)
    from hmsg.{}  a
    right join {} b
      on a.{} = b.{}
    where a.{} is null"""

    try:
      Cstr.df = pd.read_sql_query(sql_join.format(src_table, azure_table, Ckey.src_key, Ckey.target_key), dw)
    except Exception as e:
      print(e)
      Ccount.fail_ += 1
      return 'FAIL'
    print('  join count: ' + str(Cstr.df).split()[1])

    try:
      Cstr.df = pd.read_sql_query(sql_lelf.format(src_table, azure_table, Ckey.src_key, Ckey.target_key, Ckey.target_key), dw)
    except Exception as e:
      print(e)
      Ccount.fail_ += 1
      return 'FAIL'
    left_join_count_null = str(Cstr.df).split()[1]
    print('  left join count null: ' + str(left_join_count_null))

    try:
      Cstr.df = pd.read_sql_query(sql_right.format(src_table, azure_table, Ckey.src_key, Ckey.target_key, Ckey.src_key), dw)
    except Exception as e:
      print(e)
      Ccount.fail_ += 1
      return 'FAIL'
    right_join_count_null = str(Cstr.df).split()[1]
    print('  right join count null: ' + str(right_join_count_null))

    if (left_join_count_null == '0' and right_join_count_null == '0'):
      Ccount.pass_ += 1
      return 'PASS'
    else:
      Ccount.fail_ += 1
      return 'FAIL'

## TC_004
def TC_004_verify_initial_data_in_each_column(table_name):
  exec('Ckey.src_key = mapping.' + table_name + '[1][2]')
  exec('Ckey.target_key = mapping.' + table_name + '[1][0]')
  exec('Ctable.test = mapping.' + table_name + '[1:]')

  src_table = dic.src_table_of[table_name]
  azure_table = name_on_azure(table_name)
  Cstr.result = 'PASS'

  sql = """select count(1)
  from hmsg.{}  a 
  join {} b 
    on a.{} = b.{} 
  where (a.{} <> b.{})"""

  for item in Ctable.test:
    if(item[3] == None and item[0] != 'Hospital_Key'): # test if TargetField does NOT has Reference Table
      try:
        Cstr.df = pd.read_sql_query(sql.format(src_table, azure_table, Ckey.src_key, Ckey.target_key, item[2], item[0]), dw)
      except Exception as e:
        print(e)
        Cstr.result = 'FAIL'
      x = lambda a : '_pass' if a == '0' else '_fail'

      print('  item[0] =' + str(item[0]) +' ; item[2] = ' + str(item[2]) + \
        '--- count='+ str(Cstr.df).split()[1] + x(str(Cstr.df).split()[1]))

      if str(Cstr.df).split()[1] != '0' : Cstr.result = 'FAIL'
    else: #do nothing
      pass

  if Cstr.result == 'PASS':
    Ccount.pass_ += 1
  else:
    Ccount.fail_ += 1

  return Cstr.result

## TC_005
def TC_005_verify_initial_foreign_key(table_name):
  exec('Ckey.src_key = mapping.' + table_name + '[1][2]')
  exec('Ckey.target_key = mapping.' + table_name + '[1][0]')
  exec('Ctable.test = mapping.' + table_name + '[1:]')
  src_table = dic.src_table_of[table_name]
  azure_table = name_on_azure(table_name)
  Cstr.result = 'PASS'

  sql = """select count(1) 
  from hmsg.{} a
  join {} b 
    on a.{} = b.{} 
  left join {} c 
    on b.{} = c.{} 
  where (a.{} <> c.{})"""

  for item in Ctable.test:
    if(item[2] != None  and  item[5] != None): # test if TargetField has Reference Table
      target_field= item[0]
      src_field   = item[2]
      ref_table   = item[3]
      foreign_key = item[4]
      map_field   = item[5]

      #Do not test Hospital_Key
      if (target_field == 'Hospital_Key'):
        pass

      try:
        Cstr.df = pd.read_sql_query(sql.format(src_table , azure_table ,\
          Ckey.src_key, Ckey.target_key, name_on_azure(ref_table), target_field, foreign_key, src_field, map_field), dw)
      except Exception as e:
        print(e)
        Cstr.result = 'FAIL'

      x = lambda a : '_pass' if a == '0' else '_fail'
      print('test field:' + str(item[0]) + x(str(Cstr.df).split()[1]))
      if str(Cstr.df).split()[1] != '0': Cstr.result = 'FAIL'
    else: #do nothing
      pass

  if Cstr.result == 'PASS':
    Ccount.pass_ += 1
  else:
    Ccount.fail_ += 1

  return Cstr.result

##TC_006
#def TC_006_verify_initial_business_rule()

## TC_007
#def TC_007_verify_daily_load_insert_flow()

## TC_008
#def TC_008_verify_daily_load_update_flow()

def name_on_azure(table_name):
    if table_name[:4] == 'DIM_':
      return table_name.replace('DIM_','Dim.',1)
    elif table_name[:5] == 'FACT_':
      return table_name.replace('FACT_','Fact.',1)
    else: #src table
      return 'hmsg.' + table_name

def read_table(table_name):
    print("=========" + table_name + "===========")
    sql = "SELECT * FROM {}"
    if table_name[:3] == 'DIM' or table_name[:4] == 'FACT':
        df = pd.read_sql_query(sql.format(table_name), dw)
    else :
        df = pd.read_sql_query(sql.format(table_name), hmsg)
    print(df)

#read_table('DM_ICD')

## LOGGING

def tc001_result_append(content):
  tc001_result = open('/home/nminh/Jupyter/log/TC_001_result','a+')
  tc001_result.write(content)
  tc001_result.close()

def log_append(content):
  test_result = open(LOG_DIR + 'test_result','a+')
  test_result.write(content.tostring())
  test_result.close()

def print_summary():
  print('=============SUMMARY============')
  print('PASS: ' + str(Ccount.pass_))
  print('FAIL: ' + str(Ccount.fail_))
  # print('not_exec: ' + str(Ccount.none_))
  print('================================')

