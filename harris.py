from pnr import *

#// harris16.yml


def lambda_arris_v3lua_line43_10(in0, in1, in2):

  lambda_arris_v3lua_line43_48_0 = Node(in0);
  lambda_arris_v3lua_line43_42_0 = Node(in1);
  EXP_edge__0_0 = Node(lambda_arris_v3lua_line43_48_0, lambda_arris_v3lua_line43_42_0);
  lambda_arris_v3lua_line43_45_0 = Node(in2);
  lambda_arris_v3lua_line43_49_0 = Node(lambda_arris_v3lua_line43_45_0, EXP_edge__0_0);
  lambda_arris_v3lua_line43_49_shifted_0 = Node(lambda_arris_v3lua_line43_49_0);
  lambda_arris_v3lua_line43_50_0 = Node(lambda_arris_v3lua_line43_49_shifted_0);
  lambda_arris_v3lua_line43_51_0 = Node(lambda_arris_v3lua_line43_50_0);
  
  return lambda_arris_v3lua_line43_51_0;

# END lambda_arris_v3lua_line43_10


def Resp_5(in0, in1, in2, in3, in4, in5, in6, in7, in8):

  in1x_30_0 = Node(in2, name="in1x_30");
  in1x_33_0 = Node(in0);
  EXP_edge__17_0 = Node(in1x_33_0, in8);
  Resp_23_0 = Node();
  in1x_35_0 = Node(in7);
  in1x_31_0 = Node(in1);
  in1x_32_0 = Node(in1x_31_0);
  EXP_edge__16_0 = Node(in1x_30_0, in1x_32_0);
  EXP_edge__19_0 = Node(EXP_edge__16_0, EXP_edge__17_0);
  EXP_edge__18_0 = Node(in1x_35_0, in6);
  in1x_36_0 = Node(EXP_edge__18_0, EXP_edge__19_0);
  in1x_37_0 = Node(in1x_36_0, Resp_23_0);
  in1x_38_0 = Node(in1x_37_0);
  Wxx_21_0 = Node(in1x_38_0, in1x_38_0);
  Wxx_22_0 = Node(Wxx_21_0);
  Wxx_23_0 = Node(Wxx_22_0, Resp_23_0);
  in1y_19_0 = Node(in5);
  in1x_34_0 = Node(in8);
  EXP_edge__1_0 = Node(in1x_34_0, in0);
  in1y_20_0 = Node(in1y_19_0);
  EXP_edge__0_0 = Node(in1x_30_0, in1y_20_0);
  EXP_edge__3_0 = Node(EXP_edge__0_0, EXP_edge__1_0);
  in1y_21_0 = Node(in3);
  EXP_edge__2_0 = Node(in1y_21_0, in6);
  in1y_22_0 = Node(EXP_edge__2_0, EXP_edge__3_0);
  in1y_23_0 = Node(in1y_22_0, Resp_23_0);
  in1y_24_0 = Node(in1y_23_0);
  Wxy_13_0 = Node(in1x_38_0, in1y_24_0);
  Wxy_14_0 = Node(Wxy_13_0);
  Wxy_15_0 = Node(Wxy_14_0, Resp_23_0);
  Wxy_16_0 = Node(Wxy_15_0);
  Det_18_0 = Node(Wxy_16_0, Wxy_16_0);
  Det_19_0 = Node(Det_18_0);
  Wxx_24_0 = Node(Wxx_23_0);
  Wyy_16_0 = Node(in1y_24_0, in1y_24_0);
  Wyy_17_0 = Node(Wyy_16_0);
  Wyy_18_0 = Node(Wyy_17_0, Resp_23_0);
  Wyy_19_0 = Node(Wyy_18_0);
  TrSq_15_0 = Node(Wxx_24_0, Wyy_19_0);
  Det_16_0 = Node(Wxx_24_0, Wyy_19_0);
  Det_17_0 = Node(Det_16_0);
  Det_20_0 = Node(Det_17_0, Det_19_0);
  TrSq_16_0 = Node(TrSq_15_0);
  TrSq_17_0 = Node(TrSq_16_0, TrSq_16_0);
  TrSq_18_0 = Node(TrSq_17_0);
  Resp1_7_0 = Node(TrSq_18_0);
  Resp1_8_0 = Node(Det_20_0, Resp1_7_0);
  Resp_30_0 = Node(Resp1_8_0, Resp_23_0);
  Resp_31_0 = Node(Resp_30_0);
  
  return Resp_31_0;

# END Resp_5


def scheduledIRNode_28(in0, in1, in2):

  out = [];#2
  
  
  out.append( in0 );
  out.append( in1 );
  out.append( in2 );
  
  return tuple(out);

# END scheduledIRNode_28


def downCast_15(in0, in1, in2, in3, in4):

  convolve_1_5__89_0 = Node(in2);
  convolve_1_5__90_0 = Node(in4);
  convolve_1_5__91_0 = Node(in3);
  EXP_edge__3_0 = Node(convolve_1_5__89_0, convolve_1_5__91_0);
  Resp_21_0 = Node();
  convolve_1_5__88_0 = Node(in1);
  convolve_1_5__92_0 = Node(in0);
  EXP_edge__2_0 = Node(convolve_1_5__92_0, convolve_1_5__88_0);
  EXP_edge__4_0 = Node(convolve_1_5__90_0, EXP_edge__2_0);
  convolve_1_5__93_0 = Node(EXP_edge__3_0, EXP_edge__4_0);
  convolve_1_5__94_0 = Node(convolve_1_5__93_0);
  convolve_1_5__95_0 = Node(convolve_1_5__94_0, Resp_21_0);
  convolve_1_5__96_0 = Node(convolve_1_5__95_0);
  
  return convolve_1_5__96_0;

# END downCast_15


def NMS_10(in0, in1, in2, in3, in4, in5, in6, in7, in8):

  PE_4_0 = Node(in4, in7);
  PN_4_0 = Node(in4, in5);
  PW_4_0 = Node(in4, in1);
  P_8_0 = Node(in4);
  Pk_13_0 = Node(P_8_0, PW_4_0);
  PS_4_0 = Node(in4, in3);
  Pk_14_0 = Node(Pk_13_0, PE_4_0);
  Pk_15_0 = Node(Pk_14_0, PS_4_0);
  Pk_16_0 = Node(Pk_15_0, PN_4_0);
  NMS_10_0 = Node(Pk_16_0);
  
  return NMS_10_0;

# END NMS_10


def downCast_13(in0, in1, in2, in3, in4):

  convolve_1_5__56_0 = Node(in2);
  convolve_1_5__57_0 = Node(in0);
  convolve_1_5__58_0 = Node(in1);
  EXP_edge__3_0 = Node(convolve_1_5__56_0, convolve_1_5__58_0);
  Resp_19_0 = Node();
  convolve_1_5__55_0 = Node(in3);
  convolve_1_5__59_0 = Node(in4);
  EXP_edge__2_0 = Node(convolve_1_5__59_0, convolve_1_5__55_0);
  EXP_edge__4_0 = Node(convolve_1_5__57_0, EXP_edge__2_0);
  convolve_1_5__60_0 = Node(EXP_edge__3_0, EXP_edge__4_0);
  convolve_1_5__61_0 = Node(convolve_1_5__60_0);
  convolve_1_5__62_0 = Node(convolve_1_5__61_0, Resp_19_0);
  convolve_1_5__63_0 = Node(convolve_1_5__62_0);
  
  return convolve_1_5__63_0;

# END downCast_13


def top(TOP_in0, TOP_in1, TOP_in2):
  #TOP_out0;
  
  KERNEL_IP_scheduledIRNode_28_0 = TOP_in0;
  KERNEL_IP_scheduledIRNode_28_1 = TOP_in1;
  KERNEL_IP_scheduledIRNode_28_2 = TOP_in2;
  #// ------------------------------------------------------------
  (KERNEL_OP_cropSpecial0Node_10_0, KERNEL_OP_cropSpecial0Node_10_1, KERNEL_OP_cropSpecial0Node_10_2) =  scheduledIRNode_28(KERNEL_IP_scheduledIRNode_28_0, KERNEL_IP_scheduledIRNode_28_1, KERNEL_IP_scheduledIRNode_28_2);
  (KERNEL_IP_lambda_arris_v3lua_line43_10_0, KERNEL_IP_lambda_arris_v3lua_line43_10_1, KERNEL_IP_lambda_arris_v3lua_line43_10_2) = LineBuf_1_1_3_16bit_False(KERNEL_OP_cropSpecial0Node_10_0, KERNEL_OP_cropSpecial0Node_10_1, KERNEL_OP_cropSpecial0Node_10_2);
  #// ------------------------------------------------------------
  KERNEL_OP_lambda_arris_v3lua_line43_51_0 =  lambda_arris_v3lua_line43_10(KERNEL_IP_lambda_arris_v3lua_line43_10_0, KERNEL_IP_lambda_arris_v3lua_line43_10_1, KERNEL_IP_lambda_arris_v3lua_line43_10_2);
  (KERNEL_IP_downCast_13_0, KERNEL_IP_downCast_13_1, KERNEL_IP_downCast_13_2, KERNEL_IP_downCast_13_3, KERNEL_IP_downCast_13_4) = LineBuf_1_5_1_16bit_False(KERNEL_OP_lambda_arris_v3lua_line43_51_0);
  #// ------------------------------------------------------------
  KERNEL_OP_downCast_20_0 =  downCast_13(KERNEL_IP_downCast_13_0, KERNEL_IP_downCast_13_1, KERNEL_IP_downCast_13_2, KERNEL_IP_downCast_13_3, KERNEL_IP_downCast_13_4);
  (KERNEL_IP_downCast_15_0, KERNEL_IP_downCast_15_1, KERNEL_IP_downCast_15_2, KERNEL_IP_downCast_15_3, KERNEL_IP_downCast_15_4) = LineBuf_5_1_1_16bit_False(KERNEL_OP_downCast_20_0);
  #// ------------------------------------------------------------
  KERNEL_OP_downCast_38_0 =  downCast_15(KERNEL_IP_downCast_15_0, KERNEL_IP_downCast_15_1, KERNEL_IP_downCast_15_2, KERNEL_IP_downCast_15_3, KERNEL_IP_downCast_15_4);
  (KERNEL_IP_Resp_5_0, KERNEL_IP_Resp_5_1, KERNEL_IP_Resp_5_2, KERNEL_IP_Resp_5_3, KERNEL_IP_Resp_5_4, KERNEL_IP_Resp_5_5, KERNEL_IP_Resp_5_6, KERNEL_IP_Resp_5_7, KERNEL_IP_Resp_5_8) = LineBuf_3_3_1_16bit_False(KERNEL_OP_downCast_38_0);
  #// ------------------------------------------------------------
  KERNEL_OP_Resp_32_0 =  Resp_5(KERNEL_IP_Resp_5_0, KERNEL_IP_Resp_5_1, KERNEL_IP_Resp_5_2, KERNEL_IP_Resp_5_3, KERNEL_IP_Resp_5_4, KERNEL_IP_Resp_5_5, KERNEL_IP_Resp_5_6, KERNEL_IP_Resp_5_7, KERNEL_IP_Resp_5_8);
  (KERNEL_IP_NMS_10_0, KERNEL_IP_NMS_10_1, KERNEL_IP_NMS_10_2, KERNEL_IP_NMS_10_3, KERNEL_IP_NMS_10_4, KERNEL_IP_NMS_10_5, KERNEL_IP_NMS_10_6, KERNEL_IP_NMS_10_7, KERNEL_IP_NMS_10_8) = LineBuf_3_3_1_16bit_False(KERNEL_OP_Resp_32_0);
  #// ------------------------------------------------------------
  KERNEL_OP_NMS_11_0 =  NMS_10(KERNEL_IP_NMS_10_0, KERNEL_IP_NMS_10_1, KERNEL_IP_NMS_10_2, KERNEL_IP_NMS_10_3, KERNEL_IP_NMS_10_4, KERNEL_IP_NMS_10_5, KERNEL_IP_NMS_10_6, KERNEL_IP_NMS_10_7, KERNEL_IP_NMS_10_8);
  TOP_out0 = KERNEL_OP_NMS_11_0;

  return TOP_out0;
def LineBuf_3_3_1_16bit_False (in0):
    out = [];# 0 x 3 x 3 
    #// (3, 3, 1, 16, False)

    (out8, out7, out6, out5, out4, out3, out2, out1, out0) = LB_base_3_3_16bit (in0);

    out.append(out0);
    out.append(out1);
    out.append(out2);
    out.append(out3);
    out.append(out4);
    out.append(out5);
    out.append(out6);
    out.append(out7);
    out.append(out8);


    return tuple(out)


def LineBuf_5_1_1_16bit_False (in0):
    out = [];# 0 x 5 x 1 
    #// (5, 1, 1, 16, False)

    out4, out3, out2, out1, out0 = LB_base_5_1_16bit (in0);

    out.append(out0);
    out.append(out1);
    out.append(out2);
    out.append(out3);
    out.append(out4);


    return tuple(out)


def LineBuf_1_1_3_16bit_False (in2, in1, in0):
    out = [];# 2 x 1 x 1 
    #// (1, 1, 3, 16, False)

    out0 = LB_base_1_1_16bit (in0);

    out1 = LB_base_1_1_16bit (in1);

    out2 = LB_base_1_1_16bit (in2);

    out.append(out0);
    out.append(out1);
    out.append(out2);


    return tuple(out)


def LineBuf_1_5_1_16bit_False (in0):
    out = [];# 0 x 1 x 5 
    #// (1, 5, 1, 16, False)

    out4, out3, out2, out1, out0 = LB_base_1_5_16bit (in0);

    out.append(out0);
    out.append(out1);
    out.append(out2);
    out.append(out3);
    out.append(out4);


    return tuple(out)


def LB_base_1_5_16bit (inp) :
    out = [];#// 1 x 5

    inp_reg = Node(inp);#reg
    sram_out_0 = inp_reg;


    (out_0_4, out_0_3, out_0_2, out_0_1, out_0_0) = ShiftReg_base_5_16bit (sram_out_0);


    out.append(out_0_0)
    out.append(out_0_1)
    out.append(out_0_2)
    out.append(out_0_3)
    out.append(out_0_4)


    return tuple(out)


def LB_base_3_3_16bit (inp) :
    out = [];#// 3 x 3

    sram_out_0 = Node(inp);#my_lb2
    sram_out_1 = sram_out_0;
    inp_reg = Node(inp);#reg
    sram_out_2 = inp_reg;


    (out_0_2, out_0_1, out_0_0) = ShiftReg_base_3_16bit (sram_out_0);
    (out_1_2, out_1_1, out_1_0) = ShiftReg_base_3_16bit (sram_out_1);
    (out_2_2, out_2_1, out_2_0) = ShiftReg_base_3_16bit (sram_out_2);


    out.append(out_0_0)
    out.append(out_0_1)
    out.append(out_0_2)
    out.append(out_1_0)
    out.append(out_1_1)
    out.append(out_1_2)
    out.append(out_2_0)
    out.append(out_2_1)
    out.append(out_2_2)


    return tuple(out)


def LB_base_1_1_16bit (inp) :
    inp_reg = Node(inp);#reg
    sram_out_0 = inp_reg;


    out_0_0 = ShiftReg_base_1_16bit (sram_out_0);


    return out_0_0


def LB_base_5_1_16bit (inp) :
    out = [];#// 5 x 1

    sram_out_0 = Node(inp);#my_lb2
    sram_out_1 = sram_out_0;
    sram_out_2 = Node(inp);#my_lb2
    sram_out_3 = sram_out_2;
    inp_reg = Node(inp);#reg
    sram_out_4 = inp_reg;


    out_0_0 = ShiftReg_base_1_16bit (sram_out_0);
    out_1_0 = ShiftReg_base_1_16bit (sram_out_1);
    out_2_0 = ShiftReg_base_1_16bit (sram_out_2);
    out_3_0 = ShiftReg_base_1_16bit (sram_out_3);
    out_4_0 = ShiftReg_base_1_16bit (sram_out_4);


    out.append(out_0_0)
    out.append(out_1_0)
    out.append(out_2_0)
    out.append(out_3_0)
    out.append(out_4_0)


    return tuple(out)


def ShiftReg_base_3_16bit ( inp_16b ):

    out=[]; # 3


    out_0_16b = Node(inp_16b);#reg
    out_1_16b = Node(out_0_16b);#reg
    out_2_16b = Node(out_1_16b);#reg


    out.append(out_0_16b);
    out.append(out_1_16b);
    out.append(out_2_16b);

    return tuple(out)

def ShiftReg_base_1_16bit ( inp_16b ):

    out_0_16b = Node(inp_16b);#reg

    return out_0_16b

def ShiftReg_base_5_16bit ( inp_16b ):

    out=[]; # 5


    out_0_16b = Node(inp_16b);#reg
    out_1_16b = Node(out_0_16b);#reg
    out_2_16b = Node(out_1_16b);#reg
    out_3_16b = Node(out_2_16b);#reg
    out_4_16b = Node(out_3_16b);#reg


    out.append(out_0_16b);
    out.append(out_1_16b);
    out.append(out_2_16b);
    out.append(out_3_16b);
    out.append(out_4_16b);

    return tuple(out)

a = Node()
b = Node()
c = Node()
root = top(a,b,c)

print 'setting up model'
nodes = root.flatten()
connections = 0
for n in nodes:
    for i in n.inputs:
        connections += 1
print len(nodes), 'nodes, ', connections, 'connections'

s = setup(nodes,False,True,True)

s.add(root.x == 0, root.y == 0)

print 'solving'
models = list(getmodels(s, 8))
if len(models) == 0:
    print "no solutions"
else:
    mlength = None
    length = 0
    tracks = 0
    for m in models:
        t, l = stats(m,nodes)
        if mlength is None or l < length:
            tracks = t
            length = l
            mlength = m
    printmodel(mlength, nodes)
    print 'tracks', tracks, 'length', length
