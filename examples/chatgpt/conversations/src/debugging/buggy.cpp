#include <iostream>
#include <vector>

using Data = std::vector<int>;

void store_data(Data& data, int value) {
    size_t idx = value/data.size();
    data[idx] = value;
}

int main(int argc, char** argv) {
    Data data(10);
    for (int i = -100; i < 100; ++i) {
        store_data(data, i);
    }
    for (const auto& value : data) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
    return 0;
}
