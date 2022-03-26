# Set the CMake minimum version
cmake_minimum_required(VERSION 3.5)

# Declare the Project version and the Language that the project is written in
project(tsanalyser VERSION 1.0.0 LANGUAGES C)

option(BUILD_PY "Build Python wrappers for the library" OFF)

SET(SRC
	src/tsanalyser.c
	)

# Global Install Directories
include(GNUInstallDirs)

include_directories(include)

add_library(${PROJECT_NAME} SHARED ${SRC})

# Set the properties of the Shared object file that is going to be created
# The line below names the .so file aptly
set_target_properties(${PROJECT_NAME} PROPERTIES
	VERSION ${PROJECT_VERSION}
	SOVERSION 1)

# Add rules to create the binary files
add_executable(tstest tests/test.c)

TARGET_LINK_LIBRARIES(tstest ${PROJECT_NAME})

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "include/tsanalyser/tsanalyser.h")

# Set correct Install directories
install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Config
	ARCHIVE  DESTINATION ${CMAKE_INSTALL_LIBDIR}
	LIBRARY  DESTINATION ${CMAKE_INSTALL_LIBDIR}
	RUNTIME  DESTINATION ${CMAKE_INSTALL_BINDIR}
	PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/tsanalyser)

# Build clean command
add_custom_target(build_clean
	COMMAND rm -rf ./*)

# Uninstall command
add_custom_target(uninstall
	COMMAND xargs rm < install_manifest.txt
	COMMAND rm -rf ${CMAKE_INSTALL_INCLUDEDIR}/tsanalyser)

# Add test cases to test the library
add_custom_target(libtest
	COMMAND echo "Test 1 Start!"
	COMMAND ${CMAKE_CURRENT_BINARY_DIR}/tstest
	COMMAND echo "Test 1 Done!"
	COMMAND echo "Test 2 Start!"
	COMMAND ${CMAKE_CURRENT_BINARY_DIR}/tstest -d
	COMMAND echo "Test 2 Done!"
	)


#############################################################################
# Swig Config
#############################################################################

if(BUILD_PY)
	FIND_PACKAGE(SWIG REQUIRED)
	INCLUDE(${SWIG_USE_FILE})

	FIND_PACKAGE(PythonLibs)
	INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})

	set(CMAKE_SWIG_FLAGS "")

	SET_SOURCE_FILES_PROPERTIES(SOURCE wrappers/tsanalyser.i PROPERTY CPLUSPLUS ON)
	SET_SOURCE_FILES_PROPERTIES(SOURCE wrappers/tsanalyser.i PROPERTY SWIG_FLAGS "-includeall")

	SWIG_ADD_MODULE(tsanalyser python wrappers/tsanalyser.i ${SRC})
	SWIG_LINK_LIBRARIES(tsanalyser ${PYTHON_LIBRARIES})

	SET_TARGET_PROPERTIES(_tsanalyser PROPERTIES OUTPUT_NAME _${PROJECT_NAME})

	set(PYTHON_INSTALL_FILES
		${CMAKE_CURRENT_BINARY_DIR}/tsanalyser.py
		${CMAKE_CURRENT_BINARY_DIR}/_tsanalyser.so)

	# Configure setup.py and copy to output directory
	set(SETUP_PY_IN ${CMAKE_CURRENT_SOURCE_DIR}/wrappers/setup.py.in)
	set(SETUP_PY_OUT ${CMAKE_CURRENT_BINARY_DIR}/setup.py)
	configure_file(${SETUP_PY_IN} ${SETUP_PY_OUT})

	# Install target to call setup.py
	add_custom_target(pyinstall
		DEPENDS _tsanalyser
		COMMAND python ${SETUP_PY_OUT} install
		COMMAND python3 ${SETUP_PY_OUT} install
		)

endif(BUILD_PY)
