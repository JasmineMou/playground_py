# to enable usage of ExtendedInterpolation(), run the codes under py35 environment. 
# else to run code in py27 environment, replace configparser with ConfigParser.
# usage: can be used to design a viz of learning progress so far

import configparser
import os

f = "config_test.cfg"
cfparser = configparser.ConfigParser()
cfparser.read(f)
cfparser._interpolation = configparser.ExtendedInterpolation()

if not os.path.exists(f):
	createConfig(f)

def read_config():
	s = cfparser.sections()
	print(s)
	o = cfparser.options(s[0])
	print(o)
	v = cfparser.get(s[0],o[0])
	print(v)

def update_config():
	cfparser.set("course2","priority","0")
	write_changes_to_config()

def add_config():
	cfparser.add_section("project3")
	cfparser.set("project3", "result", "1")
	write_changes_to_config()

def delete_config_section():
	cfparser.remove_section("project2")
	write_changes_to_config()

def delete_config_option():
	cfparser.remove_option("project1", "to_delete")
	write_changes_to_config()

def use_interpolation():
	cfparser.set("project3","size","0")
	cfparser.set("project3","color","black")
	cfparser.set("project3", "result", "Size is ${size}. Color is ${color}. ")
	write_changes_to_config()

	a = cfparser.get("project3","result", raw=True)
	b = cfparser.get("project3","result", raw=True, vars={"size":100, "color":"red"})
	c = cfparser.get("project3","result", raw=False)

	d = cfparser.get("project3","result", raw=False, vars={"size":100, "color":"red"})
	e = cfparser.get("project3","nonexist", fallback="This value doesn't exist")

	print(a)
	print(b)
	print(c)
	print(d)	
	print(e)
	write_changes_to_config()

def write_changes_to_config():
	with open(f, "wb") as o:
		cfparser.write(o)


read_config()
# update_config()
# delete_config_section()
# delete_config_option()
# add_config()
# use_interpolation()
