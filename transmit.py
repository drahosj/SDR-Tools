#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SDR Tx IQ File
# Author: Jake Drahos
# Description: Transmit an IQ file of the given sample rate
# Generated: Thu Oct 18 16:45:39 2018
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import pmt
import time


class transmit(gr.top_block):

    def __init__(self, antenna="", bandwidth=5000, bbgain=0, center=-1, device="", ifgain=0, infile="", rfgain=0, samp_rate=-1):
        gr.top_block.__init__(self, "SDR Tx IQ File")

        ##################################################
        # Parameters
        ##################################################
        self.antenna = antenna
        self.bandwidth = bandwidth
        self.bbgain = bbgain
        self.center = center
        self.device = device
        self.ifgain = ifgain
        self.infile = infile
        self.rfgain = rfgain
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + device )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(rfgain, 0)
        self.osmosdr_sink_0.set_if_gain(ifgain, 0)
        self.osmosdr_sink_0.set_bb_gain(bbgain, 0)
        self.osmosdr_sink_0.set_antenna(antenna, 0)
        self.osmosdr_sink_0.set_bandwidth(bandwidth, 0)

        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, infile, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.osmosdr_sink_0, 0))

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self.osmosdr_sink_0.set_antenna(self.antenna, 0)

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.osmosdr_sink_0.set_bandwidth(self.bandwidth, 0)

    def get_bbgain(self):
        return self.bbgain

    def set_bbgain(self, bbgain):
        self.bbgain = bbgain
        self.osmosdr_sink_0.set_bb_gain(self.bbgain, 0)

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center
        self.osmosdr_sink_0.set_center_freq(self.center, 0)

    def get_device(self):
        return self.device

    def set_device(self, device):
        self.device = device

    def get_ifgain(self):
        return self.ifgain

    def set_ifgain(self, ifgain):
        self.ifgain = ifgain
        self.osmosdr_sink_0.set_if_gain(self.ifgain, 0)

    def get_infile(self):
        return self.infile

    def set_infile(self, infile):
        self.infile = infile
        self.blocks_file_source_0.open(self.infile, False)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self.osmosdr_sink_0.set_gain(self.rfgain, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)


def argument_parser():
    description = 'Transmit an IQ file of the given sample rate'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-A", "--antenna", dest="antenna", type="string", default="",
        help="Set Antenna Argument [default=%default]")
    parser.add_option(
        "-b", "--bandwidth", dest="bandwidth", type="intx", default=5000,
        help="Set Filter Bandwidth (Radio) [default=%default]")
    parser.add_option(
        "-B", "--bbgain", dest="bbgain", type="intx", default=0,
        help="Set Baseband Gain [default=%default]")
    parser.add_option(
        "-c", "--center", dest="center", type="intx", default=-1,
        help="Set Center Frequency [default=%default]")
    parser.add_option(
        "-D", "--device", dest="device", type="string", default="",
        help="Set Device Arguments [default=%default]")
    parser.add_option(
        "-I", "--ifgain", dest="ifgain", type="intx", default=0,
        help="Set IF Gain [default=%default]")
    parser.add_option(
        "-i", "--infile", dest="infile", type="string", default="",
        help="Set Input File [default=%default]")
    parser.add_option(
        "-R", "--rfgain", dest="rfgain", type="intx", default=0,
        help="Set RF Gain [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="intx", default=-1,
        help="Set Sample Rate [default=%default]")
    return parser


def main(top_block_cls=transmit, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    tb = top_block_cls(antenna=options.antenna, bandwidth=options.bandwidth, bbgain=options.bbgain, center=options.center, device=options.device, ifgain=options.ifgain, infile=options.infile, rfgain=options.rfgain, samp_rate=options.samp_rate)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
