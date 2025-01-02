file mkdir C:/Users/avita/OneDrive/Desktop/project_1/project_1.srcs/sources_1/new
# opens the file Node.vhd in write mode, immediately closes it, and ensures the file exists but is empty
close [ open C:/Users/avita/OneDrive/Desktop/project_1/project_1.srcs/sources_1/new/Node.vhd w ]
add_files C:/Users/avita/OneDrive/Desktop/project_1/project_1.srcs/sources_1/new/Node.vhd
update_compile_order -fileset sources_1