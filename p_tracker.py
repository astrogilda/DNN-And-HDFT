import os
import numpy
import pipes

p_f_list100 = open("param_list100run.txt", 'r')
p_100 = p_f_list100.readlines()
p_f_list500 = open("param_list500run.txt", 'r')
p_500 = p_f_list500.readlines()
p_f_list1000 = open("param_list1000run.txt", 'r')
p_1000 = p_f_list1000.readlines()

net_num = 0
for net in p_100:
    print net_num
    os.system("python trainer_tester_dropping100.py %s %d %d %d" % (pipes.quote(net), net_num, 100, 20))
    net_num += 1


net_num = 0
for net in p_500:
    print net_num
    os.system("python trainer_tester_dropping.py %s %d %d %d" % (pipes.quote(net), net_num, 101, 40))
    net_num += 1


net_num = 0
for net in p_1000:
    print net_num
    os.system("python trainer_tester_dropping1000.py %s %d %d %d" % (pipes.quote(net), net_num, 102, 80))
    net_num += 1


p_f_list1000.close()
p_f_list500.close()
p_f_list100.close()