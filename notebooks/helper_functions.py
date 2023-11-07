import osmosdr

def get_osmosdr_source(frequency, samp_rate=3500000, biastee=False, bandwidth=0):
    if(biastee == True):
        osmosdr_source = osmosdr.source(args="numchan=" + str(1) + " " + 'bladerf=0,biastee=1')
    else:
        osmosdr_source = osmosdr.source(args="numchan=" + str(1) + " " + 'bladerf=0,biastee=0')

    osmosdr_source.set_time_unknown_pps(osmosdr.time_spec_t())
    osmosdr_source.set_sample_rate(samp_rate)
    osmosdr_source.set_center_freq(frequency, 0)
    osmosdr_source.set_freq_corr(0, 0)
    osmosdr_source.set_dc_offset_mode(0, 0)
    osmosdr_source.set_iq_balance_mode(0, 0)
    osmosdr_source.set_gain_mode(False, 0)
    osmosdr_source.set_gain(10, 0)
    osmosdr_source.set_if_gain(20, 0)
    osmosdr_source.set_bb_gain(20, 0)
    osmosdr_source.set_antenna('', 0)
    osmosdr_source.set_bandwidth(bandwidth, 0)

    return osmosdr_source

def get_omsosdr_sink(frequency, samp_rate=3500000, biastee=False, bandwidth=0):
    if(biastee == True):
        osmosdr_sink = osmosdr.sink(args="numchan=" + str(1) + " " + 'bladerf=0,biastee=1')
    else:
        osmosdr_sink = osmosdr.sink(args="numchan=" + str(1) + " " + 'bladerf=0,biastee=0')
    
    osmosdr_sink.set_time_unknown_pps(osmosdr.time_spec_t())
    osmosdr_sink.set_sample_rate(samp_rate)
    osmosdr_sink.set_center_freq(frequency, 0)
    osmosdr_sink.set_freq_corr(0, 0)
    osmosdr_sink.set_gain(10, 0)
    osmosdr_sink.set_if_gain(20, 0)
    osmosdr_sink.set_bb_gain(20, 0)
    osmosdr_sink.set_antenna('', 0)
    osmosdr_sink.set_bandwidth(bandwidth, 0)