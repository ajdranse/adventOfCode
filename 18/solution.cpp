#include <iostream>
#include <map>
#include <vector>

char get_next(std::vector<std::vector<char> >& grid, uint8_t x, uint8_t y) {
    uint8_t nTrees = 0;
    uint8_t nYards = 0;
    for ( int8_t dy = -1; dy <= 1; ++dy ) {
        if ( y + dy < 0 || y + dy >= grid.size() ) {
            continue;
        }
        for ( int8_t dx = -1; dx <= 1; ++dx ) {
            if ( x + dx < 0 || x + dx >= grid[0].size() ) {
                continue;
            }

            char n = grid[y + dy][x + dx];
            if ( n == '|' ) {
                nTrees++;
            } else if ( n == '#' ) {
                nYards++;
            }
        }
    }

    char cur = grid[y][x];
    if ( cur == '.' ) {
        return nTrees >= 3 ? '|' : '.';
    } else if ( cur == '|' ) {
        return nYards >= 3 ? '#' : '|';
    } else { // must be #
        if ( nYards >= 2 && nTrees >= 1 ) {
            return '#';
        } else {
            return '.';
        }
    }
}

std::vector<std::vector<char> > get_next_grid(std::vector<std::vector<char> >& grid) {
    std::vector<std::vector<char> > new_grid(grid.size(), std::vector<char>(grid[0].size(), ' '));
    for ( uint8_t y = 0; y < grid.size(); ++y ) {
        for ( uint8_t x = 0; x < grid[0].size(); ++x ) {
            new_grid[y][x] = get_next(grid, x, y);
        }
    }

    return new_grid;
}

int main() {
    std::vector<std::vector<char> > grid;
    while ( true ) {
        std::string s;
        std::cin >> s;
        if ( s.size() == 0 ) {
            break;
        }
        std::vector<char> row;
        for (auto& c : s) {
            row.push_back(c);
        }
        grid.push_back(row);
    }

    uint8_t nRows = grid.size();
    uint8_t nCols = grid[0].size();

    std::map<std::vector<std::vector<char> >, uint32_t> cache;
    uint32_t end = 1000000000;
    for ( uint32_t i = 1; i <= end; ++i ) {
        grid = get_next_grid(grid);
        if ( cache.count(grid) == 1 ) {
            // cycle!
            uint32_t add = (end - i) / (i - cache[grid]);
            i += add * (i - cache[grid]);
        } else {
            cache[grid] = i;
        }
        if ( i == 10 ) {
            uint32_t trees = 0;
            uint32_t yards = 0;
            for ( uint8_t r = 0; r < nRows; ++r ) {
                for ( uint8_t c = 0; c < nRows; ++c ) {
                    if ( grid[r][c] == '|' ) {
                        trees++;
                    } else if ( grid[r][c] == '#' ) {
                        yards++;
                    }
                }
            }
            std::cerr << "part 1: " << trees << " " << yards << " " << trees * yards << std::endl;
        } else if ( i == end ) {
            uint32_t trees = 0;
            uint32_t yards = 0;
            for ( uint8_t r = 0; r < nRows; ++r ) {
                for ( uint8_t c = 0; c < nRows; ++c ) {
                    if ( grid[r][c] == '|' ) {
                        trees++;
                    } else if ( grid[r][c] == '#' ) {
                        yards++;
                    }
                }
            }
            std::cerr << "part 2: " << trees << " " << yards << " " << trees * yards << std::endl;
        }
    }
}
