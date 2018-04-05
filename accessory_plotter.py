import os
import numpy
import matplotlib.pyplot as pl
from vc_calculator import *

archive5000 = '/home/hdft/Documents/DNN-Complete/5000-CIFAR-Run/'

SET = 'CIFAR'

plotX_depth = []
#plotY_depth = []
plotX_conv = []
#plotY_conv = []
plotX_fc = []
#plotY_fc = []
plotX_mp = []
plotX_vc = []
plotY_er = []
plotY_acc = []

for run in [archive5000]:
    for file_list in os.listdir(run):
        data_dic = {}
        #opening network list
        if SET == 'CIFAR':
            if file_list.split('-')[4] == '10':
                nets_file = 'nets_list_CIFAR_7.txt'
            elif file_list.split('-')[4] == '20':
                nets_file = 'nets_list_CIFAR_20_7.txt'
            elif file_list.split('-')[4] == '40':
                nets_file = 'nets_list_CIFAR_40_7.txt'
            elif file_list.split('-')[4] == '80':
                nets_file = 'nets_list_CIFAR_80_7.txt'

        if SET == 'MNIST' :
            if file_list.split('-')[4] == '10':
                nets_file = 'nets_list7.txt'
            elif file_list.split('-')[4] == '20':
                nets_file = 'nets_list20_7.txt'
            elif file_list.split('-')[4] == '40':
                nets_file = 'nets_list40_7.txt'
            elif file_list.split('-')[4] == '80':
                nets_file = 'nets_list80_7.txt'

        nets_foo = open(nets_file, 'r')
        nets_list = nets_foo.readlines()

        #continuing with data analysis
        for d_file in os.listdir(run + file_list + '/'):

            data = numpy.load(run + file_list + '/' + d_file)
            train_accuracy = []
            train_error = []
            val_accuracy = []
            val_error = []
            test_accuracy = []
            test_error = []

            for tup in data:
                if tup[3] == 0:
                    train_accuracy.append(tup[0])
                    train_error.append(tup[1])
                if tup[3] == 1:
                    val_accuracy.append(tup[0])
                    val_error.append(tup[1])
            data_dic[file_list + "+" + d_file.split('_')[3].split('.')[0]] = [val_error, val_accuracy]


        for key in data_dic.iterkeys():
            network = nets_list[int(key.split('+')[1])]
            net_parts = network.split('|')
            depth = 0
            depth = len(net_parts) - 2
            vc = 0
            vc = calc_vc(network)
            conv = 0
            full = 0
            mp = 0
            for part in net_parts:
                if 'conv' in part:
                    conv += 1
                if 'full' in part:
                    full += 1
                if 'max_pooling' in part:
                    mp += 1

            plotY_er.append(min(data_dic[key][0]))
            plotY_acc.append(max(data_dic[key][1]))

            plotX_vc.append(vc)
            plotX_mp.append(mp)
            plotX_depth.append(depth)
            plotX_conv.append(conv)
            plotX_fc.append(full)


N = 20
bins, pos = binner(plotX_vc, plotY_er, N)

pl.figure("VC_BOX")
pl.boxplot(bins)

pl.figure("Depth")
pl.scatter(plotX_depth, plotY_er)

pl.figure("Conv")
pl.scatter(plotX_conv, plotY_er)

pl.figure("Fully Connected")
pl.scatter(plotX_fc, plotY_er)

pl.figure("Max Pooling")
pl.scatter(plotX_mp, plotY_er)

pl.figure("DepthACC")
pl.scatter(plotX_depth, plotY_acc)

pl.figure("ConvACC")
pl.scatter(plotX_conv, plotY_acc)

pl.figure("Fully ConnectedACC")
pl.scatter(plotX_fc, plotY_acc)

pl.figure("Max PoolingACC")
pl.scatter(plotX_mp, plotY_acc)

pl.figure("VCACC")
pl.scatter(plotX_vc, plotY_acc)

pl.figure("VC")
pl.scatter(plotX_vc, plotY_er)

# pl.figure("VC_BOX")
# pl.boxplot(plotX_vc, plotY_er)

pl.show()