ipx::infer_core -vendor xilinx.com -library user -taxonomy /UserIP C:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new
ipx::edit_ip_in_project -upgrade true -name Dummy_IP_Proj -directory C:/Users/avita/OneDrive/Desktop/Dummy/Dummy.tmp c:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new/component.xml
ipx::current_core c:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new/component.xml
update_compile_order -fileset sources_1
set_property description {my description} [ipx::current_core]
set_property ipi_drc {ignore_freq_hz false} [ipx::current_core]
set_property ipi_drc {ignore_freq_hz true} [ipx::current_core]
ipx::add_bus_parameter FREQ_TOLERANCE_HZ [ipx::get_bus_interfaces clk -of_objects [ipx::current_core]]
set_property value -1 [ipx::get_bus_parameters FREQ_TOLERANCE_HZ -of_objects [ipx::get_bus_interfaces clk -of_objects [ipx::current_core]]]
set_property core_revision 2 [ipx::current_core]
ipx::update_source_project_archive -component [ipx::current_core]
ipx::create_xgui_files [ipx::current_core]
ipx::update_checksums [ipx::current_core]
ipx::check_integrity [ipx::current_core]
ipx::save_core [ipx::current_core]
ipx::move_temp_component_back -component [ipx::current_core]
close_project -delete
set_property  ip_repo_paths  C:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new [current_project]
update_ip_catalog
update_ip_catalog -rebuild
