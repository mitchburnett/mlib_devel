`timescale 1ns/1ps
`default_nettype none 

module rfsoc_pps_in #(
  parameter SYNC_FFS=3
) (
  input wire logic pps_in,
  input wire logic pl_clk,
  output wire pps_out
);

  xpm_cdc_single #(
    .DEST_SYNC_FF(SYNC_FFS),
    .INIT_SYNC_FF(1),       // enable simulation init values
    .SIM_ASSERT_CHK(1),     // enable simulation messages
    .SRC_INPUT_REG(0)       // do not register the input
  ) cdc_inst (
    .dest_out(pps_out),
    .dest_clk(pl_clk),
    .src_clk(1'b0),
    .src_in(pps_in)
  );

endmodule : rfsoc_pps_in

