cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(normal_distributions_transform)

set(CMAKE_CXX_STANDARD 11)

FIND_PACKAGE(PCL REQUIRED)


FIND_PACKAGE(Boost REQUIRED COMPONENTS thread) # 我的boost版本是1.65.1的




include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})


add_executable(normal_distributions_transform normal_distributions_transform.cpp )
target_link_libraries (normal_distributions_transform ${PCL_LIBRARIES})
include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
add_definitions(-DBOOST_ALL_DYN_LINK)

target_link_libraries(normal_distributions_transform ${Boost_LIBRARIES})


