# Conway's Game of Life

Python implementation of Conway's Game of Life.

## Getting started

The basics of this project is pure Python 2.7. If a user wants to see the pretty wx output, then wxpython should also
be installed.

### Prerequisites

To install the dependencies, just run pip with the requirements file.
```
pip install -r requirements.txt
```

## Running the simulation

The project currently has two renderers:
* Text
* wxPython

### Running Text mode
```
python gol\text_renderer.py
```

### Running the wx mode
```
python gol\wx_renderer.py
```

## Running the tests

All unittests are written using Python's unittest framework. To execute the tests, just utilize the setup.py's test
command.
```
C:\Users\Chris\PycharmProjects\gol>python setup.py test
running test
running egg_info
creating gol.egg-info
writing gol.egg-info\PKG-INFO
writing top-level names to gol.egg-info\top_level.txt
writing dependency_links to gol.egg-info\dependency_links.txt
writing manifest file 'gol.egg-info\SOURCES.txt'
reading manifest file 'gol.egg-info\SOURCES.txt'
writing manifest file 'gol.egg-info\SOURCES.txt'
running build_ext
running test
running egg_info
writing gol.egg-info\PKG-INFO
writing top-level names to gol.egg-info\top_level.txt
writing dependency_links to gol.egg-info\dependency_links.txt
reading manifest file 'gol.egg-info\SOURCES.txt'
writing manifest file 'gol.egg-info\SOURCES.txt'
running build_ext
test_can_reference_cell (test_board.BoardTestCase) ... ok
test_cell_can_count_neighbording_dead (test_board.BoardTestCase) ... ok
test_cell_can_count_neighboring_alive (test_board.BoardTestCase) ... ok
test_cell_equivalence (test_board.BoardTestCase) ... ok
test_cell_out_of_bounds_raises (test_board.BoardTestCase) ... ok
test_cell_references_neighbors (test_board.BoardTestCase) ... ok
test_corner_cells_wrap_around (test_board.BoardTestCase) ... ok
test_edge_cells_wrap_around (test_board.BoardTestCase) ... ok
test_any_dead_cell_with_3_neighbors_becomes_alive (test_engine.EngineTestCase) ... ok
test_any_live_cell_with_2_or_3_live_neighbors_lives (test_engine.EngineTestCase) ... ok
test_any_live_cell_with_fewer_than_2_live_neighbors_dies (test_engine.EngineTestCase) ... ok
test_any_live_cell_with_greater_than_3_neighors_dies (test_engine.EngineTestCase) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.015s

OK
```

## Deployment

## Contributing
Feel free! Send me a pull request and I'll take a look as soon as I'm able. This project is mostly a fun project for
myself, but don't let that stop you!

## Authors
* **Chris Evans** - *Initial work* - [menacingChicken](https://github.com/menacingChicken)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments


learning git... just a test...