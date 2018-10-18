#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Resample
# Author: Jake Drahos
# Description: Filter to a bandwidth, then resample to an output rate.
# Generated: Thu Oct 18 16:35:58 2018
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class resample(gr.top_block):

    def __init__(self, cutoff=5000, decimation=1, gain=1, infile='', interpolation=1, outfile="", samp_rate=-1, transition=100):
        gr.top_block.__init__(self, "Resample")

        ##################################################
        # Parameters
        ##################################################
        self.cutoff = cutoff
        self.decimation = decimation
        self.gain = gain
        self.infile = infile
        self.interpolation = interpolation
        self.outfile = outfile
        self.samp_rate = samp_rate
        self.transition = transition

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interpolation,
                decimation=decimation,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, infile, True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, outfile, False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_file_sink_0, 0))

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_infile(self):
        return self.infile

    def set_infile(self, infile):
        self.infile = infile
        self.blocks_file_source_0.open(self.infile, True)

    def get_interpolation(self):
        return self.interpolation

    def set_interpolation(self, interpolation):
        self.interpolation = interpolation

    def get_outfile(self):
        return self.outfile

    def set_outfile(self, outfile):
        self.outfile = outfile
        self.blocks_file_sink_0.open(self.outfile)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    description = 'Filter to a bandwidth, then resample to an output rate.'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-c", "--cutoff", dest="cutoff", type="intx", default=5000,
        help="Set Filter Cutoff [default=%default]")
    parser.add_option(
        "-D", "--decimation", dest="decimation", type="intx", default=1,
        help="Set Decimation [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="intx", default=1,
        help="Set Gain [default=%default]")
    parser.add_option(
        "-i", "--infile", dest="infile", type="string", default='',
        help="Set Source File [default=%default]")
    parser.add_option(
        "-I", "--interpolation", dest="interpolation", type="intx", default=1,
        help="Set Interpolation [default=%default]")
    parser.add_option(
        "-o", "--outfile", dest="outfile", type="string", default="",
        help="Set Output File [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="intx", default=-1,
        help="Set Source Sample Rate [default=%default]")
    parser.add_option(
        "-t", "--transition", dest="transition", type="intx", default=100,
        help="Set Transition Width [default=%default]")
    return parser


def main(top_block_cls=resample, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(cutoff=options.cutoff, decimation=options.decimation, gain=options.gain, infile=options.infile, interpolation=options.interpolation, outfile=options.outfile, samp_rate=options.samp_rate, transition=options.transition)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
