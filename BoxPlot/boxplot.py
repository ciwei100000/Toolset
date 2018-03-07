# -*- coding:utf-8 -*-

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

import os
import argparse

plotly.tools.set_credentials_file(username='ciwei100000', api_key='8Q8vs5Q6molj0AKABaGW')


def boxplot(ifile, ofile):
    ifile = os.path.expanduser(os.path.expandvars(ifile))
    ofile = os.path.expanduser(os.path.expandvars(ofile))

    data = []
    listofgroup_x = []
    listofgroup_y = []

    if os.path.isdir(ifile):
        for dirpath, dirnames, filenames in os.walk(ifile):
            basename = os.path.basename(dirpath)
            num_file = 0
            for filename in filenames:
                num_file = num_file + 1
                x = []
                y = []
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "r") as f:
                    for line in f:

                        try:
                            tmp = float(line)
                        except ValueError:
                            continue

                        if num_file > len(listofgroup_x):
                            x.append(tmp)
                            y.append(basename)
                            listofgroup_x.append(x)
                            listofgroup_y.append(y)
                        else:
                            listofgroup_x[num_file - 1].append(tmp)
                            listofgroup_y[num_file - 1].append(basename)

        for i in range(len(listofgroup_x)):
            trace = go.Box(
                y=listofgroup_y,
                x=listofgroup_x,
                name="$d" % i,
            )

            data.append(trace)

        layout = go.Layout(
            yaxis=dict(
                title='transfer time',
                zeroline=False
            ),
            boxmode='group'
        )

        fig = go.Figure(data=data, layout=layout)

    else:
        x = []
        with open(ifile, "r") as f:
            for line in f:
                try:
                    tmp = float(line)
                except ValueError:
                    continue
                x.append(tmp)

        trace = go.Box(x=x)
        data.append(trace)
        fig = go.Figure(data)

    py.image.save_as(fig, filename='%s.png' % ofile)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='plotting transfer time between sender and receiver')

    parser.add_argument('--ifile', '-i', dest='ifile', type=str, help='The input file or directories, default is ./',
                        default='./')

    parser.add_argument('--ofile', '-o', dest='ofile', type=str,
                        help='The name of the output png file, default is ./output',
                        default='./output')

    args = parser.parse_args()

    boxplot(args.ifile, args.ofile)
