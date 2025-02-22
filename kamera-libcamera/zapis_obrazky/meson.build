project('zapis_obrazky', 'c', 'cpp',
	default_options : [
		'werror=true',
		'warning_level=2',
		'cpp_std=c++17',
	])

# simple-cam.cpp is the fully commented application
src_files = files([
	'zapis_obrazky.c',
        'pngwriter.c',
        'camera_module.cpp',
	'event_loop.cpp',
])

# Point your PKG_CONFIG_PATH environment variable to the
# libcamera install path libcamera.pc file ($prefix/lib/pkgconfig/libcamera.pc)
deps = [
      dependency('libcamera', required : true),
      dependency('libevent_pthreads'),
      dependency('libpng'),
]

cpp_arguments = [ '-Wno-unused-parameter', ]

add_project_arguments(cpp_arguments, language : 'cpp')

# simple-cam executable
zapis_obrazky = executable('zapis_obrazky', src_files,
                        dependencies : deps)

