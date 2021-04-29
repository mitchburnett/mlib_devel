
import struct

gold_param_list = """00 00 00 00 00 00 00 b0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 9a 99 99 99 99 99 19 40 00 00 00 00 00 00 b9 40 00 00 00 00 00 00 00 00 0a 00 00 00 02 00 00 00 01 00 00 00 00 00 00
00 00 00 00 00 00 00 24 40 04 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 00 00 00 00 9a 99 99 99 99 99 19
40 00 00 00 00 00 00 b9 40 00 00 00 00 00 00 00 00 0a 00 00 00 02 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 24 40 04 00 00 00 00 00
00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 00 00 00 00 9a 99 99 99 99 99 19 40 00 00 00 00 00 00 b9 40 00 00 00 00 00 00
00 00 0a 00 00 00 02 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 24 40 04 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00
00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00
00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00
00 00 00 00 00 00 00 00 00 00 9a 99 99 99 99 99 19 40 00 00 00 00 00 00 b9 40 00 00 00 00 00 00 00 00 0a 00 00 00 02 00 00 00 01 00 00 00 00
00 00 00 00 00 00 00 00 00 24 40 04 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 03 00 00 00 00 00 00 00 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 00
00 00 40 00 00 00 00 00 40 6f 40 00 00 00 00 00 40 6f 40 30 00 00 00 06 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 04 40 04 00 00 00
01 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 01 00 00 00 08 00 00 00 00 00 00
00 01 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00
00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 40 00 00 00 00 00 40 6f 40 00 00 00 00 00
40 6f 40 30 00 00 00 06 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 04 40 04 00 00 00 01 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00
00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 01 00 00 00 08 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 08 00 00 00 00 00 00
00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00
00 00 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 40 00 00 00 00 00 40 6f 40 00 00 00 00 00 40 6f 40 30 00 00 00 06 00 00 00 01 00 00 00 00
00 00 00 00 00 00 00 00 00 04 40 04 00 00 00 01 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00
00 00 00 00 01 00 00 00 08 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00
00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 00 00
00 40 00 00 00 00 00 40 6f 40 00 00 00 00 00 40 6f 40 30 00 00 00 06 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 04 40 04 00 00 00 01
00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 00 00 00 00 01 00 00 00 08 00 00 00 00 00 00 00
01 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00 00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00 00 00 00
00 08 00 00 00 00 00 00 00 00 00 00 00 03 00 00 00"""

rfdc_keys_git = [
"DEVICE_ID",
"C_BASEADDR",
"C_High_Speed_ADC",
"C_Sysref_Master",
"C_Sysref_Master",
"C_Sysref_Source",
"C_Sysref_Source",
"C_IP_Type",
"C_Silicon_Revision",
"C_DAC0_Enable",
"C_DAC0_PLL_Enable",
"C_DAC0_Sampling_Rate",
"C_DAC0_Refclk_Freq",
"C_DAC0_Fabric_Freq",
"C_DAC0_FBDIV",
"C_DAC0_OutDiv",
"C_DAC0_Refclk_Div",
"C_DAC0_Band",
"C_DAC0_Fs_Max",
"C_DAC0_Slices",
"C_DAC_Slice00_Enable",
"C_DAC_Invsinc_Ctrl00",
"C_DAC_Mixer_Mode00",
"C_DAC_Decoder_Mode00",
"C_DAC_Slice01_Enable",
"C_DAC_Invsinc_Ctrl01",
"C_DAC_Mixer_Mode01",
"C_DAC_Decoder_Mode01",
"C_DAC_Slice02_Enable",
"C_DAC_Invsinc_Ctrl02",
"C_DAC_Mixer_Mode02",
"C_DAC_Decoder_Mode02",
"C_DAC_Slice03_Enable",
"C_DAC_Invsinc_Ctrl03",
"C_DAC_Mixer_Mode03",
"C_DAC_Decoder_Mode03",
"C_DAC_Data_Type00",
"C_DAC_Data_Width00",
"C_DAC_Interpolation_Mode00",
"C_DAC_Fifo00_Enable",
"C_DAC_Adder00_Enable",
"C_DAC_Mixer_Type00",
"C_DAC_Data_Type01",
"C_DAC_Data_Width01",
"C_DAC_Interpolation_Mode01",
"C_DAC_Fifo01_Enable",
"C_DAC_Adder01_Enable",
"C_DAC_Mixer_Type01",
"C_DAC_Data_Type02",
"C_DAC_Data_Width02",
"C_DAC_Interpolation_Mode02",
"C_DAC_Fifo02_Enable",
"C_DAC_Adder02_Enable",
"C_DAC_Mixer_Type02",
"C_DAC_Data_Type03",
"C_DAC_Data_Width03",
"C_DAC_Interpolation_Mode03",
"C_DAC_Fifo03_Enable",
"C_DAC_Adder03_Enable",
"C_DAC_Mixer_Type03",
"C_DAC1_Enable",
"C_DAC1_PLL_Enable",
"C_DAC1_Sampling_Rate",
"C_DAC1_Refclk_Freq",
"C_DAC1_Fabric_Freq",
"C_DAC1_FBDIV",
"C_DAC1_OutDiv",
"C_DAC1_Refclk_Div",
"C_DAC1_Band",
"C_DAC1_Fs_Max",
"C_DAC1_Slices",
"C_DAC_Slice10_Enable",
"C_DAC_Invsinc_Ctrl10",
"C_DAC_Mixer_Mode10",
"C_DAC_Decoder_Mode10",
"C_DAC_Slice11_Enable",
"C_DAC_Invsinc_Ctrl11",
"C_DAC_Mixer_Mode11",
"C_DAC_Decoder_Mode11",
"C_DAC_Slice12_Enable",
"C_DAC_Invsinc_Ctrl12",
"C_DAC_Mixer_Mode12",
"C_DAC_Decoder_Mode12",
"C_DAC_Slice13_Enable",
"C_DAC_Invsinc_Ctrl13",
"C_DAC_Mixer_Mode13",
"C_DAC_Decoder_Mode13",
"C_DAC_Data_Type10",
"C_DAC_Data_Width10",
"C_DAC_Interpolation_Mode10",
"C_DAC_Fifo10_Enable",
"C_DAC_Adder10_Enable",
"C_DAC_Mixer_Type10",
"C_DAC_Data_Type11",
"C_DAC_Data_Width11",
"C_DAC_Interpolation_Mode11",
"C_DAC_Fifo11_Enable",
"C_DAC_Adder11_Enable",
"C_DAC_Mixer_Type11",
"C_DAC_Data_Type12",
"C_DAC_Data_Width12",
"C_DAC_Interpolation_Mode12",
"C_DAC_Fifo12_Enable",
"C_DAC_Adder12_Enable",
"C_DAC_Mixer_Type12",
"C_DAC_Data_Type13",
"C_DAC_Data_Width13",
"C_DAC_Interpolation_Mode13",
"C_DAC_Fifo13_Enable",
"C_DAC_Adder13_Enable",
"C_DAC_Mixer_Type13",
"C_DAC2_Enable",
"C_DAC2_PLL_Enable",
"C_DAC2_Sampling_Rate",
"C_DAC2_Refclk_Freq",
"C_DAC2_Fabric_Freq",
"C_DAC2_FBDIV",
"C_DAC2_OutDiv",
"C_DAC2_Refclk_Div",
"C_DAC2_Band",
"C_DAC2_Fs_Max",
"C_DAC2_Slices",
"C_DAC_Slice20_Enable",
"C_DAC_Invsinc_Ctrl20",
"C_DAC_Mixer_Mode20",
"C_DAC_Decoder_Mode20",
"C_DAC_Slice21_Enable",
"C_DAC_Invsinc_Ctrl21",
"C_DAC_Mixer_Mode21",
"C_DAC_Decoder_Mode21",
"C_DAC_Slice22_Enable",
"C_DAC_Invsinc_Ctrl22",
"C_DAC_Mixer_Mode22",
"C_DAC_Decoder_Mode22",
"C_DAC_Slice23_Enable",
"C_DAC_Invsinc_Ctrl23",
"C_DAC_Mixer_Mode23",
"C_DAC_Decoder_Mode23",
"C_DAC_Data_Type20",
"C_DAC_Data_Width20",
"C_DAC_Interpolation_Mode20",
"C_DAC_Fifo20_Enable",
"C_DAC_Adder20_Enable",
"C_DAC_Mixer_Type20",
"C_DAC_Data_Type21",
"C_DAC_Data_Width21",
"C_DAC_Interpolation_Mode21",
"C_DAC_Fifo21_Enable",
"C_DAC_Adder21_Enable",
"C_DAC_Mixer_Type21",
"C_DAC_Data_Type22",
"C_DAC_Data_Width22",
"C_DAC_Interpolation_Mode22",
"C_DAC_Fifo22_Enable",
"C_DAC_Adder22_Enable",
"C_DAC_Mixer_Type22",
"C_DAC_Data_Type23",
"C_DAC_Data_Width23",
"C_DAC_Interpolation_Mode23",
"C_DAC_Fifo23_Enable",
"C_DAC_Adder23_Enable",
"C_DAC_Mixer_Type23",
"C_DAC3_Enable",
"C_DAC3_PLL_Enable",
"C_DAC3_Sampling_Rate",
"C_DAC3_Refclk_Freq",
"C_DAC3_Fabric_Freq",
"C_DAC3_FBDIV",
"C_DAC3_OutDiv",
"C_DAC3_Refclk_Div",
"C_DAC3_Band",
"C_DAC3_Fs_Max",
"C_DAC3_Slices",
"C_DAC_Slice30_Enable",
"C_DAC_Invsinc_Ctrl30",
"C_DAC_Mixer_Mode30",
"C_DAC_Decoder_Mode30",
"C_DAC_Slice31_Enable",
"C_DAC_Invsinc_Ctrl31",
"C_DAC_Mixer_Mode31",
"C_DAC_Decoder_Mode31",
"C_DAC_Slice32_Enable",
"C_DAC_Invsinc_Ctrl32",
"C_DAC_Mixer_Mode32",
"C_DAC_Decoder_Mode32",
"C_DAC_Slice33_Enable",
"C_DAC_Invsinc_Ctrl33",
"C_DAC_Mixer_Mode33",
"C_DAC_Decoder_Mode33",
"C_DAC_Data_Type30",
"C_DAC_Data_Width30",
"C_DAC_Interpolation_Mode30",
"C_DAC_Fifo30_Enable",
"C_DAC_Adder30_Enable",
"C_DAC_Mixer_Type30",
"C_DAC_Data_Type31",
"C_DAC_Data_Width31",
"C_DAC_Interpolation_Mode31",
"C_DAC_Fifo31_Enable",
"C_DAC_Adder31_Enable",
"C_DAC_Mixer_Type31",
"C_DAC_Data_Type32",
"C_DAC_Data_Width32",
"C_DAC_Interpolation_Mode32",
"C_DAC_Fifo32_Enable",
"C_DAC_Adder32_Enable",
"C_DAC_Mixer_Type32",
"C_DAC_Data_Type33",
"C_DAC_Data_Width33",
"C_DAC_Interpolation_Mode33",
"C_DAC_Fifo33_Enable",
"C_DAC_Adder33_Enable",
"C_DAC_Mixer_Type33",
"C_ADC0_Enable",
"C_ADC0_PLL_Enable",
"C_ADC0_Sampling_Rate",
"C_ADC0_Refclk_Freq",
"C_ADC0_Fabric_Freq",
"C_ADC0_FBDIV",
"C_ADC0_OutDiv",
"C_ADC0_Refclk_Div",
"C_ADC0_Band",
"C_ADC0_Fs_Max",
"C_ADC0_Slices",
"C_ADC_Slice00_Enable",
"C_ADC_Mixer_Mode00",
"C_ADC_Slice01_Enable",
"C_ADC_Mixer_Mode01",
"C_ADC_Slice02_Enable",
"C_ADC_Mixer_Mode02",
"C_ADC_Slice03_Enable",
"C_ADC_Mixer_Mode03",
"C_ADC_Data_Type00",
"C_ADC_Data_Width00",
"C_ADC_Decimation_Mode00",
"C_ADC_Fifo00_Enable",
"C_ADC_Mixer_Type00",
"C_ADC_Data_Type01",
"C_ADC_Data_Width01",
"C_ADC_Decimation_Mode01",
"C_ADC_Fifo01_Enable",
"C_ADC_Mixer_Type01",
"C_ADC_Data_Type02",
"C_ADC_Data_Width02",
"C_ADC_Decimation_Mode02",
"C_ADC_Fifo02_Enable",
"C_ADC_Mixer_Type02",
"C_ADC_Data_Type03",
"C_ADC_Data_Width03",
"C_ADC_Decimation_Mode03",
"C_ADC_Fifo03_Enable",
"C_ADC_Mixer_Type03",
"C_ADC1_Enable",
"C_ADC1_PLL_Enable",
"C_ADC1_Sampling_Rate",
"C_ADC1_Refclk_Freq",
"C_ADC1_Fabric_Freq",
"C_ADC1_FBDIV",
"C_ADC1_OutDiv",
"C_ADC1_Refclk_Div",
"C_ADC1_Band",
"C_ADC1_Fs_Max",
"C_ADC1_Slices",
"C_ADC_Slice10_Enable",
"C_ADC_Mixer_Mode10",
"C_ADC_Slice11_Enable",
"C_ADC_Mixer_Mode11",
"C_ADC_Slice12_Enable",
"C_ADC_Mixer_Mode12",
"C_ADC_Slice13_Enable",
"C_ADC_Mixer_Mode13",
"C_ADC_Data_Type10",
"C_ADC_Data_Width10",
"C_ADC_Decimation_Mode10",
"C_ADC_Fifo10_Enable",
"C_ADC_Mixer_Type10",
"C_ADC_Data_Type11",
"C_ADC_Data_Width11",
"C_ADC_Decimation_Mode11",
"C_ADC_Fifo11_Enable",
"C_ADC_Mixer_Type11",
"C_ADC_Data_Type12",
"C_ADC_Data_Width12",
"C_ADC_Decimation_Mode12",
"C_ADC_Fifo12_Enable",
"C_ADC_Mixer_Type12",
"C_ADC_Data_Type13",
"C_ADC_Data_Width13",
"C_ADC_Decimation_Mode13",
"C_ADC_Fifo13_Enable",
"C_ADC_Mixer_Type13",
"C_ADC2_Enable",
"C_ADC2_PLL_Enable",
"C_ADC2_Sampling_Rate",
"C_ADC2_Refclk_Freq",
"C_ADC2_Fabric_Freq",
"C_ADC2_FBDIV",
"C_ADC2_OutDiv",
"C_ADC2_Refclk_Div",
"C_ADC2_Band",
"C_ADC2_Fs_Max",
"C_ADC2_Slices",
"C_ADC_Slice20_Enable",
"C_ADC_Mixer_Mode20",
"C_ADC_Slice21_Enable",
"C_ADC_Mixer_Mode21",
"C_ADC_Slice22_Enable",
"C_ADC_Mixer_Mode22",
"C_ADC_Slice23_Enable",
"C_ADC_Mixer_Mode23",
"C_ADC_Data_Type20",
"C_ADC_Data_Width20",
"C_ADC_Decimation_Mode20",
"C_ADC_Fifo20_Enable",
"C_ADC_Mixer_Type20",
"C_ADC_Data_Type21",
"C_ADC_Data_Width21",
"C_ADC_Decimation_Mode21",
"C_ADC_Fifo21_Enable",
"C_ADC_Mixer_Type21",
"C_ADC_Data_Type22",
"C_ADC_Data_Width22",
"C_ADC_Decimation_Mode22",
"C_ADC_Fifo22_Enable",
"C_ADC_Mixer_Type22",
"C_ADC_Data_Type23",
"C_ADC_Data_Width23",
"C_ADC_Decimation_Mode23",
"C_ADC_Fifo23_Enable",
"C_ADC_Mixer_Type23",
"C_ADC3_Enable",
"C_ADC3_PLL_Enable",
"C_ADC3_Sampling_Rate",
"C_ADC3_Refclk_Freq",
"C_ADC3_Fabric_Freq",
"C_ADC3_FBDIV",
"C_ADC3_OutDiv",
"C_ADC3_Refclk_Div",
"C_ADC3_Band",
"C_ADC3_Fs_Max",
"C_ADC3_Slices",
"C_ADC_Slice30_Enable",
"C_ADC_Mixer_Mode30",
"C_ADC_Slice31_Enable",
"C_ADC_Mixer_Mode31",
"C_ADC_Slice32_Enable",
"C_ADC_Mixer_Mode32",
"C_ADC_Slice33_Enable",
"C_ADC_Mixer_Mode33",
"C_ADC_Data_Type30",
"C_ADC_Data_Width30",
"C_ADC_Decimation_Mode30",
"C_ADC_Fifo30_Enable",
"C_ADC_Mixer_Type30",
"C_ADC_Data_Type31",
"C_ADC_Data_Width31",
"C_ADC_Decimation_Mode31",
"C_ADC_Fifo31_Enable",
"C_ADC_Mixer_Type31",
"C_ADC_Data_Type32",
"C_ADC_Data_Width32",
"C_ADC_Decimation_Mode32",
"C_ADC_Fifo32_Enable",
"C_ADC_Mixer_Type32",
"C_ADC_Data_Type33",
"C_ADC_Data_Width33",
"C_ADC_Decimation_Mode33",
"C_ADC_Fifo33_Enable",
"C_ADC_Mixer_Type33"
]

rfdc_keys = [
  "DEVICE_ID",
  "C_BASEADDR",
  "C_High_Speed_ADC",
  "C_Sysref_Master",
  "C_Sysref_Master",
  "C_Sysref_Source",
  "C_Sysref_Source",
  "C_IP_Type",
  "C_Silicon_Revision",
  "C_DAC0_Enable",
  "C_DAC0_PLL_Enable",
  "C_DAC0_Sampling_Rate",
  "C_DAC0_Refclk_Freq",
  "C_DAC0_Fabric_Freq",
  "C_DAC0_FBDIV",
  "C_DAC0_OutDiv",
  "C_DAC0_Refclk_Div",
  "C_DAC0_Band",
  "C_DAC0_Fs_Max",
  "C_DAC0_Slices",
  "C_DAC_Slice00_Enable",
  "C_DAC_Invsinc_Ctrl00",
  "C_DAC_Mixer_Mode00",
  "C_DAC_Decoder_Mode00",
  "C_DAC_Slice01_Enable",
  "C_DAC_Invsinc_Ctrl01",
  "C_DAC_Mixer_Mode01",
  "C_DAC_Decoder_Mode01",
  "C_DAC_Slice02_Enable",
  "C_DAC_Invsinc_Ctrl02",
  "C_DAC_Mixer_Mode02",
  "C_DAC_Decoder_Mode02",
  "C_DAC_Slice03_Enable",
  "C_DAC_Invsinc_Ctrl03",
  "C_DAC_Mixer_Mode03",
  "C_DAC_Decoder_Mode03",
  "C_DAC_Data_Type00",
  "C_DAC_Data_Width00",
  "C_DAC_Interpolation_Mode00",
  "C_DAC_Fifo00_Enable",
  "C_DAC_Adder00_Enable",
  "C_DAC_Mixer_Type00",
  "C_DAC_Data_Type01",
  "C_DAC_Data_Width01",
  "C_DAC_Interpolation_Mode01",
  "C_DAC_Fifo01_Enable",
  "C_DAC_Adder01_Enable",
  "C_DAC_Mixer_Type01",
  "C_DAC_Data_Type02",
  "C_DAC_Data_Width02",
  "C_DAC_Interpolation_Mode02",
  "C_DAC_Fifo02_Enable",
  "C_DAC_Adder02_Enable",
  "C_DAC_Mixer_Type02",
  "C_DAC_Data_Type03",
  "C_DAC_Data_Width03",
  "C_DAC_Interpolation_Mode03",
  "C_DAC_Fifo03_Enable",
  "C_DAC_Adder03_Enable",
  "C_DAC_Mixer_Type03",
  "C_DAC1_Enable",
  "C_DAC1_PLL_Enable",
  "C_DAC1_Sampling_Rate",
  "C_DAC1_Refclk_Freq",
  "C_DAC1_Fabric_Freq",
  "C_DAC1_FBDIV",
  "C_DAC1_OutDiv",
  "C_DAC1_Refclk_Div",
  "C_DAC1_Band",
  "C_DAC1_Fs_Max",
  "C_DAC1_Slices",
  "C_DAC_Slice10_Enable",
  "C_DAC_Invsinc_Ctrl10",
  "C_DAC_Mixer_Mode10",
  "C_DAC_Decoder_Mode10",
  "C_DAC_Slice11_Enable",
  "C_DAC_Invsinc_Ctrl11",
  "C_DAC_Mixer_Mode11",
  "C_DAC_Decoder_Mode11",
  "C_DAC_Slice12_Enable",
  "C_DAC_Invsinc_Ctrl12",
  "C_DAC_Mixer_Mode12",
  "C_DAC_Decoder_Mode12",
  "C_DAC_Slice13_Enable",
  "C_DAC_Invsinc_Ctrl13",
  "C_DAC_Mixer_Mode13",
  "C_DAC_Decoder_Mode13",
  "C_DAC_Data_Type10",
  "C_DAC_Data_Width10",
  "C_DAC_Interpolation_Mode10",
  "C_DAC_Fifo10_Enable",
  "C_DAC_Adder10_Enable",
  "C_DAC_Mixer_Type10",
  "C_DAC_Data_Type11",
  "C_DAC_Data_Width11",
  "C_DAC_Interpolation_Mode11",
  "C_DAC_Fifo11_Enable",
  "C_DAC_Adder11_Enable",
  "C_DAC_Mixer_Type11",
  "C_DAC_Data_Type12",
  "C_DAC_Data_Width12",
  "C_DAC_Interpolation_Mode12",
  "C_DAC_Fifo12_Enable",
  "C_DAC_Adder12_Enable",
  "C_DAC_Mixer_Type12",
  "C_DAC_Data_Type13",
  "C_DAC_Data_Width13",
  "C_DAC_Interpolation_Mode13",
  "C_DAC_Fifo13_Enable",
  "C_DAC_Adder13_Enable",
  "C_DAC_Mixer_Type13",
  "C_DAC2_Enable",
  "C_DAC2_PLL_Enable",
  "C_DAC2_Sampling_Rate",
  "C_DAC2_Refclk_Freq",
  "C_DAC2_Fabric_Freq",
  "C_DAC2_FBDIV",
  "C_DAC2_OutDiv",
  "C_DAC2_Refclk_Div",
  "C_DAC2_Band",
  "C_DAC2_Fs_Max",
  "C_DAC2_Slices",
  "C_DAC_Slice20_Enable",
  "C_DAC_Invsinc_Ctrl20",
  "C_DAC_Mixer_Mode20",
  "C_DAC_Decoder_Mode20",
  "C_DAC_Slice21_Enable",
  "C_DAC_Invsinc_Ctrl21",
  "C_DAC_Mixer_Mode21",
  "C_DAC_Decoder_Mode21",
  "C_DAC_Slice22_Enable",
  "C_DAC_Invsinc_Ctrl22",
  "C_DAC_Mixer_Mode22",
  "C_DAC_Decoder_Mode22" 
  "C_DAC_Slice23_Enable",
  "C_DAC_Invsinc_Ctrl23",
  "C_DAC_Mixer_Mode23",
  "C_DAC_Decoder_Mode23",
  "C_DAC_Data_Type20",
  "C_DAC_Data_Width20",
  "C_DAC_Interpolation_Mode20",
  "C_DAC_Fifo20_Enable",
  "C_DAC_Adder20_Enable",
  "C_DAC_Mixer_Type20",
  "C_DAC_Data_Type21",
  "C_DAC_Data_Width21",
  "C_DAC_Interpolation_Mode21",
  "C_DAC_Fifo21_Enable",
  "C_DAC_Adder21_Enable",
  "C_DAC_Mixer_Type21",
  "C_DAC_Data_Type22",
  "C_DAC_Data_Width22",
  "C_DAC_Interpolation_Mode22",
  "C_DAC_Fifo22_Enable",
  "C_DAC_Adder22_Enable",
  "C_DAC_Mixer_Type22",
  "C_DAC_Data_Type23",
  "C_DAC_Data_Width23",
  "C_DAC_Interpolation_Mode23",
  "C_DAC_Fifo23_Enable",
  "C_DAC_Adder23_Enable",
  "C_DAC_Mixer_Type23",
  "C_DAC3_Enable",
  "C_DAC3_PLL_Enable",
  "C_DAC3_Sampling_Rate",
  "C_DAC3_Refclk_Freq",
  "C_DAC3_Fabric_Freq",
  "C_DAC3_FBDIV",
  "C_DAC3_OutDiv",
  "C_DAC3_Refclk_Div",
  "C_DAC3_Band",
  "C_DAC3_Fs_Max",
  "C_DAC3_Slices",
  "C_DAC_Slice30_Enable",
  "C_DAC_Invsinc_Ctrl30",
  "C_DAC_Mixer_Mode30",
  "C_DAC_Decoder_Mode30",
  "C_DAC_Slice31_Enable",
  "C_DAC_Invsinc_Ctrl31",
  "C_DAC_Mixer_Mode31",
  "C_DAC_Decoder_Mode31",
  "C_DAC_Slice32_Enable",
  "C_DAC_Invsinc_Ctrl32",
  "C_DAC_Mixer_Mode32",
  "C_DAC_Decoder_Mode32",
  "C_DAC_Slice33_Enable",
  "C_DAC_Invsinc_Ctrl33",
  "C_DAC_Mixer_Mode33",
  "C_DAC_Decoder_Mode33",
  "C_DAC_Data_Type30",
  "C_DAC_Data_Width30",
  "C_DAC_Interpolation_Mode30",
  "C_DAC_Fifo30_Enable",
  "C_DAC_Adder30_Enable",
  "C_DAC_Mixer_Type30",
  "C_DAC_Data_Type31",
  "C_DAC_Data_Width31",
  "C_DAC_Interpolation_Mode31",
  "C_DAC_Fifo31_Enable",
  "C_DAC_Adder31_Enable",
  "C_DAC_Mixer_Type31",
  "C_DAC_Data_Type32",
  "C_DAC_Data_Width32",
  "C_DAC_Interpolation_Mode32",
  "C_DAC_Fifo32_Enable",
  "C_DAC_Adder32_Enable",
  "C_DAC_Mixer_Type32",
  "C_DAC_Data_Type33",
  "C_DAC_Data_Width33",
  "C_DAC_Interpolation_Mode33",
  "C_DAC_Fifo33_Enable",
  "C_DAC_Adder33_Enable",
  "C_DAC_Mixer_Type33",
  "C_ADC0_Enable",
  "C_ADC0_PLL_Enable",
  "C_ADC0_Sampling_Rate",
  "C_ADC0_Refclk_Freq",
  "C_ADC0_Fabric_Freq",
  "C_ADC0_FBDIV",
  "C_ADC0_OutDiv",
  "C_ADC0_Refclk_Div",
  "C_ADC0_Band",
  "C_ADC0_Fs_Max",
  "C_ADC0_Slices",
  "C_ADC_Slice00_Enable",
  "C_ADC_Mixer_Mode00",
  "C_ADC_Slice01_Enable",
  "C_ADC_Mixer_Mode01",
  "C_ADC_Slice02_Enable",
  "C_ADC_Mixer_Mode02",
  "C_ADC_Slice03_Enable",
  "C_ADC_Mixer_Mode03",
  "C_ADC_Data_Type00",
  "C_ADC_Data_Width00",
  "C_ADC_Decimation_Mode00",
  "C_ADC_Fifo00_Enable",
  "C_ADC_Mixer_Type00",
  "C_ADC_Data_Type01",
  "C_ADC_Data_Width01",
  "C_ADC_Decimation_Mode01",
  "C_ADC_Fifo01_Enable",
  "C_ADC_Mixer_Type01",
  "C_ADC_Data_Type02",
  "C_ADC_Data_Width02",
  "C_ADC_Decimation_Mode02",
  "C_ADC_Fifo02_Enable",
  "C_ADC_Mixer_Type02",
  "C_ADC_Data_Type03",
  "C_ADC_Data_Width03",
  "C_ADC_Decimation_Mode03",
  "C_ADC_Fifo03_Enable",
  "C_ADC_Mixer_Type03",
  "C_ADC1_Enable",
  "C_ADC1_PLL_Enable",
  "C_ADC1_Sampling_Rate",
  "C_ADC1_Refclk_Freq",
  "C_ADC1_Fabric_Freq",
  "C_ADC1_FBDIV",
  "C_ADC1_OutDiv",
  "C_ADC1_Refclk_Div",
  "C_ADC1_Band",
  "C_ADC1_Fs_Max",
  "C_ADC1_Slices",
  "C_ADC_Slice10_Enable",
  "C_ADC_Mixer_Mode10",
  "C_ADC_Slice11_Enable",
  "C_ADC_Mixer_Mode11",
  "C_ADC_Slice12_Enable",
  "C_ADC_Mixer_Mode12",
  "C_ADC_Slice13_Enable",
  "C_ADC_Mixer_Mode13",
  "C_ADC_Data_Type10",
  "C_ADC_Data_Width10",
  "C_ADC_Decimation_Mode10",
  "C_ADC_Fifo10_Enable",
  "C_ADC_Mixer_Type10",
  "C_ADC_Data_Type11",
  "C_ADC_Data_Width11",
  "C_ADC_Decimation_Mode11",
  "C_ADC_Fifo11_Enable",
  "C_ADC_Mixer_Type11",
  "C_ADC_Data_Type12",
  "C_ADC_Data_Width12",
  "C_ADC_Decimation_Mode12",
  "C_ADC_Fifo12_Enable",
  "C_ADC_Mixer_Type12",
  "C_ADC_Data_Type13",
  "C_ADC_Data_Width13",
  "C_ADC_Decimation_Mode13",
  "C_ADC_Fifo13_Enable",
  "C_ADC_Mixer_Type13",
  "C_ADC2_Enable",
  "C_ADC2_PLL_Enable",
  "C_ADC2_Sampling_Rate",
  "C_ADC2_Refclk_Freq",
  "C_ADC2_Fabric_Freq",
  "C_ADC2_FBDIV",
  "C_ADC2_OutDiv",
  "C_ADC2_Refclk_Div",
  "C_ADC2_Band",
  "C_ADC2_Fs_Max",
  "C_ADC2_Slices",
  "C_ADC_Slice20_Enable",
  "C_ADC_Mixer_Mode20",
  "C_ADC_Slice21_Enable",
  "C_ADC_Mixer_Mode21",
  "C_ADC_Slice22_Enable",
  "C_ADC_Mixer_Mode22",
  "C_ADC_Slice23_Enable",
  "C_ADC_Mixer_Mode23",
  "C_ADC_Data_Type20",
  "C_ADC_Data_Width20",
  "C_ADC_Decimation_Mode20",
  "C_ADC_Fifo20_Enable",
  "C_ADC_Mixer_Type20",
  "C_ADC_Data_Type21",
  "C_ADC_Data_Width21",
  "C_ADC_Decimation_Mode21",
  "C_ADC_Fifo21_Enable",
  "C_ADC_Mixer_Type21",
  "C_ADC_Data_Type22",
  "C_ADC_Data_Width22",
  "C_ADC_Decimation_Mode22",
  "C_ADC_Fifo22_Enable",
  "C_ADC_Mixer_Type22",
  "C_ADC_Data_Type23",
  "C_ADC_Data_Width23",
  "C_ADC_Decimation_Mode23",
  "C_ADC_Fifo23_Enable",
  "C_ADC_Mixer_Type23",
  "C_ADC3_Enable",
  "C_ADC3_PLL_Enable",
  "C_ADC3_Sampling_Rate",
  "C_ADC3_Refclk_Freq",
  "C_ADC3_Fabric_Freq",
  "C_ADC3_FBDIV",
  "C_ADC3_OutDiv",
  "C_ADC3_Refclk_Div",
  "C_ADC3_Band",
  "C_ADC3_Fs_Max",
  "C_ADC3_Slices",
  "C_ADC_Slice30_Enable",
  "C_ADC_Mixer_Mode30",
  "C_ADC_Slice31_Enable",
  "C_ADC_Mixer_Mode31",
  "C_ADC_Slice32_Enable",
  "C_ADC_Mixer_Mode32",
  "C_ADC_Slice33_Enable",
  "C_ADC_Mixer_Mode33",
  "C_ADC_Data_Type30",
  "C_ADC_Data_Width30",
  "C_ADC_Decimation_Mode30",
  "C_ADC_Fifo30_Enable",
  "C_ADC_Mixer_Type30",
  "C_ADC_Data_Type31",
  "C_ADC_Data_Width31",
  "C_ADC_Decimation_Mode31",
  "C_ADC_Fifo31_Enable",
  "C_ADC_Mixer_Type31",
  "C_ADC_Data_Type32",
  "C_ADC_Data_Width32",
  "C_ADC_Decimation_Mode32",
  "C_ADC_Fifo32_Enable",
  "C_ADC_Mixer_Type32",
  "C_ADC_Data_Type33",
  "C_ADC_Data_Width33",
  "C_ADC_Decimation_Mode33",
  "C_ADC_Fifo33_Enable",
  "C_ADC_Mixer_Type33"
]

if __name__=="__main__":

  rfdc_params = {}
  dt = {}
  dt['compatible'] = '"xlnx,usp-rf-data-converter-2.4";'
  dt['num-insts'] = '<0x1>;'
  dt['baseaddr'] = ''
  dt['range'] = '0x40000'

  #fd = open('dump_rfdc2.txt', 'r')
  fd = open('dump_rfdc_alpaca_snapshots.txt', 'r')

  # skip first line
  s = fd.readline()

  for s in fd.readlines():
    s = s.split()

    k = s[0]
    if "CONFIG." in k:
      v = s[3]
      rfdc_params[k[7:]] = v # strip "CONFIG." and add value
    elif "DT.CLOCKS" in k:
      clks = s[1:]
      clkstr = (len(clks)*'"{:s}"').format(*clks)
      clkstr = clkstr.replace('""', '", "')
      dt['clock-names'] = clkstr + ";"

  fd.close()

  # build param list
  param_list = ""
  rfdc_params['DEVICE_ID'] = '0'

  for k in rfdc_keys_git:
    fmt = ""

    if k == "C_BASEADDR":
      v = rfdc_params[k]
      dt['baseaddr'] = v.lower()
      # low address in little-endian
      param_list += " {:2s} {:2s} {:2s} {:2s}".format(v[8:10], v[6:8], v[4:6], v[2:4])#format(v[2:4], v[4:6], v[6:8], v[8:10])
      # high address hard coded to 0x00000000
      param_list += " 00 00 00 00"

      
    else:
      if ('_Sampling_Rate' in k) or ('_Refclk_Freq' in k) or ('_Fabric_Freq' in k) or ('_Fs_Max' in k):
        fmt = '<d' # little-endian double
        t = float
      else:
        fmt = '<i' # little-endian int
        t = int

      if k in rfdc_params.keys():
        v = rfdc_params[k]
        if v == 'true':
          v = 1
        elif v == 'false':
          v = 0
      else:
        v = 0

      # make byte conversion
      p = struct.pack(fmt, t(v)) # struct.pack('d', 250.0)
      to_add = " {:s}".format(p.hex(' ', 1))
      if fmt == '<d':
        print("{:28s} {:s} {:8.3f} {:s}".format(k, fmt, t(v), to_add))
      elif fmt == '<i':
        print("{:28s} {:s} {:8d} {:s}".format(k, fmt, t(v), to_add))
      param_list += " {:s}".format(p.hex(' ', 1))

  param_list = param_list.lower()

  dt['param-list'] = '[{:s}];'.format(param_list)

  dtreg_fmt = '<{:s} {:s} {:s} {:s}>;'
  dt['reg'] = dtreg_fmt.format('0x0', dt['baseaddr'], '0x0', dt['range'])

  # compare
  g = gold_param_list.split()
  p = param_list.split()

  k = 0
  for (i,j) in zip(g, p):
    if (i != j):
      print("ERROR", k, "g[k]=", i, "p[k]=",j)
    k+=1

  dtstr = []
  dtstr.append('/* AUTOMATICALLY GENERATED */\n')
  dtstr.append('/dts-v1/;')
  dtstr.append('/plugin/;')
  dtstr.append('/ {')
  dtstr.append('    fragment@0 {')
  dtstr.append('      target = <&amba>;')
  dtstr.append('      overlay0: __overlay__ {')
  dtstr.append('        #address-cells = <2>;')
  dtstr.append('        #size-cells = <2>;')
  dtstr.append('        usp_rf_data_converter_0: usp_rf_data_converter@{:s} {{'.format(dt['baseaddr'][2:]))
  dtstr.append('         clock-names = {:s}'.format(dt['clock-names']))
  dtstr.append('         compatible = {:s}'.format(dt['compatible']))
  dtstr.append('         num-insts = {:s}'.format(dt['num-insts']))
  dtstr.append('         param-list = {:s}'.format(dt['param-list']))
  dtstr.append('         reg = {:s}'.format(dt['reg']))
  dtstr.append('        };')
  dtstr.append('      };')
  dtstr.append('    };')
  dtstr.append('};')

  dtnode = '\n'.join(dtstr)
  print(dtnode)

  fd = open('casper-rfdc-overlay-fragment.dtsi', 'w+')
  fd.write(dtnode)
  fd.close() 
