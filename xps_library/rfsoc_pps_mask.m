%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                                             %
%   Center for Astronomy Signal Processing and Electronics Research           %
%   http://seti.ssl.berkeley.edu/casper/                                      %
%   Copyright (C) 2006 University of California, Berkeley                     %
%                                                                             %
%   This program is free software; you can redistribute it and/or modify      %
%   it under the terms of the GNU General Public License as published by      %
%   the Free Software Foundation; either version 2 of the License, or         %
%   (at your option) any later version.                                       %
%                                                                             %
%   This program is distributed in the hope that it will be useful,           %
%   but WITHOUT ANY WARRANTY; without even the implied warranty of            %
%   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             %
%   GNU General Public License for more details.                              %
%                                                                             %
%   You should have received a copy of the GNU General Public License along   %
%   with this program; if not, write to the Free Software Foundation, Inc.,   %
%   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.               %
%                                                                             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cursys = gcb;

pos = get_param(cursys,'Position');
x= pos(1);
y= pos(2);

try
  remove_all_blks(cursys);
catch ex
  % If remove_all_blks throws a CallbackDelete exception (more specifically a
  % Simulink:Engine:CallbackDelete exception), then we're in a callback of some
  % sort so we shouldn't be removing blocks or redrawing things anyway so just
  % return.
  if regexp(ex.identifier, 'CallbackDelete')
    return
  end
  % Otherwise it's perhaps a legitamite exception so dump and rethrow it.
  dump_and_rethrow(ex);
end

old_ports = ports_struct(get_param(cursys,'blocks'));

gw_name = [clear_name(gcb),'_gateway'];
old_ports = add_port(cursys,old_ports,'outport','pps_in', [350 50 380 65]);
old_ports = add_port(cursys,old_ports,'inport','sim_in', [20 50 50 65]);
add_block('xbsIndex_r4/Gateway In',[cursys,'/',gw_name],'Position', [230 50 290 70],...
    'arith_type', 'Boolean',...
    'n_bits', '1',...
    'bin_pt', '0',...
    'period','sample_period');

add_line(cursys,['sim_in/1'],[gw_name,'/1']);
add_line(cursys,[gw_name,'/1'],['pps_in/1']);

clean_ports(cursys,old_ports);
