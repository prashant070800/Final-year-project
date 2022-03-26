apt-get install -y cmake
rm -rf build
mkdir build && cd build
cmake ../
make
sudo make install
