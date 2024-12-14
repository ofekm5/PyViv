#directory must be temp, out-of-project directory that will be deleted afterwards(relevant only to this update)

ipx::edit_ip_in_project -upgrade true -name my_custom_ip_v1_0_project -directory C:/Users/avita/OneDrive/Desktop/Dummy/Dummy.tmp/my_custom_ip_v1_0_project c:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new/component.xml
update_compile_order -fileset sources_1
ipx::edit_ip_in_project -upgrade true -name my_custom_ip_v1_0_project -directory C:/Users/avita/OneDrive/Desktop/Dummy/Dummy.tmp/my_custom_ip_v1_0_project c:/Users/avita/OneDrive/Desktop/Dummy/Dummy.srcs/sources_1/new/component.xml
update_compile_order -fileset sources_1
set_property display_name my_custom_ip_v1_1 [ipx::current_core]
set_property version 1.1 [ipx::current_core]
current_project Dummy
set_property previous_version_for_upgrade xilinx.com:user:my_custom_ip:1.0 [ipx::current_core]
set_property core_revision 1 [ipx::current_core]
ipx::create_xgui_files [ipx::current_core]
ipx::update_checksums [ipx::current_core]
ipx::check_integrity [ipx::current_core]
ipx::save_core [ipx::current_core]
current_project my_custom_ip_v1_0_project
ipx::move_temp_component_back -component [ipx::current_core]
close_project -delete
