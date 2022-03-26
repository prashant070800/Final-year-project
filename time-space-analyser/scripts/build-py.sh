apt-get install -y swig cmake
rm -rf build
mkdir build && cd build
cmake -DBUILD_PY=ON ../
make -j4
sudo make install
sudo make pyinstall
