cmake_minimum_required(VERSION 3.6)

project(SimpleCam
	DESCRIPTION "A small and documented example application for libcamera"
	LANGUAGES CXX)

set (CMAKE_CXX_STANDARD 17)

set (CMAKE_CXX_FLAGS "-Wall -Winvalid-pch -Wnon-virtual-dtor -Wextra -Werror -Wno-unused-parameter")

find_package(PkgConfig)

pkg_check_modules(LIBCAMERA REQUIRED IMPORTED_TARGET libcamera)
message(STATUS "libcamera library found:")
message(STATUS "    version: ${LIBCAMERA_VERSION}")
message(STATUS "    libraries: ${LIBCAMERA_LINK_LIBRARIES}")
message(STATUS "    include path: ${LIBCAMERA_INCLUDE_DIRS}")

# libevent is used specifically by simple-cam as its event loop.
# Applications may use a different event handling implementation.
pkg_check_modules(LIBEVENT REQUIRED IMPORTED_TARGET libevent_pthreads)
message(STATUS "libevent_pthreads library found:")
message(STATUS "    version: ${LIBEVENT_VERSION}")
message(STATUS "    libraries: ${LIBEVENT_LINK_LIBRARIES}")
message(STATUS "    include path: ${LIBEVENT_INCLUDE_DIRS}")

pkg_check_modules(LIBEVENT REQUIRED IMPORTED_TARGET libpng)
message(STATUS "libpng library found:")
message(STATUS "    version: ${LIBPNG_VERSION}")
message(STATUS "    libraries: ${LIBPNG_LINK_LIBRARIES}")
message(STATUS "    include path: ${LIBPNG_INCLUDE_DIRS}")

include_directories(${CMAKE_SOURCE_DIR} ${LIBCAMERA_INCLUDE_DIRS} ${LIBEVENT_INCLUDE_DIRS} ${LIBPNG_INCLUDE_DIRS})

add_executable(zapis_obrazky camera_module.cpp event_loop.cpp zapis_obrazky.c pngwriter.c)

target_link_libraries(zapis_obrazky PkgConfig::LIBEVENT)
target_link_libraries(zapis_obrazky PkgConfig::LIBCAMERA)
target_link_libraries(zapis_obrazky PkgConfig::LIBPNG)

