file mkdir C:/Users/avita/source/repos/ofekm5/vivado-sandbox/SimTest/SimTest.srcs/sim_1/new
set_property SOURCE_SET sources_1 [get_filesets sim_1]
close [ open C:/Users/avita/source/repos/ofekm5/vivado-sandbox/SimTest/SimTest.srcs/sim_1/new/CustomTB.vhd w ]
add_files -fileset sim_1 C:/Users/avita/source/repos/ofekm5/vivado-sandbox/SimTest/SimTest.srcs/sim_1/new/CustomTB.vhd
update_compile_order -fileset sim_1