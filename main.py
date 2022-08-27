from modules.imports import *
from descriptions import * 

label = ttk.Label(window, text = 'Configure Chromite Core', font = 'Arial 15 bold').pack(side='top', anchor='center', padx=(10, 10), pady=(10, 10))

frame_1 = createFrame(window, side='left', fill = 'y', padx=(10, 10), pady=(10, 10))

num_harts_description = 'Description: Total number of harts to be instantiated in the dummy test-soc. Note that these will non-coherent cores simply acting as masters on the fast-bus.'

num_harts = createCounterField(frame_1, 
                'Number of Harts', 
                infoboxBool = True, 
                heading='num_harts', 
                description=num_harts_description, 
                default_val=1)

overlap_redirections_description = 'Description: When set to true this field indicates that the branch resolution and the new PC latching to the I$ happen in the same cycle. When set to False, there is a single cycle latency between branch resolution and the new PC being latched to the I$'

overlap_redirections = createTrueFalse(frame_1,
                "Overlap Redirections", 
                infoboxBool = True, 
                heading= 'Overlap Rediretions', 
                description=overlap_redirections_description,)

isb_sizes = createWindow(frame_1,
                        'ISB Sizes',
                        'ISB Sizes',
                        infoboxBool=True,
                        heading='ISB Sizes',
                        description=isb_sizes_description)

frame_isb_size = createFrame(isb_sizes, side='top', fill='both', pady=(10, 10), padx=(10, 10))

isb_s0s1 = createCounterField(frame_isb_size,
                "ISB S0S1",
                default_val=2)
isb_s1s2 = createCounterField(frame_isb_size,
                "ISB S1S2",
                default_val=2)
isb_s2s3 = createCounterField(frame_isb_size,
                "ISB S2S3",
                default_val=1)
isb_s3s4 = createCounterField(frame_isb_size,
                "ISB S3S4",
                default_val=2)
isb_s4s5 = createCounterField(frame_isb_size,
                "ISB S4S5",
                default_val=2)
isb_cachebuffer = createCounterField(frame_isb_size,
                "ISB Cachebuffer",
                default_val=3)                  

merged_rf = createTrueFalse(frame_1,
                "Merged RF", 
                default_val=True,
                infoboxBool = True, 
                heading= 'Overlap Rediretions', 
                description=overlap_redirections_description,)

total_events = createCounterField(frame_1, 
                'Total Events', 
                infoboxBool = True, 
                heading='num_harts', 
                description=num_harts_description, 
                default_val=0)

waw_stalls = createTrueFalse(frame_1,
                "WAW Stalls", 
                default_val=False,
                infoboxBool = True, 
                heading= 'Overlap Rediretions', 
                description=overlap_redirections_description,)

iepoch_size = createTextEntry(frame_1,
                                "IEPOCH Size",
                                default_val=2,
                                infoboxBool = True,
                                heading= 'Overlap Rediretions',
                                description=overlap_redirections_description,
                                default_fixed=True)

depoch_size = createTextEntry(frame_1,
                                "DEPOCH Size",
                                default_val=1,
                                infoboxBool = True,
                                heading= 'Overlap Rediretions',
                                description=overlap_redirections_description,
                                default_fixed=True)

noinline_modules = createWindow(frame_1,
                        'Noinline Modules',
                        'Noinline Modules',
                        infoboxBool=True,
                        heading='Noinline Modules',
                        description=isb_sizes_description)

frame_noinline_modules = createFrame(noinline_modules, side='left', fill = 'y', padx=(10, 10), pady=(10, 10))

stage0 = createTrueFalse(frame_noinline_modules, "Stage 0", default_val=False)
stage1 = createTrueFalse(frame_noinline_modules, "Stage 1", default_val=False)
stage2 = createTrueFalse(frame_noinline_modules, "Stage 2", default_val=False)
stage3 = createTrueFalse(frame_noinline_modules, "Stage 3", default_val=False)
stage4 = createTrueFalse(frame_noinline_modules, "Stage 4", default_val=False)
stage5 = createTrueFalse(frame_noinline_modules, "Stage 5", default_val=False)
mbox = createTrueFalse(frame_noinline_modules, "Mbox", default_val=False)
mbox_mul = createTrueFalse(frame_noinline_modules, "Mbox Mul", default_val=False)
mbox_div = createTrueFalse(frame_noinline_modules, "Mbox Div", default_val=False)
registerfile = createTrueFalse(frame_noinline_modules, "Register File", default_val=False)
bpu = createTrueFalse(frame_noinline_modules, "BPU", default_val=False)
riscv = createTrueFalse(frame_noinline_modules, "RISC-V", default_val=False)
csrbox = createTrueFalse(frame_noinline_modules, "CSR Box", default_val=False)
scoreboard = createTrueFalse(frame_noinline_modules, "Scoreboard", default_val=False)
bypass = createTrueFalse(frame_noinline_modules, "Bypass", default_val=False)
base_alu = createTrueFalse(frame_noinline_modules, "Base ALU", default_val=False)
decoder = createTrueFalse(frame_noinline_modules, "Decoder", default_val=False)
decompress = createTrueFalse(frame_noinline_modules, "Decompress", default_val=False)
fbox = createTrueFalse(frame_noinline_modules, "FBox", default_val=False)
dtlb = createTrueFalse(frame_noinline_modules, "DTLB", default_val=False)
itlb = createTrueFalse(frame_noinline_modules, "ITLB", default_val=False)

branch_predictor = createWindow(frame_1,
                        'Branch Predictor',
                        'Branch Predictor',
                        infoboxBool=True,
                        heading='Branch Predictor',
                        description=isb_sizes_description)

frame_branch_predictor = createFrame(branch_predictor, side='top', fill='both', pady=(10, 10), padx=(10, 10))

bp_instantiate = createTrueFalse(frame_branch_predictor, "Instantiate", default_val=False)
predictor = createTextEntry(frame_branch_predictor, "Predictor", default_val='gshare', default_fixed=True)
btb_depth = createCounterField(frame_branch_predictor, 'BTB Depth', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
bht_depth = createCounterField(frame_branch_predictor, 'BHT Depth', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
history_len = createCounterField(frame_branch_predictor, 'History Len', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
history_bits = createCounterField(frame_branch_predictor, 'History Bits', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
ras_depth = createCounterField(frame_branch_predictor, 'RAS Depth', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)

frame_2 = createFrame(window, side='left', fill = 'y', padx=(10, 10), pady=(10, 10))

icache_configuration = createWindow(frame_2,
                        'ICache Configuration',
                        'ICache Configuration',
                        infoboxBool=True,
                        heading='ICache Configuration',
                        description=isb_sizes_description)

frame_icache_configuration = createFrame(icache_configuration, side='top', fill='both', pady=(10, 10), padx=(10, 10))

ic_instantiate = createTrueFalse(frame_icache_configuration, "Instantiate", default_val=False, infoboxBool = True, heading = 'num_harts', description = num_harts_description)
sets = createCounterField(frame_icache_configuration, 'Sets', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
word_size = createCounterField(frame_icache_configuration, 'Word Size', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
block_size = createCounterField(frame_icache_configuration, 'Block Size', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
ways = createCounterField(frame_icache_configuration, 'Ways', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
fb_size = createCounterField(frame_icache_configuration, 'FB Size', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)
replacement: createDropDown(frame_icache_configuration, ['PLRU', 'RANDOM', 'RR'], 'Replacement', infoboxBool = True, heading = 'num_harts', description = num_harts_description, )
ecc_enable = createTrueFalse(frame_icache_configuration, "ECC Enable", default_val=False, infoboxBool = True, heading = 'num_harts', description = num_harts_description)
one_hot_select = createTrueFalse(frame_icache_configuration, "Instantiate", default_val=False, infoboxBool = True, heading = 'num_harts', description = num_harts_description)

a_extension = createWindow(frame_2, 'A Extension', 'A Extension', infoboxBool=True, heading='A Extension', description=isb_sizes_description)

frame_a_extension = createFrame(a_extension, side='top', fill='both', pady=(10, 10), padx=(10, 10))
reservation_size = createCounterField(frame_a_extension, 'Reservation Size', infoboxBool = True, heading = 'num_harts', description = num_harts_description, default_val=0)

fd_extension = createWindow(frame_2, 'FD Extension', 'FD Extension', infoboxBool=True, heading='FD Extension', description=isb_sizes_description)

frame_fd_extension = createFrame(fd_extension, side='top', fill='x', pady=(10, 10), padx=(10, 10))

spgma = createWindow(frame_fd_extension, 'SPGMA', 'SPGMA', infoboxBool=True, heading='SPGMA', description=isb_sizes_description)

frame_spgma = createFrame(spgma, side='top', fill='x', pady=(10, 10), padx=(10, 10))

spgma_stage_1 = createFrame(frame_spgma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
spgma_stage_1_label = createLabel(spgma_stage_1, 'Stage 1: ', infoboxBool=True, heading='Stage 1', description=isb_sizes_description, side='left')
spgma_stage_1_mod = createDropDown(spgma_stage_1, ['Pre', 'Pre_mac'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
spgma_stage_1_in = createCounterField(spgma_stage_1, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
spgma_stage_1_out = createCounterField(spgma_stage_1, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

spgma_stage_2 = createFrame(frame_spgma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
spgma_stage_2_label = createLabel(spgma_stage_2, 'Stage 2: ', infoboxBool=True, heading='Stage 2', description=isb_sizes_description, side='left')
spgma_stage_2_mod = createDropDown(spgma_stage_2, ['Mac', 'Mac_post', 'Post', 'Post_round'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
spgma_stage_2_in = createCounterField(spgma_stage_2, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
spgma_stage_2_out = createCounterField(spgma_stage_2, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

spgma_stage_3 = createFrame(frame_spgma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
spgma_stage_3_label = createLabel(spgma_stage_3, 'Stage 3: ', infoboxBool=True, heading='Stage 3', description=isb_sizes_description, side='left')
spgma_stage_3_mod = createDropDown(spgma_stage_3, ['Post', 'Post_round', 'Round', 'None'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
spgma_stage_3_in = createCounterField(spgma_stage_3, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
spgma_stage_3_out = createCounterField(spgma_stage_3, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

spgma_stage_4 = createFrame(frame_spgma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
spgma_stage_4_label = createLabel(spgma_stage_4, 'Stage 4: ', infoboxBool=True, heading='Stage 4', description=isb_sizes_description, side='left')
spgma_stage_4_mod = createDropDown(spgma_stage_4, ['Round', 'None'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
spgma_stage_4_in = createCounterField(spgma_stage_4, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
spgma_stage_4_out = createCounterField(spgma_stage_4, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

dpfma = createWindow(frame_fd_extension, 'DPFMA', 'DPFMA', infoboxBool=True, heading='DPFMA', description=isb_sizes_description)

frame_dpfma = createFrame(dpfma, side='top', fill='x', pady=(10, 10), padx=(10, 10))

dpfma_stage_1 = createFrame(frame_dpfma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
dpfma_stage_1_label = createLabel(dpfma_stage_1, 'Stage 1: ', infoboxBool=True, heading='Stage 1', description=isb_sizes_description, side='left')
dpfma_stage_1_mod = createDropDown(dpfma_stage_1, ['Pre', 'Pre_mac'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
dpfma_stage_1_in = createCounterField(dpfma_stage_1, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
dpfma_stage_1_out = createCounterField(dpfma_stage_1, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

dpfma_stage_2 = createFrame(frame_dpfma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
dpfma_stage_2_label = createLabel(dpfma_stage_2, 'Stage 2: ', infoboxBool=True, heading='Stage 2', description=isb_sizes_description, side='left')
dpfma_stage_2_mod = createDropDown(dpfma_stage_2, ['Mac', 'Mac_post', 'Post', 'Post_round'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
dpfma_stage_2_in = createCounterField(dpfma_stage_2, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
dpfma_stage_2_out = createCounterField(dpfma_stage_2, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

dpfma_stage_3 = createFrame(frame_dpfma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
dpfma_stage_3_label = createLabel(dpfma_stage_3, 'Stage 3: ', infoboxBool=True, heading='Stage 3', description=isb_sizes_description, side='left')
dpfma_stage_3_mod = createDropDown(dpfma_stage_3, ['Post', 'Post_round', 'Round', 'None'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
dpfma_stage_3_in = createCounterField(dpfma_stage_3, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
dpfma_stage_3_out = createCounterField(dpfma_stage_3, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

dpfma_stage_4 = createFrame(frame_dpfma, side='top', fill='x', pady=(0, 0), padx=(0, 0))
dpfma_stage_4_label = createLabel(dpfma_stage_4, 'Stage 4: ', infoboxBool=True, heading='Stage 4', description=isb_sizes_description, side='left')
dpfma_stage_4_mod = createDropDown(dpfma_stage_4, ['Round', 'None'], 'Mod', infoboxBool = True, heading = 'Mod', description = num_harts_description, side='left')
dpfma_stage_4_in = createCounterField(dpfma_stage_4, 'In', infoboxBool = True, heading = 'In', description = num_harts_description, default_val=0, side='left', padx=(10, 0))
dpfma_stage_4_out = createCounterField(dpfma_stage_4, 'Out', infoboxBool = True, heading = 'Out', description = num_harts_description, default_val=0, side='left', padx=(10, 0))

ordering_depth =  createCounterField(frame_fd_extension, 'Ordering Depth', infoboxBool = True, heading = 'Ordering Depth', description = num_harts_description, default_val=0)

asic_params = createWindow(frame_2, 'ASIC Parameters', 'ASIC Parameters', infoboxBool=True, heading='ASIC Parameters', description=isb_sizes_description)

asic_params_frame = createFrame(asic_params, side='top', fill='x', pady=(10, 10), padx=(10, 10))

tech_size = createCounterField(asic_params_frame, 'Tech Size', infoboxBool = True, heading = 'Tech Size', description = num_harts_description, default_val=0)
frequency_mhz = createCounterField(asic_params_frame, 'Frequency (MHz)', infoboxBool = True, heading = 'Frequency (MHz)', description = num_harts_description, default_val=0)

bsc_compile_options = createWindow(frame_2, 'BSC Compile Options', 'BSC Compile Options', infoboxBool=True, heading='BSC Compile Options', description=isb_sizes_description)
bsc_compile_options_frame = createFrame(bsc_compile_options, side='top', fill='x', pady=(10, 10), padx=(10, 10))

test_memory_size = createCounterField(bsc_compile_options_frame, 'Test Memory Size', infoboxBool = True, heading = 'Test Memory Size', description = num_harts_description, default_val=0)
assertions = createTrueFalse(bsc_compile_options_frame, 'Assertions', infoboxBool = True, heading = 'Assertions', description = num_harts_description)
trace_dump = createTrueFalse(bsc_compile_options_frame, 'Trace Dump', infoboxBool = True, heading = 'Trace Dump', description = num_harts_description)
compile_target = createDropDown(bsc_compile_options_frame, ['sim', 'asic', 'fpga'], 'Compile Target', infoboxBool = True, heading = 'Compile Target', description = num_harts_description)
suppress_warnings = createDropDown(bsc_compile_options_frame, ["none", "all", "G0010","T0054","G0020","G0024","G0023","G0096","G0036","G0117","G0015"], 'Suppress Warnings', infoboxBool = True, heading = 'Suppress Warnings', description = num_harts_description)
ovl_assertions = createTrueFalse(bsc_compile_options_frame, 'OVL Assertions', infoboxBool = True, heading = 'OVL Assertions', description = num_harts_description)

bus_protocol = createTextEntry(frame_2, 'Bus Protocol', infoboxBool = True, heading = 'Bus Protocol', description = num_harts_description, default_fixed=True, default_val="AXI4")
reset_pc = createCounterField(frame_2, 'Reset PC', infoboxBool = True, heading = 'Reset PC', description = num_harts_description, default_val=4096)

verilator_configuration = createWindow(frame_2, 'Verilator Configuration', 'Verilator Configuration', infoboxBool=True, heading='Verilator Configuration', description=isb_sizes_description)
verilator_configuration_frame = createFrame(verilator_configuration, side='top', fill='x', pady=(10, 10), padx=(10, 10))

coverage = createDropDown(verilator_configuration_frame, ['none', 'line', 'toggle', 'all'], 'Coverage', infoboxBool = True, heading = 'Coverage', description = num_harts_description)
trace = createTrueFalse(verilator_configuration_frame, 'Trace', infoboxBool = True, heading = 'Trace', description = num_harts_description)
threads = createCounterField(verilator_configuration_frame, 'Threads', infoboxBool = True, heading = 'Threads', description = num_harts_description, default_val=1)
verbosity = createTrueFalse(verilator_configuration_frame, 'Verbosity', infoboxBool = True, heading = 'Verbosity', description = num_harts_description, default_val=True)
out_dir = createTextEntry(verilator_configuration_frame, 'Out Dir', infoboxBool = True, heading = 'Out Dir', description = num_harts_description, default_val="bin")
opt_fast = createTextEntry(verilator_configuration_frame, 'Opt Fast', infoboxBool = True, heading = 'Opt Fast', description = num_harts_description, default_val='-O3')
opt_slow = createTextEntry(verilator_configuration_frame, 'Opt Slow', infoboxBool = True, heading = 'Opt Slow', description = num_harts_description, default_val='-O3')
opt = createTextEntry(verilator_configuration_frame, 'Opt', infoboxBool = True, heading = 'Opt', description = num_harts_description, default_val='-O3')

dcache_configuration = createWindow(frame_2, 'DCache Configuration', 'DCache Configuration', infoboxBool=True, heading='DCache Configuration', description=isb_sizes_description)
dcache_configuration_frame = createFrame(dcache_configuration, side='top', fill='x', pady=(10, 10), padx=(10, 10))
dcache_instantiate = createTrueFalse(dcache_configuration_frame, 'Instantiate', infoboxBool = True, heading = 'DCache Instantiate', description = num_harts_description, default_val=True)
dcache_sets = createCounterField(dcache_configuration_frame, 'Sets', infoboxBool = True, heading = 'DCache Sets', description = num_harts_description, default_val=4)
dcache_word_size = createCounterField(dcache_configuration_frame, 'Word Size', infoboxBool = True, heading = 'DCache Word Size', description = num_harts_description, default_val=8)
dcache_block_size = createCounterField(dcache_configuration_frame, 'Block Size', infoboxBool = True, heading = 'DCache Block Size', description = num_harts_description, default_val=8)
dcache_ways = createCounterField(dcache_configuration_frame, 'Ways', infoboxBool = True, heading = 'DCache Ways', description = num_harts_description, default_val=4)
dcache_fb_size = createCounterField(dcache_configuration_frame, 'FB Size', infoboxBool = True, heading = 'DCache FB Size', description = num_harts_description, default_val=8)
dcache_sb_size = createCounterField(dcache_configuration_frame, 'SB Size', infoboxBool = True, heading = 'DCache SB Size', description = num_harts_description, default_val=2)
dcache_lb_size = createCounterField(dcache_configuration_frame, 'LB Size', infoboxBool = True, heading = 'DCache LB Size', description = num_harts_description, default_val=2)
dcache_ib_size = createCounterField(dcache_configuration_frame, 'IB Size', infoboxBool = True, heading = 'DCache IB Size', description = num_harts_description, default_val=2)
dcache_replacement = createDropDown(dcache_configuration_frame, ["PLRU", "RR", "Random"], 'Replacement', infoboxBool = True, heading = 'DCache Replacement', description = num_harts_description)
dcache_ecc_enable = createTrueFalse(dcache_configuration_frame, 'ECC Enable', infoboxBool = True, heading = 'DCache ECC Enable', description = num_harts_description)
dcache_one_select = createTrueFalse(dcache_configuration_frame, 'One Select', infoboxBool = True, heading = 'DCache One Select', description = num_harts_description)
dcache_rw_ports = createDropDown(dcache_configuration_frame, ['1rw', '1r1w', '2rw'], 'RW Ports', infoboxBool = True, heading = 'DCache RW Ports', description = num_harts_description)

def makeYaml():
    from ruamel import yaml
    values = {'isb_sizes': {'isb_s0s1': int(isb_s0s1.get()),
                            'isb_s1s2': int(isb_s1s2.get()),
                            'isb_s2s3': int(isb_s2s3.get()),
                            'isb_s3s4': int(isb_s3s4.get()),
                            'isb_s4s5': int(isb_s4s5.get()),
                            'isb_cachebuffer': int(isb_cachebuffer.get())}}

    with open('configure.yaml', 'w') as file:
        yaml.dump(values, file)

    # with open("try1.yaml", "r") as stream:
    #     try:
    #         print(yaml.safe_load(stream))
    #     except yaml.YAMLError as exc:
    #         print(exc)

bottom_frame = createFrame(window, side='bottom', fill='x', pady=(10, 10), padx=(10, 10))
ttk.Button(bottom_frame, command = makeYaml, text='Generate Yaml', takefocus=0, style = 'TButton').pack(side = 'right')

run_window()