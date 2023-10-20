from .yellow_block import YellowBlock

class rfsoc_pps(YellowBlock):
    def initialize(self):
        self.add_source('infrastructure/rfsoc_pps_in.sv')
        self.requires.append('user_clk')

        self.pps_gpio = YellowBlock.make_block({
            # adding the io_net_name makes it unique when using multiple pps in's (for whatever reason)
            'fullpath': self.fullpath+"/"+self.io_net_name,
            'tag': 'xps:gpio',
            'io_group_real': 'custom',
            'io_group_custom': self.io_net_name,
            'io_dir': 'in',
            'arith_type': 'Boolean',
            'bitwidth': 1,
            'bin_pt': 0,
            'bit_index': 0,
            'use_single_ended': False,
            'use_ddr': False,
            'reg_iob': True,
            'reg_clk_phase': 0,
            'termination': None,
            'use_iodelay': False
            }, self.platform)

    def modify_top(self, top):
        pps_sync_inst = top.get_instance('rfsoc_pps_in', 'rfsoc_pps_{:s}_inst'.format(self.io_net_name))
        pps_sync_inst.add_parameter('SYNC_FFS', 2)

        pps_sync_inst.add_port('pl_clk', 'user_clk')
        # This yellow block instances a child gpio yellow block to do the required low-level heavy lifting of
        # getting information from the platform file, getting the net into the top module, and setting up constraints
        # to weire it up we use its fullname as if it had been in the user design (adding "_gateway" to the fullname
        # is required as this is what the gpio yellow block creates for itself, but there is no real way for this
        # parent yellow block to know what it was)
        pps_sync_inst.add_port('pps_in', self.pps_gpio.fullname+'_gateway', parent_sig=False)

        # `pps_out` is what is needs to be sent into the user design and this yellow block is the one
        # within the user design that has the gateway and so we use its name here
        pps_sync_inst.add_port('pps_out', self.fullname+'_gateway', parent_sig=False)


    def gen_children(self):
        children = []
        children.append(self.pps_gpio)
        return children


    def gen_constraints(self):
        const = []
        return const


    def gen_tcl_cmds(self):
        tcl_cmds = {}
        return tcl_cmds
